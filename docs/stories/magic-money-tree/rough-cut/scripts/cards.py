#!/usr/bin/env python3
"""Render every card in cards/cards.json to a 1920x1080 PNG in clips/cards/ on D:.

    cards.py                 render all
    cards.py NAME [NAME …]   render some
    cards.py --sheet         also write clips/cards/_contact.jpg (every card, small, for review)

One typeface for the whole film (Libre Baskerville, OFL, in ../fonts/), one ground, one ink.
Kinds:
  verb     "1923 · SHAKE": segments joined by a dot; the last segment bold, the rest regular and dimmer
  word     one bold word, large (PLANT, SHAKEN …)
  date     one regular line, tracked caps
  data     a large line and a smaller sub-line
  quote    italic words in curly quotes, wrapped; attribution in small tracked caps. `lit` names one
           word to keep bright while the rest dim (the "actually" card)
  column   lines stacked, revealed as separate PNGs NAME-1, NAME-2 … (each adds a line)
  title    the film's title, tracked wide
  label    TRANSPARENT; small tracked caps bottom-left: sits on V4 over its shot
  lower    TRANSPARENT; a name and a sub-line bottom-left
  payslip  two identical payslip outlines, headed with two years, an equals sign between
  placeholder  a grey card naming a picture still to be made, so the timeline has no holes
"""
import json, os, sys, textwrap
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
RC = os.path.normpath(os.path.join(HERE, ".."))
OUT = "/mnt/d/badcode-videos/magic-money-tree/clips/cards"
W, H = 1920, 1080
GROUND, INK, DIM, RED = (5, 6, 7), (238, 243, 246), (238, 243, 246, 150), (204, 43, 55)
ROMAN = os.path.join(RC, "fonts", "LibreBaskerville[wght].ttf")
ITALIC = os.path.join(RC, "fonts", "LibreBaskerville-Italic[wght].ttf")


def font(size, weight="Regular", italic=False):
    f = ImageFont.truetype(ITALIC if italic else ROMAN, size)
    try:
        f.set_variation_by_name(weight)
    except Exception:
        pass
    return f


def tracked(d, xy, text, f, fill, track=0.0, anchor="ls"):
    """Draw text with letter-spacing (track, in ems). Returns the drawn width. anchor l/m/r on x."""
    widths = [d.textlength(c, font=f) for c in text]
    total = sum(widths) + track * f.size * max(0, len(text) - 1)
    x, y = xy
    if anchor[0] == "m":
        x -= total / 2
    elif anchor[0] == "r":
        x -= total
    for c, w in zip(text, widths):
        d.text((x, y), c, font=f, fill=fill, anchor="l" + anchor[1])
        x += w + track * f.size
    return total


def fit(text, size, weight="Regular", track=0.12, maxw=1640):
    """The largest size <= size at which the tracked line fits maxw."""
    d = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    while size > 20:
        f = font(size, weight)
        if sum(d.textlength(c, font=f) for c in text) + track * size * (len(text) - 1) <= maxw:
            return f
        size -= 2
    return font(size, weight)


def canvas(transparent=False):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0) if transparent else GROUND + (255,))
    return im, ImageDraw.Draw(im)


def verb(c):
    im, d = canvas()
    segs = [s.strip() for s in c["text"].split("·")]
    size = c.get("size", 92)
    while size > 30 and fit(c["text"].replace("·", "  "), size, "Bold").size < size:
        size -= 2
    fr, fb = font(size), font(size, "Bold")
    gap = size * 0.9
    dot_r = size * 0.09
    widths = []
    for i, s in enumerate(segs):
        f = fb if i == len(segs) - 1 else fr
        widths.append(sum(d.textlength(ch, font=f) for ch in s) + 0.12 * size * (len(s) - 1))
    total = sum(widths) + gap * (len(segs) - 1)
    x, y = W / 2 - total / 2, H / 2 + size * 0.35
    for i, s in enumerate(segs):
        last = i == len(segs) - 1
        tracked(d, (x, y), s, fb if last else fr, INK if last else DIM, 0.12)
        x += widths[i]
        if not last:
            cx, cy = x + gap / 2, H / 2
            d.ellipse([cx - dot_r, cy - dot_r, cx + dot_r, cy + dot_r], fill=RED)
            x += gap
    return im


