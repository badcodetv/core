#!/usr/bin/env python3
"""Build the second half's timeline + audio plan page from the edit list and the audio plan.

    python3 scripts/gpom/second-half-video/build-audio-plan.py <out-dir>
Writes <out-dir>/index.html and <out-dir>/media/thumb-NN.jpg (a frame from each shot's clip).
Kai's notes go in the page's db, collection `notes` (doc `<shot>__<user>`).
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import edl  # noqa: E402
import shots as S  # noqa: E402

out = pathlib.Path(sys.argv[1])
media = out / 'media'
media.mkdir(parents=True, exist_ok=True)
plan = json.loads((S.SCENES / 'second-half-audio-plan.json').read_text())

rows = []
for k, (name, t, i, d, n, note) in enumerate(edl.entries()):
    thumb = media / f'thumb-{k:02d}.jpg'
    if not thumb.exists():
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', str(i + min(d / 2, 1.5)), '-i', str(S.OUT / name),
                        '-frames:v', '1', '-vf', 'scale=320:-2', '-q:v', '4', str(thumb)], check=True)
    p = plan['shots'].get(str(n), {})
    first = k == 0 or edl.entries()[k - 1][4] != n
    cue = next((c for c in plan['cues'] if c['frames'][0] <= n <= c['frames'][1]), None)
    rows.append({'k': k, 'n': n, 'file': name, 't': t, 'd': d, 'title': note, 'thumb': f'media/{thumb.name}',
                 'lines': p.get('lines', []) if first else [], 'sfx': p.get('sfx', '') if first else '',
                 'hud': p.get('hud', ''), 'cue': cue['id'] if cue else None})

data = {'rows': rows, 'voices': plan['voices'], 'cues': plan['cues'], 'themes': plan['themes'], 'approach': plan['approach'], 'total': rows[-1]['t'] + rows[-1]['d']}
page = (HERE / 'audio-plan-template.html').read_text().replace('/*DATA*/null', json.dumps(data))
(out / 'index.html').write_text(page)
print(json.dumps({'rows': len(rows), 'total': data['total'], 'files': sorted(p.name for p in media.iterdir())}))
