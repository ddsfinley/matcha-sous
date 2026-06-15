# Product imagery — how to swap in your real photos

The storefront currently ships with **on-brand SVG illustrations** of the device so
the site looks complete out of the box. They're vector, so they stay crisp at any size.
When you're ready to use your **real product photography**, replace the files below.

## The 6 illustrations and what they represent

| File | Used on | Your matching real photo |
|------|---------|---------------------------|
| `product-device.svg` | Homepage hero, product main image, cart thumbnails, "in the box" | The steel pitcher on the black powered base (your 3/4 hero shot) |
| `product-cup-interior.svg` | Homepage showcase, product gallery, how-it-works | Top-down inside the pitcher — whisk + 40/80/120 ml marks (your photo #2) |
| `product-base.svg` | Homepage showcase, product gallery, how-it-works | Close-up of the base controls — 1 / 2 / 3, timer, start (your photo #5) |
| `product-box.svg` | Product gallery, about page | The olive gift box with the gold enso (your photo #1) |
| `product-kit.svg` | Product "in the box" | A flat-lay of everything included |
| `product-lifestyle.svg` | About page, contextual sections | The device styled in a kitchen / with a matcha bowl |
| `og-image.svg` | Social sharing preview (Open Graph) | A 1200×630 branded share card |

## Two ways to swap

**Option A — keep the filenames (easiest).**
Save your photo as the **same name** but `.jpg`/`.png`, then update the file
extension in the references. Find every reference quickly with:

```bash
grep -rl "product-device.svg" .   # repeat per image
```

**Option B — drop new files and point to them.**
Add e.g. `assets/images/photos/hero.jpg`, then replace the `src="..."` in the
HTML. Recommended dimensions:

- Product / gallery images: **800 × 1000** (4:5), JPG ~80% quality
- `og-image`: **1200 × 630** PNG/JPG (social scrapers don't reliably render SVG —
  exporting a PNG here is recommended before launch)

Keep the existing `alt` text (or improve it) — it's written for SEO and accessibility.

## Logo & favicon
- `logo-enso.svg` — the gold enso brand mark (header, footer, empty cart, 404)
- `favicon.svg` — the browser tab icon (enso on olive)
