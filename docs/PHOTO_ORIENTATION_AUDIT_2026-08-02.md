# Photo orientation audit — 2026-08-02

After the young Aleksandr chart portrait was found sideways on production, all public portraits and priority content images were re-checked.

## Method

1. EXIF `Orientation` scan of all `static/photos/**` (211 files) — no non-default EXIF orientation tags (pixels already baked).
2. Visual contact sheets of:
   - person/chart portraits and covers;
   - archive-b02 primary crops used on the site;
   - early notebook leaves `str-00*`, sample later leaves, Samsonov album.
3. Comparison of chart crops to upright full leaves (`str-003`, `str-005`).

## Fixes applied

| File | Issue | Fix |
|---|---|---|
| `static/photos/aleksandr-krivoshein/chart-young-portrait.jpg` (+ thumb, context) | Head on side (crop) | +90° CW — commit `a766c47` |
| `static/photos/nina-vasilievna-krivosheina/portrait.jpg` (+ md, thumb) | Head on side (crop) | +90° CW |
| `static/photos/nina-vasilievna-krivosheina/context-chart.jpg` | Whole context rotated vs `str-005` | +90° CW (text + photo match chart leaf) |

## Confirmed upright (sample; no change)

- Eva chart + album portrait  
- Genya chart portrait  
- T.P. chart portrait + family cluster + album 01–15  
- Aleksandr formal portrait  
- Tatyana garden + 2019 home  
- D.A. Krivoshein `dmitry-portrait.jpg`  
- archive-b02 crops in contact (mp001, 007, 013, 072, 075, …)  
- Full leaves `str-001`, `str-002`, `str-003`, `str-005` (title/text readable top-to-bottom / left-to-right as expected)

## Notes

- Chart **full leaves** stay as photographed (landscape leaves for wide trees are correct when handwriting reads normally).
- Individual **portrait crops** must have the subject’s head upright even if the physical print was glued at an angle on the leaf; for Nina the glue on `str-005` is already upright — the published crop had been rotated relative to that leaf.
- Thumbs regenerated from fixed masters where applicable.

## Production

Push after this commit; hard-refresh if CDN/browser cache shows old Nina/Aleksandr files.