def word(c):
    im, d = canvas()
    tracked(d, (W / 2, H / 2 + 50), c["text"], font(c.get("size", 150), "Bold"), INK, 0.14, "ms")
    return im


def date(c):
    im, d = canvas()
    tracked(d, (W / 2, H / 2 + 30), c["text"], fit(c["text"], c.get("size", 84), track=0.14), INK, 0.14, "ms")
    return im


def data(c):
    im, d = canvas()
    tracked(d, (W / 2, H / 2 + 10), c["text"], fit(c["text"], c.get("size", 84), "Bold", 0.06), INK, 0.06, "ms")
    if c.get("sub"):
        tracked(d, (W / 2, H / 2 + 110), c["sub"], font(38), DIM, 0.18, "ms")
    return im


def quote(c, lit=None):
    im, d = canvas()
    size = c.get("size", 64)
    fi = font(size, "Regular", italic=True)
    words = ("“" + c["text"] + "”").split()
    # wrap by pixel width
    lines, cur = [], []
    for w in words:
        trial = " ".join(cur + [w])
        if d.textlength(trial, font=fi) > c.get("width", 1400) and cur:
            lines.append(cur)
            cur = [w]
        else:
            cur.append(w)
    lines.append(cur)
    lh = size * 1.5
    block_h = lh * len(lines) + (90 if c.get("by") else 0)
    y = H / 2 - block_h / 2 + size
    for ln in lines:
        x = W / 2 - d.textlength(" ".join(ln), font=fi) / 2
        for w in ln:
            bare = w.strip("“”.,;:'!?…").lower()
            fill = INK if (lit is None or bare == lit.lower()) else (238, 243, 246, 70)
            d.text((x, y), w, font=fi, fill=fill, anchor="ls")
            x += d.textlength(w + " ", font=fi)
        y += lh
    if c.get("by"):
        tracked(d, (W / 2, y + 40), c["by"], font(30), DIM, 0.2, "ms")
    return im


def column(c):
    ims = []
    for k in range(1, len(c["lines"]) + 1):
        im, d = canvas()
        size = c.get("size", 60)
        lh = size * 1.9
        y = H / 2 - lh * (len(c["lines"]) - 1) / 2 + size * 0.35
        for i, ln in enumerate(c["lines"]):
            if i < k:
                segs = [s.strip() for s in ln.split("·")]
                tracked(d, (W / 2 - 40, y), segs[0], font(size), DIM, 0.12, "rs")
                d.ellipse([W / 2 - 7, y - size * 0.35 - 7, W / 2 + 7, y - size * 0.35 + 7], fill=RED)
                tracked(d, (W / 2 + 40, y), segs[1], font(size, "Bold"), INK, 0.12, "ls")
            y += lh
        ims.append(im)
    return ims


def title(c):
    im, d = canvas()
    tracked(d, (W / 2, H / 2 + 25), c["text"], font(c.get("size", 70)), INK, 0.32, "ms")
    return im


def label(c):
    im, d = canvas(transparent=True)
    f = font(32, "Bold")
    wdt = tracked(ImageDraw.Draw(Image.new("RGBA", (1, 1))), (0, 0), c["text"], f, INK, 0.22)
    x, y = 96, H - 84
    d.rectangle([x - 16, y - 40, x + wdt + 16, y + 14], fill=(5, 6, 7, 170))
    tracked(d, (x, y), c["text"], f, INK, 0.22)
    return im


