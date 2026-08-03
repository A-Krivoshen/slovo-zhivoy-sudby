#!/usr/bin/env bash
# RU/EN figure src parity for people pages and key diary/album pairs.
# Exit 1 if any pair differs. Used in CI and local QA.
set -euo pipefail
cd "$(dirname "$0")/.."

python3 <<'PY'
from pathlib import Path
import re, sys

def figs(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return set(re.findall(r'figure src="([^"]+)"', path.read_text(encoding="utf-8")))

errors = []

# People by translationKey
en_by_key = {}
for e in Path("content/en/people").glob("*.md"):
    if e.name.startswith("_"):
        continue
    t = e.read_text(encoding="utf-8")
    m = re.search(r'translationKey:\s*"([^"]+)"', t)
    if m:
        en_by_key[m.group(1)] = e

for ru in sorted(Path("content/ru/lyudi").glob("*.md")):
    if ru.name.startswith("_"):
        continue
    t = ru.read_text(encoding="utf-8")
    m = re.search(r'translationKey:\s*"([^"]+)"', t)
    if not m:
        continue
    key = m.group(1)
    en = en_by_key.get(key)
    if not en:
        errors.append(f"no EN people page for {ru.name} key={key}")
        continue
    fr, fe = figs(ru), figs(en)
    if fr != fe:
        errors.append(
            f"people figure mismatch {ru.name} vs {en.name}: "
            f"onlyRU={sorted(fr - fe)} onlyEN={sorted(fe - fr)}"
        )

# Fixed pairs
pairs = [
    ("content/ru/foto/tetrad-semya-prodolzhenie.md", "content/en/photos/notebook-family-continued.md"),
    ("content/ru/foto/samsonov-timofey-petrovich.md", "content/en/photos/samsonov-timofey-petrovich.md"),
    ("content/ru/vospominaniya/dnevnik/00-oblozhka-i-rodoslovnye.md", "content/en/memoirs/diary/00-cover-and-charts.md"),
    ("content/ru/vospominaniya/dnevnik/19-semya-i-deti.md", "content/en/memoirs/diary/18-sons-150-161.md"),
    ("content/ru/hronologiya/_index.md", "content/en/timeline/_index.md"),
]
for a, b in pairs:
    fa, fb = figs(Path(a)), figs(Path(b))
    # chronology pages may have zero figures — still OK if equal
    if fa != fb:
        errors.append(
            f"pair mismatch {a} vs {b}: onlyRU={sorted(fa - fb)} onlyEN={sorted(fb - fa)}"
        )

# Missing static for any figure in content
missing = []
for f in Path("content").rglob("*.md"):
    for src in re.findall(r'figure src="(/[^"]+)"', f.read_text(encoding="utf-8")):
        if not Path("static" + src).exists():
            missing.append(f"{f}: {src}")
if missing:
    errors.append("missing static files:\n  " + "\n  ".join(missing[:40]))

if errors:
    print("FIGURE PARITY CHECK FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("figure parity OK")
PY
