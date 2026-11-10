#!/usr/bin/env python3
"""lagtry.py <work> <name> "<text>" <clip> <take> <lag,...> : render one clip/take pair at several audio->mouth lags and
measure each as a shot (check.py). The lag that reads right on the mouth wins. GPOM scene A round 24."""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wordwarp as WW
HERE = os.path.dirname(os.path.abspath(__file__))
work, name, text, clip, take, lags = sys.argv[1:7]
A = json.load(open(f'{work}/align.json'))
own = f'{work}/own/{os.path.basename(clip)[:-4]}.wav'
W = lambda f: [x[:3] for x in A[f'{f}|{text}']]
od = f'{work}/{name}'; os.makedirs(od, exist_ok=True)
for lag in [float(x) for x in lags.split(',')]:
    rows = WW.plan(W(take), W(own), lag)
    out = f"{od}/{os.path.basename(clip)[:-4]}--{os.path.basename(take)[:-4]}--lag{lag:+.3f}.wav"
    origin = WW.render(take, rows, out)
    json.dump(dict(clip=clip, take=take, lag=lag, text=text, origin=origin, summary=WW.summary(rows), rows=rows, out=out),
              open(out + '.json', 'w'), indent=1)
    r = subprocess.run([sys.executable, f'{HERE}/check.py', out], capture_output=True, text=True)
    line = [l for l in r.stdout.splitlines() if ' -> ' in l]
    print(f'lag {lag:+.3f} origin {origin:+.3f}', line[0].split('vox-x')[1] if line else r.stderr[-300:])
