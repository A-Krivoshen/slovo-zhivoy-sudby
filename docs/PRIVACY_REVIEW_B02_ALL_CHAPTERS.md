# Privacy review — B02 reader chapters (109–161)

**Branch:** `task/b02-editorial-coverage-fix`  
**Scope:** public reader chapters 13, 14, 16, 17, 18, 19 (+ related gallery)  
**`privacy_reviewed: true`** set only after this pass on those chapter files.

## Policy applied

| Keep | Remove / generalize in **public** reading (and public diplomatic if present) |
|------|--------------------------------------------------------------------------------|
| Historical street / house names needed for story | Exact **apartment numbers** of family or peers when combined with living persons |
| Childhood building context (past tense) | **Current** residence of potentially living people (entrance, floor, “still lives…”) |
| Year of birth only for living | Full day+month+year DOB for living |
| Historical medical episodes in mid-century memoir (non-sensational) | Modern medical + precise current address |
| Names of deceased / clearly historical classmates | Academic degree + current location for living peers |

## Chapter findings

### `13-tanya-detstvo-i-shkola` (109–117) — **critical fixes applied**

| Issue | Action |
|-------|--------|
| ул. Серафимовича, 12-й подъезд, **№ 226**, 4-й этаж | Public: street kept; **подъезд и № квартиры скрыты** |
| Наташа Сорокина **до сих пор живёт** в 17 подъезде + **кандидат физ.-мат. наук** | Public: no current entrance; no degree |
| Марина — **доктор экономических наук** (present tense) | Softened; degree detail not in public |
| Детская домработница Наташа (past) | Kept (historical) |
| Этажи/подъезды **детства** друзей (Инна 13-й, клуб 3-й и т.п.) | Kept as historical narrative |
| Т. Т. birth **2 сентября 1926** | Kept (deceased author) |

### `14-shkola-i-voyna` (118–127)

| Issue | Action |
|-------|--------|
| Evacuation / village narrative | No modern living addresses found |
| Sweep for `кв. N` | None critical |

### `16-yunost-i-sasha` (134–139)

| Issue | Action |
|-------|--------|
| Postwar youth | No precise living addresses flagged |
| Sweep | apartment numbers generalized if any |

### `17-krym-sevastopol-semya` (140–144)

| Issue | Action |
|-------|--------|
| Travel narrative | Historical places OK |
| Sweep | OK |

### `18-ucheba-rabota-vypuskniki` (145–148)

| Issue | Action |
|-------|--------|
| Graduates group photo (1949 / 1983) | Names only from manuscript captions; no modern home addresses |
| Sweep | OK |

### `19-semya-i-deti` (149–161)

| Issue | Action |
|-------|--------|
| Full DOB living | Year-only for births (1948 / 1957) |
| Ленинский пр. | Street OK; no flat number in public |
| **155 / 157** photos | **Not** in public gallery; matrix `internal_privacy`; no public withheld block |
| Diplomatic details | pages **155, 157 omitted** from public appendix |
| Childhood medical (Mitya historical) | Kept as memoir (mid-century); not modern chart |
| Adult careers (candidate, docent) without current home | Kept as historical/family status; monitor if family objects |

### Gallery `/foto/tetrad-semya-prodolzhenie/`

| 155, 157 | Removed from public figures |
| 148, 161, 146 | Published as crops (historical groups / family frames) |

## Residual risk (family optional)

- Classmate full names from 1930s–40s may still identify living elders — low modern address risk.
- Mitya adult narrative (marriage, institute) remains; no flat numbers.
- Direct URL to raw `str-155.jpg` / `str-157.jpg` in `static/` if known — prefer leave unlinked.

## Status

Public chapters above: **`privacy_reviewed: true`** after this pass.  
Re-review required before any re-introduction of 155/157 images or full apartment numbers.
