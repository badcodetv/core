"""Letter the closed bank in scene E's E03 wide street (GPOM ending, review round 2, 2026-10-22).

    ~/.cache/badcode-lips/venv/bin/python -I bank_sign_e03.py CLIP OUT [--name "DOWNLAND BANK"]

Review round 2 found E03's street did not match E02's window (chip shop, pharmacy, then a lit bookmaker where E02's
closed bank stood). The plate was remade (E03b-r1-b: the bookmaker turned into the same whitewashed bank, blank
fascia, black door) and re-animated as E03b-chain. This letters it exactly as bank_sign.py lettered E02: the same
name in the same navy serif with the thin red rule, on the blank fascia (x 465-552, y 333-371 on the chain's first
frame), and the same red-topped "THIS BRANCH HAS NOW CLOSED" sheet in the right-hand window (x 520-539, y 398-424).
The street is camera-locked but drifts and breathes a few pixels over 17 s, so the lettering follows a similarity
transform (Lucas-Kanade corners on the fixed shopfronts left of the bus, RANSAC, always measured against frame 0).
"""
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
K = 8
FASCIA = (466, 334, 551, 370)
NOTICE = (521, 399, 538, 423)
TRACK = (0, 230, 560, 520)  # the chip shop, the pharmacy and the bank: fixed, left of the receding bus
# Omni lettered the shuttered shop next door "Bank Bank" (white on a navy fascia), visible from ~1 s behind the bus.
# Its words are removed: a clean board is made once from frame REF (bus clear) by a grey opening that wipes the thin
# white strokes, then put back on every frame through the same tracking, only where the frame still matches the
# reference (so the passing bus stays in front of it).
REF = 120
DETEXT = (568, 348, 647, 385)  # in frame REF's own coordinates


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
    im = Image.new('RGBA', (W * K, H * K), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x0, y0, x1, y1 = FASCIA
    bw, bh = (x1 - x0) * K, (y1 - y0) * K
    f, (l, t, r, b) = fit(d, name, SERIF, int(bw * 0.84), int(bh * 0.40))
    tx = x0 * K + (bw - (r - l)) // 2 - l
    ty = y0 * K + (bh - (b - t)) // 2 - t - int(bh * 0.04)
    d.text((tx, ty), name, font=f, fill=(28, 38, 70, 235))
    ry = ty + b + int(bh * 0.07)
    d.rectangle([tx + l, ry, tx + r, ry + max(2, K // 2)], fill=(150, 30, 40, 200))
    nx0, ny0, nx1, ny1 = NOTICE
    d.rectangle([nx0 * K, ny0 * K, nx1 * K, ny1 * K], fill=(220, 218, 210, 255))
    d.rectangle([nx0 * K, ny0 * K, nx1 * K, int((ny0 + 3.5) * K)], fill=(170, 30, 38, 255))
    nw = (nx1 - nx0 - 3) * K
    yy = int((ny0 + 5) * K)
    for word, hfrac in (('THIS', 3), ('BRANCH', 3), ('HAS NOW', 3), ('CLOSED', 4)):
        f, (l, t, r, b) = fit(d, word, SANS, nw, hfrac * K)
        d.text(((nx0 * K + (nx1 - nx0) * K // 2) - (r - l) // 2 - l, yy - t), word, font=f, fill=(25, 25, 30, 255))
        yy += (b - t) + K
    im = im.resize((W, H), Image.LANCZOS)
    return np.asarray(im).astype(np.float32) / 255.0


cap = cv2.VideoCapture(clip)
fps = cap.get(cv2.CAP_PROP_FPS) or 24
W, H = int(cap.get(3)), int(cap.get(4))
L = layer(W, H)
rgb, alpha = L[..., [2, 1, 0]] * 255, L[..., 3]
ENC = ['-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', '-color_range', 'tv', '-colorspace', 'bt709',
       '-color_primaries', 'bt709', '-color_trc', 'bt709', '-an']
enc = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}',
                        '-r', f'{fps:g}', '-i', '-', *ENC, out], stdin=subprocess.PIPE)
def transforms():
    """Pass 1: frame 0 -> frame n similarity for every n, and frame REF itself."""
    cp = cv2.VideoCapture(clip)
    mk = np.zeros((H, W), np.uint8)
    mk[TRACK[1]:TRACK[3], TRACK[0]:TRACK[2]] = 255
    g0 = p0 = ref = None
    Ms, M = [], np.float32([[1, 0, 0], [0, 1, 0]])
    while True:
        ok, f = cp.read()
        if not ok:
            break
        g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
        if g0 is None:
            g0, p0 = g, cv2.goodFeaturesToTrack(g, 400, 0.01, 6, mask=mk)
        else:
            p1, st, _ = cv2.calcOpticalFlowPyrLK(g0, g, p0, None, winSize=(21, 21), maxLevel=3)
            good = st.ravel() == 1
            M2, _ = cv2.estimateAffinePartial2D(p0[good], p1[good], method=cv2.RANSAC, ransacReprojThreshold=1.5)
            if M2 is not None:
                M = M2.astype(np.float32)
        if len(Ms) == REF:
            ref = f.copy()
        Ms.append(M.copy())
    return Ms, ref


Ms, REFF = transforms()
# the clean board in frame-0 coordinates: open the REF frame's box, then map REF -> 0
x0, y0, x1, y1 = DETEXT
box = REFF[y0 - 6:y1 + 6, x0 - 6:x1 + 6]
clean = cv2.GaussianBlur(cv2.morphologyEx(box, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8)), (0, 0), 1.5)
cl_full, rf_full = REFF.astype(np.float32).copy(), REFF.astype(np.float32)
cl_full[y0 - 6:y1 + 6, x0 - 6:x1 + 6] = clean
dm = np.zeros((H, W), np.float32)
dm[y0:y1, x0:x1] = 1
dm = cv2.GaussianBlur(dm, (0, 0), 2)
inv = cv2.invertAffineTransform(Ms[REF])
to0 = lambda im: cv2.warpAffine(im, inv, (W, H), flags=cv2.INTER_LINEAR)  # noqa: E731
CL0, RF0, DM0 = to0(cl_full), to0(rf_full), to0(dm)
mask = np.zeros((H, W), np.uint8)
mask[TRACK[1]:TRACK[3], TRACK[0]:TRACK[2]] = 255
g0 = p0 = rgb_l = None
moves, n = [], 0
while True:
    ok, f = cap.read()
    if not ok:
        break
    g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    if g0 is None:
        g0 = g
        p0 = cv2.goodFeaturesToTrack(g0, 400, 0.01, 6, mask=mask)
        lum = cv2.GaussianBlur(g.astype(np.float32), (0, 0), 4)
        board = lum[FASCIA[1]:FASCIA[3], FASCIA[0]:FASCIA[2]].mean()
        shade = np.clip(lum / max(board, 1), 0.6, 1.1)[..., None]
        rgb_l = rgb * shade
        M = np.float32([[1, 0, 0], [0, 1, 0]])
    else:
        p1, st, _ = cv2.calcOpticalFlowPyrLK(g0, g, p0, None, winSize=(21, 21), maxLevel=3)
        good = st.ravel() == 1
        M2, inl = cv2.estimateAffinePartial2D(p0[good], p1[good], method=cv2.RANSAC, ransacReprojThreshold=1.5)
        if M2 is not None:
            M = M2.astype(np.float32)
    moves.append((M[0, 2], M[1, 2], np.hypot(M[0, 0], M[1, 0])))
    c = cv2.warpAffine(rgb_l, M, (W, H), flags=cv2.INTER_LINEAR)
    al = cv2.warpAffine(alpha, M, (W, H), flags=cv2.INTER_LINEAR)
    c = cv2.GaussianBlur(c, (0, 0), 0.6)  # the plate's own softness
    al = cv2.GaussianBlur(al, (0, 0), 0.6)[..., None] * 0.92
    ff = f.astype(np.float32)
    # the "Bank Bank" board: clean where the frame still looks like the reference (not where the bus is in front)
    Mn = Ms[n] if n < len(Ms) else M
    cl, rf, dmn = (cv2.warpAffine(x, Mn, (W, H), flags=cv2.INTER_LINEAR) for x in (CL0, RF0, DM0))
    diff = cv2.GaussianBlur(np.abs(ff - rf).mean(2), (0, 0), 2)
    clear = min(1.0, max(0.0, (n / fps - 3.0) / 0.5))  # the bus has left the board by ~3 s
    # the bus comes from the right as one solid block: find its left edge on the board, keep everything right of it
    ys, xs = np.where(dmn > 0.5)
    bus = np.zeros((H, W), np.float32)
    if len(xs):
        bx0, bx1, by0, by1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
        frac = (diff[by0:by1, bx0:bx1] > 35).mean(0)
        hit = np.where(frac > 0.3)[0]
        if len(hit):
            bus[:, max(0, bx0 + hit[0] - 3):] = 1
            bus = cv2.GaussianBlur(bus, (0, 0), 1.5)
    vis = np.maximum(1 - bus, clear) * dmn
    ff = ff * (1 - vis[..., None]) + cl * vis[..., None]
    f = np.clip(ff * (1 - al) + c * al + 0.5, 0, 255).astype(np.uint8)
    enc.stdin.write(f.tobytes())
    n += 1
enc.stdin.close()
enc.wait()
mv = np.array(moves)
print(f'{out}: {n} frames; drift max dx {np.abs(mv[:, 0]).max():.1f} dy {np.abs(mv[:, 1]).max():.1f} px, '
      f'scale {mv[:, 2].min():.3f}-{mv[:, 2].max():.3f} (followed)')
