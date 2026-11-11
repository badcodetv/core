"""Cut 10B, round 5: Kai's round-4 note (feedback/timeline-r10B4/at30): the opening girder shot "lasts a bar too long … three
quarters where it should be a half"; change the second clip (the basement ring with the banana, k13m-b), "have them all stood on a
rooftop or something", and "make the time between the first clip and the second clip equal".
Now: k19m-a 0–2.76, then k23-a (the five standing at the skyscraper parapet by the blimp) 2.76–5.34, both cut on the kick, 2.76 s
and 2.58 s. k23-a was also at 9.2 s; that slot becomes k22m-b (CRIMSON on the train step, the commuter handing him a ticket)."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
plan = json.load(open(HERE / 'plan-B4.json'))
assert [r['clip'] for r in plan[:5]] == ['k19m-a', 'k13m-b', 'y05-a', 'y04-a', 'k23-a'], [r['clip'] for r in plan[:5]]
plan[0]['end'] = 2.763
plan[1].update(start=2.763, end=5.341, clip='k23-a', **{'in': 0.0}, why='the gang stood on the skyscraper parapet (Kai: rooftop, equal to the first shot)')
plan[4].update(clip='k22m-b', **{'in': 0.5}, why='CRIMSON on the train step (k23-a moved to the second shot)')
(HERE / 'plan-B5.json').write_text(json.dumps(plan, indent=1, ensure_ascii=False))
print([(r['start'], r['end'], r['clip']) for r in plan[:6]])
