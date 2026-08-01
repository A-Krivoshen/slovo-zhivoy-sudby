# SEO meta checklist — entity pages

**Branch:** `task/archive-seo-ai-knowledge-graph`  
**Base:** `https://сжс.рф/`  
**Scope:** new entity hubs and pages — `lyudi` / `people`, `sobytiya` / `events`, `hronologiya` / `timeline`, `mesta` / `places`, `printsipy-publikacii` / `publishing-principles`.

## Rules applied

| Rule | Status |
| --- | --- |
| Unique `title`, `description`, `summary` in front matter | Yes within scope; parent/entity name collisions resolved |
| No duplicate generic hub titles | Hubs use section-specific titles (…семейного архива / …of the family archive) |
| No SEO spam | Meta is factual; no keyword stuffing or brand spam |
| `entity_id` on person/event/place leaves | Present; hubs and principles pages omit (not graph entities) |
| `robotsNoIndex` | **Not** on new entity pages. Only legacy diary split hubs (see below) |

### `robotsNoIndex` (legacy diary only)

These are **not** new entity pages; they stay noindex as redirect-style split hubs:

- `content/ru/vospominaniya/dnevnik/13-shkola-druzya-109-119.md` — title: 'Школа, друзья (разделено на две главы)'
- `content/ru/vospominaniya/dnevnik/17-krym-semya-140-149.md` — title: 'Крым и семья (разделено на две главы)'

---

## RU — Люди (`/lyudi/`)

| URL | title | description | summary | entity_id | indexable |
| --- | --- | --- | --- | --- | --- |
| `/lyudi/` | Люди семейного архива | Кто есть кто в семейном архиве: Татьяна Тимофеевна, родители Самсоновы, брат Тёма, Саша и авторы фронтовых писем. | Люди архива — короткие страницы со ссылками на тетрадь, письма и документы. | `—` | yes |
| `/lyudi/aleksandr-krivoshein/` | Кривошеин Александр Дмитриевич | Муж Татьяны Тимофеевны — Кривошеин Александр Дмитриевич (1926–1988), в тетради — Саша. Полное имя по схеме и страницам сайта. | Муж Татьяны Тимофеевны (Саша). 1926–1988. Ссылки на Крым, семью, свёкра. | `person/aleksandr-krivoshein` | yes |
| `/lyudi/dmitry-pisma-front/` | Дмитрий (письма 103–104) | Автор фронтовых писем 103 и 104 с подписью «Дмитрий». Фамилия и точная связь с семьёй пока не установлены. | Подпись «Дмитрий» на листах 103–104. Фамилия неизвестна; не Тимоша и не отец. | `person/dmitry-pisma-front` | yes |
| `/lyudi/eva-konstantinovna-samsonova/` | Ева Константиновна Самсонова (люди архива) | Карточка человека: Ева (Евдокия) Константиновна Самсонова (Морозова), 1900–1981 — мать Татьяны Тимофеевны; связи, письма и ссылка на страницу в «Родителях». | Указатель материалов: 1900–1981, мать Татьяны Тимофеевны; тетрадь, письма сына, портрет. | `person/eva-konstantinovna-samsonova` | yes |
| `/lyudi/gennady-vokhmintsev/` | Геннадий Вохминцев | Геннадий Вохминцев — автор писем Тане ноября 1943 г. (листы 132–133); письмо 131 («Танюша!») — вероятно тот же, но тождество не доказано. | Письма 132–133 (Вохминцев); 131 — «Геннадий», сверка тождества. | `person/gennady-vokhmintsev` | yes |
| `/lyudi/genya-samsonova/` | Самсонова Евгения (Геня) Тимофеевна | Сестра Татьяны Тимофеевны — Евгения (Геня / Женя) Тимофеевна Самсонова. По тетради: формы имени, главы 10–11, вставка-письмо 089–090. | Сестра Геня (Евгения). Формы имени и ссылки на рукопись; без домыслов о смерти. | `person/genya-samsonova` | yes |
| `/lyudi/misha-friolenko/` | Миша Фриоленко | Фриоленко Михаил Макарович (Миша) — автор письма Тане 20.04.1943 (листы 128–129). Товарищ, не брат. | Письмо 128–129. Михаил Макарович Фриоленко; товарищ военных лет. | `person/misha-friolenko` | yes |
| `/lyudi/tatyana-timofeevna-krivosheina/` | Кривошеина Татьяна Тимофеевна | Кривошеина Татьяна Тимофеевна (1926–2021) — автор тетради «Наша родословная. Самсоновы»; центр семейного архива. | 1926–2021. Автор рукописи, дочь Самсоновых; письма, фото и главы тетради. | `person/tatyana-timofeevna-krivosheina` | yes |
| `/lyudi/timofey-petrovich-samsonov/` | Самсонов Тимофей Петрович (люди архива) | Карточка человека: Самсонов Тимофей Петрович (1888–1955), отец Татьяны Тимофеевны — связи, документы и ссылка на полную биографию в «Родителях». | Указатель материалов: 1888–1955, отец Татьяны Тимофеевны; альбом, документы, главы тетради. | `person/timofey-petrovich-samsonov` | yes |
| `/lyudi/timofey-timofeevich-samsonov/` | Самсонов Тимофей Тимофеевич | Самсонов Тимофей Тимофеевич (Тёма, р. 1923) — брат Татьяны Тимофеевны; фронт, письма «Тимоша», медаль «За оборону Сталинграда». Не отец Т. П. | Брат (дядя Тёма). Сталинград, письма; не путать с отцом Тимофеем Петровичем. | `person/timofey-timofeevich-samsonov` | yes |

