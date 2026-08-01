#!/usr/bin/env python3
"""
Stage A: photo candidate detection for manuscript batch B02.
Auto-detection is assistive only — review_status stays 'candidate'.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import cv2
import numpy as np
import yaml
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
BATCH = ROOT / "inbox/scans/memoirs/batch_b02"
MASTERS = BATCH / "masters"
OVERLAYS = BATCH / "overlays"
PREVIEWS = BATCH / "page_previews"
CAND_DIR = BATCH / "candidates"
CONTACT = BATCH / "contact_sheets"
REPORTS = BATCH / "reports"


def load_bgr(path: Path) -> np.ndarray:
    rgb = np.array(Image.open(path).convert("RGB"))
    return cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)


def expand_bbox(x, y, w, h, iw, ih, pad_frac=0.03):
    pad_x = max(6, int(w * pad_frac))
    pad_y = max(6, int(h * pad_frac))
    x0 = max(0, x - pad_x)
    y0 = max(0, y - pad_y)
    x1 = min(iw, x + w + pad_x)
    y1 = min(ih, y + h + pad_y)
    return x0, y0, x1 - x0, y1 - y0


def iou(a, b) -> float:
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    x0, y0 = max(ax, bx), max(ay, by)
    x1, y1 = min(ax + aw, bx + bw), min(ay + ah, by + bh)
    inter = max(0, x1 - x0) * max(0, y1 - y0)
    if inter <= 0:
        return 0.0
    union = aw * ah + bw * bh - inter
    return inter / union if union else 0.0


def nms(boxes, scores, thr=0.4):
    order = sorted(range(len(boxes)), key=lambda i: scores[i], reverse=True)
    keep = []
    while order:
        i = order.pop(0)
        keep.append(i)
        order = [j for j in order if iou(boxes[i], boxes[j]) < thr]
    return keep


def split_vertical_stack(mask, x, y, bw, bh, page_area, sh):
    """If tall multi-photo stack, split on horizontal valleys."""
    if bh < sh * 0.4:
        return [(x, y, bw, bh)]
    strip = mask[y : y + bh, x : x + bw]
    row = strip.mean(axis=1)
    mid0, mid1 = int(bh * 0.2), int(bh * 0.8)
    if mid1 <= mid0 + 10:
        return [(x, y, bw, bh)]
    thr_r = float(row[mid0:mid1].mean()) * 0.5
    # find all local valleys
    valleys = []
    for i in range(mid0 + 5, mid1 - 5):
        if row[i] < thr_r and row[i] <= row[i - 3] and row[i] <= row[i + 3]:
            valleys.append(i)
    if not valleys:
        # single best valley
        best_i = mid0 + int(np.argmin(row[mid0:mid1]))
        if row[best_i] < thr_r:
            valleys = [best_i]
    if not valleys:
        return [(x, y, bw, bh)]
    # merge nearby valleys
    valleys = sorted(valleys)
    merged = [valleys[0]]
    for v in valleys[1:]:
        if v - merged[-1] > bh * 0.12:
            merged.append(v)
    cuts = [0] + merged + [bh]
    parts = []
    for a, b in zip(cuts, cuts[1:]):
        hh = b - a
        if hh * bw < page_area * 0.02:
            continue
        if hh < sh * 0.06:
            continue
        parts.append((x, y + a, bw, hh))
    return parts if parts else [(x, y, bw, bh)]


def split_side_by_side(mask, x, y, bw, bh, page_area, sw):
    """Split wide dual photos side by side."""
    if bw < sw * 0.45 or bh > bw * 1.2:
        return [(x, y, bw, bh)]
    strip = mask[y : y + bh, x : x + bw]
    col = strip.mean(axis=0)
    mid0, mid1 = int(bw * 0.3), int(bw * 0.7)
    if mid1 <= mid0:
        return [(x, y, bw, bh)]
    best_i = mid0 + int(np.argmin(col[mid0:mid1]))
    thr = float(col[mid0:mid1].mean()) * 0.55
    if col[best_i] > thr:
        return [(x, y, bw, bh)]
    left_w, right_w = best_i, bw - best_i
    if left_w * bh < page_area * 0.02 or right_w * bh < page_area * 0.02:
        return [(x, y, bw, bh)]
    return [(x, y, left_w, bh), (x + best_i, y, right_w, bh)]


def detect_candidates(bgr: np.ndarray) -> list[tuple[tuple[int, int, int, int], float]]:
    h, w = bgr.shape[:2]
    scale = min(1.0, 1200.0 / max(h, w))
    sw, sh = int(w * scale), int(h * scale)
    small = cv2.resize(bgr, (sw, sh), interpolation=cv2.INTER_AREA)
    gs = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)

    margin = max(8, int(min(sw, sh) * 0.025))
    border = np.concatenate(
        [
            small[:margin, :, :].reshape(-1, 3),
            small[-margin:, :, :].reshape(-1, 3),
            small[:, :margin, :].reshape(-1, 3),
            small[:, -margin:, :].reshape(-1, 3),
        ]
    )
    paper = np.median(border, axis=0).astype(np.float32)
    diff = np.linalg.norm(small.astype(np.float32) - paper, axis=2)
    diff_u8 = cv2.normalize(diff, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    thr = max(40, int(np.percentile(diff_u8, 62)))
    _, mask = cv2.threshold(diff_u8, thr, 255, cv2.THRESH_BINARY)
    _, dark = cv2.threshold(gs, int(np.percentile(gs, 35)), 255, cv2.THRESH_BINARY_INV)
    core = cv2.bitwise_and(mask, dark)
    strong_thr = max(thr + 20, int(np.percentile(diff_u8, 75)))
    _, strong = cv2.threshold(diff_u8, strong_thr, 255, cv2.THRESH_BINARY)
    core = cv2.bitwise_or(core, strong)

    k = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    k_open = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    core = cv2.morphologyEx(core, cv2.MORPH_CLOSE, k, iterations=2)
    core = cv2.morphologyEx(core, cv2.MORPH_OPEN, k, iterations=1)
    core = cv2.morphologyEx(core, cv2.MORPH_OPEN, k_open, iterations=1)

    page_area = sh * sw
    min_area = int(page_area * 0.02)
    max_area = int(page_area * 0.72)

    contours, _ = cv2.findContours(core, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    raw = []
    for cnt in contours:
        x, y, bw, bh = cv2.boundingRect(cnt)
        area = bw * bh
        if area < min_area or area > max_area:
            continue
        ar = bw / max(bh, 1)
        if ar > 5.5 or ar < 0.15:
            continue
        if bh < sh * 0.07 and bw > sw * 0.65:
            continue  # text band
        fill = float(np.count_nonzero(core[y : y + bh, x : x + bw])) / max(area, 1)
        if fill < 0.12:
            continue
        roi_g = gs[y : y + bh, x : x + bw]
        contrast = float(np.std(roi_g))
        mean_l = float(np.mean(roi_g))
        if mean_l > 215 and contrast < 22:
            continue
        # split stacks / pairs
        parts = split_vertical_stack(core, x, y, bw, bh, page_area, sh)
        refined = []
        for p in parts:
            refined.extend(split_side_by_side(core, *p, page_area, sw))
        for px, py, pbw, pbh in refined:
            if pbw * pbh < min_area:
                continue
            score = (
                min(contrast / 70.0, 1.0) * 0.4
                + fill * 0.25
                + min((pbw * pbh) / (page_area * 0.2), 1.0) * 0.25
                + (0.1 if mean_l < 150 else 0.0)
            )
            raw.append(((px, py, pbw, pbh), score))

    if not raw:
        return []

    boxes = [r[0] for r in raw]
    scores = [r[1] for r in raw]
    keep = nms(boxes, scores, thr=0.4)
    pairs = [(boxes[i], scores[i]) for i in keep]
    pairs = sorted(pairs, key=lambda p: (p[0][1] // 80, p[0][0]))
    pairs = [p for p in pairs if p[1] >= 0.22][:12]

    inv = 1.0 / scale
    out = []
    for (x, y, bw, bh), score in pairs:
        X, Y, BW, BH = int(x * inv), int(y * inv), int(bw * inv), int(bh * inv)
        X, Y, BW, BH = expand_bbox(X, Y, BW, BH, w, h, pad_frac=0.03)
        out.append(((X, Y, BW, BH), score))
    return out


def draw_overlay(bgr: np.ndarray, cands: list[dict], label: str) -> np.ndarray:
    vis = bgr.copy()
    colors = [
        (0, 180, 255),
        (0, 255, 128),
        (255, 128, 0),
        (255, 0, 200),
        (80, 80, 255),
        (255, 255, 0),
        (0, 255, 255),
        (180, 0, 255),
    ]
    for i, c in enumerate(cands):
        x, y, ww, hh = (
            c["bbox_px"]["x"],
            c["bbox_px"]["y"],
            c["bbox_px"]["w"],
            c["bbox_px"]["h"],
        )
        color = colors[i % len(colors)]
        overlay = vis.copy()
        cv2.rectangle(overlay, (x, y), (x + ww, y + hh), color, -1)
        vis = cv2.addWeighted(overlay, 0.16, vis, 0.84, 0)
        cv2.rectangle(vis, (x, y), (x + ww, y + hh), color, 5)
        cv2.putText(
            vis,
            c["photo_id_stub"],
            (x + 10, y + 48),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.5,
            color,
            3,
            cv2.LINE_AA,
        )
    cv2.putText(
        vis, label, (24, 48), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (20, 20, 220), 3, cv2.LINE_AA
    )
    return vis


def make_contact_sheet(paths_labels: list[tuple[Path, str]], out: Path, cols=6):
    thumbs = []
    for p, lab in paths_labels:
        if not p.exists():
            continue
        im = Image.open(p).convert("RGB")
        im.thumbnail((280, 400))
        canvas = Image.new("RGB", (im.width, im.height + 28), (245, 245, 245))
        canvas.paste(im, (0, 0))
        d = ImageDraw.Draw(canvas)
        d.text((4, im.height + 6), lab[:40], fill=(20, 20, 20))
        thumbs.append(canvas)
    if not thumbs:
        return
    cols = min(cols, len(thumbs))
    rows = math.ceil(len(thumbs) / cols)
    cell_w = max(t.width for t in thumbs)
    cell_h = max(t.height for t in thumbs)
    sheet = Image.new("RGB", (cols * cell_w + 8, rows * cell_h + 8), (255, 255, 255))
    for i, t in enumerate(thumbs):
        r, c = divmod(i, cols)
        sheet.paste(t, (4 + c * cell_w, 4 + r * cell_h))
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, quality=85)


def process_page(page_num: int) -> dict:
    name = f"m-{page_num:03d}.jpg"
    path = MASTERS / name
    bgr = load_bgr(path)
    h, w = bgr.shape[:2]
    pairs = detect_candidates(bgr)

    cands = []
    for i, ((x, y, bw, bh), score) in enumerate(pairs, 1):
        cands.append(
            {
                "photo_index_on_page": i,
                "photo_id_stub": f"ph{i:02d}",
                "photo_id": f"b02-mp{page_num:03d}-ph{i:02d}",
                "bbox_px": {"x": int(x), "y": int(y), "w": int(bw), "h": int(bh)},
                "auto_score": round(float(score), 3),
                "review_status": "candidate",
                "object_type": "uncertain",
                "detection": "auto_v3_paper_distance",
            }
        )

    OVERLAYS.mkdir(parents=True, exist_ok=True)
    PREVIEWS.mkdir(parents=True, exist_ok=True)
    label = f"m-{page_num:03d} | candidates: {len(cands)}"
    ov = draw_overlay(bgr, cands, label)
    ov_path = OVERLAYS / f"m-{page_num:03d}-overlay.jpg"
    prev_path = PREVIEWS / f"m-{page_num:03d}.jpg"
    scale = 1100 / max(h, w)
    nh, nw = int(h * scale), int(w * scale)
    ov_s = cv2.resize(ov, (nw, nh), interpolation=cv2.INTER_AREA)
    page_s = cv2.resize(bgr, (nw, nh), interpolation=cv2.INTER_AREA)
    Image.fromarray(cv2.cvtColor(ov_s, cv2.COLOR_BGR2RGB)).save(
        ov_path, quality=85, optimize=True
    )
    Image.fromarray(cv2.cvtColor(page_s, cv2.COLOR_BGR2RGB)).save(
        prev_path, quality=85, optimize=True
    )

    CAND_DIR.mkdir(parents=True, exist_ok=True)
    for c in cands:
        x, y, bw, bh = (
            c["bbox_px"]["x"],
            c["bbox_px"]["y"],
            c["bbox_px"]["w"],
            c["bbox_px"]["h"],
        )
        crop = bgr[y : y + bh, x : x + bw]
        tpath = CAND_DIR / f"m-{page_num:03d}-{c['photo_id_stub']}.jpg"
        ch, cw = crop.shape[:2]
        sc = 700 / max(ch, cw, 1)
        if sc < 1:
            crop_s = cv2.resize(
                crop, (int(cw * sc), int(ch * sc)), interpolation=cv2.INTER_AREA
            )
        else:
            crop_s = crop
        Image.fromarray(cv2.cvtColor(crop_s, cv2.COLOR_BGR2RGB)).save(
            tpath, quality=90, optimize=True
        )
        c["preview_path"] = str(tpath.relative_to(ROOT))

    return {
        "merged_page": page_num,
        "source_image": str(path.relative_to(ROOT)),
        "page_dimensions_px": {"w": w, "h": h},
        "dpi": 300,
        "page_rotation": 0,
        "candidate_count": len(cands),
        "candidates": cands,
        "overlay_path": str(ov_path.relative_to(ROOT)),
        "preview_path": str(prev_path.relative_to(ROOT)),
        "has_photo_candidates": len(cands) > 0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="start", type=int, default=1)
    ap.add_argument("--to", dest="end", type=int, default=82)
    args = ap.parse_args()

    REPORTS.mkdir(parents=True, exist_ok=True)
    CONTACT.mkdir(parents=True, exist_ok=True)
    pages = []
    all_thumbs = []
    for n in range(args.start, args.end + 1):
        rec = process_page(n)
        pages.append(rec)
        for c in rec["candidates"]:
            all_thumbs.append((ROOT / c["preview_path"], c["photo_id"]))
        print(f"m-{n:03d}: {rec['candidate_count']} candidates")

    inv = {
        "batch_id": "manuscript-2026-08-01-b02",
        "source_pdf": "inbox/scans/memoirs/_raw/samsonovy_new_scans_2026-08-01_corrected.pdf",
        "sha256": "66f69122cc6e0adac3083fb1c3b2833db8a85c9d5952c692f125188f114d424d",
        "extraction": "pdfimages -j (native JPEG 2480x3507 @ 300 DPI); load via PIL",
        "detection_note": "Auto v3 candidates only; nothing approved. Visual review required.",
        "pages": pages,
        "totals": {
            "pages": len(pages),
            "pages_with_candidates": sum(1 for p in pages if p["candidate_count"]),
            "candidates": sum(p["candidate_count"] for p in pages),
        },
    }
    inv_path = REPORTS / "photo_candidates_inventory.yaml"
    with open(inv_path, "w", encoding="utf-8") as f:
        yaml.dump(inv, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    with open(REPORTS / "photo_candidates_inventory.json", "w", encoding="utf-8") as f:
        json.dump(inv, f, ensure_ascii=False, indent=2)

    for i in range(0, len(all_thumbs), 36):
        chunk = all_thumbs[i : i + 36]
        make_contact_sheet(chunk, CONTACT / f"contact_{i // 36 + 1:02d}.jpg", cols=6)

    ov_paths = sorted(OVERLAYS.glob("m-*-overlay.jpg"))
    make_contact_sheet(
        [(p, p.stem.replace("-overlay", "")) for p in ov_paths],
        CONTACT / "all_page_overlays.jpg",
        cols=8,
    )
    prev_paths = sorted(PREVIEWS.glob("m-*.jpg"))
    make_contact_sheet(
        [(p, p.stem) for p in prev_paths],
        CONTACT / "all_page_previews.jpg",
        cols=8,
    )
    print("TOTALS:", inv["totals"])
    print("Wrote", inv_path)


if __name__ == "__main__":
    main()
