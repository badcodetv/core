#!/usr/bin/env python3
"""Karen Story: the Premiere sequence -> a timeline-page edl, dressed with beats and the narration's words.

    python3 scripts/karen/story-edl.py <state.json> <edl.json> [--render <render.mp4>] [--from <previous edl.json>]

Karen Story was cut in Premiere before the timeline tool existed (Jack, Aug-Oct 2026). This runs the generic
scripts/scene/premiere-to-edl.py, then:
- splits the film into beats by the narration's chunks (scripts/karen/narration-v2.tsv, column 2), each beat
  starting at the shot that is on screen when its first line starts;
- puts every narration line on the page with its words (A2 clips are named lvl*_<id>*.wav);
- names the stems: A1 clip sound, A2 narration, A4 score, A5 hold music. Muted tracks (A3, the old ElevenLabs
  narrator) are left off by premiere-to-edl.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument('state')
ap.add_argument('edl')
ap.add_argument('--render')
ap.add_argument('--from', dest='prev')
a = ap.parse_args()

cmd = [sys.executable, str(HERE.parent / 'scene' / 'premiere-to-edl.py'), a.state, a.edl, '--title', 'Karen Story Timeline']
if a.render:
    cmd += ['--render', a.render]
if a.prev:
    cmd += ['--from', a.prev]
subprocess.run(cmd, check=True)
edl = json.loads(pathlib.Path(a.edl).read_text())

TITLES = {1: 'The office', 2: 'Fired by A.I. Sean', 3: 'Night out with Susan', 4: 'The morning after',
          5: 'The phone box', 6: 'Susan stays in bed', 7: 'Speaks to the manager', 8: 'Viral',
          9: 'The chat show, and A.I. Sean', 10: 'The President calls back'}
words = {}
for row in (HERE / 'narration-v2.tsv').read_text().splitlines():
    lid, chunk, text = row.split('\t', 2)
    words[lid] = (int(chunk), text)
words['p02'] = words['p01']  # the cut uses the Charon take p02 of the same words

STEMS = {'A1': 'sfx-clip-sound', 'A2': 'vox-narration', 'A4': 'mus-score', 'A5': 'sfx-hold-music'}
rename = {}
for t in edl['audio']:
    new = STEMS.get(t['track'], t['name'])
    rename[t['name']] = new
    t['name'] = new
for e in edl['events']:
    e['stem'] = rename.get(e['stem'], e['stem'])

lines = []
for e in edl['events']:
    if e['stem'] != 'vox-narration':
        continue
    m = re.search(r'_((?:n|p|t)\d+)', e['what'])
    if not m or m.group(1) not in words:
        sys.exit(f'no words for narration clip {e["what"]}')
    chunk, text = words[m.group(1)]
    pres = m.group(1).startswith('p')
    lines.append({'chunk': chunk, 't': e['t'], 'dur': e['dur'], 'text': text,
                  'who': 'president' if pres else 'narrator',
                  'name': 'The President (Charon)' if pres else 'Narrator (Algenib)'})
lines.sort(key=lambda l: l['t'])

shots = sorted(edl['video'], key=lambda c: c['start'])
def cut_before(t):
    return max((c['start'] for c in shots if c['start'] <= t + 0.01), default=0.0)

order = []
for l in lines:
    if not order or order[-1] != l['chunk']:
        order.append(l['chunk'])
starts = [0.0] + [cut_before(next(l['t'] for l in lines if l['chunk'] == ch)) for ch in order[1:]]
end = edl['total']
beats = []
for i, ch in enumerate(order):
    s = starts[i]
    e = starts[i + 1] if i + 1 < len(order) else end
    bl = [{'i': j, 'who': l['who'], 'name': l['name'], 't': round(l['t'], 3), 'dur': round(l['dur'], 3), 'text': l['text']}
          for j, l in enumerate(x for x in lines if x['chunk'] == ch)]
    beats.append({'id': str(i), 'title': TITLES[ch], 'start': round(s, 3), 'dur': round(e - s, 3), 'lines': bl})

def beat_at(t):
    cur = '0'
    for b in beats:
        if t >= b['start'] - 0.01:
            cur = b['id']
    return cur

for c in edl['video']:
    c['beat'] = beat_at(c['start'])
for b in beats:
    b['see'] = f"{sum(1 for c in edl['video'] if c['beat'] == b['id'])} shots, {len(b['lines'])} lines."
edl['beats'] = beats
edl['heading'] = f"Karen Story: {edl['sequence']}"
edl['intro'] = (f"Karen Story as it stands in Premiere (sequence {edl['sequence']}, Jack's cut), brought onto a timeline "
                "page so it can be noted shot by shot. The video is Premiere's own render; effects, the spray-paint "
                "logo and fades are in the picture, not listed.")
edl['flags'] = ['Beats are the narration chunks (narration-v2.tsv). The old ElevenLabs narrator (muted A3) is left off.']
pathlib.Path(a.edl).write_text(json.dumps(edl, indent=1))
print(json.dumps({'beats': [(b['title'], b['start']) for b in beats], 'lines': len(lines), 'shots': len(edl['video'])}))
