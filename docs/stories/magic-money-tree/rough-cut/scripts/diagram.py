#!/usr/bin/env python3
"""Draw the scene-10a diagram — one QE transaction — as three build-up stills in clips/charts/.

  DIAGRAM-10A-1  the Bank of England creates new money (a red £ appears inside it)
  DIAGRAM-10A-2  the new money goes to a pension fund
  DIAGRAM-10A-3  a government bond comes back; the caption is the Bank's own point, paraphrased:
                 the fund now holds new money instead of a bond

Our own graphic (the Bank's site is non-commercial, so its graphics are never copied).
"""
import os, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cards import font, tracked, GROUND, INK, RED  # noqa: E402

OUT = "/mnt/d/badcode-videos/magic-money-tree/clips/charts"
W, H = 1920, 1080
DIM = (150, 156, 162)


def box(d, x, y, w, h, title, sub):
    d.rounded_rectangle([x, y, x + w, y + h], radius=14, outline=INK, width=4)
    tracked(d, (x + w / 2, y + h + 70), title, font(38, "Bold"), INK, 0.14, "ms")
    tracked(d, (x + w / 2, y + h + 118), sub, font(24), DIM, 0.16, "ms")


def arrow(d, x0, x1, y, col, label, up=True):
    d.line([x0, y, x1, y], fill=col, width=6)
    s = 1 if x1 > x0 else -1
    d.polygon([(x1, y), (x1 - s * 30, y - 16), (x1 - s * 30, y + 16)], fill=col)
    d.text(((x0 + x1) / 2, y + (-44 if up else 44)), label, font=font(34, "Bold"), fill=col, anchor="mm")


def draw(step):
    im = Image.new("RGB", (W, H), GROUND)
    d = ImageDraw.Draw(im)
    bx, fx, by, bw, bh = 260, 1300, 330, 360, 300
    box(d, bx, by, bw, bh, "BANK OF ENGLAND", "THE CENTRAL BANK")
    box(d, fx, by, bw, bh, "A PENSION FUND", "OR AN INSURER")
    d.text((fx + bw / 2, by + bh / 2), "BOND" if step < 3 else "£", font=font(64 if step < 3 else 120, "Bold"),
           fill=INK if step < 3 else RED, anchor="mm")
    if step == 1:
        d.text((bx + bw / 2, by + bh / 2), "£", font=font(120, "Bold"), fill=RED, anchor="mm")
        cap = "THE BANK CREATES NEW MONEY, ELECTRONICALLY"
    if step >= 2:
        arrow(d, bx + bw + 30, fx - 30, by + 100, RED, "NEW MONEY")
    if step == 2:
        cap = "IT USES THE NEW MONEY TO BUY A GOVERNMENT BOND"
    if step == 3:
        arrow(d, fx - 30, bx + bw + 30, by + bh - 100, INK, "GOVERNMENT BOND", up=False)
        d.text((bx + bw / 2, by + bh / 2), "BOND", font=font(64, "Bold"), fill=INK, anchor="mm")
        cap = "THE FUND NOW HOLDS NEW MONEY INSTEAD OF A BOND"
    tracked(d, (W / 2, 190), cap, font(40, "Bold"), INK, 0.12, "ms")
    tracked(d, (W / 2, H - 70), "ONE TRANSACTION IN QUANTITATIVE EASING · SIMPLIFIED", font(22), DIM, 0.14, "ms")
    return im


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for k in (1, 2, 3):
        p = os.path.join(OUT, f"DIAGRAM-10A-{k}.png")
        draw(k).save(p)
        print(p)
