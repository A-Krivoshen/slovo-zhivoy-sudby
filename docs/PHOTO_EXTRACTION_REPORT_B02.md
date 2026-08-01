# Photo extraction report — batch B02 (2026-08-01)

**Status:** partial — full inventory + first verified crops; **not** “all photos extracted”.

## Source

| Field | Value |
| --- | --- |
| PDF | `inbox/scans/memoirs/_raw/samsonovy_new_scans_2026-08-01_corrected.pdf` |
| SHA-256 | `66f69122cc6e0adac3083fb1c3b2833db8a85c9d5952c692f125188f114d424d` |
| Pages | 82 |
| Extraction | `pdfimages -j` — one native JPEG per page |
| Resolution | **2480 × 3507 @ 300 DPI** (no re-encode master) |
| batch_id | `manuscript-2026-08-01-b02` |
| Branch | `task/extract-archive-photos-b02` |

Heavy masters/crops stay under `inbox/scans/memoirs/batch_b02/` (gitignored).

## Inventory (Stage A)

| Metric | Count |
| --- | --- |
| Pages processed | 82 |
| Pages with auto candidates | 52 |
| Auto candidates (assistive only) | **168** |
| Numbered overlays | 82 (`overlays/m-NNN-overlay.jpg`) |
| Page previews | 82 (`page_previews/`) |
| Contact sheets | `contact_sheets/` |

Detector: `scripts/photo_detect_b02.py` (paper-distance + morphology + stack/side split).  
**Auto does not approve.** False positives common on dense handwriting (e.g. m-003/004/008/015). False negatives possible (e.g. m-007 initially missed).

## Visual review (Stage B)

| Metric | Count |
| --- | --- |
| Visually verified / manually adjusted (first block) | **7** |
| Web-published (privacy OK) | **5** |
| Withheld (`living_people_review`) | **2** (m-005 cemetery groups) |
| Remaining candidates unreviewed | ~160+ |

First verified `photo_id`s:

| photo_id | page | type | privacy | notes |
| --- | --- | --- | --- | --- |
| b02-mp001-ph01 | 001→080 | group_photo | public_historical | Dzerzhinsky / Papa caption |
| b02-mp001-ph02 | 001→080 | group_photo | public_historical | Funeral crowd |
| b02-mp002-ph01 | 002→081 | archival_photo | public_historical | Alexandrovsky Central; view rot 180° |
| b02-mp005-ph01 | 005→084 | group_photo | living_people_review | archive only |
| b02-mp005-ph02 | 005→084 | group_photo | living_people_review | archive only |
| b02-mp007-ph01 | 007→086 | group_photo | public_historical | Guests at Povstukha (left) |
| b02-mp007-ph02 | 007→086 | group_photo | public_historical | Guests (right); split refined |

Parallel visual review agents: ranges 001–020, 021–040, 041–060, 061–082 → `reports/visual_review_*.yaml` (in progress).

## Crops

Per verified photo:

- `crops/master/*-master.png` — lossless archival
- `crops/view/*-view.jpg` — viewing (local rotation applied when needed)
- `crops/context/*-context.jpg` — print + author caption
- `page_overview/m-NNN-overview.jpg`

Web: `static/photos/archive-b02/{photo_id}.jpg` + `-thumb.jpg` (max edge 1600, no upscale, EXIF stripped).

## Metadata

- Manifest: `data/archive_photos/batch-2026-08-01-b02.yaml`
- Verified review list: `inbox/.../reports/photo_review_verified.yaml`
- Auto inventory: `inbox/.../reports/photo_candidates_inventory.yaml`
- Validate: `scripts/validate_photo_manifest_b02.py`

Identity rule: only author captions; no face-based ID.

## Publication

- **Not** creating one Hugo article per photo yet.
- Web files ready for 5 historical photos; no diary/menu/URL rebuild.
- Cemetery m-005 withheld until family privacy decision.
- Existing diary page images `str-080…` remain full-page scans (separate track).

## Validation

- Manifest script: OK (run after each update)
- Large masters **not** in git
- No generative fill / face enhance / colorization

## Next

1. Merge subagent visual reviews for 001–082  
2. Manually adjust bboxes for accepted prints  
3. Crop + privacy gate  
4. Grouped Hugo galleries only for `publishable`  
5. Link duplicates to existing `static/photos/samsonov-tp/` where same print already published  

## Explicit non-claims

- Not all 82 pages fully photo-extracted  
- Not all 168 candidates reviewed  
- Not all captions transcribed  
- Full-site photo gallery not complete  
