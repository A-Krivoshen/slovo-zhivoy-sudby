<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="Слово Живой Судьбы — семейный архив о Кривошеиной Татьяне Тимофеевне">
</p>

<p align="center">
  <a href="https://сжс.рф/"><strong>сжс.рф</strong></a>
  ·
  <a href="https://сжс.рф/en/">English</a>
  ·
  <a href="./docs/WORKFLOW.md">Инструкция</a>
  ·
  <a href="./inbox/README.md">Inbox</a>
</p>

Семейный архив о жизни **Кривошеиной Татьяны Тимофеевны**: мемуары, родители, исторический контекст, фото и документы.

- **Сайт:** https://сжс.рф/
- **Стек:** [Hugo](https://gohugo.io/) + [PaperMod](https://github.com/adityatelange/hugo-PaperMod)
- **Языки:** русский (по умолчанию), English (`/en/`)

---

<p align="center">
  <img src="./assets/readme/workflow.svg" width="100%" alt="Пайплайн: скан → inbox → разбор → transcripts → content → сжс.рф">
</p>

### Как мы работаем

1. Отец / семья фотографирует рукописи → `inbox/scans/memoirs/`
2. В чате: «разбери эту пачку»
3. Расшифровка → `inbox/transcripts/`
4. После проверки фактов → статьи в `content/ru/` + `content/en/`
5. `git push` → сайт обновляется

Полная памятка (локально и в git): **[docs/WORKFLOW.md](./docs/WORKFLOW.md)**

---

<p align="center">
  <img src="./assets/readme/section-inbox.svg" width="100%" alt="Inbox — рабочая зона">
</p>

<p align="center">
  <img src="./assets/readme/inbox-map.svg" width="100%" alt="Карта папок inbox">
</p>

Рабочая зона **для семьи и разбора**, не для сайта:

| Путь | Что класть |
| --- | --- |
| `inbox/scans/memoirs/` | Фото рукописных мемуаров |
| `inbox/scans/photos/` | Семейные фото на разбор |
| `inbox/scans/documents/` | Документы, письма |
| `inbox/transcripts/` | Расшифровки до публикации |
| `inbox/notes/` | Вопросы и уточнения |

Сами фото в git **не коммитятся** (`.gitignore`). Структура папок — да.  
Подробнее: [`inbox/README.md`](./inbox/README.md)

---

<p align="center">
  <img src="./assets/readme/section-shoot.svg" width="100%" alt="Как снимать рукописи">
</p>

1. Ровный свет, без блика  
2. Страница целиком, текст читаемый  
3. Имена: `001.jpg`, `002.jpg`…  
4. Не сжимать «в ноль»

---

<p align="center">
  <img src="./assets/readme/section-sections.svg" width="100%" alt="Разделы сайта">
</p>

| RU | EN | О чём |
| --- | --- | --- |
| `/vospominaniya/` | `/en/memoirs/` | Мемуары о Татьяне Тимофеевне |
| `/roditeli/` | `/en/parents/` | Родители |
| `/istoriya/` | `/en/history/` | Исторические факты |
| `/foto/` | `/en/photos/` | Фотоархив |
| `/dokumenty/` | `/en/documents/` | Документы |
| `/search/` | `/en/search/` | Поиск |

---

<p align="center">
  <img src="./assets/readme/section-start.svg" width="100%" alt="Старт">
</p>

### Локально

```bash
git submodule update --init --recursive
hugo server -D
```

### Новая запись (мемуар)

```bash
hugo new content/ru/vospominaniya/nazvanie.md --kind memoir
hugo new content/en/memoirs/name.md --kind memoir
```

В обоих файлах — одинаковый `translationKey`.

### README SVG

Баннеры **генерируются**, не правятся руками:

```bash
python3 scripts/generate_readme_assets.py
```

На каждый push в `main` workflow **Regenerate README SVGs** пересоздаёт файлы в `assets/readme/`.

### Деплой сайта

Push в `main` → **Deploy Hugo site to Pages** → https://сжс.рф/
