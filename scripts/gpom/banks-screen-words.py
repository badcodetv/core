#!/usr/bin/env python3
"""GPOM bank takeover: draw the screen words Veo cannot write (Kai, 2026-10-19 notes), plus the
trading-floor match-cut. Clips are camera-locked, so each screen is one fixed quad, measured on frame 24.

    python3 scripts/gpom/banks-screen-words.py [laptop|board|floor|matchcut ...]

Out: clips/banks-recut/post/bk-11-laptop-words.mp4 (TRANSFERRING COMPANY FUNDS, bar filling),
bk-13-headcount-0.mp4 (HEADCOUNT 0, a Flow-edited screen pasted in), bk-14-floor-words.mp4
(TRANSFERRING MARKET FUNDS on the board) and bk-14-matchcut.mp4 (the laughing traders 1.5s, hard cut
to the same room empty). 1920x1080, 24fps, silent. Coordinates below are in the 1280x720 source.
"""
import subprocess
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

B = '/mnt/d/badcode-videos/gitpush-origin-master/clips'
V = f'{B}/banks-recut/video'
OUT = f'{B}/banks-recut/post'
W, H, FPS = 1920, 1080, 24
K = W / 1280
BOLD = '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
REG = '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'


def font(path, size):
    return ImageFont.truetype(path, size)


def frames(path, n=None):
    """Yield the clip's frames as float arrays, scaled to 1920x1080."""
    p = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-i', path, '-vf', f'scale={W}:{H}:flags=lanczos',
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    i = 0
    while n is None or i < n:
        buf = p.stdout.read(W * H * 3)
        if len(buf) < W * H * 3:
            break
        yield np.frombuffer(buf, np.uint8).reshape(H, W, 3).astype(np.float32)
        i += 1
    p.stdout.close()
    p.wait()


def writer(path):
    return subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
                             '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-vf', 'scale=in_range=full:out_range=limited', '-c:v', 'libx264', '-crf', '14',
                             '-preset', 'slow', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
                             '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
                             '-movflags', '+faststart', path], stdin=subprocess.PIPE)


def coeffs(quad, cw, ch):
    """PIL perspective coefficients mapping output pixels in `quad` back to a cw x ch card."""
    src = [(0, 0), (cw, 0), (cw, ch), (0, ch)]
    A, b = [], []
    for (x, y), (u, v) in zip(quad, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]
        b += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(b, float)).tolist()


def warp(card, quad):
    """Card (RGBA) onto the full frame at quad (1280-space corners TL, TR, BR, BL). Returns rgb, alpha."""
    q = [(x * K, y * K) for x, y in quad]
    card = card.filter(ImageFilter.GaussianBlur(1.2))  # the source is soft; razor-sharp words read as pasted on
    im = card.transform((W, H), Image.PERSPECTIVE, coeffs(q, *card.size), Image.BICUBIC)
    a = np.asarray(im, np.float32) / 255
    return a[..., :3] * 255, a[..., 3:4]


def bar(d, x, y, w, h, frac, fg, bg):
    d.rectangle([x, y, x + w, y + h], fill=bg)
    if frac > 0:
        d.rectangle([x, y, x + int(w * frac), y + h], fill=fg)


def progress(t, start=0.4, end=5.2):
    """Eased 0..1, held at 1 after `end`."""
    u = min(max((t - start) / (end - start), 0), 1)
    return 1 - (1 - u) ** 2.2


