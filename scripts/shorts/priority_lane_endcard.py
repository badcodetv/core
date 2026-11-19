#!/usr/bin/env python3
"""Priority Lane: the flatline on the monitor and the flatline logo (Jack's timeline notes on rough cut 6b, 2026-11-19).

    python3 scripts/shorts/priority_lane_endcard.py

- 22:06 "Maybe show the flatline happening on here": the Flow trace clip (r20-LG, LG20-a) is warped onto the waveform
  area of the monitor still FL18-a, so the line beats and goes flat on the screen while the cut pushes in.
  -> <media>/cut-r6/flatline-screen.mp4 (the still's own size, FL_D s; the cut script pushes in on it)
- 29:06 "make the flatline part of the logo, like we have done before with other logo Netflix-style transitions": on black,
  the flat green line (at the same height as in the Flow clip, so the cut matches) carries a bright dot to the left edge
  of the ring; the line pulls in from both sides as the ring draws itself round from that point; the red triangle blips in
  with one monitor beep (the pulse coming back); a green sweep bar wipes the wordmark on, left to right, like a monitor
  trace. Every piece is the brand file's own pixels at its own place (docs/brand/README.md: moved, masked, never redrawn).
  -> <media>/cut-r6/logo-flatline.mp4 (1080x1920, LOGO_D s) and logo-beep.wav
"""
# style-lint: story=shorts/priority-lane (this short's own end card)
import json, math, pathlib, subprocess, sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

REPO = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((REPO / 'docs/stories/shorts/priority-lane/scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
OUT = MEDIA / 'cut-r6'; OUT.mkdir(parents=True, exist_ok=True)
FPS, W, H = 24, 1080, 1920
TRACE = MEDIA / 'video/pl-r20-LG-LG20-a.mp4'          # 720x1280, two last beats then flat by ~4 s; line at 0.493 H
STILL = MEDIA / 'moodboard/FL18-a.jpg'                # 768x1376
QUAD = [(316, 436), (486, 394), (486, 820), (316, 790)]  # FL18-a's waveform area: TL, TR, BR, BL (measured by eye)
FL_IN, FL_D = 1.6, 2.4                                 # which stretch of the trace plays on the monitor (a beat, then flat)
LOGO_D = 3.6                                   # 6e: the finished logo holds ~1.2 s (it held 0.45 s in 6d)
LINE_Y = round(0.493 * H)
GREEN = (60, 255, 140)

LOGO = Image.open(REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png').convert('RGBA')
LA = np.array(LOGO)
RED = (LA[..., 0] > 150) & (LA[..., 1] < 90) & (LA[..., 3] > 40)
TOP = np.zeros(LA.shape[:2], bool); TOP[:2100] = True       # ring + triangle sit above y 2100; the wordmark below 2486
S = 640 / LOGO.width                                          # resting width 640 px, as the earlier end cards
RC = (1200, 1049.5)                                           # the ring's centre in the file
X0, Y0 = W / 2 - RC[0] * S, LINE_Y - RC[1] * S                # place the logo so the ring's centre sits on the line
RING_L = X0 + 265 * S                                         # the ring's leftmost point, on the line


def frames(path, t0, d, size):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(t0), '-t', str(d), '-i', str(path), '-vf',
                          f'fps={FPS},scale={size[0]}:{size[1]}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                         capture_output=True, check=True).stdout
    n = len(raw) // (size[0] * size[1] * 3)
    return [Image.frombytes('RGB', size, raw[i * size[0] * size[1] * 3:(i + 1) * size[0] * size[1] * 3]) for i in range(n)]


def coeffs(dst, src):
    """PIL PERSPECTIVE coefficients mapping output points dst -> input points src."""
    m = []
    for (x, y), (u, v) in zip(dst, src):
        m += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]
    return np.linalg.solve(np.array(m, float), np.array([c for p in src for c in p], float)).tolist()


def write(frames_, out, size):
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{size[0]}x{size[1]}',
                          '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', str(out)],
                         stdin=subprocess.PIPE)
    for f in frames_:
        p.stdin.write(f.tobytes())
    p.stdin.close(); p.wait()


def flatline_screen():
    still = Image.open(STILL).convert('RGB')
    tw, th = 720, 1280
    # the trace's centre band (the line and its glow), so the screen shows the line large, not the whole monitor
    band = (0, int(0.32 * th), tw, int(0.68 * th))
    src = [(band[0], band[1]), (band[2], band[1]), (band[2], band[3]), (band[0], band[3])]
    c = coeffs(QUAD, src)
    mask = Image.new('L', still.size, 0); ImageDraw.Draw(mask).polygon(QUAD, fill=235)
    mask = mask.filter(ImageFilter.GaussianBlur(1.2))
    out = []
    for fr in frames(TRACE, FL_IN, FL_D, (tw, th)):
        warped = fr.transform(still.size, Image.PERSPECTIVE, c, Image.BICUBIC)
        out.append(Image.composite(warped, still, mask))
    write(out, OUT / 'flatline-screen.mp4', still.size)


