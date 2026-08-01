# Letter date / metadata verification — B02 (visual)

**Date:** 2026-08-01  
**Method:** `read_file` on JPEG scans under `static/photos/dnevnik-tt/` (images supported); tight crops + contrast boost for ambiguous digits.  
**Rule:** no invented text; only clear public metadata corrections.

## Pages inspected

| Scan | Date on page | Author / signature | Addressee | Damage / notes | Caption/status before | Action |
|------|--------------|--------------------|-----------|----------------|----------------------|--------|
| **str-103.jpg** | **11.08.43** (top left; month digit is **08**, not 05) | Closing: **Ваш Дмитрий** (most consistent reading of original + first crop; alternate **Тимоша** not confirmed enough to change) | Родители и сестрёнка Таня; header «Действующая армия» | Folds; brown paper; right half of scan | Caption «11 **мая** 1943» **WRONG** | **Fixed** caption → 11 **августа** 1943; added `11.08.43` to body |
| **str-104.jpg** | **28.VII.44** (top left; Roman **VII**, not VI) | **Дмитрий** (full-page read) | «Здравствуйте дорогие родители»; top-right «г. Самсонов» | Torn/ragged right edge; heavy creases | Caption «28 **июня** 1944» and body `28.VI.44` **WRONG** | **Fixed** → 28 **июля** 1944 / `28.VII.44` |
| **str-105.jpg** | **14.VI.43.** | Continues to reverse (str-106) | «Здравствуй родная мама!» | Folds; complete page | Caption «14 июня 1943» OK | None |
| **str-106.jpg** | (reverse of 105) postmarks visible | Closing **Тимоша** («ваш сын») | Address block: **Самсоновой Е.К.**, Москва, ул. Серафимовича, д. Правительства, 12 под., кв 223; from **Самсонову Т.Т.**, п/п **18003 «2»** | Envelope-style reverse; stamps | Caption «Оборот…» OK | None |
| **str-107.jpg** | **13.07.44.** (Arabic; content had 13.VII.44) | **Ваш Тимоша**; «Саша целует» | Родители и сестрёнка Таня | Center fold; lower third a bit pale | Caption «13 июля 1944» OK | None (date form 13.VII vs 13.07 equivalent) |
| **str-108.jpg** | Decree **22 декабря 1942**; presentation **«23» сентября 1943** (year digit best read as **3**, not 2/5) | Certificate for **гв. сержант Самсонов Тимофей Тимофеевич**; unit **79 ГМП**; signer **гв. подполковник В. Попов** (was Ю[?]опов); blank **II № 34769** | — | Horizontal + vertical folds; round stamp lower left | Caption OK; year 1943 already correct in chapter + doc pages | **Safe text:** Попов + № 34769 in chapter/doc transcriptions |
| **str-127.jpg** | Narrative **1943 год** (author’s note, not a letter date) | Notebook hand (Т.Т. / Tanya) | Intro to letter from wounded comrade of father’s friends after Stalingrad reform | Clean white leaf | Caption «Краткая подпись…» weak | **Fixed** caption to describe intro note |
| **str-128.jpg** | No letter date on this side (continues 129) | — (continues; author on 129) | «Здравствуй, Таня!» | Blue ink blot mid-left; folds | Caption OK | None |
| **str-129.jpg** | **20 апреля 1943г.** | **Миша Фриоленко** | Таня; reply addr. **ПП 18003 „г.“** / Фриоленко М.М. | Blue blot; red pencil / dark strokes at bottom | Caption «Продолжение…» OK; date in body OK | None |
| **str-131.jpg** | **1 марта** + «С весной!» (year not on leaf) | **Геннадий** | «Танюша!» | Center folds | Caption OK | None |
| **str-132.jpg** | **18-11-43.** | Header «Письмо от Геннадия Вохминцева»; close **— Геннадий** | «Дорогая Таня!» | Folds | Caption 18.11.1943 OK | None |
| **str-133.jpg** | **29-11-43.** | **— Геннадий** | «Танюша…» | Center folds; small dark blot near signature | Caption 29.11.1943 OK | None |

## Known-issue checklist

| Claim | Visual result |
|-------|----------------|
| Ch.12 «11 мая» vs audit **11.08.1943** | **Confirmed error.** Scan shows **11.08.43**. Caption fixed to August. |
| Signature may be **Тимоша**, not **Дмитрий** (str-103) | **Keep Дмитрий.** Full page + first signature crop read Дмитрий; over-processed crop suggested Тимоша — not safe to change. Note: str-105–107 close as **Тимоша**; 103–104 as **Дмитрий** — different closing forms; do not force identity. |
| str-104 caption **28.VI.44** incorrect | **Confirmed.** Scan shows **28.VII.44**. Fixed. |

## Files touched

- `content/ru/vospominaniya/dnevnik/12-brat-front-103-108.md` — captions 103/104; body date forms; medal № / Попов
- `content/en/memoirs/diary/12-brother-front-letters-101-108.md` — same
- `content/ru/vospominaniya/dnevnik/14-voyna-evakuaciya-120-127.md` — caption 127
- `content/en/memoirs/diary/14-war-evacuation-120-127.md` — caption 127
- `content/ru/dokumenty/udostoverenie-oborona-stalingrada-samsonov-tt.md` — № 34769, signer Попов
- `content/en/documents/stalingrad-defense-medal-samsonov-tt.md` — same
- `content/ru/dokumenty/pisma-s-fronta/_index.md` + `pismo-103-1943.md` + `pismo-104.md`
- `content/en/documents/letters-from-the-front/_index.md` + `letter-103-1943.md` + `letter-104.md`

## Left alone (not safe / not wrong)

- Uncertain letter body transcriptions (word-level `[?]` remains).
- str-103/104 identity of «Дмитрий» vs brother Тимоша — metadata only; no invented biography.
- Medal year: **1943** retained (best digit reading; matches decree chronology).
