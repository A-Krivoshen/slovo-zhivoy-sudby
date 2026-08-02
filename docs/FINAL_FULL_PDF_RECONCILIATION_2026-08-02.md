# Final full PDF reconciliation — 2026-08-02

## Starting point

| Item | Value |
|------|--------|
| Initial `main` HEAD | `ba15cf61b7428e384130a2ae49b8e529bda821db` |
| Backup tag | `backup-before-final-pdf-reconcile-2026-08-02` |
| PDF path | `inbox/scans/memoirs/_raw/nasha_rodoslovnaya_samsonovy_full_archive_160_pages_download.pdf` |
| PDF SHA-256 | `84567946dea430b16249fbabc63bcbafa944c51ea659bc685de3a7bfbf9657d5` |
| Physical pages | **160** |
| Archival range | original_page **001–161** (068 omitted from cleaned PDF) |
| Working tree at start | clean, on `main` = `origin/main` |

## PDF mapping (canonical)

| Physical PDF | original_page |
|--------------|---------------|
| 001–067 | 001–067 |
| 068–078 | 069–079 |
| *(absent)* | 068 = inverted duplicate of 067 |
| 079–160 | 080–161 |

Visual sample of all 160 pages (72 DPI) under `/tmp/szhs-final-pdf-audit/pages/`.  
Critical pages re-checked at higher DPI (e.g. 050, 105–110).

### PDF problems / unresolved

| Item | Status |
|------|--------|
| Mapping vs site chapter markers | **OK** — no renumbering needed |
| original 068 | Correctly omitted; not reintroduced |
| Flat number on original 050 | **Fixed**: manuscript `№223` (was site `№23`) |
| 099–100 UA medal | Confirmed **T. T. Samsonov**; remains **internal** |
| 108 Stalingrad form | Confirmed **T. Timofeevich**, presentation **23.09.1943** |
| 103–104 Dmitry | Surname unknown — kept |
| 105–107 Timosha | Not auto-merged with “Tyoma” nickname alone |
| 128–129 Friolenko | Comrade, not brother |
| 101/102 | Same exam photo; 102 alternate |
| 155/157 | Privacy — not public |
| Dates 104 / 107 / 108 | 28.VII.44 / 13.07.44 / 23.09.1943 — retained |

## Coverage matrix

Updated: `docs/COVERAGE_MATRIX_001_161.csv` (new honest columns).

| final_status | count |
|--------------|------:|
| complete_public | 155 |
| complete_internal_privacy | 4 (099, 100, 155, 157) |
| alternate_scan | 1 (102) |
| duplicate | 1 (068) |

## RU fixes

| Fix | Detail |
|-----|--------|
| Flat **№223** | Ch.03 reader (PDF visual confirm) |
| Typo «и ,» | Ch.13 (two places) |
| Ch.09 meta | Alexandrovsky Central deferred to next chapter |
| Hub weights | Legacy hubs → weight 900/901 (out of prev/next chain) |
| Sitemap | `robotsNoIndex` hubs excluded; hubs `sitemap.disable: true` |
| translation_status | Chapters 12–19 marked complete where EN pairs published |
| Privacy policy | Historical 1930s addresses (incl. 223 / entrance 12) documented as past, not current living |

Retained uncertainty: manuscript `[?]`, struck-through phrases, author speech not modernized.

## EN fixes

| Item | Action |
|------|--------|
| Diary **12–19** | Full English reader pages; **`draft: false`** |
| Postcard 130 | New EN document page |
| Insert 089–090 | New EN document page |
| Letters index | Rows for insert + postcard; EN chapter links |
| Flat No. **223** | EN ch.03 aligned with PDF |
| Ch.09 description | Alexandrovsky Central not claimed for 072–079 |
| Diary TOC | Full 00–19 listing |

Diplomatic Russian in EN letter pages remains only as **source transcription** in fenced blocks (standard archival practice). Reader narrative is English.

EN diary chapters 12–19 previously contained Russian body dumps as drafts; those dumps are **not** published.

