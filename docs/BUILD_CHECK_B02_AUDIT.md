# BUILD_CHECK_B02_AUDIT

**Date:** 2026-08-01  
**Agent role:** build consistency / Hugo validate while other agents edit  
**Repo:** `/home/slon/Work/SZHS`  
**Git commit:** not performed (per instructions)

---

## 1. Environment

| Item | Value |
|------|--------|
| Hugo | `hugo v0.164.0+extended` (snap: `/snap/bin/hugo`) |
| BuildDate | 2026-07-06T16:39:30Z |
| OS | linux/amd64 |
| Command | `hugo --gc --minify` (repo root) |
| Final build exit | **0 (success)** |
| Final build time | ~261 ms |

Hugo is installed and usable; no need for nix/alternate install.

---

## 2. `hugo.toml` — languages & taxonomies

### Languages

| Key | Lang | `contentDir` | default | weight | label |
|-----|------|--------------|---------|--------|-------|
| `languages.ru` | ru-RU | `content/ru` | **yes** (`defaultContentLanguage = 'ru'`) | 1 | Русский |
| `languages.en` | en-US | `content/en` | no (`defaultContentLanguageInSubdir = false`) | 2 | English |

RU serves at site root; EN under `/en/`.

### Taxonomies

```toml
[taxonomies]
  tag = 'tags'
  category = 'categories'
  person = 'people'
```

Menus align with sections:

- **RU:** `/vospominaniya/`, `/roditeli/`, `/istoriya/`, `/mesta/`, `/foto/`, `/dokumenty/`, …
- **EN:** `/en/memoirs/`, `/en/parents/`, `/en/history/`, `/en/places/`, `/en/photos/`, `/en/documents/`, …

---

## 3. Content inventory (final snapshot ~21:34 MSK)

**Total Markdown under `content/ru` + `content/en`: 109**

| Section | RU | EN |
|---------|----|----|
| root pages | 5 | 5 |
| diary / dnevnik (+ indexes/about) | 21 in `vospominaniya/dnevnik` | 21 in `memoirs/diary` |
| vospominaniya / memoirs (incl. diary + templates) | 24 | 24 |
| dokumenty / documents | **16** (incl. `pisma-s-fronta/*`) | **7** |
| roditeli / parents | 5 | 5 |
| istoriya / history | 3 | 3 |
| foto / photos | 4 | 4 |
| mesta / places | 2 | 2 |

### 3.1 Diary (`dnevnik` / `diary`) — complete chapter set

Both languages have chapters **00–18** plus `_index.md` and about-notebook page:

**RU `content/ru/vospominaniya/dnevnik/`**

- `00-oblozhka-i-rodoslovnye.md` … `18-synovya-150-161.md`
- `_index.md`, `o-tetradi.md`

**EN `content/en/memoirs/diary/`**

- `00-cover-and-charts.md` … `18-sons-150-161.md`
- `_index.md`, `about-the-notebook.md`

### 3.2 Dokumenty / documents (post wait — concurrent agents added pages)

**RU**

- Core: `_index.md`, `orden-krasnogo-znameni-samsonov.md`, `pravda-o-dzerzhinskom-1929.md`, `udostoverenie-kolt-1919.md`, `vysylka-velikobritaniya-1917.md`, `znak-gpu-samsonov.md`
- **New (B02):** `udostoverenie-oborona-stalingrada-samsonov-tt.md`
- **New subsection:** `pisma-s-fronta/` (`_index.md` + 8 letter pages: 103, 104, 105–106, 107, 128–129, 131, 132, 133)

**EN**

- Core + `stalingrad-defense-medal-samsonov-tt.md`
- `letters-from-the-front/` exists as **empty directory** (no `_index.md`, no letter pages yet)

**Asymmetry:** RU 192 pages vs EN 172 pages in final Hugo stats — largely from RU-only front letters.

Cover for Stalingrad medal page: `/photos/dnevnik-tt/str-108.jpg` — **present** under `static/`.

---

## 4. Hugo build results

### Final run

```
Pages            │ RU 192 │ EN 172
Paginator pages  │ RU   9 │ EN   7
Static files     │ 203
Aliases          │ RU  67 │ EN  61
Total in 261 ms
EXIT: 0
```

### Errors related to new pages

**None.** New diary chapters 12–18, Stalingrad medal doc, and RU front-letter pages all built without fatal errors.

### Warnings (theme deprecations only)

