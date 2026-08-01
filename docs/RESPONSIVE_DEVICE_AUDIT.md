# Responsive / multi-device audit — сжс.рф

**Date:** 2026-08-01  
**Method:** local Hugo + Chrome headless (puppeteer-core), CSS-pixel viewports  
**Result:** **276 / 276 checks OK** — horizontal overflow = 0 on all combinations  
**Machine report:** `work/responsive_audit/report.json`, screenshots in `work/responsive_audit/shots/`

---

## Goal

Verify the public site is usable on **all common form factors and manufacturer viewport classes**, without device-specific UA hacks: phones, foldables, tablets, laptops, desktops; Apple / Samsung / Google / Xiaomi / Huawei / OPPO / vivo / OnePlus / Motorola and generic Android.

---

## Engines covered (behavior via progressive CSS)

| Engine | Products |
|--------|----------|
| **Blink** | Chrome, Edge, Samsung Internet, Opera, Android WebView, Chromium |
| **WebKit** | Safari iOS / iPadOS / macOS (safe-area, text-size-adjust, 16px inputs) |
| **Gecko** | Firefox desktop / Android (same CSS layout) |

No vendor sniffing. Layout depends on viewport width, orientation, `env(safe-area-inset-*)`, and media features (`prefers-reduced-motion`, `forced-colors`, `print`).

---

## Device matrix tested (34 profiles)

### Phones — portrait

| ID | Maker | Class | Size (CSS px) |
|----|-------|-------|---------------|
| `iphone-se-1` | Apple | iPhone SE (1st) / very small | 320×568 |
| `galaxy-a-small` | Samsung | Galaxy A small | 360×640 |
| `galaxy-s-base` | Samsung | Galaxy S base | 360×800 |
| `xiaomi-redmi` | Xiaomi | Redmi / POCO | 360×800 |
| `huawei-p` | Huawei | P-series | 360×780 |
| `oppo-a` | OPPO/Realme | A-series | 360×800 |
| `vivo-y` | vivo | Y-series | 360×800 |
| `galaxy-s23-ultra` | Samsung | S23/S24 Ultra class | 384×824 |
| `iphone-12-13-14` | Apple | iPhone 12/13/14 | 390×844 |
| `iphone-14-pro` | Apple | iPhone 14/15 Pro | 393×852 |
| `pixel-7` | Google | Pixel 7/8 | 412×915 |
| `oneplus-nord` | OnePlus | Nord / 11 | 412×915 |
| `motorola-edge` | Motorola | Edge class | 412×915 |
| `iphone-plus` | Apple | Plus / Max class | 428×926 |
| `iphone-pro-max` | Apple | Pro Max | 430×932 |

### Foldables

| ID | Maker | Class | Size |
|----|-------|-------|------|
| `galaxy-fold-cover` | Samsung | Z Fold cover screen | 280×653 |
| `galaxy-z-fold-inner` | Samsung | Z Fold inner | 768×882 |
| `pixel-fold-inner` | Google | Pixel Fold inner | 673×841 |

### Phones — landscape

| ID | Maker | Size |
|----|-------|------|
| `iphone-landscape` | Apple | 844×390 |
| `android-landscape` | Android | 800×360 |

### Tablets

| ID | Maker | Class | Size |
|----|-------|-------|------|
| `ipad-mini` | Apple | iPad mini | 744×1133 |
| `ipad-10` | Apple | iPad 10.9 | 820×1180 |
| `ipad-pro-11` | Apple | iPad Pro 11 | 834×1194 |
| `ipad-pro-12` | Apple | iPad Pro 12.9 | 1024×1366 |
| `ipad-landscape` | Apple | iPad landscape | 1180×820 |
| `galaxy-tab-s` | Samsung | Galaxy Tab S | 800×1280 |
| `galaxy-tab-land` | Samsung | Tab landscape | 1280×800 |
| `android-tablet` | Generic Android | 10″ tablet | 800×1280 |

### Laptop / desktop

| ID | Class | Size |
|----|-------|------|
| `netbook` | Small laptop | 1024×600 |
| `macbook-13` | MacBook 13″ | 1280×800 |
| `laptop-hd` | Common laptop | 1366×768 |
| `desktop-fhd` | FHD | 1920×1080 |
| `desktop-qhd` | QHD | 2560×1440 |
| `ultrawide` | 21:9 | 2560×1080 |

---

## Pages exercised

