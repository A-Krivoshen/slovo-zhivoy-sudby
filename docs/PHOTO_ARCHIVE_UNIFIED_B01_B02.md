# Unified photo archive — B01 + B02

**Status:** partial system in place — provenance + overlays + first verified crops + duplicate groups.  
**Not complete:** full visual approval of all auto candidates on both batches.

**Branch:** `task/extract-archive-photos-all-batches`  
**Date:** 2026-08-01

---

## Architecture (minimal extension)

Existing layout kept. Added:

| Path | Role |
| --- | --- |
| `data/archive_photos/index.yaml` | Unified index (public files + verified crops) |
| `data/archive_photos/static_photos_provenance.yaml` | Provenance of every `static/photos/**` file |
| `data/archive_photos/batch-b01.yaml` | B01 verified print crops |
| `data/archive_photos/batch-2026-08-01-b02.yaml` | B02 verified print crops |
| `data/archive_photos/duplicate_groups.yaml` | Confirmed related prints |
| `data/archive_photos/duplicate_hints.yaml` | pHash assistive hints only |
| `static/photos/archive-b01/` | New B01 print web derivatives (new URLs) |
| `static/photos/archive-b02/` | B02 print web derivatives (new URLs) |
| `inbox/scans/memoirs/batch_b01/` | Masters, overlays, crops (gitignored media) |
| `inbox/scans/memoirs/batch_b02/` | Same for B02 |
| `scripts/photo_detect_batch.py` | Stage A detector for either batch |
| `scripts/photo_detect_b02.py` / `photo_crop_b02.py` | Core detect/crop |

**URL policy:** preexisting public paths under `dnevnik-tt/`, `samsonov-tp/`, `eva-konstantinovna/`, `tatyana-tt/`, `krivoshein-da/` are **stable**. New crops use `archive-b0N/` only. No silent binary replace without documented comparison.

---

## Sources

### B01 (`manuscript-b01`)

| | |
| --- | --- |
| PDF | `nasha_rodoslovnaya_samsonovy_corrected.pdf` |
| SHA-256 | `99d859f158eaece09502b25e0082a9d8ca1294441312fb6978b64fac311a75c9` |
| Pages | **78** control PDF |
| Extraction | `pdfimages -j` → 2480×3507 @ 300 DPI |
| Masters | `inbox/scans/memoirs/batch_b01/masters/c-001.jpg` … `c-078.jpg` |
| Numbering | c 001–067 = original_page 001–067; c 068–078 = original_page **069–079**; original **068** absent (180° dup of 067) |

### B02 (`manuscript-b02`)

| | |
| --- | --- |
| PDF | `samsonovy_new_scans_2026-08-01_corrected.pdf` |
| SHA-256 | `66f69122cc6e0adac3083fb1c3b2833db8a85c9d5952c692f125188f114d424d` |
| Pages | **82** |
| Extraction | `pdfimages -j` → 2480×3507 @ 300 DPI |
| Masters | `inbox/scans/memoirs/batch_b02/masters/m-001.jpg` … `m-082.jpg` |
| original_page 080–161 | **PRELIMINARY** until junction/duplicate QA |

---

## Stage 1 — Provenance of existing `static/photos`

**123 files** catalogued in `static_photos_provenance.yaml`.

| source_type | count | examples |
| --- | ---: | --- |
| manuscript_page_scan | 93 | `dnevnik-tt/str-001…161` (full leaf / page overviews) |
| separate-family-album | 16 | `samsonov-tp/*`, `eva-konstantinovna/*` |
| manuscript_print_crop | 10 | `archive-b02/*` (+ thumbs) |
| user-photo | 3 | `tatyana-tt/2019…`, grave plaque |
| external-public-source | 1 | `krivoshein-da/dmitry-portrait.jpg` (Wikimedia) |

**Rule applied:** page numbers assigned only where naming + project docs already fix original_page (str-NNN). Family-album files are **not** auto-linked to notebook pages.

---

## Stage 2–4 — Overlays & candidates

| Batch | Pages | Pages w/ candidates | Auto candidates | Overlays |
| --- | ---: | ---: | ---: | --- |
| B01 | 78 | 41 | **199** | `batch_b01/overlays/` |
| B02 | 82 | 52 | **168** | `batch_b02/overlays/` |

