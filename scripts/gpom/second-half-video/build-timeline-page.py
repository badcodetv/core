#!/usr/bin/env python3
"""Build the cut-2 timeline page: the gpom-second-half-rough2 sequence as a playable, notable timeline.

    python3 scripts/gpom/second-half-video/build-timeline-page.py <out-dir>

Reads the cut as built (clips/second-half/audio/cut2/edl.json + rough-cut2.json, written by
`rough_audio.py --cut2`) and the words from second-half-audio-plan.json's `cut2` block. Writes
<out-dir>/index.html, media/cut.mp4 (a small proxy of the render, under the 15 MB file limit) and a
thumbnail per clip. Kai's notes go in the page's db, collection `notes`, doc `<key>__<user>`, where
key is `top`, `b<beat>`, `l<beat>-<i>`, `c<clip>`, `e<event>` or `at<frame>` (a note at the playhead).
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import shots as S  # noqa: E402

C2 = S.CLIPS / 'audio' / 'cut2'
RENDER = S.CLIPS.parent.parent / 'renders' / 'gpom-second-half-rough2.mp4'

out = pathlib.Path(sys.argv[1])
media = out / 'media'
media.mkdir(parents=True, exist_ok=True)
edl = json.loads((C2 / 'edl.json').read_text())
rc = json.loads((C2 / 'rough-cut2.json').read_text())
plan = json.loads((S.SCENES / 'second-half-audio-plan.json').read_text())
names = {v['id']: v['name'] for v in plan['voices']}
words = {b['id']: b for b in plan['cut2']['beats']}


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


proxy = media / 'cut.mp4'
if not proxy.exists() or proxy.stat().st_mtime < RENDER.stat().st_mtime:
    ff('-i', RENDER, '-vf', 'scale=640:-2', '-c:v', 'libx264', '-preset', 'slow', '-b:v', '300k', '-maxrate', '360k',
       '-bufsize', '720k', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '64k', '-ac', '2', '-movflags', '+faststart', proxy)

clips = []
for k, c in enumerate(edl['video']):
    th = media / f'c{k:02d}.jpg'
    if not th.exists():
        ff('-ss', c['start'] + min(c['dur'] / 2, 1.5), '-i', RENDER, '-frames:v', '1', '-vf', 'scale=160:-2', '-q:v', '5', th)
    src = pathlib.Path(c.get('source') or c['file']).name
    clips.append({'k': k, 't': c['start'], 'd': c['dur'], 'beat': c['beat'], 'name': src,
                  'looped': '/rt2/' in c['file'], 'img': f'media/{th.name}'})

beats = []
for b in edl['beats']:
    w = words.get(b['id'], {})
    lines = []
    for ln in rc['lines']:
        if ln['beat'] != b['id'] or ln.get('kind', 'dry') not in ('dry', None):
            continue
        src = (w.get('lines') or [])
        text = src[ln['i']] if ln['i'] < len(src) else {}
        lines.append({'i': ln['i'], 'who': ln['who'], 'name': names.get(ln['who'], ln['who']), 't': ln['t'], 'd': ln['dur'],
                      'text': text.get('text', ''), 'by': text.get('by', '')})
    # Lines with no take of their own (beat 4 reuses the row) still show their words.
    have = {x['i'] for x in lines}
    for i, text in enumerate(w.get('lines') or []):
        if i not in have:
            lines.append({'i': i, 'who': text['who'], 'name': names.get(text['who'], text['who']), 't': None, 'd': 0,
                          'text': text['text'], 'by': text.get('by', '')})
    lines.sort(key=lambda x: (x['t'] is None, x['t'] or 0, x['i']))
    beats.append({'id': b['id'], 'title': b['title'], 't': b['start'], 'd': b['dur'], 'see': w.get('see', ''),
                  'act': w.get('act', ''), 'lines': lines})

tracks = []
for a in edl['audio']:
    kind = a['name'].split('-')[0]
    ev = [{'k': k, 't': e['t'], 'd': e['dur'], 'what': e['what'], 'src': pathlib.Path(e['src']).name}
          for k, e in enumerate(edl['events']) if e['stem'] == a['name']]
    tracks.append({'track': a['track'], 'name': a['name'].split('-', 1)[1], 'kind': kind, 'events': ev})

data = {'total': edl['total'], 'fps': 24, 'beats': beats, 'clips': clips, 'tracks': tracks, 'flags': edl.get('flags', []),
        'sequence': edl.get('sequence', 'gpom-second-half-rough2')}
page = (HERE / 'timeline-template.html').read_text().replace('/*DATA*/null', json.dumps(data, ensure_ascii=False))
(out / 'index.html').write_text(page)
print(json.dumps({'beats': len(beats), 'clips': len(clips), 'tracks': len(tracks), 'events': len(edl['events']),
                  'proxyMB': round(proxy.stat().st_size / 1e6, 1)}))
