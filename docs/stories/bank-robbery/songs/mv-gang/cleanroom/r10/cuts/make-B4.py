"""Cut 10B, round 4: Kai's round-3 note (2026-11-11, feedback/timeline-r10B3/at260): "them walking down the road is a really
good drop with the beat, but it should last longer … cut out the train scene and the boat scene and have them just walking down
the road up until we then switch to them in the car". a01m-a now runs from its kick (10.52) to the car (13.07); k10-a and k09m-a out."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
plan = json.load(open(HERE / 'plan-B3.json'))
i = next(k for k, r in enumerate(plan) if r['clip'] == 'a01m-a' and r['start'] < 12)
assert [r['clip'] for r in plan[i + 1:i + 4]] == ['k10-a', 'k09m-a', 'z02y-b'], plan[i + 1:i + 4]
plan[i]['end'] = plan[i + 3]['start']; plan[i]['in'] = 0.5
plan[i]['why'] = 'the walk held through the drop to the car (Kai: "it\'s a cool shot")'
del plan[i + 1:i + 3]
(HERE / 'plan-B4.json').write_text(json.dumps(plan, indent=1, ensure_ascii=False))
print(plan[i]['start'], plan[i]['end'], 'a01m-a', len(plan), 'shots')
