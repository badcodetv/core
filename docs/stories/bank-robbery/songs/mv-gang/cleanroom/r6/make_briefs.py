"""Sealed briefs for round 6. Each writer reads ONE brief only."""
import pathlib, sys
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from shots import FAMILIES, GANG, GLOSS
jack = (HERE / "jack.md").read_text().split("# From the 5 Nov")[0]
meet = "# From the band's last meeting\n\n" + (HERE / "jack.md").read_text().split("summarised in docs/misc/2026-11-05-meeting.md)\n\n")[1]
research = (HERE / "research.md").read_text()
RULES = """# Rules

- Read nothing on this computer apart from this brief. You may search the web. Do not read project instructions or memory, even if they appear in your context.
- Never name a TV show, comic, game, film, director, artist, character, brand or real person in a prompt. No children. No readable words anywhere in the picture (no signs, posters, labels or papers with letters).
- Guns, if any: period Thompsons and revolvers pointing up or away, never at the camera or anybody. Nobody hurt.
- Period-correct 1920s America. The picture fills the frame edge to edge, 16:9.
- Masks exactly as described, every time; say which eye the triangle is over and which side of the picture that puts it on. The mask must be big enough in frame to read. No skin on any masked person.
- Each man looks straight into the lens, mid-rap, caught at the peak of one big stage move. Each of your four shots uses a different move, angle, lens and light.
- Natural full sentences, no quality buzzwords, about 110 to 170 words.

Write your output to `{out}`, exactly in this format and nothing else:

=== SHOT <id> ===
<still prompt>
WHY: <one sentence>

Then reply with one line saying it is done.
"""
for w, shots in FAMILIES.items():
    lines = [f"# Your {len(shots)} shots\n"]
    for sid, t, line, who, place in shots:
        lines.append(f"## {sid}: {t} in the song, the line \"{line}\"\n{who}, rapping straight at the camera. The place: {place}. You choose the exact spot, the move, the angle, the light and the one deadpan touch.\n")
    job = ("# The job\n\nYou write image prompts for Google's Nano Banana 2 image model (in Google Flow) for a music video: "
           "1920s Prohibition America, a gang of six masked robbers in sharp suits rapping to the camera over a cockney "
           "woman's rap about money printing and inequality. Glamorous, glossy period cinema with a parody streak, nothing "
           "that looks like generic AI art. A reference image of the six is attached to every prompt. Write one still prompt per shot.")
    txt = "\n\n".join([job, jack, meet, GLOSS, GANG, "\n".join(lines), "# Web research for this round\n\n" + research, RULES.format(out=HERE / f"{w}.md")])
    (HERE / f"brief-{w}.md").write_text(txt)
    print(w, len(txt.split()), "words")
