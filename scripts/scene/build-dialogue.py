#!/usr/bin/env python3
"""Build a dialogue options page from its options.json: one tab per dialogue, what's in the cut now, the
drafts to pick from, and every writer's version ranked underneath. See the scene-dialogue skill.

    python3 scripts/scene/build-dialogue.py <options.json> <out.html> [--notes <notes.json>]

options.json holds page_title, title, about, shapes [{id, name, title, file}], dialogues [{id, label, where,
scene, target, now_from, now [{who, line}], drafts [{id, name, length, total, bet, lines [{who, line, tags, s}],
notes}], ranking [{rank, shape, length, verdict}], keeps?, protected? {columns, rows}}], questions [{id, text}].
Each writer's approach and version of dialogue N are read from their file ("## Dialogue N" sections), as
scripts/scene/dialogue-workflow.js writes them; options.json may carry them instead (intro, shapes{id: md}).
--notes is the round file (round, plan, replies keyed by note key), so Claude's read shows under each note.
Notes on the page land in the artifact db collection "notes" ({key, note, by, at}); keys are
top, <dialogue>, <dialogue>-<draft>, <dialogue>-<draft>-L<n>, <dialogue>-s<shape>, pick-<dialogue> (the
draft id picked) and q<n>.
"""
import importlib.util
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('rp', HERE.parent / 'design' / 'build-reading-page.py')
rp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rp)


def md(text):
    # the section's own "## Dialogue N" heading is redundant inside its tab
    return rp.render(re.sub(r'^## .*\n', '', text.strip(), count=1))


def split_shape(path):
    """A writer's file: '# Shape NN: …', an approach paragraph, then one '## Dialogue N…' section per dialogue."""
    t = path.read_text()
    h1 = re.match(r'# (.*)\n', t)
    parts = re.split(r'^(## dialogue ?(?:[-:] )?\s*(\d+).*)$', t, flags=re.M | re.I)
    secs = {int(parts[j + 1]): (parts[j] + '\n' + parts[j + 2]).strip().strip('-').strip() for j in range(1, len(parts), 3)}
    return parts[0][h1.end() if h1 else 0:].strip(), secs


def main(argv):
    src, out = pathlib.Path(argv[0]), pathlib.Path(argv[1])
    d = json.loads(src.read_text())
    root = pathlib.Path(__file__).resolve().parents[2]
    files = {}
    for s in d['shapes']:
        if s.get('file') and (root / s['file']).exists():
            intro, files[s['id']] = split_shape(root / s['file'])
            s.setdefault('intro', intro)
        s['intro_html'] = rp.render(s.get('intro', ''))
    for n, x in enumerate(d['dialogues'], 1):
        # the writers' versions come from their files unless options.json carries them
        x.setdefault('shapes', {k: v[n] for k, v in files.items() if n in v})
        missing = [r['shape'] for r in x['ranking'] if r['shape'] not in x['shapes']]
        if missing:
            sys.exit(f'{x["id"]}: no text for shape(s) {missing}; check each file has a "## Dialogue {n}" heading')
        x['shapes_html'] = {k: md(v) for k, v in x['shapes'].items()}
    if '--notes' in argv:
        n = json.loads(pathlib.Path(argv[argv.index('--notes') + 1]).read_text())
        d.update({k: n[k] for k in ('round', 'plan', 'replies') if k in n})
    page = (HERE / 'dialogue-template.html').read_text()
    page = page.replace('__TITLE__', d.get('page_title', 'Dialogue Options'))
    page = page.replace('/*DATA*/', json.dumps(d, ensure_ascii=False).replace('</', '<\\/'))
    out.write_text(page)
    print(out, len(page), 'bytes')


if __name__ == '__main__':
    main(sys.argv[1:])
