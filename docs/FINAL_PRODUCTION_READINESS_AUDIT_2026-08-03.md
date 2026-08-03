# Final production readiness audit — 2026-08-03

**Project:** Слово Живой Судьбы / сжс.рф  
**Repo:** A-Krivoshen/slovo-zhivoy-sudby  
**Mode:** night total audit on `main`  
**Initial HEAD:** `df97e884b34d588ba5b53ae944f117154068b11d`  
**Final HEAD:** `27a8de0dff9e8e50b4f149aa3a9db2c0fcfce0e9`  
**Backup tag:** `backup-before-final-night-readiness-audit-2026-08-03`  
**GitHub Pages:** success (`30846018871`)  
**Auditor:** Grok Builder (automated)

---

## 1. Initial state

| Check | Result |
|---|---|
| Branch | `main` |
| Working tree | clean at start |
| `origin/main` | up to date after fetch/pull |
| Prior work | KP 2011 interview, T.P. deep bio, subjectOf JSON-LD on main |
| `sudo -v` interactive | **failed** (no TTY password prompt) |
| `sudo -n true` | **OK** (passwordless sudo available) |
| Shutdown plan | `sudo -n shutdown -h +1` after report |

---

## 2. Content inventory

| Metric | Value |
|---|---|
| Hugo build | **PASS** (`hugo --minify`, ~1s) |
| Pages RU / EN | **293 / 277** |
| Paginator pages | 11 / 7 |
| Aliases | 106 / 97 |
| Static files | 237 |
| HTML in `public/` | ~583 |
| Search index RU / EN | 75 / 73 items |
| `static/photos` | ~210 JPG (+ webp, notes) |
| `public/` size | ~60 MB |
| Graph | 13 people, 13 events, 17 places, 10 letters, 7 documents, 24 photos, 120 relations — **OK** |
| Figure parity RU/EN | **OK** |

Largest assets (document as performance notes):

- `photos/tatyana-tt/grave-plaque-2021.jpg` ~1.4 MB  
- several notebook page scans ~0.6–0.8 MB  

---

## 3. RU/EN parity

| Class | Count / notes |
|---|---|
| Shared `translationKey` | **87** |
| RU-only intentional hubs | **2**: `diary-13-hub-legacy`, `diary-17-hub-legacy` (`robotsNoIndex: true`) |
| EN-only keys | **0** |
| Central people / memoirs / documents / places | EN present |
| Cyrillic in EN body | **Intentional** in letter transcriptions and original-language titles (not UI leak) |
| EN lag phrases (`use RU`, `EN may`, etc.) | **Not found** as visitor lag disclaimers |

Parity verdict: **exact parity for public content keys; 2 intentional RU-only hubs.**

---

## 4. People and biographies

| Person | Public page | Identity notes |
|---|---|---|
| Tatyana T. | `/lyudi/…` full | **1926-09-02 – 2021-09-24**; chart `21/IV–1926` diplomatic only; KP 2011 + `subjectOf` |
| Aleksandr D. | full RU/EN | 1926–1988; not conflated with living namesake |
| T. P. Samsonov | **canonical people** | full bio; Babiy/Foma alternateName; parents album **noindex** |
| Eva K. | full | mother; KP night-fear as daughter’s memory |
| Tyoma (T.T.) | full | **not** T.P.; Stalingrad medal |
| Genya | limited full | first-marriage daughter of T.P. |
| D. A. Krivoshein | parents bio | father of Aleksandr |
| Nina V. | full | mother of Aleksandr |
| Dmitry (103–104) | evidence_limited | **no surname** |
| Misha Friolenko | evidence_limited | letter 128–129 |
| Gennady | evidence_limited | letters 131–133 |

Duplicate biographies T.P. people vs parents: **resolved earlier** (parents = album + noindex).

---

## 5. Photos and media

| Check | Result |
|---|---|
| Withheld 099–100 in public HTML | **not linked**; files **absent** from `public/photos/dnevnik-tt/` |
| Image sitemap | present via `xmlns:image` in language sitemaps |
| Lazy loading | yes on figures |
| Lightbox | `assets/js/lightbox.js` (~382 lines): open/close, pinch, pan, wheel, double-tap, Esc, arrows, +/- , focus return, swipe at zoom 1×, RU/EN hints |
| Real-device touch | **not** automated (documented limitation) |

**Fixed this pass:** captions starting with `1934.` / `1938.` were parsed as Markdown ordered lists (`<ol start=1934>`), breaking figcaptions. Rewrote to `1934 — …` with explicit `alt` on affected figures (RU/EN diary + photo album).

---

## 6. Internal linking

| Check | Result |
|---|---|
| Relative/internal hrefs (after URL-decode) | **0 broken** content targets |
| Taxonomy/people RSS paths | exist under PaperMod taxonomies |
| Canonical T.P. links | 61+ still point to parents album (OK as secondary) and people full bio |
| Orphan critical entities | none found for central people |

---

## 7. SEO

