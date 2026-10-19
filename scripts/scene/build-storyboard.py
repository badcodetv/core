#!/usr/bin/env python3
"""Build a scene's storyboard page: frames in story order, each with its still(s) and the ways to
animate it. Picks (still + animation option per frame) and notes are shared through the artifact db
(collections `picks`, `notes`). Publish with capabilities {db:{}, user:{}}.

    python3 scripts/scene/build-storyboard.py <scene-dir> <out.html>

Reads scene.json (title, heading, storyboard_intro, looks), storyboard.json and
animation-options.json. A frame's `anim` names the options entry it uses (default: its own n).
"""
import html
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from scene import Scene, data_uri  # noqa: E402

HERE = pathlib.Path(__file__).parent


def main(scene_dir, out):
    sc = Scene(scene_dir)
    sb = sc.load('storyboard.json')
    anim = sc.load('animation-options.json', {})
    by_n = {str(f['n']): f for f in anim.get('frames', [])}
    images = {}
    for f in sb['frames']:
        f['anim'] = by_n.get(str(f.get('anim', f['n'])), {})
        for sid in f['stills']:
            p = sc.still(sid)
            if p:
                images[sid] = data_uri(p, 1100)
            else:
                print('missing still:', sid, file=sys.stderr)
    payload = {'acts': sb['acts'], 'frames': sb['frames'], 'notes': anim.get('sequence_notes', []),
               'img': images, 'looks': sc.cfg.get('looks', {})}
    page = (HERE / 'storyboard-template.html').read_text()
    page = (page.replace('/*DATA*/null', json.dumps(payload, ensure_ascii=False).replace('</', '<\\/'))
            .replace('<!--TITLE-->', html.escape(sc.cfg['title'] + ' storyboard'))
            .replace('<!--HEADING-->', sc.cfg.get('heading', html.escape(sc.cfg['title'])))
            .replace('<!--INTRO-->', sc.cfg.get('storyboard_intro', '')))
    pathlib.Path(out).write_text(page)
    print(f'{out}: {len(sb["frames"])} frames, {len(images)} stills, {len(page) / 1e6:.1f} MB')


if __name__ == '__main__':
    main(*sys.argv[1:3])
