#!/usr/bin/env python3
"""Re-time the second half's picture to its voices, and place every line and music cue.

Rules (rough cut, 17 Oct 2026):
  - Dialogue stays inside its own frame; if the lines do not fit, the frame grows.
  - Narration may run on over the following frames, as long as they carry no lines of their own;
    a voiced frame never starts until the voice before it has finished (the frame before grows).
  - A frame never gets shorter than its first-assembly length (edl.py).
  - Lines in one frame play in order with GAP between them, LEAD after the frame starts, TAIL after.

Reads edl.py, the audio plan and voice/trim durations. Writes rough-cut.json beside the audio:
  clips: [file, t, in, dur, frame, extend]   (extend > 0: the clip needs more than its source has)
  voices: [key, file, t, dur, track]
  cues: [id, t, dur]

    python3 scripts/gpom/second-half-video/timing.py
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import edl  # noqa: E402
import shots as S  # noqa: E402

FPS = 24
LEAD, GAP, TAIL = 0.4, 0.35, 0.6
VOICE = S.CLIPS / 'audio' / 'voice' / 'trim'
OUT = S.CLIPS / 'audio' / 'rough-cut.json'
TRACK = {'narrator': 0, 'ai': 1, 'bot': 1, 'woman': 1, 'man': 1, 'lady': 1, 'crowd': 2}
plan = json.loads((S.SCENES / 'second-half-audio-plan.json').read_text())


def fr(s):
    return round(s * FPS) / FPS


def dur(p):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


# Frames in order, each with its clips and base length.
frames = []
for name, t, i, d, n, note in edl.entries():
    if frames and frames[-1]['n'] == n:
        frames[-1]['clips'].append([name, i, d])
    else:
        frames.append({'n': n, 'clips': [[name, i, d]]})

voices, t, busy = [], 0.0, 0.0
for k, f in enumerate(frames):
    base = sum(c[2] for c in f['clips'])
    lines = plan['shots'].get(str(f['n']), {}).get('lines', [])
    takes = []
    for i, (who, _) in enumerate(lines):
        if who == 'crowd':
            keys = sorted(p.stem for p in VOICE.glob(f"{f['n']:02d}-{i}-crowd*.wav"))
            takes.append((who, keys, max(dur(VOICE / f'{x}.wav') for x in keys)))
        else:
            key = f"{f['n']:02d}-{i}-{who}"
            takes.append((who, [key], dur(VOICE / f'{key}.wav')))
    if takes and busy + GAP > t + LEAD:
        # The voice before is still talking: the previous frame holds until it is done.
        grow = fr(busy + GAP - LEAD - t)
        frames[k - 1]['grow'] = frames[k - 1].get('grow', 0) + grow
        t = fr(t + grow)
    start, s = t, t + LEAD
    dialogue_end = t
    for who, keys, d in takes:
        for j, key in enumerate(keys):
            # Crowd voices overlap, a beat apart.
            voices.append([key, f'{key}.wav', fr(s + 0.25 * j), d, TRACK[who]])
        s = s + d + GAP
        if who != 'narrator':
            dialogue_end = s - GAP
    busy = max(busy, s - GAP) if takes else busy
    need = max(base, dialogue_end + TAIL - start) if takes else base
    f['grow'] = f.get('grow', 0) + fr(max(0, need - base))
    t = fr(start + need)
    f['start'] = start
    # Frame 18: the revolt line and "Then watch this" belong on the crowd (18a), before the CCTV.
    if f['n'] == 18 and takes:
        f['clips'][0][2] = fr(max(f['clips'][0][2], dialogue_end + 0.3 - start))
        f['grow'] = fr(max(0, need - sum(c[2] for c in f['clips'])))
        t = fr(start + sum(c[2] for c in f['clips']) + f['grow'])

# Lay the clips: each frame's growth goes to its LAST clip (the held moment), recomputed from scratch.
clips, t = [], 0.0
for f in frames:
    for j, (name, i, d) in enumerate(f['clips']):
        if j == len(f['clips']) - 1:
            d = fr(d + f.get('grow', 0))
        src = dur(S.OUT / name)
        clips.append([name, fr(t), i, d, f['n'], fr(max(0, i + d - src))])
        t = fr(t + d)
total = t

# The voices were placed on the first pass's clock; re-anchor them to the frame starts of the final lay.
starts = {}
for c in clips:
    starts.setdefault(c[4], c[1])
first_pass = {f['n']: f['start'] for f in frames}
for v in voices:
    n = int(v[0][:2])
    v[2] = fr(v[2] - first_pass[n] + starts[n])

cues = []
for c in plan['cues']:
    a, b = c['frames']
    t0 = starts[a]
    nxt = [x[1] for x in clips if x[4] > b]
    cues.append([c['id'], c['name'], t0, fr((nxt[0] if nxt else total) - t0)])

OUT.write_text(json.dumps({'total': total, 'clips': clips, 'voices': voices, 'cues': cues}, indent=1))
print(f'total {total:.2f}s (was {edl.entries()[-1][1] + edl.entries()[-1][3]:.2f}s)')
for c in clips:
    if c[3] != next(e for e in edl.entries() if e[0] == c[0])[3] or c[5]:
        print(f'  frame {c[4]:2d} {c[0]:38s} {c[3]:5.2f}s  extend {c[5]:.2f}s')
for c in cues:
    print(f'  cue {c[0]:3s} {c[1]:18s} {c[2]:6.2f} +{c[3]:.2f}s')
