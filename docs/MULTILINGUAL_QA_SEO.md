# Multilingual QA (RU/EN) — SEO / hreflang

**Branch:** `task/archive-seo-ai-knowledge-graph`  
**Date:** 2026-08-01  
**Scope:** `lyudi`/`people`, `sobytiya`/`events`, `hronologiya`/`timeline`, `mesta`/`places`, `printsipy-publikacii`/`publishing-principles`, diary chapters 12–19.

## How pairing works

- Hugo PaperMod emits `<link rel="alternate" hreflang="…">` from `.AllTranslations` (see `themes/PaperMod/layouts/_partials/head.html`).
- Pages pair when they share the same front-matter **`translationKey`**.
- **hreflang is only emitted for built (non-draft) pages.** If EN is `draft: true`, production builds without `-D` will **not** publish EN → no EN alternate for that key. That is intentional for incomplete English diary chapters.

| Rule | Practice on this site |
|------|------------------------|
| Same key, both published | Full RU↔EN hreflang |
| Same key, EN draft | RU live only; no EN hreflang until EN is undrafted |
| Key only on one language | No alternate link (OK for noindex hubs) |
| EN body must be English | Do not ship Russian manuscript body as “translation” on public EN pages |

## Status legend

| Status | Meaning |
|--------|---------|
| **OK** | Same `translationKey`, both `draft: false`, EN body is English |
| **OK (EN draft)** | Keys match; RU published; EN remains draft (no production hreflang yet) |
| **RU-only intentional** | Editorial hub / noindex / temporary; no EN needed |
| **Mismatch** | Different keys for corresponding content (must fix) |
| **Missing EN** | Public RU without EN pair |

---

## 1. People — `lyudi` ↔ `people`

| translationKey | RU path | EN path | Status |
|----------------|---------|---------|--------|
| `people` | `content/ru/lyudi/_index.md` | `content/en/people/_index.md` | **OK** |
| `person-tatyana-timofeevna-krivosheina` | `content/ru/lyudi/tatyana-timofeevna-krivosheina.md` | `content/en/people/tatyana-timofeevna-krivosheina.md` | **OK** |
| `person-timofey-petrovich-samsonov` | `content/ru/lyudi/timofey-petrovich-samsonov.md` | `content/en/people/timofey-petrovich-samsonov.md` | **OK** |
| `person-eva-konstantinovna-samsonova` | `content/ru/lyudi/eva-konstantinovna-samsonova.md` | `content/en/people/eva-konstantinovna-samsonova.md` | **OK** |
| `person-timofey-timofeevich-samsonov` | `content/ru/lyudi/timofey-timofeevich-samsonov.md` | `content/en/people/timofey-timofeevich-samsonov.md` | **OK** |
| `person-genya-samsonova` | `content/ru/lyudi/genya-samsonova.md` | `content/en/people/genya-samsonova.md` | **OK** |
| `person-aleksandr-krivoshein` | `content/ru/lyudi/aleksandr-krivoshein.md` | `content/en/people/aleksandr-krivoshein.md` | **OK** |
| `person-dmitry-pisma-front` | `content/ru/lyudi/dmitry-pisma-front.md` | `content/en/people/dmitry-front-letters.md` | **OK** |
| `person-gennady-vokhmintsev` | `content/ru/lyudi/gennady-vokhmintsev.md` | `content/en/people/gennady-vokhmintsev.md` | **OK** |
| `person-misha-friolenko` | `content/ru/lyudi/misha-friolenko.md` | `content/en/people/misha-friolenko.md` | **OK** |

**Canonical URLs (after build):** `/lyudi/…` ↔ `/en/people/…`

---

## 2. Events — `sobytiya` ↔ `events`

| translationKey | RU path | EN path | Status |
|----------------|---------|---------|--------|
| `events-hub` | `content/ru/sobytiya/_index.md` | `content/en/events/_index.md` | **OK** |
| `event-evacuation-1941` | `content/ru/sobytiya/evakuaciya-1941.md` | `content/en/events/evacuation-1941.md` | **OK** |
| `event-defense-of-stalingrad` | `content/ru/sobytiya/oborona-stalingrada.md` | `content/en/events/defense-of-stalingrad.md` | **OK** |
| `event-school-years-1940-1941` | `content/ru/sobytiya/shkola-1940-1941.md` | `content/en/events/school-1940-1941.md` | **OK** |
| `event-tatyana-meets-sasha` | `content/ru/sobytiya/znakomstvo-s-sashey.md` | `content/en/events/meeting-sasha.md` | **OK** |
| `event-crimea-trips` | `content/ru/sobytiya/krym-poezdki.md` | `content/en/events/crimea-trips.md` | **OK** |
| `event-family-start` | `content/ru/sobytiya/nachalo-semi.md` | `content/en/events/family-beginning.md` | **OK** |

