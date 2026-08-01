# Аудит публикации PDF B02 / original_page 001–161

**Дата:** 2026-08-01  
**Матрица:** [`docs/COVERAGE_MATRIX_001_161.csv`](COVERAGE_MATRIX_001_161.csv)  
**Ключевой вывод:** **вторая партия (B02, original_page 080–161) не опубликована полноценно.**

---

## 1. Что считается «опубликовано»

| Форма | Код `result_status` | Что это |
|-------|---------------------|---------|
| Связный текст главы | `published_text` | Маркер `<!-- стр. NNN -->` + читательский текст в `content/ru/vospominaniya/dnevnik/` (+ EN pair) |
| Отдельный документ | `published_document` | Страница в `dokumenty/` / `documents/` |
| Фото-кроп в коллекции | `published_photo` | **Вырезка** снимка + подпись в `foto/` / `photos/` (не full-page `str-NNN.jpg`) |
| Дубль скана | `alternate_scan` | 006↔005, 060↔058, 068↔067, 102↔101 |
| Внутреннее | `internal_privacy` | 099–100 (украинская медаль Тимофея **Тимофеевича**) |
| Нужна ручная сверка | `needs_manual` | Нечитаемо / нельзя доверять first_pass |
| Ошибка покрытия | `missing_public` | Есть в PDF-архиве, нет приемлемого публичного результата |

**Жёсткое правило:** наличие JPG в `static/photos/dnevnik-tt/str-*.jpg` **само по себе не есть публикация**.

### Три разных продукта (не путать)

1. **first_pass chapter dump** — массовая расшифровка главы с full-page `str-NNN.jpg`.  
2. **document collection** — отдельные страницы документов/писем в `dokumenty/`.  
3. **photo publication** — кропы (`archive-b0N/…`) + подписи в фото-коллекции.

**first_pass dump ≠ коллекция документов ≠ публикация фото.**

---

## 2. Партии PDF

| Партия | original_page | PDF (inbox, gitignored) | Главы сайта |
|--------|--------------:|-------------------------|-------------|
| **B01** | 001–079 | `…corrected.pdf` (78 control; 068 = дубль 067) | 00–09 |
| **B02** | 080–161 | `samsonovy_new_scans_2026-08-01_corrected.pdf` (82 стр.) | 10–18 (+ 099–100 withheld) |

Карта B01: `docs/manuscript-page-map.md`.  
Стык B01→B02: `docs/manuscript-batch-2026-08-01.md` (079 Colt/портреты → 080 новый фотоколлаж).

---

## 3. Сводка матрицы (001–161)

| `result_status` | Кол-во | Комментарий |
|-----------------|-------:|-------------|
| `published_text` | **154** | Есть глава с маркером страницы |
| `alternate_scan` | **4** | 006, 060, 068, 102 |
| `internal_privacy` | **2** | 099–100 |
| `published_document` | **1** | 108 — медаль «За оборону Сталинграда» (Т. Т.) |
| `published_photo` | **0** | **Нет** ни одной страницы, где кроп опубликован в фото-коллекции |
| `needs_manual` | **0** | Отдельный статус не выставлен; см. quality / notes |
| `missing_public` | **0** | На каждую страницу есть либо текст, либо alternate/privacy |

### Quality flags (колонка `quality`)

| Флаг | ~кол-во | Смысл |
|------|--------:|-------|
| `first_pass_dump` | ~80 | B02 (и 102/108): только bulk-глава + full-page JPG |
| `first_pass` / `partially_verified` | B01 | Статус `transcription_status` глав 00–09 |
| `has_standalone_doc` | 5 | 072, 075, 076, 079, 108 |
| `has_photo_crop` | 22 | Файл кропа в `static/photos/archive-b01` или `archive-b02` |
| `internal_withheld` | 2 | 099–100 |

**JPG в static:** 93 из 161 (`str-001…003,007,009,010,012,015,022–024,080–161`).  
Для 001–079 отсутствие JPG **не отменяет** `published_text`, если страница в главе.