def glow_line(fr, x0, x1, y, width=5):
    if x1 <= x0:
        return
    layer = Image.new('RGB', fr.size, (0, 0, 0)); d = ImageDraw.Draw(layer)
    d.line([(x0, y), (x1, y)], fill=GREEN, width=width)
    halo = layer.filter(ImageFilter.GaussianBlur(9))
    fr.paste(Image.fromarray(np.clip(np.array(fr, int) + np.array(halo, int) * 2 + np.array(layer, int), 0, 255).astype('uint8')))


def piece(mask, alpha_scale=1.0):
    a = LA.copy(); a[..., 3] = np.where(mask, a[..., 3] * alpha_scale, 0).astype('uint8')
    return Image.fromarray(a).resize((round(LOGO.width * S), round(LOGO.height * S)), Image.LANCZOS)


def ease(x):
    x = min(max(x, 0.0), 1.0); return 1 - (1 - x) ** 3


def logo_flatline():
    yy, xx = np.mgrid[0:LA.shape[0], 0:LA.shape[1]]
    ang = (np.degrees(np.arctan2(yy - RC[1], xx - RC[0])) + 360 - 180) % 360   # 0 at the ring's left point, clockwise on screen
    ring = TOP & ~RED & (LA[..., 3] > 0)
    tri = TOP & RED
    word = ~TOP & (LA[..., 3] > 0)
    words_full = piece(word)
    out = []
    n = int(LOGO_D * FPS)
    for i in range(n):
        t = i / FPS
        fr = Image.new('RGB', (W, H), (0, 0, 0))
        # 0-0.45 s: the flat line, a bright dot running to the ring's left point
        # 0.35-1.25 s: the line pulls in from both edges to that point while the ring draws round clockwise from it
        k = ease((t - 0.35) / 0.9)
        left_end, right_end = k * RING_L, W - k * (W - RING_L)
        if k < 1:
            glow_line(fr, int(left_end), int(right_end), LINE_Y)
        if t < 0.5:
            dx = RING_L * min(1, t / 0.45)
            ImageDraw.Draw(fr).ellipse([dx - 9, LINE_Y - 9, dx + 9, LINE_Y + 9], fill=(220, 255, 230))
        if k > 0:
            sweep = 360 * k
            m = ring & (ang <= sweep)
            fr.paste(piece(m), (round(X0), round(Y0)), piece(m))
        # 1.25 s: the triangle blips in (scale 1.35 -> 1 over 0.25 s), with the beep
        if t >= 1.25:
            tp = piece(tri); s = 1 + 0.35 * (1 - ease((t - 1.25) / 0.25))
            if s != 1:
                bw, bh = tp.size; big = tp.resize((round(bw * s), round(bh * s)), Image.LANCZOS)
                cx, cy = X0 + RC[0] * S, Y0 + RC[1] * S
                fr.paste(big, (round(cx - big.width * (RC[0] * S) / bw), round(cy - big.height * (RC[1] * S) / bh)), big)
            else:
                fr.paste(tp, (round(X0), round(Y0)), tp)
        # 1.55-2.35 s: a green sweep bar wipes the wordmark on, left to right
        if t >= 1.55:
            p = ease((t - 1.55) / 0.8)
            x = round(X0 + (114 + p * (2286 - 114)) * S)
            crop = words_full.crop((0, 0, max(1, x - round(X0)), words_full.height))
            fr.paste(crop, (round(X0), round(Y0)), crop)
            if p < 1:
                y0, y1 = round(Y0 + 2440 * S), round(Y0 + 2940 * S)
                glow_line(fr, x, x, 0)  # no-op keeps the helper's look consistent
                bar = Image.new('RGB', (6, y1 - y0), GREEN)
                fr.paste(bar, (x - 3, y0))
        out.append(fr)
    write(out, OUT / 'logo-flatline.mp4', (W, H))
    # the beep: one tone at 1.25 s (a monitor's pulse coming back), 0.14 s, soft attack
    sr = 48000; tt = np.arange(int(0.14 * sr)) / sr
    tone = 0.35 * np.sin(2 * math.pi * 1050 * tt) * np.minimum(1, tt / 0.005) * np.minimum(1, (0.14 - tt) / 0.03)
    wav = np.zeros(int(LOGO_D * sr), np.float32); s0 = int(1.25 * sr); wav[s0:s0 + len(tone)] = tone
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(sr), '-ac', '1', '-i', '-', '-ac', '2',
                    str(OUT / 'logo-beep.wav')], input=wav.tobytes(), check=True)


if __name__ == '__main__':
    flatline_screen()
    logo_flatline()
    print(json.dumps({'screen': str(OUT / 'flatline-screen.mp4'), 'logo': str(OUT / 'logo-flatline.mp4'), 'line_y': LINE_Y}))