Auto is assistive only. Dense handwriting produces many false positives; some real prints need manual bbox (B01 c-002 refined; B02 m-007 refined).

---

## Stage 5 — Visually verified print crops (partial)

### B01

| photo_id | op | type | privacy | web |
| --- | --- | --- | --- | --- |
| `b01-c002-ph01` | 002 | portrait | public_historical | `/photos/archive-b01/b01-c002-ph01.jpg` |

### B02

| photo_id | mp (op prelim.) | type | privacy | web |
| --- | --- | --- | --- | --- |
| `b02-mp001-ph01` | 001 (080) | group | public_historical | archive-b02 |
| `b02-mp001-ph02` | 001 (080) | group | public_historical | archive-b02 |
| `b02-mp002-ph01` | 002 (081) | building | public_historical | archive-b02 |
| `b02-mp005-ph01/02` | 005 (084) | cemetery | **living_people_review** | withheld |
| `b02-mp007-ph01/02` | 007 (086) | group | public_historical | archive-b02 |

Published **page scans** `dnevnik-tt/str-001,002,003,007,009,010,012,015,022–024`: **keep** (role = page overview, not single-print crop). Decision: **keep**, not replace.

---

## Stage 6 — Duplicate groups (visual)

| group | members | decision |
| --- | --- | --- |
| `dzerzhinsky-trio-winter` | `samsonov-tp/08-…` + `b02-mp001-ph01` | **keep both**; canonical public URL = 08 |
| `alexandrovsky-central-1910` | `samsonov-tp/09-…` + `b02-mp002-ph01` | **keep both**; canonical = 09 |
| `eva-portrait-polka-dots` | `eva-portrait.jpg` + `str-002` + `b01-c002-ph01` | **keep all**; canonical portrait URL = eva-portrait |

pHash alone **missed** trio/central pairs (hamming ~120) because of crop/tone — visual check required. `duplicate_hints.yaml` only caught self-pairs of B02 web↔view.

---

## Stage 7–8 — Index & privacy

- Unified index: `data/archive_photos/index.yaml` (~126 entries)
- Privacy: cemetery B02 m-005 withheld; 2019/home and living people need ongoing review
- No generative AI retouch; masters lossless in inbox

---

## Stage 9–10 — URL / publication

| Action | Count |
| --- | ---: |
| Old public URLs replaced | **0** |
| Old public URLs kept | all preexisting |
| New public print URLs added | archive-b01 (1) + archive-b02 (5 historical) |
| Hugo gallery pages rebuilt | **no** (not yet) |

B02 web derivatives remain; full B02 gallery publish waits for broader visual review + remaining duplicate checks.

---

## Explicit non-claims

- Not all B01/B02 prints approved  
- Not all 199+168 candidates reviewed  
- Not all samsonov-tp items proven on a notebook page  
- original_page 080–161 still preliminary  
- Full site photo section not restructured  

---

## Next steps

1. Finish visual_review YAMLs for B01 c-001–078 and B02 remainder  
2. Manual bboxes for accepted prints (especially B01 document/photo collages 072–079)  
3. Expand duplicate groups (Colt, GPU, Pravda, bust, studio portraits vs notebook pages)  
4. Optional: improve published binary only if new crop is objectively sharper **and** URL preserved  
5. Grouped Hugo sections after privacy OK  

---

## Update after visual review merge (same day)

### B02 visual review (all 82 pages)
- Pages with archival prints: **19** (1,2,5,7,13,14,22,23,38,67–69,72,74–76,78,80,82)
- Verified crops in manifest: **~36**
- Web-published historical: see `batch-2026-08-01-b02.yaml` (`published_path_ru`)
- Withheld: cemetery m-005; 1983 classmate group m-067; family m-082 (living_people_review)
- Layout-heuristic crops marked `manually_adjusted` — spot-check edges

### B01 visual review
- c-021–050: true prints on **022, 030, 031, 033, 039** (7 prints; 1 manual)
- c-051–078: true prints on **071, 072, 076, 077, 078** (8 prints)
- c-001–020: agent may still be running; c-002 mama already verified
- Accepted auto crops published under `static/photos/archive-b01/`

### Inventory QA
- `INVENTORY_FULL.yaml` merges all 8 range inventories (82 pages)
- High privacy flags on pages 76, 78 (DOB/medical/address) — documents not photo crops