---

## 4. B01 (001–079) — относительно зрелый слой

| Диапазон | Глава (primary) | Статус |
|----------|-----------------|--------|
| 001–006 | 00 обложка/схемы | `published_text` (+ 006 alternate) |
| 007–010 | 01 мама | text |
| 011–014 | 02 отец/брак | text (012–013 primary 02, не 03) |
| 015–024 | 04 война | text (частично verified 022–024) |
| 025–032 | 05 ВЧК/стихи | text (028–030 primary 05) |
| 033–040, 048–050 | 03 детство | text |
| 041–047 | 06 документы/съезды | text |
| 051–057 | 07 дача | partially_verified |
| 058–071 | 08 характер | partially_verified; 060/068 alternate; много `[?]` |
| 072–079 | 09 документы в тетради | text + companion dokumenty (Colt, Правда) |

Дубли: `docs/DIARY_DUPLICATE_MAP.md`.

**B01 gaps (не блокеры партии 2, но долг):**

- Full-page JPG только у избранных страниц.  
- Кропы `archive-b01` есть (002, 022, 031, 033, 039, 073, 077–079), но **не** заведены в Hugo-галерею как `published_photo`.  
- Глава 08 — высокая неопределённость имён; continuity notes на 083 (B02) / 071 (B01).

---

## 5. B02 (080–161) — «есть дамп, нет полноценной публикации»

### 5.1 Что уже есть

- Главы **10–18** RU+EN, `batch_id: manuscript-2026-08-01-b02`, `transcription_status: first_pass`.  
- Full-page `str-080…161.jpg` в static.  
- Частичные кропы `static/photos/archive-b02/` (≈25 web-файлов).  
- Одна document-page: Сталинград 108 (`udostoverenie-oborona-stalingrada-samsonov-tt`).  
- Фото-подборка `foto/tetrad-semya-prodolzhenie` — **только full-page** str-117,147–148,151,153–155,157,159,161 (**не** кропы).

### 5.2 Чего нет (поэтому «не полноценно»)

| Требование | Факт |
|------------|------|
| Коллекция фронтовых писем (103–107, 127–133) | Только dump в гл. 12 / 14–15 |
| Автобиография Тани 109–126 как вычитанный блок | Dump в гл. 13–14 |
| Фото-кропы в `foto/` с подписями | `archive-b02` **не** подключён к content; 0× `published_photo` |
| Privacy gate 149–160 | Текст уже public first_pass — **нужен** обзор живущих |
| 099–100 | Корректно withheld; не путать с Т. П. |
| Ручная сверка first_pass | Не завершена; EN часто = RU diplomatic + label |

---

## 6. Двенадцать потоков B02: current vs required

| # | Stream | Страницы (primary в CSV) | Required | Current |
|---|--------|---------------------------|----------|---------|
| **1** | `tp_continue_080-086` | 080–086 | Текст + **фото-кропы** 080,081,086 | first_pass гл.10; кропы 080/081/086 **на диске**, не в коллекции; 084 cemetery = living_people_review |
| **2** | `genya_tyoma_087-098` | 087–098 | Связный рассказ Гени/Тёмы | first_pass гл.10–11; кропы 092–093 на диске |
| **—** | *(099–100)* | — | **internal** only | `internal_privacy`; JPG archive-only |
| **3** | `tyoma_docs_101-108` | 101–102, 108 | Экзамен (best of 101/102) + медаль 108 | 101 text+crop; **102 alternate**; **108 = published_document** |
| **4** | `front_letters_collection` | **103–107** | **Отдельная коллекция писем** в `dokumenty/` | **Только** dump гл.12 — **главный gap потока 4** |
| **5** | `tanya_childhood_109-117` | 109–117 | Автобиография + школа; фото 117 | first_pass гл.13; crop 117 на диске; full-page в tetrad-gallery |
| **6** | `school_war_118-127` | 118–127 | 7 класс / эвакуация | first_pass гл.13–14; 127 стык с письмами |
| **7** | `friends_letters_128-133` | 128–133 | Письма друзей (Вохминцев и др.) как **коллекция** | first_pass гл.15 only |
| **8** | `youth_sasha_134-139` | 134–139 | Молодость, друзья, Победа | first_pass гл.16 |
| **9** | `crimea_family_140-144` | 140–144 | Крым / семья | first_pass гл.17 |
| **10** | `study_work_145-148` | 145–148 | Учёба/работа; **фото 145–148** | first_pass; кропы 147 (+148 privacy); full-page gallery |
| **11** | `family_children_149-160` | 149–160 | Дети / поздняя семья | first_pass гл.17–18; **privacy review** |
| **12** | `photo_album_147-161` | 161 (+cross 147–160) | **Альбом кропов** с подписями | Full-page gallery only; часть crops в static без content |

