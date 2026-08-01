# Инструкция: как ведём архив «Слово Живой Судьбы»

Локальная памятка для семьи и для разбора с ИИ.  
Сайт: https://сжс.рф/ · репозиторий: этот git.

---

## О чём проект

Семейный архив о жизни **Кривошеиной Татьяны Тимофеевны**:

- её мемуары и рассказы;
- жизнь родителей;
- исторический контекст;
- фото и документы.

Языки сайта: **русский** (основной) и **английский** (`/en/`).

---

## Две зоны

| Зона | Путь | На сайт? |
| --- | --- | --- |
| **Inbox** — сырьё | `inbox/` | Нет |
| **Контент** — готовые статьи | `content/ru/`, `content/en/` | Да |
| **Статика сайта** | `static/`, `assets/` | Да (отобранное) |

В `inbox/` кладём всё «сырое». На GitHub Pages это **не публикуется**.

---

## Папки inbox

| Путь | Что класть |
| --- | --- |
| `inbox/scans/memoirs/` | Фото рукописных мемуаров (по порядку страниц) |
| `inbox/scans/photos/` | Семейные фото на разбор |
| `inbox/scans/documents/` | Документы, письма, свидетельства |
| `inbox/scans/misc/` | Пока непонятно куда |
| `inbox/transcripts/` | Расшифровки текста **до** публикации |
| `inbox/notes/` | Вопросы, «уточнить у родных» |

Сами фото/сканы в git **игнорируются** (см. `.gitignore`).  
Структура папок и README — в репозитории.

---

## Как снимать рукописи (для отца / семьи)

1. Свет ровный, без блика и жёсткой тени.
2. Страница **целиком**, текст читаемый, телефон параллельно листу.
3. Имена по порядку: `001.jpg`, `002.jpg`… или `bloknot-a-003.jpg`.
4. Не сжимать «в ноль» — нужен читаемый почерк.
5. Пачку класть в `inbox/scans/memoirs/`.

---

## Пайплайн разбора

```text
фото рукописи
    → inbox/scans/memoirs/
    → разбор (ИИ + семья)
    → inbox/transcripts/   (черновик текста)
    → проверка фактов
    → content/ru/ + content/en/   (статьи на сайт)
    → push → GitHub Pages → сжс.рф
```

В чате достаточно написать:  
«разбери `inbox/scans/memoirs/…`» — дальше расшифровка, структура разделов, черновики RU/EN.

**Не выдумываем** даты, имена и факты. Неясное помечаем: *неразборчиво*, *уточнить год*, *кто на фото*.

---

## Новая статья на сайте

```bash
hugo new content/ru/vospominaniya/nazvanie.md --kind memoir
hugo new content/en/memoirs/name.md --kind memoir
```

В обоих файлах одинаковый `translationKey` в front matter.

| RU | EN |
| --- | --- |
| `/vospominaniya/` | `/en/memoirs/` |
| `/roditeli/` | `/en/parents/` |
| `/istoriya/` | `/en/history/` |
| `/foto/` | `/en/photos/` |
| `/dokumenty/` | `/en/documents/` |
| `/search/` | `/en/search/` |

---

## Локальный запуск

```bash
git submodule update --init --recursive
hugo server -D
```

---

## README-картинки (SVG)

Красивые баннеры в README генерируются скриптом (не правятся руками):

```bash
python3 scripts/generate_readme_assets.py
```

На каждый push в `main` GitHub Action **пересоздаёт** SVG в `assets/readme/`.  
Источник правды — `scripts/generate_readme_assets.py`.

---

## Деплой сайта

Push в `main` → workflow **Deploy Hugo site to Pages** → https://сжс.рф/
