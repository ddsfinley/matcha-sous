# Matcha Sous — Shopify setup guide

This folder is a **custom Shopify theme** built from your site. Shopify runs the
real cart, checkout and payments; this theme provides the look + product/cart pages.

A ready‑to‑upload **`matcha-sous-shopify-theme.zip`** sits in the repo root.

> ⚠️ This is **v1** — because Shopify can't be tested from the build environment,
> expect a round or two of fixes once it's on your store.

## 1. Start your store
Create a Shopify account / free trial at shopify.com. Pick any starter plan
(you can connect the domain on a paid plan).

## 2. Add the product (handle matters!)
**Products → Add product**
- Title: **Matcha Sous**
- Description: paste from the current site's product page (or your own)
- Media: upload your photos (box, device, controls, packaging)
- Pricing: **Price 148.50**, **Compare‑at price 165.00**
- Leave it a **single variant** (one color) — don't add options
- **Search engine listing → Edit → URL handle = `matcha-sous`** ← the theme links to `/products/matcha-sous`
- Set inventory + shipping as you like, then **Save**

## 3. Create the content pages (set each handle)
**Online Store → Pages → Add page** — create these and set the URL handle exactly:

| Page title | Handle |
|---|---|
| How it works | `how-it-works` |
| Our story | `about` |
| FAQ | `faq` |
| Contact | `contact` |
| Shipping & Returns | `shipping-returns` |

Paste content from the current live site. (In v1 these show as styled rich‑text;
the homepage + product page are fully designed. I can port the fancy page layouts
to custom templates next.)

**Policies:** Settings → Policies → fill in **Privacy policy** and **Terms of service**
(Shopify auto‑creates the `/policies/...` URLs the footer links to).

## 4. Upload the theme
**Online Store → Themes → Add theme → Upload zip file** → choose
`matcha-sous-shopify-theme.zip` → **Preview** it. When it looks right, **Publish**.
*(The zip already has `layout/`, `templates/`, `assets/`… at its root, which is what Shopify expects.)*

## 5. Connect Matchasous.com (your GoDaddy domain)
**Settings → Domains → Connect existing domain →** enter `matchasous.com`.
Shopify shows the exact DNS to set in **GoDaddy → DNS**:
- **A record** `@` → `23.227.38.65`
- **CNAME** `www` → `shops.myshopify.com`
Then set `matchasous.com` as the **primary domain**. SSL is automatic.

## 6. Turn on payments + test
Settings → Payments (Shopify Payments or PayPal/Stripe) → then place a test order.

## Notes for whoever maintains the theme
- Buttons assume product handle **`matcha-sous`** and the page handles above. Change them in `layout/theme.liquid` + `templates/index.liquid` if you use different handles.
- Cart/checkout are native Shopify — no custom JS cart.
- Design system is `assets/styles.css`; UI behavior is `assets/theme.js`.
