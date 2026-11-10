#!/usr/bin/env python3
"""fitline.py <work> <name> "<text>" <clip:lag,...> <take,...> [--render N] : plan every take on every clip word by
word (wordwarp.plan), rank by cost (mean + half the worst lateness + mean |log tempo|), render the best N to
<work>/<name>/<clip>--<take>.wav (clip time) with a .json plan. Lag = Omni's own audio vs its own mouth (row-measure).
Run with the badcode-lips venv (numpy, soundfile). GPOM scene A round 24."""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wordwarp as WW
HERE = os.path.dirname(os.path.abspath(__file__))
APY = os.path.expanduser('~/.cache/badcode-align/venv/bin/python')
work, name, text = sys.argv[1], sys.argv[2], sys.argv[3]
clips = [(c.rsplit(':', 1)[0], float(c.rsplit(':', 1)[1])) for c in sys.argv[4].split(',')]
takes = sys.argv[5].split(',')
N = int(sys.argv[sys.argv.index('--render') + 1]) if '--render' in sys.argv else 3
# --fix clip=word:t[;word:t] : a word's start in the clip read off the MOUTH (frame strip) where Omni's own audio is off
FREE = set(sys.argv[sys.argv.index('--free') + 1].split(',')) if '--free' in sys.argv else set()  # words with no anchor
FIX = {}
for i, a in enumerate(sys.argv):
    if i and sys.argv[i - 1] == '--fix':
        c, ws = a.split('=', 1)
        FIX[c] = {w.split(':')[0]: float(w.split(':')[1]) for w in ws.split(';')}
od = f'{work}/{name}'; os.makedirs(od, exist_ok=True)
own = []
for c, _ in clips:
    w = f'{work}/own/{os.path.basename(c)[:-4]}.wav'
    if not os.path.exists(w):
        os.makedirs(os.path.dirname(w), exist_ok=True)
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', c, '-vn', '-ac', '2', '-ar', '48000', w], check=True)
    own.append(w)
aj = f'{work}/align.json'
subprocess.run([APY, f'{HERE}/align.py', aj, text, *own, *takes], capture_output=True, check=True)
A = json.load(open(aj))
W = lambda f: [x[:3] for x in A[f'{f}|{text}']]
res = []
for (c, lag), ow in zip(clips, own):
    for t in takes:
        cw = [[w, None if w in FREE else FIX.get(os.path.basename(c)[:-4], {}).get(w, s0), e] for w, s0, e in W(ow)]
        rows = WW.plan(W(t), cw, lag)
        res.append((WW.summary(rows)['cost'], c, t, lag, rows))
res.sort(key=lambda r: r[0])
for cost, c, t, lag, rows in res:
    s = WW.summary(rows)
    print(f"{cost:6.3f} {os.path.basename(c)[:-4]:22s} {os.path.basename(t)[:-4]:14s} lag {lag:+.3f} late max {s['max_late']:.2f} mean {s['mean_late']:.2f} "
          f"tempo {s['tempo_lo']:.2f}-{s['tempo_hi']:.2f} pads {s['pads']} pause+ {s['added']:.2f} (worst {s['worst_add']:.2f})")
for cost, c, t, lag, rows in res[:N]:
    out = f"{od}/{os.path.basename(c)[:-4]}--{os.path.basename(t)[:-4]}.wav"
    origin = WW.render(t, rows, out)
    json.dump(dict(clip=c, take=t, lag=lag, text=text, origin=origin, summary=WW.summary(rows), rows=rows, out=out), open(out + '.json', 'w'), indent=1)
    print('rendered', out, 'origin', origin)
