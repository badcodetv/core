"""One sealed clip brief for the two clip-only fixes (v05 spin teleports; v11 gesture must match "don't just eat cake").
Both reuse their round-5 stills (masks checked then). Output r7/clip-fx.md -> keys v05x-a, v11x-a."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).parent; CR = HERE.parent
sys.path.insert(0, str(CR / "r3"))
from make_gesture_clip_briefs import FACTS, RULES
MB = json.load(open(CR.parent / "scene.json"))["media"] + "/moodboard"
r7 = (HERE / "research.md").read_text()
fix = r7[r7.index("## 3."):r7.index("## 4.")]; gest = r7[r7.index("## 4."):r7.index("## Sources")]
P2 = json.load(open(CR / "prompts-r2.json"))
JOBS = {"v05x-a": ("v05r5-a", "2:55", "Hungry people feed a revolution, then it's retribution, perhaps some execution",
                   "Jack on the current clip: \"when he spins around he kind of teleports please fix thanks\". No spin, no full turn: keep him facing the lens."),
        "v11x-a": ("v11r5-a", "3:05", "It's time to give, not just to take, but for heaven's sake, don't just eat cake",
                   "Jack on the current clip: \"\\\"don't just eat cake\\\" the gesturing doesnt match this line please fix thanks\". The gestures must clearly play the cake line (mimed is fine: nothing new may appear in his hands unless it is in the still).")}
parts = ["# Your 2 shots\n"]
for k, (still, t, line, note) in JOBS.items():
    parts.append(f"## {k} — {t} in the song — the lyric: \"{line}\"\nStill (open it and look): {MB}/{still}.jpg\n{note}\n")
brief = "\n\n".join(["# The job\n\nYou write image-to-video motion prompts for a glossy 1920s Prohibition music video: masked robbers in sharp suits rapping to camera over a cockney woman's rap about money printing and inequality. Each prompt animates one approved still for 6 seconds. These two replace clips the director rejected.",
                     FACTS, "\n".join(parts), "# Web research: fixing image-to-video failures\n\n" + fix, "# Web research: gestures for these lines\n\n" + gest,
                     RULES.format(out=HERE / "clip-fx.md").replace("g08-b or v01g-b", "v05x-a")])
(HERE / "brief-clip-fx.md").write_text(brief); print(len(brief.split()), "words")
