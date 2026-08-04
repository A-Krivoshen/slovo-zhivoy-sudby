# Backup & speed notes

## Backup (scans / originals)

- **Do not** rely on git alone for `inbox/scans/` (thousands of images; may be gitignored or too large).
- Keep an offline copy: external drive or cloud (Yandex Disk / similar) with the same folder tree.
- After each major photo batch, note the date and batch id in `docs/` or `inbox/transcripts/`.

## Speed / LCP (live)

Suggested checks after deploy (Chrome DevTools → Lighthouse, mobile):

1. **Home** — hero image should be preloaded; fonts: only 2 critical preloads (cyrillic or latin).
2. **Diary chapter** — first image lazy; next chapter prefetched.
3. **People page** — gallery thumbs; `decoding=async` on figures.

If LCP is still high:

- Prefer `-thumb` / `-md` derivatives for in-chapter photos where available.
- Avoid loading full-resolution scans above the fold.

## Figure shortcode

`layouts/shortcodes/figure.html` auto-adds `srcset` when `static…-thumb.*` or `…-md.*` exist next to the source path.
