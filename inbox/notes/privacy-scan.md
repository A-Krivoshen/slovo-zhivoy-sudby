# Privacy scan report

**Date:** 2026-08-01  
**Scope:**
- `/home/slon/Work/SZHS/content` (all markdown)
- `/home/slon/Work/SZHS/static/photos/dnevnik-tt` (all JPGs)

**Looked for:**
- Phone numbers (`915-xx-xx`, `+7`, `8-9xx`, similar local formats)
- Modern personal emails
- Clearly private recent contact notes

---

## Summary

| Area | Result |
|------|--------|
| Markdown phones / contact notes | **Found and redacted** (2 files) |
| Modern personal emails | **None found** |
| Images with visible private phones/emails | **None** (str-002 already cleaned) |
| Narrative “telephone” mentions (historical text) | OK — not contact data |

---

## Markdown findings and fixes

### 1. Phone / contact margin notes (redacted)

Transcribed from notebook **p. 002** (margin, blue ink). Numbers and associated names were private contact notes, not part of the memoir narrative.

**Before:** three local numbers (`915-43-71`, `915-48-21`, `915-43-71`) with name labels (Танина / Стан. Ник.; Николай Александрович; Александра?/Родионов?).

**Files fixed:**

| File | Action |
|------|--------|
| `/home/slon/Work/SZHS/content/ru/vospominaniya/dnevnik/00-oblozhka-i-rodoslovnye.md` | Whole contact block → `[скрыто]/[redacted]` |
| `/home/slon/Work/SZHS/content/en/memoirs/diary/00-cover-and-charts.md` | Same (EN parallel) |

Placeholder left so the reader still sees that margin notes existed, without leaking digits or contact names.

### 2. Emails

No matches for patterns like `user@domain.tld` (including gmail, yandex, mail.ru, etc.) under `content/`.

### 3. Not treated as leaks

- Historical narrative mentions of telephones / telegrams (e.g. father calling from work; war-time telegrams; poem lines with «телефонный») — no numbers.
- Year-like digits in congress lists (e.g. `1915`) — not phones.
- Genealogical names/dates/addresses of historical family members — public family-history material, not modern contact data.

---

## Image findings (`static/photos/dnevnik-tt`)

Scanned visually (including opening images with the image reader):

| Image | Privacy-sensitive content |
|-------|---------------------------|
| `str-001.jpg` | Cover only — clean |
| **`str-002.jpg`** | **Cleaned** — portrait of mother + caption; **no legible phones/emails** on the right margin where notes used to be. Faint residue/grid only. |
| `str-003.jpg` | Genealogy chart + photos — clean |
| `str-007.jpg` | Mother bio start — clean |
| `str-009.jpg` | Narrative handwriting — clean |
| `str-010.jpg` | Narrative handwriting — clean |
| `str-012.jpg` | Narrative handwriting — clean |
| `str-015.jpg` | Narrative + 1941 insert — clean |

### Human note: str-002.jpg

**Confirmed cleaned.** The scan no longer shows the blue-ink phone/contact list that was still present in the markdown transcription. No further image edit required for phones/emails on the files currently in this folder.

**Images needing human follow-up for privacy leaks:** none among the files listed above.

*(If additional pages from the full 79-page notebook are published later under this path, re-scan those scans the same way — only `str-001…015` subset is present now.)*

---

## Actions taken

1. Redacted RU + EN diary chapter `00` contact/phone blocks with `[скрыто]/[redacted]`.
2. Verified `str-002.jpg` has no readable private contact data.
3. Full-content grep: no remaining `915-43` / `915-48` / modern emails under `content/`.

## Residual risk / recommendations

- Living-person birth dates appear in genealogy chapters (e.g. children/grandchildren born 1976–2003). Out of scope for this “phones/emails/recent contact notes” pass; review separately if a stricter privacy policy is desired.
- Only a subset of diary page scans is in `static/photos/dnevnik-tt`; privacy on unpublished scans is N/A until they land in the tree.
