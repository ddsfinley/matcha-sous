# Matcha Sous — site

Static, no framework. Bone & aubergine identity: bright warm ground, the
wordmark's deep aubergine carrying type, buttons and feature bands, copper
only at small scale. Poiret One (display) + Jost (utility). Lives in
`/site`; the legacy storefront at the repo root is untouched.

## Prelaunch review pass

A founder-authored, 19-point prelaunch brand/copy/conversion review was
implemented close to verbatim: primary nav trimmed to Shop / How it works /
Our story / FAQ / Reserve your Sous (Journal, Where to buy, Wholesale stay
footer-only); hero gained a supporting line under the H1; the Sous Cycle
and ritual/method sections got revised copy; the Control section was
renamed "Three settings. Eighteen speeds." with an "Etched guides" card
replacing "Milliliters"; a new "Born from repetition." credibility section
was added between Control and the box marks; the buybox was trimmed to 8
primary features plus a separate "What's included" list; the "Keep the
chasen" and founder-note sections were replaced with one short line; the
Final CTA got a new headline. "Vessel" became "mixing cup" and
whisk-as-machine-action became "mix" everywhere the machine is described
(not in journal articles about hand-whisking technique, where "whisk" is
the correct word for what's being discussed). Several absolute-sounding
claims were softened per the brief's own suggested phrasing.

### Things this pass surfaced that needed a decision, not just a copy edit

1. **"The same cup, every time." was a deliberate founder choice, not an
   oversight** - reached after several rounds of revision earlier in this
   project, then explicitly asked to be shortened to exactly that line.
   This brief's item 15 named that same line as an absolute claim to
   qualify. Followed the newer, more explicit instruction (now "A more
   repeatable cup."), since a full prelaunch review supersedes an earlier
   pass - but this reverses a specific past decision, so it's flagged
   here rather than silently overwritten. **Resolved:** on review, the
   founder asked for this line back specifically. about.html reads "The
   same cup, every time." again - see "Round two" below.
2. **The brief's checkout item and an earlier instruction directly
   conflict.** This pass asks the payment page to show "the final
   post-shipment return policy." Earlier in this same project, the
   founder explicitly said "keep the we do not accept returns for change
   of mind, i dont need the 7 day return" - i.e., there is no return
   policy beyond the warranty. Nothing was added for this line pending
   which one is actually current. **Resolved:** the founder's actual
   policy (no change-of-mind returns once a unit ships, only the one-year
   warranty) is now stated formally in terms-of-sale.html's "Returns and
   the warranty" section, instead of living only in project history.
3. **`/site`'s "Reserve your Sous" button still cannot lead to a real
   payment page.** It's a static site with no backend - see "Payment
   timing" below for the same constraint already documented for the
   Shopify side. The button, copy and structure are ready; only a live
   checkout can make it literal.
4. **No Terms of Sale page exists.** Warranty and Privacy Policy do;
   there's no separate page covering general terms of sale (liability,
   governing law, arbitration, etc.) if one is wanted beyond what
   warranty.html already covers for defects specifically. **Resolved:**
   added terms-of-sale.html (agreement, orders and payment, cancellation,
   shipping, returns and the warranty, product information, and the
   liability/IP/changes-to-terms fine print), linked from every page
   footer and the sitemap.
5. **Conversion tracking (item 19) needs a platform decision before any
   code.** Adding analytics scripts would also require updating
   privacy-policy.html's Cookies section, which currently states
   correctly that the site runs no tracking today - don't add one without
   the other.
6. **The `sameAs` social links (Instagram/TikTok/YouTube) in index.html's
   Organization schema can't be verified as active from here** - no way
   to check whether those accounts exist or are live. Confirm and remove
   any that aren't before launch.
7. **`hero-vortex.mp4` is 7.2 MB**, autoplaying on every visit including
   mobile. Worth re-encoding/compressing before launch; not attempted
   here since it needs a video pipeline, not a text edit. **Resolved:**
   re-encoded (H.264 CRF 27 + a matching VP9/WebM source), verified
   frame-by-frame against the originals for no visible quality loss.
   `hero-vortex-v2` is 4.9 MB (MP4) / 2.8 MB (WebM), down from 7.2 MB.
   The product-cycle video got the same treatment as `cycle-1080-v4`. Old
   files were deleted only after confirming nothing still referenced
   them, per this file's asset-versioning convention.

### Round two: restoring warmth after founder feedback

The 19-point pass above was implemented close to verbatim, and on review
it had over-corrected - clearer and more accurate, but colder, having
quietly dropped things that mattered: the countertop-object pride in the
"Keep the chasen" section, the separate founder-note line that used to
close the page, and the personal, specific version of the origin story.
Founder feedback asked for the best of both versions: keep items 1, 2, 4
and 7 above, but bring back what made the rest feel washed out, and
recover the sense of the product as a hero on the counter rather than
something just being sold.

Kept from the 19-point pass: the trimmed nav, terminology accuracy
(mixing cup / mixing rod / saved settings), the qualified claims (aside
from item 1, reverted above), and the buybox's spec-list structure.

Restored or rebuilt, tighter than either earlier version:
- **"Keep the chasen" is a full section again**, not the single bare
  line it was cut to. One belief about the object (it belongs on the
  counter), one line of reassurance that the tea is still the drinker's
  choice, and the same closing line the old separate founder-note
  blockquote used to end the page with ("A Sous in service of the
  ritual."), now folded into the section instead of standing apart from
  it.
- **The origin story regained its personal detail.** "Born from
  repetition" now opens in the first person - behind the café bar,
  never getting silky microfoam reliably, never in a hurry - before the
  existing "we designed Sous to support that one step" paragraph, instead
  of starting from an impersonal "we."
- **The buybox closer names the counter again**: "designed to earn a
  permanent spot on your counter," replacing a line that only described
  the cycle.

Items 3, 5 and 6 above are unchanged and still open.

## Deployment

`.github/workflows/deploy-pages.yml` (manual `workflow_dispatch` only)
deploys `/site` as the GitHub Pages root — **not the repo root.** This
matters because of the line above: the repo root carries its own older,
unrelated build of this site (its own `index.html`, `checkout.html`,
`cart.html`, etc.). Uploading the repo root as-is would make the plain
Pages URL serve that stale version instead of the current one, while the
real site sat one directory down at a `/site/` path nobody was told to
visit. Found and fixed the same day the warranty and privacy pages
shipped, after a working link kept not showing the current site. Don't
change `path: "./site"` back to `path: "."` without either deleting the
legacy root files first or accepting that regression again.

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
- `warranty.html` — Magnuson-Moss Limited Warranty disclosure: coverage, exclusions,
  claims process, implied-warranty and liability terms. See "Warranty page" below.
- `privacy-policy.html` — what's collected, how it's used, who it's shared with,
  cookies, Shopify hosting/payment security. See "Privacy Policy" below.
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
   "Reserve your Sous", with `Payment is collected when you reserve. Cancel
   any time before it ships, for a full refund.` underneath - payment timing
   was corrected from "nothing is charged until it ships" to "charged at
   order" site-wide on founder direction; see "Payment timing" below for
   every place that touched. The previous `https://checkout.matchasous.com/matcha-sous`
   placeholder did not resolve, so the single most important button on the
   site did nothing when clicked. **There is exactly one place this action is
   defined** — the `<!-- CHECKOUT: -->` comment in `index.html` inside
   `#order`. When the hosted store is live, change that one `href` and set the
   label back to "Shop Matcha Sous". Every other CTA on every page is an
   anchor to `#order`, so nothing else needs touching.
   The reservation copy also answers "when does it ship", which nothing on the
   site did before: no date is claimed, but no money moves until one exists.
1b. **Price: $179, one price.** Set by the founder. History: $199 → $179 →
   $150 → **$179**. No preorder discount and nothing bundled.
   **Landed cost is $60, confirmed by the founder** (not FOB — landed).

   Where it lives — **grep `$1` before changing it**: buy box, Product schema
   `price` (as `179.00`), the `mailto:` reservation body (URL-encoded
   `%24179`), meta + OG + Twitter descriptions, `stockists.html`, five Journal
   CTAs, Shopify `fallback_price` and the CTA-band default, `SHOPIFY-SETUP.md`.
   `proposals/` still shows $150; those are superseded comps carrying an
   obsolete price and stay `Disallow:`ed in `robots.txt`.

   **The unit economics, so they are not rediscovered later.** At $60 landed,
   $179 is a **3.0x multiple** — the first price in this product's history that
   clears the 3-4x DTC floor rather than sitting under it. Per unit:

   | | $150 | **$179** | $199 | $249 |
   |---|---|---|---|---|
   | Landed | 60.00 | 60.00 | 60.00 | 60.00 |
   | Fulfilment + outbound | 12.00 | 12.00 | 12.00 | 12.00 |
   | Payment fees (2.9%+30c) | 4.65 | 5.49 | 6.07 | 7.52 |
   | Warranty/damage reserve (5%) | 7.50 | 8.95 | 9.95 | 12.45 |
   | Support | 3.00 | 3.00 | 3.00 | 3.00 |
   | **Left to acquire a customer** | **62.85** | **89.56** | **107.98** | **154.03** |

   Blended CAC for a design-led countertop appliance from a brand with no
   reviews realistically lands **$50-90**. That is why $150 was a problem: it
   broke even against its own CAC, so the business could only ever be organic.
   $179 leaves roughly $20-40 a unit after acquisition, which is thin but is a
   business.

   **Wholesale is still off the table.** 50% of MSRP is $89.50 against $60
   landed = **$29.50 a unit**, which does not cover the cost of servicing a
   stockist. **$249 is the first list price where wholesale works** ($124.50
   less $60 = $64.50, 2.1x landed). `wholesale.html` is live and promising a
   channel this price cannot fund. Either it comes down or list rises when
   wholesale becomes real. Raised twice; not yet resolved.

1b-PRICE-CEILING. **$179 is the right number today; $199 is the right number
   once there is proof — and that ordering matters.** Judged as an object
   rather than as a cost-plus calculation, the buyer's reference set is a
   chasen at $25, a handheld frother at $20, and an Aeroccino at ~$100 that
   also *heats*. What lifts Matcha Sous above them is that nothing else runs a
   matcha-specific two-stage cycle, and that the buyer is someone who already
   spends $40 on a tin — for that person the reference price is the other
   objects on the shelf, which is how Fellow holds $199 for a kettle.

   The object can carry $199. **The listing cannot, yet**, because the site has
   no reviews, no press, no ship date, no photograph of a person, and no
   photograph of the finished drink in a bowl someone is about to pick up. At
   $179 a stranger will take that on faith. At $199 they want evidence.
   Raising $179 to $199 after reviews exist is easy; cutting is not.

   **The live risk to any price above ~$120: if this is an ODM base rather
   than exclusive tooling**, a near-identical unit will surface on Amazon at
   $69-89 under three brand names, and one Reddit thread does the damage. If
   the tooling, the drive spec or the two-stage firmware is genuinely
   exclusive, $199 is safe and the price can rise. **This has not been
   confirmed and is the single biggest open question on pricing.**
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
   $179 from a brand with no reviews a return policy is usually what
   substitutes for trust not yet earned. If disputes appear after launch,
   revisit this first.
1c. **Photography is the biggest remaining gap, and it is a commercial one,
   not a stylistic one.** `photo-profile.webp` and `mood-counter.webp` are
   flash-lit phone shots: textured wall, brass rail, scratched counter, and a
   terracotta sleeve that reads as a mismatched accessory. `photo-profile` was
   the **primary buy-box image** — the frame a buyer stares at while deciding
   whether to spend $179. Both are now **retired from the homepage** in favour
   of `cycle-poster.webp` (top-down, machine plus finished matcha) and
   `detail-instrument.webp` (top-down, clean). They remain in the repo.
   The packaging shoot (`photo-kit`, `photo-case`) is genuinely good, which
   proves the standard is reachable — the machine itself has simply never been
   shot properly. **Still missing entirely: any photograph of a person, and any
   photograph of the finished drink in a glass someone would want.** Zero of
   the homepage images contain a human being. That, plus the absence of any
   review, testimonial or press mention, means the site currently asks for $179
   on typography alone. It is also the reason $179 rather than $199: the
   object can carry the higher number, the evidence cannot. A day of proper product photography would move
   conversion more than every other open item combined.
1d. **Claim verification**: contactless magnetic drive and backlit touch
   controls — both **confirmed by the founder**. Box-verified facts: 18 speed
   levels, 3 preset programs, 40–120 ml capacity, hands-free preparation,
   easy-clean design, 6 W low power; included: mixer base, matcha cup,
   power adapter, USB-C cable, user manual; marks FCC, CE, RoHS.
1d-i. **FCC, CE and RoHS badges were added to the footer, then removed on the
   founder's call, correctly.** They are three different things: FCC is US and
   genuinely applies (any device with a motor and digital electronics is an
   unintentional RF emitter under Part 15); CE and RoHS are EU marks and this
   store is US-only, so they were noise for this market regardless. More to
   the point, a mark on a website is a claim — displaying one without the
   underlying test report / Declaration of Conformity on file is a liability,
   not "free credibility." **FCC is still a real, open item**: get the
   Supplier's Declaration of Conformity or test report from the manufacturer.
   It belongs in a compliance/support doc a buyer can request, not as a footer
   badge. Do not re-add CE or RoHS unless the store starts shipping to the EU.
2. Deploy `/site` contents at the **domain root** of matchasous.com — canonicals,
   OG URLs, `sitemap.xml` and `robots.txt` already point there.
3. Submit `sitemap.xml` in Google Search Console.
4. Emails `care@` / `wholesale@matchasous.com` must exist (or edit them).
   **`care@` now receives the reservations**, so it must exist before launch or
   the buy button is dead again.
5. `proposals/` is superseded design exploration carrying an obsolete price.
   Kept for reference, but `noindex` on every page *and* `Disallow: /proposals/`
   in `robots.txt`. Do not link to it, and do not let it into the sitemap.

## Payment timing

**Payment is collected when an order is placed, not when it ships.** This
reverses the promise the site made from its very first draft through most of
this project's history: "Nothing is charged until your Sous ships." That
line was accurate for the mailto-reservation flow (no payment processor was
attached to it, so nothing *could* be charged), but it stopped being
accurate the moment real checkout enters the picture, since Shopify's
standard checkout charges at the point of purchase by default. Corrected
site-wide on founder direction rather than left as a landmine for whenever
checkout goes live:

- `site/index.html` — the buy-box `paynote` and the mailto reservation
  body text (both said "nothing is charged").
- `site/about.html`, `site/warranty.html`, `site/privacy-policy.html` — all
  three share the same CTA-band lead line, which made the same claim.
- `shopify-theme/sections/buy-box.liquid` — the `paynote` setting's
  default value.

**What didn't need to change**: `faq.html`'s cancellation answers already
said "cancelled any time before they ship, for a full refund" — a refund
promise, not a deferred-charge claim, so it was correct all along and stays
that way. The corrected wording everywhere else follows the same pattern:
state that payment happens now, and that cancelling before shipment still
gets a full refund. Don't recombine these into "nothing is charged" again;
that is no longer true anywhere real checkout exists.

**The reservation flow (`mailto:`) still doesn't charge anyone anything** -
there is no payment processor attached to a `mailto:` link. The corrected
copy describes the policy that will be true once Shopify checkout is live,
which is also the more honest framing for the reservation flow itself:
someone clicking "Reserve your Sous" today is agreeing to a policy, not
completing a transaction, and the copy should say what happens when they
actually do transact, not what technically happens with today's stand-in.

### Two things this surfaced, still open

1. **No ship date exists anywhere in this project.** Already flagged once
   in `index.html`'s own `SHIP WINDOW` comment near the reservation button,
   and worth repeating here because charging at order without stating a
   ship window is a materially bigger gap than charging at ship time
   without one - a customer paying today reasonably wants to know when
   the product arrives. `shopify-theme/sections/main-product.liquid` has a
   `shipping_estimate` setting wired up and ready, deliberately left blank.
   Fill it in the moment there's a real timeframe; don't put a placeholder
   in it before then.
2. **Shopify's actual checkout page cannot carry custom messaging on a
   standard plan.** The founder asked for the shipping timeframe and
   cancellation line to appear "on the payment page." Real Shopify
   checkout (`/checkout`) is a locked template on non-Plus plans - no
   custom body text without Shopify Plus (`checkout.liquid`, being phased
   out) or a Checkout UI Extension (a separate app-like build, not a
   theme edit). Since the store isn't live yet and the plan tier is
   unconfirmed, neither was attempted. What's built instead: both
   assurance lines live on the product page directly above the button
   (the real "Reserve your Sous" click happens right there), and the
   `name="checkout"` submit pattern sends the customer straight to
   checkout afterward, skipping the cart page - so the messaging is seen
   immediately before the redirect rather than during it. Revisit if the
   store goes Plus, or if Shopify's non-Plus checkout customization
   options change.

## Accessibility (WCAG 2.1/2.2 AA)

**Audited with axe-core (real Playwright render of every page, not static
text parsing) rather than eyeballed.** axe-core is the same engine behind
most professional accessibility tools; it catches roughly half of real WCAG
issues automatically and cannot judge the rest (motion, reading order,
whether alt text is actually accurate) — treat a clean run as a floor, not
a certificate. Re-run before any future launch:

```
cd site/tools && npm install axe-core && python3 axe_audit.py
```

See `site/tools/axe_audit.py` for the harness itself.

**Findings, first pass: 55 violations, one root cause, on every single
page.** `--copper` (`#b0714f`) is the link/accent color, and at normal text
size it fails 4.5:1 against both light backgrounds — 3.59:1 on
`--bone-page`, 3.81:1 on `--paper`. This hit `.textlink`, `.jhome .go`,
`.recipe figcaption .num`, `.buybox .preorder`, `.article a`, and the
footer's `.fine` copyright line (a *different* failure — `rgba(bone,.5)`
over plum computed to 4.15:1). Fixed both as **token swaps, not new
colors**: the four `--copper` text uses now read `--copper-deep`
(`#96593a`, already in the palette, 5.05–5.36:1 against both light
backgrounds — nobody had to invent anything), and `.fine`'s alpha went
`.5` → `.6` (4.5:1 was reachable at .55; .6 leaves margin). **55 → 0**,
confirmed by re-running the same audit, not assumed. `--copper` itself is
untouched — it still exists and is still used for large-scale/decorative
elements (button underlines, `h1 em`/`h2 em`) where the lower contrast
either doesn't apply (non-text) or the failing rule was never on a light
background to begin with. Don't restyle `.textlink` etc. back to plain
`var(--copper)` without re-running the audit first.

**Two more, real, that automated tooling cannot fully catch on its own —
found by knowing what to look for, not by the tool flagging them:**

1. **No skip link (2.4.1 Bypass Blocks).** Added `<a class="skip-link"
   href="#main">` as the first element inside every page's `<body>`, and
   `id="main"` on every page's `<main>`. Off-screen (`top:-100px`) until
   `:focus` moves it to `top:12px` — standard pattern, verified with an
   actual `Tab` keypress in Playwright, not just present-in-the-DOM.
2. **Two autoplaying, looping, unpausable videos (2.2.2 Pause/Stop/Hide) —
   both on `index.html`.** WCAG requires a way to stop moving content that
   autoplays past 5 seconds, full stop, regardless of whether the content
   is muted or decorative. Added a real `<button class="vid-toggle">` next
   to each `<video class="loopvid">`, wired by DOM proximity
   (`btn.previousElementSibling`) rather than ids, so it is copy-pasteable
   to a future third video with zero JS changes. Verified functionally in
   Playwright: click pauses the actual `<video>` element, swaps the icon,
   swaps `aria-label` to "Play video"; click again resumes. **Separately**,
   the page now checks `matchMedia('(prefers-reduced-motion: reduce)')` on
   load and pauses + un-loops both videos before first paint for anyone who
   has that OS-level preference set — verified with Playwright's
   `reduced_motion: 'reduce'` context option, not just read off the CSS.
   The button and the reduced-motion check are independent: the button
   exists for everyone; reduced-motion is a stronger default for the
   subset of visitors who asked for it.

**Not yet ported to `shopify-theme/`** — that theme already has its own
"drifted, needs a re-port" note elsewhere in this file; carry all of the
above (token swap, skip link, video toggle + reduced-motion check) into it
when that re-port happens, not before, since the theme's markup structure
for video is not identical to `/site`'s.

**On "accessibility overlay" widgets (accessiBe, UserWay and similar), for
the record**: do not install one in place of the above. They patch the
rendered DOM at runtime and do not fix the underlying markup assistive
technology actually reads. The accessibility and legal-compliance
communities do not treat them as evidence of compliance — several 2025
lawsuits were filed against sites that had one installed, and the FTC
fined a major vendor in April 2025 for falsely claiming its widget made any
site WCAG compliant. If a "compliant in one script tag" pitch resurfaces,
it is being sold to founders precisely because writing the underlying fix
(see above) is what actually works and a widget is not a shortcut around it.

## Site-wide redundancy pass

A full re-read across all 11 pages (not just single-page edits) found the
same claims restated in multiple places — some across pages, some on the
very same page. Fixed with a consistent rule: **keep the fullest statement
in the section built for it; every other instance either earns its own new
angle, or goes.**

1. **"Sous doesn't take over" — said four times, two of them on the same
   page.** `about.html`'s Restraint card, `about.html`'s "Sous stays second
   in command" section, `index.html`'s "Keep the chasen. Choose the tea.",
   and `faq.html`'s "Does it replace a chasen?" all made the identical
   claim. Kept `about.html`'s "second in command" section as the fullest
   version (it is the section built for exactly this idea) and
   `index.html`'s chasen section untouched (different job — it is an
   objection-handler on the page where someone is about to buy, not a
   restatement of brand philosophy). **Retargeted, not deleted**: the
   Restraint card no longer discusses authorship at all — see item 3 below,
   it now covers something the page said nowhere else. The FAQ chasen
   answer was cut by two-thirds to a direct answer instead of a second
   philosophy paragraph.
