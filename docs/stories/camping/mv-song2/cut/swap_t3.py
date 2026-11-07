"""Round 7 (2026-11-07, Jack: "just use T3 locked, understated style for all the clips"): swap every round-6 piece
(cb-<shot>v-...) in a clone of `camping song 2 beat 2` for the T3 clip of the same shot (cb-<shot>t3-...). Same track, slot and length;
in point kept, pulled back so the piece ends inside the clip. Writes swap-t3.json + swap-t3-N.js (premiere_eval bodies).

    python3 swap_venom.py <state json of the clone> <sequence name>
"""
import json, os, re, sys
from pathlib import Path
HERE = Path(__file__).parent
PRE = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/video/premiere/'
WIN = 'C:\\Users\\jackt\\OneDrive\\Desktop\\Youtube Vids\\animation\\songs\\camping vid\\balaclava\\video\\premiere\\'
picks = json.load(open(HERE.parents[1] / 'mv-balaclava/cleanroom/r6/picks.json'))
state = json.load(open(sys.argv[1])); SEQ = sys.argv[2]
USE = float(os.environ.get('USE', 7.9))  # usable clip length
fr = lambda s: round(s * 25) / 25
rows, skip = [], set()
for t in state['videoTracks']:
    for it in t.get('items', []):
        m = re.match(r'cb-(\w\d\d)v-', it.get('name', ''))
        if not m: continue
        i = m.group(1)
        if i not in picks: skip.add(i); continue
        f = f'cb-{i}t3-{i}r6-{picks[i]}.mp4'
        d = fr(it['end'] - it['start'])
        inp = fr(max(0.0, min(it['inPoint'], USE - d)))
        rows.append({'file': f, 'track': t['index'], 'start': fr(it['start']), 'dur': d, 'in': inp})
rows.sort(key=lambda r: r['start'])
for a, b in zip(rows, rows[1:]):  # a slot split in two: the second piece carries on from the first (no repeated move)
    if a['file'] == b['file'] and a['track'] == b['track'] and abs(a['start'] + a['dur'] - b['start']) < 0.01:
        nxt = fr(a['in'] + a['dur'])
        b['in'] = nxt if nxt + b['dur'] <= USE else fr(max(0.0, USE - b['dur']))
missing = sorted({r['file'] for r in rows if not os.path.exists(PRE + r['file'])})
json.dump(rows, open(HERE / 'swap-t3.json', 'w'), indent=1)
BODY = (HERE.parents[1] / 'mv-balaclava/premiere/swap.py').read_text().split('BODY = r"""', 1)[1].split('"""', 1)[0]
BODY = BODY.replace("const BIN='balaclava clips'", "const BIN='t3 rap clips'").replace('balaclava swap', 't3 swap')
for f in HERE.glob('swap-t3-*.js'): f.unlink()
for n, k in enumerate(range(0, len(rows), 10)):
    (HERE / f'swap-t3-{n}.js').write_text(BODY.replace('__V__', json.dumps(rows[k:k + 10])).replace('__S__', json.dumps(SEQ)).replace('__PRE__', json.dumps(WIN)))
print(len(rows), 'pieces; not swapped (no r6 clip):', sorted(skip), '; files missing:', missing)
