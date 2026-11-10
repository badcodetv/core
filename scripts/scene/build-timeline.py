#!/usr/bin/env python3
"""Build a scene's timeline page (new-scene stage 4) from its rough cut.

    python3 scripts/scene/build-timeline.py docs/stories/<story>/scenes/<scene> <out-dir>

Reads scene.json's "cut": {"edl": ..., "preview": ...} (defaults <media>/cut/edl.json and
<media>/cut/preview.mp4). The edl is in the timeline format documented in timeline.py.
Merges <scene-dir>/cut-notes.json (round, plan, replies) when present, and the newest copy of the page's
notes in <scene-dir>/feedback/timeline*/notes/ (everyone's, signed), so a page rebuilt from the repo alone, on
any machine and at any link, shows the notes Claude answered. Notes typed since that copy live only online.
Prints the files to publish alongside out-dir/index.html.
"""
import json
import pathlib
import sys
import os as _os, sys as _sys  # cut files written on another machine open on this one (scripts/drive/localmap.py)
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'drive'))
from localmap import localize  # noqa: E402

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from scene import Scene  # noqa: E402
import timeline  # noqa: E402

sc = Scene(sys.argv[1])
cut = sc.cfg.get('cut', {})
edl = pathlib.Path(cut.get('edl', sc.media / 'cut' / 'edl.json'))
preview = pathlib.Path(cut.get('preview', sc.media / 'cut' / 'preview.mp4'))
data = localize(json.loads(edl.read_text()))
if not preview.exists():  # previews never travel through Drive (scripts/drive/exclude.txt): each machine makes its own
    sys.exit(f"no preview on this machine: {preview}\n"
             f"Previews aren't synced; make it here from the edl and clips with this scene's rebuild command "
             f"(the newest 'rebuild' in {sc.dir / 'trail.json'}, or scene.json cut.script), then run this again.")
data.setdefault('title', sc.cfg.get('title', sc.slug) + ' Timeline')
data.setdefault('heading', sc.cfg.get('title', sc.slug))
notes = sc.dir / 'cut-notes.json'  # Claude's read of the notes so far (round, plan, replies), shown on the page
if notes.exists():
    n = json.loads(notes.read_text())
    data.update({k: n[k] for k in ('round', 'plan', 'replies') if k in n})
def newest_notes(scene_dir):
    """The most recent dump of the timeline page's notes: {from, notes:[{key, by, note, at, ...}]}, or None."""
    best = None
    for d in scene_dir.glob('feedback/timeline*/notes'):
        notes = [json.loads(f.read_text()) for f in sorted(d.glob('*.json'))]
        notes = [n for n in notes if isinstance(n, dict) and n.get('key') and (n.get('note') or '').strip()]
        last = max((n.get('at') or 0 for n in notes), default=0)
        if notes and (best is None or last > best[0]):
            best = (last, {'from': str(d.parent.relative_to(scene_dir)), 'notes': notes})
    return best and best[1]


record = newest_notes(sc.dir)
if record:
    data['record'] = record
people = sc.dir.parents[2] / 'people.json'  # optional {"<user id>": "Kai"}: names for notes on a signed-out page
if people.exists():
    data['people'] = json.loads(people.read_text())
print(json.dumps(timeline.build(data, preview, sys.argv[2])))
