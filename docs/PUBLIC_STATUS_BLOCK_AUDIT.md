# Public status-block and kitchen jargon audit

**Date:** 2026-08-01  
**Branch:** `task/public-content-cleanup-final-2026-08`  
**Base HEAD:** `4888350` then cleanup commit on top

## Classification rules

| Class | Meaning |
|-------|---------|
| `internal_front_matter_keep` | e.g. `transcription_status`, `batch_id` in YAML — not rendered |
| `internal_docs_keep` | `data/*`, `docs/*` manifests |
| `public_remove` | visitor HTML / captions / body labels |
| `source_text_keep` | author voice, `[?]`, names |

## Public removals completed

1. All `archive_note type="status"` blocks (0 remaining in content).
2. Shortcode `archive_note`: no visitor label «Статус проверки».
3. Shortcode `archive_source`: human «стр.» / «pages», not `original_page`.
4. `post_meta`: notebook pages + published date only (no first_pass).
5. Medal 099–100: no public withhold block; internal registry kept.
6. Captions: no `original_page NNN:` prefix.
7. EN B02 chapters: removed «Diplomatic reading … (first pass)» → «Text of the notebook page (Russian)».
8. Index RU/EN: one human note about scans and brackets.

## Control (public HTML after build)

Target counts **0** for:

- Статус проверки, first_pass, pass2, merged_page, manuscript-2026
- original_page, withheld, review_status, scan_id, photo_id, document_id
- batch_id, offline-batch, inbox/, static/photos/
- Diplomatic reading, first pass, Захиснику (on TP pages)

## Allowed public wording

- Index: family scans / square brackets note (once)
- «стр. N» / «p. N» as human page markers where needed
- Brother name Tyoma/Zhenya explanation
- `[?]` / `[неразборчиво]` / `[illegible]`

## Medal (internal)

- `data/archive_photos/index.yaml`, `data/fact_conflicts.yaml`, `data/manuscript_batches/2026-08-01.yaml`
- person_confirmed: Самсонов Тимофей Тимофеевич
- not_this_person: Самсонов Тимофей Петрович
- review_status: withheld_pending_person_page
