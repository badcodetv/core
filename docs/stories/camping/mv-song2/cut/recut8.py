"""`camping song 2 beat 8` (Jack's round-2 timeline note at1154, 2026-11-09: "please have no bob or tarquin rapping, please replace this
clip with something else, maybe an action clip that fits the lyrics, or just that clip of money in the gutter, you decide").
Beat 7 with ONE change: 44.36-47.08 (Bob in the alley, clip 13) -> the money in the gutter (ly07) from 5.0 s in, so the car rolls in on
the drop and its splash breaks around "insane". Jack: change nothing else. Writes edl-beat8.json."""
import json
from pathlib import Path
HERE = Path(__file__).parent
e = json.load(open(HERE / 'edl-beat7.json'))
LY07 = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/r10/video/premiere/r10-ly07-ly07-a.mp4'
hit = [x for x in e['V1'] if abs(x['start'] - 44.36) < 0.01 and x['src'].endswith('clips/13.mp4')]
assert len(hit) == 1, hit
hit[0].update(src=LY07, **{'in': 5.0}, shot='ly07: money in the gutter, car on the drop (at1154)')
json.dump(e, open(HERE / 'edl-beat8.json', 'w'), indent=1)
print(hit[0])
