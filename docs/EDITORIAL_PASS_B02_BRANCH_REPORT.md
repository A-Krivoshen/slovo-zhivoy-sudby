# Отчёт: editorial pass на ветке `task/b02-editorial-coverage-fix`

**Ветка:** `task/b02-editorial-coverage-fix`  
**Не:** merge в `main`, **не** production Pages.  
**Контрольная точка:** `9874db5` (empty control) → последующий editorial commit.

---

## 1. Исправленная coverage matrix

Файл: [`docs/COVERAGE_MATRIX_001_161.csv`](COVERAGE_MATRIX_001_161.csv)

| `result_status` | n | Смысл |
|-----------------|--:|--------|
| **partial_public** | **144** | Есть URL/текст, но **не** complete_public (в т.ч. bulk first_pass, B01 без HTML-аудита complete) |
| **published_document** | **11** | 103–107, 108, 128–129, 131–133 |
| **alternate_scan** | **4** | 006, 060, 068, 102 |
| **internal_privacy** | **2** | 099–100 |
| **complete_public** | **0** | Ни одна страница не объявлена complete без HTML-аудита |
| **missing_public** | **0** | Нет «пустых» страниц без любого публичного следа |

Колонка `en_status`:

- `en_available` — EN глава есть (B01, EN 10–11)
- `en_document_ok` — EN документ (письма, Сталинград)
- `translation_incomplete` — EN 12–18 **draft**, не в сборке
- `internal` — 099–100

Quality-флаг для 109–160: `scan_visible_but_editorial_work_pending`.

### Что снято с «complete / published_text»

Ранее **144** страниц числились `published_text` (как будто готовы).  
Теперь они **`partial_public`** — потому что bulk first_pass / нет editorial complete / EN incomplete.

**Ни один** JPG-only статус не считается публикацией.

---

## 2. Полноценные / рабочие RU-главы (B02)

| URL | Название | editorial_status |
|-----|----------|------------------|
| `/vospominaniya/dnevnik/10-prodolzhenie-080-089/` | Продолжение истории Тимофея Петровича; сестра Геня | structure_pass |
| `/vospominaniya/dnevnik/11-prodolzhenie-090-099/` | Сестра Геня и брат Тёма | structure_pass |
| `/vospominaniya/dnevnik/12-brat-front-103-108/` | Дядя Тёма: документы и Сталинград | structure_pass (указатели к документам) |
| `/vospominaniya/dnevnik/13-shkola-druzya-109-119/` | Таня: детство и школа; школа и война | structure_pass |
| `/vospominaniya/dnevnik/14-voyna-evakuaciya-120-127/` | Школа и война: эвакуация | structure_pass |
| `/vospominaniya/dnevnik/15-pisma-voennye-128-133/` | Письма товарищей военных лет | structure_pass |
| `/vospominaniya/dnevnik/16-druzya-pobeda-134-139/` | Юность и знакомство с Сашей | structure_pass |
| `/vospominaniya/dnevnik/17-krym-semya-140-149/` | Крым, Севастополь, учёба и начало семьи | structure_pass |
| `/vospominaniya/dnevnik/18-synovya-150-161/` | Семья и дети: Митя и Серёжа | structure_pass |

Структура страницы: **Чтение** + `<details>Как в рукописи</details>`; prev / оглавление / next.  
Главы **12** и **15** не дублируют письма — ведут в коллекцию документов.

---

## 3. EN-главы

| EN глава | Статус |
|----------|--------|
| 00–09 | публикуются (как раньше) |
| **10–11** | **public**, английский текст |
| **12–18** | **`draft: true`**, `translation_status: incomplete` — **не** в `hugo` output, **не** в EN-оглавлении |
| Письма + Сталинград EN | public documents |

Вариант **B** (не публиковать EN с русским телом).  
`translation_status: synchronized` **не** используется при русском теле.

---

## 4. Восемь URL писем (RU)

1. `/dokumenty/pisma-s-fronta/pismo-103-1943/`  
2. `/dokumenty/pisma-s-fronta/pismo-104/`  
3. `/dokumenty/pisma-s-fronta/pismo-105-106-mamochke/`  
4. `/dokumenty/pisma-s-fronta/pismo-107/`  
5. `/dokumenty/pisma-s-fronta/pismo-128-129-tane-ot-tovarishcha/`  
6. `/dokumenty/pisma-s-fronta/pismo-131-tanyusha/`  
7. `/dokumenty/pisma-s-fronta/pismo-132-gennadiy-18-11-1943/`  
8. `/dokumenty/pisma-s-fronta/pismo-133-gennadiy-29-11-1943/`  

Индекс: `/dokumenty/pisma-s-fronta/`

**Авторы (публично):**

- **103–104:** Дмитрий — *фамилия и точная связь с семьёй пока не установлены*  
- **105–107:** Тимоша (форма из источника; не авто-«Тёма»)  
- **128–129:** Миша Фриоленко (**не** брат Тёма)  
- **131–133:** Геннадий / Геннадий Вохминцев  

---

## 5. Фотографии (реальные страницы)

**Страница:** `/foto/tetrad-semya-prodolzhenie/` (+ EN)

| Стр. | Файл static | В галерее |
|------|-------------|-----------|
| 148 | `archive-b02/b02-mp069-ph01.jpg` | да |
| 161 | `b02-mp082-ph01/02/03.jpg` | да |
| 146 | `b02-mp067-ph01.jpg` | да |
| 101 | `dnevnik-tt/str-101.jpg` (один best) | да; 102 alternate only |
| 155, 157 | full-page `str-155/157` | блок **privacy** — ждут identity review |

Также crops: 080, 081, 086, 092, 093, 117, 147, 151, 153, 154, 159.

---

## 6. Privacy / identity (открыто)

| Вопрос | Статус |
|--------|--------|
| Дмитрий 103–104 | личность не установлена |
| Тимоша ↔ Тёма | не авто-отождествлять форму имени |
| Даты 104/107/108 vs PDF-аудит | расхождения со сканом зафиксированы |
| 099–100 UA-медаль | internal; **не** у Т. П. |
| 155/157, живые | full-page only; day/month DOB не в тексте |
| Митя/Серёжа DOB | публично год-only |

---

## 7. Public first_pass

- Front matter: `transcription_status: first_pass` **оставлен** (не рендерится `post_meta.html`)  
- Visitor HTML: без first_pass / batch_id / coverage jargon  

---

## 8. Hugo

```
hugo --minify  (clean public/)
RU pages: 192 | EN pages: 183
EN drafts 12–18 excluded
```

---

## 9. Merge / Pages

**Не выполнено** (по указанию).  
После review: commit на ветке → (позже) PR → main → Pages.
