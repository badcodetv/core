#!/usr/bin/env python3
"""Extract the downfall pack's still + motion prompts from the three sheets.

The sheets are the source of truth; nothing is retyped. Every still heading looks like
`### T1-A · ...` and every motion heading like `### T1 · image-to-video`.

    python3 scripts/downfall/prompts.py stills   # JSON: [{key, shot, variant, prompt}]
    python3 scripts/downfall/prompts.py motion   # JSON: {shot: prompt}
"""
import re, json, pathlib, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENES = REPO / 'docs/stories/gitpush-origin-master/scenes'
SHEETS = ['downfall-flow-businesses.md', 'downfall-flow-banks.md', 'downfall-flow-swindon.md']

# Play order across the whole 54s edit.
ORDER = ['T1', 'T2', 'T3', 'N1', 'N2', 'N3', 'SG', 'NY', 'LN', 'W1', 'W2', 'W3']

def blocks():
    stills, motion = [], {}
    for name in SHEETS:
        text = (SCENES / name).read_text()
        for m in re.finditer(r'^### ([A-Z0-9]+)(?:-([A-D]))? · (.+?)\n(.*?)(?=^### |^## |\Z)', text, re.S | re.M):
            shot, variant, title, body = m.group(1), m.group(2), m.group(3).strip(), m.group(4)
            p = re.search(r'```prompt\n(.+?)\n```', body, re.S)
            if not p:
                continue
            if variant:
                stills.append({'key': f'{shot}-{variant}', 'shot': shot, 'variant': variant,
                               'title': title, 'prompt': p.group(1).strip()})
            elif 'image-to-video' in title:
                motion[shot] = p.group(1).strip()
    stills.sort(key=lambda s: (ORDER.index(s['shot']), s['variant']))
    return stills, motion

if __name__ == '__main__':
    stills, motion = blocks()
    what = sys.argv[1] if len(sys.argv) > 1 else 'stills'
    print(json.dumps(stills if what == 'stills' else motion, indent=2))
