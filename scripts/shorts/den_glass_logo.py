#!/usr/bin/env python3
"""The Den outro: the den's factory window steams up and the condensation clears in the shape of the BadCode logo
(Jack, 2026-11-22: "an outro where it goes onto the factory glass and the condensation spells out badcode with the logo
... like the beer one for pub quiz").

The clip is a plain real-looking window (Flow). The steam is made here so it can clear in exactly the logo's shape; the
logo is the official brand file (docs/brand/logo/badcode-stacked-reversed-2400.png), never redrawn: its alpha is the
shape that clears, and its own colours (white ring and word, red triangle) show on the clear glass.

    ~/.cache/badcode-lips/venv/bin/python scripts/shorts/den_glass_logo.py <clip.mp4> <out.mp4> \
        --in 0.5 --dur 5.0 --cx 540 --cy 900 --w 560 [--debug sheet.jpg]
"""
import argparse, pathlib, subprocess
import cv2
import numpy as np

REPO = pathlib.Path(__file__).resolve().parents[2]
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
W, H, FPS = 1080, 1920, 24
T_FOG = (0.0, 0.8)        # steam spreads over the glass
T_CLEAR = (0.8, 2.6)      # the logo's shape evaporates clear
T_DRIP = (2.1, 4.2)       # drips run down from the letters
LOGO_A = (0.3, 0.9)       # the white parts: faint while the steam clears, full by the end (the red is full throughout)
T_RESOLVE = (3.2, 3.9)    # the mark resolves into the full logo


def ease(x):
    x = min(1.0, max(0.0, x)); return x * x * (3 - 2 * x)


def frames(clip, t0, dur):
    p = subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-ss', str(t0), '-i', str(clip), '-t', str(dur + 0.2),
                        '-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}',
                        '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], capture_output=True, check=True).stdout
    fs = np.frombuffer(p, np.uint8).reshape(-1, H, W, 3)
    n = round(dur * FPS)
    if len(fs) < n:
        fs = np.concatenate([fs, np.repeat(fs[-1:], n - len(fs), 0)])
    return fs[:n]


