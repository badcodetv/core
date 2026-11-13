"""`camping song 2 beat 9` (Jack 2026-11-09: "at 3 mins 15 seconds, bobs bag dissapears, please use an action clip from a prevoius
camping music video sequence there instead"). Beat 8 with ONE change: 194.48-195.84 (x3, Bob walking with his bag) -> Jack's clip 33
(a boot stamping on a MANAGER badge in the mud; used in the earlier song-2 sequences, not in beat 8), from 2.2 s so the boot lands
inside the shot, under "...but I do want change". Writes edl-beat9.json."""
import json
from pathlib import Path
HERE = Path(__file__).parent
e = json.load(open(HERE / 'edl-beat8.json'))
hit = [x for x in e['V1'] if abs(x['start'] - 194.48) < 0.01 and x['src'].endswith('ca-x3-x3r1-a.mp4')]
assert len(hit) == 1, hit
hit[0].update(src='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/clips/33.mp4', shot='clip33: boot on the MANAGER badge (Jack, 3:15)', **{'in': 2.2})
json.dump(e, open(HERE / 'edl-beat9.json', 'w'), indent=1); print(hit[0])
