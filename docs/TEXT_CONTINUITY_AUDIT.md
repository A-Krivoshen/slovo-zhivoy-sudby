# Text continuity audit (2026-08-01)

Classification of visitor-facing “breaks off” notes in diary chapters.

| Class | Meaning |
|-------|---------|
| `joined_same_sentence` | Hyphen/page join within same chapter; text continued on next original_page |
| `linked_next_chapter` | Sentence continues in the next published chapter |
| `genuinely_missing` | No continuation in available batch |
| `uncertain` | Continuity unclear; conservative note |

## Findings and fixes

| File | original_page | Class | Old wording | New wording | Reason |
|------|---------------|-------|-------------|-------------|--------|
| `01-moya-mama.md` / EN pair | 008→009 | `joined_same_sentence` | «текст обрывается — продолжение на PAGE 009» | Joined: «за эти / следила классная дама» | Same sentence across scans |
| `01-moya-mama.md` / EN | end / 010→011 | `linked_next_chapter` | «Отец был стар-» + «текст обрывается» | «Отец был стар[ше] мамы на 12 лет» + link to ch. 02 | Word split across chapters |
| `02-otec-brak-deti.md` / EN | 011 start | `linked_next_chapter` | Leading «мамы на 12 лет» alone | Editorial note; starts with Mama’s flat story | Avoid double full sentence |
| `03-detstvo-moskva.md` / EN | 040 | `genuinely_missing` | «продолжение на след. стр.» | «Фраза обрывается… не найдено» | Next leaf is a new block (cats), not table-places finish |
| `03-detstvo-moskva.md` / EN | 048→049 | `joined_same_sentence` | «текст обрывается» | Joined: «а то и / двоих троих» | Continuous narrative |
| `06-dokumenty-sezdy.md` / EN | end of flower list | `genuinely_missing` | «обрывается на конце страницы» | Honest missing-continuation note | No recovered flower-list tail |
| `08-otec-harakter.md` / EN | 071 | `genuinely_missing` | «видимо… на вклейках» | «Продолжение… не найдено» | No proof of paste-in continuation |
| `10-prodolzhenie-080-089.md` / EN | 083 | `genuinely_missing` / `uncertain` | bare «текст обрывается» | Page-specific missing note | Dense illegible end; no safe join |

## Mid-chapter indexes moved

| File | Action |
|------|--------|
| `08-otec-harakter.md` | «Люди / Места / Даты…» moved from after 060 to end `<details>` |
| `03-childhood-moscow.md` (EN) | «Extracted facts» blocks wrapped in `<details>` at end |
| `09-dokumenty-v-tetradi.md` + EN | End indexes wrapped in `<details>` (were already after 079) |

## Remaining policy

- Keep compact `<!-- стр. NNN -->` markers between leaves.
- Do not invent missing words beyond bracketed stems like `стар[ше]`.
- Prefer `genuinely_missing` wording over speculative “probably on inserts.”
