#!/usr/bin/env python3
"""Hello, I'm BadCode: three logo reveals for the end card (Jack, 2026-11-18, timeline note at 00:33:18: "this is where the
logo should appear, maybe make the logo appear the way the netflix logo does, but in a badcode way").

    python3 scripts/shorts/logo_reveal.py <out-dir>

Round 2 (Jack, 2026-11-18, picks note: "all of the letters are somewhat circular so make them roll also make a few of these
that vary and are interesting"): reveal-d (the letters roll in like wheels, then the ring), reveal-e (the red-dot o rolls
across first and each letter pops up as it passes), reveal-f (the ring appears and the red triangle glances round inside it
like an eye before snapping home), reveal-g (the ring spins like a dial, the triangle orbiting, and lands as the letters
roll in). These move the logo's own pieces (ring, triangle, each letter, cut from the brand file by position and colour);
every piece ends exactly where the file has it.

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


# ---- round 2: the logo's own pieces, moved ------------------------------------------------------------------------------
RING_BAND, WORD_BAND = (114, 1985), (2486, 2895)
LETTERS = [(113, 403), (435, 725), (756, 1045), (1077, 1330), (1355, 1644), (1676, 1966), (1997, 2287)]
OX, OY = W / 2 - LOGO.width * S0 / 2, H / 2 - LOGO.height * S0 / 2     # the logo's top-left at rest, in frame pixels


def _piece(box, keep=None):
    c = LOGO.crop(box)
    if keep:
        px = c.load()
        for y in range(c.height):
            for x in range(c.width):
                r, g, b, a = px[x, y]
                if a and not keep(r, g, b):
                    px[x, y] = (0, 0, 0, 0)
    c = c.resize((max(1, int(c.width * S0)), max(1, int(c.height * S0))), Image.LANCZOS)
    return c, (OX + box[0] * S0, OY + box[1] * S0)


RED = lambda r, g, b: r > 150 and g < 110
RING, RING_AT = _piece((0, RING_BAND[0], LOGO.width, RING_BAND[1] + 1), lambda r, g, b: not RED(r, g, b))
TRI, TRI_AT = _piece((0, RING_BAND[0], LOGO.width, RING_BAND[1] + 1), RED)
LET = [_piece((x0, WORD_BAND[0], x1 + 1, WORD_BAND[1] + 1)) for x0, x1 in LETTERS]
LR = LET[0][0].height / 2                                                 # a letter's rolling radius


def _canvas():
    return Image.new('RGBA', (W, H), (0, 0, 0, 255))


def _put(fr, img, at, angle=0.0, scale=1.0):
    if scale != 1.0:
        img = img.resize((max(1, int(img.width * scale)), max(1, int(img.height * scale))), Image.LANCZOS)
    if angle:
        img = img.rotate(angle, resample=Image.BICUBIC, expand=True)
    cx, cy = at
    fr.alpha_composite(img, (int(cx - img.width / 2), int(cy - img.height / 2)))


def _centre(piece):
    img, (x, y) = piece
    return x + img.width / 2, y + img.height / 2


def _letters(fr, t, start, gap, travel, frm=1):
    """Each letter rolls in from `frm` (1 = from the right) over `travel` px, landing in order."""
    for i, piece in enumerate(LET):
        k = ease((t - start - i * gap) / 0.55)
        if k <= 0:
            continue
        cx, cy = _centre(piece)
        d = travel * (1 - k)
        _put(fr, piece[0], (cx + frm * d, cy), angle=math.degrees(frm * d / LR))


def reveal_d(i):
    t, fr = i / FPS, _canvas()
    _letters(fr, t, 0.2, 0.12, 900)
    k = ease((t - 1.25) / 0.7)
    if k > 0:
        cx, cy = _centre((RING, RING_AT)); d = -1200 * (1 - k); r = RING.width / 2
        _put(fr, RING, (cx + d, cy), angle=math.degrees(-d / r))
    k = (t - 2.0) / 0.25
    if k > 0:
        s = 1 + 0.25 * math.sin(min(k, 1) * math.pi)            # the triangle pops in with a small overshoot
        _put(fr, TRI, _centre((TRI, TRI_AT)), scale=min(1.0, k) * s if k < 1 else 1.0)
    return fr.convert('RGB')


def reveal_e(i):
    t, fr = i / FPS, _canvas()
    dot = LET[4][0]; dcx, dcy = _centre(LET[4])
    far = _centre(LET[6])[0] + LET[6][0].width / 2 + 60             # past the last letter
    if t < 1.15:                                                     # the red-dot o rolls in from the left, past every letter
        x = -150 + (far + 150) * ease((t - 0.2) / 0.95)
    else:                                                            # ...then rolls back into its own place
        x = far + (dcx - far) * ease((t - 1.15) / 0.4)
    reach = x if t < 1.15 else far
    if t > 0.2:
        _put(fr, dot, (x, dcy), angle=math.degrees(-(x - dcx) / LR))
    for j, piece in enumerate(LET):
        if j == 4:
            continue
        cx, cy = _centre(piece)
        pop = min(1.0, max(0.0, (reach + 40 - (cx - piece[0].width / 2)) / 120))
        s = pop * (1 + 0.18 * math.sin(pop * math.pi))
        if s > 0.02:
            _put(fr, piece[0], (cx, cy + (1 - pop) * 40), scale=s)
    k = (t - 1.6) / 0.45
    if k > 0:
        y0 = _centre((RING, RING_AT))[1]
        b = ease(min(k, 1)); bounce = 30 * math.sin(min(k * 1.6, 1) * math.pi) * (1 - min(k, 1))
        _put(fr, RING, (W / 2, y0 - 900 * (1 - b) - bounce))
    if t > 2.15:
        _put(fr, TRI, _centre((TRI, TRI_AT)))
    return fr.convert('RGB')


def reveal_f(i):
    t, fr = i / FPS, _canvas()
    a = min(1.0, max(0.0, (t - 0.15) / 0.4))
    if a > 0:
        r = RING.copy(); r.putalpha(r.getchannel('A').point(lambda v: int(v * a))); _put(fr, r, _centre((RING, RING_AT)))
        for piece in LET:
            l = piece[0].copy(); l.putalpha(l.getchannel('A').point(lambda v: int(v * a))); _put(fr, l, _centre(piece))
    home = _centre((TRI, TRI_AT)); rc = _centre((RING, RING_AT))
    look = [(0.7, (rc[0] - 130, rc[1] + 40)), (1.15, (rc[0] - 120, rc[1] + 40)), (1.35, (rc[0] + 20, rc[1] + 140)),
            (1.75, (rc[0] + 30, rc[1] + 140)), (1.95, home)]           # glance left, glance down, look at you
    if t >= 0.6:
        pos = look[0][1]
        for (t0, p0), (t1, p1) in zip(look, look[1:]):
            if t0 <= t <= t1:
                k = ease((t - t0) / (t1 - t0)); pos = (p0[0] + (p1[0] - p0[0]) * k, p0[1] + (p1[1] - p0[1]) * k)
            elif t > t1:
                pos = p1
        _put(fr, TRI, pos)
    return fr.convert('RGB')


def reveal_g(i):
    t, fr = i / FPS, _canvas()
    k = ease((t - 0.2) / 1.6)
    if t > 0.2:
        rc = _centre((RING, RING_AT)); home = _centre((TRI, TRI_AT))
        spin = 720 * (1 - k)                                       # two turns, slowing onto its spot
        a = math.radians(spin); dx, dy = home[0] - rc[0], home[1] - rc[1]
        pos = (rc[0] + dx * math.cos(a) + dy * math.sin(a), rc[1] - dx * math.sin(a) + dy * math.cos(a))
        _put(fr, RING, rc, scale=0.6 + 0.4 * k)
        _put(fr, TRI, (rc[0] + (pos[0] - rc[0]) * (0.6 + 0.4 * k), rc[1] + (pos[1] - rc[1]) * (0.6 + 0.4 * k)), angle=spin)
    _letters(fr, t, 1.0, 0.09, 700, frm=-1)
    return fr.convert('RGB')


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
    which = sys.argv[2:] or ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for name, fn, at in (('a', reveal_a, 1.4), ('b', reveal_b, 0.3), ('c', reveal_c, 1.15), ('d', reveal_d, 2.0),
                         ('e', reveal_e, 2.15), ('f', reveal_f, 1.95), ('g', reveal_g, 1.8)):
        if name not in which:
            continue
        render(fn, o / f'reveal-{name}.mp4', at); print(o / f'reveal-{name}.mp4')
