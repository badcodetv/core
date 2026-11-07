"""Re-cut `camping song 2 beat 3` to the real beat → plan for `camping song 2 beat 4` (2026-11-07).

Jack: "watch and listen to it, then cut it to the beat with complete freedom, since the cutting/trimming does not match the beat".
Why it didn't: the old pass snapped to librosa's beat list, which is EIGHTH notes (172-176) running ~57 ms late; only 12 of 167
cuts sat on a real beat (median 179 ms off). The song is 88 BPM, straight, snare on 2 and 4 (../analysis/bars.py, the listening
log 2026-11-07-152100). Method from the sealed web research ../cleanroom/research-beat-cut.md ("A procedure for this cut").

Keeps every shot choice and order (the lyric matching stays); throws away every cut time and re-places it:
- every cut on a quarter-note beat, corrected by the local drum offset, 0-1 frame EARLY (picture early is safe, late is not);
- each section opens with a cut on its downbeat (the "1" before the vocal comes in on beat 2);
- minimum holds: verse 2 beats, hook 2 beats, bridge 1 bar, intro/outro 1 beat; anything shorter merges into a neighbour;
- Jack's black-flash stutters are rebuilt on real sixteenth notes: black, then 3-frame flashes one eighth apart over the
  last 2 beats, landing exactly on the beat (the drop).

    python3 recut.py <state json of beat 3>   → edl-beat4.json (V1/V2/V3 pieces) + a report
"""
import json, subprocess, sys
from bisect import bisect_left
from pathlib import Path
import numpy as np
HERE = Path(__file__).parent
FPS = 25
B = json.load(open(HERE.parent / 'analysis/bars.json'))
Q, BAR = B['beat'], B['bar']
beats = np.array(B['beats'])
loc = B['local_offset_ms_per_4_bars']
lt, lo = np.array([x[0] + 2 * BAR for x in loc]), np.array([x[1] for x in loc]) / 1000  # window centres
beats = beats + np.interp(beats, lt, lo)                              # follow the drums' small drift
down = beats[[i for i, b in enumerate(B['beats']) if abs(((b - B['first_downbeat']) / BAR) % 1) < 1e-3 or abs(((b - B['first_downbeat']) / BAR) % 1 - 1) < 1e-3]]
EARLY = 0.02  # → floor to frame gives 0-1 frame early
fr = lambda t: np.floor((t - EARLY) * FPS + 1e-6) / FPS
SECTIONS = [  # (name, vocal/section start in the song, min hold in beats)
    ('logo', 0.0, 1), ('intro', 12.0, 1), ('verse1', 21.0, 2), ('hook1', 56.0, 2), ('verse2', 77.7, 2), ('hook2', 121.6, 2),
    ('bridge', 143.6, 4), ('hook3', 183.7, 2), ('outro', 205.4, 1)]
sec_down = {}
for n, t, _ in SECTIONS[2:]:  # the downbeat at or before the vocal entry (vocals come in on beat 2)
    sec_down[n] = float(down[np.argmin(abs(down - t))])
def section(t):
    s = SECTIONS[0]
    for x in SECTIONS:
        if t >= x[1] - 0.8: s = x
    return s

_len = {}
def clip_len(p):
    if p not in _len:
        try: _len[p] = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p], capture_output=True, text=True).stdout.strip())
        except ValueError: _len[p] = 999.0
    return _len[p]

def snap(t):
    i = np.argmin(abs(beats - t)); return float(beats[i])

state = json.load(open(sys.argv[1]))
END = 220.72
report = {}

