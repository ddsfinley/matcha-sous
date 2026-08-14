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
- `stockists.html` — **Where to buy**. Direct-purchase box + a stockist list
  that is currently empty. `noindex` while empty (thin pages drag the whole
  site); the file's own comment says exactly what to switch on when the first
  stockist lands — add an `<li>`, delete the `.empty` paragraph, flip robots
  to `index, follow`, add it to the primary `<nav>` and to `sitemap.xml`.
  It is in every footer already.
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

**Microfoam is the elevation claim.** The `#how` section is framed upward
("A good matcha, *at its best.*"), not as loss. What separates a great bowl
from a merely good one is **texture**: a fine microfoam gives the tea body
and softens astringency. Two things must stay accurate here —
1. **Foam does not change the tea's chemistry.** It changes mouthfeel and
   *perception*: fine bubbles soften first contact with the tongue, so
   bitterness reads less sharp. Never write that foaming changes the flavour.
2. **Foam is not universally "correct" in the tradition.** Urasenke whisks to
   a full fine foam; Omotesenke deliberately leaves less. So the site argues
   texture and mouthfeel, never that foam is the right way — that would
   contradict the respect-the-ceremony rule.
Supporting fact used in item 03: **over-whisking draws out bitterness**
(~15 s is the usual guidance), which is a real argument for a timed cycle.
Big, bubbly froth is under-whisked and coarse — the opposite of the goal.

