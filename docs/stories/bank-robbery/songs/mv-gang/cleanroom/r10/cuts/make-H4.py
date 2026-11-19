"""Cut 10H4: cut 10H3 with the last shot swapped for wag take b (Kai, 2026-11-19: "definitely B because it's got a
cake in it"): she holds up a real slice of cake on "heaven's sake", tosses it on "Don't", wags her finger "no" to the end.
Natural speed from in 1.0 (the 0.7x slow-down of 10H3 is gone).
Also the vault's first use (1:38) goes to the sealed-mask take, so both appearances match. Page: https://claude.ai/artifact/1gJqd59bEep7A4jr35qn9w
    python3 make-H3.py && python3 make-H4.py && python3 assemble.py H4 <page-out-dir>"""
import json, pathlib
HERE = pathlib.Path(__file__).parent
plan = json.load(open(HERE / 'plan-H3.json'))
her = plan[-1]
assert her['clip'] == 'w-v11x' and her['start'] == 183.5, her
her.pop('speed')
her.update({'clip': 'w-v11x-r2b', 'in': 1.0,
            'why': "wag b: real cake on 'heaven's sake', tossed on 'Don't', finger wag 'no' to the end (Kai picked b, 2026-11-19)"})
first = plan[48]  # the vault's first use, 1:38 "Distraction is the attraction": the old mask too, swap to the sealed take
assert first['clip'] == 'w-k36m' and abs(first['start'] - 98.244) < 0.01, first
first.update({'clip': 'w-k36m-r2b', 'in': 0.0, 'why': "mask sealed re-roll w-k36m-r2b, as at 2:58 (Kai 2026-11-19: no eye or mouth gap); was: " + first['why']})
(HERE / 'plan-H4.json').write_text(json.dumps(plan, indent=1, ensure_ascii=False))
print('plan-H4.json written')
