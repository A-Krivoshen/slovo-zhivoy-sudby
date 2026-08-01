#!/usr/bin/env python3
"""Generate pure SVG assets for the repository README.

Deterministic, no network, no fonts downloaded.
Run: python3 scripts/generate_readme_assets.py
CI re-runs this on every push to main.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "readme"

# Memoir / paper archive palette (matches site favicon)
PAPER = "#F5ECDC"
PAPER_DARK = "#E8D9C0"
INK = "#5C3D2E"
INK_SOFT = "#7A5644"
ACCENT = "#8B5A3C"
LINE = "#C4A882"
WHITE = "#FFFDF8"

FONT_UI = (
    "-apple-system, BlinkMacSystemFont, 'Segoe UI', "
    "'Noto Sans', 'Helvetica Neue', Arial, sans-serif"
)
FONT_SERIF = (
    "Georgia, 'Times New Roman', 'Noto Serif', 'DejaVu Serif', serif"
)


def write(name: str, svg: str) -> None:
    path = OUT / name
    path.write_text(svg.strip() + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} ({path.stat().st_size} bytes)")


def hero() -> str:
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="360" viewBox="0 0 1200 360"
     role="img" aria-labelledby="heroTitle heroDesc">
  <title id="heroTitle">Слово Живой Судьбы — семейный архив</title>
  <desc id="heroDesc">Мемуары Кривошеиной Татьяны Тимофеевны: воспоминания, родители, история, фото и документы. Сайт сжс.рф, языки RU и EN.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{PAPER}"/>
      <stop offset="100%" stop-color="{PAPER_DARK}"/>
    </linearGradient>
    <linearGradient id="side" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{INK}"/>
      <stop offset="100%" stop-color="{ACCENT}"/>
    </linearGradient>
  </defs>

  <rect width="1200" height="360" rx="28" fill="url(#bg)"/>
  <rect x="0" y="0" width="18" height="360" rx="0" fill="url(#side)"/>
  <rect x="0" y="342" width="1200" height="18" fill="{ACCENT}" opacity="0.85"/>

  <!-- monogram -->
  <g transform="translate(72 70)">
    <circle cx="90" cy="100" r="88" fill="{WHITE}" stroke="{INK}" stroke-width="4"/>
    <circle cx="90" cy="100" r="74" fill="none" stroke="{LINE}" stroke-width="2"/>
    <text x="90" y="118" text-anchor="middle"
          font-family="{FONT_SERIF}" font-size="52" font-weight="700" fill="{INK}">СЖС</text>
  </g>

  <!-- title block -->
  <g transform="translate(300 78)" font-family="{FONT_UI}">
    <text x="0" y="0" font-size="18" letter-spacing="3" fill="{ACCENT}" font-weight="600">СЕМЕЙНЫЙ АРХИВ · FAMILY ARCHIVE</text>
    <text x="0" y="58" font-family="{FONT_SERIF}" font-size="48" font-weight="700" fill="{INK}">Слово Живой Судьбы</text>
    <text x="0" y="100" font-family="{FONT_SERIF}" font-size="28" fill="{INK_SOFT}">Word of a Living Fate</text>
    <text x="0" y="150" font-size="22" fill="{INK}">Кривошеина Татьяна Тимофеевна</text>
    <text x="0" y="184" font-size="18" fill="{INK_SOFT}">мемуары · родители · история · фото · документы</text>
  </g>

  <!-- meta chips -->
  <g transform="translate(300 290)" font-family="{FONT_UI}" font-size="16" fill="{INK}">
    <rect x="0" y="-22" width="110" height="34" rx="17" fill="{WHITE}" stroke="{LINE}"/>
    <text x="55" y="0" text-anchor="middle">сжс.рф</text>
    <rect x="124" y="-22" width="72" height="34" rx="17" fill="{WHITE}" stroke="{LINE}"/>
    <text x="160" y="0" text-anchor="middle">RU · EN</text>
    <rect x="210" y="-22" width="120" height="34" rx="17" fill="{WHITE}" stroke="{LINE}"/>
    <text x="270" y="0" text-anchor="middle">Hugo · Pages</text>
    <rect x="344" y="-22" width="150" height="34" rx="17" fill="{WHITE}" stroke="{LINE}"/>
    <text x="419" y="0" text-anchor="middle">inbox → content</text>
  </g>
</svg>
'''


def section(title_ru: str, title_en: str, subtitle: str, name: str) -> str:
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="120" viewBox="0 0 1200 120"
     role="img" aria-labelledby="{name}Title {name}Desc">
  <title id="{name}Title">{title_ru}</title>
  <desc id="{name}Desc">{subtitle}</desc>
  <rect width="1200" height="120" rx="20" fill="{PAPER}"/>
  <rect x="0" y="0" width="12" height="120" fill="{INK}"/>
  <circle cx="56" cy="60" r="22" fill="{WHITE}" stroke="{ACCENT}" stroke-width="3"/>
  <text x="56" y="67" text-anchor="middle" font-family="{FONT_SERIF}" font-size="18" font-weight="700" fill="{INK}">С</text>
  <text x="96" y="52" font-family="{FONT_SERIF}" font-size="32" font-weight="700" fill="{INK}">{title_ru}</text>
  <text x="96" y="84" font-family="{FONT_UI}" font-size="18" fill="{INK_SOFT}">{title_en} · {subtitle}</text>
</svg>
'''


def workflow() -> str:
    """Pipeline: scan → inbox → transcript → content → site."""
    steps = [
        ("1", "Скан", "фото рукописи"),
        ("2", "inbox/", "scans/…"),
        ("3", "Разбор", "ИИ + семья"),
        ("4", "transcripts/", "черновик"),
        ("5", "content/", "RU · EN"),
        ("6", "сжс.рф", "сайт"),
    ]
    cards = []
    x0 = 40
    gap = 190
    for i, (num, title, sub) in enumerate(steps):
        x = x0 + i * gap
        cards.append(f'''
  <g transform="translate({x} 48)">
    <rect width="170" height="110" rx="16" fill="{WHITE}" stroke="{LINE}" stroke-width="2"/>
    <circle cx="28" cy="28" r="16" fill="{INK}"/>
    <text x="28" y="34" text-anchor="middle" font-family="{FONT_UI}" font-size="16" font-weight="700" fill="{PAPER}">{num}</text>
    <text x="85" y="50" text-anchor="middle" font-family="{FONT_SERIF}" font-size="22" font-weight="700" fill="{INK}">{title}</text>
    <text x="85" y="80" text-anchor="middle" font-family="{FONT_UI}" font-size="15" fill="{INK_SOFT}">{sub}</text>
  </g>''')
        if i < len(steps) - 1:
            ax = x + 170
            cards.append(f'''
  <path d="M{ax + 6} 103 L{ax + 18} 103" stroke="{ACCENT}" stroke-width="3" stroke-linecap="round"/>
  <path d="M{ax + 12} 97 L{ax + 20} 103 L{ax + 12} 109" fill="none" stroke="{ACCENT}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>''')

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="200" viewBox="0 0 1200 200"
     role="img" aria-labelledby="wfTitle wfDesc">
  <title id="wfTitle">Как мы работаем с архивом</title>
  <desc id="wfDesc">Пайплайн: скан рукописи → inbox → разбор → расшифровка → content RU/EN → сайт сжс.рф</desc>
  <rect width="1200" height="200" rx="20" fill="{PAPER}"/>
  <text x="40" y="32" font-family="{FONT_UI}" font-size="16" letter-spacing="2" fill="{ACCENT}" font-weight="600">WORKFLOW · КАК МЫ РАБОТАЕМ</text>
  {''.join(cards)}
</svg>
'''


def inbox_map() -> str:
    rows = [
        ("inbox/scans/memoirs/", "рукописные мемуары"),
        ("inbox/scans/photos/", "семейные фото на разбор"),
        ("inbox/scans/documents/", "документы и письма"),
        ("inbox/transcripts/", "расшифровки (ещё не на сайт)"),
        ("inbox/notes/", "вопросы и уточнения"),
        ("content/ru · content/en", "готовые статьи → сжс.рф"),
    ]
    body = []
    for i, (path, desc) in enumerate(rows):
        y = 58 + i * 36
        body.append(f'''
  <rect x="36" y="{y - 22}" width="1128" height="32" rx="10" fill="{WHITE if i % 2 == 0 else PAPER_DARK}" stroke="{LINE}" stroke-width="1"/>
  <text x="56" y="{y}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="17" fill="{INK}">{path}</text>
  <text x="520" y="{y}" font-family="{FONT_UI}" font-size="17" fill="{INK_SOFT}">{desc}</text>''')

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="280" viewBox="0 0 1200 280"
     role="img" aria-labelledby="inTitle inDesc">
  <title id="inTitle">Карта папки inbox</title>
  <desc id="inDesc">Структура рабочей папки inbox для сканов, расшифровок и заметок</desc>
  <rect width="1200" height="280" rx="20" fill="{PAPER}"/>
  <rect x="0" y="0" width="12" height="280" fill="{ACCENT}"/>
  <text x="36" y="32" font-family="{FONT_UI}" font-size="16" letter-spacing="2" fill="{ACCENT}" font-weight="600">INBOX · РАБОЧАЯ ЗОНА (НЕ САЙТ)</text>
  {''.join(body)}
</svg>
'''


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    write("hero.svg", hero())
    write("workflow.svg", workflow())
    write("inbox-map.svg", inbox_map())
    write(
        "section-start.svg",
        section("Старт", "Getting started", "локальный запуск и новая запись", "start"),
    )
    write(
        "section-sections.svg",
        section("Разделы сайта", "Site sections", "RU ↔ EN структура контента", "sections"),
    )
    write(
        "section-inbox.svg",
        section("Inbox", "Raw archive", "сканы, расшифровки, заметки", "inbox"),
    )
    write(
        "section-shoot.svg",
        section("Как снимать", "How to photograph", "рукописи для расшифровки", "shoot"),
    )


if __name__ == "__main__":
    main()
