# Diary page coverage report (pages 1–79)

**Date:** 2026-08-01  
**Scope:** Russian diary chapter files `content/ru/vospominaniya/dnevnik/0*.md`  
**Marker format searched:** HTML comments `<!-- стр. NNN -->` (zero-padded three digits)  
**No alternate forms** (`<!-- стр. 7 -->`, unpadded, etc.) found in chapter files.

## Summary

| Metric | Count |
|--------|------:|
| Notebook pages expected | 79 |
| Distinct page markers in chapters | **76** |
| **Missing from chapter content** | **3** (pages **022, 023, 024**) |
| Pages with markers in ≥2 chapters (overlap) | 7 |

**Verdict:** Chapters do **not** yet cover all pages 1–79. Gap is contiguous: **022–024**. Full transcript of those pages exists in `batch_21_30.md`.

---

## Pages by chapter file

Markers are listed in document order as they appear in each file.

### `00-oblozhka-i-rodoslovnye.md`
| Pages | Range |
|-------|-------|
| 001, 002, 003, 004, 005, 006 | **1–6** |

### `01-moya-mama.md`
| Pages | Range |
|-------|-------|
| 007, 008, 009, 010 | **7–10** |

### `02-otec-brak-deti.md`
| Pages | Range |
|-------|-------|
| 011, 012, 013, 014 | **11–14** |

### `03-detstvo-moskva.md`
| Pages | Range |
|-------|-------|
| 012, 013 | (overlap with ch. 02) |
| 033, 034, 035, 036, 037, 038, 039, 040 | **33–40** |
| 048, 049, 050 | **48–50** |

### `04-voyna-1941.md`
| Pages | Range |
|-------|-------|
| 015, 016, 017, 018, 019, 020, 021 | **15–21** |

### `05-otec-vchk-i-stikhi.md`
| Pages | Range |
|-------|-------|
| 025, 026, 027, 028, 029, 030, 031, 032 | **25–32** |

Note: orientation table in this file mentions scan pages 022–024, but there are **no** `<!-- стр. 022 -->` … content sections.

### `06-dokumenty-sezdy.md`
| Pages | Range |
|-------|-------|
| 028, 029, 030 | (overlap with ch. 05) |
| 039, 040 | (overlap with ch. 03) |
| 041, 042, 043, 044, 045, 046, 047 | **41–47** |

Note: orientation table likewise lists 022–024 without chapter content markers.

### `07-dacha-yubilei.md`
| Pages | Range |
|-------|-------|
| 051, 052, 053, 054, 055, 056, 057 | **51–57** |

### `08-otec-harakter.md`
| Pages | Range |
|-------|-------|
| 058, 059, 060, 061, 062, 063, 064, 065, 066, 067, 068, 069, 070, 071 | **58–71** |

### `09-dokumenty-v-tetradi.md`
| Pages | Range |
|-------|-------|
| 072, 073, 074, 075, 076, 077, 078, 079 | **72–79** |

---

## Full matrix: page → chapter(s)

| Page | Chapter file(s) with `<!-- стр. NNN -->` |
|-----:|------------------------------------------|
| 001–006 | `00-oblozhka-i-rodoslovnye.md` |
| 007–010 | `01-moya-mama.md` |
| 011 | `02-otec-brak-deti.md` |
| 012 | `02-otec-brak-deti.md`, `03-detstvo-moskva.md` |
| 013 | `02-otec-brak-deti.md`, `03-detstvo-moskva.md` |
| 014 | `02-otec-brak-deti.md` |
| 015–021 | `04-voyna-1941.md` |
| **022** | **— MISSING** |
| **023** | **— MISSING** |
| **024** | **— MISSING** |
| 025–027 | `05-otec-vchk-i-stikhi.md` |
| 028–030 | `05-otec-vchk-i-stikhi.md`, `06-dokumenty-sezdy.md` |
| 031–032 | `05-otec-vchk-i-stikhi.md` |
| 033–038 | `03-detstvo-moskva.md` |
| 039–040 | `03-detstvo-moskva.md`, `06-dokumenty-sezdy.md` |
| 041–047 | `06-dokumenty-sezdy.md` |
| 048–050 | `03-detstvo-moskva.md` |
| 051–057 | `07-dacha-yubilei.md` |
| 058–071 | `08-otec-harakter.md` |
| 072–079 | `09-dokumenty-v-tetradi.md` |

---

## Missing pages 1–79

| Page | In chapters? | Batch transcript | Notes (from batch only; not invented) |
|-----:|:------------:|------------------|----------------------------------------|
| **022** | no | `batch_21_30.md` → `## PAGE 022` | Photos: mama with military / handing komsomol ticket; captions about VChK memoirs and Dzerzhinsky |
| **023** | no | `batch_21_30.md` → `## PAGE 023` | Mama’s late illness, operations, character; author as caregiver |
| **024** | no | `batch_21_30.md` → `## PAGE 024` | Continuation of 023; death 17 May 1981, Novodevichy; start of father’s poem «Еве!» (13.IV.41) |

Narrative bridge: chapter `04` ends at page **021**; chapter `05` starts at page **025**. Pages **022–024** sit in that gap (end of mama’s story / transition into father’s VChK / poetry).

---

## Overlaps (same page marker in multiple chapters)

These are intentional or residual duplicates of transcript blocks, not missing pages:

| Pages | Files |
|------:|-------|
| 012, 013 | `02-otec-brak-deti.md` + `03-detstvo-moskva.md` |
| 028, 029, 030 | `05-otec-vchk-i-stikhi.md` + `06-dokumenty-sezdy.md` |
| 039, 040 | `03-detstvo-moskva.md` + `06-dokumenty-sezdy.md` |

---

## Batch transcript index (all pages 1–79 present in batches)

| Batch file | Pages |
|------------|------:|
| `batch_01_10.md` | 001–010 |
| `batch_11_20.md` | 011–020 |
| `batch_21_30.md` | 021–030 (**includes 022–024**) |
| `batch_31_40.md` | 031–040 |
| `batch_41_50.md` | 041–050 |
| `batch_51_60.md` | 051–060 |
| `batch_61_70.md` | 061–070 |
| `batch_71_79.md` | 071–079 |

All 79 notebook pages appear as `## PAGE NNN` headings in the batch files. The only gap is chapter packaging of **022–024**.

---

## Suggested fix (documentation only)

To close coverage, add content for pages 022–024 into the chapter sequence—most naturally either:

- end of `01-moya-mama.md` / a mama-related chapter (022–024 continue mama’s late life and death), or  
- start of `05-otec-vchk-i-stikhi.md` (024 ends with father’s poem to Eva, which continues on 025 already in ch. 05),

using the existing text from `inbox/scans/memoirs/transcripts/batch_21_30.md` (`## PAGE 022` … `## PAGE 024`) and markers:

```html
<!-- стр. 022 -->
<!-- стр. 023 -->
<!-- стр. 024 -->
```

This report does not invent or paste that content.
