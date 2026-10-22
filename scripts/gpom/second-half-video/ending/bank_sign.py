"""Letter the closed bank in scene E's E02 (GPOM ending, review round 1, 2026-10-22).

    ~/.cache/badcode-lips/venv/bin/python -I bank_sign.py CLIP OUT [--name "DOWNLAND BANK"]

The Flow plate was asked for no words (Flow garbles lettering), so the bank's blank fascia and the blank card in its
middle window are lettered here, exactly: a plain fictional bank name on the fascia board (x 570-823, y 188-236 on
E02-t3's first frame) and a printed 'This branch has now closed' notice on the card (x 697-740, y 322-382). Both sit
BEHIND the wet window, so they are softened a touch and take the plate's own light. The street is locked but breathes
about 1.3 px, so each frame's offset is measured by phase correlation on the shopfront and the lettering follows it.
Nothing overlaps the woman: her head never comes right of x 460 in this take."""
import subprocess
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

a = sys.argv[1:]
clip, out = a[0], a[1]
name = a[a.index('--name') + 1] if '--name' in a else 'DOWNLAND BANK'
SERIF = '/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf'
SANS = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
SANS_R = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
K = 4  # draw at 4x, then shrink: clean edges at this size


def fit(draw, text, font_path, box_w, box_h):
    s = box_h
    while s > 4:
        f = ImageFont.truetype(font_path, s)
        l, t, r, b = draw.textbbox((0, 0), text, font=f)
        if r - l <= box_w and b - t <= box_h:
            return f, (l, t, r, b)
        s -= 1
    return ImageFont.truetype(font_path, 4), (0, 0, 1, 1)


def layer(W, H):
    """RGBA lettering at 1x on a transparent W x H canvas."""
    im = Image.new('RGBA', (W * K, H * K), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    # fascia: navy serif capitals on the off-white board, centred, with a thin rule under
    x0, y0, x1, y1 = 570, 188, 823, 236
    bw, bh = (x1 - x0) * K, (y1 - y0) * K
    f, (l, t, r, b) = fit(d, name, SERIF, int(bw * 0.80), int(bh * 0.46))
    tx = x0 * K + (bw - (r - l)) // 2 - l
    ty = y0 * K + (bh - (b - t)) // 2 - t - int(bh * 0.04)
    d.text((tx, ty), name, font=f, fill=(28, 38, 70, 235))
    ry = ty + b + int(bh * 0.07)
    d.rectangle([tx + l, ry, tx + r, ry + max(2, K)], fill=(150, 30, 40, 200))
    # notice: a white A3 sheet on the card: a red bar, then the words
    nx0, ny0, nx1, ny1 = 699, 324, 739, 380
    d.rectangle([nx0 * K, ny0 * K, nx1 * K, ny1 * K], fill=(220, 218, 210, 255))
    d.rectangle([nx0 * K, ny0 * K, nx1 * K, (ny0 + 7) * K], fill=(170, 30, 38, 255))
    nw = (nx1 - nx0 - 6) * K
    yy = (ny0 + 10) * K
    for word, fp, hfrac in (('THIS', SANS, 6), ('BRANCH', SANS, 6), ('HAS NOW', SANS, 6), ('CLOSED', SANS, 8)):
        f, (l, t, r, b) = fit(d, word, fp, nw, hfrac * K)
        d.text(((nx0 * K + (nx1 - nx0) * K // 2) - (r - l) // 2 - l, yy - t), word, font=f, fill=(25, 25, 30, 255))
        yy += (b - t) + 2 * K
    f, (l, t, r, b) = fit(d, 'thank you for banking with us', SANS_R, nw, 3 * K)
    d.text(((nx0 * K + (nx1 - nx0) * K // 2) - (r - l) // 2 - l, yy + K - t), 'thank you for banking with us', font=f,
           fill=(60, 60, 66, 255))
    im = im.resize((W, H), Image.LANCZOS)
    return np.asarray(im).astype(np.float32) / 255.0


cap = cv2.VideoCapture(clip)
fps = cap.get(cv2.CAP_PROP_FPS) or 24
W, H = int(cap.get(3)), int(cap.get(4))
L = layer(W, H)
rgb, alpha = L[..., [2, 1, 0]] * 255, L[..., 3]
ENC = ['-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', '-color_range', 'tv', '-colorspace', 'bt709',
       '-color_primaries', 'bt709', '-color_trc', 'bt709', '-an']
enc = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}',
                        '-r', f'{fps:g}', '-i', '-', *ENC, out], stdin=subprocess.PIPE)
ref, n, drift = None, 0, []
# the plate's own light on the board and the card (they are lit unevenly by the lamp): multiply the lettering by the
# local brightness of the first frame relative to its mean, so it is not flatter or brighter than the wall it is on
while True:
    ok, f = cap.read()
    if not ok:
        break
    g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)[170:400, 550:850].astype(np.float32)
    if ref is None:
        ref = g
        lum = cv2.GaussianBlur(cv2.cvtColor(f, cv2.COLOR_BGR2GRAY).astype(np.float32), (0, 0), 6)
        board = lum[188:236, 570:823].mean()
        shade = np.clip(lum / max(board, 1), 0.6, 1.15)[..., None]
        rgb_l = rgb * shade
    (dx, dy), _ = cv2.phaseCorrelate(ref, g)
    drift.append((dx, dy))
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    c = cv2.warpAffine(rgb_l, M, (W, H), flags=cv2.INTER_LINEAR)
    al = cv2.warpAffine(alpha, M, (W, H), flags=cv2.INTER_LINEAR)
    c = cv2.GaussianBlur(c, (0, 0), 0.85)  # behind the wet glass
    al = cv2.GaussianBlur(al, (0, 0), 0.85)[..., None] * 0.9
    ff = f.astype(np.float32)
    f = np.clip(ff * (1 - al) + c * al + 0.5, 0, 255).astype(np.uint8)
    enc.stdin.write(f.tobytes())
    n += 1
enc.stdin.close()
enc.wait()
d = np.array(drift)
print(f'{out}: {n} frames; shopfront drift max {np.abs(d).max():.2f}px (followed)')
