#!/usr/bin/env python3
"""Generate pure SVG assets for the repository README.

Deterministic, no network, no remote fonts.
Run: python3 scripts/generate_readme_assets.py
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "readme"

# Site tokens from assets/css/extended/archive.css (light)
PAPER = "#f3efe6"
PAPER_CARD = "#faf7f0"
INK = "#1c1915"
INK_BODY = "#2a2620"
MUTED = "#5c564c"
ACCENT = "#7a6548"
LINE = "#d0c6b6"
RULE = "#2e2a24"

FONT_UI = (
    "-apple-system, BlinkMacSystemFont, 'Segoe UI', "
    "system-ui, sans-serif"
)
FONT_SERIF = "Georgia, 'Times New Roman', 'Noto Serif', serif"
FONT_MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"


def write(name: str, svg: str) -> None:
    path = OUT / name
    path.write_text(svg.strip() + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} ({path.stat().st_size} bytes)")


def hero() -> str:
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="400" viewBox="0 0 1200 400"
     role="img" aria-labelledby="heroTitle heroDesc">
  <title id="heroTitle">Слово Живой Судьбы — семейный архив</title>
  <desc id="heroDesc">Открытый двуязычный сайт мемуаров Кривошеиной Татьяны Тимофеевны: воспоминания, родители, фото и документы. сжс.рф</desc>

  <rect width="1200" height="400" rx="4" fill="{PAPER}"/>
  <rect x="48" y="36" width="3" height="328" fill="{RULE}"/>

  <g font-family="{FONT_UI}" fill="{ACCENT}">
    <text x="80" y="72" font-size="18" letter-spacing="4">СЕМЕЙНЫЙ АРХИВ · ТЕТРАДЬ</text>
  </g>

  <g font-family="{FONT_SERIF}" fill="{INK}">
    <text x="80" y="148" font-size="52" font-weight="700">Слово Живой Судьбы</text>
    <text x="80" y="196" font-size="26" fill="{MUTED}">Мемуары Татьяны Тимофеевны Кривошеиной</text>
  </g>

  <g font-family="{FONT_UI}" fill="{INK_BODY}">
    <text x="80" y="250" font-size="20">Открытый сайт семьи: рукописи, письма, фото</text>
    <text x="80" y="278" font-size="20">и документы — по-русски и по-английски.</text>
  </g>

  <g font-family="{FONT_MONO}" fill="{MUTED}" font-size="18">
    <text x="80" y="336">сжс.рф</text>
    <text x="200" y="336">RU · EN</text>
    <text x="320" y="336">Hugo</text>
  </g>

  <!-- folio stack: real site sections -->
  <g id="folios" transform="translate(720 56)">
    <rect x="28" y="28" width="360" height="268" rx="3" fill="{LINE}"/>
    <rect x="16" y="16" width="360" height="268" rx="3" fill="#e6dfd2"/>
    <rect x="4" y="4" width="360" height="268" rx="3" fill="{PAPER_CARD}" stroke="{LINE}" stroke-width="1.5"/>
    <line x1="36" y1="4" x2="36" y2="272" stroke="{LINE}" stroke-width="1"/>
    <circle cx="36" cy="48" r="3" fill="{ACCENT}"/>
    <circle cx="36" cy="96" r="3" fill="{ACCENT}"/>
    <circle cx="36" cy="144" r="3" fill="{ACCENT}"/>
    <circle cx="36" cy="192" r="3" fill="{ACCENT}"/>
    <g font-family="{FONT_SERIF}" fill="{INK}">
      <text x="60" y="56" font-size="16" fill="{ACCENT}">тетрадь I</text>
      <text x="60" y="100" font-size="24" font-weight="700">Воспоминания</text>
      <text x="60" y="136" font-size="20" fill="{MUTED}">Родители</text>
      <text x="60" y="172" font-size="20" fill="{MUTED}">Фото · Документы</text>
      <text x="60" y="208" font-size="20" fill="{MUTED}">История · Люди</text>
    </g>
    <text x="300" y="248" font-family="{FONT_MONO}" font-size="16" fill="{ACCENT}">л. 01</text>
  </g>
</svg>
'''


def section(title: str, kicker: str, name: str) -> str:
    sid = name.replace("-", "")
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="128" viewBox="0 0 1200 128"
     role="img" aria-labelledby="{sid}Title {sid}Desc">
  <title id="{sid}Title">{title}</title>
  <desc id="{sid}Desc">{kicker}</desc>
  <rect width="1200" height="128" rx="4" fill="{PAPER}"/>
  <rect x="48" y="28" width="3" height="72" fill="{RULE}"/>
  <text x="80" y="54" font-family="{FONT_UI}" font-size="16" letter-spacing="3" fill="{ACCENT}">{kicker}</text>
  <text x="80" y="96" font-family="{FONT_SERIF}" font-size="36" font-weight="700" fill="{INK}">{title}</text>
</svg>
'''


def workflow() -> str:
    steps = [
        ("01", "Скан", "рукопись"),
        ("02", "inbox", "сырьё"),
        ("03", "Разбор", "факты"),
        ("04", "content", "RU · EN"),
        ("05", "сжс.рф", "сайт"),
    ]
    parts: list[str] = []
    for i, (num, title, sub) in enumerate(steps):
        x = 48 + i * 228
        parts.append(f'''
  <g transform="translate({x} 56)">
    <rect width="208" height="112" rx="3" fill="{PAPER_CARD}" stroke="{LINE}"/>
    <text x="16" y="32" font-family="{FONT_MONO}" font-size="16" fill="{ACCENT}">{num}</text>
    <text x="16" y="68" font-family="{FONT_SERIF}" font-size="24" font-weight="700" fill="{INK}">{title}</text>
    <text x="16" y="94" font-family="{FONT_UI}" font-size="18" fill="{MUTED}">{sub}</text>
  </g>''')
        if i < len(steps) - 1:
            ax = x + 208
            parts.append(
                f'<path d="M{ax + 6} 112 L{ax + 16} 112" stroke="{ACCENT}" stroke-width="2"/>'
            )
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="200" viewBox="0 0 1200 200"
     role="img" aria-labelledby="wfTitle wfDesc">
  <title id="wfTitle">Как архив становится сайтом</title>
  <desc id="wfDesc">Скан рукописи, inbox, проверка фактов, статьи RU/EN, публикация на сжс.рф</desc>
  <rect width="1200" height="200" rx="4" fill="{PAPER}"/>
  <text x="48" y="36" font-family="{FONT_UI}" font-size="16" letter-spacing="3" fill="{ACCENT}">ХОД РАБОТЫ</text>
  {''.join(parts)}
</svg>
'''


def inbox_map() -> str:
    rows = [
        ("inbox/scans/memoirs/", "фото рукописных мемуаров"),
        ("inbox/scans/photos/", "семейные фото на разбор"),
        ("inbox/scans/documents/", "документы и письма"),
        ("inbox/transcripts/", "расшифровки до публикации"),
        ("inbox/notes/", "вопросы к семье"),
        ("content/ru · content/en", "готовые страницы сайта"),
    ]
    body: list[str] = []
    for i, (path, desc) in enumerate(rows):
        y = 64 + i * 40
        fill = PAPER_CARD if i % 2 == 0 else PAPER
        body.append(f'''
  <rect x="48" y="{y - 26}" width="1104" height="36" fill="{fill}"/>
  <text x="64" y="{y}" font-family="{FONT_MONO}" font-size="18" fill="{INK}">{path}</text>
  <text x="560" y="{y}" font-family="{FONT_UI}" font-size="18" fill="{MUTED}">{desc}</text>''')
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320"
     role="img" aria-labelledby="inTitle inDesc">
  <title id="inTitle">Карта inbox</title>
  <desc id="inDesc">Рабочие папки сканов и расшифровок. Фото в git не коммитятся.</desc>
  <rect width="1200" height="320" rx="4" fill="{PAPER}"/>
  <rect x="48" y="24" width="3" height="40" fill="{RULE}"/>
  <text x="64" y="52" font-family="{FONT_UI}" font-size="16" letter-spacing="3" fill="{ACCENT}">INBOX · НЕ САЙТ</text>
  {''.join(body)}
</svg>
'''


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    write("hero.svg", hero())
    write("workflow.svg", workflow())
    write("inbox-map.svg", inbox_map())
    write("section-start.svg", section("Старт", "ЛОКАЛЬНО", "start"))
    write("section-sections.svg", section("Разделы сайта", "СЖС.РФ", "sections"))
    write("section-inbox.svg", section("Inbox", "СЫРЬЁ АРХИВА", "inbox"))
    write("section-shoot.svg", section("Как снимать", "РУКОПИСИ", "shoot"))


if __name__ == "__main__":
    main()
