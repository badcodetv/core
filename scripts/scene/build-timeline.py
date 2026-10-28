#!/usr/bin/env python3
"""Build a scene's timeline page (new-scene stage 4) from its rough cut.

    python3 scripts/scene/build-timeline.py docs/stories/<story>/scenes/<scene> <out-dir>

Reads scene.json's "cut": {"edl": ..., "preview": ...} (defaults <media>/cut/edl.json and
<media>/cut/preview.mp4). The edl is in the timeline format documented in timeline.py.
Merges <scene-dir>/cut-notes.json (round, plan, replies) when present.
Prints the files to publish alongside out-dir/index.html.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from scene import Scene  # noqa: E402
import timeline  # noqa: E402

sc = Scene(sys.argv[1])
cut = sc.cfg.get('cut', {})
edl = pathlib.Path(cut.get('edl', sc.media / 'cut' / 'edl.json'))
preview = pathlib.Path(cut.get('preview', sc.media / 'cut' / 'preview.mp4'))
data = json.loads(edl.read_text())
data.setdefault('title', sc.cfg.get('title', sc.slug) + ' Timeline')
data.setdefault('heading', sc.cfg.get('title', sc.slug))
notes = sc.dir / 'cut-notes.json'  # Claude's read of the notes so far (round, plan, replies), shown on the page
if notes.exists():
    n = json.loads(notes.read_text())
    data.update({k: n[k] for k in ('round', 'plan', 'replies') if k in n})
print(json.dumps(timeline.build(data, preview, sys.argv[2])))
