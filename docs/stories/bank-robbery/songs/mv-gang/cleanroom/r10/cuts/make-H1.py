"""Cut 10H1: the signed-off cut 10B5 (Balaclava Gang 10) with the gang's new leader in it (Kai, 2026-11-17).
Every slot, in-point and length stays exactly as in plan-B5; only the clip changes, to the w-<shot> clip
animated from Kai's pick (her/r5, feedback/her-shots-r1). The 8 shots still getting still fixes (her/r6)
and the 2 Kai kept (d10, q09) stay as they were."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
plan = json.load(open(HERE / 'plan-B5.json'))
SWAP = {'k04m-a': 'w-k04m', 'h06-b': 'w-h06', 'h01-b': 'w-h01', 'h02-a': 'w-h02', 'h19-a': 'w-h19', 'k36m-b': 'w-k36m',
        'h17-b': 'w-h17', 'h13-b': 'w-h13', 'h15-b': 'w-h15', 'h11-b': 'w-h11', 'p05-a': 'w-p05', 'q12-b': 'w-q12',
        'q01-b': 'w-q01', 'q04-a': 'w-q04', 'q05-b': 'w-q05', 'd06m-a': 'w-d06m', 'g08y-b': 'w-g08y', 'q08-a': 'w-q08', 'v11x-a': 'w-v11x'}
n = 0
for r in plan:
    if r['clip'] in SWAP:
        r['why'] = f"her version of {r['clip']}" + (f"; was: {r['why']}" if r.get('why') else '')
        r['clip'] = SWAP[r['clip']]; n += 1
missing = set(SWAP) - {r['clip'] for r in json.load(open(HERE / 'plan-B5.json'))}
assert not missing, missing
(HERE / 'plan-H1.json').write_text(json.dumps(plan, indent=1, ensure_ascii=False))
print(n, 'slots swapped')