```
WARN  deprecated: .Language.LanguageDirection → use .Language.Direction
WARN  deprecated: .Language.LanguageCode → use .Language.Locale
WARN  deprecated: .Language.LanguageName → use .Language.Label
```

Source: PaperMod / theme usage, not content. Non-blocking.

### Fixes applied by this agent

**None.** Build did not fail; per instructions only broken front matter / bad links that **cause build failure** were in scope. Concurrent agents still own large content tasks.

---

## 5. Front matter issues

### 5.1 Double-nested `categories` (known issue)

**Problem:** `categories: [["Воспоминания"]]` instead of `categories: ["Воспоминания"]`.

Hugo still builds; taxonomy folder stays `public/categories/воспоминания/` (no bracket-named term observed). Still incorrect YAML and inconsistent with other chapters.

| Status | Files |
|--------|--------|
| **Still broken (RU ch. 12–18)** | `content/ru/vospominaniya/dnevnik/12-brat-front-103-108.md` |
| | `…/13-shkola-druzya-109-119.md` |
| | `…/14-voyna-evakuaciya-120-127.md` |
| | `…/15-pisma-voennye-128-133.md` |
| | `…/16-druzya-pobeda-134-139.md` |
| | `…/17-krym-semya-140-149.md` |
| | `…/18-synovya-150-161.md` |
| **EN ch. 12–18** | **Fixed** during session (were `[["Memoirs"]]`, now clean) |
| **Older diary 00–11 + about** | Correct: `["Воспоминания"]` / `["Memoirs"]` |

**Recommended one-line fix (not applied here):**

```yaml
categories: ["Воспоминания"]
```

### 5.2 Other front matter notes (non-fatal)

| Issue | Files | Notes |
|-------|--------|--------|
| Missing `date` | `archives.md`, `search.md` (both langs), `o-proekte.md`, `about.md` | Pre-existing; Hugo OK |
| `draft: true` | `_shablon-zapisi.md`, `_template-entry.md` | Intentional templates |
| Editorial FM fields | many diary pages | `transcription_status`, `batch_id`, etc. — see §6 |

`translationKey` pairing: **50 keys, 0 unpaired** at last full scan (before late RU-only letter pages; new RU letters may add unpaired keys until EN mirrors exist).

---

## 6. Forbidden public jargon scan

Terms: `first_pass`, `batch_id`, `withheld_pending`, `original_page`

### Body (after second `---`)

| Term | Hits in body |
|------|----------------|
| `first_pass` | **0** |
| `batch_id` | **0** |
| `withheld_pending` | **0** |
| `original_page` | **0** |

**Result: clean.** No forbidden jargon in public page bodies.

### Front matter only (expected editorial metadata)

| Term | Approx. FM occurrences |
|------|-------------------------|
| `first_pass` (as `transcription_status` value) | ~30 |
| `batch_id` | ~18 (`"manuscript-2026-08-01-b02"`) |
| `withheld_pending` | 0 |
| `original_page` | 0 |

### Layout safety

`layouts/_partials/post_meta.html` explicitly **does not render** `transcription_status`, `batch_id`, or `original_page`. Visitor meta uses only human page range (`source_pages_original`) and publish date for `source_type: manuscript`.

`layouts/shortcodes/archive_source.html` documents: never emit field names like `original_page`.

---

## 7. Site consistency notes (non-blocking)

1. **RU/EN dokumenty imbalance** — RU has `pisma-s-fronta` (9 md files); EN has empty `letters-from-the-front/`. Other agents likely mid-task.
2. **Double-nested RU categories** on diary 12–18 — fix when safe (see §5.1).
3. **Page-count drift during audit** — prep saw ~49+49; mid-wait 50+50; final 109 md with concurrent letter/doc additions. Re-run Hugo after major content landings.
4. **Theme deprecation warnings** — PaperMod `.Language.Language*` APIs; cleanup optional.

---

## 8. Full file lists (final)

### `content/ru` (59 files)

