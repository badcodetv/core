"""Clip briefs for the six closer action stills (picked by mask check: y01 b, y02 a, y03 a, y04 a, y05 a, y06 a)."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).parent; CR = HERE.parent
sys.path.insert(0, str(CR / "r3"))
import importlib.util
_s = importlib.util.spec_from_file_location("mcb8", HERE / "make_clip_briefs.py"); M = importlib.util.module_from_spec(_s); _s.loader.exec_module(M)
from make_gesture_clip_briefs import FACTS, RULES
P8 = json.load(open(CR / "prompts-r8.json"))
r7 = (CR / "r7" / "research.md").read_text(); fix = r7[r7.index("## 3."):r7.index("## 4.")]
r8 = (HERE / "research.md").read_text(); car = r8[r8.index("## 4."):]
PICK = ["y01-b", "y02-a", "y03-a", "y04-a", "y05-a", "y06-a"]
for w, keys in {"cy1": PICK[:3], "cy2": PICK[3:]}.items():
    parts = [f"# Your {len(keys)} shots\n"]
    for k in keys:
        p = P8[k.split("-")[0]]
        parts.append(f"## {k} — {p['t']} in the song — {p['line']}\nWhat it replaces and why: {p['what']}\nStill (open it and look): {M.MB}/{k.replace('-', 'r8-')}.jpg\nThe still's prompt was:\n{p['prompt']}\n")
    brief = "\n\n".join(["# The job\n\nYou write image-to-video motion prompts (Google Flow, its fast image-to-video model, 6 s, 16:9) for a glossy 1920s Prohibition music video: masked robbers in sharp suits pulling heists. These replace action clips the director rejected (masks wrong, or AI slop).",
                         M.jack, FACTS, M.EXTRA.replace("rapping shots", "action shots"), "- Action: one simple, physical action with weight that completes and settles; one dominant motion; nothing weightless or foam-like.",
                         "\n".join(parts), "# Web research: keeping the mask stable\n\n" + M.mask, "# Web research: physical action that reads as real\n\n" + fix, "# Web research: the getaway car\n\n" + car,
                         RULES.format(out=HERE / f"clip-{w}.md").replace("g08-b or v01g-b", "y01-b")])
    (HERE / f"brief-clip-{w}.md").write_text(brief); print(w, keys, len(brief.split()))
