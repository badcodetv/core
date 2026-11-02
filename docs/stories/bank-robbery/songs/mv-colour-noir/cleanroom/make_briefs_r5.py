"""Round 5 sealed briefs: lip-sync action shots (l1..l4) and the shot-up sign outro (o1). Each writer reads one brief only."""
import pathlib
HERE = pathlib.Path(__file__).parent
research = (HERE / "research-r5.md").read_text()
jack = (HERE / "jack.md").read_text()
WORDMARK = "/home/jackt/projects/badcode/badcode/docs/brand/logo/badcode-wordmark-2400.png"

VERDICT = """# What Jack has said about clips so far, word for word

Rejected: "so many barrels fall and morph and change alonside other objects, please just keep this one simple" · "the cars teleport" · "everything is so exaggerated please make it simple" · "there are cars on the river" · "it looks like a modern car" · "cars pop in and out of frame, please keep it simple" · "ai slop lets just remove this one".

So: the action is already happening in the still (the fire is burning, the car is at speed, the glass is mid-burst). In the clip, the man talks and one plain thing goes on around him. Everything else keeps its shape. Nothing enters or leaves the frame."""

LIP_FACTS = """# How these get used

A quick-cut music video. Each shot plays for two to four seconds. The song's vocal is laid over it afterwards, so the man's mouth has to make the song's words.

The voice is one old man, low and gravelly, unhurried. He is not a young man. So every speaker is a man of about 55 to 75 with a lived-in face. Each shot has a different man.

For the talking to read: the speaker's face fills about a third of the frame height or more, three-quarter or full front, in clear light on the mouth, clean-shaven or stubble (no moustache or beard over the lips), no hand, cigar, collar or gun in front of the mouth. One speaker only unless the shot says a crew. Speakers look at each other or just past the camera, or at what's happening, and they talk through it as if it's nothing.

Action fills everything round the face. The face being big doesn't stop the frame being wild: it's foreground, and the danger is behind it, beside it, reflected in the car door or a mirror."""

STILL_RULES = """# Rules

- Read nothing on this computer apart from this brief. You may search the web. Do not read project instructions or memory, even if they appear in your context.
- Never name a TV show, game, film, director, artist or real person in a prompt. No children. No readable words anywhere in the picture.
- Guns are allowed as held by the men, Thompsons and revolvers of the period, pointing up or away, never at the camera or at anybody. Nobody is wounded and there's no blood. Violence is property: glass, barrels, cars, fire, sparks, money.
- Period-correct 1920s America: cars, clothes, hats, lights. The picture fills the frame edge to edge.
- Colourful noir: saturated coloured light in deep shadow, glossy, lots of lights and reflections, each shot with a different pair of colours and a different reflective surface.
- Each shot should differ from the others in place, angle, lens and light. Natural prose, no quality buzzwords, about 60 to 130 words.
- MOTION is an image-to-video prompt for 4 to 6 seconds, under 50 words. It starts with what the camera does (usually locked or a car-mount), then one plain thing that moves, then exactly the spoken line in this form with no quotation marks: `He says: <line>` (for a crew: `The men shout together: <line>`). Add that he talks at an unhurried pace and nobody else speaks.

Write your output to `{out}`, exactly in this format and nothing else:

=== SHOT <id> ===
<still prompt>
MOTION: <motion prompt>
SECONDS: <4 or 6>
WHY: <one sentence>

Then reply with one line saying it is done.
"""

