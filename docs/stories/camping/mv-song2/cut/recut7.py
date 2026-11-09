"""`camping song 2 beat 7` (Jack's round-1 notes on the beat-6 timeline page, 2026-11-09; notes and answers:
docs/stories/camping/mv-r10/feedback/timeline-r1, cut-notes.json). From edl-beat6.json, overwrite in place:

Opening: the new dark stadium st11d (0-2.08) and, on the bass (4.12-5.48), the stadium pulsing: st11d with its floodlit twin st11p
cut in for 3 frames on every beat. Verse 1: Bob's view of Tarquin at the X8 (film 20) before Tarquin's look; Tarquin through the
Waitrose doors (clip 5); the X8 driving (film 10) + the BAD C0DE plate (film 68) on "wheels on tick"; the X8 into the bays (film 17);
a Bob action shot from the downbeat of the drop (44.40); the new DJ (st04) in place of Glastonbury. Verse 2: the rap from "You are
intent" (77.64); Tarquin action sandwiched between the rap clips on their lines; the M3 lane change on "lane in my M3" (boat overlay
off, the boat on "plenty"); the wine on "drink my Chateau". Hook 2 (V2): keys out (film 7 in), the horse from mid-gallop. Bridge: the
four masked shots swapped for their fixed re-makes (du02x du05x du06x du07x). Hook 3: the headphones clip out (film 29 in).
Writes edl-beat7.json; build7.py makes the Premiere scripts."""
import json
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
def bt(b):
    i = k0 + int(np.floor(b)); f = b - np.floor(b)
    t = beats[i] + f * (beats[i + 1] - beats[i])
    return float(np.floor((t - 0.02) * FPS + 1e-6) / FPS)

V = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/'
FILM = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/Camping Comic/Camping Video NEW!/new clips/'
P = json.load(open(HERE.parent / 'cleanroom/r10/picks.json'))
def r10(k): return V + f'r10/video/premiere/r10-{k}-{k}-{P.get(k, "?")}.mp4'
def act(k): return V + 'action/video/premiere/' + {'t2': 'ca-t2-t2r1-a', 't23': 'ca-t23-t23r2-a', 'x2': 'ca-x2-x2r1-c', 't4': 'ca-t4-t4r1-a'}[k] + '.mp4'
def film(n): return V + 'r10/video/premiere/film-17-1080.mp4' if n == 17 else FILM + f'{n}.mp4'  # 17 is 4K: 1080p copy

e = json.load(open(HERE / 'edl-beat6.json'))
log = []
def ov(tr, s, t1, src, inp, why):
    """Overwrite [s, t1) on a track: cut what overlaps (keeping each piece's own in point running), put src there."""
    s, t1 = round(s, 3), round(t1, 3)
    out = []
    for x in e[tr]:
        if x['end'] <= s + 1e-3 or x['start'] >= t1 - 1e-3: out.append(x); continue
        if x['start'] < s - 1e-3: out.append({**x, 'end': s})
        if x['end'] > t1 + 1e-3:
            out.append({**x, 'start': t1, 'in': None if x['in'] is None else round(x['in'] + (t1 - x['start']), 3)})
    if src: out.append({'start': s, 'end': t1, 'src': src, 'in': round(inp, 3), 'shot': why.split(':')[0]})
    e[tr] = sorted(out, key=lambda x: x['start']); log.append(f'{tr} {s:.2f}-{t1:.2f} {why}')
def swap(old, new):
    n = 0
    for tr in ('V1', 'V2', 'V3'):
        for x in e[tr]:
            if x['src'] and old in x['src']: x['src'] = new; n += 1
    log.append(f'swap {old} -> {Path(new).name} x{n}')

# Opening
ov('V1', 0.0, 2.08, r10('st11d'), 0.3, 'st11d: dark stadium, the DJ readable')
t, b, inp = 4.12, 5, 2.4
for k in range(2):  # beats 5 and 6 (4.12, 4.80): 3 lit frames on the beat, then dark
    s = bt(b + k); e1 = bt(b + k + 1) if k < 1 else 5.48
    ov('V1', s, s + 0.12, r10('st11p'), inp + (s - 4.12), 'st11p: pulse on the beat')
    ov('V1', s + 0.12, e1, r10('st11d'), inp + (s + 0.12 - 4.12), 'st11d: dark between pulses')
