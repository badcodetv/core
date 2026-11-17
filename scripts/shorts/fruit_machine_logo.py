#!/usr/bin/env python3
"""The BadCode logo landing like a pub fruit machine (True Scale end card, 2026-11-16).

    python3 scripts/shorts/fruit_machine_logo.py <out.mp4> [--seconds 4.2] [--w 1080 --h 1920 --fps 24]

Jack, 2026-11-16: "put the badcode logo after, animate it like a pub fruit machine but the name and logo instead".
Three reels spin through plain fruit-machine symbols (7, BAR, cherries, bell, drawn here) and stop one by one, left to
right, on the logo's three parts: the mark | "bad" | "code" (cut from the official files in docs/brand/logo/, never
redrawn: the letters are the logo's own), on dark reels (the logo files are the reversed, light version). Then the window
frame and the bulbs blink (2 a second, under the 3/s flash
limit), and it holds. Cabinet colours are invented here; the logo keeps its own colours.
"""
import argparse, math, pathlib, subprocess, tempfile

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

REPO = pathlib.Path(__file__).resolve().parents[2]
LOGO = REPO / 'docs/brand/logo'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


def logo_parts():
    st = Image.open(LOGO / 'badcode-stacked-reversed-2400.png').convert('RGBA')
    mark = st.crop((0, 100, st.width, 2000)); mark = mark.crop(mark.getbbox())
    wm = Image.open(LOGO / 'badcode-wordmark-reversed-2400.png').convert('RGBA')
    bad = wm.crop((40, 0, 1050, wm.height)); bad = bad.crop(bad.getbbox())
    code = wm.crop((1060, 0, wm.width, wm.height)); code = code.crop(code.getbbox())
    return mark, bad, code


def fit(im, w, h):
    s = min(w / im.width, h / im.height)
    return im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.LANCZOS)