**Canonical URLs:** `/sobytiya/…` ↔ `/en/events/…`

---

## 3. Timeline — `hronologiya` ↔ `timeline`

| translationKey | RU path | EN path | Status |
|----------------|---------|---------|--------|
| `timeline` | `content/ru/hronologiya/_index.md` | `content/en/timeline/_index.md` | **OK** |

**Canonical URLs:** `/hronologiya/` ↔ `/en/timeline/`

---

## 4. Places — `mesta` ↔ `places` (new entity pages)

| translationKey | RU path | EN path | Status |
|----------------|---------|---------|--------|
| `places` | `content/ru/mesta/_index.md` | `content/en/places/_index.md` | **OK** |
| `places-moscow` | `content/ru/mesta/moskva-semeynaya.md` | `content/en/places/family-moscow.md` | **OK** |
| `places-metropol-moscow` | `content/ru/mesta/metropol-moscow.md` | `content/en/places/metropol-moscow.md` | **OK** |
| `places-serafimovich-street` | `content/ru/mesta/serafimovich-street.md` | `content/en/places/serafimovich-street.md` | **OK** |
| `places-crimea-family` | `content/ru/mesta/crimea-family.md` | `content/en/places/crimea-family.md` | **OK** |
| `places-sevastopol` | `content/ru/mesta/sevastopol.md` | `content/en/places/sevastopol.md` | **OK** |
| `places-stalingrad-volgograd` | `content/ru/mesta/stalingrad-volgograd.md` | `content/en/places/stalingrad-volgograd.md` | **OK** |

**Canonical URLs:** `/mesta/…` ↔ `/en/places/…`

---

## 5. Publishing principles

| translationKey | RU path | EN path | Status |
|----------------|---------|---------|--------|
| `publishing-principles` | `content/ru/printsipy-publikacii.md` | `content/en/publishing-principles.md` | **OK** |

**Canonical URLs:** `/printsipy-publikacii/` ↔ `/en/publishing-principles/`

Linked from about pages: RU `o-proekte.md`, EN `about.md`.

---

## 6. Diary chapters 12–19

RU reader structure was split/renamed (see [B02_URL_MIGRATION_MAP.md](./B02_URL_MIGRATION_MAP.md)). EN still uses older page ranges on some files; **`translationKey` values are aligned to the RU reader chapters** so hreflang will work when EN is undrafted.

**Policy:** all EN diary files for this range stay **`draft: true`** until translation is complete. Do not publish EN by undrafting without a real English body.

| translationKey | RU (published) | EN (draft) | Status |
|----------------|----------------|------------|--------|
| `diary-12-brat-front-101-108` | `ru/.../12-brat-front-103-108.md` | `en/.../12-brother-front-letters-101-108.md` | **OK (EN draft)** |
| `diary-13-tanya-childhood-school` | `ru/.../13-tanya-detstvo-i-shkola.md` | `en/.../13-school-friends-109-119.md` | **OK (EN draft)** — EN file still spans 109–119; re-split later |
| `diary-14-school-and-war` | `ru/.../14-shkola-i-voyna.md` | `en/.../14-war-evacuation-120-127.md` | **OK (EN draft)** — EN range 120–127 vs RU 118–127 |
| `diary-15-pisma-128-133` | `ru/.../15-pisma-voennye-128-133.md` | `en/.../15-wartime-letters-128-133.md` | **OK (EN draft)** |
| `diary-16-youth-sasha` | `ru/.../16-yunost-i-sasha.md` | `en/.../16-friends-victory-134-139.md` | **OK (EN draft)** |
| `diary-17-crimea-family` | `ru/.../17-krym-sevastopol-semya.md` | `en/.../17-crimea-family-140-149.md` | **OK (EN draft)** — EN file still includes later pages; re-split later |
| `diary-18-study-work` | `ru/.../18-ucheba-rabota-vypuskniki.md` | `en/.../18-study-work-reunions.md` | **OK (EN draft)** — short EN stub |
| `diary-19-family-children` | `ru/.../19-semya-i-deti.md` | `en/.../18-sons-150-161.md` | **OK (EN draft)** — EN slug still `18-sons-…`; key matches RU ch. 19 |

