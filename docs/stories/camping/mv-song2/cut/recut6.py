"""`camping song 2 beat 6` (Jack 2026-11-09, ../cleanroom/r10/jack.md): from edl-beat5.json, two sections re-cut with the round-10
clean-room clips (../../mv-r10, prompts ../cleanroom/r10/), every cut on the measured 88 BPM beat (bars.json + drift), 0-1 frame early.

1. Opening 0-10.96: the dark stadium, his screen snapping on to BADCODE on the first drum hit (2.8), light banks on the beat, the
   lit bowl on the bass (4.2), the crowd, the DJ, him from behind -> the tunnel run (unchanged) at 10.96.
2. Bridge 142.61-183.5 (bar 52 to the hook-3 downbeat): the masked rappers trading lines (du) intercut with the real Bob and Tarquin
   meeting and arguing in the car park (re), speaker matched to the lyric sheet; lyric cutaways on their words (ly, plus t21 for the
   sack, b23 for "rained on", and Jack's verse-1 Waitrose clip 4.mp4 for "when we very first met"); the clink on "same SIDE" (178.96);
   one held two-shot of both shouting over the drum stop into the hook. V2/V3 inside the bridge are cleared.
Writes edl-beat6.json; build6.py makes the Premiere scripts. Clink frame: CLINK_AT (s into the du08 clip) measured from the clip."""
import json, sys
from pathlib import Path
import numpy as np
HERE = Path(__file__).parent
FPS = 25
B = json.load(open(HERE.parent / 'analysis/bars.json'))
beats = np.array(B['beats'])
loc = B['local_offset_ms_per_4_bars']
lt, lo = np.array([x[0] + 2 * B['bar'] for x in loc]), np.array([x[1] for x in loc]) / 1000
beats = beats + np.interp(beats, lt, lo)
k0 = int(np.argmin(abs(beats - B['first_downbeat'])))
def bt(b):  # time of beat number b (counted from the first downbeat, fractions allowed), 0-1 frame early
    i = k0 + int(np.floor(b)); f = b - np.floor(b)
    t = beats[i] + f * (beats[i + 1] - beats[i])
    return float(np.floor((t - 0.02) * FPS + 1e-6) / FPS)

V = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/'
P = json.load(open(HERE.parent / 'cleanroom/r10/picks.json'))
def r10(k): return V + f'r10/video/premiere/r10-{k}-{k}-{P[k]}.mp4'
OLD = {'t21': V + 'action/video/premiere/ca-t21-t21r2-b.mp4', 'b23': V + 'action/video/premiere/ca-b23-b23r2-b.mp4',
       'first-met': V + 'clips/4.mp4'}
def src(k): return OLD.get(k) or r10(k)
CLINK_AT = float(sys.argv[1]) if len(sys.argv) > 1 else 3.55
SIDE = 178.96  # "side" in "same side all along" (whisper)

OPEN = [  # (beat, shot, in point) — beat 0 = first downbeat 0.75; ends at the tunnel run 10.96
    (None, 'st01d', 0.3), (2, 'st04d', 1.0), (3, 'st02', 0.2), (4, 'st03', 0.5), (4.5, 'st04', 1.0), (5, 'st01', 0.5),
    (7, 'st05', 0.5), (8, 'st03', 3.0), (8.5, 'st06', 0.5), (10, 'st04', 3.0), (12, 'st05', 2.0), (13, 'st07', 0.5)]
BRIDGE = [  # beat 208 = bar 52 = 142.61
    (208, 're01', 0.3), (210, 'du01', 0.3), (212, 're02', 0.3), (214, 'du01', 1.8), (215, 'b23', 0.44), (216, 're02', 2.0),
    (217, 'du02', 0.3), (220, 't21', 0.44), (221, 'ly01', 0.5), (222, 'ly02', 0.5), (223, 'du03', 0.3), (225, 'ly03', 0.5),
    (227, 'du03', 2.0), (230, 'ly04', 5.0), (232, 're03', 0.3), (233, 'du04', 0.3), (235, 're03', 1.6), (237, 'du04', 1.5),
    (239, 'ly05', 0.5), (241, 'du05', 0.3), (242, 'ly06', 0.5), (244, 'du05', 1.5), (246, 're02', 4.0), (247, 'ly07', 0.5),
    (249, 're04', 0.5), (251, 'first-met', 3.2), (253, 'du06', 0.5), (256, 'du07', 0.5), (258, 're05', 0.5),
    (260, 'du08', None), (262, 're06', 0.5), (264, 'du09', 0.3)]
BR_END_BEAT = 268  # hook 3 downbeat (183.5): the existing hook piece starts here

def build(plan, t0, t_end):
    out = []
    for i, (b, k, inp) in enumerate(plan):
        s = t0 if b is None else bt(b)
        e = t_end if i == len(plan) - 1 else bt(plan[i + 1][0])
        if k == 'du08':  # the glass meets the bottle on "side"
            inp = round(max(0.0, CLINK_AT - (SIDE - s)), 3)
        out.append({'start': round(s, 3), 'end': round(e, 3), 'src': src(k), 'in': inp, 'shot': k})
    return out

e = json.load(open(HERE / 'edl-beat5.json'))
OPEN_END, BR0, BR1 = 10.96, bt(208), bt(BR_END_BEAT)
new = {}
for tr in ('V1', 'V2', 'V3'):
    keep = []
    for x in e[tr]:
        if x['end'] <= OPEN_END + 1e-3 and tr == 'V1': continue
        if x['start'] < BR1 - 1e-3 and x['end'] > BR0 + 1e-3:  # overlaps the bridge
            if tr == 'V1' and x['start'] < BR0 - 1e-3: keep.append({**x, 'end': BR0})  # trim the hook-2 tail
            continue
        keep.append(x)
    new[tr] = keep
new['V1'] += build(OPEN, 0.0, OPEN_END) + build(BRIDGE, BR0, BR1)
for tr in new: new[tr].sort(key=lambda x: x['start'])
json.dump(new, open(HERE / 'edl-beat6.json', 'w'), indent=1)
v1 = new['V1']
gaps = [(round(a['end'], 2), round(b['start'], 2)) for a, b in zip(v1, v1[1:]) if abs(b['start'] - a['end']) > 0.03]
print('V1', len(v1), 'V2', len(new['V2']), 'V3', len(new['V3']), 'bridge', BR0, '->', BR1, 'gaps', gaps)
for x in v1:
    if x['start'] < 11 or BR0 - 0.1 <= x['start'] <= BR1:
        print(f"{x['start']:7.2f}-{x['end']:7.2f} {x['end']-x['start']:4.2f} {x.get('shot', Path(x['src'] or 'BLACK').name)} in {x['in']}")