def logo_layer(cx, cy, w):
    lg = cv2.imread(str(LOGO), cv2.IMREAD_UNCHANGED).astype(np.float32) / 255
    h = round(lg.shape[0] * w / lg.shape[1]); lg = cv2.resize(lg, (int(w), h), interpolation=cv2.INTER_AREA)
    lay = np.zeros((H, W, 4), np.float32); x0, y0 = int(cx - w / 2), int(cy - h / 2)
    lay[y0:y0 + h, x0:x0 + int(w)] = lg
    return lay


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('clip'); ap.add_argument('out')
    ap.add_argument('--in', dest='tin', type=float, default=0.0); ap.add_argument('--dur', type=float, default=5.0)
    ap.add_argument('--cx', type=float, default=540); ap.add_argument('--cy', type=float, default=900)
    ap.add_argument('--w', type=float, default=560); ap.add_argument('--fade', type=float, default=0.5)
    ap.add_argument('--debug')
    a = ap.parse_args()
    fs = frames(a.clip, a.tin, a.dur)
    rng = np.random.default_rng(11)
    lay = logo_layer(a.cx, a.cy, a.w)
    red = (lay[..., 2] > 0.5) & (lay[..., 1] < 0.4)                          # the triangle and the o's dot (BGR)
    shape = cv2.GaussianBlur((lay[..., 3] > 0.3).astype(np.float32), (0, 0), 1.2)
    shape = cv2.GaussianBlur(cv2.dilate(shape, np.ones((3, 3), np.uint8)), (0, 0), 1.5)  # the mark itself is the clear glass
    # the order the shape clears in: low-frequency noise, so it evaporates in patches, not a wipe
    nz = cv2.resize(rng.random((24, 14)).astype(np.float32), (W, H), interpolation=cv2.INTER_CUBIC)
    nz = (nz - nz.min()) / (nz.max() - nz.min())
    # steam texture: mottled, with fine bead speckle
    mott = cv2.GaussianBlur(rng.random((H // 8, W // 8)).astype(np.float32), (0, 0), 3)
    mott = cv2.resize((mott - mott.min()) / (mott.max() - mott.min()), (W, H))
    beads = (rng.random((H, W)) > 0.9965).astype(np.float32); beads = cv2.GaussianBlur(beads, (0, 0), 1.0) * 3
    # drips: from the lowest points of the mark, straight down
    ys, xs = np.where(lay[..., 3] > 0.5)
    drips = []
    for x in rng.choice(np.unique(xs), 7, replace=False):
        yb = ys[xs == x].max(); drips.append((int(x), int(yb), rng.uniform(140, 320), rng.uniform(0, 0.6)))
    enc = subprocess.Popen(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}',
                            '-r', str(FPS), '-i', '-', '-vf', 'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)',
                            '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
                            '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', a.out], stdin=subprocess.PIPE)
    sheet = []
    for i, f in enumerate(fs):
        t = i / FPS
        clear = f.astype(np.float32) / 255
        fog = cv2.GaussianBlur(clear, (0, 0), 16)
        grey = np.array([0.80, 0.80, 0.78], np.float32)
        fog = fog * 0.45 + grey * 0.55
        fog = fog * (0.9 + 0.12 * mott[..., None]) + beads[..., None] * 0.25
        fa = 0.92 * ease((t - T_FOG[0]) / (T_FOG[1] - T_FOG[0]))              # how steamed the glass is
        k = ease((t - T_CLEAR[0]) / (T_CLEAR[1] - T_CLEAR[0]))
        reveal = np.clip((k * 1.25 - nz) * 6, 0, 1) * shape                  # patches of the shape evaporate
        dm = np.zeros((H, W), np.float32)
        for x, yb, L, lag in drips:
            p = ease((t - T_DRIP[0] - lag) / (T_DRIP[1] - T_DRIP[0]))
            if p > 0:
                y1 = int(yb + L * p); cv2.line(dm, (x, yb), (x + int(3 * p), y1), 1.0, 5); cv2.circle(dm, (x + int(3 * p), y1), 6, 1.0, -1)
        dm = cv2.GaussianBlur(dm, (0, 0), 1.2)
        clr = np.clip(reveal + dm, 0, 1)
        a_fog = fa * (1 - clr)
        # a slightly darker wet rim where the steam meets the clear glass
        rim = np.clip(cv2.GaussianBlur(clr, (0, 0), 3) - clr, 0, 1) * fa * 0.35
        img = clear * (1 - a_fog[..., None]) + fog * a_fog[..., None]
        img = img * (1 - rim[..., None])
        wa = LOGO_A[0] + (LOGO_A[1] - LOGO_A[0]) * ease((t - T_RESOLVE[0]) / (T_RESOLVE[1] - T_RESOLVE[0]))
        la = lay[..., 3] * reveal * np.where(red, 0.9, wa)                     # the logo's colours, only where clear
        img = img * (1 - la[..., None]) + lay[..., :3] * la[..., None]
        d = a.dur - t
        if a.fade and d < a.fade:
            img = img * max(0.0, d / a.fade)
        o = (np.clip(img, 0, 1) * 255).astype(np.uint8)
        enc.stdin.write(o.tobytes())
        if a.debug and i % 12 == 0:
            s = cv2.resize(o, (270, 480)); cv2.putText(s, f'{t:.1f}', (8, 24), 0, 0.7, (0, 255, 255), 2); sheet.append(s)
    enc.stdin.close(); enc.wait()
    if a.debug and sheet:
        while len(sheet) % 6: sheet.append(np.zeros_like(sheet[0]))
        cv2.imwrite(a.debug, np.vstack([np.hstack(sheet[r:r + 6]) for r in range(0, len(sheet), 6)]))
    print(a.out)


if __name__ == '__main__':
    main()