def recut_track(items, gaps_are_black):
    """items: [{start,end,src,in}] in order on one track. Returns the re-cut list."""
    out = []
    # 1) find stutter groups: runs of short pieces (<0.3 s) incl. tiny black gaps, ending at a landing piece
    i = 0
    pieces = sorted(items, key=lambda x: x['start'])
    groups = []
    while i < len(pieces):
        j = i
        while j < len(pieces) and pieces[j]['end'] - pieces[j]['start'] < 0.3: j += 1
        if j - i >= 3:   # a stutter: >= 3 micro flashes
            groups.append((i, j)); i = j
        else: i += 1
    stutter_idx = {k for a, b in groups for k in range(a, b)}
    # 2) snap boundaries of normal pieces
    for k, p in enumerate(pieces):
        if k in stutter_idx: continue
        out.append({**p, 's0': p['start'], 'start': snap(p['start']) if p['start'] > 0.05 else 0.0,
                    'end': snap(p['end']) if p['end'] < END - 0.05 else END})
    # 3) section openings: the piece covering a section downbeat gets a cut there (if none within half a beat)
    for n, d in sec_down.items():
        if any(abs(p['start'] - d) < Q / 2 for p in out): continue
        cov = [p for p in out if p['start'] < d < p['end']]
        if not cov: continue
        p = cov[0]
        nxt = min((x for x in out if x['start'] >= p['end'] - 1e-6), key=lambda x: x['start'], default=None)
        if nxt and nxt['start'] - d <= 2 * Q:        # pull the next shot back onto the one
            nxt['s0'] -= nxt['start'] - d; nxt['start'] = d; p['end'] = d
        elif d - p['start'] <= 2 * Q:                # or push this cut forward onto the one
            p['s0'] += d - p['start']; p['start'] = d
    # 4) enforce minimum holds by merging short pieces into the previous one (never into a stutter)
    out.sort(key=lambda x: x['start'])
    merged = []
    for p in out:
        mn = (section(p['start'])[2] if p['src'] else 1) * Q - 0.01  # a black of a beat or more is Jack's; keep it
        if merged and p['end'] - p['start'] < mn and p['end'] > p['start']:
            prev = merged[-1]
            if abs(prev['end'] - p['start']) < 0.01 and prev['src'] and (prev['end'] - prev['start']) >= (p['end'] - p['start']):
                prev['end'] = p['end']; report.setdefault('merged', []).append([round(p['s0'], 2), Path(p['src'] or 'BLACK').name]); continue
        if p['end'] - p['start'] < 0.01:
            report.setdefault('dropped', []).append([round(p['s0'], 2), Path(p['src'] or 'BLACK').name]); continue
        merged.append(p)
    # 5) rebuild stutters on sixteenths: the landing beat is the beat nearest the old group's end
    for a, b in groups:
        g = pieces[a:b]
        land = snap(g[-1]['end'])
        flashes = [x for x in g if x['src']][-4:]
        for m, x in enumerate(flashes):
            st = land - 2 * Q + m * Q / 2
            merged.append({**x, 's0': x['start'], 'start': st, 'end': st + 3 / FPS, 'stutter': True})
        report.setdefault('stutters', []).append(round(land, 3))
    # 6) frame-round (0-1 frame early), fix in points, clip to the clip length
    res = []
    for p in sorted(merged, key=lambda x: x['start']):
        s, e = max(0.0, fr(p['start'])), fr(p['end']) if p['end'] < END - 0.05 else END
        if p.get('stutter'): e = s + 3 / FPS
        if e - s < 1 / FPS - 1e-6: continue
        q = {'start': round(s, 3), 'end': round(e, 3), 'src': p['src'], 'in': None}
        if p['src']:
            L = clip_len(p['src'])
            inp = p['in'] + (s - p['s0'])
            q['in'] = round(max(0.0, min(inp, L - (e - s) - 0.05)), 3)
        res.append(q)
    # no overlaps: each piece ends where the next begins at the latest
    for x, y in zip(res, res[1:]):
        if x['end'] > y['start']: x['end'] = y['start']
    return [x for x in res if x['end'] - x['start'] >= 1 / FPS - 1e-6]

def items(t):
    return [{'start': i['start'], 'end': i['end'], 'src': i['mediaPath'], 'in': i['inPoint']} for i in state['videoTracks'][t]['items']]

V1 = items(0)
# black gaps on V1 are pieces too (Jack's blacks): fill them as src None so they get snapped like the rest
full, t = [], 0.0
for p in sorted(V1, key=lambda x: x['start']):
    if p['start'] - t > 0.01: full.append({'start': t, 'end': p['start'], 'src': None, 'in': None})
    full.append(p); t = p['end']
new = {'V1': [x for x in recut_track(full, True) if x['src']], 'V2': recut_track(items(1), False), 'V3': recut_track(items(2), False)}
json.dump(new, open(HERE / 'edl-beat4.json', 'w'), indent=1)
cuts = sorted({x['start'] for x in new['V1']} | {x['end'] for x in new['V1']})
err = [(c - beats[np.argmin(abs(beats - c))]) * 1000 for c in cuts if 1 < c < 219]
print(json.dumps({'V1': len(new['V1']), 'V2': len(new['V2']), 'V3': len(new['V3']), 'section_downbeats': {k: round(v, 3) for k, v in sec_down.items()},
                  'cut_vs_beat_ms': {'median': round(float(np.median(err)), 1), 'max_abs': round(float(np.max(np.abs(err))), 1)},
                  'stutters': report.get('stutters'), 'merged': len(report.get('merged', [])), 'dropped': len(report.get('dropped', []))}, indent=1))
json.dump(report, open(HERE / 'recut-report.json', 'w'), indent=1)
