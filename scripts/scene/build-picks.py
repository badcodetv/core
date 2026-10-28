#!/usr/bin/env python3
"""A picks page: options laid out per decision (stills, clips, voice takes, Suno links), Pick one per row, a note per row.

    python3 scripts/scene/build-picks.py <picks.json> <out.html>

picks.json:
  {"title": "Kill Bots Picks", "eyebrow": "GPOM second half · picks", "heading": "...", "intro": "...",
   "sections": [{"h": "...", "lede": "...", "groups": [
      {"slot": "e5-parl", "title": "...", "line": "...", "kind": "image|video|audio|link",
       "opts": [{"id": "a", "src": "e5/a.jpg", "label": "a: closer", "warn": ""}]}]}]}   # link options use "href"
`src` paths are the page's published files: publish out.html with every media file at its `src` path and
`capabilities: {db:{}, user:{}}`. Every image opens large on click (arrows step through the row; Pick works there).
Picks land in db collection `picks`, doc `<slot>__<user>` {slot, pick, note, by, at}: dump it into the repo before
reading (docs/provenance, "Artifacts are the UI").
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent

spec = json.loads(pathlib.Path(sys.argv[1]).read_text())
html = (HERE / 'picks-template.html').read_text()
html = html.replace('<title>Picks</title>', f"<title>{spec.get('title', 'Picks')}</title>", 1)
html = html.replace('/*DATA*/null', json.dumps(spec, ensure_ascii=False))
pathlib.Path(sys.argv[2]).write_text(html)
files = sorted({o['src'] for s in spec['sections'] for g in s['groups'] for o in g['opts'] if o.get('src')})
print(json.dumps({'page': sys.argv[2], 'groups': sum(len(s['groups']) for s in spec['sections']), 'files': files}))
