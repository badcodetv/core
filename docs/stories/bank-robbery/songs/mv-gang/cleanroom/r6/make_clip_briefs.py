"""Sealed clip briefs, round 6 (Jack 2026-11-05 picked 14 rap-to-camera stills; "uxp is open").
Each writer reads ONE brief and looks at its stills. Output r6/clip-cwN.md; parse_clips.py turns them into video jobs."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).parent
CR = HERE.parent
sys.path.insert(0, str(CR / "r3"))
from make_gesture_clip_briefs import FACTS, RULES  # the clip facts and rules from round 3d, unchanged
P = json.load(open(CR / "prompts-r6.json"))
MB = json.load(open(CR.parent / "scene.json"))["media"] + "/moodboard"
r6 = (HERE / "research.md").read_text()
moves = r6[r6.index("## 1."):r6.index("## 2.")]
parody = r6[r6.index("## 4."):]
clipres = (CR / "research-clips.md").read_text()
clipres = clipres[clipres.index("## 1."):clipres.index("## 4.")]
PICKS = ["p01-a", "p02-a", "p03-b", "p04-b", "p05-a", "p06-b", "p07-b", "p08-b", "p10-b", "p11-b", "p12-a", "p13-a", "p15-a", "p16-a"]
JOBS = [(k, k.replace("-", "r6-")) for k in PICKS]
WRITERS = {f"cw{i + 1}": JOBS[i::4] for i in range(4)}
JACK = """# What the director has said, word for word

Today: "please come up with stills of them rapping at the camera at cinematic cool prohabition era places, rapping like eminem does live in the early 200s, with how they gesture." He then picked these stills to animate.
Earlier: "all of the balaclava rappers are not gesturing enough, they kind of just point sometimes, but think of eminiem when he is perfoming on stage and use those gestures but in a sarcastic way."
On earlier clips: "everything is so exaggerated please make it simple" · "ai slop lets just remove this one": that was about physics and objects (things morphing, cars teleporting), not performance. The BODY performs big; the world stays simple and solid.
From the band's meeting: the clips replace repeated shots in the cut; "it's the attitude of the body movement"."""
if __name__ == "__main__":
    for w, jobs in WRITERS.items():
        parts = [f"# Your {len(jobs)} shots\n"]
        for key, still in jobs:
            p = P[key.split("-")[0]]
            parts.append(f"## {key} — {p['t']} in the song — the lyric: \"{p['line']}\" — {p['who']}, {p['place']}\nStill (open it and look): {MB}/{still}.jpg\nThe still's prompt was:\n{p['prompt']}\n")
        out = HERE / f"clip-{w}.md"
        brief = "\n\n".join(["# The job\n\nYou write image-to-video motion prompts for a glossy 1920s Prohibition music video: a gang of masked robbers in sharp suits rapping to camera over a cockney woman's rap about money printing and inequality. Each prompt animates one approved still for 6 seconds; the job is the performance: big, sarcastic stage-rapper moves straight at the lens, with the deadpan bystander carrying on.",
                             JACK, FACTS, "\n".join(parts), "# Web research: the stage moves\n\n" + moves, "# Web research: parody touches\n\n" + parody,
                             "# Web research: writing image-to-video prompts\n\n" + clipres, RULES.format(out=out).replace("g08-b or v01g-b", "p01-a")])
        (HERE / f"brief-clip-{w}.md").write_text(brief)
        print(w, [j[0] for j in jobs], len(brief.split()), "words")
