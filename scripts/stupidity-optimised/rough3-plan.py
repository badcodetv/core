"""Stupidity Optimised rough 3: the build plan, from rough 2's bridge state (2026-11-02).

Rough 2 is the base. Three ripple inserts (in rough-2 time), the r3 voice swaps, the longer music cues, the lip-synced
shots on V2 and the graphics on V3. Clip sound (A1, linked to V1) is capped so its loudest second sits at -38 dB rms or
lower, and muted on the shots whose Flow sound carries made-up speech. Rough 2 is not touched.

  E1 377.833 (end of shot 55): +1.8 s more of shot 55 (Brandon's longer line), then the 19.8 s water block for 088
  E2 441.167 (end of shot 60): +10.4 s, the label replay, 8 x 1.3 s over Act 2 shots
  E3 469.875 (end of shot 62): +1.3 s, the last piece of shot 62 runs longer for the new 072

  python3 scripts/stupidity-optimised/rough3-plan.py r2state.json lipsync-r3.json out/rough3-plan.json

Plan: {"video": [[path, t, in, dur, track]], "audio": [[path, t, track, level_db]], "a1": [[t, level_db]], "total"}.
Paths are Windows form. level_db is clip Volume relative to 0 dB; None = mute.
"""
import json, math, os, subprocess, sys
import numpy as np

state, ls_manifest, out = sys.argv[1:4]
S = json.load(open(state))
LS = json.load(open(ls_manifest)) if os.path.exists(ls_manifest) else {}
ROOT = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/optimised stupidity/clips/film'
VID, GFX, VOX, MUS = f'{ROOT}/video', f'{ROOT}/gfx', f'{ROOT}/voices/trimmed-r3', f'{ROOT}/music/cues'
E1, E2, E3 = 377.8333, 441.1667, 469.0417  # E3: in rough 2's timeline shot 62 ends here (its last sliver merged into 63)
INS1, INS2, INS3 = 21.6, 10.4, 1.6
BABBLE = {7, 14, 47, 54}
A1_CAP = -38.0


def f(t):
    """rough-2 time -> rough-3 time"""
    return t + (INS1 if t >= E1 - 1e-3 else 0) + (INS2 if t >= E2 - 1e-3 else 0) + (INS3 if t >= E3 - 1e-3 else 0)


def win(p):
    return p[5].upper() + ':' + p[6:].replace('/', '\\') if p.startswith('/mnt/') else p


def level(c):
    for comp in c.get('components', []):
        if comp['displayName'] == 'Volume':
            for p in comp['params']:
                if p['name'] == 'Level':
                    return round(20 * math.log10(max(p['value'], 1e-6) / 0.17782794), 2)
    return 0.0


def shot_of(name):
    return int(name.split('-')[1]) if name.startswith('so-') else 72


V1 = sorted(S['videoTracks'][0]['items'], key=lambda c: c['start'])
A2 = S['audioTracks'][1]['items']
A3 = S['audioTracks'][2]['items']
first = {}
for c in V1:
    first.setdefault(shot_of(c['name']), c)

video, audio = [], []
for c in V1:
    d = c['end'] - c['start']
    video.append([c['mediaPath'], f(c['start']), c['inPoint'], d, 0, shot_of(c['name'])])
# E3: shot 62 runs on for the longer 072 (its clip is used up, so it repeats from the start, rough 2's convention)
video.append([first[62]['mediaPath'], f(E3 - 0.01) + 0.01, 0, INS3, 0, 62])

# E1: shot 55 runs on (0.75 s, its own clip continuing), a 1.05 s cutaway to the hall (53), then the water block
p55, p53 = first[55]['mediaPath'], first[53]['mediaPath']
t = E1
video += [[p55, t, 7.25, 0.75, 0, 55], [p53, t + 0.75, 3.0, 1.05, 0, 53]]
B = E1 + 1.8
video += [[f'{GFX}/gfx-leaflet.mp4', B, 0, 6.2, 0, None],
          [first[15]['mediaPath'], B + 6.2, 1.0, 6.0, 0, 15],
          [p55, B + 12.2, 0.5, 3.4, 0, 55],
          [first[62]['mediaPath'], B + 15.6, 0, 4.2, 0, 62]]
video.append([f'{GFX}/gfx-62-plan.mov', B + 15.6, 0, 4.2, 2, None])
audio.append([f'{VOX}/088-narrator.wav', B + 0.4, 1, 0.0])

# E2: the label replay
L = [(40, 'uptime'), (48, 'field-fitness'), (36, 'signature'), (51, 'access'), (54, 'source-meeting'),
     (53, 'infiltration'), (56, 'debrief'), (49, 'handler')]
t = E2 + INS1
for i, (sh, nm) in enumerate(L):
    video.append([first[sh]['mediaPath'], t + i * 1.3, 2.0, 1.3, 0, sh])
    video.append([f'{GFX}/gfx-label-{i + 1}-{nm}.mov', t + i * 1.3, 0, 1.3, 2, None])

