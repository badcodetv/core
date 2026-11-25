#!/usr/bin/env python3
"""Karen cut r7: the Times Square clip (Flow, locked-off) with its headline band made clean.

Kai (r6 note at7305) asked for Times Square to be made in Flow, not skewed over; Flow made the scene, the crowd watching the
screen, but garbles the last letters where the band wraps round the building corner. The band faces the camera square-on
and the camera never moves, so a flat band is painted over its straight front (same red, same place, slight blur and grain
to sit in the picture) with the headline set in type. Writes clips/r6/post/times-r7.mp4.

    python3 scripts/karen/times-band-r7.py
"""
import pathlib, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
K = pathlib.Path('/mnt/d/badcode-videos/karen-story')
SRC = K / 'clips/r6/video/r6-r7times-timessq3-a.mp4'
OUT = K / 'clips/r6/post/times-r7.mp4'
TEXT = 'PRESIDENT SACKED ON LIVE TV BY SEAN AI'
tmp = OUT.with_suffix('.png')
fr = OUT.with_suffix('.frame.png')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', '1', '-i', SRC, '-frames:v', '1', fr], check=True)
a = np.asarray(Image.open(fr).convert('RGB')).astype(int)
H, W, _ = a.shape
red = (a[..., 0] > 140) & (a[..., 1] < 70) & (a[..., 2] < 80)
ys = [y for y in range(H) if red[y].sum() > W * 0.3]
y0, y1 = ys[0] - 1, ys[-1] + 2
cols = red[y0:y1].sum(0)
xs = [x for x in range(W) if cols[x] > (y1 - y0) * 0.5]
x0, x1 = xs[0] - 1, xs[-1] + 20            # the straight front, and the start of the corner
col = tuple(int(c) for c in np.median(a[y0 + 4:y1 - 4, x0 + 4:x0 + 30].reshape(-1, 3), 0))
s = 4                                        # draw big, then shrink (clean edges)
im = Image.new('RGBA', (W * s, H * s), (0, 0, 0, 0))
d = ImageDraw.Draw(im)
bh = (y1 - y0) * s
d.polygon([(x0 * s, y0 * s), (x1 * s, y0 * s), ((x1 + 24) * s, (y0 + 18) * s), ((x1 + 24) * s, (y1 + 18) * s), (x1 * s, y1 * s), (x0 * s, y1 * s)],
          fill=col + (255,))
d.polygon([(x1 * s, y0 * s), ((x1 + 24) * s, (y0 + 18) * s), ((x1 + 24) * s, (y1 + 18) * s), (x1 * s, y1 * s)], fill=tuple(int(c * 0.72) for c in col) + (255,))
f = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf', 10)
size = 10
while True:
    f2 = ImageFont.truetype('/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf', size + 2)
    bb = d.textbbox((0, 0), TEXT, font=f2)
    if bb[2] - bb[0] > (x1 - x0 - 34) * s or bb[3] - bb[1] > bh * 0.56:
        break
    size += 2; f = f2
bb = d.textbbox((0, 0), TEXT, font=f)
tx = x0 * s + ((x1 - x0) * s - (bb[2] - bb[0])) / 2 - bb[0]
ty = y0 * s + (bh - (bb[3] - bb[1])) / 2 - bb[1]
d.text((tx, ty), TEXT, font=f, fill=(246, 242, 236, 255))
im = im.resize((W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.7))
im.save(tmp)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', SRC, '-i', tmp, '-filter_complex',
                '[0:v][1:v]overlay=0:0,noise=alls=6:allf=t,scale=1920:1080:flags=lanczos,fps=24[v]', '-map', '[v]', '-an',
                '-c:v', 'libx264', '-crf', '17', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', OUT], check=True)
subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve().parents[1] / 'provenance/prov.py'), 'card', str(OUT), '--kind', 'video',
                '--engine', 'ffmpeg', '--tool', 'scripts/karen/times-band-r7.py', '--parent', str(SRC), '--why',
                "Kai r6 note at7305: Times Square made in Flow; the band's garbled letters replaced by a flat band with the headline set in type"],
               capture_output=True)
print(OUT, (x0, y0, x1, y1), col, size)
