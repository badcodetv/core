"""Round 3: every rap-to-camera shot remade in Jack's picked design. Sealed writers, one brief each.
Each writer may look at its shots' original frames (to copy place, framing and pose) and the picked design still."""
import json, pathlib

HERE = pathlib.Path(__file__).parent
CR = HERE.parent
MEDIA = pathlib.Path(json.load(open(CR.parent / "scene.json"))["media"])
jack1 = (CR / "jack.md").read_text()
jack2 = (CR / "r2" / "jack.md").read_text()
research1 = (CR / "research.md").read_text()
p2 = json.load(open(CR / "prompts-r2.json"))

JACK3 = """# What Jack said (2026-11-05, round 3, verbatim)

ive picked them but make sure they never show skin. Thanks
"""

# shot id, original clip, what the original frame shows (plain facts from looking at it)
ROUGH = [
    ("s01", "bob rapping/1.mp4", "originals/bob-1.jpg", "Night, a narrow London brick alley with graffiti, big wheelie bins and steam from a vent. Close shot, head and shoulders, slightly low, he leans into the lens mid-line."),
    ("s02", "bob rapping/1.1.mp4", "originals/bob-1.1.jpg", "Night, under a concrete motorway flyover beside a wet road, graffiti on the pillars, a fire burning in an oil drum on the right, a car passing behind. Medium shot standing, both arms spread wide, palms up."),
    ("s03", "bob rapping/2.mp4", "originals/bob-2.jpg", "Dusk, a flat London rooftop, the city skyline behind and below with lights coming on. Medium-wide standing, hands low in front of him working the beat."),
    ("s04", "bob rapping/3.mov", "originals/bob-3.jpg", "Night, the same brick alley, graffiti, bins, steam. Tight close-up, head and shoulders filling the frame, pushing toward the lens."),
    ("s05", "bob rapping/4.mp4", "originals/bob-4.jpg", "Night, under the flyover, graffiti pillars, a fire drum on the left, small tents behind. Medium shot, walking toward the camera, one hand swinging down on the beat."),
    ("s06", "bob rapping/5.5.mp4", "originals/bob-5.5.jpg", "Night, sitting on the pavement of the Thames embankment against the river wall, a small green tent beside him, St Paul's dome lit behind across the water, a foil tray of coins at his feet. Seated, both hands open and spread."),
    ("m12", "12.mp4 (maybe a rap shot)", "originals/maybe-12.jpg", "Night, under the flyover, graffiti pillars, a fire drum on the left. Medium shot standing, facing the camera."),
    ("m13", "13.mp4 (maybe a rap shot)", "originals/maybe-13.jpg", "Night, the brick alley, bins, thick steam. Low wide full-length shot, standing square to the camera, arms down."),
]
POSH = [
    ("t01", "Tarquin rapping/1.mp4", "originals/tarquin-1.jpg", "Day, a glass-walled office high over the City of London, towers through the windows. Close wide-angle shot, he leans right into the lens, grinning attitude."),
    ("t02", "Tarquin rapping/2.mp4", "originals/tarquin-2.jpg", "Day, the same high office by the window, the City spread below. Close shot leaning in, one hand low."),
    ("t03", "Tarquin rapping/2.1.mp4", "originals/tarquin-2.1.jpg", "Evening, a fine-dining restaurant, white tablecloth, a plated dish, other diners and pendant lights behind. Seated at his table facing the camera, both hands gesturing in front of him."),
    ("t04", "Tarquin rapping/3.mp4", "originals/tarquin-3.jpg", "Day, a rooftop terrace with a glass balustrade, a glass tower beside it, the City below. Very close low wide-angle, he looks down into the lens."),
    ("t05", "Tarquin rapping/4.3.mp4", "originals/tarquin-4.3.jpg", "Day, the deck of a large white motor yacht at sea, white seating behind. Medium shot standing, one hand raised, gesturing."),
    ("t06", "Tarquin rapping/4.4.mp4", "originals/tarquin-4.4.jpg", "Day, a tropical beach, reclining on a lounger under palms, a cocktail in one hand, a laptop on his lap, the sea behind."),
    ("t07", "Tarquin rapping/5.mp4", "originals/tarquin-5.jpg", "An underground car park, fluorescent strip lights, concrete pillars, a black luxury saloon right behind him. Medium-wide standing, leaning forward, hands low."),
    ("t08", "Tarquin rapping/6.mp4", "originals/tarquin-6.jpg", "Day, an English country-house garden party: lawn, a pool, guests in summer clothes with champagne behind. Medium shot standing, facing the camera."),
    ("m19", "19.mp4 (maybe a rap shot)", "originals/maybe-19.jpg", "Grey day, just inside the glass entrance of a supermarket, rain outside. Tight close-up, face to the camera, angry."),
    ("m23", "23.mp4 (maybe a rap shot)", "originals/maybe-23.jpg", "Sunset, a City of London street in front of tall glass office towers. Medium shot, pointing at the camera."),
]
WRITERS = {"w1": ("rough", "a7", "ref-rough", ROUGH), "w2": ("posh", "b1", "ref-posh", POSH[:5]), "w3": ("posh", "b1", "ref-posh", POSH[5:])}

