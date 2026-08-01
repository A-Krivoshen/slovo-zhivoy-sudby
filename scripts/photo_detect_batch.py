#!/usr/bin/env python3
"""
Generic Stage-A photo candidate detection for manuscript batches B01/B02.
Auto-detection is assistive only — review_status stays 'candidate'.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import cv2
import numpy as np
import yaml
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]

# Reuse detector core from b02 script if available
sys.path.insert(0, str(ROOT / "scripts"))
from photo_detect_b02 import (  # noqa: E402
    detect_candidates,
    draw_overlay,
    load_bgr,
    make_contact_sheet,
)


def corrected_to_original(corrected: int) -> int | None:
    """Control PDF B01: c 001–067 → op 001–067; c 068–078 → op 069–079."""
    if 1 <= corrected <= 67:
        return corrected
    if 68 <= corrected <= 78:
        return corrected + 1
    return None


def process_page(
    page_num: int,
    master_path: Path,
    overlays: Path,
    previews: Path,
    cand_dir: Path,
    photo_id_prefix: str,
    page_label: str,
) -> dict:
    bgr = load_bgr(master_path)
    h, w = bgr.shape[:2]
    pairs = detect_candidates(bgr)
    cands = []
    for i, ((x, y, bw, bh), score) in enumerate(pairs, 1):
        stub = f"ph{i:02d}"
        pid = f"{photo_id_prefix}-ph{stub[-2:]}" if False else f"{photo_id_prefix}-ph{i:02d}"
        cands.append(
            {
                "photo_index_on_page": i,
                "photo_id_stub": stub,
                "photo_id": f"{photo_id_prefix}-ph{i:02d}",
                "bbox_px": {"x": int(x), "y": int(y), "w": int(bw), "h": int(bh)},
                "auto_score": round(float(score), 3),
                "review_status": "candidate",
                "object_type": "uncertain",
                "detection": "auto_v3_paper_distance",
            }
        )

    overlays.mkdir(parents=True, exist_ok=True)
    previews.mkdir(parents=True, exist_ok=True)
    label = f"{page_label} | candidates: {len(cands)}"
    ov = draw_overlay(bgr, cands, label)
    ov_path = overlays / f"{page_label}-overlay.jpg"
    prev_path = previews / f"{page_label}.jpg"
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

    cand_dir.mkdir(parents=True, exist_ok=True)
    for c in cands:
        x, y, bw, bh = (
            c["bbox_px"]["x"],
            c["bbox_px"]["y"],
            c["bbox_px"]["w"],
            c["bbox_px"]["h"],
        )
        crop = bgr[y : y + bh, x : x + bw]
        tpath = cand_dir / f"{page_label}-{c['photo_id_stub']}.jpg"
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
        "page_label": page_label,
        "page_num": page_num,
        "source_image": str(master_path.relative_to(ROOT)),
        "page_dimensions_px": {"w": w, "h": h},
        "dpi": 300,
        "page_rotation": 0,
        "candidate_count": len(cands),
        "candidates": cands,
        "overlay_path": str(ov_path.relative_to(ROOT)),
        "preview_path": str(prev_path.relative_to(ROOT)),
        "has_photo_candidates": len(cands) > 0,
    }


def run_b01(start: int, end: int) -> dict:
    batch = ROOT / "inbox/scans/memoirs/batch_b01"
    masters = batch / "masters"
    pages = []
    thumbs = []
    for c in range(start, end + 1):
        path = masters / f"c-{c:03d}.jpg"
        if not path.exists():
            print("missing", path)
            continue
        op = corrected_to_original(c)
        label = f"c-{c:03d}"
        prefix = f"b01-c{c:03d}"
        rec = process_page(
            c,
            path,
            batch / "overlays",
            batch / "page_previews",
            batch / "candidates",
            prefix,
            label,
        )
        rec["corrected_page"] = c
        rec["original_page"] = op
        rec["batch_id"] = "manuscript-b01"
        pages.append(rec)
        for cand in rec["candidates"]:
            thumbs.append((ROOT / cand["preview_path"], cand["photo_id"]))
        print(f"{label} (op {op}): {rec['candidate_count']} candidates")
    return pages, thumbs


def run_b02(start: int, end: int) -> dict:
    batch = ROOT / "inbox/scans/memoirs/batch_b02"
    masters = batch / "masters"
    pages = []
    thumbs = []
    for m in range(start, end + 1):
        path = masters / f"m-{m:03d}.jpg"
        if not path.exists():
            print("missing", path)
            continue
        label = f"m-{m:03d}"
        prefix = f"b02-mp{m:03d}"
        rec = process_page(
            m,
            path,
            batch / "overlays",
            batch / "page_previews",
            batch / "candidates",
            prefix,
            label,
        )
        rec["merged_page"] = m
        rec["original_page_proposed"] = 79 + m  # preliminary 080–161
        rec["batch_id"] = "manuscript-b02"
        pages.append(rec)
        for cand in rec["candidates"]:
            thumbs.append((ROOT / cand["preview_path"], cand["photo_id"]))
        print(f"{label}: {rec['candidate_count']} candidates")
    return pages, thumbs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", choices=["b01", "b02"], required=True)
    ap.add_argument("--from", dest="start", type=int, default=1)
    ap.add_argument("--to", dest="end", type=int, default=None)
    args = ap.parse_args()

    if args.batch == "b01":
        end = args.end or 78
        pages, thumbs = run_b01(args.start, end)
        batch_dir = ROOT / "inbox/scans/memoirs/batch_b01"
        inv = {
            "batch_id": "manuscript-b01",
            "source_pdf": "inbox/scans/memoirs/_raw/nasha_rodoslovnaya_samsonovy_corrected.pdf",
            "sha256": "99d859f158eaece09502b25e0082a9d8ca1294441312fb6978b64fac311a75c9",
            "pages_in_pdf": 78,
            "original_page_range_note": "corrected 001–067=op001–067; corrected 068–078=op069–079; op068 absent (dup of 067@180)",
            "extraction": "pdfimages -j native JPEG 2480x3507 @ 300 DPI",
            "detection_note": "Auto candidates only; nothing approved.",
            "pages": pages,
            "totals": {
                "pages": len(pages),
                "pages_with_candidates": sum(1 for p in pages if p["candidate_count"]),
                "candidates": sum(p["candidate_count"] for p in pages),
            },
        }
    else:
        end = args.end or 82
        pages, thumbs = run_b02(args.start, end)
        batch_dir = ROOT / "inbox/scans/memoirs/batch_b02"
        inv = {
            "batch_id": "manuscript-b02",
            "source_pdf": "inbox/scans/memoirs/_raw/samsonovy_new_scans_2026-08-01_corrected.pdf",
            "sha256": "66f69122cc6e0adac3083fb1c3b2833db8a85c9d5952c692f125188f114d424d",
            "pages_in_pdf": 82,
            "original_page_range_note": "proposed op 080–161 PRELIMINARY",
            "extraction": "pdfimages -j native JPEG 2480x3507 @ 300 DPI",
            "detection_note": "Auto candidates only; nothing approved.",
            "pages": pages,
            "totals": {
                "pages": len(pages),
                "pages_with_candidates": sum(1 for p in pages if p["candidate_count"]),
                "candidates": sum(p["candidate_count"] for p in pages),
            },
        }

    reports = batch_dir / "reports"
    contact = batch_dir / "contact_sheets"
    reports.mkdir(parents=True, exist_ok=True)
    contact.mkdir(parents=True, exist_ok=True)
    inv_path = reports / "photo_candidates_inventory.yaml"
    with open(inv_path, "w", encoding="utf-8") as f:
        yaml.dump(inv, f, allow_unicode=True, sort_keys=False)
    with open(reports / "photo_candidates_inventory.json", "w", encoding="utf-8") as f:
        json.dump(inv, f, ensure_ascii=False, indent=2)
    for i in range(0, len(thumbs), 36):
        make_contact_sheet(
            thumbs[i : i + 36], contact / f"contact_{i // 36 + 1:02d}.jpg", cols=6
        )
    print("TOTALS:", inv["totals"])
    print("Wrote", inv_path)


if __name__ == "__main__":
    main()