2. **The two-stage mechanism, explained fresh five times.** `index.html`
   ("Mix first. Foam second.", then "Two-speed, automatic cycle.", now
   named outright as "The Sous Cycle™" with its stages "Incorporate" /
   "Refine"), `how-to-use.html` ("A change of pace, by
   design."), and three separate FAQ entries ("Why two speeds?", "What is
   the second speed doing?", "Will it create a mirror finish?") all
   re-derived the same fast-then-slow, settle-the-bubbles explanation.
   Kept `index.html`'s version as the primary/anchor. `how-to-use.html`
   keeps its own explanation — that page's whole reason for existing is to
   go deeper — but now states something index does not: the ~30 second
   total cycle time, previously buried in this page's own HowTo JSON-LD
   and never stated in the visible copy. The three FAQ entries collapsed
   into one ("Why does Sous use two speeds?"), absorbing the one genuinely
   useful fact from the other two (finish quality depends on tea/dose/
   water) before deleting them — **both from the visible `<details>` list
   and the FAQPage JSON-LD**, which must stay in exact parity: run
   `grep -c '<summary>' faq.html` against the JSON-LD question count before
   shipping any FAQ edit. (The Prop 65 question is the one deliberate
   exception — 12 visible, 11 in JSON-LD, by design; see that section.)
3. **Consistency, stated twice on `about.html`.** The Origin story and the
   Consistency value card both argued the same point: results hold up under
   time pressure / at service volume. Kept the Origin story (it is the
   founding narrative, the highest-value telling of it) and rewrote the
   Consistency card down to a single line — *"The same cup, every time."*
   — deliberately shorter than what it replaced, on the founder's direction
   to cut rather than pad once a section stops adding anything new.
   **The Restraint card was retargeted rather than left stating the same
   thing as item 1.** Its old copy ("No app, no subscription, no opinion
   about your tea") was flagged by the founder as answering a question
   nobody asked — nobody assumes a matcha mixer needs an app, so denying it
   isn't restraint, it's a non-answer. Renamed the card **Restraint →
   Finish** and gave it real content the page states nowhere else: *"Smooth
   microfoam, mixed evenly, every single time."* The heading changed
   because the content changed — a card's name has to match what it now
   says, not what it used to.
4. **The Journal blurb, copy-pasted verbatim across two pages.** *"Tea,
   water, temperature, cultivar, milk, ratios, tools and the details that
   separate matcha from matcha properly prepared"* appeared word-for-word
   in both `about.html`'s Journal teaser and `journal/index.html`'s own
   hero. Kept the Journal page's own hero unchanged (it is the canonical
   home for its own tagline) and rewrote the `about.html` teaser to
   something shorter that still does the teaser's actual job — sending a
   reader from About to Journal — without repeating the destination's own
   headline: *"What we've learned about tea, water and technique, written
   up as we go."*

**What this pass did not touch, on purpose**: the brand line ("Behind every
great matcha is a Sous") recurring in hero/footer/CTA bands, the Prop 65
warning appearing in multiple buy boxes, and price/shipping/warranty near
every buy button. All three are expected repetition — a tagline, a legal
requirement, and standard commerce practice — not the kind this pass was
looking for.

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

## Starting recipes photos (how-to-use.html)

Three files, one shared 1:1 crop convention, three different origins:

- `recipe-straight-v2.webp` — center-square crop of `tile-matcha-v5.webp`,
  the GrabCut cutout hero shot from the earlier photography pass (see
  "Cutting the matcha silhouette" above). Founder-supplied, sourced via
  Google Drive early in the project. **v2, not v1** — an earlier pass
  mapped this file backwards (see below) and fixed it by overwriting
  `recipe-straight-v1.webp` *in place*, which is exactly the caching bug
  this project's own "Image caching" section warns about: same filename,
  new bytes, and a browser or GitHub's CDN can keep serving the stale ones
  indefinitely. The filename is versioned now specifically so that mistake
  can't repeat silently — **always bump the version suffix when a file's
  content changes, never overwrite in place**, even for a same-session fix.
- `recipe-hot-v1.webp` — founder's own photo, emailed directly (mug shot,
  steaming, on a wood table). **Do not confuse this with "straight" by
  filename** — an earlier pass mapped these two backwards (the mug photo
  was briefly `recipe-straight-v1.webp`) before the founder caught it. The
  fix was a rename, not a re-crop; the crop itself was already correct.
  This file's own name never changed, so it carried no cache risk.
- `recipe-iced-v1.webp` — Unsplash, "a green drink with ice cubes in it" by
  Daniel Stiel. Free commercial license, no attribution required, confirmed
  against unsplash.com/license before use.

**Why the founder's own emailed photos needed a detour through Gmail's raw
MIME rather than a normal file save**: in this session, an image pasted
directly into chat never landed on any filesystem path the agent could
read, and Google Drive access hit a permission wall that repeated retries
didn't clear. Gmail was already connected with no auth prompt, but its
`get_message`/`get_thread` tools return only attachment *metadata*
(filename, id, mime type), not bytes — there was no exposed
"download attachment" call. `messageFormat: RAW` was the way through: it
returns the full RFC822 MIME message as one base64 blob, which Python's
`email` stdlib parses directly, handing back each attachment's real bytes
to write to disk. If a future session hits the same "user sent a photo but
there's no file for it" wall, this is the path: have them email it to an
already-connected inbox, fetch RAW, parse with `email.message_from_bytes`.

**Why 1:1 square, specifically**: a 4:5 portrait crop was tried first and
rejected — on the mug photo it cropped away the rim entirely and read as an
abstract green blur with no cup visible. Tested side by side against a
square crop before deciding. Square keeps all three source photos legible
despite wildly different native shapes (a tight landscape mug shot, a tall
portrait glass shot, a near-square cutout). If a fourth recipe or a reshoot
ever changes these files, keep the 1:1 convention rather than sizing each
photo to its own best crop — the point is that the three read as one set.

## California Proposition 65

**This is the one part of the site that is legally operative. Do not edit it
for tone, length or rhythm.** The wording is the safe-harbor text from
27 CCR 25603(a)(2); departing from it forfeits the safe harbor.

**As of August 2026, this warning no longer appears anywhere on `index.html`.**
Both the buy-box link and the footer's full-text block were removed per
founder direction, together rather than one at a time - the link only stays
compliant as long as it points at the full text somewhere, so deleting either
half without the other would have left a dead link or an unreferenced
warning, neither of which is a valid state. `stockists.html` was
deliberately left untouched and still carries the complete, compliant pair
described below. The two pages are no longer symmetrical on this. That's a
real asymmetry, not an oversight - revisit only if asked to make the same
change on `stockists.html`.

**Where it is now — split across two places on purpose, not one, on the one
page that still carries it.** A short link reading **"WARNING: California
Prop 65"** sits in `.buybox` on `stockists.html`, right beside the button.
The full paragraph lives once, at the very bottom of that page, inside
`<footer>` as `#prop65` (and inside the Shopify `sections/footer.liquid`,
which renders on every page in the Shopify theme - that theme was not
touched by the `index.html` removal above, so it still carries both halves
everywhere it renders).

This split is a founder request, and it is compliant **only because of how
it's built** — do not "simplify" it back into one block without re-reading
this section. 27 CCR 25602(b) treats the internet warning as **a distinct
requirement from the one on the physical product** (27 CCR 25602(a)); one does
not satisfy the other. A plain relocation of the full text to the footer with
nothing near the buy button would fail the regulation's own test, which says a
warning is **not** "prominently displayed" if the purchaser has to search for
it in the general content of the page. What makes the footer placement legal
is that the regulation names a second safe harbor, **method (2): a link on the
product display page, clearly marked with the word WARNING, that leads to the
full text.** That is exactly what the buy-box link is. Delete the link while
keeping only the footer text, and the site is out of compliance again — the
footer paragraph existing somewhere on the domain is not enough; the *link*
next to the purchase decision is the part doing the legal work.

`p65_chemical` / `p65_harm` now exist as **two setting pairs** — on
`sections/buy-box.liquid` (which renders the link) and on
`sections/footer.liquid` (which renders the destination) — and they **must be
kept identical**, because the link promises a specific warning and the footer
has to deliver the one promised. Blanking one without the other either points
the link at nothing or shows a warning nobody referenced.

`faq.html` carries a Q&A that *explains* the warning; that answer is not a
substitute for either half of it and must never become one. It is
deliberately kept out of the FAQPage JSON-LD — an FAQ rich result reading
"why is there a cancer warning" is not something to invite into a search
listing.

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
   three remaining places at once**: `stockists.html`, the Shopify setting,
   and the FAQ answer's sentence about which part the chemical comes from.
   (`index.html` no longer carries this warning - see the callout above.)
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

## Warranty page

`warranty.html` is a legal disclosure, built to satisfy the Magnuson-Moss
Warranty Act (15 U.S.C. §2301) requirement that any written consumer
warranty on a product over $15 be labelled **FULL** or **LIMITED** and
disclose its terms "in simple and readily understood language." It is
labelled **Limited** throughout, on purpose — repair/replace/refund at
the warrantor's discretion doesn't meet the Act's stricter definition of a
Full warranty, which requires a no-cost remedy with no conditions attached.

**Its substantive clauses are copied verbatim from the real Matcha Sous
User Guide** ("10. Sous Support" / "One-Year Limited Warranty"), supplied
by the founder as a PDF - see "Sourced from the real user guide" and
"Superseded again: the final print booklet" below for the full account of
what that replaced and why, twice. Every `.prose` paragraph in the
warranty sections of this page should trace back to that document; if the
guide is ever revised, this page needs the same revision, not an
independent edit.

**It's disclosed purely online, which is deliberate and compliant.** The
FTC's Pre-Sale Availability Rule (16 CFR 702) and the E-Warranty Act of 2015
allow a warranty to be posted online-only, as long as a non-internet way to
*get* the terms is also offered. That's what the "request a free copy of
this warranty" line near the bottom is for — remove it and the page stops
covering that requirement.

**Linked from every place a purchase decision or a warranty question
happens**: two separate links in `index.html`'s own buy box now (the "Includes
a One-Year Limited Warranty..." line directly under the price, and the
original `.assure` trust-badge line lower down), `stockists.html`'s `.assure`
line, the FAQ's shipping/warranty answer, and the footer nav — labelled
"Limited Warranty" there, not just "Warranty" — on every page. All of these
should keep pointing at `warranty.html` rather than restating its terms in
their own words.

