#!/usr/bin/env python3
"""Validate public archive knowledge-graph YAML under data/archive/public/.

Checks:
  - relation subject/object entity_ids resolve in people|events|places|
    letters|documents|photos registries
  - public letters have url_ru
  - no 099–100 entities (withheld privacy pages must not enter the public graph)
  - optional: public:false relations are listed but not treated as public

Prints errors. Exit 0 if clean, 1 if errors (always prints a summary).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    print("error: PyYAML required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "data" / "archive" / "public"

# Primary registries named in the task, plus collections/chapters used by relations.
ENTITY_KEYS = (
    "people",
    "events",
    "places",
    "letters",
    "documents",
    "photos",
    "collections",
    "chapters",
)

BANNED_ID_EXACT = re.compile(
    r"(?:^|[_-])(?:099|100)(?:[_-]|$)|(?:str|page|mp|merged|list)[_-]?(?:099|100)\b",
    re.I,
)


def load_public_yaml() -> dict[str, Any]:
    """Merge all *.yaml / *.yml under data/archive/public/."""
    merged: dict[str, Any] = {k: [] for k in ENTITY_KEYS}
    merged["relations"] = []
    if not PUBLIC.is_dir():
        print(f"warn: missing directory {PUBLIC}")
        return merged

    files = sorted(list(PUBLIC.glob("*.yaml")) + list(PUBLIC.glob("*.yml")))
    if not files:
        print(f"warn: no YAML files in {PUBLIC}")
        return merged

    for path in files:
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except Exception as e:  # noqa: BLE001
            print(f"error: cannot parse {path}: {e}")
            continue
        if not isinstance(data, dict):
            print(f"error: {path.name}: root must be a mapping")
            continue
        for key in ENTITY_KEYS + ("relations",):
            if key not in data:
                continue
            val = data[key]
            if val is None:
                continue
            if not isinstance(val, list):
                print(f"error: {path.name}: '{key}' must be a list")
                continue
            merged[key].extend(val)
    return merged


def entity_id_of(item: Any) -> str | None:
    if not isinstance(item, dict):
        return None
    eid = item.get("entity_id") or item.get("id")
    if eid is None:
        return None
    return str(eid).strip()


def collect_ids(merged: dict[str, Any]) -> dict[str, str]:
    """entity_id -> registry name."""
    ids: dict[str, str] = {}
    for key in ENTITY_KEYS:
        for item in merged.get(key) or []:
            eid = entity_id_of(item)
            if not eid:
                continue
            if eid in ids:
                # duplicate across registries — flag later
                pass
            ids[eid] = key
    return ids


def looks_like_099_100_id(text: str) -> bool:
    """True if text is (or encodes) withheld notebook pages 099–100 as an entity id."""
    t = text.strip()
    if not t:
        return False
    if BANNED_ID_EXACT.search(t):
        return True
    if re.search(r"(?:str|page|list|лист)[_-]?0?99\b", t, re.I):
        return True
    if re.search(r"(?:str|page|list|лист)[_-]?100\b", t, re.I):
        return True
    if re.fullmatch(r"0?99|100", t):
        return True
    return False


def scan_item_for_099_100(item: dict[str, Any], where: str) -> list[str]:
    """Flag entities that *are* pages 099–100, not notes that mention withholding them."""
    errs: list[str] = []
    eid = entity_id_of(item) or ""
    if looks_like_099_100_id(eid):
        errs.append(f"{where}: banned 099–100 entity_id '{eid}'")
    # Positive publication / path fields only (not free-text notes).
    for field in (
        "entity_id",
        "id",
        "url_ru",
        "url_en",
        "path",
        "src",
        "page_scan_src",
        "published_path_ru",
    ):
        if field not in item:
            continue
        val = item[field]
        if isinstance(val, str) and looks_like_099_100_id(val):
            errs.append(f"{where}: banned 099–100 token in {field}={val!r}")
    for field in ("source_pages", "original_page", "merged_page", "source_page"):
        if field not in item:
            continue
        val = item[field]
        pages: list[int] = []
        if isinstance(val, (int, float)):
            pages.append(int(val))
        elif isinstance(val, list):
            for x in val:
                if isinstance(x, (int, float)):
                    pages.append(int(x))
                elif isinstance(x, str) and x.strip().isdigit():
                    pages.append(int(x.strip()))
        elif isinstance(val, str) and val.strip().isdigit():
            pages.append(int(val.strip()))
        for p in pages:
            if p in (99, 100):
                errs.append(f"{where}: banned page {p} in field '{field}'")
    return errs


def main() -> int:
    errors: list[str] = []
    merged = load_public_yaml()
    ids = collect_ids(merged)

    # duplicate entity_ids
    seen: dict[str, str] = {}
    for key in ENTITY_KEYS:
        for item in merged.get(key) or []:
            if not isinstance(item, dict):
                errors.append(f"{key}: non-object entry {item!r}")
                continue
            eid = entity_id_of(item)
            if not eid:
                errors.append(f"{key}: entry missing entity_id: {item!r}")
                continue
            if eid in seen:
                errors.append(
                    f"duplicate entity_id '{eid}' in {key} (also in {seen[eid]})"
                )
            else:
                seen[eid] = key
            errors.extend(scan_item_for_099_100(item, f"{key}/{eid}"))

    # letters must have url_ru
    for item in merged.get("letters") or []:
        if not isinstance(item, dict):
            continue
        eid = entity_id_of(item) or "?"
        url = item.get("url_ru")
        if not url or not str(url).strip():
            errors.append(f"letter '{eid}': missing required url_ru")
        elif not str(url).startswith("/"):
            errors.append(f"letter '{eid}': url_ru should be a site path, got {url!r}")

    # relations
    for i, rel in enumerate(merged.get("relations") or []):
        if not isinstance(rel, dict):
            errors.append(f"relations[{i}]: non-object entry")
            continue
        subj = rel.get("subject") or rel.get("subject_id")
        obj = rel.get("object") or rel.get("object_id")
        pred = rel.get("predicate") or rel.get("rel") or rel.get("type")
        where = f"relations[{i}]"
        if not subj:
            errors.append(f"{where}: missing subject")
        if not obj:
            errors.append(f"{where}: missing object")
        if not pred:
            errors.append(f"{where}: missing predicate")
        if subj and str(subj) not in ids:
            errors.append(
                f"{where}: subject entity_id '{subj}' not in people/events/places/"
                f"letters/documents/photos/collections/chapters"
            )
        if obj and str(obj) not in ids:
            errors.append(
                f"{where}: object entity_id '{obj}' not in people/events/places/"
                f"letters/documents/photos/collections/chapters"
            )
        for side, val in (("subject", subj), ("object", obj)):
            if val and looks_like_099_100_id(str(val)):
                errors.append(f"{where}: banned 099–100 {side} '{val}'")
        # public:false should not be required to resolve for templates, but still
        # validate ids so private stubs cannot smuggle banned pages.
        if rel.get("public") is False:
            # still counted above; note only
            pass

    # summary
    counts = {k: len(merged.get(k) or []) for k in ENTITY_KEYS}
    nrel = len(merged.get("relations") or [])
    print("=== graph integrity ===")
    print(f"registry: {PUBLIC}")
    for k, n in counts.items():
        print(f"  {k}: {n}")
    print(f"  relations: {nrel}")
    print(f"  unique entity_ids: {len(ids)}")
    print()
    if errors:
        print(f"ERRORS: {len(errors)}")
        for e in errors:
            print(f"  - {e}")
        print("FAIL")
        return 1
    print("OK: no integrity errors")
    return 0


if __name__ == "__main__":
    sys.exit(main())
