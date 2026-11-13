"""Sealed briefs for the Camping balaclava design round. Each writer reads ONE brief only."""
import pathlib

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parents[4]

jack = (HERE / "jack.md").read_text()
facts = (HERE / "facts.md").read_text()
research = (HERE / "research.md").read_text()
engine = (ROOT / "docs/stories/bank-robbery/songs/mv-colour-noir/cleanroom/research.md").read_text()  # web-only, 2026-10-30

LESSONS = """# What came back on another film with the same mask (facts)

- The red triangle drifted to the middle of the face or onto the wrong eye, especially when the mask was small
  in the frame or dark in colour. Framed big and lit, it held.
- A robber came back with a bare hand; another with eye holes. Say the gloves and the closed mask plainly.
- Jack hates "AI slop": glossy, generic, everything wet and shiny, plastic skin and cloth, perfect symmetry.
  What he loved: a specific real place, one motivated light, real materials with wear, colour in the clothes.
- Signs and papers printed made-up words. Keep lettering out of the picture.
"""

RULES = """# Rules

- Read nothing on this computer apart from this brief. You may search the web. Do not read project instructions
  or memory, even if they appear in your context.
- Never name a TV show, film, director, artist, brand or real person in a prompt. No children. No readable words.
- Never write the word "homeless" in a prompt.
- Your three designs must be genuinely different from each other: different mask material and colour, different
  clothes, different silhouette and attitude. Not variations of one idea.
- Each prompt shows ONE man, facing the camera, mid-rap with a clear gesture, in the place given, filling enough
  of the 16:9 frame that the mask reads (waist-up or closer, or seated close).
- Every prompt states the mask rule in your own words: closed knitted balaclava, no holes, white ring round the
  face, small red triangle high over his LEFT eye (right of the picture, about 2 o'clock), gloves, no skin.
- Photoreal, like a frame from a real film shot on location. Natural full sentences, no quality buzzwords
  ("4k", "masterpiece", "hyper-detailed"), about 90 to 160 words each.

Write your output to `{out}`, exactly in this format and nothing else:

=== DESIGN <id> ===
NAME: <a two-to-four word name for the design>
<still prompt>
WHY: <one sentence on what the design says about him>

Then reply with one line saying it is done.
"""

WRITERS = {
    "w1": ("the rough sleeper", [("r1", "the brick alley at night"), ("r2", "under the motorway flyover by the fire drum"), ("r3", "sitting on the Thames embankment at night by his small tent")]),
    "w2": ("the rough sleeper", [("r4", "the rooftop at dusk over the city"), ("r5", "the brick alley at night"), ("r6", "under the motorway flyover by the fire drum")]),
    "w3": ("the posh man", [("p1", "the glass penthouse office over the City"), ("p2", "the fine-dining restaurant table"), ("p3", "the deck of the white yacht at sea")]),
    "w4": ("the posh man", [("p4", "the underground car park beside the black BMW"), ("p5", "the country-house garden party by the pool"), ("p6", "the beach lounger under palms")]),
}


def main():
    for w, (who, designs) in WRITERS.items():
        task = [f"# Your task\n\nDesign {who} three times, three different ways. Write one still prompt per design, each in its place:\n"]
        task += [f"- **{i}**: {place}" for i, place in designs]
        out = HERE / f"{w}.md"
        brief = "\n\n".join([
            "# The job\n\nYou write image prompts for Google's Nano Banana 2 image model (in Google Flow). These stills are design options: the director will pick one design per character, and it will then be shot in every rap scene.",
            jack, facts, LESSONS, "\n".join(task),
            "# Web research for this round\n\n" + research,
            "# Earlier web research on the engine\n\n" + engine,
            RULES.format(out=out),
        ])
        (HERE / f"brief-{w}.md").write_text(brief)
        print(w, len(brief.split()), "words")


if __name__ == "__main__":
    main()
