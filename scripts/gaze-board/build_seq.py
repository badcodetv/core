#!/usr/bin/env python3
"""Build the Gaze RUNNING ORDER board — the scene as a numbered filmstrip.

Third in the set. build.py = the wide pick pass (295 options). build_notes.py = the
shortlist with a comment box each. This one takes Kai's spoken order (scenes/the-gaze-sequence.md)
and lays the starred stills out in the order they would be cut, so the scene can be read
before a single Veo credit is spent.

    python3 scripts/gaze-board/build_seq.py [OUT]
"""
import re, json, subprocess, pathlib, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
MD = REPO / 'docs/stories/gitpush-origin-master/scenes/the-gaze.md'
STILLS = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/the-gaze/stills')
HERE = pathlib.Path(__file__).resolve().parent
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / 'out-seq'
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
TALL = STILLS / '01-grid-tall'

# Kai's order. Spoken 2026-09-19, then RE-ORDERED by him on the running-order board
# (beatnotes 1, 2, 3, 4, 6) the same evening. This is revision B — his numbers, decoded.
BEATS = [
    dict(n='1', name='The executives', line='The market roars, the deals get done, the ribbon gets cut, and they leave. Re-ordered by Kai: 1.3 \u2192 1.1 \u2192 1.2 \u2192 1.6 \u2192 1.7 \u2192 1.4 \u2192 1.5 \u2192 1.8\u20131.11.',
         shots=[('23-f1-b', 'the stock market is roaring'),
                ('23-f2-b', 'the celebration \u2014 pay packets'),
                ('21-f5-b', 'the deal, at leisure'),
                ('21-f1-b', 'the executive cars'),
                ('21-f3-b', 'the executive planes \u2014 they fly to the golf club'),
                ('22-f1-a', 'the golf course, watered'),
                ('21-f2-b', 'the conference'),
                ('20-f1-a', 'the ribbon'),
                ('20-f3-b', 'the ribbon, the other angle'),
                ('20-f5-b', 'the red carpet, afterwards, nobody on it'),
                ('21-f4-b', 'the hall, afterwards, the empty seats')]),
    dict(n='2', name='The build', line='Small camp \u2192 big build \u2192 the towers are there \u2192 the power \u2192 inside \u2192 the board \u2192 pull out to the world. Kai dropped the two interiors with figures.',
         shots=[('25-f4-b', 'the small camp'),
                ('25-f3-a', 'still small'),
                ('25-f1-a', 'now it is a big build'),
                ('25-f2-a', 'the towers are there'),
                ('27-f1-b', 'the power comes online'),
                ('27-f2-a', 'the power'),
                ('27-f4-b', 'the power'),
                ('28-f3-a', 'inside \u2014 Kai: "a good one"'),
                ('28-f4-b', 'THE CONTROL BOARD \u2014 "now I\u2019ve got a home I can work with"'),
                ('T1-b', 'PULL OUT \u2014 the data centres given a body in the world')]),
    dict(n='3', name='The weather, and the soil', line='Merged by Kai. His face first, so a human carries it; the dust wall is gone. 5.1 \u2192 4.1 \u2192 4.2 \u2192 4.3 \u2192 5.3.',
         shots=[('04-f3-a', 'the farmer \u2014 the human emotion that opens it'),
                ('02-f1-b', 'the UK from orbit'),
                ('02-f4-b', 'over the top of the clouds'),
                ('02-f3-a', 'inside the cloud, toward the sun'),
                ('04-f1-a', 'the farmer, after')]),
    dict(n='4', name='How it\u2019s going', line='The montage of working people, under music and the narrator. Ends on the dam wall \u2014 the graph was on the world all along.',
         shots=[('05-f2-b', 'happiness'), ('05-f3-b', 'happiness'), ('05-f4-a', 'happiness'),
                ('07-f1-b', 'water'),
                ('10-f2-a', 'birth rate'), ('10-f4-b', 'birth rate'),
                ('15-f1-b', 'the checkout'), ('15-f4-b', 'the checkout'),
                ('16-f1-a', 'the doorway'), ('16-f3-b', 'the doorway'), ('16-f5-a', 'the doorway'),
                ('17-f1-b', 'the school run'), ('17-f5-b', 'the school run'),
                ('18-f1-a', 'the high street'), ('18-f2-a', 'the high street'),
                ('19-f1-a', 'the playground'), ('19-f2-a', 'the playground'),
                ('19-f3-a', 'the playground'), ('19-f4-a', 'the playground'),
                ('11-f4-a', 'THE DAM WALL \u2014 the trend line, already painted on the world')]),
]

TALL_SRC = {'T1-a': '00-a.jpg', 'T1-b': '00-b.jpg', 'T2-a': '01-a.jpg', 'T2-b': '01-b.jpg',
            'T3-a': '02-a.jpg', 'T3-b': '02-b.jpg', 'T4-a': '03-a.jpg', 'T4-b': '03-b.jpg'}

titles = {}
for m in re.finditer(r'^## (\d\d) · (.+?)\n', MD.read_text(), re.M):
    titles[m.group(1)] = m.group(2).strip()


def source(key):
    if key in TALL_SRC:
        return TALL / TALL_SRC[key]
    num, f, c = key.split('-')
    return STILLS / FOLDERS[num] / f'{int(f[1:]) - 1:02d}-{c}.jpg'


out, missing, n = [], [], 0
for b in BEATS:
    items = []
    for key, cap in b['shots']:
        src = source(key)
        if not src.exists():
            missing.append(key); continue
        dst = IMG / f'{key}.jpg'
        if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
            subprocess.run(['convert', str(src), '-resize', '1100x', '-quality', '80', str(dst)], check=True)
        n += 1
        items.append({'key': key, 'src': f'img/{key}.jpg', 'cap': cap,
                      'no': f"{b['n']}.{len(items) + 1}",
                      'shot': titles.get(key.split('-')[0], '')})
    out.append({'n': b['n'], 'name': b['name'], 'line': b['line'],
                'pick': bool(b.get('pick')), 'items': items})

page = (HERE / 'template_seq.html').read_text().replace('/*DATA*/null', json.dumps({'beats': out, 'total': n}))
(OUT / 'index.html').write_text(page)
size = sum(p.stat().st_size for p in IMG.glob('*.jpg')) / 1e6
print(f'{n} frames across {len(out)} beats -> {OUT}/index.html ({size:.1f} MB)')
if missing:
    print('MISSING:', ', '.join(missing))