def lower(c):
    im, d = canvas(transparent=True)
    x, y = 120, H - 150
    d.rectangle([x - 24, y - 60, x + 900, y + 60], fill=(5, 6, 7, 150))
    tracked(d, (x, y), c["text"], font(44, "Bold"), INK, 0.12)
    if c.get("sub"):
        tracked(d, (x, y + 46), c["sub"], font(28), DIM, 0.18)
    return im


def payslip(c):
    im, d = canvas()
    years = c["years"]
    fr, fb, fm = font(30), font(34, "Bold"), font(26)
    for i, yr in enumerate(years):
        x0 = 330 + i * 760
        d.rectangle([x0, 260, x0 + 500, 820], outline=INK, width=3)
        tracked(d, (x0 + 250, 330), "PAYSLIP", fb, INK, 0.2, "ms")
        tracked(d, (x0 + 250, 380), yr, fr, DIM, 0.2, "ms")
        for j, (k, v) in enumerate(c["rows"]):
            yy = 470 + j * 70
            d.text((x0 + 40, yy), k, font=fm, fill=DIM, anchor="ls")
            d.text((x0 + 460, yy), v, font=fm, fill=INK, anchor="rs")
            d.line([x0 + 40, yy + 18, x0 + 460, yy + 18], fill=(238, 243, 246, 60), width=1)
    tracked(d, (W / 2, 560), "=", font(120), RED, 0, "ms")
    return im


def placeholder(c):
    im = Image.new("RGBA", (W, H), (28, 30, 32, 255))
    d = ImageDraw.Draw(im)
    tracked(d, (W / 2, H / 2 - 30), c["name"], font(40, "Bold"), (180, 186, 190), 0.2, "ms")
    for i, ln in enumerate(textwrap.wrap(c["text"], 60)):
        d.text((W / 2, H / 2 + 40 + i * 48), ln, font=font(34, italic=True), fill=(180, 186, 190), anchor="ms")
    tracked(d, (W / 2, H - 90), "PICTURE TO COME", font(24), (120, 126, 130), 0.3, "ms")
    return im


KINDS = dict(verb=verb, word=word, date=date, data=data, quote=quote, title=title, label=label,
             lower=lower, payslip=payslip, placeholder=placeholder)


def save(im, name):
    p = os.path.join(OUT, name + ".png")
    (im if im.mode == "RGBA" and name.startswith(("LABEL", "LOWER")) else im.convert("RGB")).save(p)
    return p


def main(args):
    sheet = "--sheet" in args
    names = [a for a in args if not a.startswith("--")]
    cards = json.load(open(os.path.join(RC, "cards", "cards.json")))["cards"]
    os.makedirs(OUT, exist_ok=True)
    done = []
    for c in cards:
        if names and c["name"] not in names:
            continue
        if c["kind"] == "column":
            for k, im in enumerate(column(c), 1):
                done.append(save(im, f"{c['name']}-{k}"))
            continue
        done.append(save(KINDS[c["kind"]](c), c["name"]))
        if c["kind"] == "quote" and c.get("lit"):
            done.append(save(quote(c, c["lit"]), c["name"] + "-LIT"))
    print(f"{len(done)} cards → {OUT}")
    if sheet:
        thumbs = [Image.open(p).convert("RGB").resize((384, 216)) for p in sorted(done)]
        cols = 5
        rows = (len(thumbs) + cols - 1) // cols
        sh = Image.new("RGB", (cols * 388, rows * 246), (90, 90, 90))
        dd = ImageDraw.Draw(sh)
        for i, (t, p) in enumerate(zip(thumbs, sorted(done))):
            x, y = (i % cols) * 388 + 2, (i // cols) * 246 + 2
            sh.paste(t, (x, y))
            dd.text((x + 4, y + 220), os.path.basename(p)[:-4], font=font(16), fill=(255, 255, 255))
        sh.save(os.path.join(OUT, "_contact.jpg"), quality=88)


if __name__ == "__main__":
    main(sys.argv[1:])
