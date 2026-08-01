# Privacy review — B02 family / children (original_page ≈149–160)

**Date:** 2026-08-01  
**Scope:** Diary chapters on Crimea/family and the sons; photo captions; related “about Tatyana” and genealogy charts.  
**Rules applied:**

- Potentially living people: do **not** publish full DOB (day + month + year).
- Year of birth alone is OK when already part of the public family narrative (e.g. Seryozha **1957**, Mitya **1948**).
- Medical episodes: keep if historical and non-sensational; flag modern/sensitive medical detail for family decision.
- User note: manuscript holds full birth dates for Mitya and Seryozha; public site prefers **year-only**.

No git commit was made as part of this review.

---

## Files inspected

| Path | Role |
|------|------|
| `content/ru/vospominaniya/dnevnik/17-krym-semya-140-149.md` | Birth of Mitya (orig. ~144–145) |
| `content/en/memoirs/diary/17-crimea-family-140-149.md` | EN counterpart |
| `content/ru/vospominaniya/dnevnik/18-synovya-150-161.md` | Sons narrative (orig. ~150–161) |
| `content/en/memoirs/diary/18-sons-150-161.md` | EN counterpart |
| `content/ru/foto/tetrad-semya-prodolzhenie.md` | Photo captions B02 family |
| `content/en/photos/notebook-family-continued.md` | EN photo page |
| `content/ru/vospominaniya/o-tatyane-timofeevne.md` | Overlap: children/grandchildren wording |
| `content/en/memoirs/about-tatyana-timofeevna.md` | EN about page |
| `content/ru/vospominaniya/dnevnik/00-oblozhka-i-rodoslovnye.md` | Genealogy chart p.004 (living DOBs) |
| `content/en/memoirs/diary/00-cover-and-charts.md` | EN chart |

Inbox / data archives (`inbox/scans/…`, `data/archive_photos/…`) still hold full manuscript dates; they are **not** public site content and were not altered.

---

## Findings

### 1. Full / partial birth dates (living descendants)

| Person | Manuscript (local archive) | Was on public site before review | Action |
|--------|----------------------------|----------------------------------|--------|
| **Митя / Дмитрий А.** | Full date on page (~144): **28 июля 1948** (consistent across pass2 transcripts) | Full day+month+year in ch.17 RU + EN | **Redacted → year only** |
| **Серёжа / Сергей А.** | Full date on page (~155): **16 сентября 1957** (caption + body in inbox transcripts) | Already year-only in captions (`род. 1957`); body still had **month+year** «В сентябре 1957» | **Month stripped → year only** |
| Grandchildren (Алёша 1981, Алёна/Елена years on chart) | Year-level in narrative/chart | Year only | No change |
| Spouses on chart (Белла 1948, Татьяна 1957, etc.) | Year on chart | Year only | No change |

**User note vs manuscript:** the task note mentioned Mitya **28 May 1948**; the published and archive transcriptions of this leaf give **28 июля 1948**. Expected due date in the narrative (“в конце мая”) is kept as pregnancy timing, not a published DOB. Public wording is now **year-only**, so day/month discrepancy is not exposed. Full dates remain only offline in the family archive.

### 2. Genealogy (page 004 / chart)

Already privacy-safe:

- Living lines use **year only** (1948, 1957, 1976, 1977, 1981, 1982, 1986, 2003, …).
- Explicit privacy note: living relatives → year + relationship only; full dates kept local.

No edit required.

### 3. Photo pages (`tetrad-semya-prodolzhenie` / `notebook-family-continued`)

Captions already avoid full DOBs:

- «Серёжа», «Митя с дедом», «Митя в детстве», years only where used (e.g. «1950-х»).
- Intro note: full birth dates of living people not published.

No edit required for DOB. Residual risk: **page scan images** (`str-155.jpg` etc.) may still show handwritten full dates in the manuscript photo; text captions are year-only. Family may later choose crops or blurred bands on those scans.

### 4. About Tatyana pages

- Deceased principal: full life dates OK (1926–2021; plaque-backed).
- Children/grandchildren: only pointer to charts + “для живых — только годы”.

No edit required for this review.

### 5. Medical content (historical narrative — kept)

In ch.18 (and mirrored EN body): childhood/youth episodes — angina, tonsil/adenoid surgery, concussion, dysentery, post-op heart concern, broken arm in institute, hospital stays; death of father T.P. Samsonov 28.10.1955; later hospital mentions for other relatives.

**Assessment:** mid-20th-century family history, non-sensational, integral to the memoir. **Kept** per rule (historical / non-sensational).

**Flag for family decision (no edit now):** any future addition of *modern* clinical detail for living people should stay offline unless explicitly approved.

### 6. Address unit (related residual)

| Location | Issue | Action |
|----------|--------|--------|
| Ch.18 p.157 caption line | Full unit: `Ленинск. пр. д. 11 кв. 116` (living-family photo context; flagged high in prior `privacy_scan_b02.md` for m-078) | **Redacted** → `Ленинск. пр. [адрес скрыт]` (RU + EN) |
| Other mentions | «Ленинском пр.» / «Б. Калужскую (Ленинск. пр) д. 4» without apartment | Left as historical street-level narrative |

### 7. Not in scope / OK

- Deceased: Tatyana Timofeevna, parents, husband Alexander (1926–1988) — full dates remain appropriate.
- Historical document dates, wartime dates, Sputnik/October 1957 as event context — not DOBs of living people.
- Photo captions naming only given names without full DOB — OK.

---

## Changes made (public content)

| File | Change |
|------|--------|
| `content/ru/vospominaniya/dnevnik/17-krym-semya-140-149.md` | `28 июля 1948г. у нас родился сын` → `В 1948 г. у нас родился сын` |
| `content/en/memoirs/diary/17-crimea-family-140-149.md` | Same body line (RU manuscript text block) |
| `content/ru/vospominaniya/dnevnik/18-synovya-150-161.md` | `В сентябре 1957 г. у нас родился Серёжа` → `В 1957 г. …`; unit address redacted |
| `content/en/memoirs/diary/18-sons-150-161.md` | Same two edits |

Intro notes already present on ch.17/18 and photo pages (“year only / no full birth dates for living”) left as-is. Front matter `privacy_reviewed: true` retained (now consistent with year-only births after these fixes).

---

## Residual / family decisions

1. **Manuscript page images** on the public site may still display handwritten full DOBs (especially Seryozha leaf / `str-155`). Option: crop, blur date band, or replace with cropped portraits only.
2. **Alyona 1990** (diary) vs **Елена 1986** (chart) — naming/year consistency is editorial/factual, not a full-DOB privacy issue; not changed here.
3. **Modern medical / contacts** of living people: do not add without explicit family approval.
4. Local archive and inbox transcripts intentionally keep full dates for private use.

---

## Summary status

| Area | Status after review |
|------|---------------------|
| Full DOB Mitya on public diary text | **Fixed** (year-only) |
| Month+year Seryozha birth on public diary text | **Fixed** (year-only) |
| Captions photo B02 | Already OK |
| Genealogy living lines | Already OK |
| Historical medical childhood narrative | Kept |
| Full residential unit on p.157 line | **Fixed** (redacted) |
| Scan images with handwritten dates | Residual — family optional crop/blur |
