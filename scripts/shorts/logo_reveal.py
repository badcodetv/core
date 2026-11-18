#!/usr/bin/env python3
"""Hello, I'm BadCode: three logo reveals for the end card (Jack, 2026-11-18, timeline note at 00:33:18: "this is where the
logo should appear, maybe make the logo appear the way the netflix logo does, but in a badcode way").

    python3 scripts/shorts/logo_reveal.py <out-dir>

Writes reveal-a.mp4 (out of the eye: start inside the red triangle, pull back to the whole logo), reveal-b.mp4 (power on: a
CRT switch-on line opens into the logo), reveal-c.mp4 (glitch in: slices settle into the logo). 1080x1920, 24 fps, 3.0 s,
each with a low thump made here (no Netflix sound, no Netflix shapes). The logo is the brand file, only moved and scaled,
never redrawn (docs/brand/README.md).
"""
# style-lint: story=short-hello-im-badcode (this script belongs to one short)
import math, pathlib, random, subprocess, sys

from PIL import Image, ImageChops

ROOT = pathlib.Path(__file__).resolve().parents[2]
LOGO = Image.open(ROOT / 'docs/brand/logo/badcode-stacked-reversed-2400.png').convert('RGBA')
W, H, FPS, D = 1080, 1920, 24, 3.0
N = int(FPS * D)
LW = 640                                   # the logo's resting width on the end card (as rough cuts 1-4)
S0 = LW / LOGO.width
EYE = (1488, 870)                          # the red triangle's centre in the 2400 px logo file


def ease(x):
    return 1 - (1 - min(max(x, 0), 1)) ** 3


def place(scale, cx, cy, alpha=1.0):
    """The logo at `scale` (of the file) with file point (cx, cy) at the frame centre."""
    img = LOGO.resize((max(1, int(LOGO.width * scale)), max(1, int(LOGO.height * scale))), Image.LANCZOS)
    fr = Image.new('RGBA', (W, H), (0, 0, 0, 255))
    x, y = int(W / 2 - cx * scale), int(H / 2 - cy * scale)
    if alpha < 1:
        img.putalpha(img.getchannel('A').point(lambda a: int(a * alpha)))
    fr.alpha_composite(img, (x, y)) if -img.width < x < W and -img.height < y < H else None
    return fr.convert('RGB')


def rest():
    return place(S0, LOGO.width / 2, LOGO.height / 2)


def reveal_a(i):
    t = i / FPS
    if t < 0.25:
        return Image.new('RGB', (W, H))
    k = ease((t - 0.25) / 1.3)
    s = S0 * 14 * (1 - k) + S0 * k                        # from deep inside the triangle to the resting size
    cx = EYE[0] * (1 - k) + LOGO.width / 2 * k
    cy = EYE[1] * (1 - k) + LOGO.height / 2 * k
    return place(s, cx, cy)


def reveal_b(i):
    t = i / FPS
    base = rest()
    if t < 0.3:
        return Image.new('RGB', (W, H))
    k = ease((t - 0.3) / 0.6)
    h = max(2, int(H * k))
    fr = Image.new('RGB', (W, H))
    band = base.resize((W, h)) if k < 1 else base
    fr.paste(band, (0, (H - h) // 2))
    if k < 1:                                              # the bright switch-on line
        line = Image.new('RGB', (int(W * (0.3 + 0.7 * k)), 4), (235, 240, 245))
        fr.paste(line, ((W - line.width) // 2, H // 2 - 2))
    return fr


def reveal_c(i):
    t = i / FPS
    base = rest()
    if t < 0.25:
        return Image.new('RGB', (W, H))
    if t > 1.15:
        return base
    random.seed(int(t * 6))                                # the slices jump 6 times a second, not every frame
    fr = base.copy()
    amt = 1 - (t - 0.25) / 0.9
    for _ in range(9):
        y = random.randrange(H // 2 - 500, H // 2 + 500)
        h = random.randrange(10, 70)
        dx = int(random.uniform(-140, 140) * amt)
        strip = base.crop((0, y, W, y + h))
        fr.paste(strip, (dx, y))
    r, g, b = fr.split()
    off = int(18 * amt)
    return Image.merge('RGB', (ImageChops.offset(r, off, 0), g, ImageChops.offset(b, -off, 0)))


def thump(out, at):
    # A low thump at the reveal: a 55 Hz sine falling to 38 Hz, fast attack, 1.4 s decay. Made here, no sample.
    expr = f"if(gte(t,{at}),sin(2*PI*(55-17*min((t-{at})/1.4,1))*(t-{at}))*exp(-3*(t-{at})),0)"
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'lavfi', '-i', f"aevalsrc='{expr}':s=48000:d={D}",
                    '-af', 'volume=0.9,aformat=channel_layouts=stereo', str(out)], check=True)


def render(fn, out, at):
    p = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                          '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt',
                          'yuv420p', str(out.with_suffix('.v.mp4'))], stdin=subprocess.PIPE)
    for i in range(N):
        p.stdin.write(fn(i).tobytes())
    p.stdin.close(); p.wait()
    wav = out.with_suffix('.wav'); thump(wav, at)
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(out.with_suffix('.v.mp4')), '-i', str(wav), '-c:v', 'copy',
                    '-c:a', 'aac', '-b:a', '192k', '-shortest', str(out)], check=True)
    out.with_suffix('.v.mp4').unlink(); wav.unlink()


if __name__ == '__main__':
    o = pathlib.Path(sys.argv[1]); o.mkdir(parents=True, exist_ok=True)
    for name, fn, at in (('a', reveal_a, 1.4), ('b', reveal_b, 0.3), ('c', reveal_c, 1.15)):
        render(fn, o / f'reveal-{name}.mp4', at); print(o / f'reveal-{name}.mp4')
