#!/usr/bin/env python3
"""The Starting Gate outro: a photo finish (Jack, 2026-11-22: "do a cool horse badcode outro thanks").

The last frame of the one-gate shot freezes, a camera flash fires, and a photo-finish print scans across the frame from
left to right (a bright slit, black-and-white print behind it, the colour frame ahead of it). The print then carries
the judges' header "PHOTOGRAPH" (the word a UK course calls for a photo finish), a timing ruler along the bottom and a
thin finish line across the field, which is level from rail to rail. The print dissolves into the logo card. The logo
is the brand file rendered as is (docs/brand/logo/badcode-stacked-reversed.svg, via sharp); nothing here draws or edits it.

    ~/.cache/badcode-lips/venv/bin/python scripts/shorts/gate_outro.py <shot.mp4> <out.mp4> <sfx.wav> [--line-y 0.62] [--zoom 1.35]

<shot.mp4> is the one-gate piece of the cut (1080x1920); its last frame is frozen. --line-y is where the finish line
crosses (a fraction of the frame height, on the horses' hooves); the push in is centred on it. Writes the picture (no audio) and its own sound
(the shutter click and the print's whirr, synthesised here: no outside sound used).
"""
import argparse, pathlib, subprocess
import cv2
import numpy as np

REPO = pathlib.Path(__file__).resolve().parents[2]
W, H, FPS = 1080, 1920, 24
T_SCAN0, T_SCAN1 = 0.15, 1.05      # the slit crosses the frame
T_MARKS = 1.05                     # header, ruler and finish line come in
T_DISS0, T_DISS1 = 2.05, 2.55      # the print dissolves into the logo card
T_END = 4.45
LOGO_W = 640                       # as the cut's old card: the stacked logo 640 px wide, centred
FONT = '/usr/share/fonts/opentype/urw-base35/NimbusMonoPS-Bold.otf'


def logo_card():
    png = pathlib.Path('/tmp') / f'gate-outro-stacked-{LOGO_W}.png'
    if not png.exists():
        subprocess.run(['node', '-e', f"require('sharp')('docs/brand/logo/badcode-stacked-reversed.svg',{{density:600}})"
                        f".resize({LOGO_W}).png().toFile('{png}')"], cwd=REPO, check=True)
    lg = cv2.imread(str(png), cv2.IMREAD_UNCHANGED).astype(np.float32) / 255
    card = np.zeros((H, W, 3), np.float32)
    h, w = lg.shape[:2]; x0, y0 = (W - w) // 2, (H - h) // 2
    a = lg[..., 3:4]
    card[y0:y0 + h, x0:x0 + w] = lg[..., :3] * a
    return card


def last_frame(p):
    n = int(subprocess.run(['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v:0', '-show_entries',
                            'stream=nb_read_frames', '-of', 'csv=p=0', str(p)], capture_output=True, text=True).stdout)
    cap = cv2.VideoCapture(str(p)); cap.set(cv2.CAP_PROP_POS_FRAMES, n - 1); ok, f = cap.read()
    if not ok:
        raise SystemExit(f'could not read the last frame of {p}')
    return cv2.resize(f, (W, H)).astype(np.float32) / 255


def print_look(f, rng):
    g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    lo, hi = np.percentile(g, 2), np.percentile(g, 98)
    g = np.clip((g - lo) / max(hi - lo, 1e-3), 0, 1)
    g = g * g * (3 - 2 * g)                                         # a harder, printed contrast
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    vig = 1 - 0.35 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
    g = np.clip(g * vig + rng.normal(0, 0.035, g.shape).astype(np.float32), 0, 1)
    paper = np.array([0.86, 0.93, 0.97], np.float32)               # a slightly warm paper white (BGR)
    return g[..., None] * paper


def text(img, s, cx, y, size, a=1.0, spacing=0.0):
    """Draw text with the font file through PIL (cv2 has no OTF), centred on cx, alpha a."""
    from PIL import Image, ImageDraw, ImageFont
    font = ImageFont.truetype(FONT, size)
    lay = Image.new('L', (W, size * 2), 0); d = ImageDraw.Draw(lay)
    widths = [d.textlength(c, font=font) for c in s]
    tw = sum(widths) + spacing * (len(s) - 1); x = cx - tw / 2
    for c, cw in zip(s, widths):
        d.text((x, 0), c, font=font, fill=255); x += cw + spacing
    m = np.asarray(lay, np.float32)[..., None] / 255 * a
    y0 = int(y); h = min(m.shape[0], H - y0)
    img[y0:y0 + h] = img[y0:y0 + h] * (1 - m[:h]) + m[:h]


