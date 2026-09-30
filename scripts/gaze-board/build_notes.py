#!/usr/bin/env python3
"""Build the Gaze SHORTLIST board — the keeps only, one comment box per image.

The sibling of build.py. That one is the wide pick pass (295 options, keep/maybe/no);
this one hoists whatever Kai marked keep or maybe and gives each surviving still a
comment field, so his note per image can be collected into the cut proposal.

    python3 scripts/gaze-board/build_notes.py PICKS_DIR [OUT]

PICKS_DIR is a folder of <key>.json files dumped from the option board's `picks`
collection (ArtifactData list --out_dir). OUT defaults to ./out-notes.
"""
import re, json, subprocess, pathlib, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
MD = REPO / 'docs/stories/gitpush-origin-master/scenes/the-gaze.md'
STILLS = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/the-gaze/stills')
HERE = pathlib.Path(__file__).resolve().parent
PICKS = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / 'out-notes'
IMG = OUT / 'img'
IMG.mkdir(parents=True, exist_ok=True)

FOLDERS = {'01': '01-grid', '02': '02-dive', '03': '03-soil-vast', '04': '04-soil-farmer',
           '05': '05-happiness-bus', '06': '06-happiness-city', '07': '07-water-reservoir',
           '08': '08-water-queue', '09': '09-birth-estate', '10': '10-birth-kitchen',
           '11': '11-dam-wall', '12': '12-b1-exodus', '13': '13-b2-towers', '14': '14-b3-downs',
           '15': '15-prices', '16': '16-doorway', '17': '17-school-run', '18': '18-high-street',
           '19': '19-playground', '20': '20-ribbon', '21': '21-summit', '22': '22-sprinklers',
           '23': '23-good-news', '24': '24-photo-op', '25': '25-build', '26': '26-mansions',
           '27': '27-power', '28': '28-inside', '29': '29-scar', '30': '30-campus'}

# The blocks of the-gaze-plan.md §2, in cut order. This is the page's spine.
BLOCKS = [
    ('A', 'The grid', 'Where the trillions went. The machine arrives in its own accommodation.', ['01']),
    ('B', 'The gaze leaves', 'Out of the gauge, out of the building, down through the cloud.', ['02']),
    ('C', 'Soil', 'The first reading. The ground itself leaving.', ['03', '04']),
    ('C', 'Happiness', 'The second reading — a feeling, read as a number.', ['05', '06']),
    ('C', 'Water', 'The third reading. Who the water went to.', ['07', '08']),
    ('C', 'Birth rate', 'The fourth reading. Nobody is coming.', ['09', '10']),
    ('C′', 'The street', 'The readings our reader actually lives on.', ['15', '16', '17', '18', '19']),
    ('D', 'The trend line', 'The graph already painted on the world.', ['11']),
    ('E', 'The ceremony', 'Humans carrying on. Aimed up, at the decision.', ['20', '21', '22', '23', '24']),
    ('E', 'The estate', "The capex as a landscape — the mansions the machine was given.", ['25', '26', '27', '28', '29', '30']),
    ('F', 'The bulletins', 'The collapse as news, ending in Swindon.', ['12', '13', '14']),
]

picks = {}
for f in PICKS.glob('*.json'):
    picks[f.stem] = json.loads(f.read_text())

text = MD.read_text()
shots = {}
for m in re.finditer(r'^## (\d\d) · (.+?)\n(.*?)(?=^## |^# |\Z)', text, re.S | re.M):
    num, title, body = m.group(1), m.group(2).strip(), m.group(3)
    job = re.search(r'\*\*Job:\*\*\s*(.+)', body)
    shots[num] = {'title': title, 'job': job.group(1).strip() if job else '',
                  'prompts': re.findall(r'^\d\. `(.+?)`\s*$', body, re.M)}

groups, kept = [], 0
for block, name, note, nums in BLOCKS:
    items = []
    for num in nums:
        s = shots.get(num)
        if not s:
            continue
        for i, prompt in enumerate(s['prompts']):
            for c in 'ab':
                key = f'{num}-f{i+1}-{c}'
                v = picks.get(key, {}).get('v')
                if v not in ('keep', 'maybe'):
                    continue
                src = STILLS / FOLDERS[num] / f'{i:02d}-{c}.jpg'
                if not src.exists():
                    continue
                dst = IMG / f'{key}.jpg'
                if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
                    subprocess.run(['convert', str(src), '-resize', '1200x',
                                    '-quality', '80', str(dst)], check=True)
                items.append({'key': key, 'src': f'img/{key}.jpg', 'v': v, 'shot': num,
                              'title': s['title'], 'job': s['job'], 'prompt': prompt})
                kept += 1
    if items:
        groups.append({'block': block, 'name': name, 'note': note, 'items': items})

data = {'groups': groups, 'total': kept}
page = (HERE / 'template_notes.html').read_text().replace('/*DATA*/null', json.dumps(data))
(OUT / 'index.html').write_text(page)
(OUT / 'files.json').write_text(json.dumps(
    {f'img/{p.name}': str((IMG / p.name)) for p in sorted(IMG.glob('*.jpg'))}, indent=1))
size = sum(p.stat().st_size for p in IMG.glob('*.jpg')) / 1e6
print(f'{kept} stills across {len(groups)} blocks -> {OUT}/index.html  ({size:.1f} MB of images)')