### Editorial hubs (no EN)

| translationKey | RU path | Status |
|----------------|---------|--------|
| `diary-13-hub-legacy` | `ru/.../13-shkola-druzya-109-119.md` (`robotsNoIndex: true`) | **RU-only intentional** |
| `diary-17-hub-legacy` | `ru/.../17-krym-semya-140-149.md` (`robotsNoIndex: true`) | **RU-only intentional** |

Hubs only point readers to split chapters; no hreflang expected.

### Key remaps applied on this QA pass

| EN file | Old key | New key |
|---------|---------|---------|
| `13-school-friends-109-119.md` | `diary-13-shkola-109-119` | `diary-13-tanya-childhood-school` |
| `14-war-evacuation-120-127.md` | `diary-14-voyna-120-127` | `diary-14-school-and-war` |
| `16-friends-victory-134-139.md` | `diary-16-druzya-134-139` | `diary-16-youth-sasha` |
| `17-crimea-family-140-149.md` | `diary-17-krym-140-149` | `diary-17-crimea-family` |
| `18-sons-150-161.md` | `diary-18-synovya-150-161` | `diary-19-family-children` |
| `18-study-work-reunions.md` | *(new draft)* | `diary-18-study-work` |

---

## 7. Out-of-scope unpaired keys (noted, not fixed here)

Public RU letter pages without EN mirrors (other workstreams):

| translationKey | RU path |
|----------------|---------|
| `doc-letter-insert-sister-089-090` | `content/ru/dokumenty/pisma-s-fronta/pismo-vstavka-sestre-089-090.md` |
| `doc-postcard-130-new-year` | `content/ru/dokumenty/pisma-s-fronta/otkrytka-130-novyj-god.md` |

These do not affect entity-hub hreflang. Add short EN drafts when letter EN coverage is next.

---

## 8. QA checklist (local)

```bash
# List keys and parity
python3 - <<'PY'
import re
from pathlib import Path
from collections import defaultdict
by = defaultdict(list)
for f in Path('content').rglob('*.md'):
    t = f.read_text(encoding='utf-8')
    if not t.startswith('---'):
        continue
    end = t.find('\n---', 3)
    fm = t[3:end]
    m = re.search(r'^translationKey:\s*["\']?([^"\'\n]+)', fm, re.M)
    d = re.search(r'^draft:\s*(true|false)', fm, re.M)
    if m:
        lang = 'ru' if '/ru/' in str(f) else 'en'
        by[m.group(1).strip()].append((lang, d.group(1) if d else 'false', str(f)))
for k, items in sorted(by.items()):
    langs = {i[0] for i in items}
    if langs != {'ru', 'en'}:
        print('UNPAIRED', k, items)
PY

# Production-like build: drafts must not appear under /en/memoirs/diary/12…18
hugo --gc --minify
# Then: no EN diary 12–18 HTML if draft:true; entity hubs should have mutual hreflang in head
```

### After undrafting an EN page

1. Confirm body is **English** (not a Russian dump).
2. Confirm `translationKey` still matches the RU reader chapter.
3. Rebuild without `-D` and check `<link rel="alternate" hreflang="en">` / `hreflang="ru"` on both URLs.
4. Prefer re-splitting EN diary files to match RU chapter boundaries before undrafting multi-range drafts (13, 17).

---

## 9. Summary (this pass)

| Area | Pairs | Issues fixed |
|------|------:|--------------|
| People | 10/10 OK | none needed |
| Events | 7/7 OK | none needed |
| Timeline | 1/1 OK | none needed |
| Places | 7/7 OK | none needed |
| Publishing principles | 1/1 OK | none needed |
| Diary 12–19 content keys | 8/8 paired; EN all draft | remapped 5 EN keys; added draft EN for `diary-18-study-work` |
| Diary hubs | 2 RU-only noindex | intentional |

**No commit** performed as requested.
