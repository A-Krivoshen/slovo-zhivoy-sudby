# Final editorial audit — 2026-08

Branch: `task/final-archive-editorial-fixes-2026-08`  
Base HEAD at start of this pass: `4543848` (medal withhold already committed).

## Goals (this stage)

1. Continuity of public manuscript text (joins vs true losses).
2. Remove mid-narrative “kitchen” indexes.
3. Chapter order (`weight`) + explicit prev/next navigation.
4. Archive-friendly post meta (not blog event date).
5. Terminology: «рукописная тетрадь» on the home page.
6. Photo album visitor UI without file-path residue.
7. Pravda 1929 date = album caption **20 July** (`source_caption_only`).
8. Ukrainian 1999 medal remains **Uncle Tyoma**, withheld from T.P. materials.
9. B02 chapters 080–098 published structure preserved; 099–100 withheld.

## Continuity

See `docs/TEXT_CONTINUITY_AUDIT.md`.

## Structure

| Item | Status |
|------|--------|
| `weight` 5…120 on diary intro + chapters 00–11 | done RU/EN |
| Footer nav «← prev · contents · next →» | done RU/EN |
| Mid-chapter People/Places tables | moved / `<details>` |
| `layouts/_partials/post_meta.html` | manuscript shows original_page + status + «опубликовано» |

## Ukrainian medal 1999

| Field | Value |
|-------|--------|
| original_page | 099–100 (B02 m-020–021) |
| document_id | `doc-b02-medal-zahysnyku-vitichyzny` |
| photo_id | `pub-photos__dnevnik-tt__str-099`, `…str-100` |
| person_confirmed | Самсонов Тимофей Тимофеевич |
| not_this_person | Самсонов Тимофей Петрович |
| review_status | `withheld_pending_person_page` |
| On T.P. bio / album / documents | **0** |

## Pravda 1929

Public wording: **20 июля 1929** by album caption (`data/fact_conflicts.yaml` → `pravda-dzerzhinsky-1929-date`, `source_caption_only`).

## Photo album (T.P.)

Removed visitor-facing `**File:**`, `static/photos/…`, `inbox/…`, public Google Photos line. Kept image URLs stable.

## B02 status

| Range | Site |
|-------|------|
| 080–089 | chapter 10 (content file present) |
| 090–098 | chapter 11 published narrative |
| 099–100 | withheld (medal, Uncle Tyoma) |
| 101–161 | inventory / not yet as chapters |

## RU/EN parity

Continuity, weights, nav, medal note, Pravda captions: synchronized for touched pairs.

## Not fully done in this pass (follow-up)

- Dual view UI «Связный текст / По строкам» (documented preference; public text is reading-friendly joins only).
- Full photo crop pipeline expansion for all B02 leaves.
- Push + GitHub Pages (requires explicit deploy).
- Commit of large `static/photos/dnevnik-tt/str-080…161` set (size/review).
