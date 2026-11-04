"""Sealed briefs for round 3. Each writer reads ONE brief only."""
import pathlib, sys
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from shots import FAMILIES, GANG, SINGER, GLOSS

jack = (HERE / "jack.md").read_text()
research = (HERE / "research.md").read_text()
more = (HERE / "research-more-action.md").read_text()
only = sys.argv[1:]

RULES = """# Rules

- Read nothing on this computer apart from this brief. You may search the web. Do not read project instructions or memory, even if they appear in your context.
- Never name a TV show, comic, game, film, director, artist, character or real person in a prompt. No children. No readable words anywhere in the picture (no signs, posters or papers with letters).
- Guns: period Thompsons and revolvers, held pointing up or away, never at the camera or at anybody. Nobody is wounded, no blood. Violence is property: glass, cars, barrels, fire, money, fruit.
- Period-correct 1920s America. The picture fills the frame edge to edge, 16:9.
- Masks exactly as described, every time; say which eye the triangle is over and which side of the picture that puts it on. No skin on any masked person.
- Where a lyric line is given, the picture should make sense with it.
- Each of your shots differs from the others in place, angle, lens and light. Natural full sentences, no quality buzzwords, about 100 to 170 words.

Write your output to `{out}`, exactly in this format and nothing else:

=== SHOT <id> ===
<still prompt>
WHY: <one sentence>

Then reply with one line saying it is done.
"""

for w, (theme, shots) in FAMILIES.items():
    if only and w not in only: continue
    singer = shots[0][0].startswith("h")
    lines = [f"# Your {len(shots)} shots (theme: {theme})\n"]
    for sid, t, line, pic, rap in shots:
        lines.append(f"## {sid} — {t} in the song — the line: \"{line}\"\n{pic}\n")
    job = ("# The job\n\nYou write image prompts for Google's Nano Banana 2 image model (in Google Flow) for a music video: "
           "1920s Prohibition America, a gang of masked robbers in sharp suits robbing banks and rapping to the camera over a "
           "cockney woman's rap about money printing and inequality. Glamorous, glossy period cinema with a parody streak, "
           "nothing that looks like generic AI art. Write one still prompt for each of your shots.")
    parts = [job, jack, GLOSS, SINGER if singer else GANG, "\n".join(lines),
             "# Web research for this round\n\n" + research + ("\n\n# More web research: new parody set pieces\n\n" + more if shots[0][0] >= "k17" else ""), RULES.format(out=HERE / f"{w}.md")]
    if singer:
        parts[3] += "\n(No reference image is attached to your prompts.)"
    (HERE / f"brief-{w}.md").write_text("\n\n".join(parts))
    print(w, len("\n\n".join(parts).split()), "words")
