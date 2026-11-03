"""Sealed briefs for the balaclava-gang round. Each writer reads ONE brief only."""
import pathlib, sys
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from shots import FAMILIES, GANG, RAP

jack = (HERE / "jack.md").read_text()
research = (HERE / "research.md").read_text()
engine = (HERE.parents[1] / "mv-colour-noir/cleanroom/research.md").read_text()  # web-only engine notes, 2026-10-30

LESSONS = """# What came back last time (facts from the previous rounds)

- Jack loved: a jeweller's shop robbery on a hot bright afternoon, a broad robber in a plum hand-knitted balaclava and a chalk-striped mustard suit admiring himself in a ruby tiara while the old jeweller holds up a mirror; a second robber in bottle green behind. Specific place, one motivated light, real materials, colour in the walls and clothes.
- Jack hated: "AI slop" (glossy, generic, everything wet and shiny), psychedelic effects, matching-colour teams of people, people wandering in for no reason.
- Faults seen: the red triangle drifted to the centre of the face or to the wrong eye; a robber had a bare hand; signs printed made-up words.
"""

RULES = """# Rules

- Read nothing on this computer apart from this brief. You may search the web. Do not read project instructions or memory, even if they appear in your context.
- Never name a TV show, game, film, director, artist or real person in a prompt. No children. No readable words anywhere in the picture (no signs, posters or papers with letters).
- Guns: period Thompsons and revolvers, held pointing up or away, never at the camera or at anybody. Nobody is wounded, no blood. Violence is property: glass, cars, barrels, fire, money.
- Period-correct 1920s America: cars, clothes, hats, police, lights. The picture fills the frame edge to edge, 16:9.
- The gang's masks and colours exactly as in the gang sheet, every time; say which eye the triangle is over and which side of the picture that puts it on. No skin on any gang member.
- The picture must show the lyric line literally: someone who hears the line and sees the still should get it at once.
- Each of your four shots differs from the others in place, angle, lens and light. Natural full sentences, no quality buzzwords, about 90 to 160 words.

Write your output to `{out}`, exactly in this format and nothing else:

=== SHOT <id> ===
<still prompt>
WHY: <one sentence>

Then reply with one line saying it is done.
"""


def main():
    for w, (theme, shots) in FAMILIES.items():
        lines = [f"# Your four shots (theme: {theme})\n"]
        for sid, t, line, pic, rap in shots:
            lines.append(f"## {sid} — at {t} in the song — the line: \"{line}\"\n{pic}\n")
        out = HERE / f"{w}.md"
        brief = "\n\n".join([
            "# The job\n\nYou write image prompts for Google's Nano Banana 2 image model (in Google Flow) for a music video: a gang of masked robbers in 1920s Prohibition America robbing banks and rapping to the camera over a song about money printing and inequality. Stylised colourful noir, period-correct, cinematic, nothing that looks like generic AI art. Write one still prompt for each of your four shots.",
            jack, GANG, RAP, LESSONS, "\n".join(lines),
            "# Web research for this round\n\n" + research,
            "# Earlier web research on the engine\n\n" + engine,
            RULES.format(out=out),
        ])
        (HERE / f"brief-{w}.md").write_text(brief)
        print(w, len(brief.split()), "words")


if __name__ == "__main__":
    main()