## RU — События (`/sobytiya/`)

| URL | title | description | summary | entity_id | indexable |
| --- | --- | --- | --- | --- | --- |
| `/sobytiya/` | События семейного архива | События семейного архива: школа, эвакуация, Сталинград, знакомство с Сашей, Крым, начало семьи. | Опорные события по тетради, письмам и документам — с кратким «зачем читать». | `—` | yes |
| `/sobytiya/evakuaciya-1941/` | Эвакуация 1941 | Эвакуация семьи из Москвы в 1941 году: паника 16 октября, Куйбышев, возвращение — по тетради Татьяны Тимофеевны. | 1941–1942 (примерно). Москва → восток (Куйбышев); возвращение — по рукописи. | `event-evacuation-1941` | yes |
| `/sobytiya/krym-poezdki/` | Поездки в Крым | Крымские поездки семьи: 1946 и следующие годы — Севастополь, Бахчисарай, Судак, Симферополь — по тетради Татьяны Тимофеевны. | С 1946. Крым с семьёй Кривошеиных; Севастополь после войны. | `event-crimea-trips` | yes |
| `/sobytiya/nachalo-semi/` | Начало семьи | Начало семейной жизни Татьяны Тимофеевны и Саши: решение о браке, регистрация, рождение Мити — по тетради. | Конец 1940-х. Брак с А. Д. Кривошеиным; рождение сына Дмитрия (Мити) в 1948. | `event-family-start` | yes |
| `/sobytiya/oborona-stalingrada/` | Оборона Сталинграда | Оборона Сталинграда в семейном архиве: медаль Самсонова Тимофея Тимофеевича и контекст писем 1943 года. | 1942–1943. Медаль «За оборону Сталинграда» — Т. Т. Самсонов, не отец Т. П. | `event-defense-of-stalingrad` | yes |
| `/sobytiya/shkola-1940-1941/` | Школа 1940–1941 | Предвоенные и военные школьные годы Татьяны Тимофеевны: класс, друзья, 22 июня 1941, учёба в эвакуации и после возвращения. | Около 1940–1943. Школа в Москве; война; Куйбышев; возвращение в класс. | `event-school-years-1940-1941` | yes |
| `/sobytiya/znakomstvo-s-sashey/` | Знакомство с Сашей | Знакомство Татьяны Тимофеевны с Александром (Сашей) Кривошеиным — школа после возвращения из эвакуации, юность. | Середина 1940-х. Одноклассник Саша Кривошеин; дружба и юность. | `event-tatyana-meets-sasha` | yes |

## RU — Хронология

| URL | title | description | summary | entity_id | indexable |
| --- | --- | --- | --- | --- | --- |
| `/hronologiya/` | Хронология семейного архива | Главные даты семейного архива по порядку: от рождения родителей к войне, Крыму и поздним годам — со ссылками на людей, места, документы и главы. | Даты архива по времени: куда кликнуть дальше. | `—` | yes |

## RU — Места (`/mesta/`)

