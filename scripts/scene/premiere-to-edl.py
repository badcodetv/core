#!/usr/bin/env python3
"""Turn a hand-cut Premiere sequence into a timeline-format edl, so it can have a timeline page.

    python3 scripts/scene/premiere-to-edl.py <state.json> <edl.json> [--end SECONDS] [--title T]
        [--from <previous edl.json>] [--by NAME] [--render <render.mp4>] [--stem A1=sfx-clip-sound ...] [--beats-from A3,A4]

--from: the edl the page showed before this Premiere edit. Its beats, words and headings are kept, and each
  shot that is still there keeps its note; anything new or moved is marked as NAME's hand edit (--by, default
  Kai). Clips are matched by their path inside the story folder, so an edit saved on another machine matches.
--render: Premiere's own render of the sequence, scaled to 1080p as preview.mp4 beside the edl.

<state.json> is the bridge's dump of the sequence (premiere_get_sequence writes
<project dir>/.bridge/state-<sequence>.json). The other direction from premiere-plan.py: here
Premiere is the source and the page follows it (a cut Kai made by hand, e.g. "01 GPOM start").

- Beats come from the sequence markers (each marker = one beat; a marker starting at/after --end is dropped).
- Picture: every clip on every unmuted video track, merged into one lane in start order (a two-track
  checkerboard edit reads as one row of shots; overlaps are the crossfades).
- Sound: each unmuted audio track with clips becomes one stem; each clip one event.
- Effects, speed ramps and transitions are not carried: the page plays the render as the truth.
The preview (the playable cut) is the sequence's own render, trimmed; this script only writes the edl.
"""
import argparse
import json
import pathlib
import re
import os as _os, sys as _sys  # cut files written on another machine open on this one (scripts/drive/localmap.py)
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'drive'))
from localmap import localize, story_relpath, to_shell  # noqa: E402
import subprocess

ap = argparse.ArgumentParser()
ap.add_argument('state')
ap.add_argument('edl')
ap.add_argument('--end', type=float)
ap.add_argument('--title')
ap.add_argument('--from', dest='prev')
ap.add_argument('--by', default='Kai')
ap.add_argument('--render')
ap.add_argument('--stem', action='append', default=[], metavar='A1=sfx-clip-sound',
                help='name a track\'s stem (kind-name: vox, mus or sfx); default mus-<track>')
ap.add_argument('--beats-from', metavar='A3,A4',
                help='no markers? one beat per clip on these tracks (e.g. the music cues), titled by clip name')
a = ap.parse_args()
STEM_NAMES = dict(x.split('=', 1) for x in a.stem)

st = localize(json.loads(pathlib.Path(a.state).read_text()))
for _tr in st.get('videoTracks', []) + st.get('audioTracks', []):  # D:\\x -> /mnt/d/x here, so file names read cleanly
    for _it in _tr.get('items', []):
        if isinstance(_it.get('mediaPath'), str):
            _it['mediaPath'] = to_shell(_it['mediaPath'])
seq = st['sequence']
end = a.end or seq['end']

mk = st.get('markers', [])
mk = mk.get('items', []) if isinstance(mk, dict) else mk
marks = [m for m in mk if m['start'] < end - 0.05]
if not marks and a.beats_from:
    want = {t.strip().upper() for t in a.beats_from.split(',')}
    cues = [it for tr in st['audioTracks'] if tr['label'].upper() in want for it in tr.get('items', [])
            if it['start'] < end - 0.05]
    cues.sort(key=lambda it: it['start'])
    nice = lambda n: re.sub(r'([-_ ]\d+[a-z]?)+$', '', re.sub(r'^[a-z]*[-_ ]?\d+[-_ ](\d+[-_ ])?', '', pathlib.Path(n).stem)
                            ).replace('-', ' ').strip().capitalize()  # m10-01-cafe, ms-02-plan-7e -> Cafe, Plan
    marks = [{'name': nice(it['name']), 'start': 0.0 if i == 0 else it['start'],
              'duration': (cues[i + 1]['start'] if i + 1 < len(cues) else end) - (0.0 if i == 0 else it['start'])}
             for i, it in enumerate(cues)]