| Item | Status |
|---|---|
| `sitemap.xml` index | RU + EN child sitemaps |
| Language sitemaps | hreflang + image entries |
| `robots.txt` | present, allows public surface |
| Canonicals | on person/content pages |
| hreflang | present on content pages |
| Duplicate T.P. bio | prevented (parents noindex) |
| Search `index.json` | live, includes KP/Babiy/etc. terms |

---

## 8. Structured data (JSON-LD)

| Type | Approx. count |
|---|---|
| WebSite / Organization | site-wide |
| Person | 20 (RU+EN people with entity_id) |
| Place | 12 |
| Event | 12 |
| CreativeWork | 38 |
| BlogPosting / BreadcrumbList | PaperMod defaults |

Notable:

- Tatyana: `subjectOf` → external `NewsArticle` (KP 2011, no `articleBody`)  
- T.P.: `sameAs` Wikipedia RU/EN + Wikidata  

---

## 9. AI-ready

| Asset | Status |
|---|---|
| `llms.txt` | present, public TOC |
| `ai.txt` | present |
| Source registry | `data/archive/public/documents.yaml` + claims |
| Graph integrity | **PASS** |
| Private paths | not in llms public list for 099–100 |

---

## 10. Accessibility

| Item | Status |
|---|---|
| Content figure alts | generally from caption/alt; **fixed** year-list regressions |
| Tracker pixels (Yandex) | empty alt intentional |
| Skip link | present in base layout |
| Lightbox focus | close button focus + restore lastFocus |
| Manual a11y audit (screen reader) | **not** run tonight — limitation |

---

## 11. Performance

| Item | Status |
|---|---|
| CSS/JS assets | ~116 KB under `public/assets` |
| Public total | ~60 MB (photo-heavy, expected) |
| Largest image | grave plaque ~1.4 MB — **low-priority** recompress candidate |
| Minify build | yes |

---

## 12. Privacy

| Rule | Status |
|---|---|
| Living people: year only | observed on public people pages |
| Medal 099–100 / МН number | not public HTML; withheld in data |
| Local paths `/home/slon` | not in visitor content |
| Late entrance from KP 2011 | not published |
| Historical apt 223 / entrance 12 | remains on letter/notebook source pages only (documented policy), not place card |

---

## 13. Build / tests

| Command | Result |
|---|---|
| `hugo --minify` | PASS |
| `scripts/check_graph_integrity.py` | PASS |
| `scripts/check-figure-parity.sh` | PASS |
| Internal link scan | PASS (0 broken after unquote) |
| Production smoke (19 URLs) | all **200** |

---

## 14. Production

Host: GitHub Pages, custom domain **сжс.рф** (`xn--f1avb.xn--p1ai`).

Sample checks (all HTTP 200):

- `/`, `/en/`  
- Tatyana, Aleksandr, T.P. RU/EN  
- KP source card, Serafimovich place  
- Diary index RU/EN, timeline, search  
- `llms.txt`, `robots.txt`, `sitemap.xml`, `index.json`  

---

## 15. Fixed issues (this audit)

1. **Markdown ordered-list bug** in figure captions (`1934.` / `1938.`) → rewritten with em dash + explicit `alt` (6 files RU/EN).  
2. Audit documentation consolidated in this file.

No critical identity or privacy regressions found requiring content removal.

---

## 16. Remaining issues

| Priority | Item |
|---|---|
| Low | Recompress `grave-plaque-2021.jpg` / large page scans |
| Low | Expand Aleksandr Person JSON-LD `sameAs` if Wikimedia/Wikidata IDs confirmed later |
| Manual | Real-device pinch/pan/lightbox QA (iOS Safari / Android Chrome) |
| Manual | Full screen-reader pass |
| Family/archive | 1938 arrest vs dismissal dual-layer remains open in T.P. conflicts |
| Family/archive | Death-year 1956 handbook variants retained only as conflict notes |
| Intentional | 2 RU diary hubs noindex; parents T.P. album noindex |

---

## 17. Final verdict

### **PRODUCTION READY WITH DOCUMENTED MINOR LIMITATIONS**

Rationale:

- Build, graph, figure parity, links, production smoke, RU/EN parity for content keys: **green**  
- Privacy withheld material: **not exposed in public HTML**  
- SEO / JSON-LD / AI surface: **present and coherent**  
- Residual items are **non-blocking** (image weight, real-device touch, open historical conflicts already disclosed on pages)

---

## 18. Shutdown status

- Interactive `sudo -v` unavailable (no TTY).  
- `sudo -n` works → scheduled: `shutdown -h +1` after final commit/push/Pages if required.  

---

## Commits from this audit

See git log after push (figure caption fixes + this report).

---

Русская и английская версии семейного архива прошли итоговый production-readiness аудит: контент, биографии, фотографии, внутренняя перелинковка, SEO, JSON-LD, AI-ready структура, accessibility, performance и privacy проверены; изменения опубликованы в main, GitHub Pages и production проверены.