| URL | title | description | summary | entity_id | indexable |
| --- | --- | --- | --- | --- | --- |
| `/mesta/` | Места семейного архива | Исторические места семейного архива: Москва, Крым, Сталинград/Волгоград, дома и адреса из рукописи — не туризм. | Москва, Метрополь, Серафимовича, Крым, Севастополь, Сталинград — OpenStreetMap, по рукописи. | `—` | yes |
| `/mesta/crimea-family/` | Крым семейный | Крым в семейной хронике 1946–1949: Кривошеины, поездки Татьяны Тимофеевны, Симферополь, побережье — по рукописи, не как туризм. | 1946–1949: облисполком, гости, Гурзуф, поездки; место семейных встреч Самсоновых и Кривошеиных. | `place-crimea` | yes |
| `/mesta/metropol-moscow/` | Гостиница «Метрополь» (1-й дом Советов) | Гостиница «Метрополь» как 1-й дом Советов в семейной истории: жильё Самсоновых после свадьбы, до переездов на Арбат и Воздвиженку. | Ранние 1920-е: «Метрополь» — 1-й дом Советов; место знакомства Лели с мамой, рождения детей рядом по времени. | `place-metropol` | yes |
| `/mesta/moskva-semeynaya/` | Москва семейная | Главные московские точки из дневника Татьяны Тимофеевны: дом мамы, Лубянка, Воздвиженка, сад, Новодевичье. | 2-я Брестская, Белорусский → Лубянка, Воздвиженка, Александровский сад, Новодевичье. | `place-moscow` | yes |
| `/mesta/serafimovich-street/` | Улица Серафимовича (Дом правительства) | Улица Серафимовича и Дом правительства в семейной хронике: переезд 1931 года, адрес фронтовых писем — без номеров квартир. | С 1931 — дом на ул. Серафимовича (Дом правительства). Семейный и эпистолярный адрес. | `place-serafimovich` | yes |
| `/mesta/sevastopol/` | Севастополь | Севастополь в рукописи Татьяны Тимофеевны: визит 1946 года в разрушенный город, Малахов курган, памятник затопленным кораблям. | 1946: разрушенный после войны Севастополь глазами гостьи семьи Кривошеиных. | `place-sevastopol` | yes |
| `/mesta/stalingrad-volgograd/` | Сталинград (Волгоград) | Сталинград / Волгоград в семейном архиве: оборона 1942–1943 и медаль брата Татьяны Тимофеевны — Самсонова Тимофея Тимофеевича. | Историческое имя — Сталинград; ныне Волгоград. Связь архива — оборона и медаль Т. Т. Самсонова. | `place-stalingrad-volgograd` | yes |

## RU — Принципы публикации

| URL | title | description | summary | entity_id | indexable |
| --- | --- | --- | --- | --- | --- |
| `/printsipy-publikacii/` | Принципы публикации | Как семейный архив публикует источники, помечает неуверенность и защищает приватность. | Источники, неуверенность, приватность — правила публикации на сжс.рф. | `—` | yes |

## EN — People (`/en/people/`)