def laptop():
    """bk-11: the CEO's laptop. The screen is white and flickers, so the words multiply into it."""
    quad = [(443, 424), (642, 418), (664, 559), (446, 579)]
    cw, ch = 900, 600
    w = writer(f'{OUT}/bk-11-laptop-words.mp4')
    for i, f in enumerate(frames(f'{V}/bk-11-CE1-ef-a.mp4')):
        t = i / FPS
        p = progress(t)
        card = Image.new('RGBA', (cw, ch), (255, 255, 255, 255))
        d = ImageDraw.Draw(card)
        d.text((70, 120), 'TRANSFERRING', font=font(BOLD, 84), fill=(28, 32, 40, 255))
        d.text((70, 220), 'COMPANY FUNDS', font=font(BOLD, 84), fill=(28, 32, 40, 255))
        bar(d, 70, 380, 760, 34, p, (28, 32, 40, 255), (205, 210, 218, 255))
        d.text((70, 440), f'{int(p * 100)}%', font=font(REG, 56), fill=(60, 66, 78, 255))
        rgb, a = warp(card, quad)
        out = f * (1 - a) + f * (rgb / 255) * a
        w.stdin.write(np.clip(out, 0, 255).astype(np.uint8).tobytes())
    w.stdin.close()
    w.wait()


def board():
    """bk-13: the boardroom wall screen reads HEADCOUNT 0 (the opening's wall said -200,000).
    Kai 2026-10-20: the drawn-on version's perspective was off ("doesn't work"), so the screen is now a
    Nano Banana edit of the clip's own first frame (post/bk-13-headcount-plate.jpg, flow_edit_image cand. a:
    "change only the large dark wall-mounted screen… HEADCOUNT… 0… flat white line"), pasted over the
    locked clip through a soft mask of just the changed screen (post/bk-13-headcount-mask.png, from
    |edit - frame0| > 25, largest region, filled, dilated 10px, feathered 6px)."""
    plate = np.asarray(Image.open(f'{OUT}/bk-13-headcount-plate.jpg').convert('RGB').resize((W, H), Image.LANCZOS),
                       np.float32)
    a = np.asarray(Image.open(f'{OUT}/bk-13-headcount-mask.png').convert('L'), np.float32)[..., None] / 255
    w = writer(f'{OUT}/bk-13-headcount-0.mp4')
    for f in frames(f'{V}/bk-13-BO1-cd-b.mp4'):
        out = f * (1 - a) + plate * a
        w.stdin.write(np.clip(out, 0, 255).astype(np.uint8).tobytes())
    w.stdin.close()
    w.wait()


def floor_card(p):
    cw, ch = 1440, 500
    card = Image.new('RGBA', (cw, ch), (10, 20, 16, 255))
    d = ImageDraw.Draw(card)
    green = (70, 200, 120, 255)
    d.text((70, 90), 'TRANSFERRING MARKET FUNDS', font=font(BOLD, 76), fill=green)
    bar(d, 70, 270, 1300, 46, p, green, (24, 52, 38, 255))
    d.text((70, 350), f'{int(p * 100)}%', font=font(BOLD, 76), fill=green)
    return card


FLOOR_QUAD = [(467, 196), (820, 195), (821, 313), (467, 313)]


def floor_frames():
    for i, f in enumerate(frames(f'{V}/bk-14-FL1-ef-a.mp4')):
        rgb, a = warp(floor_card(progress(i / FPS)), FLOOR_QUAD)
        yield f * (1 - a * 0.95) + rgb * a * 0.95


def floor():
    w = writer(f'{OUT}/bk-14-floor-words.mp4')
    for f in floor_frames():
        w.stdin.write(np.clip(f, 0, 255).astype(np.uint8).tobytes())
    w.stdin.close()
    w.wait()


def matchcut():
    """The laughing traders (bulletin-v2 04-trading-floor, same camera) for 1.5s, hard cut to the empty room."""
    w = writer(f'{OUT}/bk-14-matchcut.mp4')
    for f in frames(f'{B}/bulletin-v2/cut/04-trading-floor.mp4', int(1.5 * FPS)):
        w.stdin.write(f.astype(np.uint8).tobytes())
    for f in floor_frames():
        w.stdin.write(np.clip(f, 0, 255).astype(np.uint8).tobytes())
    w.stdin.close()
    w.wait()


if __name__ == '__main__':
    jobs = {'laptop': laptop, 'board': board, 'floor': floor, 'matchcut': matchcut}
    for name in sys.argv[1:] or list(jobs):
        jobs[name]()
        print('done', name)
