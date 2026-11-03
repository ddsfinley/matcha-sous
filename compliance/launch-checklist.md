# Matcha Sous launch checklist

Run November 3, 2026, against the static site (`/site`) and the Shopify theme
(`/shopify-theme`). No Shopify store exists at the moment, so anything that
needs a live store is marked for re-testing once one is set up.

This is a technical record, not legal advice. Items marked **Lawyer** need a
qualified attorney's sign-off.

**Status key:** **Pass** · **Fixed** (was a problem, fixed today) ·
**You** (a business decision or account setting only the owner can do) ·
**Store** (test again on the live Shopify store) · **Lawyer**

---

## 1. Accessibility

| Item | Status | Evidence / notes |
|---|---|---|
| Keyboard-only use of menus, buttons, links | **Pass** | All 15 pages tabbed through in Chromium: every control reachable and usable with Tab, Enter and Space; skip link works on every page. Product selection and checkout: **Store** (Shopify-hosted). |
| Focus visible, never trapped | **Pass / Fixed** | No traps; every focused element shows a 2px copper outline; nothing hidden behind the sticky header (WCAG 2.2, 2.4.11). Form fields had a weak focus style, fixed. No pop-ups exist. |
| Alt text on images, logos, graphics | **Pass** | Every image has a description; logos inside labeled links use empty alt correctly; decorative icons hidden from screen readers. **You:** add alt text to each product photo in Shopify. |
| Contrast (4.5:1 text) | **Pass / Fixed** | axe-core: 0 contrast failures. Struck-through $159 was 3.2:1, fixed to 6.4:1. |
| Heading order, form labels | **Pass / Fixed** | One heading per page at top level; wholesale page jumped h1 to h3, fixed. All form fields labeled. Shopify product page had no h1, fixed in theme. |
| 200% zoom, mobile reflow | **Pass** | No horizontal scrolling on any page at 320px wide or 1280px at 200% zoom. |
| Screen readers announce products, prices, buttons | **Pass (automated) / You** | Accessibility tree checked for the buy box: price reads "Preorder price $149, Regular price $159"; every button and link has a clear name. Still needed: a real screen-reader pass (VoiceOver), including checkout errors (**Store**). |
| Variants, quantity, cart, discount codes, payment | **Store** | Theme variant select and cart quantity fields are labeled. Discount codes and payment forms are Shopify checkout; test on the live store. |
| Video captions, pausable animation | **Pass** | Both videos have no audio track, so captions are not required; each has a text description and a pause button; no autoplay when the device asks for reduced motion. |
| Contact method and accessibility statement | **Fixed** | New `accessibility.html`, linked in every footer; contact care@matchasous.com. **You:** paste `shopify-pages/accessibility.html` into a Shopify page and add it to the Footer menu. |
| Widgets, pop-ups, chat, third-party apps | **Pass** | None installed (network check: zero outside requests). Re-check every Shopify app before adding it. |
| Automated scan + manual review recorded | **Pass / You** | axe-core 4.14: 0 violations on 15 pages (WCAG 2.0, 2.1, 2.2 A/AA). accessiBe accessScan: passed (owner). Keyboard review: passed. Screen-reader review: not yet done. |

## 2. Privacy and customer data