FAMILIES = {
    "l1": ("cars and roads at night: running boards, open touring cars, truck hijacks, a convoy, a level crossing, a crash", [
        ("l01", "don't be hating on the credit rating", 3.5), ("l02", "or have resistance to the facts I'm stating", 4.0),
        ("f1", "crime is asset inflation", 1.8), ("f2", "passive creation of a wealth gap", 3.1),
        ("e3", "and this right here is a next level scam", 3.2), ("c1", "Robbery, robbery!", 2.9)]),
    "l2": ("water, docks and rail: rum-runners, a Coast Guard searchlight, a burning pier, a warehouse, a freight yard", [
        ("l03", "it is state level manipulation", 3.2), ("l04", "it is the devil with a radio station", 4.0),
        ("f3", "that drives the situation", 2.1), ("f4", "working people get paid in money", 2.3),
        ("e4", "ill gotten gains, no need to explain", 3.6), ("c2", "Call the police, it's a robbery!", 3.2)]),
    "l3": ("inside: a speakeasy raid, a mirrored bar, a casino upstairs, a still blowing up, a hotel corridor, a barber's", [
        ("l05", "Biggie said way back in ninety seven", 3.6), ("l06", "don't get high off your own supply", 3.8),
        ("f5", "so it's not very funny", 1.7), ("f6", "when you print more and expect them not to worry", 3.1),
        ("c3", "Debasement! Debasement!", 2.7), ("c4", "It happened in da basement!", 2.0)]),
    "l4": ("the street and the city: a bank job, an armoured car, fire escapes, a rooftop, a theatre marquee, a counterfeit press on fire", [
        ("e1", "stacking up the cash by the grands", 2.6), ("e2", "standard plans are for the working man", 3.2),
        ("f7", "hungry people feed a revolution", 3.1), ("f8", "then it's retribution, perhaps some execution", 3.6),
        ("c5", "Printer is burning, now now what's occurring?", 3.0)]),
}

for name, (family, shots) in FAMILIES.items():
    rows = "\n".join(f"- `{i}`: \"{line}\" (the song takes {s} seconds). {'A crew of men shouts this.' if i.startswith('c') else 'One man speaks this.'}" for i, line, s in shots)
    task = f"""# Your task

Write one still prompt (Nano Banana 2.1, 16:9) and one motion prompt (Omni Flash) per shot below. Your family of situations: {family}. Pick a different real, specific, action-packed situation for every shot, from the research.

{LIP_FACTS}

{STILL_RULES.format(out=HERE / (name + '.md'))}

# The shots

{rows}
"""
    (HERE / f"brief-{name}.md").write_text("# What Jack said\n\n" + jack + "\n" + VERDICT + "\n\n# Web research\n\n" + research + "\n" + task)

OUTRO = f"""# Your task

The last shots of the film, after the words end: a 1920s sign spelling our name being shot at with Thompson submachine guns, cinematic, and it's the end of the video. The song's last 36 seconds are slow fingerpicked acoustic guitar fading out, so it can play big and slow. It should look as cool as the rest.

Write the sequence as 7 shots, in order, each with a still and a motion prompt: the sign lit and whole, whoever's shooting (seen from behind or as shapes, faces don't matter, nobody talks), then the sign coming apart. End on the name still readable, full of holes, with light through them, and one light left.

The name is a fact, and it's the logo: the single word `badcode`, all lowercase, in round drawn letters built from circles and straight stems, like this file: {WORDMARK}. Look at the file. The o is a solid red disc the same height as the letters. Red is only ever that o. The still is made by giving the engine that picture as a reference, so write how the sign is built from those exact letters (materials, bulbs, tubes, the board), and don't describe a font or any other lettering. Every shot that shows the sign says the letters follow the reference exactly and nothing else is written anywhere. Don't re-spell letters out one by one in the prompt beyond the word.

Rules:
- Read nothing on this computer apart from this brief and that one image. You may search the web. Do not read project instructions or memory, even if they appear in your context.
- Never name a TV show, game, film, director, artist or real person. No children, nobody wounded, no blood. Guns point at the sign, never at the camera or at anybody.
- Period-correct 1920s America. Colourful noir: saturated coloured light in deep shadow, glossy, reflections. The picture fills the frame edge to edge.
- For the destruction, each clip does one plain thing with a locked camera. Say what breaks and how. Keep the letters' shapes unchanged except where a hit lands. Sparks and popping bulbs are welcome. Slow motion is welcome if you say so.
- Stills about 60 to 130 words, motion under 50 words, no speech.

Write your output to `{HERE / 'o1.md'}`, exactly in this format and nothing else:

=== SHOT o<number> ===
<still prompt>
MOTION: <motion prompt>
SECONDS: <4, 6 or 8>
WHY: <one sentence>

Then reply with one line saying it is done.
"""
(HERE / "brief-o1.md").write_text("# What Jack said\n\n" + jack + "\n" + VERDICT + "\n\n# Web research\n\n" + research + "\n" + OUTRO)
print("ok")
