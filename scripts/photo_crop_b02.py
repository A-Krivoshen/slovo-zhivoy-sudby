#!/usr/bin/env python3
"""
Crop image_only / context / page_overview from reviewed bboxes.
Masters stay under inbox (gitignored). Web view crops optional.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BATCH = ROOT / "inbox/scans/memoirs/batch_b02"
MASTERS = BATCH / "masters"
CROPS = BATCH / "crops"
OVERVIEW = BATCH / "page_overview"


def crop_one(page: int, photo_id: str, bbox: dict, context_bbox: dict | None, pad_extra=0):
    master = MASTERS / f"m-{page:03d}.jpg"
    im = Image.open(master).convert("RGB")
    W, H = im.size
    x, y, w, h = bbox["x"], bbox["y"], bbox["w"], bbox["h"]
    if pad_extra:
        x = max(0, x - pad_extra)
        y = max(0, y - pad_extra)
        w = min(W - x, w + 2 * pad_extra)
        h = min(H - y, h + 2 * pad_extra)
    image_only = im.crop((x, y, x + w, y + h))

    CROPS.mkdir(parents=True, exist_ok=True)
    master_dir = CROPS / "master"
    view_dir = CROPS / "view"
    ctx_dir = CROPS / "context"
    master_dir.mkdir(exist_ok=True)
    view_dir.mkdir(exist_ok=True)
    ctx_dir.mkdir(exist_ok=True)

    # archival master: PNG lossless
    master_path = master_dir / f"{photo_id}-master.png"
    image_only.save(master_path)

    # view JPEG q=92, long edge max 2400 no upscale
    view = image_only.copy()
    max_edge = 2400
    if max(view.size) > max_edge:
        view.thumbnail((max_edge, max_edge), Image.Resampling.LANCZOS)
    view_path = view_dir / f"{photo_id}-view.jpg"
    view.save(view_path, quality=92, optimize=True)

    context_path = None
    if context_bbox:
        cx, cy, cw, ch = (
            context_bbox["x"],
            context_bbox["y"],
            context_bbox["w"],
            context_bbox["h"],
        )
        ctx = im.crop((cx, cy, cx + cw, cy + ch))
        if max(ctx.size) > max_edge:
            ctx.thumbnail((max_edge, max_edge), Image.Resampling.LANCZOS)
        context_path = ctx_dir / f"{photo_id}-context.jpg"
        ctx.save(context_path, quality=92, optimize=True)

    return {
        "crop_master_path": str(master_path.relative_to(ROOT)),
        "crop_view_path": str(view_path.relative_to(ROOT)),
        "context_crop_path": str(context_path.relative_to(ROOT)) if context_path else None,
        "image_only_px": {"w": image_only.size[0], "h": image_only.size[1]},
    }


def page_overview(page: int, max_edge=1200):
    master = MASTERS / f"m-{page:03d}.jpg"
    im = Image.open(master).convert("RGB")
    OVERVIEW.mkdir(parents=True, exist_ok=True)
    ov = im.copy()
    ov.thumbnail((max_edge, max_edge), Image.Resampling.LANCZOS)
    path = OVERVIEW / f"m-{page:03d}-overview.jpg"
    ov.save(path, quality=85, optimize=True)
    return str(path.relative_to(ROOT))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--review",
        default=str(BATCH / "reports/photo_review_verified.yaml"),
        help="YAML with verified photos list",
    )
    args = ap.parse_args()
    review_path = Path(args.review)
    if not review_path.exists():
        print("No review file:", review_path)
        return
    data = yaml.safe_load(review_path.read_text(encoding="utf-8"))
    results = []
    pages_seen = set()
    for item in data.get("photos", []):
        if item.get("review_status") not in (
            "visually_verified",
            "manually_adjusted",
            "publishable",
        ):
            continue
        page = int(item["merged_page"])
        photo_id = item["photo_id"]
        paths = crop_one(page, photo_id, item["bbox_px"], item.get("context_bbox_px"))
        if page not in pages_seen:
            ov = page_overview(page)
            pages_seen.add(page)
        else:
            ov = str((OVERVIEW / f"m-{page:03d}-overview.jpg").relative_to(ROOT))
        item = {**item, **paths, "page_overview_path": ov}
        results.append(item)
        print("cropped", photo_id)

    out = {
        "batch_id": data.get("batch_id", "manuscript-2026-08-01-b02"),
        "photos": results,
        "count": len(results),
    }
    out_path = BATCH / "reports/photo_crops_done.yaml"
    out_path.write_text(
        yaml.dump(out, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )
    print("Wrote", out_path, "count", len(results))


if __name__ == "__main__":
    main()
