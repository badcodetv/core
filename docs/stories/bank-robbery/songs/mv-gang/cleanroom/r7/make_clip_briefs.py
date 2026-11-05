"""Sealed clip briefs, round 7 (Jack picked 7 fixes + 9 rap shots on 2026-11-05). Output r7/clip-cwN.md -> parse_clips.py."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).parent; CR = HERE.parent
sys.path.insert(0, str(CR / "r3"))
from make_gesture_clip_briefs import FACTS, RULES
P = json.load(open(CR / "prompts-r7.json"))
MB = json.load(open(CR.parent / "scene.json"))["media"] + "/moodboard"
r7 = (HERE / "research.md").read_text(); r6 = (HERE.parent / "r6" / "research.md").read_text()
fix = r7[r7.index("## 3."):r7.index("## 4.")]; moves = r6[r6.index("## 1."):r6.index("## 2.")]
clipres = (CR / "research-clips.md").read_text(); clipres = clipres[clipres.index("## 1."):clipres.index("## 4.")]
PICKS = ["z01-b", "z02-a", "z03-a", "z04-b", "z05-a", "z06-b", "z07-a", "q01-b", "q02-a", "q04-a", "q05-b", "q07-b", "q08-a", "q09-a", "q11-a", "q12-b"]
JOBS = [(k, k.replace("-", "r7-")) for k in PICKS]
WRITERS = {f"cw{i + 1}": JOBS[i::4] for i in range(4)}
JACK = (HERE / "jack.md").read_text()
EXTRA = """# More facts for this round

- The cut will now HOLD shots longer (2 to 5 seconds), so the whole 6 seconds may be seen: the motion must stay clean and physical to the end, with no drift, morphing or teleporting.
- Action (z shots): one simple physical action that completes, then settles; the camera locked. Masks stay big and face-on or three-quarter; heads turn less than 30 degrees; nothing passes over a mask.
- Rap (q shots): big sarcastic stage-rapper moves on the beat from the first half-second, as in the gesture research; no spins or full turns."""
if __name__ == "__main__":
    for w, jobs in WRITERS.items():
        parts = [f"# Your {len(jobs)} shots\n"]
        for key, still in jobs:
            p = P[key.split("-")[0]]
            what = p.get("what") or f"{p['who']} rapping to camera, {p['place']}"
            parts.append(f"## {key} — {p['t']} in the song — the lyric: \"{p['line']}\" — {what}\nStill (open it and look): {MB}/{still}.jpg\nThe still's prompt was:\n{p['prompt']}\n")
        out = HERE / f"clip-{w}.md"
        brief = "\n\n".join(["# The job\n\nYou write image-to-video motion prompts for a glossy 1920s Prohibition music video: a gang of masked robbers in sharp suits pulling off action-movie heists and rapping to camera over a cockney woman's rap about money printing and inequality. Each prompt animates one approved still for 6 seconds.",
                             JACK, FACTS, EXTRA, "\n".join(parts), "# Web research: fixing image-to-video failures\n\n" + fix, "# Web research: the stage moves\n\n" + moves,
                             "# Web research: writing image-to-video prompts\n\n" + clipres, RULES.format(out=out).replace("g08-b or v01g-b", "z01-b")])
        (HERE / f"brief-clip-{w}.md").write_text(brief)
        print(w, [j[0] for j in jobs], len(brief.split()))
