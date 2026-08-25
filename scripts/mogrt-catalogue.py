#!/usr/bin/env python3
"""
List the Motion Graphics Templates installed on this machine, and every box each one exposes.

    scripts/mogrt-catalogue.py                    # one line per template
    scripts/mogrt-catalogue.py --controls         # every exposed control, grouped
    scripts/mogrt-catalogue.py --find lower       # match on name or category
    scripts/mogrt-catalogue.py --markdown         # the docs table
    scripts/mogrt-catalogue.py --json             # everything, machine-readable

A `.mogrt` is a zip, and its `definition.json` carries `clientControls` — the exact list of
fields Premiere will show in the Essential Graphics panel. **So the whole parameter surface is
readable without Premiere running**, which is the point: you can tell someone precisely which
boxes they will need to fill in before you place a single template.

🔴 Whether those controls can be SET through the UXP API is a separate, open question (T11).
Reading them here does not imply writing them there.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
import zipfile

# The Windows install path, reached through WSL. Override with --root.
DEFAULT_ROOT = pathlib.Path(
    '/mnt/c/Program Files/Adobe/Adobe Premiere Pro 2026/Essential Graphics'
)

# Control types, inferred from the shape of every control across all 77 shipped templates:
# type 1 always carries a boolean `value`; type 2 always carries min/max/value; types 6 and 8
# never carry a value, and 8 is used for the unnamed and section-named separators.
CONTROL_TYPES = {
    1: 'checkbox',
    2: 'slider',
    4: 'colour',
    6: 'text',
    8: 'group',
}


def english(ui: object) -> str:
    """Pull en_US out of Adobe's localised string bundle."""
    if not isinstance(ui, dict):
        return str(ui or '')
    for entry in ui.get('strDB', []):
        if entry.get('localeString') == 'en_US':
            return entry.get('str', '')
    db = ui.get('strDB') or [{}]
    return db[0].get('str', '')


def read_template(path: pathlib.Path) -> dict:
    try:
        with zipfile.ZipFile(path) as z:
            definition = json.loads(z.read('definition.json'))
    except (zipfile.BadZipFile, KeyError, json.JSONDecodeError, OSError) as err:
        return {'path': str(path), 'name': path.stem, 'error': str(err), 'controls': []}

    controls = []
    for control in definition.get('clientControls', []):
        kind = control.get('type')
        entry = {
            'name': english(control.get('uiName', {})),
            'type': CONTROL_TYPES.get(kind, f'type{kind}'),
            'id': control.get('id'),
        }
        if 'value' in control:
            value = control['value']
            # Text defaults arrive as Adobe's localised string bundle, not a string.
            entry['default'] = english(value) if isinstance(value, dict) and 'strDB' in value else value
        if 'min' in control:
            entry['min'], entry['max'] = control['min'], control.get('max')
        controls.append(entry)

    return {
        'path': str(path),
        'name': english(definition.get('capsuleNameLocalized', {})) or definition.get('capsuleName', path.stem),
        'category': path.parent.name,
        'controls': controls,
    }


def load_all(root: pathlib.Path) -> list[dict]:
    if not root.exists():
        print(f'no templates found at {root}', file=sys.stderr)
        return []
    return [read_template(p) for p in sorted(root.rglob('*.mogrt'))]


def summarise(controls: list[dict]) -> str:
    counts: dict[str, int] = {}
    for c in controls:
        if c['type'] == 'group':
            continue
        counts[c['type']] = counts.get(c['type'], 0) + 1
    if not counts:
        return 'no editable controls'
    return ', '.join(f'{n} {k}' for k, n in sorted(counts.items()))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--root', type=pathlib.Path, default=DEFAULT_ROOT)
    ap.add_argument('--find', help='substring match on template name or category')
    ap.add_argument('--controls', action='store_true', help='list every control')
    ap.add_argument('--markdown', action='store_true')
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()

    templates = load_all(args.root)
    if args.find:
        needle = args.find.lower()
        templates = [t for t in templates
                     if needle in t['name'].lower() or needle in t.get('category', '').lower()]
    if not templates:
        return 1

    if args.json:
        print(json.dumps(templates, indent=2))
        return 0

    if args.markdown:
        by_category: dict[str, list[dict]] = {}
        for t in templates:
            by_category.setdefault(t.get('category', '(top level)'), []).append(t)
        for category, items in sorted(by_category.items()):
            print(f'### {category} — {len(items)}\n')
            print('| Template | Text | Colour | Other | Named controls |')
            print('| --- | --- | --- | --- | --- |')
            for t in sorted(items, key=lambda x: x['name']):
                kinds = [c for c in t['controls'] if c['type'] != 'group']
                text = [c for c in kinds if c['type'] == 'text']
                colour = [c for c in kinds if c['type'] == 'colour']
                other = [c for c in kinds if c['type'] in ('checkbox', 'slider')]
                # Adobe's own templates call every text box "TextLayer", so only distinct,
                # meaningful names are worth printing.
                named = sorted({c['name'] for c in kinds
                                if c['name'] and c['name'] not in ('TextLayer', 'LayerName')})
                detail = ', '.join(f'`{n}`' for n in named[:5]) or '—'
                if len(named) > 5:
                    detail += f' …+{len(named) - 5}'
                print(f"| **{t['name']}** | {len(text)} | {len(colour)} | {len(other)} | {detail} |")
            print()
        return 0

    for t in templates:
        print(f"{t.get('category','')}/{t['name']}  —  {summarise(t['controls'])}")
        if args.controls:
            for c in t['controls']:
                if c['type'] == 'group':
                    print(f"    ── {c['name'] or '(unnamed section)'}")
                    continue
                bits = [f"{c['type']:8s} {c['name']!r}"]
                if 'default' in c:
                    bits.append(f"default={c['default']}")
                if 'min' in c:
                    bits.append(f"range={c['min']}–{c['max']}")
                print('    ' + '  '.join(bits))
            print()

    if not args.controls:
        total = sum(len([c for c in t['controls'] if c['type'] != 'group']) for t in templates)
        print(f"\n{len(templates)} templates, {total} editable controls")
    return 0


if __name__ == '__main__':
    sys.exit(main())
