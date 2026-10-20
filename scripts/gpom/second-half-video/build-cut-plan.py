#!/usr/bin/env python3
"""Build the cut-2 plan page: an animatic of beats 0-18 plus the words, new shots, voices, music and effects.

    python3 scripts/gpom/second-half-video/build-cut-plan.py <out-dir>

Reads `cut2` and `voices` from second-half-audio-plan.json (the single source) and frame thumbnails
from the rough cut's clips. Durations are estimates: the rough-cut length of the frame, stretched to
fit the words at WPS words a second (timing.py's rule). Kai's notes go in the page's db, collection
`plan`, doc `<key>__<user>`.
"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import edl  # noqa: E402
import shots as S  # noqa: E402

WPS, LEAD, GAP, TAIL = 2.6, 0.4, 0.35, 0.6
PAUSE = {'[pause]': 0.6, '[short pause]': 0.4, '[long pause]': 1.2}
NEW_LEN = {'13': 3.0, '14a': 4.5, '14b': 0.0, '12': 3.0, '11b': 2.0}
OPENING = pathlib.Path('/mnt/c/Users/kai/Pictures/Screenshots/Screenshot 2026-10-19 154346.png')

out = pathlib.Path(sys.argv[1])
media = out / 'media'
media.mkdir(parents=True, exist_ok=True)
plan = json.loads((S.SCENES / 'second-half-audio-plan.json').read_text())
rc = json.loads((S.CLIPS / 'audio' / 'rough-cut.json').read_text())
cut = plan['cut2']
names = {v['id']: v['name'] for v in plan['voices']}


def thumb(name, i, d, tag):
    f = media / f'{tag}.jpg'
    if not f.exists():
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', str(i + min(d / 2, 2.0)), '-i', str(S.OUT / name),
                        '-frames:v', '1', '-vf', 'scale=640:-2', '-q:v', '4', str(f)], check=True)
    return f'media/{f.name}'


# A frame's own length is its first-assembly length (edl.py): the rough cut stretched frames to the OLD words.
frame_len = {}
for name, t, i, d, n, note in edl.entries():
    frame_len[n] = frame_len.get(n, 0) + d
# First clip of each frame (and the CCTV replay, 18b) from the rough cut, for the pictures.
frame_img, cctv = {}, None
for k, (name, t, i, d, n, ext) in enumerate(rc['clips']):
    if n not in frame_img:
        frame_img[n] = thumb(name, i, d, f'f{n:02d}')
    if '18b' in name:
        cctv = thumb(name, i, d, 'cctv')
if OPENING.exists() and not (media / 'opening.jpg').exists():
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(OPENING), '-vf', 'scale=640:-2', '-q:v', '4',
                    str(media / 'opening.jpg')], check=True)


def say_len(text, who):
    if who == 'crowd':
        return 2.5
    pause = sum(v * text.count(k) for k, v in PAUSE.items())
    words = len(re.sub(r'\[[^\]]*\]', '', text).split())
    return round(words / WPS + pause, 2)


beats = []
for b in cut['beats']:
    lines = [{**ln, 'name': names.get(ln['who'], ln['who']), 'len': say_len(ln['text'], ln['who'])} for ln in b['lines']]
    talk = LEAD + sum(x['len'] for x in lines) + GAP * max(0, len(lines) - 1) + TAIL if lines else 0
    pic = b['pic']
    base = NEW_LEN.get(b['id'], frame_len.get(pic.get('frame'), 3.0) if pic['kind'] == 'have' else 3.5)
    if b['id'] == '0':
        base = 3.0  # the roll-off over the camera, after she stops talking
        talk += 2.0  # she rolls up before she speaks
    if b['id'] == '8':
        base += 1.0  # the muffled row plays over the POV before the flip
    dur = round(max(base if b['id'] != '0' else 0, talk) + (base if b['id'] == '0' else 0), 1)
    img = 'media/opening.jpg' if pic.get('frame') == 'opening' else frame_img.get(pic.get('frame')) if pic['kind'] == 'have' else None
    frames = [{'img': img, 'shot': pic.get('shot'), 'at': 0}]
    if b['id'] == '17' and cctv:
        frames.append({'img': cctv, 'shot': None, 'at': 0.55})
    beats.append({**b, 'lines': lines, 'dur': dur, 'frames': frames})

shots = {s['id']: s for s in cut['shots']}
data = {'beats': beats, 'shots': cut['shots'], 'music': cut['music'], 'sfx': cut['sfx'], 'sfxNote': cut['sfxNote'],
        'voices': [v for v in plan['voices'] if v['id'] in ('bot', 'ai', 'woman', 'man', 'lady', 'crowd')],
        'total': round(sum(b['dur'] for b in beats), 1)}
page = (HERE / 'cut-plan-template.html').read_text().replace('/*DATA*/null', json.dumps(data, ensure_ascii=False))
(out / 'index.html').write_text(page)
print(json.dumps({'beats': len(beats), 'total': data['total'], 'files': sorted(p.name for p in media.iterdir())}))
