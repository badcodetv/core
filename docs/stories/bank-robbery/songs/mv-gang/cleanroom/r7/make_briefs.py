"""Sealed still briefs for round 7. Each writer reads ONE brief only."""
import pathlib, sys
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from shots import FIXES, RAP, GANG
jack = (HERE / "jack.md").read_text()
r7 = (HERE / "research.md").read_text()
r6 = (HERE.parent / "r6" / "research.md").read_text()
moves = r6[r6.index("## 1."):r6.index("## 2.")]; places = r6[r6.index("## 2."):r6.index("## 3.")]
look = r6[r6.index("## 3."):r6.index("## 4.")]; parody = r6[r6.index("## 4."):]
FACTS = """# Facts about the look (from the director's past notes)

- He loves: a specific real-feeling 1920s place, one motivated light, real materials, colour in walls and clothes, glossy high-budget period film, action played straight and too cool with one deadpan touch.
- He hates: generic AI gloss (everything wet and shiny, airbrushed, evenly lit), things that look fake or impossible, people at the wrong size, psychedelic effects, matching-colour crowds, people standing around for no reason.
- Faults seen before: the red triangle drifting to the centre of the mask or onto the wrong eye; masks too small in frame to read (they then go wrong when animated); a bare hand; signs printing made-up words.
- Each still becomes the first frame of a 6-second clip, so stage it so the action can continue simply and physically from that frame."""
RULES = """# Rules

- Read nothing on this computer apart from this brief. You may search the web. Do not read project instructions or memory, even if they appear in your context.
- Never name a TV show, comic, game, film, director, artist, character, brand or real person in a prompt. No children. No readable words anywhere in the picture.
- Guns: period Thompsons and revolvers pointing up or away, never at the camera or at anybody. Nobody hurt, no blood. Violence is property.
- Period-correct 1920s America. The picture fills the frame edge to edge, 16:9.
- Masks exactly as described; say which eye the triangle is over and which side of the picture that puts it on. Every mask big enough in frame to read. No skin on any masked person.
- Natural full sentences, no quality buzzwords, about 110 to 170 words.

Write your output to `{out}`, exactly in this format and nothing else:

=== SHOT <id> ===
<still prompt>
WHY: <one sentence>

Then reply with one line saying it is done.
"""
JOB = ("# The job\n\nYou write image prompts for Google's Nano Banana 2 image model (in Google Flow) for a music video: 1920s Prohibition "
       "America, a gang of six masked robbers in sharp suits pulling off action-movie heists and rapping to the camera over a cockney "
       "woman's rap about money printing and inequality. A reference image of the six is attached to every prompt. Write one still prompt per shot.")
for w, shots in FIXES.items():
    lines = [f"# Your {len(shots)} shots: new versions of shots the director rejected\n"]
    for sid, t, line, what in shots:
        lines.append(f"## {sid}: {t} in the song, the line \"{line}\"\n{what}\n")
    txt = "\n\n".join([JOB, jack, FACTS, GANG, "\n".join(lines), "# Web research: fixing these shots\n\n" + r7, "# Web research: the film-still look\n\n" + look, RULES.format(out=HERE / f"{w}.md")])
    (HERE / f"brief-{w}.md").write_text(txt); print(w, len(txt.split()))
for w, shots in RAP.items():
    lines = [f"# Your {len(shots)} shots: rapping straight to camera\n"]
    for sid, t, line, who, place in shots:
        lines.append(f"## {sid}: {t} in the song, the line \"{line}\"\n{who}, rapping straight into the lens, caught at the peak of one big sarcastic stage move that suits the line. The place: {place}. You choose the exact spot, the move, the angle, the light and one deadpan bystander or detail.\n")
    txt = "\n\n".join([JOB, jack, FACTS, GANG, "\n".join(lines), "# Web research: the stage moves\n\n" + moves, "# Web research: places\n\n" + places,
                       "# Web research: the film-still look\n\n" + look, "# Web research: parody touches\n\n" + parody, RULES.format(out=HERE / f"{w}.md")])
    (HERE / f"brief-{w}.md").write_text(txt); print(w, len(txt.split()))