```
content/ru/_index.md
content/ru/archives.md
content/ru/konfidencialnost.md
content/ru/o-proekte.md
content/ru/search.md
content/ru/dokumenty/_index.md
content/ru/dokumenty/orden-krasnogo-znameni-samsonov.md
content/ru/dokumenty/pisma-s-fronta/_index.md
content/ru/dokumenty/pisma-s-fronta/pismo-103-1943.md
content/ru/dokumenty/pisma-s-fronta/pismo-104.md
content/ru/dokumenty/pisma-s-fronta/pismo-105-106-mamochke.md
content/ru/dokumenty/pisma-s-fronta/pismo-107.md
content/ru/dokumenty/pisma-s-fronta/pismo-128-129-tane-ot-tovarishcha.md
content/ru/dokumenty/pisma-s-fronta/pismo-131-tanyusha.md
content/ru/dokumenty/pisma-s-fronta/pismo-132-gennadiy-18-11-1943.md
content/ru/dokumenty/pisma-s-fronta/pismo-133-gennadiy-29-11-1943.md
content/ru/dokumenty/pravda-o-dzerzhinskom-1929.md
content/ru/dokumenty/udostoverenie-kolt-1919.md
content/ru/dokumenty/udostoverenie-oborona-stalingrada-samsonov-tt.md
content/ru/dokumenty/vysylka-velikobritaniya-1917.md
content/ru/dokumenty/znak-gpu-samsonov.md
content/ru/foto/_index.md
content/ru/foto/samsonov-timofey-petrovich.md
content/ru/foto/tatyana-timofeevna-2019.md
content/ru/foto/tetrad-semya-prodolzhenie.md
content/ru/istoriya/_index.md
content/ru/istoriya/kak-chitaem-istoriyu.md
content/ru/istoriya/samsonov-i-epoha.md
content/ru/mesta/_index.md
content/ru/mesta/moskva-semeynaya.md
content/ru/roditeli/_index.md
content/ru/roditeli/eva-konstantinovna.md
content/ru/roditeli/krivoshein-dmitriy-aleksandrovich.md
content/ru/roditeli/otets-i-mat.md
content/ru/roditeli/samsonov-timofey-petrovich.md
content/ru/vospominaniya/_index.md
content/ru/vospominaniya/_shablon-zapisi.md
content/ru/vospominaniya/o-tatyane-timofeevne.md
content/ru/vospominaniya/dnevnik/_index.md
content/ru/vospominaniya/dnevnik/o-tetradi.md
content/ru/vospominaniya/dnevnik/00-oblozhka-i-rodoslovnye.md
… 01–11 …
content/ru/vospominaniya/dnevnik/12-brat-front-103-108.md
content/ru/vospominaniya/dnevnik/13-shkola-druzya-109-119.md
content/ru/vospominaniya/dnevnik/14-voyna-evakuaciya-120-127.md
content/ru/vospominaniya/dnevnik/15-pisma-voennye-128-133.md
content/ru/vospominaniya/dnevnik/16-druzya-pobeda-134-139.md
content/ru/vospominaniya/dnevnik/17-krym-semya-140-149.md
content/ru/vospominaniya/dnevnik/18-synovya-150-161.md
```

### `content/en` (50 files)

```
content/en/_index.md
content/en/about.md
content/en/archives.md
content/en/privacy.md
content/en/search.md
content/en/documents/_index.md
content/en/documents/colt-certificate-1919.md
content/en/documents/expulsion-uk-1917.md
content/en/documents/gpu-badge-samsonov.md
content/en/documents/order-of-the-red-banner-samsonov.md
content/en/documents/pravda-on-dzerzhinsky-1929.md
content/en/documents/stalingrad-defense-medal-samsonov-tt.md
# letters-from-the-front/ — empty dir, no md yet
content/en/history/…
content/en/memoirs/… (incl. diary 00–18)
content/en/parents/…
content/en/photos/…
content/en/places/…
```

---

## 9. Verdict

| Check | Result |
|-------|--------|
| Hugo installed | Yes (snap 0.164.0 extended) |
| `hugo --gc --minify` | **PASS** (exit 0) |
| New diary pages build | **PASS** |
| New dokumenty (Stalingrad, RU letters) build | **PASS** |
| Forbidden jargon in **body** | **PASS** (0 hits) |
| Forbidden jargon in FM / not rendered | OK via `post_meta.html` policy |
| Double-nested `categories` (RU 12–18) | **WARN** — fix recommended, not build-blocking |
| EN front-letter mirror | **PENDING** (empty dir) |
| Content rewrites / git commit | **Not done** (per scope) |

**Overall:** site builds cleanly with current B02 content. Only recommended follow-up for this agent’s scope: flatten RU diary 12–18 `categories` arrays; complete EN `letters-from-the-front` when ready.
