# Privacy / public graph leak check

**Branch:** `task/archive-seo-ai-knowledge-graph`  
**Date:** 2026-08-01  
**Scope:** Public Hugo content (`content/**`), public archive graph (`data/archive/public/**`), and residual static unlinked files.  
**Out of scope:** Private static JPEGs may remain on disk if unlinked; this pass does **not** delete them.

## Summary

| Check | Result | Notes |
|-------|--------|-------|
| 099 / 100 Ukrainian medal as **public entity** | **PASS** | No content page, no figure, no `data/archive/public` entity for medal «Захиснику Вітчизни». Tyoma public person lists Stalingrad only. |
| `str-155` / `str-157` as **published gallery** | **PASS** (after fix) | Were linked from EN diary ch. 18; figures removed. RU gallery + RU ch. 19 already withheld. |
| Apartment / current entrance (`№ 226`, `17 подъезде`, living degree) | **PASS** (after fix) | EN ch. 13 still had raw manuscript lines; redacted to match RU ch. 13. |
| Full DOB for **living** reintroduced | **PASS** | Living-person births remain year-only in public reader text (1948 / 1957 / 1981 / 1990). Full DOBs present only for deceased / historical figures already on site. |
| `withheld_pending` in **visitor body** | **PASS** | 0 hits in content body after front matter. Editorial terms only in FM / internal `data/` / docs. |
| Public graph export hygiene | **PASS** | `data/archive/public/people.yaml` only; no living sons entities; no medal 099–100; no apartment fields. |

**Overall: PASS** (after content fixes below).

---

## Fixes applied this pass

### 1. EN diary — living address / degree (ch. 13)

**File:** `/home/slon/Work/SZHS/content/en/memoirs/diary/13-school-friends-109-119.md`

| Before (leak) | After |
|---------------|--------|
| `ул. Серафимовича в 12-ый подъезд, № 226, на 4-ом этаже` | `ул. Серафимовича [подъезд и номер квартиры скрыты]` |
| `Теперь Марина – доктор экономических наук` | `Позже Марина получила учёную степень [подробности в публичной версии не уточняем]` |
| `Наташа до сих пор живет в нашем доме, только в 17 подъезде. Она – кандидат физ.-мат. наук.` | `Наташа и позже оставалась связана с нашим домом [точные нынешние подъезд и учёная степень в публичной версии не приводим]` |

Aligned with RU reader chapter  
`/home/slon/Work/SZHS/content/ru/vospominaniya/dnevnik/13-tanya-detstvo-i-shkola.md`  
and policy in `docs/PRIVACY_REVIEW_B02_ALL_CHAPTERS.md`.

### 2. EN diary — `str-155` / `str-157` figures (ch. 18)

**File:** `/home/slon/Work/SZHS/content/en/memoirs/diary/18-sons-150-161.md`

- Removed public `{{< figure src="/photos/dnevnik-tt/str-155.jpg" … >}}`
- Removed public `{{< figure src="/photos/dnevnik-tt/str-157.jpg" … >}}`
- Left HTML comments: full-page scan not published (living-person photo privacy)
- Transcription text for those pages retained (year-only birth for Seryozha)

RU already correct: gallery note + no figures in  
`content/ru/foto/tetrad-semya-prodolzhenie.md`,  
`content/en/photos/notebook-family-continued.md`,  
and footnote in `content/ru/vospominaniya/dnevnik/19-semya-i-deti.md`.

---

## Check details

### A. Ukrainian medal pages 099–100

| Surface | Status |
|---------|--------|
| `content/**` reference to `str-099` / `str-100` | **0** |
| Public document page for «Захиснику Вітчизни» | **None** |
| Series/number `МН 178440` in content/layouts | **0** |
| `data/archive/public/people.yaml` medal entity | **Absent** |
| Internal hold (`data/archive_photos/index.yaml`, `fact_conflicts.yaml`, etc.) | OK to keep private/internal |

**Residual (not fail):** JPEGs still on disk and in Hugo `static/` / built `public/photos/` if previously built:

