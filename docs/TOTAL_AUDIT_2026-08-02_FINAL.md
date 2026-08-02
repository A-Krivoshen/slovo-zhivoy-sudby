# Total audit — 2026-08-02 (final re-pass)

**HEAD at audit start:** `4afd028`  
**Branch:** `main` (clean)

## Automated checks

| Check | Result |
|---|---|
| Visible `[фото]` / `[photo]` placeholders | **0** (fence-only manuscript labels remain) |
| `figure src` → missing static file | **0** |
| RU/EN people figure parity (10 pairs) | **OK** |
| Foto albums RU/EN figure parity | **OK** (35+15) |
| Cover images for people | **OK** |
| Private str-099/100/155/157 static files | **absent** |
| Content figure refs to private str | **0** |
| YAML people/photos/events/relations | **load OK** |
| `hugo --minify` | **PASS** (RU 286 / EN 270) |
| Sample public broken hrefs (key pages) | **0** |
| Draft content | templates only (`_shablon`, `_template`) |

## Finding fixed this pass

| Issue | Fix |
|---|---|
| EN `18-sons-150-161` missing 4 figures present on RU `19-semya-i-deti` (`b02-mp080`, `b02-mp082`×3) | Added public crops + EN captions; fixed duplicate footer link |

## Known acceptable residual

| Item | Notes |
|---|---|
| RU hub pages `diary-13-hub-legacy` / `diary-17-hub-legacy` without EN twin | `robotsNoIndex` + sitemap disable; point to split chapters |
| EN letter pages with Cyrillic body | Diplomatic manuscript text (intentional) |
| EN ch. 18-sons shorter prose than RU ch. 19 | Reader EN may omit later travel narrative; **figures** now matched; full RU linked |

## People / biography layer

| Status | Count / notes |
|---|---|
| full_biography_published (A) | Tatyana, Aleksandr, T.P., Eva, Tyoma, Genya, D.A., Nina |
| evidence_limited (C) | Dmitry letters, Misha, Gennady |
| living private (E) | sons/grandchildren — year only |

Coverage: `docs/PEOPLE_BIOGRAPHY_COVERAGE.csv`

## Production smoke (after push)

See commit message / CI run.