| URL | title | description | summary | entity_id | indexable |
| --- | --- | --- | --- | --- | --- |
| `/en/people/` | People of the family archive | Who is who in the family archive: Tatyana Timofeevna, the Samsonov parents, brother Tyoma, Sasha, and authors of wartime letters. | People of the archive — short pages with links to the notebook, letters, and documents. | `—` | yes |
| `/en/people/aleksandr-krivoshein/` | Aleksandr Dmitrievich Krivoshein | Husband of Tatyana Timofeevna — Aleksandr Dmitrievich Krivoshein (1926–1988), Sasha in the notebook. Full name from the chart and site pages. | Tatyana Timofeevna’s husband (Sasha). 1926–1988. Links to Crimea, family, father-in-law. | `person/aleksandr-krivoshein` | yes |
| `/en/people/dmitry-front-letters/` | Dmitry (front letters) | Author signing as Dmitry on wartime letters 103 and 104. Surname and exact family link not established. | Letters 11.08.1943 and 28.07.1944. Signature Dmitry only — no invented surname. | `person/dmitry-pisma-front` | yes |
| `/en/people/eva-konstantinovna-samsonova/` | Eva Konstantinovna Samsonova (People) | Person card: Eva (Evdokia) Konstantinovna Samsonova (née Morozova), 1900–1981 — mother of Tatyana Timofeevna; links, letters, and the Parents page. | Archive index: 1900–1981, mother of Tatyana Timofeevna; notebook, son’s letters, portrait. | `person/eva-konstantinovna-samsonova` | yes |
| `/en/people/gennady-vokhmintsev/` | Gennady Vokhmintsev | Gennady (Gennady Vokhmintsev) — wartime correspondent of Tanya; letters 131–133 in the front collection. | Letters to Tanyusha / Tanya, 1943. Surname from family heading on letter 132. | `person/gennady-vokhmintsev` | yes |
| `/en/people/genya-samsonova/` | Evgenia (Genya) Timofeevna Samsonova | Sister of Tatyana Timofeevna — Evgenia (Genya / Zhenya) Timofeevna Samsonova. Name forms, diary chapters 10–11, letter insert pp. 089–090. | Sister Genya (Evgenia). Name forms and manuscript links; no invented death detail. | `person/genya-samsonova` | yes |
| `/en/people/misha-friolenko/` | Mikhail Makarovich Friolenko | Mikhail Makarovich Friolenko (Misha) — wartime comrade; author of the 20 April 1943 letter to Tanya. Not brother Tyoma. | Comrade, not brother. Letter 128–129, field post 18003. | `person/misha-friolenko` | yes |
| `/en/people/tatyana-timofeevna-krivosheina/` | Tatyana Timofeevna Krivosheina | Tatyana Timofeevna Krivosheina (1926–2021) — author of the notebook “Our genealogy: the Samsonovs,” central figure of the family archive. | 1926–2021. Notebook author; daughter of T. P. Samsonov and Eva Konstantinovna. | `person/tatyana-timofeevna-krivosheina` | yes |
| `/en/people/timofey-petrovich-samsonov/` | Timofey Petrovich Samsonov (People) | Person card: Timofey Petrovich Samsonov (1888–1955), father of Tatyana Timofeevna — links, documents, and the full Parents biography. | Archive index: 1888–1955, father of Tatyana Timofeevna. Not to be confused with son Timofey Timofeevich. | `person/timofey-petrovich-samsonov` | yes |
| `/en/people/timofey-timofeevich-samsonov/` | Timofey Timofeevich Samsonov | Timofey Timofeevich Samsonov (Tyoma; b. 1923) — brother of Tatyana Timofeevna; Stalingrad defence medal; wartime letters signed Timosha. | Brother Tyoma (b. 1923). Not father Timofey Petrovich. Stalingrad medal T. T. | `person/timofey-timofeevich-samsonov` | yes |

## EN — Events (`/en/events/`)

| URL | title | description | summary | entity_id | indexable |
| --- | --- | --- | --- | --- | --- |
| `/en/events/` | Events of the family archive | Events of the family archive: school, evacuation, Stalingrad, meeting Sasha, Crimea, beginning of the family. | Anchor events from the notebook, letters, and documents — with a short “why open this”. | `—` | yes |
| `/en/events/crimea-trips/` | Crimea trips | Family trips to Crimea: 1946 and following years — Sevastopol, Bakhchisarai, Sudak, Simferopol — from the notebook. | From 1946. Crimea with the Krivoshein family; postwar Sevastopol. | `event-crimea-trips` | yes |
| `/en/events/defense-of-stalingrad/` | Defence of Stalingrad | The Defence of Stalingrad in the family archive: medal of Timofey Timofeevich Samsonov and 1943 letter context. | 1942–1943. Medal “For the Defence of Stalingrad” — T. T. Samsonov, not father T. P. | `event-defense-of-stalingrad` | yes |
| `/en/events/evacuation-1941/` | Evacuation 1941 | Family evacuation from Moscow in 1941: 16 October panic, Kuybyshev, return — from Tatyana Timofeevna’s notebook. | 1941–1942 (approx.). Moscow → east (Kuybyshev); return per the manuscript. | `event-evacuation-1941` | yes |
| `/en/events/family-beginning/` | Beginning of the family | Beginning of Tatyana Timofeevna and Sasha’s family life: decision to marry, registration, birth of Mitya — from the notebook. | Late 1940s. Marriage to A. D. Krivoshein; son Dmitry (Mitya) born 1948. | `event-family-start` | yes |
| `/en/events/meeting-sasha/` | Meeting Sasha | How Tatyana Timofeevna met Aleksandr (Sasha) Krivoshein — school after evacuation, youth. | Mid-1940s. Classmate Sasha Krivoshein; friendship and youth. | `event-tatyana-meets-sasha` | yes |
| `/en/events/school-1940-1941/` | School 1940–1941 | Pre-war and wartime school years of Tatyana Timofeevna: class, friends, 22 June 1941, study in evacuation and after return. | About 1940–1943. School in Moscow; war; Kuybyshev; return to class. | `event-school-years-1940-1941` | yes |

## EN — Timeline

