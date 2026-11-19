"""Cut 10H3: the final cut 10H2 with two changes (Kai, 2026-11-19).
1. The ending, option B from the cake page (https://claude.ai/artifact/1gJqd59bEep7A4jr35qn9w), after Tom's note
   that she doesn't look like she's saying the words: grandma's jacket shot (v07m-b) held to 183.5 s, then her
   shot (w-v11x) from in 0.5 at 0.7x speed, so she looks up on "heaven's" and mimes the cake on "eat cake".
2. The vault (178.26-180.88): w-k36m grew an eye gap and a mouth gap in her mask from ~3.3 s ("looks like a
   human under the balaclava"). Swapped for a re-roll with the mask sealed in the prompt (VAULT, IN below).
    python3 make-H3.py && python3 assemble.py H3 <page-out-dir>"""
import json, pathlib
HERE = pathlib.Path(__file__).parent
VAULT, VAULT_IN = 'w-k36m-r2b', 0.8  # r2b: cleaner gestures than r2a; 0.8-3.42 s keeps to the early part, the lens point lands on 'execution'
plan = json.load(open(HERE / 'plan-H2.json'))
v07, her, vault = plan[-2], plan[-1], plan[-3]
assert (v07['clip'], her['clip'], vault['clip']) == ('v07m-b', 'w-v11x', 'w-k36m'), (v07['clip'], her['clip'], vault['clip'])
v07['end'] = her['start'] = 183.5
v07['why'] += "; held to 183.5 s for the cake ending (Kai picked B, 2026-11-19)"
her.update({'in': 0.5, 'speed': 0.7, 'why': "B: her at 0.7x, cake mime on 'eat cake' (Tom's note, Kai picked B 2026-11-19); " + her['why']})
vault.update({'clip': VAULT, 'in': VAULT_IN, 'why': f"mask sealed re-roll {VAULT} (Kai 2026-11-19: no eye or mouth gap); was: " + vault['why']})
(HERE / 'plan-H3.json').write_text(json.dumps(plan, indent=1, ensure_ascii=False))
print('plan-H3.json written')
