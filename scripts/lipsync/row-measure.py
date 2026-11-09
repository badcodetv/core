#!/usr/bin/env python3
"""row-measure.py <edl.json> <t0> <t1> [--out DIR] [--map shotfile=stem ...]   (2026-11-06, GPOM scene A round 19, Kai at3436)

Measures lip sync on an ASSEMBLED cut, shot by shot, the way the eye sees it: for every V1 shot in [t0, t1] it cuts the
shot out of its source at its edl in/dur, tracks the mouth at the shot's own frame rate (MediaPipe, lips.py), and lines it
up against the stem of the person on screen (a vox-* stem from the edl's audio list). Per shot it prints:

  lag     the voice's best offset against the mouth (+ = voice late; late is forgiven up to ~0.13 s, early is not past ~0.05 s)
  corr    how well loudness follows the mouth gap at that lag (0..1; 0.5+ reads as talking together)
  early   voice onsets that land before the mouth opens (s each; the worst errors)
  shut    seconds of loud voice over a shut mouth
  mute    seconds of a talking (moving) mouth with no voice
  score   good / ok / bad

and writes a 12 fps tracked strip per shot (<out>/<shot>-strip.jpg) with the voice loudness drawn under each frame.
Who is on screen: --map <substring of the shot file>=<stem id>, e.g. --map 6-0=vox-sandra --map 7d-=vox-derek.
run with ~/.cache/badcode-lips/venv/bin/python"""
import sys, os, json, subprocess, tempfile
import numpy as np, cv2, librosa

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lips

args = sys.argv[1:]
edl_path, t0, t1 = args[0], float(args[1]), float(args[2])
out = args[args.index('--out') + 1] if '--out' in args else tempfile.mkdtemp()
os.makedirs(out, exist_ok=True)
maps = [a.split('=', 1) for i, a in enumerate(args) if i and args[i - 1] == '--map']
edl = json.load(open(edl_path))
stems = {a.get('name') or a.get('id') or os.path.basename(a['file']): a['file'] for a in edl['audio']}
stems.update({os.path.basename(a['file']).split('-', 1)[-1].rsplit('.', 1)[0]: a['file'] for a in edl['audio']})


def track(clip):
    lm = lips.landmarker(); crop = lips.find_crop(clip, lm, 'big')
    cap = cv2.VideoCapture(clip); fps = cap.get(cv2.CAP_PROP_FPS) or 24
    g, frames, ctr = [], [], []
    while True:
        ok, fr = cap.read()
        if not ok: break
        frames.append(fr)
        fs = lips.detect(lm, fr, crop) if crop else []
        if not fs: fs = lips.detect(lm, fr, (0, 0, 1, 1))
        if fs:
            size = lambda f: abs(f[152][1] - f[10][1]); f = max(fs, key=size)
            g.append(abs(f[14][1] - f[13][1]) / max(1e-6, size(f)))
            ctr.append(((f[13][0] + f[14][0]) / 2, (f[13][1] + f[14][1]) / 2, size(f)))
        else:
            g.append(np.nan); ctr.append(None)
    return fps, np.array(g, float), frames, ctr


def envelope(wav, start, dur, fps, n):
    y, sr = librosa.load(wav, sr=16000, offset=max(0, start), duration=dur, mono=True)
    hop = int(sr / fps)
    rms = np.array([np.sqrt(np.mean(y[i * hop:(i + 1) * hop] ** 2)) if i * hop < len(y) else 0 for i in range(n)])
    db = 20 * np.log10(rms + 1e-6)
    return db


def runs(mask):
    r, i = [], 0
    while i < len(mask):
        if mask[i]:
            j = i
            while j < len(mask) and mask[j]: j += 1
            r.append((i, j)); i = j
        else: i += 1
    return r


