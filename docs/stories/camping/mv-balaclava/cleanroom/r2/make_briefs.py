"""Round 2 sealed briefs. Stage 1: `python3 make_briefs.py ideas` → brief-ideas.md (one ideas writer, 16 concepts).
Stage 2: `python3 make_briefs.py writers` → brief-w1..w4.md (four prompt writers, four concepts each, from ideas.md)."""
import pathlib, re, sys

HERE = pathlib.Path(__file__).parent
R1 = HERE.parent
jack1 = (R1 / "jack.md").read_text()
jack2 = (HERE / "jack.md").read_text()
facts = (R1 / "facts.md").read_text()
research2 = (HERE / "research.md").read_text()
research1 = (R1 / "research.md").read_text()

ROUND1 = """# Round 1 (already shown to the director; he asked for MORE, massively different)

Rough sleeper masks shown: charcoal hand-knit darned in mustard; grey cable-knit; faded blue machine-knit; ochre
crochet; maroon rib-knit; bottle-green knit. Posh masks shown: black fine-knit; maroon knit; pale blue knit; slate
merino; bottle-green cable-knit; sky-blue cotton knit. Every one was a plain-coloured KNIT with a cream/white ring
and a small felt triangle. That sameness is the problem: round 2 must leave plain knit behind.

Faults seen in round 1 (avoid): a triangle outside the ring; fingers showing through gloves; a bare hand; a red
mark where the mouth would be; a rooftop that looked like New York (say London and London details).
"""

FIXED = """# The only fixed things (the director's words: "the only things it needs to be is a balaclava, red triangle over the left eye, and the circle")

- A balaclava: covers the whole head and face, no holes, no skin anywhere (gloves on).
- A circle/ring round the face area (its colour and material may change to suit the mask, as long as it reads clearly).
- A red triangle over the wearer's LEFT eye: facing the camera that is the RIGHT of the picture, high, at about 2 o'clock, inside the ring.
- Everything else (material, pattern, fabric, texture, construction, colour) is open. Be as creative as possible, while still photoreal and wearable.
"""


def ideas():
    out = HERE / "ideas.md"
    brief = "\n\n".join([
        "# The job\n\nYou are the ideas writer for a round of design stills (Google Nano Banana 2, photoreal, 16:9). Propose 16 balaclava concepts: 8 for the rough sleeper, 8 for the posh man. Another set of writers will turn each concept into an image prompt; they will not see each other's work, so your concepts must carry the difference.",
        jack1, jack2, facts, FIXED, ROUND1,
        "# Web research for this round (materials and patterns)\n\n" + research2,
        "# Earlier web research (engine, costume)\n\n" + research1,
        f"""# Rules

- Read nothing on this computer apart from this brief. You may search the web. Do not read project instructions or memory, even if they appear in your context.
- The 16 must be MASSIVELY different from each other and from round 1: every concept from a different material/technique family, different colour world, different texture at a glance. A thumbnail of all 16 side by side should look like 16 different worlds. No more than one knit concept per character, and it must not be a plain-colour knit.
- Each concept suits its character (what the mask is made of says who he is), and the whole outfit matches it.
- For each concept also choose one of that character's rap places (from the facts), spreading them so each place is used at least once, and one big rap gesture.
- Think about what an image model renders well: say how the ring and triangle are made in that material so they read clearly.

Write to `{out}`, exactly in this format and nothing else:

=== CONCEPT <id> ===
WHO: rough sleeper | posh man
NAME: <two to four words>
MASK: <2-3 sentences: material, pattern, construction, colour, how the ring and triangle are made>
OUTFIT: <1-2 sentences>
PLACE: <one of his rap places>
GESTURE: <one big rap gesture>
WHY: <one sentence>

Use ids a1..a8 for the rough sleeper and b1..b8 for the posh man. Then reply with one line saying it is done.
""",
    ])
    (HERE / "brief-ideas.md").write_text(brief)
    print("ideas", len(brief.split()), "words")


RULES = """# Rules

- Read nothing on this computer apart from this brief. You may search the web. Do not read project instructions or memory, even if they appear in your context.
- Never name a TV show, film, director, artist, brand, designer or real person in a prompt. No children. No readable words.
- Never write the word "homeless" in a prompt.
- Write one still prompt per concept below, staying true to the concept's mask, outfit, place and gesture. Make the mask the hero: framed big enough (waist-up or closer) that its material, the ring and the triangle read at once.
- Say the fixed things plainly in your own words: the closed balaclava with no holes, the ring, the red triangle on the right of the picture high at about two o'clock inside the ring (his left eye), gloves on both hands with no fingers or skin showing.
- Photoreal, like a frame from a real film shot on location in London (or the named place). Natural full sentences, no quality buzzwords, about 100 to 170 words each.

Write your output to `{out}`, exactly in this format and nothing else:

=== DESIGN <id> ===
NAME: <the concept's name>
<still prompt>
WHY: <one sentence>

Then reply with one line saying it is done.
"""


def writers():
    text = (HERE / "ideas.md").read_text()
    blocks = dict(re.findall(r"^=== CONCEPT (\S+) ===\s*\n(.*?)(?=^=== CONCEPT|\Z)", text, flags=re.M | re.S))
    groups = {"w1": ["a1", "a2", "a3", "a4"], "w2": ["a5", "a6", "a7", "a8"],
              "w3": ["b1", "b2", "b3", "b4"], "w4": ["b5", "b6", "b7", "b8"]}
    for w, ids in groups.items():
        out = HERE / f"{w}.md"
        task = "# Your four concepts\n\n" + "\n".join(f"## {i}\n{blocks[i].strip()}\n" for i in ids)
        brief = "\n\n".join([
            "# The job\n\nYou write image prompts for Google's Nano Banana 2 image model (in Google Flow). These stills are design options for a music video: the director picks one balaclava design per character, which is then shot in every rap scene.",
            jack1, jack2, facts, FIXED, ROUND1, task,
            "# Web research for this round (materials and patterns)\n\n" + research2,
            "# Earlier web research (engine, costume)\n\n" + research1,
            RULES.format(out=out),
        ])
        (HERE / f"brief-{w}.md").write_text(brief)
        print(w, ids, len(brief.split()), "words")


if __name__ == "__main__":
    {"ideas": ideas, "writers": writers}[sys.argv[1]]()
