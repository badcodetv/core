#!/usr/bin/env python3
"""Provenance: recipe cards, the scene trail and the frozen final recipe (docs/provenance/README.md).

    # a card for a file a tool did not stamp itself (an ffmpeg composite, a Freesound effect, a Premiere render)
    python3 scripts/provenance/prov.py card <file> --kind sfx --engine freesound --tool manual \\
        --prompt "door slam, heavy" --input url=https://freesound.org/s/123 --why "Kai 23 Oct: the door must slam"
    python3 scripts/provenance/prov.py card <file> --merge --setting sheet=docs/.../music.md   # add to an existing card

    # one line in the scene's trail per page published (and the page link kept in scene.json "boards")
    python3 scripts/provenance/prov.py trail <scene-dir> --stage timeline --round 2 --url <artifact url> \\
        --what "cut 2: door slam in, Maddie turns away" [--notes <file of the page's db notes>]

    # which files in the cut have no card
    python3 scripts/provenance/prov.py check <scene-dir>

    # Kai says the cut is done: every shot and sound traced to its recipe, written into the repo
    python3 scripts/provenance/prov.py freeze <scene-dir>

A card is written beside the file (<file>.prov.json) AND into the repo mirror
(docs/provenance/cards/<path under the media root>.prov.json). The TypeScript twin is
packages/flow-mcp/src/prov.ts; keep the two writing the same shape.
"""
import argparse
import datetime
import json
import os
import pathlib
import shutil
import sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCHEMA = 'badcode.prov/1'
KINDS = ('image', 'video', 'voice', 'music', 'sfx', 'cut', 'other')
STAGES = ('brief', 'moodboard', 'storyboard', 'clips', 'timeline', 'premiere', 'other')


def media_root():
    return pathlib.Path(os.environ.get('BADCODE_MEDIA_ROOT', '/mnt/d/badcode-videos'))


def mirror_root():
    return pathlib.Path(os.environ.get('BADCODE_PROV_MIRROR', REPO / 'docs/provenance/cards'))


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')


def mirror_path(file):
    """Where a file's card lives in the repo: its path under the media root, else under _elsewhere/."""
    p = pathlib.Path(file).resolve()
    try:
        rel = p.relative_to(media_root().resolve())
    except ValueError:
        rel = pathlib.Path('_elsewhere') / str(p).lstrip('/')
    return mirror_root() / f'{rel}.prov.json'


def write_card(file, **card):
    """Write one card beside the file and into the repo mirror. Never raises: a card must not cost a take."""
    body = {'schema': SCHEMA, 'file': str(pathlib.Path(file).resolve()), 'made': now(), 'by': 'claude', **card}
    text = json.dumps(body, indent=1, ensure_ascii=False) + '\n'
    wrote = []
    for p in (pathlib.Path(str(pathlib.Path(file).resolve()) + '.prov.json'), mirror_path(file)):
        try:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text)
            wrote.append(str(p))
        except OSError as e:
            print(f'prov: could not write {p}: {e}', file=sys.stderr)
    return wrote


def read_card(file):
    """The card for a file: the repo mirror first (git keeps it), then the one beside the file."""
    for p in (mirror_path(file), pathlib.Path(str(pathlib.Path(file).resolve()) + '.prov.json')):
        if p.exists():
            return json.loads(p.read_text())
    return None


def chain(file, depth=6):
    """The file's card, then its parent's, and so on back to the first prompt (a clip → its still → its golden)."""
    out, seen = [], set()
    while file and depth and str(file) not in seen:
        seen.add(str(file))
        c = read_card(file)
        if not c:
            out.append({'file': str(file), 'missing': True})
            break
        out.append(c)
        file, depth = c.get('parent'), depth - 1
    return out


def _scene(scene_dir):
    d = pathlib.Path(scene_dir).resolve()
    if not (d / 'scene.json').exists():
        sys.exit(f'no scene.json in {d}')
    return d, json.loads((d / 'scene.json').read_text())


def _edl(d, cfg):
    media = pathlib.Path(cfg['media'])
    cut = cfg.get('cut', {})
    edl = pathlib.Path(cut.get('edl', media / 'cut' / 'edl.json'))
    if not edl.exists():
        sys.exit(f'no edl at {edl} (scene.json "cut.edl")')
    return edl, pathlib.Path(cut.get('preview', media / 'cut' / 'preview.mp4')), json.loads(edl.read_text())


def _uses(data):
    """Every media file the cut uses: picture by its source clip, sound by its source take."""
    shots = [{'t': v['start'], 'dur': v['dur'], 'beat': v.get('beat'), 'looped': bool(v.get('looped')),
              'file': v.get('source') or v['file']} for v in data.get('video', [])]
    sounds = [{'stem': e['stem'], 't': e['t'], 'dur': e['dur'], 'what': e.get('what', ''), 'file': e['src']}
              for e in data.get('events', []) if e.get('src')]
    return shots, sounds


