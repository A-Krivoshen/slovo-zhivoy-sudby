# Слово Живой Судьбы / Word of a Living Fate

Семейный архив о жизни **Кривошеиной Татьяны Тимофеевны**: мемуары, родители, исторический контекст, фото и документы.

- Сайт: https://сжс.рф/
- Стек: [Hugo](https://gohugo.io/) + [PaperMod](https://github.com/adityatelange/hugo-PaperMod)
- Языки: русский (по умолчанию), English (`/en/`)

## Локальная разработка

```bash
git submodule update --init --recursive
hugo server -D
```

## Новая запись (мемуар)

```bash
hugo new content/ru/vospominaniya/nazvanie.md --kind memoir
# English twin:
hugo new content/en/memoirs/name.md --kind memoir
```

У связанных переводов укажите одинаковый `translationKey` во front matter.

## Разделы

| RU | EN | О чём |
| --- | --- | --- |
| `/vospominaniya/` | `/en/memoirs/` | Мемуары о Татьяне Тимофеевне |
| `/roditeli/` | `/en/parents/` | Родители |
| `/istoriya/` | `/en/history/` | Исторические факты |
| `/foto/` | `/en/photos/` | Фотоархив |
| `/dokumenty/` | `/en/documents/` | Документы |
| `/search/` | `/en/search/` | Поиск (Fuse.js) |

## Inbox (сырьё для разбора)

Рабочая папка **для семьи и разбора с ИИ**, не для сайта:

- `inbox/scans/memoirs/` — фото рукописных мемуаров  
- `inbox/scans/photos/` — семейные фото на разбор  
- `inbox/scans/documents/` — документы  
- `inbox/transcripts/` — расшифровки до публикации  
- `inbox/notes/` — заметки и вопросы  

Сами фото в git **не коммитятся** (см. `.gitignore`). Подробности: [`inbox/README.md`](inbox/README.md).

## Деплой

GitHub Actions → GitHub Pages при push в `main`.
