# B02 URL migration map

**Branch:** `task/b02-editorial-coverage-fix`  
**Purpose:** old production diary URLs must not 404 after merge.

## Unambiguous renames → Hugo `aliases`

| Old public URL | New canonical URL | Mechanism |
|----------------|-------------------|-----------|
| `/vospominaniya/dnevnik/14-voyna-evakuaciya-120-127/` | `/vospominaniya/dnevnik/14-shkola-i-voyna/` | `aliases` on new page |
| `/vospominaniya/dnevnik/16-druzya-pobeda-134-139/` | `/vospominaniya/dnevnik/16-yunost-i-sasha/` | `aliases` |
| `/vospominaniya/dnevnik/18-synovya-150-161/` | `/vospominaniya/dnevnik/19-semya-i-deti/` | `aliases` |

Hugo aliases emit pages at the old path that redirect/serve the new content (PaperMod/Hugo standard).

## Split chapters → short hub pages (`robotsNoIndex: true`)

| Old public URL | Hub content |
|----------------|-------------|
| `/vospominaniya/dnevnik/13-shkola-druzya-109-119/` | Links to childhood school + school/war |
| `/vospominaniya/dnevnik/17-krym-semya-140-149/` | Links to Crimea family + study/work |

Hubs do **not** duplicate full text. `robotsNoIndex: true` → PaperMod `noindex, nofollow` when supported.

## New canonical chapters (no old slug)

| New URL | source_pages (FM) |
|---------|-------------------|
| `/vospominaniya/dnevnik/13-tanya-detstvo-i-shkola/` | 109–117 |
| `/vospominaniya/dnevnik/14-shkola-i-voyna/` | 118–127 |
| `/vospominaniya/dnevnik/16-yunost-i-sasha/` | 134–139 |
| `/vospominaniya/dnevnik/17-krym-sevastopol-semya/` | 140–144 |
| `/vospominaniya/dnevnik/18-ucheba-rabota-vypuskniki/` | 145–148 |
| `/vospominaniya/dnevnik/19-semya-i-deti/` | 149–161 |

## Unchanged B02 diary URLs

| URL | Notes |
|-----|-------|
| `/vospominaniya/dnevnik/10-prodolzhenie-080-089/` | kept |
| `/vospominaniya/dnevnik/11-prodolzhenie-090-099/` | kept |
| `/vospominaniya/dnevnik/12-brat-front-103-108/` | kept (title humanized) |
| `/vospominaniya/dnevnik/15-pisma-voennye-128-133/` | kept |

## Document collection (new; no production collision)

| URL |
|-----|
| `/dokumenty/pisma-s-fronta/` and letter pages |
| `/dokumenty/udostoverenie-oborona-stalingrada-samsonov-tt/` |

## Verification

After `hugo --minify`, check that each **Old public URL** path exists under `public/vospominaniya/dnevnik/…/index.html`.
