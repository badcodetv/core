#!/usr/bin/env python3
"""Build the second half's script page: every beat in cut order, its picture, its words, a notes box per line.

    python3 scripts/gpom/second-half-video/build-script-page.py <out-dir>

Order and timecodes come from the rough cut (rough-cut.json, timing.py) because that is the timeline
Kai is watching; the words, effects and HUD come from second-half-audio-plan.json (the single source:
the page shows them, it does not hold them). Kai's notes go in the page's db, collection `script`,
doc `<key>__<user>` where key is `top`, `bridge`, `b<frame>` or `l<frame>-<line>`.
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import shots as S  # noqa: E402

SLUG = {
    'hunt': 'EXT. THE DOWNS NEAR SWINDON. DAY',
    'row': 'INT. THE BUNKER UNDER THE HILL',
    'kill': 'EXT. THE DOWNS. KILL MODE',
    'gate': 'EXT. / INT. THE BLAST DOORS',
    'meet': 'INT. THE BUNKER CANTEEN',
    'clean': 'INT. THE TIME MACHINE',
    'end': 'EXT. A HIGH STREET. NOW',
}

out = pathlib.Path(sys.argv[1])
media = out / 'media'
media.mkdir(parents=True, exist_ok=True)
plan = json.loads((S.SCENES / 'second-half-audio-plan.json').read_text())
board = json.loads((S.SCENES / 'second-half-storyboard.json').read_text())
rc = json.loads((S.CLIPS / 'audio' / 'rough-cut.json').read_text())
frames = {f['n']: f for f in board['frames']}
acts = {a['id']: a for a in board['acts']}
who = {v['id']: v['name'] for v in plan['voices']}

beats = []
for k, (name, t, i, d, n, ext) in enumerate(rc['clips']):
    thumb = media / f'sc-{k:02d}.jpg'
    if not thumb.exists():
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', str(i + min(d / 2, 2.0)), '-i', str(S.OUT / name),
                        '-frames:v', '1', '-vf', 'scale=360:-2', '-q:v', '4', str(thumb)], check=True)
    if beats and beats[-1]['n'] == n:
        beats[-1]['thumbs'].append(f'media/{thumb.name}')
        beats[-1]['d'] = round(t + d - beats[-1]['t'], 2)
        continue
    f, p = frames[n], plan['shots'].get(str(n), {})
    beats.append({'n': n, 't': t, 'd': d, 'act': f['act'], 'actTitle': acts[f['act']]['title'], 'slug': SLUG[f['act']],
                  'title': f['title'], 'see': f['line'], 'thumbs': [f'media/{thumb.name}'],
                  'lines': [[w, who.get(w, w), text] for w, text in p.get('lines', [])],
                  'sfx': p.get('sfx', ''), 'hud': p.get('hud', ''),
                  'cue': next((c['id'] + ' · ' + c['name'] for c in plan['cues'] if c['frames'][0] <= n <= c['frames'][1]), '')})

opening = plan.get('opening')
shot = pathlib.Path('/mnt/c/Users/kai/Pictures/Screenshots/Screenshot 2026-10-19 154346.png')  # Kai's frame of the bot shot
if opening and shot.exists() and not (media / 'opening.jpg').exists():
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(shot), '-vf', 'scale=720:-2', '-q:v', '4', str(media / 'opening.jpg')], check=True)
if opening:
    opening = {**opening, 'thumb': 'media/opening.jpg' if (media / 'opening.jpg').exists() else None,
               'drafts': [{**x, 'lines': [[w, who.get(w, w), t] for w, t in x['lines']]} for x in opening['drafts']]}
data = {'beats': beats, 'total': rc['total'], 'opening': opening}
page = (HERE / 'script-template.html').read_text().replace('/*DATA*/null', json.dumps(data))
(out / 'index.html').write_text(page)
print(json.dumps({'beats': len(beats), 'lines': sum(len(b['lines']) for b in beats), 'total': rc['total'],
                  'thumbs': len(list(media.iterdir()))}))