def symbol(kind, cw, ch, font):
    c = Image.new('RGBA', (cw, ch), (0, 0, 0, 0)); d = ImageDraw.Draw(c)
    if kind == '7':
        d.text((cw / 2, ch / 2), '7', font=font, fill=(214, 40, 40), anchor='mm', stroke_width=6, stroke_fill=(250, 210, 60))
    elif kind == 'BAR':
        d.rounded_rectangle((cw * .12, ch * .36, cw * .88, ch * .64), 14, fill=(60, 60, 64), outline=(250, 210, 60), width=6)
        d.text((cw / 2, ch / 2), 'BAR', font=ImageFont.truetype(BOLD, int(ch * .17)), fill=(250, 210, 60), anchor='mm')
    elif kind == 'cherry':
        d.line((cw * .5, ch * .25, cw * .38, ch * .55), fill=(40, 140, 40), width=8)
        d.line((cw * .5, ch * .25, cw * .64, ch * .58), fill=(40, 140, 40), width=8)
        for x, y in ((.36, .62), (.64, .64)):
            d.ellipse((cw * x - ch * .11, ch * y - ch * .11, cw * x + ch * .11, ch * y + ch * .11), fill=(200, 20, 40))
    elif kind == 'bell':
        d.pieslice((cw * .28, ch * .26, cw * .72, ch * .78), 180, 360, fill=(240, 190, 40))
        d.rectangle((cw * .28, ch * .52, cw * .72, ch * .66), fill=(240, 190, 40))
        d.ellipse((cw * .46, ch * .64, cw * .54, ch * .72), fill=(170, 120, 20))
    return c


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('out'); ap.add_argument('--seconds', type=float, default=4.2)
    ap.add_argument('--w', type=int, default=1080); ap.add_argument('--h', type=int, default=1920); ap.add_argument('--fps', type=int, default=24)
    a = ap.parse_args(); W, H, FPS = a.w, a.h, a.fps
    mark, bad, code = logo_parts()
    cw, ch = int(W * 0.27), int(W * 0.36)  # reel cell
    gap = int(W * 0.025); x0 = (W - (3 * cw + 2 * gap)) // 2; y0 = int(H * 0.40)
    font = ImageFont.truetype(BOLD, int(ch * .55))
    sym = {k: symbol(k, cw, ch, font) for k in ('7', 'BAR', 'cherry', 'bell')}
    # "bad" and "code" share one scale (the name stays one size); the mark is sized to the name's height x 2.6
    s = min(cw * .86 / bad.width, cw * .86 / code.width, ch * .62 / bad.height, ch * .62 / code.height)
    sized = [fit(mark, cw * .86, bad.height * s * 2.6)] + [w.resize((int(w.width * s), int(w.height * s)), Image.LANCZOS) for w in (bad, code)]
    targets = []
    for f in sized:
        c = Image.new('RGBA', (cw, ch), (0, 0, 0, 0))
        c.paste(f, ((cw - f.width) // 2, (ch - f.height) // 2), f); targets.append(c)
    order = ['7', 'cherry', 'BAR', 'bell', 'cherry', '7', 'bell', 'BAR']
    strips = []
    for r in range(3):
        cells = [sym[order[(i + 3 * r) % len(order)]] for i in range(14)] + [targets[r]] + [sym[order[(r + 1) % len(order)]]]
        s = Image.new('RGBA', (cw, ch * len(cells)), (12, 12, 14, 255))  # dark reels: the logo is the reversed (light) version
        for i, cell in enumerate(cells): s.paste(cell, (0, i * ch), cell)
        strips.append(s)
    stop = [1.2, 1.75, 2.3]; spin_from = 0.15; total_cells = 14  # the target sits at cell 14
    # cabinet
    base = Image.new('RGB', (W, H), (5, 6, 7)); d = ImageDraw.Draw(base)
    cab = (x0 - int(W * .07), y0 - int(H * .09), x0 + 3 * cw + 2 * gap + int(W * .07), y0 + ch + int(H * .09))
    d.rounded_rectangle(cab, 40, fill=(120, 14, 22), outline=(210, 170, 70), width=10)
    d.rounded_rectangle((x0 - 18, y0 - 18, x0 + 3 * cw + 2 * gap + 18, y0 + ch + 18), 18, fill=(15, 12, 10), outline=(230, 220, 200), width=6)
    bulbs = []
    for i in range(14):
        tx = cab[0] + 40 + i * (cab[2] - cab[0] - 80) / 13
        bulbs += [(tx, cab[1] + 26), (tx, cab[3] - 26)]
    n = int(round(a.seconds * FPS)); tmp = pathlib.Path(tempfile.mkdtemp())
    for k in range(n):
        t = k / FPS; im = base.copy(); dd = ImageDraw.Draw(im)
        won = t >= stop[2] + 0.15
        blink = won and int((t - stop[2]) * 4) % 2 == 0  # 2 on-off cycles a second
        for i, (bx, by) in enumerate(bulbs):
            on = blink if won else (i + int(t * 6)) % 3 == 0
            dd.ellipse((bx - 11, by - 11, bx + 11, by + 11), fill=(255, 225, 120) if on else (90, 60, 30))
        for r in range(3):
            if t < spin_from: pos = 0.0
            elif t >= stop[r]: pos = float(total_cells)
            else:
                u = (t - spin_from) / (stop[r] - spin_from)
                pos = total_cells * (1 - (1 - u) ** 2.2)  # fast, easing to the stop
            speed = 0 if t >= stop[r] else total_cells * 2.2 * (1 - (t - spin_from) / (stop[r] - spin_from)) ** 1.2 / (stop[r] - spin_from) if t >= spin_from else 0
            off = int(pos * ch); win = strips[r].crop((0, off, cw, off + ch))
            if speed > 6: win = win.filter(ImageFilter.BoxBlur(0)).resize((cw, ch)).filter(ImageFilter.GaussianBlur((0, min(30, speed * 1.2)))) if False else win.filter(ImageFilter.GaussianBlur(min(14, speed * 0.6)))
            bounce = int(math.sin(min(1, (t - stop[r]) / 0.18) * math.pi) * ch * 0.04) if stop[r] <= t < stop[r] + 0.18 else 0
            if bounce: win = strips[r].crop((0, off - bounce, cw, off - bounce + ch))
            im.paste(win.convert('RGB'), (x0 + r * (cw + gap), y0))
        if won:  # the window frame flashes gold with the bulbs (2 a second)
            dd.rounded_rectangle((x0 - 18, y0 - 18, x0 + 3 * cw + 2 * gap + 18, y0 + ch + 18), 18,
                                 outline=(255, 215, 90) if blink else (230, 220, 200), width=10 if blink else 6)
        im.save(tmp / f'{k:04d}.png')
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-framerate', str(FPS), '-i', str(tmp / '%04d.png'), '-vf',
                    'scale=in_range=full:out_range=limited,format=yuv420p,lutyuv=y=clip(val\\,20\\,235)', '-c:v', 'libx264',
                    '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv', '-colorspace', 'bt709',
                    '-color_primaries', 'bt709', '-color_trc', 'bt709', a.out], check=True)
    print(a.out)


if __name__ == '__main__':
    main()
