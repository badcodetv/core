#!/usr/bin/env python3
"""Build the Gaze option-still board.

Reads the prompts from docs/stories/gitpush-origin-master/scenes/the-gaze.md, thumbnails the
stills out of the scene's scratch folder, and writes index.html + files.json into OUT (a
scratchpad folder — the media never enters the repo).

    python3 scripts/gaze-board/build.py [OUT]

Lives in the repo because the scratchpad is wiped between sessions and this was lost once.
"""
import re, json, subprocess, pathlib, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
MD = REPO / 'docs/stories/gitpush-origin-master/scenes/the-gaze.md'
STILLS = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/the-gaze/stills')
HERE = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / 'out'
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
GROUP = {'01': 'The grid', '02': 'The gaze leaves', '03': 'Soil', '04': 'Soil',
         '05': 'Happiness', '06': 'Happiness', '07': 'Water', '08': 'Water',
         '09': 'Birth rate', '10': 'Birth rate', '11': 'The trend line', '12': 'Bulletin 1',
         '13': 'Bulletin 2', '14': 'Bulletin 3', '15': 'The street', '16': 'The street',
         '17': 'The street', '18': 'The street', '19': 'The street', '20': 'The ceremony',
         '21': 'The ceremony', '22': 'The ceremony', '23': 'The ceremony', '24': 'The ceremony',
         '25': 'The estate', '26': 'The estate', '27': 'The estate', '28': 'The estate',
         '29': 'The estate', '30': 'The estate'}

text = MD.read_text()
shots = []
for m in re.finditer(r'^## (\d\d) · (.+?)\n(.*?)(?=^## |^# |\Z)', text, re.S | re.M):
    num, title, body = m.group(1), m.group(2).strip(), m.group(3)
    job = re.search(r'\*\*Job:\*\*\s*(.+)', body)
    prompts = re.findall(r'^\d\. `(.+?)`\s*$', body, re.M)
    framings = []
    for i, p in enumerate(prompts):
        cands = []
        for c in 'ab':
            src = STILLS / FOLDERS[num] / f'{i:02d}-{c}.jpg'
            key = f'{num}-f{i+1}-{c}'
            if src.exists():
                dst = IMG / f'{key}.jpg'
                if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
                    subprocess.run(['convert', str(src), '-resize', '1100x', '-quality', '80', str(dst)], check=True)
                cands.append({'key': key, 'src': f'img/{key}.jpg'})
            else:
                cands.append({'key': key, 'src': None})
        framings.append({'n': i + 1, 'prompt': p, 'cands': cands})
    shots.append({'num': num, 'title': title, 'group': GROUP[num],
                  'job': job.group(1).strip() if job else '', 'framings': framings})

done = sum(1 for s in shots for f in s['framings'] for c in f['cands'] if c['src'])
total = sum(len(f['cands']) for s in shots for f in s['framings'])
page = (HERE / 'template.html').read_text().replace('/*DATA*/null', json.dumps({'shots': shots, 'done': done, 'total': total}))
(OUT / 'index.html').write_text(page)
(OUT / 'files.json').write_text(json.dumps({f'img/{p.name}': f'img/{p.name}' for p in sorted(IMG.glob('*.jpg'))}))
print(f'{done}/{total} stills on the board -> {OUT}/index.html')
