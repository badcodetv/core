"""Cut 10H2: cut 10H1 plus the 8 shots Kai approved on the shots page round 2 (feedback/her-shots-r2):
the six still fixes (her/r6, take a) and his original picks for h12 (peg man stays) and h18. Same slots,
in-points and lengths as plan-B5. d10 and q09 stay the originals (Kai kept them)."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
plan = json.load(open(HERE / 'plan-H1.json'))
SWAP = {'a01m-a': 'w-a01m', 'a02m-a': 'w-a02m', 'c03g-b': 'w-c03g', 'h07-b': 'w-h07', 'h12-a': 'w-h12', 'h18-b': 'w-h18',
        'k01m-a': 'w-k01m', 'k19m-a': 'w-k19m'}
n = 0
for r in plan:
    if r['clip'] in SWAP:
        r['why'] = f"her version of {r['clip']}" + (f"; was: {r['why']}" if r.get('why') else '')
        r['clip'] = SWAP[r['clip']]; n += 1
left = set(SWAP) - {r['clip'] for r in json.load(open(HERE / 'plan-H1.json'))}
assert not left, left
(HERE / 'plan-H2.json').write_text(json.dumps(plan, indent=1, ensure_ascii=False))
print(n, 'more slots swapped')
