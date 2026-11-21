#!/usr/bin/env python3
"""The Retreat: a meditative logo outro. The logo file is never edited, only revealed and moved.

    python3 scripts/shorts/retreat_logo.py <out.mp4> [--dur 5.0]

On a warm dusk background (the sunset's colours going dark): the ring draws itself slowly clockwise like one long out
breath, the triangle glows in, then the whole mark breathes (a slow, small swell and settle) while the name fades in.
Sound: a singing-bowl tone made in ffmpeg (sine partials with a long decay), struck once as the ring starts and once,
softer, as the triangle lands. Uses docs/brand/logo/badcode-stacked-reversed-2400.png (transparent, white and red).
"""
# style-lint: story=short-the-retreat
import argparse, math, pathlib, subprocess, tempfile
import numpy as np
from PIL import Image

REPO = pathlib.Path(__file__).resolve().parents[2]
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
W, H, FPS = 1080, 1920, 24
CX, CY, R = 1200, 1050, 1087        # ring centre and outer radius in the logo file
MARK_BOTTOM, NAME_TOP = 1985, 2486  # mark rows end / name rows start in the logo file


def ease(x):
    x = min(1.0, max(0.0, x)); return x * x * (3 - 2 * x)


def background():
    y = np.linspace(0, 1, H)[:, None]
    top, bottom = np.array([58, 34, 22]), np.array([8, 6, 6])  # dusk amber to near black
    g = top * (1 - y) ** 1.4 + bottom * (1 - (1 - y) ** 1.4)
    return np.repeat(g[:, None, :], W, axis=1).reshape(H, W, 3)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('out'); ap.add_argument('--dur', type=float, default=5.0); a = ap.parse_args()
    logo = np.array(Image.open(LOGO).convert('RGBA')).astype(np.float32) / 255
    hgt, wid = logo.shape[:2]
    yy, xx = np.mgrid[0:hgt, 0:wid]
    ang = (np.degrees(np.arctan2(xx - CX, -(yy - CY))) + 360) % 360  # 0 at the top, clockwise
    rgb, al = logo[..., :3], logo[..., 3]
    red = (rgb[..., 0] > 0.6) & (rgb[..., 1] < 0.45)
    is_mark = yy < MARK_BOTTOM + 40
    tri = red & is_mark
    ring = is_mark & ~tri
    name = yy >= NAME_TOP - 40
    bg = background()
    scale0 = 560 / wid  # logo width on screen
    n = int(a.dur * FPS)
    with tempfile.TemporaryDirectory() as td:
        for f in range(n):
            t = f / FPS
            draw = ease(t / 1.8) * 360.0                      # ring draws over 1.8 s
            ring_a = (ang <= draw).astype(np.float32) if draw < 360 else np.ones_like(al)
            tri_a = ease((t - 1.7) / 0.7)
            name_a = ease((t - 2.4) / 0.9)
            m = al * (ring * ring_a + tri * tri_a + name * name_a)
            breathe = 1 + 0.02 * math.sin(2 * math.pi * max(0.0, t - 1.8) / 3.2)  # one slow breath
            s = scale0 * breathe
            lw, lh = int(wid * s), int(hgt * s)
            layer = np.dstack([rgb, m])
            im = Image.fromarray((layer * 255).astype(np.uint8), 'RGBA').resize((lw, lh), Image.LANCZOS)
            frame = Image.fromarray(bg.astype(np.uint8), 'RGB')
            frame.paste(im, ((W - lw) // 2, int(H * 0.47 - lh / 2)), im)
            frame.save(f'{td}/f{f:04d}.png')
        bowl = (f"sine=f=220:d={a.dur},volume=0.5[a];sine=f=440.6:d={a.dur},volume=0.25[b];sine=f=661.9:d={a.dur},volume=0.12[c];"
                f"[a][b][c]amix=inputs=3:normalize=0,afade=t=in:d=0.02,volume='exp(-t/1.6)':eval=frame,asplit[s1][s2];"
                f"[s2]adelay=1700|1700,volume=0.45[s2d];[s1][s2d]amix=inputs=2:normalize=0,atrim=end={a.dur},volume=0.6,aformat=channel_layouts=stereo[o]")
        subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', '-framerate', str(FPS), '-i', f'{td}/f%04d.png',
                        '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-filter_complex', bowl.replace('[a];', '[a];', 1),
                        '-map', '0:v', '-map', '[o]', '-t', str(a.dur), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
                        '-pix_fmt', 'yuv420p', '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709',
                        '-color_trc', 'bt709', '-c:a', 'aac', '-b:a', '192k', a.out], check=True)
    print(a.out)


if __name__ == '__main__':
    main()
