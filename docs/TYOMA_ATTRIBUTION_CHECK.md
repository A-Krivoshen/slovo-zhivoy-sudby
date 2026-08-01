# Tyoma attribution check (Самсонов Тимофей Тимофеевич)

**Date:** 2026-08-01  
**Scope:** Public site representation of uncle Tyoma vs father Timofey Petrovich; Ukrainian 1999 medal hold; people taxonomy.  
**Git commit:** not made (per task).

## 1. How people tags work (Hugo)

Configured in `/home/slon/Work/SZHS/hugo.toml`:

```toml
[taxonomies]
  tag = 'tags'
  category = 'categories'
  person = 'people'
```

- Front matter key: `people: ["…"]` (array of display names).
- Hugo builds term lists under `/people/<slug>/` (RU) and `/en/people/<slug>/` (EN).
- **Language-specific names** create separate terms:
  - RU: `Самсонов Тимофей Тимофеевич` → `/people/самсонов-тимофей-тимофеевич/`
  - EN: `Timofey Timofeevich Samsonov` → `/en/people/timofey-timofeevich-samsonov/`
- There is **no** dedicated bio under `content/ru/roditeli/` for Tyoma; the people term page is a listing of tagged posts only (PaperMod list template). Visitor meta does **not** surface internal front-matter flags (`transcription_status`, `batch_id`, etc.) — see `layouts/_partials/post_meta.html`.

## 2. Content that mentions Tyoma

| Location | Role | `people` tag |
| --- | --- | --- |
| `content/ru/vospominaniya/dnevnik/11-prodolzhenie-090-099.md` | Narrative «Мой брат»; names Тёма / Женя; war path Stalingrad→Berlin | `Самсонов Тимофей Тимофеевич` |
| `content/en/memoirs/diary/11-notebook-continued-090-099.md` | EN pair | `Timofey Timofeevich Samsonov` |
| `content/ru/vospominaniya/dnevnik/12-brat-front-103-108.md` | Exam photo, front letters, Stalingrad certificate text + figure `str-108.jpg` | same |
| `content/en/memoirs/diary/12-brother-front-letters-101-108.md` | EN pair | same |
| `content/ru/dokumenty/udostoverenie-oborona-stalingrada-samsonov-tt.md` | Standalone Stalingrad document; explicit «не отец Т. П.» | only Tyoma |
| `content/en/documents/stalingrad-defense-medal-samsonov-tt.md` | EN pair | only Tyoma |
| `content/ru/dokumenty/_index.md` / EN documents index | Lists Stalingrad as **brother**, not father | n/a |
| `content/ru/vospominaniya/dnevnik/00-oblozhka-i-rodoslovnye.md` | Chart: son Т. Т., b. Moscow 1923 | (page people: Tatyana only) |
| `content/ru/roditeli/otets-i-mat.md` (updated this pass) | Short «Дети Самсоновых» navigation block | now includes Tyoma |
| `content/en/parents/father-and-mother.md` (updated) | EN pair | now includes Tyoma |

**Chapter numbering note:** file/key `…090-099` vs published body **090–098** is intentional: manuscript pages **099–100** (Ukrainian medal) are skipped in the chapter body. Nav footer jumps 098 → 101–108.

**Names in source:** On p. 093 he is **Тимофей Тимофеевич (Тёма)**; later the same brother is often **Женя** in the manuscript (editorial note already on ch. 11).

## 3. Ukrainian 1999 medal (099–100) — public hold

| Check | Result |
| --- | --- |
| Content page under `dokumenty/` / `documents/` for 099–100 | **None** (preferred) |
| Any `content/**` body/caption with `Захиснику` / `Вітчизни` / series МН 178440 | **0 matches** |
| Any `public/**/*.html` with those strings | **0 matches** |
| Any `content/**` reference to `str-099` / `str-100` | **0 matches** |
| On T. P. bio / album / T. P. documents | **Absent** |
| On Tyoma people listing / Stalingrad doc page | **Absent** (no wrong attribution; medal not published at all) |

**Internal registry (keep):**

