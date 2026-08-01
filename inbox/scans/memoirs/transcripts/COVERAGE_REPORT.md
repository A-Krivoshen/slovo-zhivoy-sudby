# Diary page coverage report (pages 1–79)

**Date:** 2026-08-01 (updated)  
**Scope:** Russian and English diary chapter files  
**Marker format RU:** HTML comments `<!-- стр. NNN -->`  
**Marker format EN:** HTML comments `<!-- p. NNN -->`

## Summary

| Metric | Count |
|--------|------:|
| Notebook pages in first scan batch | 79 |
| Distinct page markers in RU chapters | **79** |
| Distinct page markers in EN chapters | **79** |
| **Missing from chapter content** | **0** |
| Pages with markers in ≥2 chapters (overlap) | 7 |

**Verdict:** First batch pages **1–79** are packaged into chapters RU+EN. EN pages **022–024** were completed on 2026-08-01 (were stubs). Scans `str-022.jpg`–`str-024.jpg` published under `static/photos/dnevnik-tt/`.

This does **not** mean the whole family archive is finished — only the first notebook scan batch.

---

## Pages by chapter file (RU)

| Chapter | Pages |
|---------|-------|
| `00-oblozhka-i-rodoslovnye.md` | 001–006 |
| `01-moya-mama.md` | 007–010 |
| `02-otec-brak-deti.md` | 011–014 |
| `03-detstvo-moskva.md` | 012–013 (overlap), 033–040, 048–050 |
| `04-voyna-1941.md` | 015–024 (includes mama’s later years & death) |
| `05-otec-vchk-i-stikhi.md` | 025–032 |
| `06-dokumenty-sezdy.md` | 028–030, 039–040 (overlaps), 041–047 |
| `07-dacha-yubilei.md` | 051–057 |
| `08-otec-harakter.md` | 058–071 |
| `09-dokumenty-v-tetradi.md` | 072–079 |

---

## Overlaps (same page marker in multiple chapters)

| Pages | Files |
|------:|-------|
| 012, 013 | `02` + `03` |
| 028, 029, 030 | `05` + `06` |
| 039, 040 | `03` + `06` |

Overlaps are residual duplicate transcript blocks, not missing pages. Future cleanup may de-duplicate without changing URLs.

---

## Published notebook scan images (`static/photos/dnevnik-tt/`)

| File | Page |
|------|-----:|
| str-001 … str-003 | 1–3 |
| str-007, 009, 010, 012, 015 | selected |
| **str-022, str-023, str-024** | **22–24** (added this batch) |

Master scans remain in local `inbox/scans/memoirs/` (gitignored media). Not every page is published as a site image yet.

---

## Batch transcript index (offline)

| Batch file | Pages |
|------------|------:|
| `batch_01_10.md` … `batch_71_79.md` | 001–079 |

All 79 notebook pages appear as `## PAGE NNN` in batch files under `inbox/scans/memoirs/transcripts/`.
