#!/usr/bin/env python3
"""Draw the scene-10b chart as three short animations (and a still of each last frame) into
clips/charts/ on D:, from rough-cut/data/debt-1946-1973.csv (Bank of England, Millennium dataset).

  CHART-10B-A  the national debt in pounds draws in (0–45 £bn axis): it ends bigger
  CHART-10B-B  the axis widens to 0–90 and the economy draws in over it: it rose faster
  CHART-10B-C  debt as a share of the economy draws in, falling from 259% to 48% (in the brand red)

Same ground, ink and typeface as the cards. 1920x1080, 25 fps, H.264 at high quality.
"""
import csv, os, subprocess, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cards import font, tracked, GROUND, INK, RED  # noqa: E402

RC = os.path.normpath(os.path.join(HERE, ".."))
OUT = "/mnt/d/badcode-videos/magic-money-tree/clips/charts"
W, H, FPS = 1920, 1080, 25
X0, X1, Y0, Y1 = 300, 1480, 250, 850          # plot box: left, right, top, bottom
DIM = (238, 243, 246, 110)
FAINT = (238, 243, 246, 40)
SOURCE = "SOURCE: BANK OF ENGLAND, A MILLENNIUM OF MACROECONOMIC DATA FOR THE UK"

rows = list(csv.DictReader(open(os.path.join(RC, "data", "debt-1946-1973.csv"))))
YEARS = [int(r["year"]) for r in rows]
DEBT = [float(r["debt_bn"]) for r in rows]
GDP = [float(r["gdp_bn"]) for r in rows]
PCT = [float(r["debt_pct_gdp"]) for r in rows]


def ease(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def xpos(i):
    return X0 + (X1 - X0) * i / (len(YEARS) - 1)


def ypos(v, top):
    return Y1 - (Y1 - Y0) * v / top


def frame(title, top, ticks, fmt, series, source=True, start_label=None):
    """series: list of (values, fraction drawn 0..1, colour, width, end label or None)."""
    im = Image.new("RGBA", (W, H), GROUND + (255,))
    d = ImageDraw.Draw(im, "RGBA")
    tracked(d, (X0, 170), title, font(40, "Bold"), INK, 0.14)
    ft = font(26)
    for v in ticks:
        y = ypos(v, top)
        if y < Y0 - 2:
            continue
        d.line([X0, y, X1, y], fill=FAINT, width=1)
        d.text((X0 - 24, y), fmt(v), font=ft, fill=DIM, anchor="rm")
    d.line([X0, Y1, X1, Y1], fill=DIM, width=2)
    for i, yr in enumerate(YEARS):
        if yr in (1946, 1950, 1955, 1960, 1965, 1970, 1973):
            d.text((xpos(i), Y1 + 40), str(yr), font=ft, fill=DIM, anchor="mm")
    for vals, frac, col, wid, label in series:
        n = (len(vals) - 1) * frac
        k = int(n)
        pts = [(xpos(i), ypos(vals[i], top)) for i in range(k + 1)]
        if k < len(vals) - 1:
            f = n - k
            pts.append((xpos(k) + (xpos(k + 1) - xpos(k)) * f,
                        ypos(vals[k] + (vals[k + 1] - vals[k]) * f, top)))
        if len(pts) > 1:
            d.line(pts, fill=col, width=wid, joint="curve")
        if pts:
            x, y = pts[-1]
            d.ellipse([x - wid, y - wid, x + wid, y + wid], fill=col)
            if label and frac >= 0.999:
                d.text((x + 24, y), label, font=font(30, "Bold"), fill=col, anchor="lm")
    for vals, frac, col, wid, label in series:
        if frac > 0 and start_label:
            d.text((X0 - 24 - 90, ypos(vals[0], top) - 34), start_label, font=font(30, "Bold"), fill=col, anchor="lm")
    if source:
        tracked(d, (X0, H - 70), SOURCE, font(20), DIM, 0.12)
    return im.convert("RGB")


def encode(name, frames):
    os.makedirs(OUT, exist_ok=True)
    dst = os.path.join(OUT, name + ".mp4")
    p = subprocess.Popen(["ffmpeg", "-nostdin", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
                          "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "12",
                          "-preset", "slow", "-pix_fmt", "yuv420p", "-color_range", "tv",
                          "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", dst],
                         stdin=subprocess.PIPE)
    last = None
    for im in frames:
        p.stdin.write(im.tobytes())
        last = im
    p.stdin.close()
    p.wait()
    last.save(os.path.join(OUT, name + ".png"))
    print(dst)


def pounds(v):
    return f"£{int(v)}BN"


def main():
    s = FPS
    # A: debt in pounds, 3.5 s draw, 1.5 s hold
    encode("CHART-10B-A", (frame("THE NATIONAL DEBT, IN POUNDS", 45, range(0, 50, 10), pounds,
                                 [(DEBT, ease(i / (3.5 * s)), INK, 6, "£39BN")]) for i in range(int(5 * s))))
    # B: axis widens 45 -> 90 over 1 s, then the economy draws over 3 s, 1.5 s hold
    def b(i):
        t = i / s
        top = 45 + 45 * ease(t / 1.0)
        return frame("THE NATIONAL DEBT, AND THE ECONOMY", top, range(0, 100, 10), pounds,
                     [(DEBT, 1.0, (120, 126, 132), 5, "DEBT £39BN"), (GDP, ease((t - 1.0) / 3.0), INK, 6, "ECONOMY £81BN")])
    encode("CHART-10B-B", (b(i) for i in range(int(5.5 * s))))
    # C: debt as a share of the economy, 4 s draw, 2 s hold
    encode("CHART-10B-C", (frame("THE DEBT, AS A SHARE OF THE ECONOMY", 280, range(0, 300, 50), lambda v: f"{int(v)}%",
                                 [(PCT, ease(i / (4 * s)), RED, 7, "48%")], start_label="259%") for i in range(int(6 * s))))


if __name__ == "__main__":
    main()
