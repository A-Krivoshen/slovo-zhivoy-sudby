#!/usr/bin/env python3
"""Scan content for /photos/ refs vs static/photos; report orphans and broken links.

Exit 0 by default (summary always printed). Pass --fail to exit 1 when
broken refs or unexpected orphans remain (CI). Privacy-withheld files
str-099, str-100, str-155, str-157 may be unlinked intentionally.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
STATIC_PHOTOS = ROOT / "static" / "photos"

# Paths under /photos/ that may exist on disk but stay unlinked on purpose.
INTENTIONAL_UNLINKED = {
    "dnevnik-tt/str-099.jpg": (
        "privacy: pages 099–100 withheld (UA medal → Timofey Timofeevich, not T.P.)"
    ),
    "dnevnik-tt/str-100.jpg": (
        "privacy: pages 099–100 withheld (UA medal → Timofey Timofeevich, not T.P.)"
    ),
    "dnevnik-tt/str-155.jpg": (
        "privacy: page 155 left unlinked (living-family DOB / internal_privacy)"
    ),
    "dnevnik-tt/str-157.jpg": (
        "privacy: page 157 left unlinked (address / living-family internal_privacy)"
    ),
}

PHOTO_REF_RE = re.compile(
    r"""(?:src|image|href|url)\s*[=:]\s*["'](/photos/[^"'#?]+)["']"""
    r"""|\]\((/photos/[^)#?]+)\)"""
    r"""|["'](/photos/[^"'#?\s]+\.(?:jpg|jpeg|webp|png))["']""",
    re.IGNORECASE,
)
LOOSE_PHOTO_RE = re.compile(r"/photos/[A-Za-z0-9_./-]+\.(?:jpg|jpeg|webp|png)", re.I)
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".webp", ".png"}


def normalize_ref(ref: str) -> str:
    ref = ref.strip()
    if ref.startswith("/photos/"):
        ref = ref[len("/photos/") :]
    return ref.lstrip("/")


def collect_content_refs() -> dict[str, list[str]]:
    """Map normalized path under photos/ -> list of content files that reference it."""
    refs: dict[str, list[str]] = {}
    if not CONTENT.is_dir():
        return refs
    for md in CONTENT.rglob("*.md"):
        try:
            text = md.read_text(encoding="utf-8")
        except OSError as e:
            print(f"warn: cannot read {md}: {e}", file=sys.stderr)
            continue
        found: set[str] = set()
        for m in PHOTO_REF_RE.finditer(text):
            raw = next(g for g in m.groups() if g)
            found.add(normalize_ref(raw))
        for m in LOOSE_PHOTO_RE.finditer(text):
            found.add(normalize_ref(m.group(0)))
        rel = str(md.relative_to(ROOT))
        for r in found:
            refs.setdefault(r, []).append(rel)
    return refs


def collect_static_images() -> set[str]:
    """Relative paths under static/photos for jpg/webp (and jpeg/png)."""
    out: set[str] = set()
    if not STATIC_PHOTOS.is_dir():
        return out
    for p in STATIC_PHOTOS.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix.lower() not in IMAGE_SUFFIXES:
            continue
        out.add(str(p.relative_to(STATIC_PHOTOS)).replace("\\", "/"))
    return out


def base_without_thumb(path: str) -> str:
    """b02-mp001-ph01-thumb.jpg -> b02-mp001-ph01.jpg (same stem family)."""
    p = Path(path)
    stem = p.stem
    if stem.endswith("-thumb"):
        return str(p.with_name(stem[: -len("-thumb")] + p.suffix))
    return path


def is_covered(path: str, referenced: set[str]) -> bool:
    """Image is used if itself, its non-thumb base, or its -thumb sibling is referenced."""
    if path in referenced:
        return True
    base = base_without_thumb(path)
    if base in referenced:
        return True
    # full image referenced via thumb path
    p = Path(path)
    if not p.stem.endswith("-thumb"):
        thumb = str(p.with_name(p.stem + "-thumb" + p.suffix))
        if thumb in referenced:
            return True
    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fail",
        action="store_true",
        help="exit 1 if broken refs or non-intentional orphans exist",
    )
    args = parser.parse_args(argv)

    refs = collect_content_refs()
    referenced = set(refs)
    static = collect_static_images()

    broken: list[tuple[str, list[str]]] = []
    for ref, files in sorted(refs.items()):
        if ref not in static:
            # broken if neither the ref nor a reasonable variant exists
            broken.append((ref, files))

    orphans: list[str] = []
    intentional_orphans: list[tuple[str, str]] = []
    for img in sorted(static):
        if is_covered(img, referenced):
            continue
        if img in INTENTIONAL_UNLINKED:
            intentional_orphans.append((img, INTENTIONAL_UNLINKED[img]))
            continue
        # privacy set may be listed without exact path match variations
        orphans.append(img)

    print("=== orphan image check ===")
    print(f"content refs: {len(referenced)}")
    print(f"static images (jpg/webp/…): {len(static)}")
    print()

    print(f"broken content refs (file missing): {len(broken)}")
    for ref, files in broken:
        print(f"  MISSING  /photos/{ref}")
        for f in files[:5]:
            print(f"           <- {f}")
        if len(files) > 5:
            print(f"           <- … +{len(files) - 5} more")
    print()

    print(f"orphan static images (never referenced): {len(orphans)}")
    for img in orphans:
        print(f"  ORPHAN   /photos/{img}")
    print()

    print(
        f"intentional unlinked (privacy str-099,100,155,157): "
        f"{len(intentional_orphans)}"
    )
    for img, note in intentional_orphans:
        print(f"  OK-UNLINK /photos/{img}")
        print(f"            {note}")
    # Flag if privacy files are missing from static entirely
    for key, note in INTENTIONAL_UNLINKED.items():
        if key not in static:
            print(f"  NOTE     privacy path not on disk: /photos/{key}")
            print(f"            {note}")
    print()

    print("--- summary ---")
    print(f"broken={len(broken)} orphans={len(orphans)} "
          f"intentional_unlinked={len(intentional_orphans)}")

    problems = len(broken) + len(orphans)
    if args.fail and problems:
        print(f"FAIL (--fail): {problems} issue(s)")
        return 1
    print("OK (exit 0; use --fail for CI non-zero on issues)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
