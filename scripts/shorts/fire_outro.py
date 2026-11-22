#!/usr/bin/env python3
"""Fire Sale outro: "Going, going, gone" into the mask (Kai, 2026-11-22: "do this").

The masked auctioneer (Flow clip OUTc) brings the gavel down; the camera rushes into the mask and holds. Then the mask's
white ring (an oval, measured on the clip's own frames) is squeezed into the exact place and size of the logo's ring on
the final logo card, everything outside it fades to black, and the mask dissolves into the logo card. The logo is the
brand file rendered as is (docs/brand/logo/badcode-stacked-reversed.svg, via sharp); nothing here draws or edits it.

    ~/.cache/badcode-lips/venv/bin/python scripts/shorts/fire_outro.py <out.mp4>    # 1080x1920, 24 fps, no audio

Timing (clip seconds): gavel crack 2.47 (the clip's own sound; the picture lands 2.40); ring at rest from 5.4.
"""
import json, pathlib, subprocess, sys
import cv2
import numpy as np

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((REPO / 'docs/stories/short-fire-sale/scenes/fire-sale/scene.json').read_text()))
CLIP = pathlib.Path(cfg['media']) / 'video/fire-sale-OUTc-OUT.mp4'
W, H, FPS = 1080, 1920, 24
T_MORPH0, T_MORPH1 = 5.6, 6.3      # the ring squeezes onto the logo's ring
T_DISS0, T_DISS1 = 6.05, 6.55      # the mask dissolves into the logo card
T_END = 7.7
LOGO_W = 640                       # the logo card's size (as the cut's old card: stacked logo 640 px wide, centred)
# the stacked logo's ring in its own SVG units: centre (0,0), radius 75.85 + stroke 12.3/2; viewBox -105.2 -92 210.41 263.75
VB_X, VB_Y, VB_W, VB_H, R_OUT = -105.2, -92.0, 210.41, 263.75, 75.85 + 6.15


def logo_card():
    png = pathlib.Path('/tmp') / f'fire-outro-stacked-{LOGO_W}.png'
    if not png.exists():
        subprocess.run(['node', '-e', f"require('sharp')('docs/brand/logo/badcode-stacked-reversed.svg',{{density:600}})"
                        f".resize({LOGO_W}).png().toFile('{png}')"], cwd=REPO, check=True)
    lg = cv2.imread(str(png), cv2.IMREAD_UNCHANGED).astype(np.float32) / 255
    card = np.zeros((H, W, 3), np.float32)
    h, w = lg.shape[:2]; x0, y0 = (W - w) // 2, (H - h) // 2
    a = lg[..., 3:4]
    card[y0:y0 + h, x0:x0 + w] = lg[..., :3] * a + card[y0:y0 + h, x0:x0 + w] * (1 - a)
    s = w / VB_W
    return card, (x0 - VB_X * s, y0 - VB_Y * s), R_OUT * s


def ring(fr):
    hsv = cv2.cvtColor(fr, cv2.COLOR_BGR2HSV)
    m = ((hsv[..., 2] > 150) & (hsv[..., 1] < 60)).astype(np.uint8) * 255
    m[:, :40] = 0; m[:, -40:] = 0
    cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    (cx, cy), (a, b), _ = cv2.fitEllipse(max(cs, key=cv2.contourArea))
    return cx, cy, a / 2, b / 2


def ease(x):
    x = min(1.0, max(0.0, x)); return x * x * (3 - 2 * x)


def main():
    out = sys.argv[1]
    cap = cv2.VideoCapture(str(CLIP)); sfps = cap.get(cv2.CAP_PROP_FPS)
    frames = []
    while True:
        ok, fr = cap.read()
        if not ok: break
        frames.append(fr)
    k = 1.5  # 720x1280 -> 1080x1920
    rs = np.array([ring(frames[int(t * sfps)]) for t in (5.6, 6.5, 7.5)])
    cx, cy, ax, ay = rs.mean(0) * k
    card, (lx, ly), lr = logo_card()
    print(json.dumps({'mask_ring': [round(float(v), 1) for v in (cx, cy, ax, ay)], 'logo_ring': [round(lx, 1), round(ly, 1), round(lr, 1)]}))
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    ff = subprocess.Popen(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}',
                           '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-pix_fmt', 'yuv420p',
                           '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', out],
                          stdin=subprocess.PIPE)
    for i in range(int(round(T_END * FPS))):
        t = i / FPS
        src = frames[min(len(frames) - 1, int(round(t * sfps)))]
        base = cv2.resize(src, (W, H), interpolation=cv2.INTER_CUBIC).astype(np.float32) / 255
        m = ease((t - T_MORPH0) / (T_MORPH1 - T_MORPH0))
        if m > 0:
            sx = 1 + m * (lr / ax - 1); sy = 1 + m * (lr / ay - 1)
            tx = cx + m * (lx - cx); ty = cy + m * (ly - cy)
            A = np.float32([[sx, 0, tx - sx * cx], [0, sy, ty - sy * cy]])  # ring centre -> moving centre, oval -> circle
            base = cv2.warpAffine(base, A, (W, H), flags=cv2.INTER_CUBIC, borderValue=(0, 0, 0))
            rx, ry = ax * sx, ay * sy  # outside the (moving) ring fades to black
            d = np.sqrt(((xx - tx) / rx) ** 2 + ((yy - ty) / ry) ** 2)
            keep = np.clip((1.06 - d) / 0.06, 0, 1)[..., None]
            o = ease(min(1.0, (t - T_MORPH0) / 0.22))  # the outside is dark within 0.22 s, before the frame's edge can show
            base = base * (1 - o + o * keep)
        dv = ease((t - T_DISS0) / (T_DISS1 - T_DISS0))
        frame = base * (1 - dv) + card * dv
        ff.stdin.write((np.clip(frame, 0, 1) * 255).astype(np.uint8).tobytes())
    ff.stdin.close(); ff.wait()


if __name__ == '__main__':
    main()
