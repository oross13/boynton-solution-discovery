#!/usr/bin/env python3
"""Generate the plugin listing icon at plugins/boynton-solution-discovery/.claude-plugin/icon.png.

A simple, brand-neutral discovery motif: a magnifying glass on a deep indigo rounded square.
1024x1024 PNG (within the 512–2048 px requirement). Reproducible; run: `python3 scripts/make-icon.py`.
Requires Pillow.
"""
import os
from PIL import Image, ImageDraw

SIZE = 1024
OUT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "plugins", "boynton-solution-discovery", ".claude-plugin", "icon.png",
)

BG = (26, 43, 71)          # deep indigo
GLASS = (233, 236, 240)    # off-white
ACCENT = (240, 180, 90)    # warm amber (lens tint / highlight)


def rounded_rect_mask(size, radius):
    m = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=255)
    return m


def main():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img)

    # Magnifying glass geometry
    cx, cy, r = 430, 420, 230          # lens center + outer radius
    ring = 54                           # ring thickness

    # Lens tint (subtle amber fill inside the ring)
    draw.ellipse([cx - r + ring, cy - r + ring, cx + r - ring, cy + r - ring],
                 fill=(36, 58, 92))
    # inner highlight arc
    draw.arc([cx - r + ring + 20, cy - r + ring + 20, cx + r - ring - 20, cy + r - ring - 20],
             start=150, end=250, fill=ACCENT, width=18)

    # Ring
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=GLASS, width=ring)

    # Handle (thick rounded line from lens edge outward to lower-right)
    import math
    ang = math.radians(45)
    hx0 = cx + (r - ring // 2) * math.cos(ang)
    hy0 = cy + (r - ring // 2) * math.sin(ang)
    hx1 = cx + (r + 230) * math.cos(ang)
    hy1 = cy + (r + 230) * math.sin(ang)
    draw.line([hx0, hy0, hx1, hy1], fill=GLASS, width=90)
    draw.ellipse([hx1 - 45, hy1 - 45, hx1 + 45, hy1 + 45], fill=GLASS)

    # Apply rounded-square mask so corners are rounded on the listing card
    mask = rounded_rect_mask(SIZE, radius=180)
    out = Image.new("RGB", (SIZE, SIZE), BG)
    out.paste(img, (0, 0), mask)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    out.save(OUT, "PNG")
    print(f"wrote {OUT} ({SIZE}x{SIZE})")


if __name__ == "__main__":
    main()
