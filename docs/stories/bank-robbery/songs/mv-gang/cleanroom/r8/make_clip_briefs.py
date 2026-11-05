"""Round 8 clip briefs. 'pf' = the six performers whose masks drifted, re-animated from mask-correct stills with mask-safe motion
(research r8 §1). 'cw' = the six new closer action stills (after they are made). Output r8/clip-<w>.md."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).parent; CR = HERE.parent
sys.path.insert(0, str(CR / "r3"))
from make_gesture_clip_briefs import FACTS, RULES
MB = json.load(open(CR.parent / "scene.json"))["media"] + "/moodboard"
r8 = (HERE / "research.md").read_text(); mask = r8[r8.index("## 1."):r8.index("## 2.")]
r6 = (CR / "r6" / "research.md").read_text(); moves = r6[r6.index("## 1."):r6.index("## 2.")]
jack = (HERE / "jack.md").read_text()
P2, P3, P6, P7 = (json.load(open(CR / f)) for f in ("prompts-r2.json", "prompts-r3.json", "prompts-r6.json", "prompts-r7.json"))
PF = [("z02y-b", "z02r7-b", P7["z02"]), ("p03y-b", "p03r6-b", P6["p03"]), ("z06y-b", "z06r7-b", P7["z06"]),
      ("g08y-b", "g08r5-b", P3["g08"]), ("v05y-a", "v05r5-a", P2["v05"])]
NOTE = {"v05y-a": "Line: \"Hungry people feed a revolution\". The previous clip of this still spun round (rejected); then one with mimed hunger and a fist up had the mask drift. Keep him square to the lens.",
        "g08y-b": "The gag: a stage magician's 'look at the hand' — one gloved hand held up to the lens while the other slips a banknote into his pocket."}
EXTRA = """# This round's one job: the masks must hold for the whole 6 seconds

The director has rejected these clips because the mask went wrong in motion (the red triangle slid to the centre or vanished, eye holes appeared, the ring broke). Each still below is mask-correct. Write motion that keeps every mask exactly as in the first frame:
- the masked head stays large, square to the lens, turning no more than about 15 degrees; no ducking out of frame, no hands or objects passing over a mask;
- the performance lives in the shoulders, chest, arms and hands (still big and on the beat for rapping shots), not in head turns;
- one short sentence locking the mask's look, as the research suggests; camera locked."""
OUT = sys.argv[1] if len(sys.argv) > 1 else "pf"
ONLY = sys.argv[2:]
if __name__ == "__main__":
    PF = [x for x in PF if not ONLY or x[0] in ONLY]
    parts = [f"# Your {len(PF)} shots\n"]
    for key, still, p in PF:
        parts.append(f"## {key} — {p.get('t','')} in the song — the lyric: \"{p.get('line','')}\"\nStill (open it and look): {MB}/{still}.jpg\n{NOTE.get(key,'')}\nThe still's prompt was:\n{p['prompt']}\n")
    brief = "\n\n".join(["# The job\n\nYou write image-to-video motion prompts (Google Flow, its fast image-to-video model, 6 s, 16:9) for a glossy 1920s Prohibition music video: masked robbers in sharp suits rapping to camera and pulling heists.",
                         jack, FACTS, EXTRA, "\n".join(parts), "# Web research: keeping the mask stable\n\n" + mask, "# Web research: stage moves\n\n" + moves,
                         RULES.format(out=HERE / ("clip-" + OUT + ".md")).replace("g08-b or v01g-b", "z02y-a")])
    (HERE / f"brief-clip-{OUT}.md").write_text(brief); print(len(brief.split()), "words")