rows = []
for k, v in enumerate(edl['video']):
    s, d = v['start'], v['dur']
    if s + d <= t0 or s >= t1: continue
    label = os.path.basename(v.get('tag', v['file']))
    stem = next((st for sub, st in maps if sub in label), None)
    if not stem: continue
    name = label.replace('-muted.mp4', '').replace('.mp4', '')
    seg = f'{out}/{k:02d}-{name}.mp4'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f"{v['in']:.4f}", '-i', v['file'], '-t', f'{d:.4f}', '-an',
                    '-c:v', 'libx264', '-crf', '14', '-r', '24', seg], check=True)
    fps, g, frames, ctr = track(seg)
    n = len(g)
    db = envelope(stems[stem], s, d, fps, n)
    # mouth: rescale to the shot's own 10th-95th percentile; "moving" = frame-to-frame change (speech is a mouth that CHANGES)
    lo, hi = np.nanpercentile(g, 10), np.nanpercentile(g, 95)
    r = np.clip((g - lo) / max(1e-6, hi - lo), 0, 1.5)
    rr = np.nan_to_num(r, nan=0)
    mv = np.abs(np.gradient(np.convolve(rr, np.ones(3) / 3, 'same')))
    talk_m = (np.convolve(mv, np.ones(5) / 5, 'same') > 0.06) & (rr > 0.15)
    vthr = max(db.max() - 28, -50)
    talk_v = db > vthr
    # lag by cross-correlating loudness with mouth gap (both z-scored), +-0.5 s
    a = (rr - rr.mean()) / (rr.std() + 1e-6)
    bv = np.clip(db, vthr, None); b = (bv - bv.mean()) / (bv.std() + 1e-6)
    best = (0, -9)
    for L in range(-12, 13):
        if L >= 0: x, y = a[:n - L], b[L:]
        else: x, y = a[-L:], b[:n + L]
        if len(x) > 10:
            c = float(np.mean(x * y))
            if c > best[1]: best = (L, c)
    lag, corr = best[0] / fps, best[1]
    early = []
    for i, j in runs(talk_v):
        if j - i < 3: continue
        # first frame of the voice run vs the mouth's first open frame at or near it
        if not (r[i] > 0.25 if not np.isnan(r[i]) else False):
            k2 = i
            while k2 < n and not (not np.isnan(r[k2]) and r[k2] > 0.25): k2 += 1
            if k2 < n and k2 - i <= 12: early.append(round((k2 - i) / fps, 3))
    shut = float(np.sum(talk_v & (np.nan_to_num(r, nan=1) < 0.12))) / fps
    mute = float(np.sum(talk_m & ~talk_v)) / fps
    miss = int(np.isnan(g).sum())
    worst_early = max(early) if early else 0
    score = 'good'
    if worst_early > 0.06 or abs(lag) > 0.12 or lag < -0.05 or shut > 0.35 or corr < 0.4: score = 'ok'
    if worst_early > 0.15 or lag < -0.09 or lag > 0.2 or shut > 0.7 or corr < 0.25 or mute > 1.2: score = 'bad'
    strip = ''.join('?' if np.isnan(x) else '#' if x > .55 else '+' if x > .25 else '.' for x in r)
    vstr = ''.join('#' if x > vthr + 14 else '+' if x > vthr else '.' for x in db)
    row = dict(shot=name, at=round(s, 3), dur=round(d, 3), stem=stem, lag=round(lag, 3), corr=round(corr, 2),
               early=early, shut=round(shut, 2), mute=round(mute, 2), missing=miss, score=score)
    rows.append(row)
    print(f"\n{k:02d} {name}  @{s:.2f}+{d:.2f}  {stem}  lag {lag:+.3f}  corr {corr:.2f}  early {early}  shut {shut:.2f}s  "
          f"mute {mute:.2f}s  missing {miss}  -> {score.upper()}")
    for i in range(0, n, 48):
        print(f'  {i / fps:5.2f} M {strip[i:i + 48]}\n        V {vstr[i:i + 48]}')
    # 12 fps tracked strip with voice bar
    tiles = []
    for i in range(0, n, 2):
        c = next((ctr[q] for q in [i, i - 1, i + 1, i - 2, i + 2] if 0 <= q < n and ctr[q]), None)
        fr = frames[i]; H, W = fr.shape[:2]
        if c:
            cx, cy, sz = c[0] * W, c[1] * H, c[2] * H * 0.55
            x0, y0 = int(max(0, cx - sz)), int(max(0, cy - sz * 0.6))
            crop_ = fr[y0:int(min(H, cy + sz * 0.6)), x0:int(min(W, cx + sz))]
        else:
            crop_ = fr
        t = cv2.resize(crop_, (110, 66)) if crop_.size else np.zeros((66, 110, 3), np.uint8)
        bar = np.full((22, 110, 3), 255, np.uint8)
        lv = int(np.clip((db[i] - vthr) / 30, 0, 1) * 100)
        cv2.rectangle(bar, (5, 2), (5 + lv, 9), (40, 40, 220), -1)
        gv = int(np.clip(rr[i], 0, 1) * 100)
        cv2.rectangle(bar, (5, 12), (5 + gv, 19), (20, 20, 20), -1)
        t = np.vstack([t, bar])
        cv2.putText(t, f'{i / fps:.2f}', (2, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.38, (0, 255, 255), 1)
        tiles.append(t)
    cols = 12
    while len(tiles) % cols: tiles.append(np.zeros_like(tiles[0]))
    sheet = np.vstack([np.hstack(tiles[i:i + cols]) for i in range(0, len(tiles), cols)])
    cv2.imwrite(f'{out}/{k:02d}-{name}-strip.jpg', sheet)
json.dump(rows, open(f'{out}/measure.json', 'w'), indent=1)
print('\n' + '\n'.join(f"{r['shot']:28s} {r['score']:5s} lag {r['lag']:+.2f} corr {r['corr']:.2f} early {r['early']}" for r in rows))
