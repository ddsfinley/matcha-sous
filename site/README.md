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

**Hero**: full bleed and **moving** — `assets/vid/hero-vortex.webm` (4.1 MB)
+ `hero-vortex.mp4` (7.1 MB), **1080x1360**, 12.5 s, cut straight from the
founder's original `IMG_2071_3.MOV` (HEVC Main 10, HLG/bt2020, 1080x1920
with a -90 rotation flag). Pipeline: tone-map HLG->bt709
(`zscale=t=linear:npl=100,tonemap=hable,zscale=p=bt709:t=bt709:m=bt709:r=tv`),
`crop=1080:1360:0:140` — cup only, base off the bottom and busy counter off
the top — then 1.25x, a restrained warm/saturation lift (tone-mapping
flattens), mild unsharp, audio stripped.

**Always cut from the originals in `~/.claude/uploads`, never from the
760x1226 `p1.mp4`/`p2.mp4` intermediates.** Those were downscaled early on,
and building the hero from them threw away a third of the resolution for
nothing: the rebuild took the retina-desktop stretch from 3.8x to 2.67x and
the phone from 1.78x to 1.60x *while* zooming in further.

`hero-bleed.webp` is the poster, cut from the same frame so there is no jump
when the video takes over.

The reading field is carved out with CSS scrims in the *same* aubergine the
footage is graded toward, which is why there is no seam between media and
page. Rebuild the still with `tools/hero_bleed.py`.

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

`assets/vid/cycle-1080.webm` (2.7 MB, VP9) + `cycle-1080.mp4` (4.8 MB, H.264
Main) — **1080x1440, 30 fps, 11.9 s**, from the founder's 1080x1920 upload.
3:4 crop at y=380 keeps the cup and the lit countdown on the base; mild warm
lift so the grey counter sits with the bone page; audio stripped; natural
speed (the countdown reads in real seconds, so do not speed it up).

**Two sources, WebM first.** Chromium builds without proprietary codecs
cannot decode H.264 at all — `canPlayType('video/mp4; codecs="avc1..."')`
returns empty — which is why local playback checks silently "failed" for
months while the file was fine. The WebM makes playback verifiable here and
adds a smaller, faster source for Chrome/Firefox; the MP4 covers Safari/iOS.
**Verify with `readyState === 4` and a advancing `currentTime`, not a
screenshot** — a screenshot only proves the poster rendered.

**Do not enlarge the video tile** — a standing decision from the founder,
independent of resolution. Small and sharp beats big and soft. Under 860px
the tile is capped at **270 CSS px and centred**, which is 810 real pixels on
a 3x iPhone against a 760 px master — near enough to native. On a 2x desktop
the 568 px tile still upscales ~1.49x; fixing that needs either a
higher-resolution master or a smaller desktop tile, and is not to be
"fixed" by growing anything.

**Wanted: a 1080p master.** The founder's 4K originals live in Drive but
cannot be retrieved — the Drive connector caps downloads at 10 MB, the Drive
API needs an OAuth token, and every Google file-serving host is blocked by
the proxy. A 1080x1920 export uploaded through chat (under 30 MB) would allow
~1100-1200 px wide output, which would finally cover the 2x tile without
upscaling. That is the only remaining gain — the tile size is settled.

**Cache-busting**: stylesheet links carry `?v=N` (currently **v=30**).
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
