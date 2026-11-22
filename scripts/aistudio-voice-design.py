#!/usr/bin/env python3
"""Make AI Studio designed voices (voice design) from one-sentence descriptions.

    python3 scripts/aistudio-voice-design.py <designs.json> <designed-voices.json> --prefix firesale [--gender male]

designs.json: [{"name": "jim-r2-a", "desc": "..."}] (or {"designs": [...]}). Each design becomes a reusable `voice_…`
id (POST v1beta/voices, type prompted, en-GB, model gemini-3.8-flash-tts) merged into designed-voices.json as
{name: {id, desc, role?}}. Names already there are skipped. Method: docs/rules/voices.md.
"""
import argparse, json, os, pathlib, sys, time, urllib.error, urllib.request

REPO = pathlib.Path(__file__).resolve().parents[1]


def key():
    if os.environ.get('GEMINI_API_KEY'):
        return os.environ['GEMINI_API_KEY']
    for ln in (REPO / '.env').read_text().splitlines():
        ln = ln.removeprefix('export ').strip()
        if ln.startswith('GEMINI_API_KEY='):
            return ln.split('=', 1)[1].strip().strip('"\'')
    sys.exit('no GEMINI_API_KEY')


def design(k, name, desc, gender):
    body = {'display_name': name, 'type': 'prompted', 'language_code': 'en-GB', 'gender': gender,
            'model': 'models/gemini-3.8-flash-tts', 'store': True, 'prompted': {'input': desc}}
    for wait in (0, 20, 40, 60):
        time.sleep(wait)
        req = urllib.request.Request(f'https://generativelanguage.googleapis.com/v1beta/voices?key={k}',
                                     data=json.dumps(body).encode(), headers={'Content-Type': 'application/json'})
        try:
            return json.load(urllib.request.urlopen(req))
        except urllib.error.HTTPError as e:
            msg = e.read().decode()[:400]
            if e.code != 429:
                raise SystemExit(f'{name}: HTTP {e.code} {msg}')
    raise SystemExit(f'{name}: still 429')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('designs'); ap.add_argument('out')
    ap.add_argument('--prefix', required=True, help='display-name prefix, e.g. the story (firesale)')
    ap.add_argument('--gender', default='male'); ap.add_argument('--role', default='')
    a = ap.parse_args()
    d = json.loads(pathlib.Path(a.designs).read_text())
    d = d['designs'] if isinstance(d, dict) else d
    out = pathlib.Path(a.out); have = json.loads(out.read_text()) if out.exists() else {}
    k = key()
    for x in d:
        if x['name'] in have:
            print(f"skip {x['name']} (exists)"); continue
        r = design(k, f"{a.prefix}-{x['name']}", x['desc'], x.get('gender', a.gender))
        have[x['name']] = {'id': r['id'], 'role': x.get('role', a.role), 'desc': x['desc']}
        out.write_text(json.dumps(have, indent=1, ensure_ascii=False) + '\n')
        print(x['name'], r['id'])


if __name__ == '__main__':
    main()
