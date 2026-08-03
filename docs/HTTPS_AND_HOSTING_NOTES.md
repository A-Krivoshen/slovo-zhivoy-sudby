# HTTPS and hosting notes (сжс.рф)

**Checked:** 2026-08-03

## Status

- Host: **GitHub Pages** (`a-krivoshein.github.io` → custom domain).
- Certificate: **Let's Encrypt**, CN/SAN = `xn--f1avb.xn--p1ai`, `www.xn--f1avb.xn--p1ai` (Unicode **сжс.рф**).
- Validity (sample): Aug 2026 – Oct 2026 (auto-renewed by GitHub).
- `http://` → **301** to `https://`.
- OpenSSL verify: **0 (ok)** when SNI = punycode.

## “Not secure” on some devices

Usually **not** a broken site cert. Common causes:

1. Old Android / browser missing trust for current LE intermediates (YR2).
2. Wrong device clock/date.
3. Antivirus HTTPS inspection.
4. Captive Wi‑Fi / operator proxy.

Workarounds for visitors: open `https://сжс.рф/` or `https://xn--f1avb.xn--p1ai/`; try mobile data; update browser.

## HSTS

GitHub Pages **does not** support arbitrary `_headers` / custom HSTS for project sites the way Cloudflare Pages does. HTTPS is enforced at the edge for custom domains when “Enforce HTTPS” is on in the repo **Settings → Pages**.

Recommended (repo owner in GitHub UI):

1. Settings → Pages → **Custom domain** = `сжс.рф` (and optional `www`).
2. Enable **Enforce HTTPS**.
3. DNS: `CNAME` / apex records as GitHub documents (already pointed at Pages).

## Latin alias (optional)

A second hostname (e.g. `szhs…`) needs:

- DNS A/CNAME to GitHub Pages;
- domain added in Pages settings;
- cert re-issue for the new name.

Do **not** invent a domain; only add when the family chooses and DNS is ready.

## Mixed content

Homepage and audited content pages should use relative or `https://` assets only. Re-check after adding third-party widgets.