**Итог по потокам:** все 12 «закрыты» first_pass-главами (кроме 099–100), но **ни один** из фото- и document-heavy потоков (1, 3–4, 7, 10–12) не доведён до требуемой формы публикации.

---

## 7. Важные фото-страницы

| op | Скан | Crop static | В `foto/` | Нужно |
|---:|------|:-----------:|:---------:|-------|
| 080 | yes | yes (mp001) | no crop | gallery + caption (Дзержинский / похороны) |
| 081 | yes | yes (mp002) | no | Александровский централ |
| 086 | yes | yes (mp007) | no | гости / Гвостуха |
| 092 | yes | yes (mp013) | no | Геня, Тёма, семья 1925 |
| 101 | yes | yes (mp022) | no | экзамен ГО — **best** frame |
| 102 | yes | yes (mp023) | — | **alternate** 101 |
| 117 | yes | yes (mp038) | full-page only | class 6«а» crop |
| 145–146 | yes | 146 yaml/privacy | no | youth/family prints |
| 147–148 | yes | 147 yes | full-page | album stream 12 |
| 151,154,157,161 | yes | partial | full-page | children/family; privacy |

---

## 8. Privacy / identity

| Тема | Правило |
|------|---------|
| **099–100** | Медаль «Захиснику Вітчизни» → **Тимофей Тимофеевич** (дядя Тёма). **Не** Т. П. Самсонов. Не в bio/album/documents отца. |
| **108** | Медаль «За оборону Сталинграда» → тоже **Т. Т.**; отдельная страница dokumenty OK. |
| **149–160** | Дети/внуки/живущие — год-only в публичных подписях; нужен privacy pass. |
| **084** cemetery crops | `living_people_review` — не web-publish без решения. |

---

## 9. Минимум следующих работ (порядок)

1. **Поток 4 + 7 — коллекции писем**  
   - Вынести 103–107 и 128–133 (и при необходимости 127) в `dokumenty/` (RU+EN), связать с людьми, не оставлять только в дампе главы.  

2. **Поток 12 (+ важные фото 1/3/5/10)**  
   - Подключить **уже существующие** `archive-b02` кропы к `foto/` (не full-page str).  
   - 101 vs 102: опубликовать **один** best crop; 102 = alternate.  
   - 080, 081, 086, 092, 117, 147, 151, 154, 157, 161 — caption from author notes only.  

3. **Privacy pass 149–160** (+ 084, 146, 148, 155, 157, 161 living)  
   - Решить publish / year-only / withhold.  

4. **Second-pass текста B02**  
   - Приоритет: 080–086 (фото+подписи), 103–108 (письма/медаль), 109–117 (автобиография), 128–133 (письма).  
   - Снять «first_pass_dump» только после ручной сверки.  

5. **Не раздувать scope B01** в этом треке, кроме явных companion-doc/photo, уже начатых.

6. **Не** публиковать 099–100, пока нет person-page дяди Тёмы и явного family decision.

---

## 10. Явные non-claims

