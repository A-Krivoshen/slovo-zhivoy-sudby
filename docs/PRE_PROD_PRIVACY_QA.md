# Pre-production privacy QA

**Branch:** `task/archive-seo-ai-knowledge-graph`  
**Date:** 2026-08-01  
**Scope:** Public Hugo content (`content/**`), public knowledge graph (`data/archive/public/**`), experimental `llms.txt`, and built `public/` search/sitemap surfaces where present.  
**Out of scope for FAIL:** Private static JPEGs remaining on disk if unlinked; internal indices under `data/archive_photos/`, `data/manuscript_batches/`, `inbox/`, `docs/` (non-visitor).  
**Related prior pass:** `docs/PRIVACY_GRAPH_LEAK_CHECK.md`

## Overall verdict

| Result | Detail |
|--------|--------|
| **PASS** | All six pre-prod checklist items pass. **No content or graph fixes required** in this recheck. |

---

## Checklist (pass / fail)

| # | Check | Result | Evidence |
|---|--------|--------|----------|
| 1 | No **099–100** public content pages or graph entities as public | **PASS** | No `str-099` / `str-100` in `content/**` or `data/archive/public/**`. No public document entity for Ukrainian medal «Захиснику Вітчизни» / series `МН 178440`. `documents.yaml` explicitly forbids 099–100 as public entities. Tyoma person note: Stalingrad only; “UA medal leaves withheld.” |
| 2 | No **str-155**, **str-157** in foto public pages (as published assets) | **PASS** | Zero `figure` / `src` hits for `str-155.jpg` / `str-157.jpg` in `content/**` and built `public/**/*.html`. RU/EN gallery pages mention 155/157 only as **not shown** until family decision. EN diary ch. 18 uses HTML comments: full-page scan not published (living-person photo privacy). `data/archive/public/photos.yaml` excludes pages 099, 100, 155, 157. |
| 3 | No **№ 226**, **17 подъезде** (current living) in reader chapters | **PASS** | Zero hits for `№ 226`, `17 подъезде`, and related “still lives in entrance…” patterns in `content/**` and built HTML. RU ch. 13 and EN ch. 13 use redactions: street kept; entrance/flat hidden; current entrance + degree generalized. |
| 4 | `people.yaml` and `relations.yaml` — no private exports | **PASS** | Only public-safe people (no living sons as entities). No address / apartment / phone / full living DOB fields. Relations are public typed links only (family, letters, medals Stalingrad, events, photos). Private tree marker: `data/archive/private/NOTE.yaml` only. |
| 5 | `llms.txt` — no private URLs | **PASS** | **Source** `static/llms.txt`: public section links only; 099–100 / 155–157 listed under “Out of scope” **without** paths to `/photos/dnevnik-tt/…`. **Built** `public/llms.txt` (PaperMod home output): auto list of published pages; no `str-099/100/155/157` image URLs. Chapter slug `…090-099` is the public Genya/Tyoma reader chapter, not private medal scans. |
| 6 | Apartment numbers on **lyudi** / **sobytiya** pages | **PASS** | No `кв.` / `квартир` / `подъезд` / `apartment` / `entrance N` / flat numbers in `content/ru/lyudi`, `content/en/people`, `content/ru/sobytiya`, `content/en/events`. Only non-apartment uses (e.g. school № 74, city names). Place pages state policy: no apartment/entrance numbers on open place pages. |

---

## Per-check detail

### 1. Pages 099–100 (Ukrainian medal)

| Surface | Status |
|---------|--------|
| `content/**` `str-099` / `str-100` / medal title / series number | **0** |
| Public document page | **None** |
| `data/archive/public/documents.yaml` entity | **Absent** (header comment forbids) |
| `data/archive/public/people.yaml` | Tyoma: Stalingrad only |
| `data/archive/public/photos.yaml` | Excluded by registry comment; no `source_page: 99\|100` |
| Built `public/index.json` / sitemaps image refs | **0** for private str-099/100 |

**Residual (not FAIL):** JPEGs still at `static/photos/dnevnik-tt/str-099.jpg` and `str-100.jpg` (unlinked). Direct URL theoretically fetchable if known. Optional later: remove from `static/` or block at CDN.

### 2. str-155 / str-157 (living-person photo privacy)

| Surface | Status |
|---------|--------|
| `content/**` figure `str-155.jpg` / `str-157.jpg` | **0** |
| RU `foto/tetrad-semya-prodolzhenie.md` | Note only: not shown |
| EN `photos/notebook-family-continued.md` | Same |
| EN `memoirs/diary/18-sons-150-161.md` | Comments at p.155 / p.157; no figures |
| RU `vospominaniya/dnevnik/19-semya-i-deti.md` | No 155/157 figures (prior policy) |
| Public graph photos | Not listed |
| Built HTML | **0** image refs |

**Residual (not FAIL):** Unlinked files `static/photos/dnevnik-tt/str-155.jpg`, `str-157.jpg`; internal paths in `data/archive_photos/*` only.

### 3. Current living address / entrance (№ 226, 17-й подъезд)

