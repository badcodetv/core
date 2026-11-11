#!/usr/bin/env python3
"""flow-align.py <clip.mp4> <voice.wav> <out-dir> <name> [--lead 0.03] [--lo 0.88] [--hi 1.14]
(2026-11-11, GPOM bridge round 11, Kai at571: LatentSync's repainted mouths show; "back out of this approach ... just
regenerate in flow". And: "that's where we started and the timing just drifts massively, so it would be really useful to
have some kind of system of lining the timing up between the flow video and the audio that we're stitching in.")

The system, in one call, for a Flow (Omni) talking clip whose line was written into its prompt:
  1. MEASURE the mouth from the picture (lips.py, MediaPipe): runs of movement. Never Omni's own audio or whisper: Omni's
     sound does not follow its picture (0.45 s off on Karen 10b2; 0.7 s late on GPOM br36).
  2. PLACE the voice: the take is split at its own pauses (silences >= 0.25 s). If it has as many phrases as the mouth has
     runs, each phrase starts on its run (+lead, never early); otherwise the whole take starts on the first run. Words are
     never cut inside a phrase and never sped up (place-dub.py).
  3. WARP the picture to the placed voice (picture-warp.py): dynamic time warping of mouth gap against loudness, local
     speed clamped to [lo, hi] so the head never looks sped up; frames are sampled, never interpolated.
  4. SCORE: picture-warp prints each voiced run's mouth-voice offset before and after. A line ships when every run is
     within -0.05 s (early) / +0.13 s (late); otherwise it is heard over another shot (Kai's rule for Derek, 11 Nov).
Writes <out>/<name>-in.mp4 (24 fps, the clip's length), <out>/<name>-voice.wav (the placed voice, same length) and
<out>/<name>-align.json (runs, phrases, placements, score). The cut scripts read -in.mp4 + -voice.wav like a LatentSync pair.
run with ~/.cache/badcode-lips/venv/bin/python"""
import json, os, re, subprocess, sys

H = os.path.dirname(os.path.abspath(__file__))
a = sys.argv[1:]
clip, voice, out, name = a[0], a[1], a[2], a[3]
opt = lambda k, d: float(a[a.index(k) + 1]) if k in a else d
LEAD, LO, HI = opt('--lead', 0.03), opt('--lo', 0.88), opt('--hi', 1.14)
os.makedirs(out, exist_ok=True)
PY = sys.executable


def probe(f):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f]))


# 1 · the mouth
lj = os.path.join(out, f'{name}.lips.json')
if not os.path.exists(lj):
    subprocess.run([PY, os.path.join(H, 'lips.py'), clip, '--face', 'big', '--json', lj], check=True, capture_output=True)
runs = []
for s, e in json.load(open(lj))['runs']:
    if runs and s - runs[-1][1] < 0.25:
        runs[-1][1] = e
    else:
        runs.append([s, e])
runs = [r for r in runs if r[1] - r[0] >= 0.2]

# 2 · the voice's own phrases (split at its pauses)
log = subprocess.run(['ffmpeg', '-hide_banner', '-i', voice, '-af', 'silencedetect=n=-40dB:d=0.25', '-f', 'null', '-'],
                     capture_output=True, text=True).stderr
vd = probe(voice)
sil = [(float(s), float(e)) for s, e in zip(re.findall(r'silence_start: ([\d.]+)', log), re.findall(r'silence_end: ([\d.]+)', log))]
edges, t = [], 0.0
for s, e in sil:
    if s > t + 0.05:
        edges.append([t, s])
    t = e
if t < vd - 0.05:
    edges.append([t, vd])
phr = [p for p in edges if p[1] - p[0] >= 0.1]
D = probe(clip)
if len(phr) == len(runs) and runs:
    place = [{'src': voice, 'from': max(0, p[0] - 0.02), 'to': min(vd, p[1] + 0.06), 'at': round(r[0] + LEAD - 0.02, 3),
              'text': f'phrase {i + 1}'} for i, (p, r) in enumerate(zip(phr, runs))]
    how = 'phrase by phrase'
else:
    on = phr[0][0] if phr else 0.0
    st = (runs[0][0] if runs else 0.4) + LEAD
    place = [{'src': voice, 'from': max(0, on - 0.02), 'to': vd, 'at': round(st - 0.02, 3), 'text': 'whole take'}]
    how = f'whole take ({len(phr)} phrases, {len(runs)} mouth runs)'
for i in range(1, len(place)):                     # never overlap the phrase before
    prev = place[i - 1]
    end = prev['at'] + prev['to'] - prev['from']
    if place[i]['at'] < end + 0.05:
        place[i]['at'] = round(end + 0.05, 3)
pj = os.path.join(out, f'{name}-phrases.json')
json.dump({'duration': D, 'phrases': place}, open(pj, 'w'), indent=1)
vo = os.path.join(out, f'{name}-voice.wav')
pd = subprocess.run([PY, os.path.join(H, 'place-dub.py'), pj, vo], capture_output=True, text=True, check=True).stdout

# 3 · warp the picture to it, 4 · score
vi = os.path.join(out, f'{name}-in.mp4')
pw = subprocess.run([PY, os.path.join(H, 'picture-warp.py'), clip, '0', f'{D:.3f}', vo, '0', vi, '--lo', str(LO), '--hi', str(HI),
                     '--pad', '0'], capture_output=True, text=True)
rep = pw.stdout + pw.stderr
json.dump({'clip': clip, 'voice': voice, 'mouth_runs': runs, 'voice_phrases': phr, 'how': how, 'placed': place,
           'place_dub': pd, 'warp': rep, 'warp_ok': pw.returncode == 0}, open(os.path.join(out, f'{name}-align.json'), 'w'), indent=1)
print(f'{name}: {how}\n mouth runs {runs}\n voice phrases {[[round(x, 2) for x in p] for p in phr]}\n{pd}{rep}')