beats = [{'id': str(i), 'title': m['name'], 'start': round(m['start'], 3),
          'dur': round(min(m['start'] + m['duration'], end) - m['start'], 3),
          'see': m.get('comments', ''), 'lines': []} for i, m in enumerate(marks)]
if not beats:
    beats = [{'id': '0', 'title': seq['name'], 'start': 0.0, 'dur': round(end, 3), 'lines': []}]


def beat_at(t):
    cur = beats[0]['id']
    for b in beats:
        if t >= b['start'] - 0.01:
            cur = b['id']
    return cur


video = []
for tr in st['videoTracks']:
    if tr.get('muted'):
        continue
    for it in tr.get('items', []):
        if it.get('disabled') or it['start'] >= end:
            continue
        video.append({'file': it['mediaPath'], 'source': it['mediaPath'], 'start': round(it['start'], 3),
                      'dur': round(min(it['end'], end) - it['start'], 3), 'beat': beat_at(it['start']),
                      'track': tr['label'], 'in': round(it.get('inPoint', 0), 3), 'speed': it.get('speed', 1)})
video.sort(key=lambda c: (c['start'], c['track']))

audio, events = [], []
for tr in st['audioTracks']:
    items = [it for it in tr.get('items', []) if not tr.get('muted') and not it.get('disabled') and it['start'] < end]
    if not items:
        continue
    stem = STEM_NAMES.get(tr['label'], f"mus-{tr['label'].lower()}")
    audio.append({'track': tr['label'], 'name': stem})
    for it in items:
        events.append({'stem': stem, 't': round(it['start'], 3), 'dur': round(min(it['end'], end) - it['start'], 3),
                       'what': it['name'], 'src': it['mediaPath']})

fps = 24
if a.prev:  # carry the page forward: its beats and words, and each surviving shot's note
    prev = localize(json.loads(pathlib.Path(a.prev).read_text()))
    fps, beats = prev.get('fps', fps), prev['beats']
    rel = lambda p: (story_relpath(p)[1] or p).lower()
    kept = 0
    for c in video:
        c['beat'] = beat_at(c['start'])
        same = [v for v in prev['video'] if rel(v['file']) == rel(c['file']) and abs(v['start'] - c['start']) < 1.5]
        exact = [v for v in same if abs(v['start'] - c['start']) < 0.05 and abs(v['dur'] - c['dur']) < 0.05]
        if exact:
            c.update({k: exact[0][k] for k in ('why', 'id', 'beat') if k in exact[0]}); kept += 1
        elif same:
            c.update({k: same[0][k] for k in ('id', 'beat') if k in same[0]})
            c['why'] = same[0].get('why', '') + f' ({a.by} re-trimmed it in Premiere)'
        else:
            c['why'] = f"{a.by}'s hand edit in Premiere"
    for b in beats:
        b['see'] = f"{sum(1 for v in video if v['beat'] == b['id'])} shots. " + (b.get('see') or '').split('. ', 1)[-1]

edl = {'sequence': seq['name'], 'fps': fps, 'total': round(end, 3), 'beats': beats, 'video': video,
       'audio': audio, 'events': events,
       'flags': ['Built from the Premiere sequence as Kai cut it by hand; the video plays its render. '
                 'Crossfades show as overlapping shots; effects are in the render, not listed.']}
if a.prev:
    edl.update({k: prev[k] for k in ('title', 'heading') if k in prev})
    edl['intro'] = (f"{a.by}'s edit in Premiere (sequence {seq['name']}), brought back onto this page shot for shot: "
                    f"{kept} shots as before, {len(video) - kept} hand edits (marked in each shot's note).")
    edl['flags'] = []
if a.title:
    edl['title'] = a.title
if a.render:
    edl['render'] = a.render
    pathlib.Path(a.edl).parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', a.render, '-vf', 'scale=1920:1080', '-c:v', 'libx264', '-preset',
                    'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
                    str(pathlib.Path(a.edl).parent / 'preview.mp4')], check=True)
pathlib.Path(a.edl).parent.mkdir(parents=True, exist_ok=True)
pathlib.Path(a.edl).write_text(json.dumps(edl, indent=1))
print(json.dumps({'beats': len(beats), 'clips': len(video), 'stems': len(audio), 'total': end}))
