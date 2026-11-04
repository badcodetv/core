#!/usr/bin/env python3
"""Switch the bridge's TV off: paint its glowing screen as dark glass, tracked frame by frame.

    ~/.cache/badcode-lips/venv/bin/python scripts/gpom/second-half-video/tv-off.py IN.mp4 OUT.mp4 [--box x0 y0 x1 y1]

Kai, 3 Nov (bridge timeline r1): "the TV screen needs to be turned off... the eye is drawn to it" (before the film, and
in the boom shot). The screen is found each frame as the bright red/green pixels inside --box (default: around the TV in
br2/br3), grown a few px and feathered, and only those are painted as dark, slightly lit glass, so whatever passes in
front of the set stays (a soft top-left sheen, the room's own
grain kept by blending 85%). The picture is otherwise untouched. 1280x720/24, yuv420p, limited range.
"""
import subprocess
import sys

import cv2
import numpy as np

src, dst = sys.argv[1], sys.argv[2]
box = (700, 400, 920, 600)
if '--box' in sys.argv:
    k = sys.argv.index('--box')
    box = tuple(int(v) for v in sys.argv[k + 1:k + 5])
cap = cv2.VideoCapture(src)
fps = cap.get(cv2.CAP_PROP_FPS) or 24
w, h = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
enc = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{w}x{h}',
                        '-r', str(fps), '-i', '-', '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p',
                        '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
                        dst], stdin=subprocess.PIPE)
SCREEN = (778, 449, 95, 77)   # the screen in the first frame of br2/br3 (x, y, w, h), measured off the clip
x, y, w0, h0 = SCREEN
tmpl = None
pos = (x, y)
while True:
    ok, f = cap.read()
    if not ok:
        break
    grey = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    # where is the glow this frame? the largest bright red/green patch near the set (the jolt moves it)
    sx0, sy0, sx1, sy1 = box
    roi = f[sy0:sy1, sx0:sx1].astype(int)
    b_, g_, r_ = roi[..., 0], roi[..., 1], roi[..., 2]
    lm = roi.mean(axis=2)
    gm = ((((r_ > 140) & (r_ - g_ > 40)) | ((g_ > 140) & (g_ - r_ > 40))) & (lm > 90)).astype(np.uint8)
    n, _, st, _ = cv2.connectedComponentsWithStats(gm)
    found = None
    if n > 1:
        i = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
        if st[i, cv2.CC_STAT_AREA] > 300:
            found = (sx0 + st[i, 0], sy0 + st[i, 1])
    if tmpl is None:   # the set with its bezel, from the first frame
        tmpl = grey[y - 12:y + h0 + 12, x - 12:x + w0 + 28].copy()
    else:              # follow it through the jolt: best match near where it was
        sx, sy = pos[0] - 12 - 60, pos[1] - 12 - 70
        area = grey[max(sy, 0):sy + tmpl.shape[0] + 140, max(sx, 0):sx + tmpl.shape[1] + 120]
        r = cv2.matchTemplate(area, tmpl, cv2.TM_CCOEFF_NORMED)
        _, score, _, loc = cv2.minMaxLoc(r)
        if score > 0.6:
            pos = (max(sx, 0) + loc[0] + 12, max(sy, 0) + loc[1] + 12)
        elif found:
            pos = found
    X, Y = pos[0] - 4, pos[1] - 4
    w0, h0 = SCREEN[2] + 8, SCREEN[3] + 8
    part = f[Y:Y + h0, X:X + w0].astype(np.float32)
    lum = part.mean(axis=2)
    # the glow is bright; heads in front of the set are dark silhouettes and stay as they are
    g = np.clip((lum - 60) / 35, 0, 1).astype(np.float32)
    rr = np.zeros((h0, w0), np.float32)
    cv2.rectangle(rr, (0, 0), (w0 - 1, h0 - 1), 1, -1)
    g = cv2.GaussianBlur(g * cv2.GaussianBlur(rr, (5, 5), 0), (3, 3), 0)[..., None]
    yy, xx = np.mgrid[0:h0, 0:w0]
    glass = 20 + np.clip(1 - (xx / w0 + yy / h0), 0, 1)[..., None] * 14 + np.array([0, 2, 0], np.float32)
    grain = (part - cv2.GaussianBlur(part, (0, 0), 1.5)) * 0.4
    out = part * (1 - g * 0.95) + (glass + grain) * g * 0.95
    f[Y:Y + h0, X:X + w0] = np.clip(out, 0, 255).astype(np.uint8)
    enc.stdin.write(f.tobytes())
enc.stdin.close()
enc.wait()
