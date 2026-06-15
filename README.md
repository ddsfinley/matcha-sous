# Matcha Sous™ — Storefront

A premium, SEO-optimized e-commerce storefront for **Matcha Sous**, *the first
hands-free matcha mixer* — "The Sous Chef for Matcha."

Built as a fast, dependency-free **static site** (HTML + CSS + vanilla JS) styled to
feel like a high-end Shopify store. Every page is real and every link resolves.

## Preview locally

No build step. Serve the folder with any static server:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

(Opening `index.html` directly via `file://` also works, though a server is
recommended so the cart, fonts and relative paths behave exactly as in production.)

## Pages

| Page | File | Notes |
|------|------|-------|
| Home | `index.html` | Hero, benefits, by-hand vs. Matcha Sous comparison, how-it-works, reviews |
| Product | `product.html` | Gallery, finish variants, qty, add-to-cart, specs, reviews |
| How it works | `how-it-works.html` | Method, the 3 speeds, recipes, care |
| Our story | `about.html` | Brand narrative & values |
| FAQ | `faq.html` | Accordion + FAQPage structured data |
| Contact | `contact.html` | Mock contact form + wholesale |
| Cart | `cart.html` | Live cart (localStorage) |
| Checkout | `checkout.html` | Demo checkout — **no real payment** |
| Order confirmation | `order-confirmation.html` | Order summary after checkout |
| Shipping & returns / Privacy / Terms | `shipping-returns.html`, `privacy.html`, `terms.html` | Policies |
| 404 | `404.html` | Friendly not-found |

## How it's wired

- **Design system:** `assets/css/styles.css` — one stylesheet, CSS custom properties
  for the palette (olive green + champagne gold, drawn from the packaging).
- **Cart:** `assets/js/cart.js` — a small `localStorage`-backed cart shared across
  pages (`window.MSCart`). Persists items, quantities and a mock placed order.
- **UI:** `assets/js/main.js` — header, mobile nav, scroll-reveal, accordions,
  product gallery, add-to-cart, and cart/checkout/confirmation rendering.
- **Imagery:** `assets/images/` — on-brand SVG illustrations of the device.
  See [`assets/images/README.md`](assets/images/README.md) to swap in real photos.

## SEO

Per-page `<title>`/meta descriptions, canonical URLs, Open Graph + Twitter cards,
semantic HTML, descriptive `alt` text, `sitemap.xml`, `robots.txt`, and JSON-LD
structured data (Organization, WebSite, Product + Offer, BreadcrumbList, FAQPage).

> Set your real domain in the canonical/OG tags and `sitemap.xml` (currently
> `https://matchasous.com`) before launch.

## ⚠️ Before you go live

The product specs, pricing, ratings and policies are **sensible placeholders**.
Review and confirm everything in [`SPECS-TO-VERIFY.md`](SPECS-TO-VERIFY.md).

## Deploy

It's a static site — host the repo root on GitHub Pages, Netlify, Vercel, Cloudflare
Pages, or any static host. No server or build required.