def marks(img, k, line_y):
    """Header bar, ruler and finish line, faded in by k (0..1)."""
    if k <= 0:
        return img
    o = img.copy()
    cv2.rectangle(o, (65, 290), (W - 65, 390), (0, 0, 0), -1)
    img = img * (1 - 0.85 * k) + o * 0.85 * k
    text(img, 'PHOTOGRAPH', W / 2, 308, 64, a=k, spacing=10)
    ry = 1205
    o = img.copy()
    cv2.line(o, (65, ry), (W - 65, ry), (1, 1, 1), 2)
    for i, x in enumerate(range(65, W - 64, 19)):
        cv2.line(o, (x, ry), (x, ry - (26 if i % 5 == 0 else 12)), (1, 1, 1), 2)
    img = img * (1 - k) + o * k
    # the finish line draws out from the centre
    half = int((W / 2) * min(1, k * 1.4)); y = int(line_y * H)
    o = img.copy(); cv2.line(o, (W // 2 - half, y), (W // 2 + half, y), (1, 1, 1), 3)
    return img * (1 - k) + o * k


def ease(x):
    x = min(1, max(0, x)); return x * x * (3 - 2 * x)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('shot'); ap.add_argument('out'); ap.add_argument('sfx')
    ap.add_argument('--line-y', type=float, default=0.62)
    ap.add_argument('--zoom', type=float, default=1.35, help='how far the push in goes by the dissolve'); a = ap.parse_args()
    rng = np.random.default_rng(7)
    col = last_frame(a.shot); card = logo_card()
    prints = [print_look(col, np.random.default_rng(s)) for s in range(4)]   # grain that flickers, not frozen
    enc = subprocess.Popen(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}',
                            '-r', str(FPS), '-i', '-', '-vf', 'scale=in_range=full:out_range=limited,format=yuv420p',
                            '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
                            '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', a.out], stdin=subprocess.PIPE)
    n = round(T_END * FPS)
    for i in range(n):
        t = i / FPS
        z = 1 + (a.zoom - 1) * ease(t / T_DISS0)                    # a push in on the field, centred on its row
        cy = a.line_y * H
        M = np.float32([[z, 0, (1 - z) * W / 2], [0, z, (1 - z) * cy]])
        c = cv2.warpAffine(col, M, (W, H)); p = cv2.warpAffine(prints[(i // 2) % 4], M, (W, H))
        sx = int(W * ease((t - T_SCAN0) / (T_SCAN1 - T_SCAN0)))
        img = c * 0.8
        if sx > 0:
            img[:, :sx] = p[:, :sx]
        if 0 < sx < W:                                              # the slit, with a soft glow
            for dx, g in ((0, 1.0), (3, 0.5), (8, 0.22), (16, 0.08)):
                for s in (sx - dx, sx + dx):
                    if 0 <= s < W:
                        img[:, s] = img[:, s] * (1 - g) + g
        img = marks(img, ease((t - T_MARKS) / 0.35), a.line_y)
        fl = 0.9 * np.exp(-max(0, t) / 0.12) if t < 0.6 else 0     # the flash
        img = img * (1 - fl) + fl
        d = ease((t - T_DISS0) / (T_DISS1 - T_DISS0))
        img = img * (1 - d) + card * d
        enc.stdin.write((np.clip(img, 0, 1) * 255).astype(np.uint8).tobytes())
    enc.stdin.close(); enc.wait()
    # sound: shutter click at 0, the print's whirr under the scan, quiet
    subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y',
                    '-f', 'lavfi', '-i', 'anoisesrc=d=0.05:c=white:a=0.9,highpass=f=2500,afade=t=out:d=0.05',
                    '-f', 'lavfi', '-i', 'anoisesrc=d=0.03:c=white:a=0.6,highpass=f=1500,afade=t=out:d=0.03',
                    '-f', 'lavfi', '-i', f'anoisesrc=d={T_SCAN1 - T_SCAN0}:c=pink:a=0.25,bandpass=f=900:w=600,'
                                         f'tremolo=f=38:d=0.6,afade=t=in:d=0.1,afade=t=out:st={T_SCAN1 - T_SCAN0 - 0.15}:d=0.15',
                    '-filter_complex', f'[0]adelay=0|0[a];[1]adelay=70|70[b];[2]adelay={int(T_SCAN0 * 1000)}|{int(T_SCAN0 * 1000)}[c];'
                                       f'[a][b][c]amix=inputs=3:normalize=0,aformat=channel_layouts=stereo,apad=whole_dur={T_END},atrim=end={T_END}[o]',
                    '-map', '[o]', '-ar', '48000', a.sfx], check=True)
    print(a.out)


if __name__ == '__main__':
    main()
