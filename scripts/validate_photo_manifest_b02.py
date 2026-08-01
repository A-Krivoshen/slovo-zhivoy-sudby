#!/usr/bin/env python3
"""Validate archive photo manifest for batch B02."""
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data/archive_photos/batch-2026-08-01-b02.yaml"

def main():
    errors = []
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    ids = set()
    for p in data.get("photos", []):
        pid = p.get("photo_id")
        if not pid:
            errors.append("missing photo_id")
            continue
        if pid in ids:
            errors.append(f"duplicate photo_id {pid}")
        ids.add(pid)
        for key in ("merged_page", "bbox_px", "review_status", "batch_id"):
            if key not in p:
                errors.append(f"{pid}: missing {key}")
        bb = p.get("bbox_px") or {}
        for k in ("x", "y", "w", "h"):
            if k not in bb:
                errors.append(f"{pid}: bbox missing {k}")
            elif bb[k] < 0:
                errors.append(f"{pid}: negative bbox {k}")
        if p.get("review_status") == "publishable" and p.get("privacy_status") in (
            "living_people_review",
            "private",
            "unknown",
            "contains_sensitive_text",
        ):
            errors.append(f"{pid}: publishable with unsafe privacy_status")
        pub = p.get("published_path_ru")
        if pub and pub.startswith("/"):
            web = ROOT / "static" / pub.lstrip("/")
            if not web.exists():
                errors.append(f"{pid}: published file missing {web}")
    print(f"photos: {len(ids)}")
    if errors:
        print("FAIL:")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    print("OK")
    return 0

if __name__ == "__main__":
    main()