**No em dashes in copy.** Founder's rule. All 145 were removed across the
site and the theme, each sentence rewritten rather than patched: em dash to
full stop where two clauses stood alone, to comma where an aside was
parenthetical, to colon where a list or definition followed, to semicolon
where the clauses were balanced. Title separators use `|`, price separators
use `·` (already the design's separator), and `aria-label` reads
"Matcha Sous, home". **En dashes stay** — they are correct in ranges
(40–120 ml, 1–2 tsp) and are not what was objected to. A stray one or two
is tolerated; do not reintroduce them wholesale.

**The matcha-quality line** (founder's, and it is a positioning claim as much
as a caveat): **Sous cannot fix a poor matcha — it brings a good one to its
full flavour.** It says the machine is an amplifier, not a rescue, which is
consistent with respecting the ceremony *and* protects against reviews from
people who bought $8 culinary powder. It sits in the `#how` lead, the
homepage Q&A "Can I use any matcha?" and `faq.html`'s "What matcha works
best?" (+ its schema). Never let "works with any matcha" stand alone
without it.

### Creative direction: retrospective inevitability

The product's real promise is not a better bowl, it is **frequency**. Owners
move from occasional matcha to daily matcha, and once something is daily it
stops being an appliance and becomes part of the counter. The customer's
realisation is therefore backward-looking: *how was I doing this before?*
That is what the founder means by "impact", "life-changing", "never look
back", and it is why benefit copy kept missing — benefit copy describes the
machine, and this feeling is about the owner's life.

**Two rules fall out of it.**
1. **Never claim it.** "Life-changing", "the thing you didn't know you
   needed" and "you'll never go back" are assertions of indispensability,
   which is the least persuasive form of that message and is banned promo
   language besides. The brand's job is to let the reader reach it. That
   arrives properly with reviews, not copy.
2. **Ask, then predict.** The page opens on a question and closes on a
   prediction, and both hand the conclusion to the reader:
   - Hero: *"Does it count as taking up counter space if you use it every day?"*
   - Close: *"Give it a month. Then try going back."*
   The interrogative is the ownable voice here. Almost nobody in DTC asks.

**The close ties the claim to the guarantee.** "Give it a month" is exactly
the 30-day return window named in the line beneath it, so the headline and
the fine print now argue together: the return policy is the mechanism that
makes the dare credible. Do not separate them.

**The hero lead is the counter-space line** (the founder's, verbatim):
**"Does it count as taking up counter space if you use it every day?"**
It replaced "Smooth, consistent matcha at the press of a button", which
restated a spec in the most-read position on the site. This one does the
opposite of the rest of the page: every other line describes the machine,
this one describes the owner's life. It also answers the real objection to a
$199 single-purpose appliance by refusing the premise rather than arguing
with it, and it earns "Made to live on your counter" further down. Do not
replace it with a benefit statement.

**No orphaned words in headings.** Founder's rule: a heading must never drop
a single word onto its own line. `text-wrap:balance` on `h1,h2,h3` plus
`text-wrap:pretty` on body copy is only half of it — balance cannot rescue a
two- or three-word heading that is being *forced* to wrap by a container
narrower than the words need. Three real causes were fixed:
1. `.head--idx .head-body{max-width:44ch}` was sized for the lead but caged
   the much larger heading. Heading and lead now carry separate measures
   (`h2.display` 19ch of its own font; the lead stays 44ch).
2. `.pagehero .inner{max-width:680px}` capped the page-hero h1 below the
   width its words needed. The cap moved to the lead; the h1 takes 22ch.
3. Four feature cards at 1024px left each column too narrow for a two-word
   head, so the 2-up breakpoint moved from 1000px to 1100px.
`.pagehero h1` is `clamp(1.85rem,8.2vw,4.4rem)`: the small floor is what
makes a three-word head fit a 360px phone, and the steep 8.2vw is what stops
that floor flattening every phone to the same size.
**Verify with `scratchpad/orphans.py`** — it walks every h1/h2/h3 on all 11
pages at 9 widths and reports any whose last visual line holds one word.
Currently zero. Re-run it after any type-size or container-width change.

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
1b. **Price**: **$199, one price.** No preorder discount — the $20 off was
   ~35% of net profit at a realistic CAC while being too small to move
   anyone, and it broke the wholesale maths. The preorder benefit is instead
   **first-run access + starter matcha in the box**, which costs a fraction
   of $20 and is worth more. Landed cost is **$62**, so $199 is a 3.2x
   multiple — barely inside the 3-4x DTC floor. **Do not discount below
   $199 without redoing the unit economics**; at $179 the multiple is 2.9x
   and a 50%-of-MSRP wholesale deal leaves $27.50/unit, which cannot fund a
   stockist programme. If wholesale becomes a real channel, list should rise
   to **$229-249** (at $249, keystone leaves $62.50 = 2x landed).
   Price appears in: buy box, CTA band, five Journal CTAs, meta + OG
   descriptions, Product schema `price`, Shopify `fallback_price`.
   `proposals/` still shows $150 by design. **Grep `$1` before changing it.**
1b-iii. **No matcha in the box, and no preorder incentive at all.** The
   founder's call: $199 flat, nothing bundled, no discount. The preorder
   therefore offers only first-run access and free cancellation — worth
   knowing if preorder conversion comes in low, since there is currently no
   reason to order now rather than at launch. A bundled tin (collab or
   private label) remains the cheapest lever if that becomes a problem.
1b-0. **US shipping only, first run.** Stated in the buy box ("free US
   shipping" + "Free shipping across the US"), the CTA band, about,
   how-to-use, `stockists.html`, and as a Q&A on both the homepage and
   `faq.html`. The Product offer carries `shippingDetails` (free, US) and
   `areaServed: US`. **The stockists page said "worldwide" for one deploy** —
   if the scope changes again, grep `worldwide|free shipping|international`
   before announcing it.
1b-ii. **Preorder cancellation** (founder's terms): cancellable any time
   before shipping, full refund, no reason required; the 30-day return takes
   over once it has shipped. Stated in the buy box assurances, the homepage
   Q&A and `faq.html` — and mirrored in the FAQPage schema, which must stay
   1:1 with the visible `<summary>` list or Google drops the rich result.
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

**Tile size follows the master's width, not taste.** The 270px phone cap is
gone: it existed only because the old cut was a 760px master. Against the
current 1080px one the tile runs full width and still downsamples —
350 CSS px on a 390px phone is 1050 real pixels at 3x. Measured:

| viewport | tile | real px | vs 1080 master |
|---|---|---|---|
| 360 @3x | 320 | 960 | native |
| 390 @3x | 350 | 1050 | native |
| 430 @3x | 387 | 1161 | 1.07x |
| 390 @4x | 350 | 1400 | 1.30x |
| 768 @2x | 691 | 1382 | 1.28x |
| 1440 @2x | 568 | 1136 | 1.05x |

The founder does not want the **desktop** tile grown; 568 CSS px stays.
Before changing any of these, check the master's width and redo the sum.

**Wanted: a 1080p master.** The founder's 4K originals live in Drive but
cannot be retrieved — the Drive connector caps downloads at 10 MB, the Drive
API needs an OAuth token, and every Google file-serving host is blocked by
the proxy. A 1080x1920 export uploaded through chat (under 30 MB) would allow
~1100-1200 px wide output, which would finally cover the 2x tile without
upscaling. That is the only remaining gain — the tile size is settled.

**Cache-busting**: stylesheet links carry `?v=N` (currently **v=39**).
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
- JSON-LD: Organization, WebSite, Product+Offer ($199), BreadcrumbList, FAQPage
