# Matcha Sous — Shopify theme

An Online Store 2.0 theme carrying the current matchasous.com design: bone
ground, aubergine anchors, copper accents, Cormorant Garamond + Jost.

## Upload

1. Shopify admin → **Online Store → Themes → Add theme → Upload zip file**
2. Select `matcha-sous-shopify-theme.zip`
3. **Customize** to preview, then **Publish** when it looks right.

## First-run checklist

1. **Create the product** — Products → Add product → "Matcha Sous", price
   $199, upload the photography, set inventory. Then in the theme editor open
   the **Buy box** and **Hero** sections and select that product; the buy box
   switches to a real add-to-cart form and Shopify's checkout.
   Until a product is selected the buy box shows the fallback price and links
   to the catalogue, so the page never looks broken.
2. **Menus** — Navigation → create `main-menu` (Shop / How it works / Our story
   / Journal / FAQ / Wholesale) and `footer`. The header and footer sections
   read whichever menus you pick.
3. **Blog** — the Journal strip reads the blog handle set in that section
   (`news` by default). Create the blog and posts, or change the handle.
4. **Pages** — create "Our story", "FAQ" and "Wholesale" pages and point the
   menu at them; they render through `templates/page.json`.
5. **Announcement bar** — edit the text in the theme editor.

## Structure

- `layout/theme.liquid` — head, fonts (served from theme assets), the
  autoplay-rescue script, and the three global sections.
- `sections/` — every homepage block is an editable section with presets, so
  the whole page can be reordered in the theme editor without code.
- `templates/*.json` — which sections each template renders.
- `assets/base.css` — the site stylesheet, unchanged apart from the font
  declarations, which move to `theme.liquid` so they can use `asset_url`.
- `assets/` — photography, the looping video, wordmarks, favicon, fonts.

## Notes

- The `.mp4` loop autoplays muted and inline; the script in `theme.liquid`
  retries playback if a browser blocks the first attempt.
- Prices come from the product record, so changing the price in Shopify
  changes it everywhere on the page.