- Матрица **не** утверждает дипломатическую точность first_pass.  
- `published_text` для B02 = «глава существует и ссылается на страницу», **не** «готово к архивной цитате».  
- `has_photo_crop` = файл в static, **не** = `published_photo`.  
- original_page 080–161 numbering: working assignment after junction QA (`manuscript-batch-2026-08-01.md`); control remains B02 merged 001–082 → op 080–161.  
- Старые аудиты (`SITE_FULL_AUDIT`, `manuscript-batch` «101–161 not published») **устарели** относительно появления глав 12–18: главы есть, **полноценной** публикации — нет.

---

## 11. Файлы-источники

| Источник | Роль |
|----------|------|
| `content/ru/vospominaniya/dnevnik/*.md` | маркеры `<!-- стр. -->`, primary text |
| `content/en/memoirs/diary/*.md` | EN pairs |
| `content/ru/dokumenty/*`, `content/en/documents/*` | standalone docs |
| `content/ru/foto/*`, `content/en/photos/*` | photo collections |
| `static/photos/dnevnik-tt/str-*.jpg` | full-page scans |
| `static/photos/archive-b0{1,2}/*` | print crops |
| `data/archive_photos/*.yaml` | manifest croпов |
| `docs/DIARY_DUPLICATE_MAP.md` | ownership / alternate |
| `docs/B02_CHAPTERS_101_161.md` | chapter theme map |
| `docs/manuscript-page-map.md` | B01 numbering |
| `docs/manuscript-batch-2026-08-01.md` | B02 batch + medal hold |
| `docs/PHOTO_ARCHIVE_UNIFIED_B01_B02.md` | crop system status |

---

## 12. Одной фразой

**B01 (001–079)** даёт читаемый каркас тетради; **B02 (080–161)** выложена как **first_pass chapter dumps + raw JPGs**, с одним сильным document (108) и заготовками кропов, но **без** коллекций писем, **без** `published_photo` и **без** privacy-закрытия семейного хвоста — то есть **вторая партия не опубликована полноценно.**


---

## 9. Прогресс после параллельной публикации (2026-08-01, вечер)

Выполнено субагентами + сборка оркестратором:

| Поток | Было | Стало |
|------:|------|-------|
| 4 + 7 Письма | только главы 12/15 | **коллекция** `/dokumenty/pisma-s-fronta/` + EN `/en/documents/letters-from-the-front/` (8 писем: чтение + дипломатическая расшифровка + prev/next) |
| 3 Сталинград 108 | dump в главе 12 | **документ** `/dokumenty/udostoverenie-oborona-stalingrada-samsonov-tt/` (Т. Т., не Т. П.) |
| 12 Фотоальбом | full-page `str-*` | **23 кропа** `archive-b02` + блок полных кадров для 146/148/155/157/161 |
| TOC B02 | «Продолжение 080–089» | **12 потоков** с якорями в оглавлении |
| 101/102 | два равных кадра | **101 primary**, 102 alternate |
| Privacy 149–160 | полные даты в тексте | год-only для рождений; адрес кв. скрыт |
| 099–100 | — | internal only (без public page) |

### Важные уточнения по сканам
- **103**: дата **11.08.1943** (не «11 мая»); подпись **«Ваш Дмитрий»** — не смешивать автоматически с Тимошей.
- **104**: **28.VII.44**, сильные повреждения; подпись «Дмитрий».
- **105–107**: **Тимоша** → родители/мама/Таня.
- **128–129**: **Миша Фриоленко**, 20.04.1943 — **не** брат Тёма.
- **108**: вручение на бланке **23.09.1943** (не 1945); № II 34769; 79 ГМП; командир В. Попов.

### Что ещё не «полноценно»
- Главы 10–18 всё ещё bulk first_pass (текст + full page), даже при наличии doc/photo параллелей.
- EN 12–18: английский lead, тело часто по-русски.
- Кропы 146, 148, 155, 157, 161 — в inbox, не в static (privacy/QA).
- Литературная шлифовка автобиографии Тани / Крым / дети — впереди.

Матрица CSV обновлена: pages 103–107, 108, 128–129, 131–133 → `published_document`.