| Pattern | `content/**` |
|---------|----------------|
| `№ 226` / apt 226 | **0** |
| `17 подъезде` (current living) | **0** |
| Redacted Serafimovich move (RU + EN ch. 13) | Present as policy text |

Aligned with `docs/PRIVACY_REVIEW_B02_ALL_CHAPTERS.md` and prior EN fix in `docs/PRIVACY_GRAPH_LEAK_CHECK.md`.

### 4. Public graph exports (`people.yaml`, `relations.yaml`)

| Requirement | Status |
|-------------|--------|
| No living sons as public people entities | **PASS** (absent) |
| No 099–100 medal / document entity | **PASS** |
| No str-155/157 photo entities | **PASS** |
| No apartment / current address fields | **PASS** |
| Relations only among public entities | **PASS** |
| Private data not under `data/archive/public/` | **PASS** (`private/NOTE.yaml` only) |

### 5. llms.txt

| File | Private image/page URLs? |
|------|---------------------------|
| `static/llms.txt` | **No** — privacy notes without URLs |
| `public/llms.txt` (PaperMod `LLMs` output) | **No** — published page list only |

Note: built `public/llms.txt` **differs** from curated `static/llms.txt` (Hugo output format wins on build). Neither leaks private photo URLs. Before deploy, confirm which file is served at `/llms.txt` after a clean `hugo` build.

### 6. lyudi / sobytiya apartment sweep

| Path | Apartment / entrance numbers |
|------|------------------------------|
| `content/ru/lyudi/**` | **None** |
| `content/en/people/**` | **None** |
| `content/ru/sobytiya/**` | **None** (school № only) |
| `content/en/events/**` | **None** |

---

## Additional surfaces checked (supporting)

| Surface | Result |
|---------|--------|
| Built `public/**/*.html` for 226 / 17 подъезд / str-155/157/099/100 | **0** |
| `public/index.json` (search index) for same patterns | **0** |
| Sitemaps image locs for private str-scans | **0** |
| Living-person full DOB reintroduced in reader sons chapters | **PASS** — year-only births (1948 / 1957 / 1981 / 1990); author/parents full dates allowed as deceased/historical |

---

## Historical context kept by policy (not FAIL)

Prior editorial policy keeps **historical** childhood / wartime addresses separately from **current living** redactions:

| Item | Where | Policy |
|------|--------|--------|
| Entrance 12, **кв. 223** (1930s House on the Embankment) | Diary ch. 02, wartime letter 105–106, some 1938 photo captions | Historical manuscript / document address — not “current living” |
| Childhood entrances of classmates (10-й, 13-й, club 3-й, etc.) | Reader chapters | Past-tense narrative |
| Serafimovich **street** without flat | Ch. 13 redaction, place pages | Street OK; flat/entrance hidden for sensitive lines |

Inconsistency (document only, not checklist FAIL): RU ch. 18 caption uses `[кв. скрыто]` for 223 while gallery figure caption still quotes manuscript “кв. 223, 12 подъезд” (1938). Family may later align captions; not required for this pre-prod checklist.

---

## Fixes applied this recheck

**None.** All checklist items already clean after prior privacy passes (EN ch. 13 address redaction; EN ch. 18 removal of 155/157 figures).

---

## Residual risk (optional hardening, not FAIL)

1. Direct GET to unlinked static scans if URL is known: `str-099`, `str-100`, `str-155`, `str-157` under `static/photos/dnevnik-tt/`.
2. Handwritten full dates may remain visible **on** other published page-scan images — separate crop/blur decision.
3. EN sons chapter may remain `draft: true`; privacy figures already withheld so undraft does not re-publish 155/157.
4. If agents add entities under `data/archive/public/`, re-run greps below.
5. Confirm post-build which `llms.txt` is deployed (static vs PaperMod output).

---

## Re-run commands

```bash
# Checklist cores
rg -n 'str-155\.jpg|str-157\.jpg|str-099\.jpg|str-100\.jpg|№\s*226|17\s*подъезд|МН\s*178440|Захисник' \
  content layouts data/archive/public static/llms.txt

# Graph
rg -n 'entity_id|155|157|099|100|apartment|квартир|подъезд|withheld|zahys' data/archive/public

# People / events hubs
rg -n 'кв\.|квартир|подъезд|apartment|entrance [0-9]|flat [0-9]' \
  content/ru/lyudi content/en/people content/ru/sobytiya content/en/events

# Built (after hugo)
rg -n 'str-155\.jpg|str-157\.jpg|str-099\.jpg|str-100\.jpg|№\s*226|17\s*подъезд' \
  public --glob '*.{html,xml,json,txt}'
```

---

## Sign-off

| Item | Status |
|------|--------|
| 099–100 public content / graph | **PASS** |
| str-155 / str-157 in public foto | **PASS** |
| № 226 / 17 подъезде current living | **PASS** |
| people.yaml / relations private exports | **PASS** |
| llms.txt private URLs | **PASS** |
| Apartment numbers on lyudi/sobytiya | **PASS** |
| **Overall pre-prod privacy** | **PASS** |

No commit created (per task instruction).
