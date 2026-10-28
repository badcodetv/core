#!/usr/bin/env python3
"""The Bank Robbery short, cut 6: the money is typed, not printed (Jack: "do this and 5").

The Bank of England's own 2009 pamphlet said of QE that "no new money will actually be printed": reserves are credited
electronically. So after the press, one key is pressed and this screen does the rest: an old bank terminal, green
phosphor on black, the amount rolling up through the zeros to the paying-in slip's £200,000,000,000 and landing on
PAID IN. Made in code, not Flow, because it has to read exactly: legible text, a number that rolls like an odometer,
scan lines, a curved glass face, bloom, a faint reflection of the work lamp, grain. No real institution is named.

usage: ~/.cache/badcode-recut/venv/bin/python screen6.py <out.mov> [seconds] [roll_start] [roll_land]
"""
import subprocess, sys
import cv2, numpy as np
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[1]
D = float(sys.argv[2]) if len(sys.argv) > 2 else 4.0
W, H, FPS = 1280, 720, 24
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
BIG, MID = ImageFont.truetype(MONO, 64), ImageFont.truetype(MONO, 34)
TARGET = 200_000_000_000
R0 = float(sys.argv[3]) if len(sys.argv) > 3 else 0.35   # the roll starts (s)
R1 = float(sys.argv[4]) if len(sys.argv) > 4 else 1.75   # and lands on PAID IN: the builder times it to the narrator's 'This lot are paying it in'
GREEN = (120, 255, 140)

def amount(t):
    if t < R0: return 0
    if t >= R1: return TARGET
    u = (t - R0) / (R1 - R0)
    return int(TARGET * (10 ** (11 * u) - 1) / (10 ** 11 - 1))   # climbs through the orders of magnitude, like an odometer

def screen(t):
    im = Image.new('L', (W, H), 0); g = ImageDraw.Draw(im)
    x = 150
    g.text((x, 120), 'TRANSFER   RESERVE ACCOUNT', font=MID, fill=170)
    g.text((x, 170), 'REF        APF/0001', font=MID, fill=170)
    g.text((x, 250), 'CREDIT', font=MID, fill=170)
    g.text((x, 300), '£ {:>19,}'.format(amount(t)), font=BIG, fill=255)
    if t >= R1:
        if int((t - R1) * 3) % 2 == 0 or t > R1 + 1.4: g.text((x, 420), 'STATUS     PAID IN', font=BIG, fill=255)
    else:
        g.text((x, 420), 'STATUS     PROCESSING' + '.' * (int(t * 6) % 4), font=MID, fill=150)
    if int(t * 2.5) % 2 == 0: g.rectangle((x, 540, x + 26, 576), fill=220)   # the cursor
    a = np.asarray(im, np.float32) / 255
    bloom = cv2.GaussianBlur(a, (0, 0), 9) * 0.9 + cv2.GaussianBlur(a, (0, 0), 3) * 0.5
    a = np.clip(a + bloom, 0, 1.3)
    a *= (0.82 + 0.18 * (np.arange(H) % 3 != 0))[:, None]                    # scan lines
    rgb = np.dstack([a * c / 255 for c in GREEN[::-1]])                       # BGR
    rgb += 0.035                                                              # the black of a lit tube is not black
    return rgb

# the tube's curved glass: barrel distortion, darker toward the corners
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
nx, ny = (xx - W / 2) / (W / 2), (yy - H / 2) / (H / 2)
r2 = nx * nx + ny * ny; k = 0.07
mapx = ((nx * (1 + k * r2)) * W / 2 + W / 2).astype(np.float32); mapy = ((ny * (1 + k * r2)) * H / 2 + H / 2).astype(np.float32)
shade = np.clip(1.05 - 0.5 * r2, 0, 1)[..., None]
glare = (np.exp(-(((xx - 0.82 * W) / 160) ** 2 + ((yy - 0.18 * H) / 90) ** 2)) * 0.12)[..., None]   # the work lamp in the glass
bezel = ((np.abs(nx * (1 + k * r2)) > 0.985) | (np.abs(ny * (1 + k * r2)) > 0.975))[..., None]

N = int(round(D * FPS)); rng = np.random.default_rng(6)
enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                        '-c:v', 'libx264', '-crf', '14', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-an', OUT + '.v.mp4'], stdin=subprocess.PIPE)
for i in range(N):
    t = i / FPS
    f = cv2.remap(screen(t).astype(np.float32), mapx, mapy, cv2.INTER_LINEAR) * shade + glare
    f *= 0.97 + 0.03 * np.sin(t * 2 * np.pi * 7.3)                            # tube flicker
    f = np.where(bezel, 0.02, f)
    f += rng.normal(0, 0.018, (H, W, 1))
    enc.stdin.write((np.clip(f, 0, 1) * 255).astype(np.uint8).tobytes())
enc.stdin.close(); enc.wait()
# sound: relay ticks while it rolls, one terminal beep as it lands
ticks = f"between(t,{R0},{R1})*0.25*sin(2*PI*1900*t)*exp(-mod(t,0.045)*400)"
beep = f"between(t,{R1},{R1 + 0.25})*0.22*sin(2*PI*1046.5*t)"
hum = "0.015*sin(2*PI*50*t)+0.01*sin(2*PI*15734*t)"
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', OUT + '.v.mp4', '-f', 'lavfi', '-i', f"aevalsrc=exprs='{ticks}+{beep}+{hum}':s=48000:d={D}",
                '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'pcm_s16le', '-ac', '2', '-t', f'{D:.3f}', OUT], check=True)
print('screen frames', N)
