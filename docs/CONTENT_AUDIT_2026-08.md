# Content audit — August 2026

**Baseline HEAD:** `eab4706755695ba9d866587833d0548a6fda2e3a`  
**Branch:** `task/archive-content-audit-2026-08`  
**Site:** https://сжс.рф  
**Build (before cleanup):** Hugo 0.164.0 extended — 152 RU / 150 EN pages  

Status legend:

| Code | Meaning |
|------|---------|
| scan_ready | Scan prepared in local inbox |
| first_pass | Primary machine-assisted transcription published |
| partial_verify | Some pages visually re-checked |
| manual_verify | Full manual verification (rare so far) |
| editorial | Editor-written page (not diplomatic transcript) |
| tr_draft | EN draft exists |
| tr_sync | EN roughly matches RU structure |
| tr_reviewed | EN reviewed for parity |

## Public RU ↔ EN inventory

### Core / portal

| RU | EN | Type | Notes |
|----|----|------|-------|
| `_index.md` | `_index.md` | portal | “95 years” age claim; birth conflict |
| `o-proekte.md` | `about.md` | editorial | |
| `search.md` | `search.md` | system | |
| `archives.md` | `archives.md` | editorial | |

### Memoirs / diary

| RU | EN | original_pages | transcription | manual check | EN | `[?]` ~ | Workflow residue | Overlaps |
|----|----|----------------|---------------|--------------|-----|--------|------------------|----------|
| `vospominaniya/_index.md` | `memoirs/_index.md` | — | editorial | — | tr_sync | — | — | — |
| `o-tatyane-timofeevne.md` | `about-tatyana-timofeevna.md` | — | editorial | partial | tr_sync | — | medical caption | birth 1924 vs chart 1926 |
| `dnevnik/_index.md` | `diary/_index.md` | 001–079 | first_pass | partial | tr_sync | — | overclaim softened earlier | — |
| `dnevnik/o-tetradi.md` | `diary/about-the-notebook.md` | 001–079 | editorial | partial | tr_sync | — | — | — |
| `00-oblozhka-i-rodoslovnye` | `00-cover-and-charts` | 001–006 | first_pass | partial | tr_sync | 1 | phones redacted wording; living-person full dates | 005≈006 leaf |
| `01-moya-mama` | `01-my-mother` | 007–010 | first_pass | first_pass | tr_sync | 5 | — | — |
| `02-otec-brak-deti` | `02-father-marriage-children` | 011–014 | first_pass | first_pass | tr_sync | 14 | — | 012–013 w/ 03 |
| `03-detstvo-moskva` | `03-childhood-moscow` | 012–013, 033–040, 048–050 | first_pass | first_pass | tr_sync | 46 | FACTS + batch_ | 012–013, 039–040 |
| `04-voyna-1941` | `04-war-1941` | 015–024 | first_pass | partial (022–024) | tr_sync | 15 | — | 021 w/ 05/06 |
| `05-otec-vchk-i-stikhi` | `05-father-cheka-verses` | 025–032 | first_pass | first_pass | tr_sync | 12 | rot=, FACTS, batch_ | 028–030 w/ 06 |
| `06-dokumenty-sezdy` | `06-documents-congresses` | 028–030, 039–047 | first_pass | first_pass | tr_sync | 37 | rot=, FACTS, tables, batch_ | 028–030, 039–040, 021 |
| `07-dacha-yubilei` | `07-dacha-anniversaries` | 051–057 | partial_verify | partial (051–057) | tr_sync | 29 | — | — |
| `08-otec-harakter` | `08-father-character` | 058–071 | partial_verify | partial (058–060) | tr_sync | 164 | FACTS H1, batch_, paths | 060≈058 |
| `09-dokumenty-v-tetradi` | `09-documents-in-notebook` | 072–079 | first_pass | first_pass | tr_sync | 6 | Facts extracted H1 | — |

### Parents

| RU | EN | Type | Privacy / issues |
|----|----|------|------------------|
| `roditeli/_index` | `parents/_index` | editorial | — |
| `samsonov-timofey-petrovich` | `timofey-petrovich-samsonov` | editorial + docs | deceased |
| `eva-konstantinovna` | `eva-konstantinovna` | editorial | deceased |
| `otets-i-mat` | `father-and-mother` | editorial | — |
| `krivoshein-dmitriy-aleksandrovich` | `dmitry-aleksandrovich-krivoshein` | editorial + wiki | deceased |

### Documents, history, places, photos

| RU | EN | Notes |
|----|----|-------|
| `dokumenty/*` (5 + index) | `documents/*` | External/public docs; some TBD on dates |
| `istoriya/*` | `history/*` | Editorial; “Bashkir TBD” |
| `mesta/moskva-semeynaya` | `places/family-moscow` | Maps |
| `foto/*` | `photos/*` | Captions need privacy check on 2019 photo |

### Templates (should stay draft / not listed as finished archive)

- `_shablon-zapisi.md` / `_template-entry.md`

## Canonical numbering

See `docs/manuscript-page-map.md`.

Additional leaf mapping:

| physical_leaf_id | original_page | alternate_scan | note |
|------------------|---------------|----------------|------|
| genealogy-krivoshein-01 | 005 | 006 | Two scans of one Krivoshein chart leaf (visual; order preserved) |
| diary-pudovkin-accident | 058 | 060 (cropped) | 060 is partial re-scan of 058, not a new story |
| diary-duplicate-067 | 067 | 068 | 068 = 067 @ 180° removed from control PDF |

## Critical conflicts

1. **Tatyana birth year** — `data/fact_conflicts.yaml` → `tatyana-birth-year`  
2. **Васильки (051) vs Валуево (064)** — unresolved pending 064 re-check  
3. **Лудовкин[?]** name spelling vs historical Pudovkin — manuscript form kept  

## Privacy findings (pre-cleanup)

- Genealogy **original_page 004**: full DOB for living descendants (day/month/year).  
- Phone notes on page 002 already redacted in image; text still says `[скрыто]/[redacted]` (mixed RU/EN).  
- Photo caption 2019: fixed 2026-08-01 — no “last year of life”; death 24.09.2021 from plaque.  
 
- Age “95 years” implies a birth year — must not be used to settle conflict.  

## Workflow residue (pre-cleanup count)

Patterns found across diary chapters: `rot=`, `FACTS EXTRACTED`, `Извлечённые факты`, `batch_*.md`, `work/p-`, `pages/*.jpg`, `End of batch`, orientation tables.

## Images without confirmed identity

- Group photos on diary pages without named captions beyond author notes.  
- “Unknown” military personnel on page 022 — correctly anonymous.  
- Portraits on charts: named only when chart or author label supports it.  

## Completeness honesty

No chapter may claim full manual verification of all 79 pages.  
Verified subsets: **022–024** (EN filled), **051–060** (visual QA batch).  

## Follow-up work (this audit branch)

1. Privacy redaction + privacy policy pages  
2. Remove public workflow residue  
3. Duplicate ownership map + reduce full re-posts  
4. Front matter status fields + single H1  
5. Neutral birth wording + stronger about-Tatyana structure without invention  
