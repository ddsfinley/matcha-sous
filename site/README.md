# Matcha Sous — site

Static, no framework. Bone & aubergine identity: bright warm ground, the
wordmark's deep aubergine carrying type, buttons and feature bands, copper
only at small scale. Poiret One (display) + Jost (utility). Lives in
`/site`; the legacy storefront at the repo root is untouched.

## Pages
- `index.html` — rebuilt to the founder's full copy deck (17 sections):
  hero → brand moment → the experience → how Sous prepares matcha →
  the method (4 steps) → design → control → the chasen → the tea →
  our story → why Sous → **product** → matcha your way → questions →
  Journal → final CTA → email.
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

**The cycle is two phases, not one speed.** Founder-supplied and now the
spine of the `#how` section: matcha does not dissolve, it **suspends**, so
what matters is how it is moved through water. Sous starts on a fast vortex
to suspend the powder evenly, then **slows** to work larger bubbles down
into a finer foam. First suspension, then refinement. The old copy said
"calibrated speeds hold the fast, shallow motion", which described a single
sustained speed and was **wrong**. The three numbered items are now the
sequence (suspend, refine, stop) rather than three unrelated claims.
**Verify against the firmware before print**: this is a specific mechanical
claim, and it should hold across all three presets or be qualified.

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

**Do not reinstate a trial framing in the close** ("give it a month", "try
it", "then go back"). There are no returns, so there is nothing for the buyer
to fall back on if they dislike it. An earlier close made exactly that
mistake because it had been written against a 30-day window.

**The hero and the closing band currently have no copy but the headline and
the offer.** Both lines the founder had approved were pulled: the hero lead
("Does it count as taking up counter space...") and the closing headline
("A month in, you won't remember the other way"). The hero is now statement
plus button; the closing band is offer plus button. Both slots are open.
`.hero h1 + .cta` carries the extra top margin the missing lead used to
provide, as an adjacent-sibling rule so it self-heals if a lead returns.
The Shopify hero `benefit` and cta-band `eyebrow`/`heading` default to blank
and are now guarded with `!= blank`, so the theme does not render empty
elements.

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
1. **Checkout**: the buy button is now a **working reservation**, not a dead
   link. It opens a pre-filled email to `care@matchasous.com` and is labelled
   "Reserve your Sous", with `Nothing is charged until your Sous ships.`
   underneath. The previous `https://checkout.matchasous.com/matcha-sous`
   placeholder did not resolve, so the single most important button on the
   site did nothing when clicked. **There is exactly one place this action is
   defined** — the `<!-- CHECKOUT: -->` comment in `index.html` inside
   `#order`. When the hosted store is live, change that one `href` and set the
   label back to "Shop Matcha Sous". Every other CTA on every page is an
   anchor to `#order`, so nothing else needs touching.
   The reservation copy also answers "when does it ship", which nothing on the
   site did before: no date is claimed, but no money moves until one exists.
1b. **Price: $150, one price.** Set by the founder. History: $199 →
   $179 → **$150**. No preorder discount and nothing bundled.

   Where it lives — **grep `$1` before changing it**: buy box, Product schema
   `price` (as `150.00`), the `mailto:` reservation body (URL-encoded
   `%24150`), meta + OG + Twitter descriptions, `stockists.html`, five Journal
   CTAs, Shopify `fallback_price` and the CTA-band default, `SHOPIFY-SETUP.md`.
   `proposals/` also shows $150, but by coincidence now rather than by design —
   those are superseded comps and stay `Disallow:`ed in `robots.txt`.

   **The economics, recorded plainly so they are not rediscovered later.**
   Landed cost is **$62**. At $150 that is a **2.4x multiple**, below the 3-4x
   DTC floor (it was 3.2x at $199 and 2.9x at $179). Two consequences:
   - **DTC**: $88 gross a unit has to cover CAC, payment fees, support,
     returns-in-practice and overhead. Paid acquisition for a $150 first-time
     countertop appliance from an unknown brand rarely comes in under $50-70,
     so paid is close to break-even from day one. This price works if the
     channel is organic, owned audience and word of mouth; it does not
     self-fund a paid engine.
   - **Wholesale is off the table at this price.** A 50%-of-MSRP stockist
     deal is $75 against $62 landed — **$13 a unit**, which does not cover
     the cost of servicing a stockist, let alone fund the programme. The site
     still has a `wholesale.html`. If wholesale is ever meant to be a real
     channel, list has to rise (at $249, keystone leaves $62.50 = 2x landed)
     or landed cost has to fall.

   Raised both points; the founder chose $150. Not a blocker — it is a
   coherent strategy for an organic-first launch — but the wholesale page is
   now writing a cheque the price cannot cash.
1b-BOX-CONFLICT. **The two box renders disagree with each other, and the site
   currently follows the insert card.** `assets/images/launch-guide.jpg` shows
   the printed back panel, whose WHAT'S INCLUDED reads: Mixer Base, Matcha Cup,
   **Power Adapter**, USB-C Cable, User Manual — **no mixing rod**, and no
   recipes. The insert card the site was built from lists a mixing rod and
   "full manual + recipes" instead. The buy box says "Mixing rod · included".
   One of the two is wrong and only the founder can say which. **If the printed
   carton is the one going out, the buy box is promising an item that is not in
   it**, which is the kind of small untruth that generates support tickets and
   chargebacks. Settle it before the run ships. (The back panel also carries
   **6 W low power**, a spec that appears nowhere on the site.)
1b-BOX. **Box contents per the packaging insert.** Mixing base, stainless steel
   mixing cup, **mixing rod**, **USB-C charging cable**, full manual + recipes. Two things this corrected
   on the site: the mixing rod appeared nowhere at all, and "Powered USB-C"
   implied a cord. It **charges**, so it runs cordless, which is a selling
   point the site had never claimed. Also retired "Nothing goes in the cup"
   from the mechanism copy: the mixing element sits in the cup, so the true
   claim is that no whisk and no hand do.
1b-iii. **No matcha in the box, and no preorder incentive at all.** The
   founder's call: one flat price, nothing bundled, no discount. The preorder
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
1b-ii. **No returns. Cancellation before shipping, plus a 1-year warranty
   against manufacturing defects. That is the whole policy** (founder's
   decision). Cancellation is now the only pre-purchase reassurance the site
   offers, so it stays first in the buy box assurances and prominent in both
   FAQs, mirrored in the FAQPage schema, which must stay 1:1 with the visible
   `<summary>` list or Google drops the rich result. Product schema declares
   `hasMerchantReturnPolicy: MerchantReturnNotPermitted` rather than leaving
   it unstated. **Risk accepted knowingly:** taking preorder money with no
   return path is the highest-exposure profile for card chargebacks, and at
   $199 from a brand with no reviews a return policy is usually what
   substitutes for trust not yet earned. If disputes appear after launch,
   revisit this first.
1c. **Photography is the biggest remaining gap, and it is a commercial one,
   not a stylistic one.** `photo-profile.webp` and `mood-counter.webp` are
   flash-lit phone shots: textured wall, brass rail, scratched counter, and a
   terracotta sleeve that reads as a mismatched accessory. `photo-profile` was
   the **primary buy-box image** — the frame a buyer stares at while deciding
   whether to spend $199. Both are now **retired from the homepage** in favour
   of `cycle-poster.webp` (top-down, machine plus finished matcha) and
   `detail-instrument.webp` (top-down, clean). They remain in the repo.
   The packaging shoot (`photo-kit`, `photo-case`) is genuinely good, which
   proves the standard is reachable — the machine itself has simply never been
   shot properly. **Still missing entirely: any photograph of a person, and any
   photograph of the finished drink in a glass someone would want.** Zero of
   the homepage images contain a human being. That, plus the absence of any
   review, testimonial or press mention, means the site currently asks for $199
   on typography alone. A day of proper product photography would move
   conversion more than every other open item combined.
1d. **Claim verification**: contactless magnetic drive and backlit touch
   controls — both **confirmed by the founder**. Box-verified facts: 18 speed
   levels, 3 preset programs, 40–120 ml capacity, hands-free preparation,
   easy-clean design, 6 W low power; included: mixer base, matcha cup,
   power adapter, USB-C cable, user manual; marks FCC, CE, RoHS.
2. Deploy `/site` contents at the **domain root** of matchasous.com — canonicals,
   OG URLs, `sitemap.xml` and `robots.txt` already point there.
3. Submit `sitemap.xml` in Google Search Console.
4. Emails `care@` / `wholesale@matchasous.com` must exist (or edit them).
   **`care@` now receives the reservations**, so it must exist before launch or
   the buy button is dead again.
5. `proposals/` is superseded design exploration that still shows **$150**.
   Kept for reference, but `noindex` on every page *and* `Disallow: /proposals/`
   in `robots.txt`. Do not link to it, and do not let it into the sitemap.

## Editorial rules learned the hard way

- **Use contractions.** The landing page ran with exactly one contraction on
  it, and that one was a possessive. No rule required this; it happened by
  default, and it is the single loudest tell that copy was not written by a
  person. "You don't touch it" and "you do not touch it" carry the same
  meaning and completely different temperatures.
- **Break the symmetry.** Tricolons, `X, not Y` antitheses and premise /
  contrast / conclusion arguments read as assembled. The page had four of the
  antitheses and five tricolons at once. One is a flourish. Five is a machine.
- **Do not state the moral.** "So that is the part Sous takes" explains the
  conclusion the reader was about to reach on their own, which kills it.
- **Sensation before argument.** "Foam fine enough to hold a line" does more
  than any sentence explaining why consistency matters.
- **No puns.** "Sousper smooth" closed the opening section for one deploy and
  was cut on the founder's call. The reason is structural, not taste: it was
  the only joke on an otherwise straight-faced page, so it did not read as
  wit, it read as a lapse in a voice that is otherwise completely composed.
  A brand can be funny or it can be composed; one pun buys neither. The
  section now closes by bolding the end of the line above it, which keeps the
  visual full stop without inventing a third sentence to carry it.

- **Say a thing once.** The homepage carried four sections making the same
  argument: "The Experience", "The Chasen", "The Tea" and "Why Sous" each
  ended on some form of *you choose the tea, Sous handles its part* — the
  sentence appeared near-verbatim three times. The Chasen and The Tea are now
  one section ("Keep the chasen. Choose the tea."), The Experience lost the
  paragraph Why Sous already owned, and Why Sous is two paragraphs. That is
  the real reason the page was ~13,000 px, not length for its own sake.
- **The price goes above the philosophy.** The buy box used to be section 12
  of 17, roughly 9,000 px down, behind seven consecutive prose blocks. It now
  sits directly after Control, at about the halfway mark. Brand copy that
  needs to convince someone still runs *after* the decision point, where it
  serves the people who need it.
- **Numbered lists must be one set.** "How Sous prepares matcha" listed
  01 The faster stage, 02 The finishing stage, 03 Press start. Items 1 and 2
  are stages of the machine's cycle; item 3 is a thing the owner does before
  either, and its body copy was a slogan rather than a step. Removed.
- **US spellings on a US-only store.** "Millilitres", "honour", "moulded",
  "colour" were all live. Grep before shipping copy.
- **One verb for one action.** "Buy now", "Preorder" and "Reserve your Sous"
  all pointed at the same anchor. Three labels read as three offers.

## California Proposition 65

**This is the one part of the site that is legally operative. Do not edit it
for tone, length or rhythm.** The wording is the safe-harbor text from
27 CCR 25603(a)(2); departing from it forfeits the safe harbor.

**Where it is.** Inside `.buybox` on `index.html` and `stockists.html`, plus a
`p65_chemical` / `p65_harm` setting pair on `sections/buy-box.liquid`. It is in
the buy box, not the footer and not behind a toggle, because 27 CCR 25602(b)
requires an internet warning to reach the buyer **before the purchase
completes, without them having to seek it out**. `faq.html` carries a Q&A that
*explains* the warning; that answer is not a substitute for the warning and
must never become one. It is deliberately kept out of the FAQPage JSON-LD — an
FAQ rich result reading "why is there a cancer warning" is not something to
invite into a search listing.

**The symbol** is the regulation's, not the brand's: black exclamation mark in
a yellow equilateral triangle with a bold black outline, to the left of the
text, at a height no smaller than the word WARNING. `.p65-mark` is sized in
`em` so it tracks the type. Do not recolour it to the palette.

### Two things that must be settled before launch

1. **THE CHEMICAL NAMED IS A PLACEHOLDER.** The warning currently names
   **DEHP**, which is the most probable candidate for this product class — the
   usual exposure route for a small appliance is the plasticiser in a
   PVC-jacketed cable or power adapter, and DEHP is listed for both cancer and
   reproductive harm, so one name covers both endpoints. **It has not been
   confirmed.** Settle it by getting the factory's Prop 65 / CA compliance
   statement and test report, or by sending a unit for a lab screen (SGS,
   Bureau Veritas, Intertek; roughly $300–800). Then change the name in **all
   four places at once**: `index.html`, `stockists.html`, the Shopify setting,
   and the FAQ answer's sentence about which part the chemical comes from.
2. **The retail box carries FCC, CE and RoHS but no Prop 65 warning.** If a
   warning is required, it is required on the package too, not only on the
   website, and the box art is already finished. The cheap fix everyone uses
   when they find this late is a label on the carton; the expensive fix is a
   reprint. Decide before the run, not after.

### Things worth knowing before spending money on this

- **Under 10 employees is a real exemption.** Prop 65 applies to businesses
  with 10 or more employees. A smaller company is outside the statute. That
  exemption evaporates the moment you sell through Amazon or a chain retailer,
  because they impose compliance contractually regardless, and it does not
  stop a bounty-hunter firm sending a 60-day notice you then have to answer.
- **Warning when you did not have to is cheap; not warning when you had to is
  not.** Private enforcers can seek up to $2,500 per violation per day plus
  fees, and most Prop 65 activity is plaintiff-firm driven.
- **The short-form warning changed on 1 Jan 2025** and now has to name a
  chemical. Products manufactured and labelled before **1 Jan 2028** may still
  use the old short form. The site uses the **long form**, which is a valid
  safe harbor either way and does not depend on what the box ends up saying.

*Not legal advice. This section is a build note. Have a products lawyer confirm
before the first run ships.*

## The box marks

The band above the buy box (`.marks`, `section.bg-plum`) is the four icons
printed down the side panel of the retail box, redrawn as line art: spiral /
fingertip / cup / droplet, labelled **Smooth, uniform texture · One-touch
operation · Consistent results · Easy-clean design**. Same four, same order,
same words as the print.

- **Why it exists.** The alternative on the table was an "In the box" contents
  section built from the insert card. That was rejected: a contents list is
  logistics, and the site already lists what the thing does in the buy box. The
  icons are the only part of the packaging that makes an *argument*, and
  repeating them verbatim is what makes the box feel like it came from the same
  place as the site. Buy the product and the unboxing confirms the page.
- **Drawn, not traced.** `assets/images/box.jpg` and `launch-guide.jpg` are
  renders; the icons in them are ~40 px tall in a progressive JPEG, so there is
  no usable line art to extract. All four are hand-authored SVG on a 48 grid,
  `stroke-width:1.4`, round caps. **If real vector art ever arrives from the
  packaging designer, replace the paths and keep the labels and order.**
- **The spiral is the brand mark.** Its path is `assets/images/logo-enso.svg`
  scaled 64→48 (×0.75), not a new drawing. Do not redraw it freehand.
- **Optically centred, not nominally.** Each icon's raw path centres somewhere
  other than (24,24), so each sits in a `<g transform="translate(…)">` that
  pulls its measured bounding box onto the grid centre. Measured in-browser
  with `getBBox()`; a translate is used rather than a scale **on purpose**,
  because scaling scales the stroke and a 1.30 stroke next to a 1.52 stroke is
  visible at 60 px. To resize an icon, edit its path numbers, not the
  transform — that is why the cup's geometry is larger than the box render's.
- **No heading and no body copy**, by design: the box does not explain them
  either, and the whole point is that the two artefacts agree.
- **Mirrored in Shopify** as `sections/box-marks.liquid`, wired into
  `templates/index.json` between `presets` and `buy`. The icon is a `select`
  block setting rather than an image upload so a merchant cannot break the set
  by dropping in a mismatched graphic.

## Cutting the matcha silhouette

`tile-matcha-v4.webp` is `IMG_2146` with its background masked off, via
GrabCut. Three things decide whether the edge looks clean:

- **Seed with a mask, not a rectangle.** The cup fills almost the whole frame,
  so a rect-initialised GrabCut clings to the seed rectangle down one side and
  flattens the cup's edge. Certain background in a 1.5% border, certain
  foreground in the middle third, everything else probable, twelve iterations.
- **Never `approxPolyDP` the contour.** It turns a curve into line segments and
  the facets show. The earlier `epsilon=1.2` pass is what made the edge look
  chipped.
- **Smooth by blur-and-rethreshold, not by eroding.** GrabCut runs at half
  resolution, so every mask pixel is 2px at full size and the boundary
  stair-steps. Upscale with `INTER_LINEAR`, Gaussian sigma 18, rethreshold at
  127. That rounds the steps off without moving the shape. Then a 5px erode to
  bite off the light colour fringe, and sigma 1.6 for a ~2px anti-aliased
  alpha ramp. Save with `exact=True` so WebP keeps the ramp.

- **Fill dents in polar, not in 2D.** Blur-and-rethreshold smooths the edge but
  leaves inward dents where GrabCut clipped the rim. Take the boundary as a
  radius profile r(theta) around the centroid, run a circular grey closing over
  it (~11 degrees wide), then a light circular smooth. Closing can only raise a
  value, so dents fill and the spout, a +22px positive feature, is untouched.
  On the last pass this took the lower-right dent from -8.2 to -0.6 and the
  left from -8.2 to -3.8, in thousandths of the mean radius.
  The residual readings near 259 and 301 degrees are not defects: they are the
  concave shoulders either side of the spout, which are real.

What does **not** work: suppressing dark pixels near the mask edge to remove
the black base showing past the rim. The rim in shadow is as dark as the base,
so it bites notches out of the cup.

## Image caching

**Version the filename whenever an image's content changes.** Three different
cut-outs shipped as `tile-matcha.webp` in one afternoon, and the browser kept
serving the first one, which was the badly cropped version. Every re-cut looked
identical on the live site because the bytes never got refetched. It cost three
rounds of the founder telling me the picture was wrong while the repo held the
right one. The file is now `tile-matcha-v3.webp`; `cycle-1080-v3.*` carries the
same suffix for the same reason. CSS has `?v=NN`; images and video get a
suffix in the name.

## Video

`assets/vid/cycle-1080-v3.webm` / `.mp4` (1080x1440, 8.80 s, 30 fps) is the
showcase clip, cut from `matcha_short10.mov` (1080x1920 HEVC, 8.77 s) with
`crop=1080:1440:0:140` and `-r 30`, audio dropped, at **native speed**.

- **Crop offset 140** of the 480 available. It keeps the spout fully in frame
  with headroom above it and leaves the base and its countdown visible along
  the bottom. 230 also frames the cup but pushes the spout tip against the top
  edge; past 320 the spout is cut off.
- **No speed change on this clip.** Its predecessor was sped up 1.5x because
  11.9 s dragged. This one is 8.8 s in the can, within a second of what that
  1.5x version ran at, so it is already the right pace.
- **Lock the frame rate anyway.** `setpts` rewrites timestamps but sets no
  output rate: on the previous clip VP9 emitted 45 fps while x264 defaulted to
  25 and discarded a third of the frames. Pass `-r 30` whether or not the
  speed changes.

The poster (`assets/img/cycle-poster-v2.webp`) is **frame 0 of the encoded
video**, so nothing jumps when playback starts. It is also the buy-box primary
image and one of the four Product schema images, so it changes in three places
at once. Regenerate it whenever the video changes.

Filenames carry a version suffix on purpose. Videos and images are cached hard
and a same-named replacement serves stale bytes; see the caching section above.

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

**Cache-busting**: stylesheet links carry `?v=N` (currently **v=41**).
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
