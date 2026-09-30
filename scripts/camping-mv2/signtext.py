# Put lyric text ON the blank signs of a Flow clip: lay out, warp to the sign's corners,
# follow the sign frame to frame (ORB homography on the sign region, template-match fallback),
# blend into the surface. Usage: signtext.py NN [NN...]   (config in signs.json)
import cv2, json, math, random, subprocess, sys, numpy as np
from PIL import Image, ImageDraw, ImageFont

S = __import__('os').environ.get('MV2_WORK', '/tmp/camping-mv2')  # work dir holding takes/, text/, font/ and signs.json
CFG = __import__('os').environ.get('SIGNS', S + '/signs.json')  # re-cut: SIGNS=scripts/camping-mv2/recut-signs.json
FONTS = {'marker': S + '/font/PermanentMarker-Regular.ttf', 'serif': S + '/font/Cinzel.ttf', 'led': S + '/font/DotGothic16.ttf',
         'oswald': S + '/font/Oswald.ttf'}
STYLE = {  # ink colour (RGB), blend, font, per-word tilt (deg), weight for variable fonts
    'marker': dict(ink=(28, 24, 22), blend='multiply', font='marker', tilt=3.0, opacity=0.92),
    'engraved': dict(ink=(70, 48, 18), blend='multiply', font='serif', tilt=0, opacity=0.9, wght=700),
    'enamel': dict(ink=(18, 22, 40), blend='multiply', font='serif', tilt=0, opacity=0.95, wght=700),
    'gold': dict(ink=(214, 178, 96), blend='normal', font='serif', tilt=0, opacity=0.95, wght=700),
    'label': dict(ink=(40, 20, 22), blend='multiply', font='serif', tilt=0, opacity=0.92, wght=700),
    'led': dict(ink=(255, 170, 40), blend='glow', font='led', tilt=0, opacity=1.0),
    # 2026-09-29 re-cut surfaces
    'frost': dict(ink=(38, 42, 50), blend='multiply', font='oswald', tilt=0, opacity=0.85, wght=600),   # vinyl on a frosted door band
    'receipt': dict(ink=(55, 55, 62), blend='multiply', font='led', tilt=0, opacity=0.9),               # thermal till roll
    'news': dict(ink=(18, 18, 20), blend='multiply', font='oswald', tilt=0, opacity=0.9, wght=700),     # a broadsheet headline
    # 2026-09-30 breathing-room surfaces
    'paint': dict(ink=(226, 222, 212), blend='normal', font='marker', tilt=2.5, opacity=0.82, blur=1.0),  # spray/paint on a shutter, wall or bus side
    'vinyl': dict(ink=(236, 236, 232), blend='normal', font='oswald', tilt=0, opacity=0.95, wght=600, shade_min=0.85),  # white cut-vinyl on dark glass
    'screen': dict(ink=(235, 240, 245), blend='glow', font='oswald', tilt=0, opacity=0.95, wght=500),     # a phone screen
    'fog': dict(ink=(120, 128, 136), blend='multiply', font='marker', tilt=2.0, opacity=0.8, blur=1.6),  # a finger through condensation
}
SCALE = 3  # text canvas supersampling