- `static/photos/dnevnik-tt/str-099.jpg`
- `static/photos/dnevnik-tt/str-100.jpg`

Unlinked from all content; direct URL remains theoretically fetchable. **Do not remove in this pass** (per task). Optional later hardening: move out of `static/` or CDN deny.

### B. `str-155` / `str-157` gallery publish status

| Surface | Status |
|---------|--------|
| `content/**` figure `str-155.jpg` / `str-157.jpg` | **0** after fix |
| Photo album RU/EN public gallery pages | Explicit **not shown** note; no figures |
| RU reader ch. 19 | Note that 155/157 not published; no `withheld` jargon |

**Residual:** raw files remain at `static/photos/dnevnik-tt/str-155.jpg` and `str-157.jpg` (unlinked). Photo index may still list paths for internal use; not a public graph entity file under `data/archive/public/`.

### C. Apartment numbers / current living entrance

| Pattern | Public content after fix |
|---------|--------------------------|
| `№ 226` | **0** in `content/` |
| `17 подъезде` (current living) | **0** in `content/` |
| Historical childhood entrances (other floors/подъезды, past tense) | Kept per privacy policy |
| Historical apt. 223 in old captions (1930s dining room, etc.) | Not re-opened this pass; prior policy treated childhood/historical context separately from current living |

### D. Full DOB for living

| Person class | Public text |
|--------------|-------------|
| Sons / grandchildren (living or treat-as-living) | Year only (`1957`, `1948`, `1981`, `1990`) |
| Author T. T. (deceased) | Full DOB allowed (`2 сентября 1926`) |
| Parents / brother Tyoma (historical published) | Full or partial dates already on public bios / diary |

No reintroduction of day+month+year for living sons in public reader chapters or `data/archive/public/people.yaml` (sons not present as public people entities).

### E. `withheld_pending` in visitor body

Script scan: for every `content/**/*.md`, body after second `---` front-matter fence:

| Term | Body hits |
|------|-----------|
| `withheld_pending` | **0** |
| `first_pass` | **0** |
| `batch_id` | **0** |
| `original_page` | **0** |

These terms remain only in front matter and internal data/docs (expected). Layouts must continue not to render them (see `docs/BUILD_CHECK_B02_AUDIT.md`).

### F. Public archive graph (`data/archive/public/`)

At check time:

```
data/archive/public/people.yaml   # only public-safe people entities
data/archive/private/README.md    # private tree marker; no private people dump yet
```

| Requirement | Status |
|-------------|--------|
| No Ukrainian medal public entity (099–100) | **PASS** |
| No str-155 / str-157 as published assets in public yaml | **PASS** (not listed) |
| No apartment / current address fields | **PASS** |
| No `withheld_pending` strings in public yaml | **PASS** |
| No public entities for living sons as graph people | **PASS** (absent) |
| Private materials not copied into `public/` | **PASS** |

Tyoma (`person-timofey-timofeevich-samsonov`) notes Stalingrad medal and disambiguation from T. P.; **no** Ukrainian 1999 medal fields or series number.

---

## Residual risk (family / later hardening)

1. Direct URL to unlinked static scans (`str-099`, `str-100`, `str-155`, `str-157`) if URL is known.  
2. Handwritten full dates may still be visible **on** page scans that *are* published for other pages — separate crop/blur decision.  
3. EN ch. 18 may still be `draft: true` / incomplete translation; privacy figures fixed so a future undraft does not re-publish 155/157.  
4. If later agents add more files under `data/archive/public/`, re-run the greps in §Check details.

## Re-run commands

```bash
rg -n 'str-155\.jpg|str-157\.jpg|№\s*226|17\s*подъезд|withheld_pending|МН\s*178440|Захисник|str-099\.jpg|str-100\.jpg' content layouts data/archive/public
rg -n 'entity_id|medal|zahys|155|157|226|withheld' data/archive/public
```

---

## Verdict

**PASS** — public content and public graph free of the listed privacy leaks after EN ch. 13 address/degree redaction and EN ch. 18 removal of `str-155` / `str-157` published figures. Static private/unlinked files left on disk intentionally.
