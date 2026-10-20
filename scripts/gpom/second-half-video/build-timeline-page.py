#!/usr/bin/env python3
"""Build the cut-2 timeline page: the gpom-second-half-rough2 sequence as a playable, notable timeline.

    python3 scripts/gpom/second-half-video/build-timeline-page.py <out-dir>

Turns the cut as built (clips/second-half/audio/cut2/edl.json + rough-cut2.json, written by
`rough_audio.py --cut2`) and the words from second-half-audio-plan.json's `cut2` block into the
timeline format, then renders it with the new-scene tool (scripts/scene/timeline.py, which documents
the format and where notes land).
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.append(str(HERE.parents[1] / 'scene'))  # after HERE: scene/ has its own shots.py
import shots as S  # noqa: E402
import timeline  # noqa: E402

C2 = S.CLIPS / 'audio' / 'cut2'
RENDER = S.CLIPS.parent.parent / 'renders' / 'gpom-second-half-rough2.mp4'

edl = json.loads((C2 / 'edl.json').read_text())
rc = json.loads((C2 / 'rough-cut2.json').read_text())
plan = json.loads((S.SCENES / 'second-half-audio-plan.json').read_text())
names = {v['id']: v['name'] for v in plan['voices']}
words = {b['id']: b for b in plan['cut2']['beats']}
notes = json.loads((S.SCENES / 'second-half-cut2-notes.json').read_text())  # Claude's read of Kai's notes, per round

beats = []
for b in edl['beats']:
    w = words.get(b['id'], {})
    said = w.get('lines') or []
    lines = [{'i': ln['i'], 'who': ln['who'], 'name': names.get(ln['who'], ln['who']), 't': ln['t'], 'dur': ln['dur'],
              'text': said[ln['i']]['text'] if ln['i'] < len(said) else '', 'by': said[ln['i']].get('by', '') if ln['i'] < len(said) else ''}
             for ln in rc['lines'] if ln['beat'] == b['id'] and ln.get('kind', 'dry') == 'dry']
    # Lines with no take of their own (beat 4 reuses the row) still show their words.
    have = {x['i'] for x in lines}
    lines += [{'i': i, 'who': x['who'], 'name': names.get(x['who'], x['who']), 't': None, 'dur': 0, 'text': x['text'], 'by': x.get('by', '')}
              for i, x in enumerate(said) if i not in have]
    lines.sort(key=lambda x: (x['t'] is None, x['t'] or 0, x['i']))
    beats.append({**b, 'see': w.get('see', ''), 'act': w.get('act', ''), 'lines': lines})

data = {**edl, 'beats': beats, 'video': [{**c, 'looped': '/rt2/' in c['file']} for c in edl['video']],
        'round': notes['round'], 'plan': notes['plan'], 'replies': notes['replies'],
        'title': 'Cut 2 Timeline', 'heading': 'GPOM second half · cut 2, part 1',
        'intro': 'The gpom-second-half-rough2 sequence as it stands in Premiere, beats 0–18. Play it, click any beat, '
                 "clip, line or sound, and leave a note in its yellow slip. Notes save as you type. Tell Claude when you're done."}
print(json.dumps(timeline.build(data, RENDER, sys.argv[1])))
