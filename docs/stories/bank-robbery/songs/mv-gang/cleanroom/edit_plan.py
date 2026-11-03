"""The cut: each lyric line of "the version.wav" (Whisper times, song-transcript.json) → the clip that shows it.
Writes edit-plan.json: [{start, end, clip, line}]. A clip id is <shot>-<take>, file <media>/video/<shot>r2-<take>.mp4."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
CUTS = [  # start, clip, what is heard — round 2, Jack's 34 picks + the 16 clips made before he picked (2026-11-03)
 (0.00,"a01-a","intro guitar"),(3.90,"a01-b","intro guitar"),(7.80,"a02-b","Robbery!"),(13.40,"a03-b","music"),(16.80,"x02-a","music"),
 (20.14,"v01-b","they say you can't make money from a tree / make hay"),(25.26,"v03-b","work and get paid though"),
 (28.50,"d01-b","where does it go? nobody knows (v04 not picked)"),(31.30,"v05-b","means of production means a reduction"),
 (33.34,"v06-b","standards bleeding, landlords needing"),(35.92,"v07-b","quantitative easing, grandma freezing"),
 (38.68,"v08-b","stimulus checks, get wrecked / rent seeking (v09 not picked)"),(43.72,"a02-a","sorry, did I interrupt your meeting? (v10 not picked)"),
 (46.46,"v11-b","remember kids, the Fed is not your friend"),(48.68,"v12-b","it prints all the dollars that the government spends"),
 (51.66,"v13-b","this fiat system is insistent on debt's existence"),(55.30,"x03-b","so don't be hating on the credit rating"),
 (59.48,"x01-a","or have resistance to the facts I'm stating"),
 (61.86,"c01-b","Robbery, robbery!"),(64.60,"c02-b","call the police, it's a robbery"),(67.04,"c03-a","debasement, it happened in da basement"),
 (69.60,"c04-a","printer is burning"),(72.52,"x04-a","Robbery, robbery!"),(74.32,"c02-a","call the police, it's a robbery"),
 (77.36,"c03-b","debasement, it happened in da basement"),(79.98,"c04-b","printer is burning"),
 (82.76,"d01-a","stacks and stacks of elastic cash"),(85.14,"d02-b","distracted by a dyspraxic flash"),
 (87.80,"d02-a","mob, angry at their shitty little job (d03 not picked)"),(90.06,"d05-a","the right and the left both witness the theft / blaming each other"),
 (95.26,"d06-a","institutional, dilutional, the usual"),(98.70,"x02-a","distraction is the attraction (d07 not picked)"),
 (101.88,"d08-b","divide and conquer, just look at the hand"),(105.36,"a03-a","not your standard propaganda, worth a couple grand (e02 not picked)"),
 (108.42,"d10-a","state level manipulation, the devil with a radio station"),
 (113.46,"d11-a","stack up the vaults like a wheelbarrow"),(115.76,"d12-b","risk of default is really rather narrow"),
 (118.46,"x06-a","Biggie said way back in ninety seven"),(121.16,"v14-a","don't get high off your own supply"),
 (123.74,"c01-b","Robbery, robbery!"),(126.48,"x01-a","call the police, it's a robbery"),(129.00,"c03-b","debasement, it happened in da basement"),
 (131.62,"c04-a","printer is burning"),(134.44,"x04-a","Robbery, robbery!"),(136.46,"c02-a","call the police, it's a robbery"),
 (139.30,"c03-a","debasement, it happened in da basement"),(141.94,"c04-b","printer is burning"),
 (144.18,"x02-a","you know the real star is Pablo Escobar"),(146.62,"d01-b","who has elastic bands, not plastic hands (e02 not picked)"),
 (149.66,"d01-a","stacking up the cash by the grands"),(152.10,"e03-a","standard plans are for the working man"),
 (154.74,"f01-a","and this right here is a next level scam"),(157.04,"x07-b","ill gotten gains, no need to explain"),
 (159.84,"f02-a","'bail' and 'out' will never mean the same"),(162.54,"f03-b","own the printer and you don't fear winter"),
 (164.92,"v12-b","crime is asset inflation, a wealth gap (f04 not picked)"),
 (170.08,"v03-b","working people get paid in money (f05 not picked)"),(172.70,"d11-a","so it's not very funny when you print more"),
 (175.94,"v05-b","hungry people feed a revolution, retribution (f06 not picked)"),
 (180.52,"f08-b","it's time to give, not just to take, but for heaven's sake"),
 (184.62,"v11-b","don't just eat cake (f09 not picked)"),(188.46,"x03-b","Robbery!"),(194.00,"x01-a","Robbery!"),(199.14,"x07-b","Robbery!"),
 (204.00,"a01-a","Robbery! (end)"),
]
END = 209.6
rows = [{"start": s, "end": (CUTS[i + 1][0] if i + 1 < len(CUTS) else END), "clip": c, "line": l} for i, (s, c, l) in enumerate(CUTS)]
for r in rows: r["dur"] = round(r["end"] - r["start"], 2)
json.dump(rows, open(HERE.parent / "edit-plan.json", "w"), indent=1, ensure_ascii=False)
print(len(rows), "cuts; longest", max(r["dur"] for r in rows), "s")