def text_canvas(text, w, h, style, seed):
    """RGBA canvas (w*SCALE x h*SCALE) with the words laid out to fill ~80% of the sign."""
    st = STYLE[style]; W, H = int(w * SCALE), int(h * SCALE); rnd = random.Random(seed)
    lines_in = text.split('\n')
    best = None
    for size in range(int(H * 0.9), 8, -2):
        font = ImageFont.truetype(FONTS[st['font']], size)
        if 'wght' in st:
            try: font.set_variation_by_axes([st['wght']])
            except Exception: pass
        # greedy wrap each forced line to 84% width
        lines = []
        for src in lines_in:
            cur = ''
            for word in src.split():
                t = (cur + ' ' + word).strip()
                if font.getlength(t) <= W * 0.84 or not cur: cur = t
                else: lines.append(cur); cur = word
            if cur: lines.append(cur)
        lh = size * 1.12
        if len(lines) * lh <= H * 0.80 and all(font.getlength(l) <= W * 0.86 for l in lines):
            best = (font, lines, size, lh); break
    font, lines, size, lh = best
    canvas = Image.new('L', (W, H), 0)
    y0 = (H - len(lines) * lh) / 2 + size * 0.05
    for i, line in enumerate(lines):
        words = line.split(); gap = font.getlength(' ')
        total = sum(font.getlength(wd) for wd in words) + gap * (len(words) - 1)
        x = (W - total) / 2 + rnd.uniform(-0.02, 0.02) * W * (st['tilt'] > 0)
        y = y0 + i * lh
        for wd in words:
            ww = int(font.getlength(wd)) + size; hh = int(size * 1.5)
            tile = Image.new('L', (ww, hh), 0)
            ImageDraw.Draw(tile).text((size // 2, int(size * 0.1)), wd, font=font, fill=255)
            ang = rnd.uniform(-st['tilt'], st['tilt'])
            tile = tile.rotate(ang, resample=Image.BICUBIC, expand=True)
            dy = rnd.uniform(-0.04, 0.04) * size * (st['tilt'] > 0)
            canvas.paste(255, (int(x - size // 2 - (tile.width - ww) / 2), int(y + dy - (tile.height - hh) / 2)), tile)
            x += font.getlength(wd) + gap
    a = np.asarray(canvas).astype(np.float32) / 255.0
    return a


def track(frames, quad):
    """Per-frame 3x3 homography mapping frame-0 coords to frame-i coords, for the sign region."""
    q = np.array(quad, np.float32)
    x0, y0 = q.min(0); x1, y1 = q.max(0); pad = 0.25 * max(x1 - x0, y1 - y0)
    x0, y0 = max(0, int(x0 - pad)), max(0, int(y0 - pad)); x1, y1 = min(1279, int(x1 + pad)), min(719, int(y1 + pad))
    g0 = cv2.cvtColor(frames[0], cv2.COLOR_BGR2GRAY)
    mask = np.zeros_like(g0); mask[y0:y1, x0:x1] = 255
    orb = cv2.ORB_create(1500)
    k0, d0 = orb.detectAndCompute(g0, mask)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    tmpl = g0[y0:y1, x0:x1]
    Hs = [np.eye(3)]
    for f in frames[1:]:
        g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
        H = None
        m2 = np.zeros_like(g); m2[max(0, y0 - 80):min(720, y1 + 80), max(0, x0 - 80):min(1280, x1 + 80)] = 255
        k1, d1 = orb.detectAndCompute(g, m2)
        if d0 is not None and d1 is not None and len(k0) > 12 and len(k1) > 12:
            ms = bf.match(d0, d1)
            if len(ms) >= 12:
                p0 = np.float32([k0[m.queryIdx].pt for m in ms]); p1 = np.float32([k1[m.trainIdx].pt for m in ms])
                A, inl = cv2.estimateAffinePartial2D(p0, p1, method=cv2.RANSAC, ransacReprojThreshold=2.5)
                if A is not None and inl is not None and inl.sum() >= 10:
                    H = np.vstack([A, [0, 0, 1]])
        if H is None:  # fallback: translation by template match
            sx0, sy0 = max(0, x0 - 60), max(0, y0 - 60)
            res = cv2.matchTemplate(g[sy0:min(720, y1 + 60), sx0:min(1280, x1 + 60)], tmpl, cv2.TM_CCOEFF_NORMED)
            _, _, _, loc = cv2.minMaxLoc(res)
            H = np.array([[1, 0, loc[0] + sx0 - x0], [0, 1, loc[1] + sy0 - y0], [0, 0, 1]], float)
        Hs.append(H)
    # smooth: moving average of the six affine params over 7 frames, and reject jumps
    P = np.array([h[:2].ravel() for h in Hs])
    for i in range(1, len(P)):
        if np.abs(P[i] - P[i - 1])[[2, 5]].max() > 25: P[i] = P[i - 1]
    k = 7; Ps = np.array([P[max(0, i - k // 2):i + k // 2 + 1].mean(0) for i in range(len(P))])
    return [np.vstack([p.reshape(2, 3), [0, 0, 1]]) for p in Ps]


def render(nn, cfg, src, dst, static=False):
    cap = cv2.VideoCapture(src); frames = []
    while True:
        ok, f = cap.read()
        if not ok: break
        frames.append(f)
    out = [f.astype(np.float32) for f in frames]
    for si, sign in enumerate(cfg['signs']):
        quad = np.float32(sign['quad'])
        w = (np.linalg.norm(quad[1] - quad[0]) + np.linalg.norm(quad[2] - quad[3])) / 2
        h = (np.linalg.norm(quad[3] - quad[0]) + np.linalg.norm(quad[2] - quad[1])) / 2
        st = STYLE[sign['style']]
        a = text_canvas(sign['text'], w, h, sign['style'], seed=int(''.join(ch for ch in nn if ch.isdigit())) * 10 + si)
        Wc, Hc = a.shape[1], a.shape[0]
        src_pts = np.float32([[0, 0], [Wc, 0], [Wc, Hc], [0, Hc]])
        Hsign = cv2.getPerspectiveTransform(src_pts, quad)
        keys = sign.get('keys')  # [[t, quad], ...]: hand-set corners, linearly interpolated (for surfaces the tracker loses)
        if keys:
            kt = [k[0] for k in keys]; kq = [np.float32(k[1]) for k in keys]
            def quad_at(t):
                if t <= kt[0]: return kq[0]
                for j in range(len(kt) - 1):
                    if t <= kt[j + 1]:
                        u = (t - kt[j]) / (kt[j + 1] - kt[j]); return kq[j] * (1 - u) + kq[j + 1] * u
                return kq[-1]
            Hs = [cv2.getPerspectiveTransform(src_pts, quad_at(i / 24.0)) @ np.linalg.inv(Hsign) for i in range(len(frames))]
        else:
            Hs = [np.eye(3)] * len(frames) if (static or sign.get('static')) else track(frames, sign['quad'])
        t0, t1 = sign.get('from', 0), sign.get('to', 99)
        for i, f in enumerate(out):
            t = i / 24.0
            if not (t0 <= t < t1): continue
            fade = min(1.0, (t - t0) / 0.25) if t0 > 0 else 1.0
            M = Hs[i] @ Hsign
            aa = a
            if 'wipe' in sign:  # write-on: reveal left to right, line by line in reading order
                w0, w1 = sign['wipe']; prog = min(1.0, max(0.0, (t - w0) / (w1 - w0)))
                rows = np.where(a.max(1) > 0.1)[0]
                aa = np.zeros_like(a)
                if prog > 0 and len(rows):
                    # split rows into text lines by gaps
                    breaks = np.where(np.diff(rows) > 4)[0]; starts = np.r_[rows[0], rows[breaks + 1]]; ends = np.r_[rows[breaks], rows[-1]]
                    n = len(starts); per = 1.0 / n
                    for li in range(n):
                        lp = min(1.0, max(0.0, (prog - li * per) / per))
                        if lp <= 0: break
                        cols = np.where(a[starts[li]:ends[li] + 1].max(0) > 0.1)[0]
                        xcut = int(cols[0] + lp * (cols[-1] - cols[0] + 1))
                        aa[starts[li]:ends[li] + 1, :xcut] = a[starts[li]:ends[li] + 1, :xcut]
            al = cv2.warpPerspective(aa, M, (1280, 720), flags=cv2.INTER_AREA)
            al = cv2.GaussianBlur(al, (0, 0), st.get('blur', 0.6)) * st['opacity'] * fade
            al3 = al[..., None]
            ink = np.array(st['ink'][::-1], np.float32)
            if st['blend'] == 'multiply':
                f[:] = f * (1 - al3) + (f * ink / 255.0) * al3
            elif st['blend'] == 'normal':
                shade = (f.mean(2, keepdims=True) / 160.0).clip(st.get('shade_min', 0.55), 1.25)  # pick up the surface light
                f[:] = f * (1 - al3) + (ink * shade) * al3
            else:  # glow: amber LED dots + soft bloom
                bloom = cv2.GaussianBlur(al, (0, 0), 3.0)[..., None]
                f[:] = np.minimum(255, f * (1 - 0.6 * al3) + ink * al3 + ink * bloom * 0.6)
    # a touch of the clip's own grain over the whole frame so the ink sits in it
    rng = np.random.default_rng(int(''.join(ch for ch in nn if ch.isdigit())))
    p = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', '1280x720', '-r', '24', '-i', '-',
                          '-i', src, '-map', '0:v', '-map', '1:a?', '-c:v', 'libx264', '-crf', '15', '-preset', 'slow', '-pix_fmt', 'yuv420p',
                          '-c:a', 'copy', '-shortest', dst], stdin=subprocess.PIPE)
    for f in out:
        f += rng.normal(0, 2.0, f.shape).astype(np.float32)
        p.stdin.write(np.clip(f, 0, 255).astype(np.uint8).tobytes())
    p.stdin.close(); p.wait()


if __name__ == '__main__':
    cfgs = json.load(open(CFG))
    for nn in sys.argv[1:]:
        c = cfgs[nn]
        src = c.get('src', f'takes/{nn}.mp4'); src = src if src.startswith('/') else f'{S}/{src}'
        render(nn, c, src, f"{S}/text/{c.get('out', nn)}.mp4")
        print(nn, 'done', flush=True)