RULES = """# Rules

- Read nothing on this computer apart from this brief and the image files it names (look at them). You may search the web. Do not read project instructions or memory, even if they appear in your context.
- The picked design still is ATTACHED to every generation as a reference image. Say the man's mask and clothes are exactly as in the attached reference. Then restate the fixed rules plainly: the closed balaclava with no holes, the ring round the face, the red triangle high on the right of the picture at about two o'clock inside the ring (his left eye), and NO SKIN ANYWHERE: gloves on both hands with no fingers, wrists or palms bare, collar or scarf closed round the neck, cuffs over the wrists. The director's one note this round is "make sure they never show skin".
- Rebuild each original shot: same place, time of day, framing, lens feel, pose and gesture as the original frame, with the masked man in place of the original man. Do not describe the original man's face or hair. Keep the mask large in frame so the ring and triangle read.
- Never name a TV show, film, director, artist, brand or real person. No children. No readable words. Never write "homeless".
- Photoreal, a frame from a real film shot on location. Natural sentences, no quality buzzwords, 90 to 160 words each.

Write your output to `{out}`, exactly in this format and nothing else:

=== SHOT <id> ===
<still prompt>
WHY: <one sentence>

Then reply with one line saying it is done.
"""


def main():
    shots = {}
    for w, (who, did, ref, rows) in WRITERS.items():
        design = p2[did]
        lines = [f"# Your shots ({len(rows)})\n"]
        for sid, clip, img, what in rows:
            lines.append(f"## {sid} (replaces clip `{clip}`)\nOriginal frame to look at: `{MEDIA / img}`\n{what}\n")
            shots[sid] = {"writer": w, "who": who, "ref": ref, "clip": clip, "orig": img, "what": what}
        out = HERE / f"{w}.md"
        brief = "\n\n".join([
            "# The job\n\nYou write image prompts for Google's Nano Banana 2 image model (in Google Flow), each run with one reference image attached. A British music video: in the shots where the original men rapped to the camera, a masked man now raps in their place. The design is picked; your job is to put it into each shot.",
            jack1, jack2, JACK3,
            f"# The picked design: {design['name']} ({who})\n\nThe still the director picked (look at it): `{MEDIA / 'reference' / ('rough-duct-tape.jpg' if who == 'rough' else 'posh-tweed.jpg')}`\n\nThe prompt that made it, for reference only (do not copy it):\n\n{design['prompt']}",
            "\n".join(lines),
            "# Earlier web research (engine, costume)\n\n" + research1,
            RULES.format(out=out),
        ])
        (HERE / f"brief-{w}.md").write_text(brief)
        print(w, len(rows), len(brief.split()), "words")
    json.dump(shots, open(HERE / "shots.json", "w"), indent=1)


if __name__ == "__main__":
    main()
