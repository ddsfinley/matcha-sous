# Matcha Sous MS-01 — site v2 (Direction B × C type)

Static, no framework. Ink/paper/vermilion identity (Direction B) set in
Fraunces italic + Archivo (Direction C pairing). Lives in `/site`; the legacy
storefront at the repo root is untouched.

## Pages
- `index.html` — single scrolling product page: hero → why → gallery (figures)
  → by-hand-vs-MS-01 comparison → method → **order area** → engraved spec plate → Q&A
- `faq.html` — FAQ & support (native `<details>`, zero JS) + matching FAQPage JSON-LD
- `wholesale.html` — hospitality pitch + enquiry form (composes a mailto; no backend)
- `proposals/` — Stage-1 design directions (kept for the record, noindex)

## Launch checklist
1. **Checkout**: replace `https://checkout.matchasous.com/ms-01` (marked `TODO`)
   in `index.html` with the real hosted checkout URL.
2. Deploy `/site` contents at the **domain root** of matchasous.com — canonicals,
   OG URLs, `sitemap.xml` and `robots.txt` already point there.
3. Submit `sitemap.xml` in Google Search Console.
4. Emails `care@` / `wholesale@matchasous.com` must exist (or edit them).

## Performance notes (budget: Lighthouse mobile 90+, LCP < 2.5 s)
- Self-hosted woff2 subsets (~15–29 KB each), preloaded per page, `font-display: swap`
- One small CSS file, no JS on home/FAQ (Q&A uses native `<details>`); ~10 lines of JS on wholesale only
- WebP images with explicit width/height (no CLS), `fetchpriority=high` + preload on the LCP hero,
  `loading=lazy` below the fold
- JSON-LD: Organization, WebSite, Product+Offer ($150), BreadcrumbList, FAQPage
