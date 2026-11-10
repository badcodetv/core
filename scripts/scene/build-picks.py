#!/usr/bin/env python3
"""A picks page: options laid out per decision (stills, clips, voice takes, Suno links), Pick one per row, a note per row.

    python3 scripts/scene/build-picks.py <picks.json> <out.html>

picks.json:
  {"title": "Kill Bots Picks", "eyebrow": "GPOM second half · picks", "heading": "...", "intro": "...",
   "sections": [{"h": "...", "lede": "...", "groups": [
      {"slot": "e5-parl", "title": "...", "line": "...", "kind": "image|video|audio|link",
       "opts": [{"id": "a", "src": "e5/a.jpg", "label": "a: closer", "warn": ""}]}]}]}   # link options use "href"
Rounds (optional): top-level "round": N and a group "round" (default 1). With N > 1 the page lists this round's
groups first, tagged New, and folds earlier rounds into one closed panel that shows the viewer's pick per group.
`src` paths are the page's published files: publish out.html with every media file at its `src` path and
`capabilities: {db:{}, user:{}}`. Every image opens large on click (arrows step through the row; Pick works there).
Picks land in db collection `picks`, doc `<slot>__<user>` {slot, pick, note, by, at}: dump it into the repo before
reading (docs/provenance, "Artifacts are the UI").
"""
import json
import pathlib
import sys
import os as _os, sys as _sys  # cut files written on another machine open on this one (scripts/drive/localmap.py)
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'drive'))
from localmap import localize  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent

spec = localize(json.loads(pathlib.Path(sys.argv[1]).read_text()))
html = (HERE / 'picks-template.html').read_text()
html = html.replace('<title>Picks</title>', f"<title>{spec.get('title', 'Picks')}</title>", 1)
html = html.replace('/*DATA*/null', json.dumps(spec, ensure_ascii=False))
pathlib.Path(sys.argv[2]).write_text(html)
files = sorted({o['src'] for s in spec['sections'] for g in s['groups'] for o in g['opts'] if o.get('src')})
print(json.dumps({'page': sys.argv[2], 'groups': sum(len(s['groups']) for s in spec['sections']), 'files': files}))
