# Matcha Sous — site

Static, no framework. Bone & aubergine identity: bright warm ground, the
wordmark's deep aubergine carrying type, buttons and feature bands, copper
only at small scale. Poiret One (display) + Jost (utility). Lives in
`/site`; the legacy storefront at the repo root is untouched.

## Pages
- `index.html` — journey-ordered single page (desire → understanding →
  demonstration → differentiation → credibility → purchase): full-bleed
  hero → Fill·Press·Pour → product showcase → how it works → presets →
  origin → ceremony band + use cases → **purchase** → spec plate → FAQ →
  Journal → final CTA → letter.
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
page `#F7F4EE` / paper `#FDFBF7` / warm alt `#F0EBE2`,
aubergine `#1A1322` — the logo background, **exact** — / deep `#140E1B`
(buttons, footer, announce, CTA band, compare column, `.bg-deep`, numerals,
feature icons), body text `#251D30`,
bone `#EDE4D8` (type on aubergine surfaces),
copper `#B0714F` / deep `#96593A` / soft `#D9B49E` / bright `#E2914F`
(the hero's "Sous." only) — **small scale only**
(eyebrows, links, heading italics, plate numbers, rules, markers),
stone `#6F6862` (warm-grey secondary text — deliberately no violet cast),
mat `#EFE9DF` (photo frames). No pastel purples anywhere: purple exists
only as the deep aubergine.

**Usage rules**
1. The ground stays bright; aubergine appears as confident anchors — the
   cinematic hero, the mood band, the announce bar, buttons, the "Matcha Sous" compare column, the founder band
   (`.bg-deep`), the CTA band and the footer. Body text itself is
   aubergine-tinted, never plain black — that is the only purple on light
   ground; never tint surfaces lavender or lilac.
2. Copper is a seasoning, not a color field: eyebrows, text links, the Q&A
   "+", thin rules, the live dot, focus rings, the compare ribbon. Never
   fill a large surface or a primary button with copper.
3. The header uses `wordmark-ink.png` on light ground; the footer keeps the
   bone `wordmark.png` on aubergine. Favicon/touch icon stay ink-tiled (the
   logo's native staging).
4. Photography mounts in warm mats (`--mat`); never borderless on lilac.

**Voice** (per the packaging design brief): the story is **quiet expertise
and consistency, never time-saving**. The product is a sous — it handles the
technical work so the bowl, the pour and the moment stay the user's. Category
line: **"The Hands-Free Matcha Mixer"** (product title, page titles,
Product schema). Working copy: "Controlled vortex motion mixes matcha and
water with consistent, hands-free precision. Start the cycle and let your
sous handle the rest." Never frame the chasen as the slow alternative — the
sous works beside the tradition. Positioning vs hand whisking: **we respect
it and do not compete with it** — the Sous is an alternative for volume.
The side-by-side comparison was removed from the homepage; if one returns,
it reads as two tools/one craft — same marker in both columns, no scoring
visuals, no "easier" badges. Avoid: matcha-leaf/bamboo/whisk/bowl
graphics, vortex symbols, MS monograms, badges, promo language, spec-heavy
front sections. Speed figures (~30 s) are facts for spec contexts only. **Wording rule:
whisking is ceremony — zen and calm for the matcha community — never
"labor," "effort," "chore," "guesswork," "wrist work," or anything that
frames the practice as a burden. The Sous is framed around convenience and
on-the-go moments ("for mornings that move quickly"), never as rescue from
the whisk.** House line for the dark mood band: **"The ceremony,
preserved. The Sous, in service of it."** — ceremony first, the Sous
second and subordinate; also a candidate for the box interior.

**Hero**: full bleed — the type lives *inside* the photograph, no card and no
frame. `assets/img/hero-bleed.webp` (2400×1200, landscape) and
`hero-bleed-sm.webp` (1000×1300, portrait, art-directed via `<picture>` under
760px) are graded from `action-01-vortex.jpg` and blended 14% toward the
brand aubergine, so the stainless and the counter read as page ground. The
reading field is then carved out with CSS scrims in that *same* aubergine —
which is why there is no seam between image and page. Rebuild with
`tools/hero_bleed.py` (point `UP` at the founder’s original uploads). Keep the photo bright: the scrims do the
darkening, not the file. Both variants are preloaded behind matching `media`
queries — the hero is the LCP element.

**Type** maps onto the two halves of the wordmark. **Poiret One** is the
display face (`--disp`) — the closest free match to the mark's SOUS: a
high-contrast geometric sans with circular bowls and thin joins. It carries
every statement, heading and numeral. **Jost** is the utility face
(`--util`) — geometric monoline, the same voice as the mark's tracked
MATCHA — and carries body, nav, labels and eyebrows.

Three rules follow from Poiret being a light display cut:
1. **No negative tracking.** Its `@font-face` declares `font-weight:400 700`
   against one file so a `font-weight:600` rule matches it rather than
   synthesising a faux bold, and `.display` zeroes the base −.01em.
2. **No italic** — the family has none, so `h1 em`/`h2 em` are upright
   copper, which is also how the wordmark sets SOUS. Italic pull quotes
   (`.founder blockquote`, `.story .pull`, `.buybox .no`, `.plate .no`) use
   `--quote`, the one Cormorant Garamond italic file kept for the purpose.
3. **Hairline stroke on the display face.** Poiret is a light cut, so every
   `--disp` selector carries `-webkit-text-stroke-width:.013em`, and the
   light-on-dark surfaces that thin optically over photography — the hero
   statement, `.mood-line`, `.cta-band h2` — carry `.016em`. **Ceiling is
   ~.017em**: past that the thick/thin contrast flattens and it stops
   reading as the mark's face. Ladder the values in a browser before
   changing them.

**Layout signature**: homepage section heads sit left under a hairline rule
(`.head--idx`) — no numerals. The "how it works" section uses `.split`
(heading left, numbered items right).
The hero and the two full-bleed bands break that rhythm, so the
page reads as an editorial index rather than a stack of identical blocks.

**Tagline hierarchy** (one voice, three jobs):
1. **"Behind every great matcha is a Sous."** — the primary line (the hero
   headline itself, footer, OG card, Organization `slogan`). Capital S: *a Sous* is
   the product as a noun, echoing "behind every great chef is a sous." The
   full sentence should sit near the wordmark, which closes the analogy.
2. **"Behind every great matcha."** — the short/stamp form, as printed on
   the box; use standalone where space is tight.
3. **"The sous chef for matcha"** — the descriptor, used inside sentences
   ("Meet the sous chef for matcha"). "Crafted in ceremony" stays reserved
   for packaging stamps only.

## Launch checklist
0. **Shopify**: `shopify-theme/` is now an Online Store 2.0 theme carrying
   this design (see `shopify-theme/SHOPIFY-SETUP.md`), packaged as
   `matcha-sous-shopify-theme.zip`. Upload, then create the product and
   select it in the Hero and Buy box sections to switch on real checkout.
1. **Checkout**: replace `https://checkout.matchasous.com/matcha-sous` (marked `TODO`)
   in `index.html` with the real hosted checkout URL.
1b. **Price**: the site sells at $150; the packaging brief anticipates
   $179–199 retail. Reconcile before launch (price appears in buy box, nav,
   CTAs, Product schema and meta description).
1c. **Lifestyle photography**: `assets/img/mood-counter.webp` (the light mood
   band, "The counter is the new café.") is a placeholder — a regraded product
   shot. Replace with a real home-counter scene at 1400×786 WebP and revisit the
   line at the same time. The dark band's `mood-ritual.webp` is also a regrade.
1d. **Claim verification**: contactless magnetic drive and backlit touch
   controls — both **confirmed by the founder**. Box-verified facts: 18 speed
   levels, 3 preset programs, 40–120 ml capacity, hands-free preparation,
   easy-clean design, 6 W low power; included: mixer base, matcha cup,
   power adapter, USB-C cable, user manual; marks FCC, CE, RoHS.
2. Deploy `/site` contents at the **domain root** of matchasous.com — canonicals,
   OG URLs, `sitemap.xml` and `robots.txt` already point there.
3. Submit `sitemap.xml` in Google Search Console.
4. Emails `care@` / `wholesale@matchasous.com` must exist (or edit them).

## Video

`assets/vid/matcha-sous-loop-hq.mp4` (8.0 MB), 25.8 s at **760x1226, 30 fps,
2.5 Mb/s** — the full mixing cycle, built from the founder's two split clips
(`p1.mp4`/`p2.mp4`, 12 Mb/s masters): joined with the concat filter at CFR 30
(the demuxer mis-times these variable-frame-rate phone files), sped 1.25x,
mild unsharp, audio stripped. Autoplays muted, inline and looping as the lead
tile in the gallery.

**Encode at the masters' native size.** The previous build downscaled to
640x1032 at 795 kb/s and was the main cause of the softness the founder
flagged — the gallery tile renders 568x757 CSS, which is **1136x1514 real
pixels on a 2x display**, so 640 px was being upscaled 1.8x on top of a
starved bitrate. 760 px still under-covers that tile, which is why the tile
must not be enlarged until a higher-resolution master arrives.

**Do not enlarge the video tile** — a standing decision from the founder,
independent of resolution. It stays at 568 CSS px in the gallery.

**Wanted: a 1080p master.** The founder's 4K originals live in Drive but
cannot be retrieved — the Drive connector caps downloads at 10 MB, the Drive
API needs an OAuth token, and every Google file-serving host is blocked by
the proxy. A 1080x1920 export uploaded through chat (under 30 MB) would allow
~1100-1200 px wide output, which would finally cover the 2x tile without
upscaling. That is the only remaining gain — the tile size is settled.

**Cache-busting**: stylesheet links carry `?v=N` (currently **v=26**).
GitHub Pages caches CSS aggressively — **bump N on every `site.css`
change**, or edits will not reach returning visitors.

## Checking layout locally

Chromium is available here, so layout can be verified rather than guessed:

```python
from playwright.sync_api import sync_playwright
EXE = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=EXE, args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.goto("file:///home/user/bristol-dental-automation/site/index.html")
    pg.screenshot(path="out.png")
```

Worth measuring on every hero change: horizontal overflow
(`scrollWidth - clientWidth` should be 0) and whether the CTA is above the
fold at 390×844.

## Performance notes (budget: Lighthouse mobile 90+, LCP < 2.5 s)
- Self-hosted woff2 subsets (~15–29 KB each), preloaded per page, `font-display: swap`
- One small CSS file, no JS on home/FAQ (Q&A uses native `<details>`); ~10 lines of JS on wholesale only
- WebP images with explicit width/height (no CLS), `fetchpriority=high` + preload on the LCP hero,
  `loading=lazy` below the fold
- JSON-LD: Organization, WebSite, Product+Offer ($150), BreadcrumbList, FAQPage
