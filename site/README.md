# Matcha Sous — site

Static, no framework. Cream / forest / champagne-gold identity set in
Cormorant Garamond (display) + Jost (utility). Lives in `/site`; the legacy
storefront at the repo root is untouched.

## Pages
- `index.html` — single scrolling product page: hero → why → gallery (figures)
  → by-hand-vs-Matcha Sous comparison → method → **order area** → engraved spec plate → Q&A
- `how-to-use.html` — the full method: weigh, sift, fill, whisk, build (ice/milk), sweeten + care (HowTo schema)
- `journal/` — SEO article hub + 4 posts (Article schema)
- `about.html` — Our story (founder narrative, values, craft — the sous chef framing)
- `faq.html` — FAQ & support (native `<details>`, zero JS) + matching FAQPage JSON-LD
- `wholesale.html` — hospitality pitch + enquiry form (composes a mailto; no backend)
- `proposals/` — Stage-1 design directions (kept for the record, noindex)

## Brand

**The mark** is an M/S monogram woven into a shield ("vessel"), drawn as a
single continuous stroke, with a matcha leaf resting in the valley of the M.
Rationale: leaf (the tea) + vessel (the craft) + M/S (the name). That is the
whole story — no puzzle-piece symbolism. The leaf carries a single midrib
vein; at very small sizes it reads as a solid leaf, by design.

**Files** (all production vector art, generated from one geometry):
- `assets/img/logo.svg` — primary mark, forest on transparent (for light
  backgrounds: header, documents)
- `assets/img/logo-cream.svg` — cream variant (for dark backgrounds: footer,
  dark packaging)
- `favicon.svg` — bare-shield submark on a forest tile, stroke weight and
  S-gaps optically boosted for 16 px
- `apple-touch-icon.png` — 180×180 flattened tile
- `assets/img/logo-512.png` — square lockup for Organization structured data

**Usage rules**
1. Leaf green `#8DB23D` is a **mark color only** — ~2.2:1 contrast on cream,
   so never use it for text or buttons. Dark forest `#24311E` does that work.
2. Below ~24 px, use the bare shield (favicon art), not the full leaf mark.
3. Palette: forest `#24311E` / `#2F3A30`, cream `#F6F2E9`, paper `#FBF9F3`,
   gold `#C2A36B` / `#A6884F`, leaf `#8DB23D` (mark only).

**Tagline hierarchy** (one voice, three jobs):
1. **"Behind every great matcha."** — the primary line. It is printed on the
   box; it leads the hero eyebrow, the footer, the OG card and the
   Organization `slogan`.
2. **"The sous chef for matcha"** — the descriptor, used inside sentences
   ("Meet the sous chef for matcha").
3. **"Crafted in ceremony"** — reserved for the stamp/badge lockup on
   packaging and print; not used as a headline on the site.

## Launch checklist
1. **Checkout**: replace `https://checkout.matchasous.com/matcha-sous` (marked `TODO`)
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
