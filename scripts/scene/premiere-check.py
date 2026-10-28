#!/usr/bin/env python3
"""Is each timeline page's Premiere sequence still what the page says? One line per scene.

    python3 scripts/scene/premiere-check.py docs/stories/<story> [--write]

For every scene in the story's timelines.json whose scene.json names a current Premiere build
(premiere.current -> premiere.<round>.sequence + .edl), compare the bridge's last state dump of that
sequence (<project dir>/.bridge/state-<sequence>.json, written by premiere_get_sequence) with the edl
the page was built from:
  in sync        V1 shots, their start/in/dur and the total match the edl, and nobody added effects
                 (effects are only seen in a dump read with params on)
  page ahead     the edl changed after the sequence was built (notes answered, not yet in Premiere)
  edited in Pr   the sequence differs from the edl: Kai worked on it by hand, so never rebuild over it
  no state       no dump yet: call premiere_get_sequence({name, params:false}) first
The state dump is only as fresh as the last get_sequence call, so read every sequence just before
running this. --write stores the result on the round record (premiere.<round>.check), which the
overview board shows.
"""
import json
import os
import pathlib
import sys
from datetime import datetime


def check(rec):
    edl_p = pathlib.Path(rec['edl'])
    st_p = pathlib.Path(rec['project']).parent / '.bridge' / f'state-{rec["sequence"]}.json'
    if not st_p.exists():
        return 'no state', ''
    st, edl = json.loads(st_p.read_text()), json.loads(edl_p.read_text())
    v1 = st['videoTracks'][0]['items']
    diffs = []
    if len(v1) != len(edl['video']):
        diffs.append(f'{len(v1)} shots on V1, edl has {len(edl["video"])}')
    for i, (c, x) in enumerate(zip(v1, edl['video'])):
        if c['name'].replace('-noaudio', '') != os.path.basename(x['file']):
            diffs.append(f'shot {i + 1} is {c["name"]}, edl has {os.path.basename(x["file"])}')
        elif max(abs(c['start'] - x['start']), abs(c['duration'] - x['dur']), abs(c['inPoint'] - x['in'])) > 0.05:
            diffs.append(f'shot {i + 1} retimed')
    if abs(st['sequence']['end'] - edl['total']) > 0.05:
        diffs.append(f'length {st["sequence"]["end"]:.2f}s, edl {edl["total"]:.2f}s')
    fx = sum(len(c.get('components', [])) for t in st['videoTracks'] + st['audioTracks'] for c in t['items'])
    if fx:
        diffs.append(f'{fx} effects added')
    if diffs:
        return 'edited in Pr', '; '.join(diffs[:4])
    built = rec.get('built_at') or rec.get('built', '')
    edl_t = datetime.fromtimestamp(edl_p.stat().st_mtime).isoformat(timespec='minutes')
    if built and edl_t[:len(built)] > built:
        return 'page ahead', f'edl changed {edl_t}'
    return 'in sync', ''


def scenes(story):
    t = json.loads((story / 'timelines.json').read_text())
    for s in t['sections']:
        for p in [s] + s.get('parts', []):
            if p.get('scene') and (story / p['scene'] / 'scene.json').exists():
                yield p, story / p['scene'] / 'scene.json'


def main(argv):
    story = pathlib.Path(argv[0]).resolve()
    write = '--write' in argv
    for part, path in scenes(story):
        raw = path.read_text()
        cfg = json.loads(raw)
        pr = cfg.get('premiere') or {}
        cur = pr.get('current')
        if not cur:
            continue
        rec = dict(pr[cur])
        rec.setdefault('project', next((r['project'] for r in pr.values() if isinstance(r, dict) and r.get('project')), ''))
        state, why = check(rec)
        print(f'{part["id"]:<12} {rec["sequence"]:<20} {state:<13} {why}')
        if write:
            pr[cur]['check'] = {'at': datetime.now().isoformat(timespec='minutes'), 'state': state, 'why': why}
            indent = len(raw.split('\n')[1]) - len(raw.split('\n')[1].lstrip())
            path.write_text(json.dumps(cfg, indent=indent or 2, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    main(sys.argv[1:])
