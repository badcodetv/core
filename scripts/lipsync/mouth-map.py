#!/usr/bin/env python3
"""Where a face's mouth is shut, opening and moving in a clip, read from the PICTURE (2026-10-19, Karen 10b2).

Runs scripts/lipsync/lips.py (MediaPipe inner-lip gap, landmarks 13/14 over face height) unless a lips JSON is given,
then prints (1) a strip, one character per frame: '#' open, '+' slightly open, '.' shut; (2) every shut->open moment.
Those openings are where dubbed phrases should START (0-0.1 s after, never before). Do not trust Omni's own audio or
whisper word starts for this: Omni's audio was 0.45 s off its own picture on Karen 10b2.
usage: mouth-map.py <video> [--json lips.json] [--from S] [--to S]
run with ~/.cache/badcode-lips/venv/bin/python
"""
import json, os, subprocess, sys
H = os.path.dirname(os.path.abspath(__file__))
v = sys.argv[1]; a = sys.argv
js = a[a.index('--json') + 1] if '--json' in a else None
t0 = float(a[a.index('--from') + 1]) if '--from' in a else 0.0
t1 = float(a[a.index('--to') + 1]) if '--to' in a else 1e9
if not js or not os.path.exists(js):
    js = js or v + '.lips.json'
    subprocess.run([sys.executable, os.path.join(H, 'lips.py'), v, '--face', 'big', '--json', js], check=True, capture_output=True)
L = json.load(open(js)); fps = L['fps']; g = [x or 0 for x in L['gap']]
OPEN, HALF = 0.02, 0.008
strip = ''.join('#' if x > OPEN else '+' if x > HALF else '.' for x in g)
print(f'fps {fps}, {len(g)} frames ({len(g) / fps:.2f} s); runs of movement (lips.py): {L["runs"]}')
for i in range(0, len(strip), 48):
    if t0 - 2 <= i / fps <= t1: print(f'{i / fps:6.2f} {strip[i:i + 48]}')
ons = [i / fps for i in range(1, len(g)) if g[i - 1] < 0.012 and g[i] >= OPEN and t0 <= i / fps <= t1]
print('mouth opens (shut -> open):', ' '.join(f'{t:.2f}' for t in ons))
