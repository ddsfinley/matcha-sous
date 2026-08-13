"""Build the full-bleed hero art: the vortex dissolving into the aubergine ground.

RGBA WebP so the hero's CSS radial-gradient shows through the fade — the photo
and the page background become one surface instead of a photo in a box.
"""
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

UP = "/tmp/claude-0/-home-user-bristol-dental-automation/224537ea-5543-5bf6-9fdf-6a4d9d0de4be/scratchpad/uploads"
OUT = "/home/user/bristol-dental-automation/site/assets/img"
AUB = (26, 19, 34)  # #1a1322 — the logo ground, exact


def gray_world(im, strength=0.55):
    a = np.asarray(im, dtype=np.float32)
    means = a.reshape(-1, 3).mean(0)
    target = means.mean()
    gain = 1.0 + (target / means - 1.0) * strength
    return Image.fromarray(np.clip(a * gain, 0, 255).astype(np.uint8))


def grade(im):
    v = gray_world(im, 0.55)
    a = np.asarray(v, dtype=np.float32)
    a[..., 0] *= 1.030          # warm shift
    a[..., 2] *= 0.975
    a = np.clip(a, 0, 255)
    v = Image.fromarray(a.astype(np.uint8))
    v = ImageEnhance.Color(v).enhance(1.06)
    v = ImageEnhance.Contrast(v).enhance(1.08)
    # Pull the frame toward the brand aubergine so the stainless and the
    # counter read as page ground, then bring the matcha's green back up —
    # the green is the hero, the scrim does the darkening in CSS.
    v = Image.blend(v, Image.new("RGB", v.size, AUB), 0.14)
    v = ImageEnhance.Color(v).enhance(1.34)
    v = ImageEnhance.Brightness(v).enhance(1.06)
    return v


def vortex_center(im):
    """Centroid of the green (matcha) pixels — where the eye lands."""
    a = np.asarray(im.resize((400, 265)), dtype=np.float32)
    g = a[..., 1] - (a[..., 0] + a[..., 2]) / 2
    m = g > np.percentile(g, 82)
    ys, xs = np.nonzero(m)
    return xs.mean() / 400, ys.mean() / 265


def smoothstep(t):
    t = np.clip(t, 0, 1)
    return t * t * (3 - 2 * t)


def place(photo, cw, ch, cx, cy, scale_by, pc):
    """Scale `photo` so it covers the canvas by `scale_by`, then position its
    focal point `pc` at canvas fraction (cx, cy). Returns an RGB canvas."""
    pw, ph = photo.size
    s = max(cw / pw, ch / ph) * scale_by
    nw, nh = int(pw * s), int(ph * s)
    ph_r = photo.resize((nw, nh), Image.LANCZOS)
    ox = int(cx * cw - pc[0] * nw)
    oy = int(cy * ch - pc[1] * nh)
    ox = min(0, max(cw - nw, ox))       # never expose bare canvas
    oy = min(0, max(ch - nh, oy))
    canvas = Image.new("RGB", (cw, ch))
    canvas.paste(ph_r, (ox, oy))
    return canvas


src = Image.open(f"{UP}/action-01-vortex.jpg").convert("RGB")
pc = vortex_center(src)
print("source", src.size, "vortex centre", tuple(round(v, 3) for v in pc))
g = grade(src)

# Full-bleed and opaque: the CSS scrims (same aubergine, so the join is
# invisible) carve the reading area, rather than baking a fade into the file.
# ---- desktop: 2:1 band, vortex right of centre, bleeding off top and bottom -
place(g, 2400, 1200, 0.55, 0.50, 1.18, pc).save(
    f"{OUT}/hero-bleed.webp", quality=84, method=6)

# ---- mobile: tall, vortex low so the type has the top third -----------------
place(g, 1000, 1300, 0.54, 0.68, 1.02, pc).save(
    f"{OUT}/hero-bleed-sm.webp", quality=84, method=6)

for f in ("hero-bleed.webp", "hero-bleed-sm.webp"):
    im = Image.open(f"{OUT}/{f}")
    import os
    print(f, im.size, im.mode, f"{os.path.getsize(f'{OUT}/{f}')//1024} KB")
