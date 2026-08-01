# Full site audit — 2026-08-01

**Branch:** `task/final-archive-editorial-fixes-2026-08`  
**HEAD (at audit):** `2865dbe` (+ fix for photo-album residual line after audit)  
**Build:** `hugo --minify` OK  

| Metric | Value |
|--------|------:|
| Pages RU | 157 |
| Pages EN | 155 |
| HTML files in `public/` | 313 |
| Static images | 193 (~43 MB) |
| Images > 1.5 MB | 0 |
| Search JSON | `public/index.json`, `public/en/index.json` |
| Sitemap URL counts | root 2 · ru 92 · en 92 |

Hugo deprecations (theme PaperMod only): `.Language.LanguageDirection` / `LanguageCode` / `LanguageName` — non-blocking.

---

## 1. Pass / fail summary

| Check | Result | Notes |
|-------|--------|--------|
| Hugo build | **PASS** | 194 ms, no errors |
| Broken internal links | **PASS** | 0 |
| Missing images (parsed `src` / photo paths) | **PASS** | 0 broken targets in audit parser |
| Multiple H1 on content pages | **PASS** | 0 multi-H1 |
| Zero H1 | **WARN** | only `/ru/index.html` (language shim; root `/` and `/en/` have H1) |
| hreflang present on section pages | **PASS** | 0 missing on scanned content pages |
| hreflang targets resolve | **PASS** | 0 broken |
| Kitchen paths in public HTML | **PASS** after album fix | was residual empty “Источник альбома / Сырые файлы” in search index |
| Medal 1999 on T.P. pages | **PASS** | 0 on bio / album / documents |
| Medal series МН 178440 public | **PASS** | 0 |
| “Последний год жизни” / medical wording | **PASS** | 0 |
| June 1929 public wording | **PASS** | 0 (July album caption in use) |
| Tatyana bio 02.09.1926–24.09.2021 | **PASS** | home + about page |
| 21/IV–1926 | **PASS** | diplomatic chart only + disclaimer |
| RU/EN diary translationKey parity | **PASS** | 13+13 pairs match |
| Diary `weight` 5…120 | **PASS** | all chapter files |
| Chapter prev/next nav | **PASS** | diary chapters |
| Archive post-meta (manuscript) | **PASS** | original_page · first_pass · сверка · опубликовано |
| Draft templates not published | **PASS** | `_template` / `_shablon` draft:true |
| `work/` not in git | **PASS** | untracked only |
| `inbox/` raw media not mass-committed | **PASS** | 36 tracked README/notes only |
| Deployed to сжс.рф (`main`) | **FAIL / pending** | branch pushed; **not merged to main** → production may lag |

---

## 2. Content structure (diary)

| weight | RU | EN |
|-------:|----|----|
| 5 | o-tetradi | about-the-notebook |
| 10…100 | 00–09 (B01) | 00–09 |
| 110 | 10 · 080–089 | 10 |
| 120 | 11 · 090–098 (+ 099–100 withheld note) | 11 |

**B02:** narrative published for **080–098**; **099–100** medal withheld (`document_id` `doc-b02-medal-zahysnyku-vitichyzny`, person = Timofey **Timofeevich**); scans **099–161** in git for archive numbering.

---

## 3. Factual / privacy

| Topic | Status |
|-------|--------|
| Ukrainian medal 1999 | Uncle Tyoma only; not on T.P. materials |
| Pravda “О Дзержинском” | Public: **20 July 1929** (album caption, `source_caption_only`) |
| Living-relative full birth day/month | Chart privacy note present; year-only for living in public wording |
| Phones | 0 `+7…` in content |
| Medal serial | not published |

**1924** hits in diary are **Party membership years in delegate lists**, not Tatyana’s birth year — OK.

---

## 4. Medium findings (not blockers)

### 4.1 Editorial kitchen still inside manuscript prose (ch. 08)

Visitor HTML for `08-otec-harakter` still contains operator notes such as:

- «скан в сырье перевёрнут»
- «offline-batch … не подтверждены»
- «PAGE 060»

These are **inside** the reading text / remarks (not mid-chapter People tables — those are in `<details>` at end).  
**Recommendation:** rewrite as short archival notes or move into `<details>` / docs.

### 4.2 `/ru/index.html`

Zero H1 and odd `<title>` (URL-like). Root `public/index.html` is the real RU home with H1. Confirm language routing / redirects on GitHub Pages.

### 4.3 Dual transcription modes

No “Связный текст / По строкам” UI yet. Public text uses joined reading form + page markers; full diplomatic line-breaks not dual-mode.

### 4.4 Photo album residual (fixed in audit pass)

RU album had leftover line after path redaction:

`Источник альбома: . Сырые файлы для работы: .`

**Fixed** in content; rebuild before merge.

### 4.5 Tags still say «дневник»

UI tags/categories retain “дневник” (URL `/dnevnik/` intentionally stable). Home copy uses «рукописная тетрадь». Optional later: softer public tag labels without URL change.

### 4.6 B02 chapters 101–161

Scans present; **no** published chapter markdown yet (except inventory/transcripts in inbox).

---

## 5. Control commands re-run (expectations)

```bash
hugo --minify
# broken links / missing imgs: 0 (HTML parser audit)

rg -n -i 'Захиснику|Вітчизни|Defender of the Fatherland' \
  public/roditeli public/en/parents public/foto public/en/photos
# expect: 0

rg -n -i 'последний год жизни|last year of her life' public
# expect: 0

rg -n '20\.06\.1929|20 июня 1929|20 June 1929' content public
# expect: 0

rg -n -i 'inbox/|FACTS EXTRACTED|Извлечённые факты' public
# expect: 0 visitor-facing
```

---

## 6. Git / deploy checklist

| Step | Status |
|------|--------|
| Commits on feature branch | yes |
| Push `origin/task/final-archive-editorial-fixes-2026-08` | yes |
| Merge → `main` | **not done** |
| GitHub Pages success | **not verified on production** |
| Production URL spot-check | pending after merge |

Suggested production smoke after merge:

- https://сжс.рф/
- https://сжс.рф/vospominaniya/dnevnik/
- https://сжс.рф/vospominaniya/dnevnik/01-moya-mama/
- https://сжс.рф/vospominaniya/dnevnik/11-prodolzhenie-090-099/
- https://сжс.рф/roditeli/samsonov-timofey-petrovich/
- https://сжс.рф/foto/samsonov-timofey-petrovich/
- https://сжс.рф/en/memoirs/diary/01-my-mother/

---

## 7. Verdict

**Site quality for merge-ready feature branch: GOOD (with medium follow-ups).**

Blockers for calling production “done”: **merge to main + Pages run + smoke URLs**.  
No critical broken links, missing images, medal mis-attribution to T.P., or Tatyana birth/death regressions found in this audit build.