| URL | title | description | summary | entity_id | indexable |
| --- | --- | --- | --- | --- | --- |
| `/en/timeline/` | Timeline of the family archive | Main dates of the family archive in time order: from the parents’ births through the war, Crimea, and later years — with links to people, places, documents, and chapters. | Archive dates in order: where to click next. | `—` | yes |

## EN — Places (`/en/places/`)

| URL | title | description | summary | entity_id | indexable |
| --- | --- | --- | --- | --- | --- |
| `/en/places/` | Places of the family archive | Historical places in the family archive: Moscow, Crimea, Stalingrad/Volgograd, homes and addresses from the manuscript — not tourism. | Moscow, Metropol, Serafimovich, Crimea, Sevastopol, Stalingrad — OpenStreetMap | `—` | yes |
| `/en/places/crimea-family/` | Crimea (family years) | Crimea in the family chronicle 1946–1949: the Krivosheins, Tatyana Timofeevna’s visits, Simferopol and the coast — from the manuscript, not as tourism. | 1946–1949: regional executive, guests, Gurzuf, travel; meeting ground of Samsonovs and Krivosheins. | `place-crimea` | yes |
| `/en/places/family-moscow/` | Family Moscow | Main Moscow points from Tatyana Timofeevna’s diary: mother’s home, Lubyanka, Vozdvizhenka, the garden, Novodevichy. | 2nd Brestskaya, Belorussky → Lubyanka, Vozdvizhenka, Alexandrovsky Garden, Novodevichy. | `place-moscow` | yes |
| `/en/places/metropol-moscow/` | Hotel Metropol (1st House of Soviets) | Hotel Metropol as the 1st House of Soviets in family history: Samsonov lodging after marriage, before moves to the Arbat and Vozdvizhenka. | Early 1920s: Metropol as 1st House of Soviets; Lelya meets Mama; births of the children nearby in time. | `place-metropol` | yes |
| `/en/places/serafimovich-street/` | Serafimovich Street (House of Government) | Serafimovich Street and the House of Government in the family chronicle: the 1931 move, wartime letter address — without apartment numbers. | From 1931 — the house on Serafimovich Street (House of Government). Family and epistolary address. | `place-serafimovich` | yes |
| `/en/places/sevastopol/` | Sevastopol | Sevastopol in Tatyana Timofeevna’s manuscript: a 1946 visit to the ruined city, Malakhov Kurgan, the sunken ships monument. | 1946: postwar Sevastopol as seen by a guest of the Krivoshein family. | `place-sevastopol` | yes |
| `/en/places/stalingrad-volgograd/` | Stalingrad (Volgograd) | Stalingrad / Volgograd in the family archive: the 1942–1943 defence and the medal of Tatyana Timofeevna’s brother, Timofey Timofeevich Samsonov. | Historical name Stalingrad; today Volgograd. Archive link — defence and T. T. Samsonov’s medal. | `place-stalingrad-volgograd` | yes |

## EN — Publishing principles

| URL | title | description | summary | entity_id | indexable |
| --- | --- | --- | --- | --- | --- |
| `/en/publishing-principles/` | Publishing principles | How this family archive publishes sources, marks uncertainty, and protects privacy. | Sources, uncertainty, and privacy rules for publication on сжс.рф. | `—` | yes |

## Absolute URLs (canonical host)

All paths above resolve under `https://сжс.рф` (RU at site root; EN under `/en/`).

## Uniqueness checks (this scope)

- Duplicate titles: **0**
- Duplicate descriptions: **0**
- Duplicate summaries: **0**

## Parent / entity title disambiguation

Full biographies live under **Родители / Parents**. Matching person cards under **Люди / People** use distinct titles so SERP/tabs do not collide:

| Entity page title | Biography page title |
| --- | --- |
| Самсонов Тимофей Петрович (люди архива) | Самсонов Тимофей Петрович |
| Ева Константиновна Самсонова (люди архива) | Ева Константиновна Самсонова |
| Timofey Petrovich Samsonov (People) | Timofey Petrovich Samsonov |
| Eva Konstantinovna Samsonova (People) | Eva Konstantinovna Samsonova |

## Notes

- `entity_id` on people leaves uses the content form `person/…` (bridged to registry `person-…` in templates). Events and places use registry-aligned `event-…` / `place-…` ids.
- Hub pages and publishing-principles have no `entity_id` (section/policy pages, not graph entities).
- Do not add `robotsNoIndex` to entity hubs or leaves.