| Item | Status | Evidence / notes |
|---|---|---|
| Privacy policy (collection, purposes, sharing, retention, contact) | **Fixed** | Updated November 3: retention, no selling or sharing for targeted ads, "Your choices" section, Global Privacy Control. Shopify version in `shopify-pages/privacy-policy.html`. **Lawyer:** review before launch. |
| Identify analytics, pixels, cookies, email software, processors | **Pass** | Static site: 0 outside requests, 0 cookies, 0 browser storage across all pages. Processors named in the policy: Shopify, payment processor, carrier. **Store:** re-run the network check on the live store. |
| Does CCPA/CPRA apply? | **Lawyer** | Applies to for-profit businesses over about $26.6M revenue, or that buy, sell or share data of 100,000+ California consumers, or earn half their revenue from selling or sharing data. Likely not yet, but confirm. California's wiretap law (CIPA), the basis of most current suits, has no size threshold. |
| Opt-out mechanisms, notices, preference controls | **You** | Nothing is sold or shared today. On Shopify: turn on Settings → Customer privacy → cookie banner and the "Your privacy choices" page. |
| Honor Global Privacy Control | **Pass** | Policy commits to it; nothing on the site to opt out of today. On Shopify, confirm the cookie banner setting respects it. |
| Email and SMS consent and unsubscribe | **You** | None set up. Email: CAN-SPAM requires an unsubscribe link and a physical mailing address in every marketing email. SMS needs prior express written consent (TCPA); it is a heavily litigated area. **Lawyer** before starting SMS. |
| Customer data protected, access restricted, old data deleted | **You / Store** | No customer data is stored on the static site (wholesale form opens the visitor's email app). On Shopify: limit staff accounts, use two-factor sign-in, follow the retention promise in the policy. |
| Notices for each state or country targeted | **Pass / Lawyer** | US-only shipping. Most state privacy laws have size thresholds; confirm with counsel if selling outside the US. |

## 3. Business, policies and checkout

| Item | Status | Evidence / notes |
|---|---|---|
| Legal business identity and support contact | **You** | Support email is on every page. The legal entity (Presso Inc., Costa Mesa) appears only on the warranty page. Recommend a line such as "Matcha Sous is a brand of Presso Inc." in the footer and terms of sale. |
| Shipping and delivery policy | **You (high priority)** | Free US shipping is stated, but no ship date anywhere while payment is collected at reservation. The FTC Mail, Internet, or Telephone Order Merchandise Rule requires shipping within 30 days when no time is stated, or sending a delay notice that offers cancellation and a full refund. State a shipping window as soon as it's known (a commented-out line is ready in `index.html`). **Lawyer.** |
| Return, refund, exchange, cancellation policy | **Pass / You** | Terms of sale: cancel before shipping for a full refund; no change-of-mind returns after shipping; defects covered by warranty. Recommend stating "no returns after shipping" next to the buy button too, not only in the terms. |
| Terms of sale and website terms | **Pass / You** | Terms of sale published. No separate website terms of use (optional). Governing law and venue left unnamed in warranty and terms. **Lawyer.** |
| Full price, shipping, fees, taxes before purchase | **Pass / Store** | $149 preorder, $159 regular, free shipping, "prices don't include sales tax" in terms. Shopify checkout shows tax; confirm on the live store. |
| Payment confirmation and receipts | **Store** | |
| Sales tax and economic nexus | **You** | Shopify Tax can calculate; register in states where you pass thresholds (California at minimum). Accountant. |
| Claims, promotions, testimonials, photos accurate | **You** | No testimonials or discount codes on the site. Check: "$159 regular price" must reflect a genuine planned selling price; the site's structured data lists Instagram, TikTok and YouTube accounts (@matchasous), so confirm they exist or remove them; confirm photos show the actual product. |
| Subscriptions and auto-renewal | **Pass** | None offered. |
| Gift cards and store credit | **Store** | Shopify gift cards don't expire by default; keep it that way (California generally bans expiration dates and fees). |

## 4. Product compliance

Matcha Sous is an appliance, not a food, so most food-labeling rules don't
apply unless matcha itself is sold. Appliance rules apply instead.

| Item | Status | Evidence / notes |
|---|---|---|
| Names, sizes, variants, descriptions | **Pass** | Model LHMC0110, 4 W, 5V/1A USB-C, 40–120 ml, specs match the final user guide. |
| Food labeling, allergens, nutrition, health claims | **N/A** | Not selling food. Becomes relevant if matcha is sold; the site makes no organic, health, antioxidant or caffeine claims. |
| Prop 65 | **You / Lawyer** | Warning removed from the static homepage (owner's decision); still shown in the Shopify buy box and on stockists. Chemical (DEHP) is a placeholder pending a supplier test report. Decide with counsel based on that report. |
| Food-contact materials, electrical safety, battery shipping | **You** | Get from the manufacturer: food-contact compliance for the cup, whisk and sleeve; FCC and safety certification; UN38.3 test summary for the battery (carriers require it). |
| Rights to photos, logos, fonts | **Pass / You** | Fonts (Poiret One, Jost, Cormorant Garamond) are free open-license. Confirm you own or licensed all photography. |

## 5. Security and launch quality

| Item | Status | Evidence / notes |
|---|---|---|
| HTTPS everywhere | **Store** | GitHub Pages and Shopify both serve HTTPS. Confirm the certificate once the domain is reconnected. |
| Two-factor sign-in on admin accounts | **You** | Shopify, GitHub (ddsfinley), GoDaddy (domain hijacking risk), email. |
| Trusted payment processor, no stored card numbers | **Pass** | Shopify checkout; the site never handles card data. |
| Demo content, broken links, placeholders, unused plugins | **Fixed** | 0 broken links. The deploy was publishing internal files (README with business and legal notes, old design drafts, scripts) and internal HTML comments; now excluded. Remaining placeholders: no stockists yet (page hidden from search), Prop 65 chemical, ship window. |
| Test purchase and refund on desktop, iPhone, Android | **Store** | |
| Emails, tax, shipping rates, abandoned cart, inventory | **Store** | |
| Accessibility tests, fixes, issues, owners documented | **Pass** | This file. |
| Post-launch reviews | **You** | Re-run the accessibility scan and network check after any theme, app or checkout change; review this list quarterly. |

---

## Open items by owner

**Owner (Andrew)**
1. Ship window: decide and publish, or plan FTC delay notices (high priority).
2. Show the legal entity (Presso Inc.) in the footer and terms.
3. Prop 65 decision once the supplier test report arrives.
4. Manufacturer documents: food-contact, FCC/safety, battery UN38.3.
5. Confirm photo rights and the social accounts listed on the site.
6. Two-factor sign-in on Shopify, GitHub, GoDaddy, email.
7. Real screen-reader pass (VoiceOver).

**Attorney**
Privacy policy, CCPA applicability, terms (governing law), shipping-delay
handling, Prop 65, SMS consent if used.

**When the Shopify store is rebuilt**
Checkout keyboard and screen-reader test, alt text on product photos, cookie
banner, accessibility and privacy pages, network check for trackers, test
purchase and refund on three devices, receipts, tax, HTTPS.
