#!/usr/bin/env python3
"""Turn a hand-cut Premiere sequence into a timeline-format edl, so it can have a timeline page.

    python3 scripts/scene/premiere-to-edl.py <state.json> <edl.json> [--end SECONDS] [--title T]

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
import os as _os, sys as _sys  # cut files written on another machine open on this one (scripts/drive/localmap.py)
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'drive'))
from localmap import localize  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument('state')
ap.add_argument('edl')
ap.add_argument('--end', type=float)
ap.add_argument('--title')
a = ap.parse_args()

st = localize(json.loads(pathlib.Path(a.state).read_text()))
seq = st['sequence']
end = a.end or seq['end']

mk = st.get('markers', [])
mk = mk.get('items', []) if isinstance(mk, dict) else mk
marks = [m for m in mk if m['start'] < end - 0.05]
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
    stem = f"mus-{tr['label'].lower()}"
    audio.append({'track': tr['label'], 'name': stem})
    for it in items:
        events.append({'stem': stem, 't': round(it['start'], 3), 'dur': round(min(it['end'], end) - it['start'], 3),
                       'what': it['name'], 'src': it['mediaPath']})

edl = {'sequence': seq['name'], 'fps': 24, 'total': round(end, 3), 'beats': beats, 'video': video,
       'audio': audio, 'events': events,
       'flags': ['Built from the Premiere sequence as Kai cut it by hand; the video plays its render. '
                 'Crossfades show as overlapping shots; effects are in the render, not listed.']}
if a.title:
    edl['title'] = a.title
pathlib.Path(a.edl).parent.mkdir(parents=True, exist_ok=True)
pathlib.Path(a.edl).write_text(json.dumps(edl, indent=1))
print(json.dumps({'beats': len(beats), 'clips': len(video), 'stems': len(audio), 'total': end}))