# voices: rough 2's, swapped where r3 replaced a line
SWAP = {'059-jenny.wav': '059r3-jenny.wav', '065-brandon.wav': '065r3-brandon.wav', '072-narrator.wav': '072r3-narrator.wav'}
for c in A2:
    if c['name'] in SWAP:
        audio.append([f'{VOX}/{SWAP[c["name"]]}', f(c['start']), 1, 0.0])  # baked at -16 LUFS
    else:
        audio.append([c['mediaPath'], f(c['start']), 1, level(c)])
# music: m5 and m6 longer
for c in A3:
    p = c['mediaPath']
    if c['name'] in ('m5.wav', 'm6.wav'):
        p = f'{MUS}/{c["name"][:2]}-r3.wav'
        audio.append([p, f(c['start']), 2, 3.5])  # the r3 cuts measure -32.5 to -32.8 against rough 2's -32.0 at +3
    else:
        audio.append([p, f(c['start']), 2, level(c)])

# lip sync on V2
for shot, m in LS.items():
    fd = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', m['file']],
                              capture_output=True, text=True).stdout)
    video.append([m['file'], f(m['t0']), 0, math.floor(min(m['t1'] - m['t0'], fd) * 24 - 0.5) / 24, 1, int(shot)])

# graphics on V3, from each shot's start (rough-2 shots dict via V1)
starts = {}
for c in V1:
    starts.setdefault(shot_of(c['name']), c['start'])
ends = {}
for c in V1:
    ends[shot_of(c['name'])] = c['end']
G = [('06-search', 6, 5), ('35-lockad', 35, 5), ('36-firstuse', 36, 8.2), ('43-perms', 43, 13), ('46-partner', 46, 8.4),
     ('50-sorry', 50, 8.8), ('56-journal', 56, 15.8), ('63-goals', 63, 14), ('64-badge', 64, 7.4), ('66-complete', 66, 3.5)]
for nm, sh, d in G:
    t0 = f(starts[sh]); d = min(d, f(ends[sh] - 0.001) + 0.001 - t0)
    video.append([f'{GFX}/gfx-{nm}.mov', t0, 0, d, 2, None])
# ambulance flashes, centred on the cut
for sh in (10, 24, 32, 27, 29, 31):
    video.append([f'{GFX}/gfx-flash.mov', f(starts[sh]) - 0.45, 0, 0.9, 2, None])


# clip sound: loudest second of each V1 piece
def loudest(path, ss, dur):
    b = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{ss:.3f}', '-t', f'{dur:.3f}', '-i', path, '-vn', '-ac', '1', '-ar', '8000',
                        '-f', 'f32le', '-'], capture_output=True).stdout
    x = np.frombuffer(b, np.float32)
    if len(x) < 800:
        return None
    w = 8000 if len(x) >= 8000 else len(x)
    c = np.cumsum(np.concatenate([[0], x.astype(np.float64) ** 2]))
    r = np.sqrt((c[w:] - c[:-w]) / w).max()
    return 20 * math.log10(max(r, 1e-9))


a1 = []
for p, t, i, d, tr, sh in video:
    if tr != 0 or not p.endswith('.mp4') or '/gfx/' in p:
        continue
    if sh in BABBLE:
        a1.append([t, None]); continue
    pk = loudest(p, i, d)
    a1.append([t, None if pk is None else round(min(0.0, A1_CAP - pk), 1)])

total = max(t + d for _, t, _, d, _, _ in video)
plan = {'video': [[win(p), round(t, 4), round(i, 4), round(d, 4), tr] for p, t, i, d, tr, _ in sorted(video, key=lambda v: (v[4], v[1]))],
        'audio': [[win(p), round(t, 4), tr, lv] for p, t, tr, lv in sorted(audio, key=lambda a: (a[2], a[1]))],
        'a1': sorted(a1), 'total': round(total, 4)}

# checks: overlaps per track, V1 gaps
for tr in (0, 1, 2):
    vs = sorted([v for v in plan['video'] if v[4] == tr], key=lambda v: v[1])
    for a, b in zip(vs, vs[1:]):
        if a[1] + a[3] > b[1] + 0.02:
            print(f'V{tr + 1} overlap {a[0].split(chr(92))[-1]} @{a[1]:.2f}+{a[3]:.2f} > {b[0].split(chr(92))[-1]} @{b[1]:.2f}')
        if tr == 0 and b[1] - (a[1] + a[3]) > 0.02:
            print(f'V1 gap at {a[1] + a[3]:.2f}')
for tr in (1, 2):
    As = sorted([a for a in plan['audio'] if a[2] == tr], key=lambda a: a[1])
    for a, b in zip(As, As[1:]):
        da = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0',
                                   '/mnt/' + a[0][0].lower() + a[0][2:].replace('\\', '/')], capture_output=True, text=True).stdout)
        if a[1] + da > b[1] + 0.02:
            print(f'A{tr + 1} overlap {a[0].split(chr(92))[-1]} ends {a[1] + da:.2f} > {b[0].split(chr(92))[-1]} @{b[1]:.2f}')
json.dump(plan, open(out, 'w'), indent=0)
print('video', len(plan['video']), 'audio', len(plan['audio']), 'total', plan['total'])
