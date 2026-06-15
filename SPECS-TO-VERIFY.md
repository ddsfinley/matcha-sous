# ⚠️ Claims to verify before launch

You chose to use sensible **placeholder specs** so the site looks complete now.
Everything below was **invented as a plausible default** and should be confirmed
(or corrected) before the store goes live, so no claim is inaccurate. Each item
notes where it appears so you can find and edit it fast.

## Product specifications
| Claim (placeholder) | Where it appears | Verified? |
|---------------------|------------------|-----------|
| Price **$149.00**, compare-at **$189.00** ("Save $40") | everywhere | ☐ |
| **Food-grade 304 stainless steel** pitcher | product, index, how-it-works, faq | ☐ |
| **Contactless magnetic whisk** drive | product, index, how-it-works | ☐ |
| **3 speeds** + **built-in timer** (auto-stop) | product, index, how-it-works | ☐ |
| Whisks a bowl in **~20 seconds** | hero, product, how-it-works | ☐ |
| Etched **40 / 80 / 120 ml** markings | product, index, images | ☐ |
| **USB-C powered** (cable included) | product, index, how-it-works | ☐ |
| Weight **~600 g** | product (specs table) | ☐ |
| Finishes: **Onyx · Sage · Champagne** | product (variant swatches), specs | ☐ |
| "Whisper-quiet", "backlit touch controls", "hand-wash only" | product, index | ☐ |
| What's in the box: base, steel pitcher, magnetic whisk, USB-C cable, ritual guide | product, images | ☐ |

## Policies & guarantees
| Claim (placeholder) | Where | Verified? |
|---------------------|-------|-----------|
| **Free express shipping**, dispatched in **1–2 business days** | global trust bar, product, shipping page | ☐ |
| **30-night trial** | global, product, shipping page | ☐ |
| **2-year warranty** | global, product, shipping page | ☐ |
| Delivery time estimates (US / international) | shipping-returns | ☐ |

## Social proof (placeholder / illustrative)
| Claim | Where | Verified? |
|-------|-------|-----------|
| **4.9 / 5 from 237 reviews** (also in Product JSON-LD `aggregateRating`) | index, product | ☐ |
| "Loved by 10,000+ matcha drinkers" | index | ☐ |
| Named testimonials (Aiko, Marco, Sofia, Rina, James, Noor) are fictional | index, product | ☐ |

> ⚠️ Review-rating structured data (`aggregateRating`) can trigger Google rich
> results. Only keep it if the numbers are real, or remove the `aggregateRating`
> blocks in `index.html` and `product.html` to stay compliant.

## Brand contact details (placeholder)
| Item | Value used | Verified? |
|------|-----------|-----------|
| Support email | care@matchasous.com | ☐ |
| Privacy email | privacy@matchasous.com | ☐ |
| Social handles | @matchasous (IG / TikTok / YouTube) | ☐ |
| Domain (canonical/sitemap/OG) | https://matchasous.com | ☐ |
| Support hours | Mon–Fri, 9–5 PT | ☐ |

## How to change the price everywhere
The price string `$149` / `149` appears in page copy, the `data-price` attributes
on add-to-cart buttons, and the Product JSON-LD. Search and replace:

```bash
grep -rln "149" --include=*.html .
```
