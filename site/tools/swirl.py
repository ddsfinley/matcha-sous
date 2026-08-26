#!/usr/bin/env python3
"""Tapered-ribbon spiral for the Matcha Sous mark.

SVG cannot vary stroke-width along a path, which is why the previous icon was a
uniform hairline and read as concentric rings rather than a brushed enso. This
builds the stroke as a FILLED ribbon: sample a logarithmic spiral centreline,
offset perpendicular by +/- w(t)/2, close the two edges. Width runs from w_max
at the head to zero at the tail, so the brush lands heavy and lifts to a real
point, and no separate centre dot is needed.
"""
import math

CX = CY = 24.0


def spiral(turns, r_out, r_in, w_max, taper=1.25, start_deg=0.0, n=96):
    T = turns * 2 * math.pi
    k = math.log(r_out / r_in) / T
    a0 = math.radians(start_deg)

    def centre(t):
        th = t * T
        r = r_out * math.exp(-k * th)
        return CX + r * math.cos(a0 + th), CY + r * math.sin(a0 + th)

    def width(t):
        return w_max * (1.0 - t) ** taper

    pts = [centre(i / (n - 1)) for i in range(n)]
    left, right = [], []
    for i, (x, y) in enumerate(pts):
        px, py = pts[max(i - 1, 0)]
        qx, qy = pts[min(i + 1, n - 1)]
        dx, dy = qx - px, qy - py
        L = math.hypot(dx, dy) or 1e-9
        nx, ny = -dy / L, dx / L
        h = width(i / (n - 1)) / 2.0
        left.append((x + nx * h, y + ny * h))
        right.append((x - nx * h, y - ny * h))

    f = lambda s: " ".join(f"{x:.1f} {y:.1f}" for x, y in s)
    h0 = w_max / 2.0
    lx, ly = left[0]
    rx, ry = right[0]
    # down the left edge, the tail is a natural point, back up the right edge,
    # then a true semicircular cap across the head from right[0] to left[0].
    return (f"M{lx:.1f} {ly:.1f}L{f(left[1:])}L{f(list(reversed(right)))}"
            f"A{h0:.1f} {h0:.1f} 0 0 0 {lx:.1f} {ly:.1f}Z")


# The shipped mark. w_max=3.0 was chosen by rendering the icon beside the three
# stroked siblings at 56px: a ribbon tapering 3.0 -> 0 averages about 1.4, which
# is exactly their stroke-width, so the spiral reads as brushed without
# out-weighting the set. n=80 is the smallest sampling that stays smooth at 5x
# the icon's display size. Anything heavier than ~3.4 dominates the row.
SHIPPED = dict(turns=2.05, r_out=19.2, r_in=1.8, w_max=3.0, taper=1.20, n=80)

# Applied in index.html and box-marks.liquid as translate(-4.25 -3.4), which
# pulls the measured bounding box centre onto (24,24). Re-measure with
# getBBox() if any parameter above changes; do not eyeball it.
if __name__ == "__main__":
    print(spiral(**SHIPPED))