| Page | Path |
|------|------|
| Home RU | `/` |
| Home EN | `/en/` |
| Person entity | `/lyudi/timofey-timofeevich-samsonov/` |
| Photo album | `/foto/tetrad-semya-prodolzhenie/` |
| Photo index | `/foto/` |
| Diary chapter | `/vospominaniya/dnevnik/13-shkola-druzya-109-119/` |
| Letter | `/dokumenty/pisma-s-fronta/pismo-103-1943/` |
| Letters index | `/dokumenty/pisma-s-fronta/` |
| Events | `/sobytiya/` |
| Timeline | `/hronologiya/` |

Phones: core set (home, person, album, photo index, diary, letter, letters).  
Tablets / desktop: + events, timeline, EN home.

**Pass criterion:** `document.scrollWidth - clientWidth < 3` and no content images past the right edge.

---

## Result summary

| Metric | Value |
|--------|-------|
| Checks | **276** |
| HTTP / layout failures | **0** |
| Max horizontal overflow | **0 px** |
| Images past viewport | **0** |
| Screenshots archived | 56 (representative devices × key pages) |

### Menu height on home (expected chip wrap)

| Width | Example | menuH ≈ |
|-------|---------|---------|
| 280 | Fold cover | 331 px |
| 320 | iPhone SE | 290 px |
| 360 | Galaxy / Xiaomi / Huawei | 248 px |
| 390–412 | iPhone 14 / Pixel | 206 px |
| 428–430 | Pro Max | 165 px |

Tall multi-row menu on small phones is **by design** (full archive nav, ≥44 px chips). Content is not clipped horizontally.

---

## CSS / meta shipped

| Item | File |
|------|------|
| Multi-breakpoint layer (≤320 / ≤480 / 481–719 / 720–1023 / ≥1024 / ≥1400) | `assets/css/extended/responsive.css` |
| Chip mobile menu, touch targets, safe-area, tables/pre scroll | same |
| Landscape phone lightbox, reduced-motion, forced-colors, print | same |
| Lightbox safe-area + touch-action | `assets/css/extended/lightbox.css` |
| `viewport-fit=cover`, theme-color, format-detection | `layouts/_partials/extend_head.html` |

### Breakpoints (mobile-first logic)

1. **≤320** — ultra-narrow fold cover / SE: denser chips, smaller logo  
2. **≤480** — phones: column header, chip menu, single-column home  
3. **481–719** — large phones / phablets: 2-col home cards  
4. **720–1023** — tablets  
5. **≥1024** — desktop nav density  
6. **≥1400** — wider main column  

---

## Manufacturers → what is covered

| Firm | Coverage approach |
|------|-------------------|
| **Apple** | SE → Pro Max + landscape + iPad mini/10/Pro + MacBook; WebKit-safe (`viewport-fit`, 16px inputs, `-webkit-text-size-adjust`) |
| **Samsung** | A / S / Ultra + Z Fold cover/inner + Tab S |
| **Google** | Pixel + Pixel Fold inner |
| **Xiaomi / Huawei / OPPO / Realme / vivo / OnePlus / Motorola** | Shared Android widths 360 / 412 (dominant market CSS widths) |
| **Generic Android tablets** | 800×1280 |
| **Windows / Linux desktops** | 1024–2560 + forced-colors |

Individual model names differ; layout is driven by **viewport width/height**, which is what CSS can observe. Brand-specific browsers (Samsung Internet, Yandex Browser, etc.) use Blink and inherit the same rules.

---

## Residual risks (not blockers)

1. **EN menu labels** longer than RU — still wraps, may use one extra row.  
2. **Yandex floor ads** (production only) can cover the bottom; `top-link` offset includes safe-area.  
3. **Real Safari iOS** not run in this headless matrix — same CSS; recheck on a physical iPhone after Pages deploy.  
4. **Very long unbreakable strings** in future content — mitigated with `overflow-wrap` on breadcrumbs / related / captions; tables already scroll horizontally.

---

## How to re-run

```bash
hugo server -D --bind 127.0.0.1 --port 1313
# other terminal:
node work/responsive_audit/audit.mjs
# report → work/responsive_audit/report.md
```

---

## Verdict

**PASS** for multi-device adaptive layout across phones, foldables, tablets, laptops, and desktops, covering major manufacturers via representative viewports. Ship `responsive.css` + viewport meta to production with this audit.
