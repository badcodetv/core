"""Writes one sealed brief per writer: Jack's words + the web research + the task + that writer's shot type."""
import pathlib
HERE = pathlib.Path(__file__).parent

BAND = "The band (the same people wherever they appear): five musicians in sharp 1930s gangster clothes: a very tall thin man on upright bass, a stout older man on trumpet, a young man on clarinet, a grey-haired woman on a small drum kit, and a broad woman in her forties with a silver streak in her black hair, who fronts the band at a period microphone."
MASK = "The masks: knitted balaclavas. Sewn on the forehead of each one, big enough to read in the frame, is the BadCode logo: a thin pale ring with one small red triangle inside it, off centre toward 2 o'clock, with rounded corners. No lettering."

SHOTS = {
    1: ("the speakeasy den and its band", "The secret den where the mob and the band live: colourful noir, the heart of the look. Include the band in at least two of your four shots. Faces with closed mouths or mid-breath for now: a wide-open singing mouth gets refused by the engine, and lip sync comes later.\n\n" + BAND),
    2: ("the band under the bridge at night", "The same band playing under a city bridge at night, gangster style, on the bank of a river. City lights reflect off the water. Parked cars' headlights are what light the band. Faces with closed mouths or mid-breath for now: a wide-open singing mouth gets refused by the engine.\n\n" + BAND),
    3: ("car chases", "Fast Prohibition-era car chases through the city: gangsters and cops. Vary who and where. It must feel fast, not posed."),
    4: ("the first-person driver", "One recurring thread: we see only through the eyes of one driver, from behind the wheel of a 1930s getaway car, in four different places and moments. The only things we ever see of the driver: oxblood leather driving gloves and a mustard check shirt cuff. It is one thread among many, so each moment should be something happening around the car, not a story about the driver."),
    5: ("the dragged safe", "A car has pulled a small safe out of a wall with a chain and is dragging it behind them, sparks flying, as they flee the cops. Four different moments or vantages of it."),
    6: ("the balaclava robberies", "A compilation of different robberies, each a different place and kind of target, by people in the masks below, with people being robbed. Colourful and fun to look at, a bit of swagger. Keep any weapons out of frame.\n\n" + MASK),
    7: ("Prohibition-era cities", "Pretty Prohibition-era American cities at night or dusk, with lights and reflections: shots built to be slow pans when animated. Interesting vantage points. No people needed. Four different cities or districts."),
    8: ("old-school hot rod racing", "Old-school hot rod racing, 1930s and 1940s cut-down roadsters. Vary where (a dry lake, a night road, a city street, anywhere good). Fast, loud, dangerous-looking."),
}

TASK = """# Your task

Write FOUR still-image prompts for Google Flow's Nano Banana 2.1 (16:9) on this one subject: **{name}**.

{detail}

Rules of the job:
- Read nothing on this computer apart from this brief. You may search the web yourself, especially for real photographs and film references of your subject.
- These are not a story. Jack wants "a bunch of cool stuff": each shot should stand on its own and make someone stop and look. Your four must differ from each other in place, vantage, scale and light.
- Everything Jack dislikes is in his words above. Don't describe those things, even to ban them.
- Write the look as visual traits. Never name a TV show, game, film, director, artist or real person in a prompt. The engine won't obey it, and we can't use it.
- No children in frame. No readable words anywhere: signs, plates and labels stay blank or illegible.
- Weapons stay out of frame. Never one pointed at a person.
- Known engine trap: the word "photograph" can give a baked-in cream border, so make sure your wording gives a picture that fills the frame edge to edge.
- Narrative prose, as long as the picture needs. No quality buzzwords.
- For each shot, also say one realistic way out of it into another shot when it's cut (a real transition, no trickery: a pillar passing the lens, a whip pan, a match on a shape or a light).

Write your output to `{out}`, exactly in this format and nothing else:

=== SHOT <n> ===
<the prompt>
WAY OUT: <one sentence>
WHY: <one sentence>

(repeat for all four, then reply with one line saying it is done)
"""

jack = (HERE / "jack.md").read_text()
research = (HERE / "research.md").read_text()
for n, (name, detail) in SHOTS.items():
    out = HERE / f"w{n}.md"
    (HERE / f"brief-w{n}.md").write_text(
        "# What Jack said, word for word\n\n" + jack + "\n# Web research\n\n" + research + "\n" + TASK.format(name=name, detail=detail, out=out))
    print(f"brief-w{n}.md", name)
