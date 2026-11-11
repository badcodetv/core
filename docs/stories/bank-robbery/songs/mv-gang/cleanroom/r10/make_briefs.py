"""Sealed still briefs for round 10. Each writer reads ONE brief only (w1..w5, four shots each)."""
import pathlib, sys
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from shots import SHOTS, GANG
kai = (HERE / "kai.md").read_text()
r6 = (HERE.parent / "r6" / "research.md").read_text()
moves = r6[r6.index("## 1."):r6.index("## 2.")]; look = r6[r6.index("## 3."):r6.index("## 4.")]; parody = r6[r6.index("## 4."):]
JOB = ("# The job\n\nYou write image prompts for Google's Nano Banana 2 image model (in Google Flow) for a music video: 1920s Prohibition "
       "America, a gang of six masked robbers in sharp suits pulling off action-movie heists, cut with the gang rapping to the camera, over a "
       "cockney woman's rap about money printing and inequality. This round: the WHOLE GANG performing at the lens together like a modern street "
       "rap crew in its own video, in places that are already in the film. Each prompt is sent with two attached pictures: a frame of the place "
       "from the film, and the gang's line-up card. Each still becomes the first frame of a 6-second clip of them performing.")
FACTS = """# Facts about the look (from the directors' past notes)

- They love: a specific real-feeling 1920s place, one motivated light, real materials, colour in walls and clothes, glossy high-budget period film, played straight and too cool with one deadpan touch.
- They hate: generic AI gloss (everything wet and shiny, airbrushed, evenly lit), things that look fake or impossible, people at the wrong size, psychedelic effects, matching-colour crowds.
- Faults seen before: the red triangle drifting to the centre of the mask or onto the wrong eye; masks too small in frame to read (they then go wrong when animated); a bare hand; signs printing made-up words; one man drawn far bigger than the others.
- The group shots that worked in this film so far: the six packed shoulder to shoulder in a cellar round a printing press, fists up; the six on a jazz-club bandstand pointing at the lens; the six in a boxing ring staring up at the lens; the six on a ferry deck wagging fingers. All six faces large, close together, filling the frame.
- Each still becomes the first frame of a 6-second clip, so catch them mid-move in a way the motion can carry on simply."""
RULES = """# Rules

- Read nothing on this computer apart from this brief. You may search the web: research how a modern UK street rap crew (five or six young men) performs at the camera in its videos, the group body language, the formation, the camera position, so the gang can move that way in 1920s suits. Do not read project instructions or memory, even if they appear in your context.
- Never name a TV show, comic, game, film, director, artist, rapper, crew, song, character, brand or real person in a prompt. Describe bodies and framing only. No children. No readable words anywhere in the picture.
- No guns in these shots; their hands are busy performing. Nobody hurt. No obscene gestures, no gang hand signs.
- Use the place: say it is the place in the attached frame from the film, keep its light, colour and materials, and make the adjustment given. Refer to each attached picture by what it shows, never by "first" or "second".
- All six men in frame (five is fine if the sixth is doing one deadpan thing just behind), all at normal human scale, packed close, the nearest about waist-up. Every mask big enough to read. Vary the camera: low, wide-angle, close to the front man, slightly tilted, as such videos do; your four shots must not share an angle or a formation.
- Masks exactly as described; say which eye the triangle is over and which side of the picture that puts it on. No skin on any masked man.
- Period-correct 1920s America; the picture fills the frame edge to edge, 16:9.
- Natural full sentences, no quality buzzwords, about 120 to 180 words.

Write your output to `{out}`, exactly in this format and nothing else:

=== SHOT <id> ===
<still prompt>
WHY: <one sentence>

Then reply with one line saying it is done.
"""
for w, shots in SHOTS.items():
    lines = [f"# Your {len(shots)} shots\n"]
    for sid, place, adjust in shots:
        lines.append(f"## {sid}\nThe place as it is in the film (the attached frame): {place}.\nThe adjustment: {adjust}.\nYou choose the formation, the moment of the move, the camera, and one deadpan detail.\n")
    txt = "\n\n".join([JOB, kai, FACTS, GANG, "\n".join(lines), "# Web research from an earlier round: stage moves of one solo rapper\n\n" + moves,
                       "# Web research: the film-still look\n\n" + look, "# Web research: parody touches\n\n" + parody, RULES.format(out=HERE / f"{w}.md")])
    (HERE / f"brief-{w}.md").write_text(txt); print(w, len(txt.split()))
