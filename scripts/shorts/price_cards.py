#!/usr/bin/env python3
"""Handwritten prices drawn onto blank paper cards in a locked-off clip; the price changes in the wake of whatever passes over it.

    python3 scripts/shorts/price_cards.py <clip.mp4> <out.mp4> <spec.json>

Jack, 2026-11-18 (The Malevolent Force): "have the prices labels blanks and change the prices in the edit instead of in
flow, so that we can have the hand go over the prices and as the hand goes over it the prices change". The clip is
animated from a still whose cards are blank. This draws each card's price in marker, warped to the card's four corners,
and keys the ink by the paper's own brightness, so a dark hand passing over the card hides it. From a state's `from`
time, every part of the card the hand has covered shows the NEW price (it changes in the hand's wake); at `settle`, any
part the hand never touched fades over in `fade` seconds, so nothing is left half-changed.

spec.json:
  {"font": "scripts/shorts/fonts/PermanentMarker-Regular.ttf", "key": 150,
   "cards": [{"quad": [[x,y] TL, TR, BR, BL],            # on the 720x1280 clip
              "states": [{"text": "50p"},
                         {"text": "£5", "from": 1.8, "settle": 4.6, "fade": 0.25}]},
             {"quad": [...], "states": [{"text": "10p"}, {"text": "10p", "strike": true, "add": "£12", "from": 2.0, "settle": 4.4}]}]}
"strike" crosses the text out; "add" writes a second price beside it, as a shopkeeper would.
"""
# Words are ffmpeg/post (scene-animation skill): never ask the video model for readable text.
import json, pathlib, subprocess, sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

REPO = pathlib.Path(__file__).resolve().parents[2]
W, H, FPS = 720, 1280, 24
INK = np.array([26, 26, 32], float)
CW, CH = 600, 360  # flat card canvas before warping


def coeffs(src, dst):
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]
        B += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(B, float)).tolist()


def flat_card(state, font_path):
    im = Image.new('L', (CW, CH), 0)
    d = ImageDraw.Draw(im)
    main, add = state['text'], state.get('add')
    box_w, size = (CW * 0.32 if add else CW * 0.8), 260
    while size > 20:
        f = ImageFont.truetype(font_path, size)
        l, t, r, b = d.textbbox((0, 0), main, font=f)
        if r - l <= box_w and b - t <= CH * 0.7:
            break
        size -= 6
    l, t, r, b = d.textbbox((0, 0), main, font=f)
    x, y = CW * (0.27 if add else 0.5) - (r - l) / 2 - l, CH / 2 - (b - t) / 2 - t
    d.text((x, y), main, font=f, fill=255)
    if state.get('strike'):
        d.line([(x + l - 8, y + t + (b - t) * 0.62), (x + r + 8, y + t + (b - t) * 0.38)], fill=255, width=max(6, size // 12))
    if add:  # the new price, bigger, with clear space after the struck one
        s2 = int(size * 1.15)
        while s2 > 20:
            f2 = ImageFont.truetype(font_path, s2)
            l2, t2, r2, b2 = d.textbbox((0, 0), add, font=f2)
            if r2 - l2 <= CW * 0.36 and b2 - t2 <= CH * 0.7:
                break
            s2 -= 6
        d.text((CW * 0.74 - (r2 - l2) / 2 - l2, CH / 2 - (b2 - t2) / 2 - t2), add, font=f2, fill=255)
    return im


def ink(state, quad, font_path):
    """The state's ink as a float alpha (0-1) on the full frame, warped to the card, softened like marker on paper."""
    q = np.array(quad, float); c = q.mean(0); q = c + (q - c) * 0.9
    im = flat_card(state, font_path).transform((W, H), Image.PERSPECTIVE, coeffs([(0, 0), (CW, 0), (CW, CH), (0, CH)], [tuple(p) for p in q]), Image.BICUBIC)
    return np.asarray(im.filter(ImageFilter.GaussianBlur(0.8)), float) / 255 * 0.92


def frames(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-vf', f'scale={W}:{H},fps={FPS},format=rgb24', '-f', 'rawvideo', '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)


def main():
    clip, out, spec_path = sys.argv[1:4]
    spec = json.loads(pathlib.Path(spec_path).read_text())
    font = str(REPO / spec.get('font', 'scripts/shorts/fonts/PermanentMarker-Regular.ttf'))
    key = spec.get('key', 150)
    fr = frames(clip)
    cards = []
    for c in spec['cards']:
        m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).polygon([tuple(p) for p in c['quad']], fill=255)
        cards.append({'mask': np.asarray(m, bool), 'inks': [ink(s, c['quad'], font) for s in c['states']], 'states': c['states'],
                      'covered': [np.zeros((H, W), bool) for _ in c['states']]})
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-crf', '14', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
    report = []
    for i, f in enumerate(fr):
        t = i / FPS
        img = f.astype(float)
        lum = img @ [0.299, 0.587, 0.114]
        paper = np.clip((lum - key) / 25 + 0.5, 0, 1)            # soft key: paper shows ink, the hand hides it
        dark = lum < key
        for c in cards:
            alpha = c['inks'][0].copy()
            for si in range(1, len(c['states'])):
                st = c['states'][si]
                if t < st['from']:
                    continue
                cov = c['covered'][si]
                cov |= dark & c['mask']                            # every pixel the hand has passed over, from `from`
                share = np.asarray(Image.fromarray((cov * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(9)), float) / 255
                if t >= st.get('settle', 1e9):
                    share = np.maximum(share, min(1.0, (t - st['settle']) / st.get('fade', 0.25)))
                alpha = alpha * (1 - share) + c['inks'][si] * share
            a = (alpha * paper)[..., None]
            img = img * (1 - a) + INK * a
        enc.stdin.write(np.clip(img, 0, 255).astype(np.uint8).tobytes())
    for c in cards:
        for si in range(1, len(c['states'])):
            report.append(f"{c['states'][si]['text']}: hand covered {c['covered'][si][c['mask']].mean():.0%} of the card")
    enc.stdin.close(); enc.wait()
    print(json.dumps({'out': out, 'frames': len(fr), 'wake': report}))


if __name__ == '__main__':
    main()
