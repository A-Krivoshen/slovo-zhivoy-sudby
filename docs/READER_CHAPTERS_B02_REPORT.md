# Отчёт: читательские главы B02 (feature branch)

**Ветка:** `task/b02-editorial-coverage-fix`  
**Merge main / Pages:** **не** выполнялись.

## Коммиты (этапы)

См. `git log` на ветке. Этапы: baseline → childhood/war → sasha/crimea/family → inserts → privacy.

## Новые RU-главы (потоки 5–6, 8–11)

| URL | title | source_pages (FM only) |
|-----|-------|------------------------|
| `/vospominaniya/dnevnik/13-tanya-detstvo-i-shkola/` | Таня: детство и школа | 109–117 |
| `/vospominaniya/dnevnik/14-shkola-i-voyna/` | Школа и война | 118–127 |
| `/vospominaniya/dnevnik/16-yunost-i-sasha/` | Юность и знакомство с Сашей | 134–139 |
| `/vospominaniya/dnevnik/17-krym-sevastopol-semya/` | Крым, Севастополь и начало семьи | 140–144 |
| `/vospominaniya/dnevnik/18-ucheba-rabota-vypuskniki/` | Учёба, работа и встречи выпускников | 145–148 |
| `/vospominaniya/dnevnik/19-semya-i-deti/` | Семья и дети | 149–161 |

Старые bulk-файлы `13-shkola-druzya…`, `14-voyna-evakuaciya…`, `16-druzya…`, `17-krym-semya…`, `18-synovya…` **удалены**.

Принцип: голос Т. Т., соединение переносов, подзаголовки по смыслу источника, фото у эпизодов, дипломатия в `<details>`, **[?]** без домыслов.

## Документы (п. 2)

- `/dokumenty/pisma-s-fronta/pismo-vstavka-sestre-089-090/`
- `/dokumenty/pisma-s-fronta/otkrytka-130-novyj-god/`

## Privacy 155/157 (п. 3)

- Не в `/foto/tetrad-semya-prodolzhenie/`
- Matrix: `internal_privacy`
- Без публичного «withheld»-блока

## EN

- 12–18 по-прежнему **draft**
- Полный EN-перевод — после стабилизации RU (не в этом отчёте)

## Спорные даты (не подгонялись)

- 103/104: Дмитрий  
- 107: 13.07.44 Тимоша  
- 108: 23.09.1943 на бланке  
- 128–129: Миша Фриоленко  
- Митя: публично год 1948  

## Hugo

`hugo --minify` clean: RU ~203, EN ~183
