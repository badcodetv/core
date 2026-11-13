#!/usr/bin/env python3
"""Real photos as the starting look of a scene: search Unsplash, save the hits as references, build a picks page.

Kai and Jack, 2026-11-13 meeting (docs/misc/2026-11-13-meeting.md): Jack's trick of finding a real photo on
Unsplash and using it as the Flow reference (the taxi for Infinite Yous, the ambulance for Priority Lane) becomes
step one of a scene's look. "Give me some sentences, I'll search Unsplash and stick some examples on the artifact
for you to pick from."

    python3 scripts/scene/unsplash-refs.py <scene-dir> "<query>" ["<query>" ...] [--n 6] [--beat <key>]

- Needs UNSPLASH_ACCESS_KEY in the repo's .env: a free key from https://unsplash.com/developers (New Application;
  the demo tier allows 50 requests an hour, plenty for this). Without it the script stops and says so.
- Saves each hit to <media>/reference/unsplash/<photo-id>.jpg (portrait first when the scene is 9:16), tells
  Unsplash about the download (their API guideline), and records the photographer and page in
  <scene-dir>/refs.json for the credit. The Unsplash licence allows use as a reference without payment.
- Writes <scene-dir>/refs-picks.json for scripts/scene/build-picks.py, one row per query. Build and publish:
      python3 scripts/scene/build-picks.py <scene-dir>/refs-picks.json <out.html>
  publishing out.html with files {"unsplash/<id>.jpg": "<media>/reference/unsplash/<id>.jpg", ...} and
  capabilities {db:{}, user:{}}. The picked photo is named in look.md (Anchors) and handed to the clean-room
  writers, who say whether to attach it in Flow or describe it.
"""
import argparse
import json
import os
import pathlib
import sys
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts' / 'drive'))
from localmap import localize  # noqa: E402


def env_key():
    if os.environ.get('UNSPLASH_ACCESS_KEY'):
        return os.environ['UNSPLASH_ACCESS_KEY']
    env = ROOT / '.env'
    if env.exists():
        for line in env.read_text().splitlines():
            if line.strip().startswith('UNSPLASH_ACCESS_KEY='):
                return line.split('=', 1)[1].strip().strip('"\'')
    return None


def api(url, key):
    req = urllib.request.Request(url, headers={'Authorization': f'Client-ID {key}', 'Accept-Version': 'v1'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('scene_dir')
    ap.add_argument('queries', nargs='+')
    ap.add_argument('--n', type=int, default=6)
    ap.add_argument('--beat', default='')
    a = ap.parse_args()

    key = env_key()
    if not key:
        sys.exit('No UNSPLASH_ACCESS_KEY in .env. Get a free key at https://unsplash.com/developers '
                 '(New Application, copy the Access Key), add UNSPLASH_ACCESS_KEY=... to .env, and rerun. '
                 'Until then: search unsplash.com by hand and drop the photo in <media>/reference/.')

    scene_dir = pathlib.Path(a.scene_dir)
    scene = localize(json.loads((scene_dir / 'scene.json').read_text()))
    media = pathlib.Path(scene['media'])
    out = media / 'reference' / 'unsplash'
    out.mkdir(parents=True, exist_ok=True)
    portrait = (scene.get('video') or {}).get('aspect', '9:16') == '9:16'

    refs_path = scene_dir / 'refs.json'
    refs = json.loads(refs_path.read_text()) if refs_path.exists() else []
    seen = {r['id'] for r in refs}
    groups = []
    for q in a.queries:
        params = {'query': q, 'per_page': a.n, 'content_filter': 'high'}
        if portrait:
            params['orientation'] = 'portrait'
        res = api('https://api.unsplash.com/search/photos?' + urllib.parse.urlencode(params), key)
        opts = []
        for p in res.get('results', []):
            pid = p['id']
            dest = out / f'{pid}.jpg'
            if not dest.exists():
                urllib.request.urlretrieve(p['urls']['regular'], dest)
                try:  # Unsplash's API guideline: report each download
                    api(p['links']['download_location'], key)
                except Exception:
                    pass
            who = p['user']['name']
            if pid not in seen:
                refs.append({'id': pid, 'query': q, 'beat': a.beat, 'file': str(dest),
                             'photographer': who, 'profile': p['user']['links']['html'],
                             'page': p['links']['html'], 'alt': p.get('alt_description') or ''})
                seen.add(pid)
            opts.append({'id': pid, 'src': f'unsplash/{pid}.jpg', 'label': f'{(p.get("alt_description") or q)[:60]} · {who}'})
        groups.append({'slot': f'ref-{len(groups) + 1}', 'title': q, 'line': 'Pick the photo whose look this scene should start from.',
                       'kind': 'image', 'opts': opts})
        print(f'{q!r}: {len(opts)} photos', file=sys.stderr)

    refs_path.write_text(json.dumps(refs, indent=1, ensure_ascii=False))
    title = scene.get('title', scene_dir.name)
    picks = {'title': f'{title} Look Refs', 'eyebrow': f'{title} · look references',
             'heading': f'{title}: pick a real photo to start the look from',
             'intro': 'Real photos from Unsplash, one row per search. Pick one per row (or none) and leave a note on what you like in it.',
             'sections': [{'h': 'Searches', 'lede': 'Photos by their Unsplash photographers, named under each one.', 'groups': groups}]}
    (scene_dir / 'refs-picks.json').write_text(json.dumps(picks, indent=1, ensure_ascii=False))
    files = {o['src']: str(out / f"{o['id']}.jpg") for g in groups for o in g['opts']}
    print(json.dumps({'picks': str(scene_dir / 'refs-picks.json'), 'files': files}, indent=1))


if __name__ == '__main__':
    main()
