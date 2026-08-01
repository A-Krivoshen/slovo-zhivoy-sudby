# SEO: sitemap, image extension, robots, experimental llms.txt

**Branch:** `task/archive-seo-ai-knowledge-graph`  
**Site:** [сжс.рф](https://сжс.рф/) · Hugo extended (tested with 0.164)

## Sitemap structure

Multilingual Hugo emits:

| File | Role |
|------|------|
| `/sitemap.xml` | **Sitemap index** → language sitemaps |
| `/ru/sitemap.xml` | Russian URL set (default language; also reachable as language home sitemap) |
| `/en/sitemap.xml` | English URL set |

With `defaultContentLanguageInSubdir = false`, the RU language sitemap is under `/ru/sitemap.xml` in the index (Hugo default), while most RU pages live at the site root (`/vospominaniya/…`, not `/ru/…`).

Config (`hugo.toml`):

```toml
[sitemap]
  changefreq = 'weekly'
  priority = 0.5
  filename = 'sitemap.xml'
```

### Image sitemap (Google extension)

**Implemented** via project override:

- [`layouts/_default/sitemap.xml`](../layouts/_default/sitemap.xml)

Extends the embedded Hugo sitemap template:

- Keeps every default `<url>` entry: `loc`, `lastmod`, `changefreq`, `priority`, `xhtml:link` hreflang.
- Adds namespace `xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"`.
- For each page, nests up to the images discovered from:

  1. PaperMod front matter `cover.image` (optional `cover.alt` / `cover.caption` → `image:title` / `image:caption`)
  2. Page-bundle image resources (`.Resources.ByType "image"`)
  3. Body sources: `figure` / `img` `src="…"` and markdown `![alt](path)` for common image extensions

Images are de-duplicated per page URL. There is **no** separate `image-sitemap.xml`; Google supports image tags **inside** the regular sitemap ([Image sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps)).

**Secondary signal:** figures should keep real captions (`figure` shortcode `caption=…` or markdown). Captions in HTML help humans and parsers even when the sitemap only lists `image:loc`.

**Not included on purpose**

- Favicons, theme icons, OG default graphic unless referenced from page body/cover
- Private / draft pages (not in `.Pages` build set)
- Pages with `sitemap: disable: true` (Hugo `Sitemap.Disable`)

### Compatibility

Override must stay a strict superset of Hugo’s default URL list so existing Search Console sitemap submissions keep working. Do not remove hreflang `xhtml:link` blocks.

## robots.txt

Sources of truth (prefer layout when `enableRobotsTXT = true`):

- [`layouts/robots.txt`](../layouts/robots.txt) — generated in production builds
- [`static/robots.txt`](../static/robots.txt) — fallback / mirror of Allow rules

Rules:

- Production: **Allow: /** — site fully crawlable
- Explicit **Allow** for knowledge-graph sections so they are never blocked by accident:
  - `/lyudi/`, `/sobytiya/`, `/hronologiya/`
  - EN mirrors: `/en/people/`, `/en/events/`, `/en/timeline/`
- Non-production: `Disallow: /` (PaperMod/Hugo convention)
- `Sitemap:` points at absolute `sitemap.xml`

**Do not** add `Disallow` for those entity paths. Legacy diary hubs use `robotsNoIndex: true` (meta noindex in PaperMod head), not robots.txt blocks.

## Experimental llms.txt

PaperMod ships [`themes/PaperMod/layouts/llms.txt`](../themes/PaperMod/layouts/llms.txt): a plain-text outline of sections and page links for AI agents (similar in spirit to [llmstxt.org](https://llmstxt.org/)).

Enabled experimentally in `hugo.toml`:

```toml
[outputs]
  home = ['HTML', 'RSS', 'JSON', 'LLMs']

[outputFormats.LLMs]
  mediaType = 'text/plain'
  baseName = 'llms'
  isPlainText = true
  notAlternative = true
```

Build produces:

- `/llms.txt` (default language / RU home)
- `/en/llms.txt` (English home)

**Status:** experimental. Not a Google ranking factor. Safe to drop `LLMs` from `home` outputs if undesired. Not a substitute for crawlable HTML entity pages (`/lyudi/`, etc.) or JSON-LD.

`robots.txt` comments the llms URL; it is not a standard Sitemap directive.

## Verification

```bash
hugo --minify
# index present
test -f public/sitemap.xml
# language sitemaps include image namespace when any page has images
grep -q 'xmlns:image=' public/en/sitemap.xml
grep -q '<image:image>' public/en/sitemap.xml
# robots does not block entity sections
grep -E 'lyudi|sobytiya|hronologiya' public/robots.txt
# experimental AI map
test -f public/llms.txt || test -f public/en/llms.txt
```

After deploy: resubmit `/sitemap.xml` in Google Search Console if the index URL is already registered (image tags refresh on recrawl).

## Related

- [docs/SEO_AI_ARCHITECTURE_AUDIT.md](./SEO_AI_ARCHITECTURE_AUDIT.md) — gap list (image sitemap was open; now closed)
- [docs/ARCHIVE_RELATION_VOCABULARY.md](./ARCHIVE_RELATION_VOCABULARY.md) — relation types for entity graph