## Letters / documents

| Leaf | Public URL (RU) | Notes |
|------|-----------------|-------|
| 089–090 | `/dokumenty/pisma-s-fronta/pismo-vstavka-sestre-089-090/` | Insert; damaged edges |
| 103 | `…/pismo-103-1943/` | Dmitry, 11.08.43 |
| 104 | `…/pismo-104/` | Dmitry, 28.VII.44 |
| 105–106 | `…/pismo-105-106-mamochke/` | Timosha → mother |
| 107 | `…/pismo-107/` | Timosha; “Sasha” ≠ husband |
| 108 | `/dokumenty/udostoverenie-oborona-stalingrada-samsonov-tt/` | T.T. only |
| 128–129 | Friolenko | Comrade |
| 130 | postcard | Year/sender need verify |
| 131–133 | Gennady | As published |

## Photos

- **No new crops** in this pass.
- Matched existing public crops; captions left where already correct.
- **Removed from `static/`** (and git): `str-099`, `str-100`, `str-155`, `str-157` (direct-URL residual risk).
- Alternate: 102 of 101.
- missing_photo_candidates: none requiring new public cards this pass (private leaves recorded as privacy, not empty cards).

## Graph

- `scripts/check_graph_integrity.py` → **OK**
- Attribution rules (Dmitry, Timosha, Friolenko, Stalingrad T.T., Sasha husband vs letter 107) unchanged and re-verified.

## Privacy

| Check | Result |
|-------|--------|
| 099–100 public content | None |
| 155/157 public embeds | None |
| Private static scans | Removed from deploy tree |
| Living full DOB | Not reintroduced |
| Status blocks in visitor HTML | Not rendered (post_meta whitelist) |

## SEO / AI

- Production build: `hugo --minify` without drafts
- hreflang for diary 12–19 now pairs RU↔EN
- Sitemap excludes noindex hubs
- `llms.txt` / `ai.txt` present; no private photo URLs
- SearchAction retained with working search template
- Residual Cyrillic on EN: medal names in parentheses / source quotes only (low volume)

## UX / a11y (this pass)

- No viewport re-run of full 9-device matrix (prior audit: `docs/RESPONSIVE_DEVICE_AUDIT.md` still baseline)
- Skip link, lightbox assets unchanged
- Hub prev/next interference reduced via weights

## Tests / build

```
hugo --minify   # OK — RU 279 pages, EN 267 pages
python3 scripts/check_graph_integrity.py  # OK
python3 scripts/check_orphan_images.py    # OK exit 0; privacy paths gone from disk
```

## Remaining uncertainty (honest)

- Some manuscript `[?]` readings (e.g. *ital’yanki*, place names)
- Postcard 130 sender/year
- Insert 089–090 signature on cut edge
- Dmitry surname (103–104)
- EN long chapters are **reader-quality translations** of published RU readers; full line-by-line diplomatic EN of every leaf is not duplicated (RU retains diplomatic blocks)
- Orphan static full-page scans 156/158–161 still unlinked (not private flags; optional later album work — **no re-crop**)
- Some alias pages still have 0/2 H1 from legacy aliases (pre-existing)

## Git

| Item | Value |
|------|--------|
| Final `main` HEAD | `789d830a57b9b83c768e27399797370d85aeefdd` |
| Push | `origin/main` updated `ba15cf6..789d830` (one push after local commits) |
| Pages | Deploy Hugo site to Pages run **success** (SHA `789d830…`) |
| Force push | **Not used** |
| Branches removed | `task/archive-seo-ai-knowledge-graph`, `task/b02-editorial-coverage-fix`, `task/final-archive-editorial-fixes-2026-08` (all ancestors of main) |
| Backup tag kept | `backup-before-final-pdf-reconcile-2026-08-02` |
| Production smoke | https://сжс.рф — key URLs **200**; private str-099/155 **404**; flat **№223** live |

## Repository size (no history rewrite)

Measured after work (see shell): `.git` size, object counts, top blobs — report in final push section if needed. No filter-repo / BFG.
