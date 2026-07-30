# Matcha Sous — site

Static, no framework. Ink & bone identity drawn from the wordmark: deep
aubergine-ink ground, warm bone type, linen accents. Cormorant Garamond
(display) + Jost (utility). Lives in `/site`; the legacy storefront at the
repo root is untouched.

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

**The mark** is the stacked wordmark — MATCHA in tracked caps over SOUS in a
custom display face whose letterforms carry vortex slashes (the whisk's
motion, cut into the type). The slashed **O** doubles as the standalone
glyph: favicon, touch icon, stamps. A soft circle-glow arc is the secondary
motif (CTA band, OG card).

**Files**:
- `assets/img/wordmark.png` — keyed transparent bone lockup (266×94, ~2×
  header display size). Cut from the supplied art; **raster** — request the
  master vector file from the logo's designer before any print use.
- `favicon.svg` — slashed-O glyph on an ink tile
- `apple-touch-icon.png` — 180×180 ink tile + O
- `assets/img/logo-512.png` — square lockup for Organization structured data
- `assets/img/og.jpg` — 1200×630 social card (wordmark + glow arc + tagline)

**Palette** (sampled from the wordmark art):
ink `#1A1322` (page) / `#140E1B` (deep) / panel `#221A2E` / `#2A2138`,
bone `#EDE4D8` (type, primary CTAs), bright `#F6F0E5`,
linen `#D9CAB0` / `#C4B493` (accents: eyebrows, numerals, rules),
muted `#A79D98` (secondary text), mat `#E7DDCC` (photo frames).

**Usage rules**
1. Bone on ink is the identity: type and primary buttons are bone; the
   comparison table's "Matcha Sous" column inverts to a bone panel.
2. Linen is the only accent family — no greens, no golds brighter than
   `#E6DCC8`.
3. Photography mounts in bone mats (`--mat`) so warm product photos sit like
   prints on a dark wall; never place photos borderless on raw ink.

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