# Verse 1
ov('V1', 15.72, 17.12, film(20), 0.5, 'film20: Bob sees Tarquin at the X8 (at441)')
ov('V1', 21.20, 23.92, V + 'clips/5.mp4', 3.0, 'clip5: Tarquin through the Waitrose doors (at582)')
ov('V1', 32.08, 33.44, film(10), 1.0, 'film10: Tarquin driving the X8, "paid for your wheels" (at822)')
ov('V1', 33.44, 34.80, film(68), 1.0, 'film68: the BAD C0DE plate, "on tick" (at822)')
ov('V1', 35.48, 36.88, film(17), 2.0, 'film17: the X8 into the bays (at907)')
d0, d1 = bt(64), bt(68)
ov('V1', d0, d1, V + 'clips/13.mp4', 1.0, f'clip13: Bob, from the downbeat of the drop {d0} (at1120)')
ov('V1', 56.64, 58.68, r10('st04'), 4.0, 'st04: the TV-head DJ in place of Glastonbury (at1448)')
ov('V1', 60.04, 62.08, r10('st07'), 2.0, 'st07: the DJ from behind, rest of the Glastonbury clip out (at1448)')
ov('V1', 62.08, 64.80, r10('st06'), 3.0, 'st06: the stands, rest of the Glastonbury clip out (at1448)')
# Verse 2
ov('V1', 77.08, 77.64, V + 'clips/badcode guy/3.mp4', 7.76, 'badcode guy 3 runs on to the line')
ov('V1', 77.64, 79.84, V + 'balaclava/video/premiere/cb-t04g-t04gr9-a.mp4', 0.0, 'rap t04g from "You are intent" (at1948)')
ov('V1', 81.20, 82.56, film(53), 1.0, 'film53: Tarquin looks down at Bob, "pathetic" (at2631)')
ov('V1', 85.28, 86.64, film(14), 1.0, 'film14: beer in the tent, "drowning your sorrow" (at2631)')
ov('V1', 91.40, 92.80, film(42), 1.0, 'film42: the money counter, "the grift" (at2631)')
ov('V1', 97.56, 98.92, film(45), 2.0, 'film45: the shotgun, "what the fuck you think this is" (at2631)')
ov('V1', 102.32, 103.68, act('t23'), 0.5, 't23: the helicopter, "platinum card" (at2631)')
ov('V2', 109.12, 110.48, None, 0, 'boat overlay off the M3 (at2738)')
ov('V1', 108.44, 110.48, V + 'clips/37.mov', 3.8 - (109.48 - 108.44), 'clip37: the M3 lane change on "lane in my M3" (at2738)')
ov('V1', 111.84, 113.20, act('t2'), 0.4, 't2: the boat, "you could have plenty" (at2738)')
ov('V1', 118.68, 120.72, act('x2'), 0.5, 'x2: the wine, "let me drink my Chateau" (at3009)')
# Hook 2 (V2)
ov('V2', 132.32, 133.68, film(7), 2.0, 'film7: Tarquin at the Shard window, keys out (at3320)')
ov('V2', 135.04, 136.40, act('t4'), 3.0, 't4: the horse from mid-gallop (at3386)')
# Bridge masks
for k in ('du02', 'du05', 'du06', 'du07'):
    if k + 'x' in P: swap(f'/r10-{k}-', r10(k + 'x'))
    else: log.append(f'!! {k}x not picked yet: {k} kept')
# Hook 3
ov('V1', 201.28, 202.64, film(29), 0.5, 'film29: the tent city at night, headphones clip out (at5021)')

# Jack's own edit in Premiere on beat 6 (found 2026-11-09 before building beat 7, by: jack, in Premiere): the ending cut short —
# 32.mp4 (212.2-217.64) and the black after it gone, the logo 4.mp4 at 212.2-214.6 (in 1.36), the song trimmed to end at 214.6.
e['V1'] = [x for x in e['V1'] if x['start'] < 212.19] + [{'start': 212.2, 'end': 214.6, 'src': [x for x in e['V1'] if x['start'] > 218][0]['src'], 'in': 1.36, 'shot': 'logo (Jack, in Premiere)'}]
e['V1'] = [x for x in e['V1'] if not (x['start'] < 212.19 and x['end'] > 212.21)] + [dict(x, end=212.2) for x in e['V1'] if x['start'] < 212.19 and x['end'] > 212.21]
e['V1'].sort(key=lambda x: x['start']); e['total'] = 214.6
log.append("Jack's ending from beat 6 kept: logo at 212.2-214.6, song ends 214.6")
json.dump(e, open(HERE / 'edl-beat7.json', 'w'), indent=1)
v1 = e['V1']
gaps = [(round(a['end'], 2), round(b['start'], 2)) for a, b in zip(v1, v1[1:]) if abs(b['start'] - a['end']) > 0.03]
print('\n'.join(log)); print('V1', len(v1), 'V2', len(e['V2']), 'V3', len(e['V3']), 'gaps', gaps, 'drop', d0, d1)
