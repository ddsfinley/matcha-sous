# Matcha Sous — site

Static, no framework. Bone & aubergine identity: bright warm ground, the
wordmark's deep aubergine carrying type, buttons and feature bands, copper
only at small scale. Cormorant Garamond (display) + Jost (utility). Lives in
`/site`; the legacy storefront at the repo root is untouched.

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

**Palette** (bright ground, aubergine anchor, copper hints):
page `#F7F4EE` / paper `#FDFBF7` / warm alt `#F0EBE2` / lilac tint `#EFE9F0`,
aubergine `#2B1F38` / deep `#221933` (buttons, footer, announce, CTA band,
compare column, `.bg-deep`), body text `#2A2135`,
plum `#6D5987` (numerals, icons, heading italics),
bone `#EDE4D8` (type on aubergine surfaces),
copper `#B0714F` / deep `#96593A` / soft `#D9B49E` — **small scale only**,
stone `#6F6579` (secondary text), mat `#EFE9DF` (photo frames).

**Usage rules**
1. The ground stays bright; aubergine appears as confident anchors — the
   announce bar, buttons, the "Matcha Sous" compare column, the founder band
   (`.bg-deep`), the CTA band and the footer — plus a lilac whisper in
   gradients. Body text itself is aubergine-tinted, never plain black.
2. Copper is a seasoning, not a color field: eyebrows, text links, the Q&A
   "+", thin rules, the live dot, focus rings, the compare ribbon. Never
   fill a large surface or a primary button with copper.
3. The header uses `wordmark-ink.png` on light ground; the footer keeps the
   bone `wordmark.png` on aubergine. Favicon/touch icon stay ink-tiled (the
   logo's native staging).
4. Photography mounts in warm mats (`--mat`); never borderless on lilac.

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