- `data/fact_conflicts.yaml` → `ukraine-medal-zahysnyku-vitichyzny-1999`
  - `person_confirmed`: Самсонов Тимофей Тимофеевич (дядя Тёма)
  - `not_this_person`: Самсонов Тимофей Петрович (cannot receive a 1999 award; d. 1955)
  - `review_status`: `withheld_pending_person_page`
- Also: `data/manuscript_batches/2026-08-01.yaml`, `data/archive_photos/index.yaml`, `static_photos_provenance.yaml`, docs audits.

**Residual (not a content attribution bug):** JPEG files remain at:

- `static/photos/dnevnik-tt/str-099.jpg`
- `static/photos/dnevnik-tt/str-100.jpg`
- and the built copies under `public/photos/dnevnik-tt/`

They are **not linked** from any published page or HTML, but a direct URL is still fetchable if known. Prefer leave unlinked; do not add a public medal article. Optional hardening (move out of `static/` / block in `robots`/CDN) is out of this pass unless family decides.

**Do not publish** certificate series/number **МН 178440** on the public site (registry rule).

## 4. Stalingrad medal vs Timofey Petrovich

| Check | Result |
| --- | --- |
| Stalingrad certificate name on form | **гв. сержант Самсонов Тимофей Тимофеевич** (`str-108.jpg`, ch. 12 + doc page) |
| False attribution to Т. П. on public content | **None found** |
| Explicit disambiguation | Doc page + documents index + ch. 12 link line: «брат Тёма, не отец Т. П.» |
| T. P. bio awards | Only family-album T. P. materials: Red Banner, GPU badge, Colt, Pravda — **no** Stalingrad, **no** Ukrainian medal |

Diary mentions of «сын … от Сталинграда до Берлина» (e.g. ch. 04) are **manuscript voice about the son (Tyoma)**, not awards attached to the father page.

## 5. `content/ru/roditeli/samsonov-timofey-petrovich.md` review

- `people:` only T. P., Tatyana, Dzerzhinsky — **not** Tyoma (correct: Tyoma is not a subject of that bio).
- Chronology and «Награды и органы»: revolutionary/Cheka materials only.
- No Stalingrad, no 1999 Ukrainian award, no brother-war documents mixed in.
- EN pair `content/en/parents/timofey-petrovich-samsonov.md`: same clean split.
- Photo album `content/ru/foto/samsonov-timofey-petrovich.md`: T. P. only.

**No content fixes required** on the T. P. bio for attribution.

## 6. Change made this pass (non-duplicative navigation)

Full brother narrative already lives in diary ch. 11–12; Stalingrad has its own document page (likely from a parallel agent). **No second biography** was added.

**Added** a short **«Дети Самсоновых» / «The Samsonov children»** block on:

- `/home/slon/Work/SZHS/content/ru/roditeli/otets-i-mat.md`
- `/home/slon/Work/SZHS/content/en/parents/father-and-mother.md`

Links to people term, diary ch. 11–12, and Stalingrad document; one-line **T. T. ≠ T. P.** reminder. Tagged `people` with Tyoma so the parents hub appears on his people list.

## 7. Public build note

At check time, `public/dokumenty/` may still list only older T. P. documents until the next Hugo build; **source content** for the Stalingrad T. T. page is present under `content/`. Rebuild before deploy to refresh people lists and documents index.

## 8. Verdict

| Requirement | Status |
| --- | --- |
| Tyoma correctly tagged in people taxonomy | **OK** (RU + EN) |
| Diary + Stalingrad document link chain | **OK** |
| Ukrainian 099–100 never on T. P. or wrong public bio | **OK** (no public medal page) |
| No false Stalingrad/Ukrainian → T. P. | **OK** (0 public false hits) |
| T. P. bio careful review | **OK**, unchanged |
| Light navigation for brother | **Added** on parents hub only |

### Recommended later (not done)

1. Rebuild Hugo so `public/` matches content (Stalingrad doc + parents hub + people lists).  
2. Decide whether to remove or unpublish raw `str-099`/`str-100` from `static/photos` (residual direct-URL exposure).  
3. If a full Tyoma person bio is wanted, create it under a non-`roditeli` path or extend people term content; only then reconsider lifting the Ukrainian medal hold — still with correct T. T. attribution and without series number.
