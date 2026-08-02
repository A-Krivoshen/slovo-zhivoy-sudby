# Family portrait coverage audit

**Date:** 2026-08-02  
**Scope:** Genealogy charts (notebook pp. 002–006), person pages, albums, text mentions of portraits.  
**Identity rule:** caption / tree node / document / family confirmation only — never face matching.

**Backup tag:** `backup-before-family-portraits-lightbox-total-audit-2026-08-02`  
**Baseline HEAD before pass:** `559e992`

---

## Working table

| mention_text | language | content_path | person_or_group | current_public_image | image_exists_in_repo | source_page_or_tree | identity_evidence | crop_exists | public_page_exists | person_entity_exists | linked_from_person | linked_from_tree | linked_from_album | linked_from_related | search_indexed | image_sitemap | status | action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| «Моя мама» / polka-dot dress | ru+en | `00-oblozhka` / `00-cover-and-charts` | Eva Konstantinovna | `/photos/eva-konstantinovna/chart-portrait.jpg` | yes | p.002 leaf | caption «Моя мама» | yes | yes | person-samsonova-ek | yes | yes | yes | yes | via page | in page sitemap images | complete_visible | keep |
| Eva album portrait | ru+en | person + parents | Eva | `/photos/eva-konstantinovna/eva-portrait.jpg` | yes | album | manuscript + prior publish | yes | yes | yes | yes | n/a | yes | yes | yes | yes | complete_visible | keep (distinct from chart) |
| Т.П. on Samsonov chart | ru+en | chart + person | Timofey Petrovich | `/photos/samsonov-tp/chart-portrait.jpg` | yes | p.003 node | node years 1888–1955 | yes | yes | person-samsonov-tp | yes | yes | yes | yes | yes | yes | complete_visible | keep |
| Т.П. studio oval | ru+en | person + album | Timofey Petrovich | `/photos/samsonov-tp/05-studio-moscow-oval.jpg` | yes | album | editorial curated album | yes | yes | yes | yes | n/a | yes | yes | yes | yes | complete_visible | primary cover remains studio |
| «Моя сестра Геня» | ru+en | chart + person | Genya / Evgenia | `/photos/genya-samsonova/chart-portrait.jpg` | yes | p.003 | caption on node | yes | yes | person-genya-samsonova | yes | yes | yes | yes | yes | yes | complete_visible | cover switched to chart portrait |
| Young man in cap — husband of Samsonova T.T. | ru+en | chart + person | Aleksandr D. | `/photos/aleksandr-krivoshein/chart-young-portrait.jpg` | yes | p.004 husband node | chart label «муж Самсоновой Т.Т.» | yes | yes | person-alexander-krivoshein | yes | yes | yes | yes | yes | yes | complete_visible | full p.004 leaf not published (living) |
| A.D. formal portrait | ru+en | person + album | Aleksandr D. | `/photos/aleksandr-krivoshein/portrait.jpg` | yes | family print | family_confirmed 2026-08-02 | yes | yes | yes | yes | n/a | yes | yes | yes | yes | complete_visible | keep |
| Nina on Krivoshein chart | ru+en | chart + person + album | Nina Vasilievna | `/photos/nina-vasilievna-krivosheina/portrait.jpg` | yes | p.005 node | node «Кривошеина (Петрова) Нина Васильевна» 1907–1991 | yes | yes | person-nina-vasilievna-krivosheina | yes | yes | yes | yes | yes | yes | complete_visible | str-005 full leaf published as context |
| Tatyana garden portrait | ru+en | person + album | Tatyana T. | `/photos/tatyana-tt/garden-portrait.jpg` | yes | family print | family_confirmed 2026-08-02 | yes | yes | person-krivosheina-tt | yes | n/a | yes | yes | yes | yes | complete_visible | keep |
| Portrait of Sergey | ru+en | chart p.004 | Sergey A. (living) | — | master only | p.004 | chart node (living) | no public | no person page | no public entity | no | text only | no | no | no | no | private | do not crop/publish |
| Dmitry and Bella, young | ru+en | chart p.004 | Dmitry A. + spouse (living) | — | master only | p.004 | chart; label **Белла** (not «Вела») | no public | no person pages | no | no | text only | no | no | no | no | private | do not crop; spelling Bella/Белла |
| Grandchildren portraits on p.004 | ru+en | chart | living | — | master only | p.004 | living | no | no | no | no | text | no | no | no | no | private | withhold |
| Three male portraits lower right p.005 | ru+en | chart p.005 | unknown males | — | in str-005 only | p.005 | no individual captions | no | no | no | no | candidate note | no | no | no | no | candidate_requires_family_confirmation | show full leaf only |
| D.A. Krivoshein (1905–1979) portrait | ru+en | chart text | Dmitry Aleksandrovich Sr | — | not isolated | p.005 | name on chart; no clear portrait crop labeled as him | no | parents page exists | person-krivoshein-da | no portrait | tree text | no | no | n/a | no | text_only_no_image_found | need family confirmation of any portrait |
| User phrase «Вела» | internal | — | spouse of Dmitry Jr | — | — | p.004 | chart reads **Белла** | — | — | — | — | — | — | — | — | — | — | publish chart spelling; keep «Вела» as internal search note only |

---

## Chart node map (portraits)

### p.002 — mother leaf
| exact label | years | spouse/parent context | source | confidence | person entity | public crop |
|---|---|---|---|---|---|---|
| Моя мама / Самсонова (Морозова) Ева Константиновна | 1900–1981 | mother of T.T. | str-002 + chart-portrait | high | person-samsonova-ek | yes |

