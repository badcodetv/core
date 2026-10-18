#!/usr/bin/env python3
"""The Bank Robbery short, cut 4: the estate agent's window as a fruit machine, on the new plate (e01n-estate).

Cut 3's slot was flat drawtext over a flat window, and Jack asked for it to "look better". Here each price is laid out
on a flat card, rolled like a fruit-machine reel (a column of prices sliding down, blurred along the roll while it
spins, easing to a stop on double the old price), then warped onto the blank panel's four corners in the plate and
multiplied into it, so the glass reflections and the rain run over the ink. Camera is locked, so the corners are fixed.

usage: ~/.cache/badcode-recut/venv/bin/python slot4.py <plate.mp4|plate.jpg> <out.mov> [seconds]
"""
import random, subprocess, sys
import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont

SRC, OUT = sys.argv[1], sys.argv[2]
D = float(sys.argv[3]) if len(sys.argv) > 3 else 3.8
W, H, FPS = 1280, 720, 24
FONT = '/home/jackt/.cache/badcode-recut/font/Oswald.ttf'
# the blank white price panels in e01n-estate at 1280x720 (TL, TR, BR, BL), read off a grid
CARDS = [((168, 333), (352, 335), (355, 460), (163, 482)),
         ((470, 339), (557, 342), (557, 432), (468, 445)),
         ((618, 343), (667, 345), (667, 420), (618, 428))]
OLD = [180000, 210000, 195000]
R0 = 0.5                                     # the old prices hold this long
STOPS = [1.5, 1.95, 2.4]                      # each reel stops in turn
CW, CH = 600, 420                             # the flat card the price is drawn on
random.seed(7)

def font(px): return ImageFont.truetype(FONT, px)
BIG, SMALL = font(150), font(52)
def price(v): return '£{:,}'.format(v)

def card(text, dy=0.0, blur=0, prev=None, nxt=None):
    """the card's ink as a float mask (1 = ink): a small label, and the price strip scrolled by dy pixels"""
    im = Image.new('L', (CW, CH), 0); g = ImageDraw.Draw(im)
    g.text((CW / 2, 70), 'OFFERS OVER', font=SMALL, fill=255, anchor='mm')
    reel = Image.new('L', (CW, CH), 0); r = ImageDraw.Draw(reel); cy = 255
    for k, t in ((-1, prev), (0, text), (1, nxt)):
        if t: r.text((CW / 2, cy + dy + k * 190), t, font=BIG, fill=255, anchor='mm')
    a = np.asarray(reel, np.float32) / 255
    if blur > 1: a = cv2.blur(a, (1, int(blur)))           # motion blur along the roll only
    win = np.zeros_like(a); win[140:370] = 1                # the reel window: the strip shows only here
    return np.maximum(np.asarray(im, np.float32) / 255, a * win)

def ease(x): return 1 - (1 - x) ** 3

def frames(n):
    if SRC.endswith('.jpg'):
        f = cv2.resize(cv2.imread(SRC), (W, H)); return [f] * n
    p = subprocess.run(['ffmpeg', '-v', 'error', '-ss', '0.3', '-i', SRC, '-t', f'{D + 0.2}', '-vf', f'scale={W}:{H},fps={FPS}', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], capture_output=True).stdout
    fs = [np.frombuffer(p[i * W * H * 3:(i + 1) * W * H * 3], np.uint8).reshape(H, W, 3) for i in range(len(p) // (W * H * 3))]
    return (fs + [fs[-1]] * n)[:n]

N = int(round(D * FPS)); base = frames(N)
reels = [[price(random.randrange(120, 499) * 1000) for _ in range(40)] for _ in CARDS]
M = [cv2.getPerspectiveTransform(np.float32([[0, 0], [CW, 0], [CW, CH], [0, CH]]), np.float32(q)) for q in CARDS]
ink = np.array([60, 30, 25], np.float32) / 255      # dark navy (BGR), printed, not black
enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                        '-c:v', 'libx264', '-crf', '14', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-an', OUT + '.v.mp4'], stdin=subprocess.PIPE)
SPEED = 190 * 14                                    # px a second at full spin: fourteen prices a second
for i in range(N):
    t = i / FPS; f = base[i].astype(np.float32) / 255
    for k, (q, m) in enumerate(zip(CARDS, M)):
        new = price(2 * OLD[k])
        if t < R0: a = card(price(OLD[k]))
        elif t >= STOPS[k]: a = card(new)
        else:
            # spin up over 0.2 s, full speed, then the last 0.35 s eases the reel down onto the new price
            s = t - R0; T = STOPS[k] - R0
            if T - s < 0.35:
                u = ease(1 - (T - s) / 0.35); dy = (1 - u) * 190 * 0.9; a = card(new, dy=dy, blur=(1 - u) * 60, prev=reels[k][0])
            else:
                pos = SPEED * max(0.0, s - 0.1); j = int(pos // 190); dy = pos % 190
                a = card(reels[k][j % 40], dy=dy, blur=min(70, 10 + 300 * s), prev=reels[k][(j + 1) % 40], nxt=reels[k][(j - 1) % 40])
        w = cv2.warpPerspective(a, m, (W, H), flags=cv2.INTER_AREA)
        w = cv2.GaussianBlur(w, (0, 0), 0.6 + 0.4 * k)          # the further cards sit softer, like the photo
        f = f * (1 - w[..., None]) + (f * ink) * w[..., None] * 0.9 + f * w[..., None] * 0.1
    # one warm flash as the last reel lands, like a machine paying out
    J = STOPS[-1] + 0.1
    if J <= t < J + 0.12: f = np.clip(f * 1.18 + 0.03, 0, 1)
    g = np.random.normal(0, 0.012, (H, W, 1)).astype(np.float32)   # grain over the ink as well as the plate
    enc.stdin.write((np.clip(f + g, 0, 1) * 255).astype(np.uint8).tobytes())
enc.stdin.close(); enc.wait()
print('slot frames', N)
