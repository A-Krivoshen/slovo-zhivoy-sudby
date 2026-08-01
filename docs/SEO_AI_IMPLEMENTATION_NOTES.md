# SEO / AI implementation notes

**Branch:** `task/archive-seo-ai-knowledge-graph`  
**Base audit:** [SEO_AI_ARCHITECTURE_AUDIT.md](./SEO_AI_ARCHITECTURE_AUDIT.md)  
**Relation vocabulary:** [ARCHIVE_RELATION_VOCABULARY.md](./ARCHIVE_RELATION_VOCABULARY.md)

This document records what was built on this branch for discoverability, machine navigation, and a **public** knowledge graph — without private material, without claiming `llms.txt` as an SEO ranking factor.

## Goals

1. Make public archive structure legible to crawlers and AI tools via normal HTML + optional hints.
2. Introduce a **typed entity graph** (YAML) that can later feed related blocks and JSON-LD.
3. Add **integrity checks** so broken photo links and invalid graph edges fail in CI when desired.
4. State **publishing principles** (sources, uncertainty, privacy) on the public site.

## What was built

### 1. Orphan / broken image checker

| Path | Role |
|------|------|
| [`scripts/check_orphan_images.py`](../scripts/check_orphan_images.py) | Scan `content/**/*.md` for `/photos/` refs; scan `static/photos` for `jpg`/`webp` (also `jpeg`/`png`); report **orphans** (static never referenced) and **broken** refs (content points to missing file). |

- Default **exit 0** always (prints summary). Optional **`--fail`** for CI non-zero when broken refs or non-intentional orphans remain.
- **`-thumb` companions** count as covered when the full image (or the thumb) is referenced.
- **Privacy note:** unlinked `str-099`, `str-100`, `str-155`, `str-157` under `dnevnik-tt/` are treated as **intentional** (withheld medal 099–100; living-family internal_privacy 155/157). See privacy reviews in `docs/PRIVACY_REVIEW_B02_*.md`.

```bash
python3 scripts/check_orphan_images.py
python3 scripts/check_orphan_images.py --fail   # CI
```

### 2. Public graph integrity checker

| Path | Role |
|------|------|
| [`scripts/check_graph_integrity.py`](../scripts/check_graph_integrity.py) | Load `data/archive/public/*.yaml`; verify relation subject/object `entity_id`s exist in people/events/places/letters/documents/photos; require **`url_ru` on every public letter**; reject **099–100** entities/tokens in the public graph. |

```bash
python3 scripts/check_graph_integrity.py
```

Exit **0** if clean, **1** if errors (summary always printed).

### 3. Public entity registry (seed graph)

Under [`data/archive/public/`](../data/archive/public/):

| File | Contents |
|------|----------|
| `people.yaml` | Public persons (T.T., parents, siblings, husband, uncertain letter authors, Dzerzhinsky as historical) |
| `places.yaml` | Family / wartime / Crimea places |
| `events.yaml` | War, evacuation, school, Crimea, family, reunions, UK expulsion 1917 |
| `letters.yaml` | Front-letter + postcard entities with required **`url_ru`** |
| `documents.yaml` | Colt, expulsion, Red Banner, GPU badge, Pravda, Stalingrad medal (T.T.) |
| `photos.yaml` | B02 priority prints + key album portraits (no 099/100/155/157 entities) |
| `collections.yaml` | Diary B02, letters-from-front, notebook album, parents’ docs |
| `chapters.yaml` | Manuscript chapters referenced by `mentioned_in` relations |
| `relations.yaml` | Typed edges (`child_of`, `author_of`, `depicted_in`, …) + `confidence` + `public` |

- **Private** tree `data/archive/private/` stays empty of publishable graph data on purpose.
- **No** entities for notebook pages **099–100** (integrity script enforces).
- Predicates follow `docs/ARCHIVE_RELATION_VOCABULARY.md`.
- Integrity also resolves **collections** and **chapters** (relation targets beyond the six primary types).

This seed is **curated and partial** — enough for integrity tooling, related-block wiring, and JSON-LD; not a dump of every prose mention.

### 4. Experimental `llms.txt`

| Path | Role |
|------|------|
| [`static/llms.txt`](../static/llms.txt) | Optional machine navigation: short **EN/RU** site description + **public canonical** section links only. |

Explicitly marked **experimental**; **not** claimed as an SEO ranking factor; **no** private/draft/withheld targets (099–100, 155/157, private notes, draft EN chapters).

Served at site root as `/llms.txt` via Hugo `static/`.

### 5. Publishing principles (public pages)

| Path | Lang | `translationKey` |
|------|------|------------------|
| [`content/ru/printsipy-publikacii.md`](../content/ru/printsipy-publikacii.md) | RU | `publishing-principles` |
| [`content/en/publishing-principles.md`](../content/en/publishing-principles.md) | EN | `publishing-principles` |

Covers: **sources**, **uncertainty**, **privacy** (including intentional unlinked scans). Linked from:

- [`content/ru/o-proekte.md`](../content/ru/o-proekte.md) → `/printsipy-publikacii/`
- [`content/en/about.md`](../content/en/about.md) → `/en/publishing-principles/`

Canonical URLs after build:

- `https://сжс.рф/printsipy-publikacii/`
- `https://сжс.рф/en/publishing-principles/`

## Intentionally not done on this slice

| Item | Reason |
|------|--------|
| Full `/lyudi/`, `/sobytiya/`, `/hronologiya/` entity HTML | Scaffold dirs may exist; page generation is a follow-up |
| JSON-LD Person/Event/Place beyond PaperMod defaults | Needs stable entity pages + graph→template |
| Image sitemap | Separate deliverable |
| Private graph content | Must never ship in `public/` YAML or `llms.txt` |
| Treating `llms.txt` as ranking SEO | Explicitly disclaimed |

## Privacy invariants (do not regress)

- Public graph and `llms.txt` must **not** introduce pages **099–100** (UA medal / Timofey Timofeevich attribution).
- **155 / 157** may exist as files under `static/photos/dnevnik-tt/` but should stay **unlinked** in content unless a new privacy review says otherwise.
- Living people: year + relationship in public text; see site privacy pages.

## Suggested CI / local QA

```bash
python3 scripts/check_graph_integrity.py
python3 scripts/check_orphan_images.py --fail   # after intentional orphans are accepted or fixed
hugo --gc --minify                              # existing build check
```

## Follow-ups

1. Expand public YAML as new entity pages ship; keep integrity script green.
2. Wire relations into “related” HTML blocks and matching JSON-LD.
3. Decide whether remaining photo orphans (gallery crops, thumbs, album-only files) need content links or explicit allow-lists.
4. Revisit `llms.txt` only if a stable community convention emerges — keep experimental label.

## File index (this implementation)

```
scripts/check_orphan_images.py
scripts/check_graph_integrity.py
data/archive/public/people.yaml
data/archive/public/places.yaml
data/archive/public/events.yaml
data/archive/public/letters.yaml
data/archive/public/documents.yaml
data/archive/public/photos.yaml
data/archive/public/collections.yaml
data/archive/public/chapters.yaml
data/archive/public/relations.yaml
static/llms.txt
content/ru/printsipy-publikacii.md
content/en/publishing-principles.md
content/ru/o-proekte.md          # link added
content/en/about.md              # link added
docs/SEO_AI_IMPLEMENTATION_NOTES.md
```