def cmd_card(a):
    f = pathlib.Path(a.file)
    old = read_card(f) if a.merge else None
    if a.merge and not old:
        sys.exit(f'--merge: {f} has no card yet')
    card = {k: v for k, v in (old or {}).items() if k not in ('schema', 'file', 'made', 'by')}
    for k in ('kind', 'engine', 'tool', 'model', 'parent', 'why', 'source_id'):
        v = getattr(a, k)
        if v is not None:
            card[k] = str(pathlib.Path(v).resolve()) if k == 'parent' and pathlib.Path(v).exists() else v
    prompt = pathlib.Path(a.prompt_file).read_text().strip() if a.prompt_file else a.prompt
    if prompt is not None:
        card['prompt'] = prompt
    for field, pairs in (('inputs', a.input), ('settings', a.setting)):
        if pairs:
            card[field] = {**card.get(field, {}), **dict(p.split('=', 1) for p in pairs)}
    missing = [k for k in ('kind', 'engine', 'tool') if not card.get(k)]
    if missing:
        sys.exit(f'card needs --{" --".join(missing)}')
    for p in write_card(f, **card):
        print(p)


def cmd_trail(a):
    d, cfg = _scene(a.scene)
    row = {'at': now(), 'stage': a.stage, 'round': a.round, 'url': a.url, 'what': a.what}
    if a.notes:
        snap = d / 'notes' / f"{a.stage}-r{a.round if a.round is not None else 0}.json"
        snap.parent.mkdir(exist_ok=True)
        shutil.copyfile(a.notes, snap)
        row['notes'] = str(snap.relative_to(d))
    trail_file = d / 'trail.json'
    trail = json.loads(trail_file.read_text()) if trail_file.exists() else []
    trail.append({k: v for k, v in row.items() if v is not None})
    trail_file.write_text(json.dumps(trail, indent=1, ensure_ascii=False) + '\n')
    # The page link is also kept where the scene's tools look for it, so it can never be lost again.
    if a.url and a.stage in ('moodboard', 'storyboard', 'timeline') and cfg.get('boards', {}).get(a.stage) != a.url:
        cfg.setdefault('boards', {})[a.stage] = a.url
        (d / 'scene.json').write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps(trail[-1], ensure_ascii=False))


def cmd_check(a):
    d, cfg = _scene(a.scene)
    _, _, data = _edl(d, cfg)
    shots, sounds = _uses(data)
    files = sorted({u['file'] for u in shots + sounds})
    bare = [f for f in files if not read_card(f)]
    print(json.dumps({'files': len(files), 'with_card': len(files) - len(bare), 'no_card': bare}, indent=1))


def cmd_freeze(a):
    d, cfg = _scene(a.scene)
    edl, preview, data = _edl(d, cfg)
    shots, sounds = _uses(data)
    for u in shots + sounds:
        u['chain'] = chain(u['file'])
    bare = sorted({u['file'] for u in shots + sounds if u['chain'][0].get('missing')})
    words = {n: json.loads((d / n).read_text()) for n in ('script.json', 'voices.json') if (d / n).exists()}
    final = {'schema': 'badcode.final/1', 'story': cfg.get('story'), 'scene': cfg.get('scene', d.name),
             'sequence': data.get('sequence'), 'frozen': now(), 'note': a.note,
             'edl': str(edl), 'preview': str(preview), 'total': data.get('total'),
             'boards': cfg.get('boards', {}), 'words': words,
             'shots': shots, 'sounds': sounds, 'no_card': bare}
    out = d / 'final.json'
    if out.exists():  # an earlier freeze is history, not something to overwrite
        old = json.loads(out.read_text())
        out.rename(d / f"final-{old.get('frozen', 'old')[:10]}-{old.get('sequence') or 'cut'}.json")
    out.write_text(json.dumps(final, indent=1, ensure_ascii=False) + '\n')
    # The edl itself lives on the drive with the media: keep a copy beside the recipe.
    shutil.copyfile(edl, d / 'final-edl.json')
    print(json.dumps({'final': str(out), 'shots': len(shots), 'sounds': len(sounds), 'no_card': bare}, indent=1))


def main():
    ap = argparse.ArgumentParser(description='recipe cards, the scene trail, the frozen final recipe')
    sub = ap.add_subparsers(dest='cmd', required=True)
    c = sub.add_parser('card', help='write (or --merge into) the card for one file')
    c.add_argument('file')
    c.add_argument('--kind', choices=KINDS)
    c.add_argument('--engine')
    c.add_argument('--tool')
    c.add_argument('--model')
    c.add_argument('--prompt')
    c.add_argument('--prompt-file')
    c.add_argument('--parent', help='the file this one was made from')
    c.add_argument('--source-id', dest='source_id', help="the engine's own id (Flow mediaId, Suno song id)")
    c.add_argument('--why')
    c.add_argument('--input', action='append', metavar='KEY=VALUE')
    c.add_argument('--setting', action='append', metavar='KEY=VALUE')
    c.add_argument('--merge', action='store_true', help='add to the existing card instead of replacing it')
    t = sub.add_parser('trail', help="add a line to the scene's trail.json")
    t.add_argument('scene')
    t.add_argument('--stage', choices=STAGES, required=True)
    t.add_argument('--round', type=int)
    t.add_argument('--url')
    t.add_argument('--what', required=True, help='what this round is, in a sentence')
    t.add_argument('--notes', help="a JSON file of the page's db notes, snapshotted into <scene>/notes/")
    for name, h in (('check', 'list the files in the cut that have no card'),
                    ('freeze', 'write <scene>/final.json: every shot and sound traced to its recipe')):
        s = sub.add_parser(name, help=h)
        s.add_argument('scene')
        if name == 'freeze':
            s.add_argument('--note', help="why it was frozen, in Kai's words")
    a = ap.parse_args()
    {'card': cmd_card, 'trail': cmd_trail, 'check': cmd_check, 'freeze': cmd_freeze}[a.cmd](a)


if __name__ == '__main__':
    main()
