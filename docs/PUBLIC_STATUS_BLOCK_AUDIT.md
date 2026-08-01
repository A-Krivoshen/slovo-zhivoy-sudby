# Public status-block audit (2026-08-01)

## Goal

Remove visitor-facing verification / pipeline status from HTML. Keep internal fields in front matter and `data/`.

## Classification of matches

| Pattern | Class | Action |
|---------|-------|--------|
| `archive_note type="status"` in chapters | public_remove | **Deleted** (8 blocks) |
| Front matter `transcription_status`, `batch_id`, `editorial_status` | internal_front_matter_keep | Kept (not rendered) |
| `data/*.yaml` medal / batch IDs | internal_docs_keep | Kept |
| `docs/*` audits | internal_docs_keep | Kept |
| Manuscript `[?]` markers | source_text_keep | Kept (reader-facing uncertainty) |
| Brother name Tyoma/Zhenya note | source_text_keep | Kept (helps reading) |
| Medal withhold long note on ch.11 | public_remove | **Deleted** (internal registry only) |
| `caption="original_page NNN:…"` | public_remove | **Humanized** |
| `archive_source` … original_page | public_remove | Shortcode now says «стр. / pages» |
| post_meta `first_pass` / `original_page` | public_remove | Meta shows «Стр. N–M · опубликовано» only |

## B02 chapters after cleanup

### RU/EN 10 (080–089)
- Human intro; no status box
- Captions without `original_page`
- Front matter statuses remain internal

### RU/EN 11 (090–098)
- Human intro about Genya / Tyoma
- **No** public medal/withhold block
- Medal still in `data/archive_photos/index.yaml` + fact_conflicts + manuscript batch yaml

## Index one-liner (allowed once)

RU diary `_index.md`: family-scans note without codes.  
EN diary `_index.md`: same.

## Shortcode changes

- `archive_note`: status type no longer labels «Статус проверки» (and no status usages left in content)
- `archive_source`: «Рукописная тетрадь …, стр. …» / “Handwritten notebook …, pages …”