### p.003 — Samsonovs
| exact label | years | context | source | confidence | person | public crop |
|---|---|---|---|---|---|---|
| Самсонов Тимофей Петрович | 1888–1955 | father | str-003 + chart-portrait | high | person-samsonov-tp | yes |
| Самсонова Евгения Тимофеевна / «Моя сестра Геня» | — | daughter 1st marriage | chart-portrait | high | person-genya-samsonova | yes |
| Самсонов Тимофей Тимофеевич | b. 1923 | son | — | high as name | person-samsonov-tt | no individual chart crop (uses album B02) |
| Самсонова (Кривошеина) Татьяна Тимофеевна | chart date note | daughter | garden portrait separate | high | person-krivosheina-tt | yes (album, not chart crop) |

### p.004 — Krivoshein nuclear (husband + children)
| exact label | years | context | public? |
|---|---|---|---|
| Кривошеин Александр Дмитриевич — муж Самсоновой Т.Т. | 1926–1988 | husband | **yes** chart-young-portrait |
| Кривошеин Дмитрий Александрович + Белла, children | living | son branch | **private** |
| Кривошеин Сергей Александрович + family | living | son branch | **private** |

Full leaf str-004 **not** published (living portraits on same sheet).

### p.005 — Krivosheins (parents of husband)
| exact label | years | public? |
|---|---|---|
| Кривошеин Дмитрий Александрович | 1905–1979 | name only; no isolated portrait |
| Кривошеина (Петрова) Нина Васильевна | 1907–1991 | **yes** portrait + str-005 context |
| Three male portraits (unlabeled) | ? | **candidates** only |

---

## Photo entities added this pass

| entity_id | src | people |
|---|---|---|
| photo-eva-konstantinovna-chart-portrait | `/photos/eva-konstantinovna/chart-portrait.jpg` | Eva |
| photo-samsonov-tp-chart-portrait | `/photos/samsonov-tp/chart-portrait.jpg` | T.P. |
| photo-genya-samsonova-chart-portrait | `/photos/genya-samsonova/chart-portrait.jpg` | Genya |
| photo-aleksandr-dmitrievich-chart-young-portrait | `/photos/aleksandr-krivoshein/chart-young-portrait.jpg` | A.D. |
| photo-chart-krivosheins-leaf-005 | `/photos/dnevnik-tt/str-005.jpg` | context (Nina) |

Prior entities retained: photo-eva-portrait, photo-album-samsonov-tp-05, photo-tatyana-*, photo-aleksandr-dmitrievich-portrait-undated, photo-nina-vasilievna-chart-portrait, B02 set.

---

## Person-page cover summary

| person | cover image | status |
|---|---|---|
| Eva | eva-portrait.jpg | complete |
| T.P. | 05-studio-moscow-oval.jpg | complete (+ chart in body) |
| Genya | chart-portrait.jpg | complete (updated this pass) |
| Aleksandr | portrait.jpg formal | complete (+ chart young in body) |
| Nina | chart portrait | complete |
| Tatyana | garden portrait | complete |
| Tyoma | album/wartime as before | complete (no new chart crop) |
| Living sons | — | no public person pages / no portraits |

---

## Lightbox (2026-08-02)

| feature | status |
|---|---|
| Pinch zoom | yes (pointer events, 2-finger) |
| Pan when zoomed | yes |
| Double-tap / double-click reset or 2.5× | yes |
| Wheel zoom (desktop) | yes |
| Keyboard Esc / arrows / + − / 0 | yes |
| Bounds clamp | yes (basic) |
| Focus return on close | yes |
| Hint RU/EN by `html[lang]` | yes |
| CSS stage/viewport/hint/is-zoomed | aligned with JS |
| Full p.004 living crops | N/A (not published) |

---

## Privacy

- Living: year-only + relationship text; **no** portrait crops from p.004 living nodes.
- Private notebook pages 099, 100, 155, 157: still excluded from photos.yaml / public figures.
- No generative face restore / recolor / upscale-to-fake-HD.

---

## Candidates for family confirmation

1. **Three male portraits** lower-right on p.005 — who are they (D.A.? relatives?).
2. **Any portrait of D.A. Krivoshein (1905–1979)** if one exists outside unlabeled cluster.
3. **Whether any living-person chart portraits** may ever be published (explicit opt-in).
4. Internal note only: user said «Вела» — chart/manuscript form is **Белла**.

---

## RU/EN parity (this pass)

| page | RU | EN |
|---|---|---|
| Cover & charts | figures + privacy notes | matched |
| Eva / T.P. / Genya / Aleksandr people | chart figures | matched |
| Album tetrad / notebook-family | chart block added | matched |
| Nina on chart leaf | figure + str-005 | matched |

---

## Status counts (chart + confirmed family portraits)

| status | count (approx.) |
|---|---|
| complete_visible | 9+ primary portraits |
| private (living chart) | Sergey, Dmitry+Bella, grandchildren |
| candidate_requires_family_confirmation | 3 unlabeled males p.005; D.A. isolated portrait |
| text_only_no_image_found | D.A. dedicated portrait |
| duplicate avoided | chart vs studio (T.P.); chart young vs formal (A.D.); Eva chart vs album |

---

*Generated as part of family-portraits + pinch-zoom lightbox + total RU/EN audit pass.*