### Sourced from the real user guide, not an approximation of one

Earlier passes on this page (formal-register rewrite, Magnuson-Moss
compliance framing) were written without access to the actual product
documentation - the best available approximation at the time, built from
general small-appliance warranty conventions and the facts already
established elsewhere on the site. The founder then supplied the real
`Matcha Sous User Guide` PDF, and its page 11 fully replaced that
approximation. Two things are worth recording about that swap:

**Clauses that existed only in the approximation, and are gone now**:
a liability cap tied to the price paid ("will not exceed the price you
paid for a comparable replacement"), "sole and exclusive remedy" framing,
and an Acts-of-God / fire-or-flood exclusion. None of these appear in the
real warranty. They were reasonable things for a warranty like this to
say, but saying them without them actually being in the governing document
would have been the site making a promise (or a limitation) that isn't
real. The real document's own "Limitations" section is narrower: implied-
warranty duration, incidental/consequential damages, and the standard
"varies by State" line - nothing about a liability cap.

**Facts that are new to this project, not just to this page**:
- **Presso Inc.** is named as the warrantor - the first place any legal
  entity name has appeared anywhere on this site. `index.html`'s Product
  JSON-LD, the footer copyright line, `terms-of-sale.html` and
  `privacy-policy.html` all currently speak generically ("we," "Matcha
  Sous," no named company) rather than naming this entity. Whether that
  should change sitewide is a real decision, not a copywriting one - flag
  it to the founder rather than propagating it unprompted.
- **Model number LHMC0110** doesn't appear anywhere else on the site
  (buybox specs, `about.html`, `how-to-use.html`).
- **A spare mixing whisk ships with every unit**, stored in a holder built
  into the underside of the base ("Storage," page 8: "A spare mixing whisk
  is stored in the holder on the underside of the base"). This is real
  news, not just missing copy: it's evidence toward resolving
  `1b-BOX-CONFLICT` above in favor of the part being genuinely included
  (a spare wouldn't ship if the part itself didn't), and it's a concrete,
  differentiating fact - most comparable mixers don't include a
  backup part - that currently appears nowhere on the site at all.
- **A real mailing address** - 1733 Monrovia Ave., Suite Y, Costa Mesa, CA
  92627 - given under "Contact" in the guide as somewhere warranty
  correspondence can be mailed, not just emailed. This is the first
  physical address anywhere on the site. It's also the first concrete
  data point relevant to the still-open "governing-law / venue state"
  question below, though a support address alone doesn't establish where
  the company is legally organized - don't write a governing-law clause
  from this address without the founder confirming it.

**A naming conflict surfaced by the real source - and it's a third data
point on an already-open question, not a new one.** The guide consistently
calls the removable part inside the cup the **"mixing whisk,"** including
in the warranty's own exclusions clause ("loss of the removable mixing
whisk or charging cable"), reproduced verbatim on this page. Every other
page on this site - `index.html`, `about.html`, `how-to-use.html`,
`faq.html`, journal articles, the Shopify theme - calls the same part the
**"mixing rod."** That wasn't an arbitrary copywriting choice: see
`1b-BOX-CONFLICT` and `1b-BOX` above, where the site was built to match a
founder-supplied *packaging insert card* that names the part "mixing rod"
- while a photo of the actual box back panel (`launch-guide.jpg`) omits
the part entirely from its contents list, a conflict already flagged there
as unresolved. This User Guide is a third, independent source, and it says
"mixing whisk." Of the three, the User Guide is the most complete and
formal (an 18-page manual, not a box panel or insert card), which is some
evidence it's the final, correct term - but that's a reasonable guess, not
a confirmed fact. This page now uses "mixing whisk" in the one paragraph
where the wording is verbatim, which is inconsistent with "mixing rod"
everywhere else on the site. **Resolved by the founder: renamed "mixing
rod" to "mixing whisk" sitewide**, to match the User Guide. Changed in
`about.html`, `faq.html` (both the JSON-LD and visible answer), `index.html`
(the etched-guides photo alt text and the buybox's "What's included" line),
and both journal articles that mention the part
(`matcha-without-a-whisk.html`, `how-to-choose-matcha.html`) - seven
occurrences across five pages, verified as zero remaining afterward.
`warranty.html` already said "mixing whisk" from the verbatim source text,
so it needed no change. This also settles `1b-BOX-CONFLICT`'s naming half
in the User Guide's favor; the box-contents half (whether the part ships
at all) is separately supported by the spare-whisk fact two paragraphs up.

The full source PDF is also saved at
`assets/docs/matcha-sous-user-guide.pdf`, unlinked from anywhere on the
site for now - it wasn't asked for as a public download, only as the
source for this page's own text.

### Superseded again: the final print booklet

The founder then supplied a second document - `V1_Matcha_Sous_Booklet_
Print_11x8.25.pdf`, the final print-ready guide, 10 pages in reader-spread
imposition (two half-letter pages per PDF page, hence the 11x8.25" trim -
not a 61-page document; that figure in the upload notice was wrong, and
was double-checked against the PDF's actual page-object count before
trusting the 10-page reading). It replaced the first PDF as source of
record at `assets/docs/matcha-sous-user-guide.pdf` (same filename,
overwritten - the old one wasn't kept, since the founder called this one
"the final manual"). Diffing the two revealed the earlier PDF wasn't
final either, so warranty.html changed a second time, verbatim again
against the new source (every `.prose` paragraph checked programmatically,
same discipline as the first pass):

- **The warranty clock now starts at purchase, not delivery** - "one year
  from the date of purchase" replaces "one year from the date the product
  is delivered," in both the main coverage sentence and the implied-
  warranty limitation. This has a real ripple effect on a preorder site:
  payment is collected at reservation, well before the unit ships, so the
  covered year may now start weeks or months before a customer ever
  receives their Sous. Nothing on this site currently discloses that gap
  explicitly - worth the founder's attention, not just a copywriting fix.
  Fixed everywhere the site echoed "delivery" as the warranty's start:
  `index.html`'s buybox notice ("beginning on delivery" -> "beginning on
  purchase") and `terms-of-sale.html`'s Returns section ("within a year of
  delivery" -> "within a year of purchase").
- **A new sentence**: "A current list of authorized sellers is available
  at matchasous.com." No such list exists on the site yet - `stockists.html`
  lists physical retail locations, not an explicit "authorized online
  sellers" list. Flagged, not built; that's a business decision (which
  resellers are actually authorized) this project has no visibility into.
- **A new clause**: parts bought separately (extra mixing whisks, charging
  cables) carry their own 90-day warranty. The site doesn't currently sell
  spare parts anywhere, so this has no home yet - worth remembering if/when
  it does.
- **"Beverage syrup" is now defined**: "a clear, pourable, dairy-free
  flavoring syrup," reproduced verbatim in the exclusions paragraph.
- **A personal-injury carve-out was added** to the damages-limitation
  paragraph: "Nothing in this warranty limits liability for personal
  injury to the extent such limitation is prohibited by applicable law."
  Legally prudent boilerplate, reproduced as-is.
- **Minor cleanup**: the charging-cable paragraph dropped a redundant
  "Loss," (already covered by the main exclusions sentence), and "from the
  date it is returned or delivered to you" simplified to "from the date
  you receive it" for the replacement-product coverage window. Neither
  changes the actual terms.
- **"Made in China" is gone from the Contact section**, along with the
  separate "Product identification" field the first PDF had. The model
  number now lives in the main warranty sentence instead of a separate
  field, so the standalone "Product: Matcha Sous, model LHMC0110. Made in
  China." line this page used to synthesize was removed rather than kept
  unsupported by the current source. This doesn't mean "Made in China" is
  now false - just that it isn't in the document this page is required to
  match verbatim, so it isn't asserted here anymore either.

**Also found while cross-referencing, fixed as directly motivated by the
new source rather than scope creep:**
- **Recipe measurements on `how-to-use.html` didn't match the guide's own
  Starting Recipes.** Matcha, straight: 80 ml water corrected to 70 ml.
  Both lattes: 4 g matcha corrected to 3 g. Three spec lines fixed;
  verified no other page states Sous-specific recipe amounts that needed
  the same fix (`usucha-vs-koicha.html`'s numbers are general tea-ceremony
  ratios, unrelated to Sous, and correctly left alone).
- **A real internal contradiction in `how-to-use.html`'s HowTo JSON-LD**:
  the "Build" step (add milk or ice) was listed *before* the "Sweeten and
  finish" step, which itself said to stir in sweetener "before adding milk
  or ice" - backwards from its own instruction. Restructured into three
  steps (Pour / Sweeten / Finish) in the order that actually makes sense,
  and made explicit that sweetening happens after pouring the concentrate
  out of the mixing cup - the guide's safety instructions explicitly
  prohibit putting honey, milk, ice, or anything but matcha, water and
  beverage syrup into the appliance itself, and the old wording didn't
  make clear where the "stir honey into the warm concentrate" step was
  meant to happen.
- **A new Troubleshooting section**, adapted from the guide's own
  troubleshooting table (symptom / likely cause / what to do) into this
  site's existing question-and-answer voice. Placed on `faq.html`, not
  `how-to-use.html` as first planned - FAQ is already the site's support
  hub with a working `.qa` accordion component built for exactly this,
  and troubleshooting fits "when something's wrong" better than
  "how it works." Added to the FAQPage JSON-LD too, unlike the Prop 65
  answer on the same page: there's no reason to keep this out of search
  results the way there is for a warning-label explanation.
- **A new Specifications section on `how-to-use.html`**: model LHMC0110,
  4 W rated power, DC 5 V/1 A charging input, 40-120 ml working capacity,
  175°F/79°C max water temperature - none of which existed anywhere on
  the site before. Uses `.plate`, a component that was already fully
  styled in this file's own stylesheet and already used for this exact
  purpose in the Shopify theme's `spec-plate.liquid`, just never
  instantiated on the static site until now. Deliberately kept to the
  five figures the guide's own Specifications section states, not the
  fuller battery-chemistry/weight/IP-rating list the *first* PDF's
  Specifications page had - this final booklet's own spec table is
  shorter, and this page now matches what it actually says rather than
  the superseded, longer list.
- **The Shopify theme's own spec plate had the wrong power figure**:
  "6 W low power" in both `spec-plate.liquid`'s preset and the live
  `templates/index.json` override, corrected to "4 W rated power" in both
  to match the real spec.

### Still open regardless of the new source

1. **No governing-law / venue state is named.** The "Limitations" section
   (verbatim from the guide) covers implied-warranty limits and the
   damages exclusion but never says which state's law governs a dispute -
   the real source document doesn't answer this either. That's a founder
   decision (typically wherever the company is incorporated), not a
   copywriting one.
2. **Commercial and hospitality units carry the same one-year term as
   consumer units.** `about.html` and `wholesale.html` both actively market
   Sous for café and hotel use, where duty cycles run far heavier than a
   home kitchen. The real warranty doesn't distinguish commercial use
   either. Left alone until the founder decides whether wholesale accounts
   need their own clause, here or in `wholesale.html`'s enquiry terms.

*Not legal advice. Have a products lawyer read this page before the first
unit ships, same as the Prop 65 section above.*

### Pre-purchase disclosure pass

A founder request asked for the warranty to be surfaced before purchase in
several specific places, matching how the FTC's Pre-Sale Availability Rule
(16 CFR 702) is usually implemented in practice: visible near the price,
repeated at checkout, printable, downloadable, and not buried in an FAQ or
gated behind an account.

**Done:**
- A new line directly under the price in `index.html`'s buy box: "Includes
  a One-Year Limited Warranty beginning on delivery," linking straight to
  this page.
- Footer link relabelled "Limited Warranty" (was "Warranty") on all 14
  pages, for the more precise legal term.
- A "Print this page" button and a real "Download PDF" link, both new,
  directly below this page's own hero. The PDF
  (`assets/docs/matcha-sous-limited-warranty.pdf`) is generated straight
  from this page's own HTML via a new print stylesheet (`@media print` in
  site.css, hides the header, footer, nav and video) run through
  Playwright's `page.pdf()` - screen, print and PDF are one source
  rendered three ways, not three documents that can quietly drift apart.
  Regenerate it the same way after any future change to this page's
  content.
- The closing "want a printed copy" line reworded to the founder's exact
  requested phrasing: "To request a free copy of this warranty, email
  care@matchasous.com."

**"Exactly as written on page 11 of the current user guide" - resolved in
a follow-up pass.** At the time this page was first built, no such
document was available - see "Sourced from the real user guide" above for
the full account. The founder subsequently supplied the actual PDF, and
this page's substantive clauses were replaced with that verbatim text.

**Not done, and can't be from here:**
- **"Repeat the warranty link during checkout before payment is
  submitted."** There is no checkout to repeat it in. `/site` is a static
  site with no backend - see "Payment timing" above, a pre-existing,
  already-documented gap, not something new. On the Shopify side, the
  theme's product form already routes straight to Shopify's own hosted
  checkout (see `main-product.liquid` / `buy-box.liquid`), but that hosted
  checkout page itself isn't part of this theme's files - it's Shopify's
  own system, configured in Shopify admin, not something a theme file can
  add a warranty link to.

## Privacy Policy

`privacy-policy.html` follows the same rule as the warranty page: match the
requested format, but don't state anything about this business that isn't
actually true. Two places where that mattered:

**Cookies.** The page says plainly that the site runs no analytics,
advertising or tracking scripts today, because that's a fact you can verify
with one grep (`rg -i "gtag|analytics|pixel|dataLayer|klaviyo|hotjar" site/`
turns up nothing). A generic privacy-policy template usually assumes a
cookie-consent banner exists; this site doesn't have one, so the page
doesn't claim one. It describes the *future* state instead — the checkout
cart cookies that will exist once Shopify checkout is live — clearly framed
as forward-looking, not as something happening today.

**Shopify.** Unlike the cookie section, this part isn't a stretch:
`shopify-theme/` is a real, maintained parallel deploy target for this
brand (see `shopify-theme/SHOPIFY-SETUP.md`), so the "runs on Shopify" and
PCI-DSS payment-processing language is accurate as a statement of what the
business runs on, not aspirational copy. What *is* still forward-looking is
payment processing itself — per the Launch checklist above, the buy button
is currently a `mailto:` reservation, not a live Shopify order, so nothing
is actually being charged or processed yet. The policy is written to be
correct on the day checkout switches on, not only in some hypothetical
future rewrite.

**No legal entity name is asserted anywhere on this page**, same as
`warranty.html` — it says "Matcha Sous" throughout because no registered
company name exists yet anywhere in this repo to state accurately. If one
gets registered, this is one of the places that should name it.

Effective date is set to the date this page was written (**August 26,
2026**); update it any time the policy's substance changes, not on every
unrelated site edit.

Linked from the footer nav on every page, same placement as Warranty
(footer only, not the primary nav, to keep the primary nav to six items).

*Not legal advice. Have a products lawyer read this page before the first
unit ships.*

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
- **The spiral is generated, not drawn: `site/tools/swirl.py`.** Run it to
  reprint the exact path that ships. It went through two failed cuts first, and
  both failures were the same root cause, so they are worth knowing:
  1. Scaling `assets/images/logo-enso.svg` 64→48 produced a **uniform hairline
     built from perfect circular arcs**, which reads as concentric rings.
  2. Restoring the enso's terminal curl and centre dot helped but did not fix
     it, because the actual problem is that **SVG cannot vary stroke-width
     along a path.** An enso reads as brushed because the stroke tapers.

  So the mark is a **filled ribbon**, not a stroke: a logarithmic spiral
  centreline sampled `n` times, offset perpendicular by ±w(t)/2, with width
  running from `w_max` at the head to zero at the tail. The tail comes to a
  real point the way a lifted brush does, so no centre dot is needed, and the
  head gets a true semicircular cap (**sweep-flag 0** — flag 1 bites a concave
  notch out of it, which is what the first attempt did).

  `w_max=3.0` is not arbitrary: a ribbon tapering 3.0→0 averages ≈1.4, which is
  exactly the `stroke-width` of the three sibling icons, so the spiral reads as
  brushed without out-weighting the row. Above ~3.4 it dominates. `n=80` is the
  smallest sampling that stays smooth at 5× display size.

  It is `fill="currentColor"` with **no stroke**, unlike its three siblings.
  Its `translate(-4.25 -3.4)` was measured with `getBBox()`, not eyeballed —
  **re-measure if any generator parameter changes.**
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
- JSON-LD: Organization, WebSite, Product+Offer ($179), BreadcrumbList, FAQPage
