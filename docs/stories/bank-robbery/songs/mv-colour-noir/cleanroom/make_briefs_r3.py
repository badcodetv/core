"""Round 3 sealed briefs, on Jack's clip and still notes: new reference stills (n1..n3) and clips for his approved stills (c1, c2)."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).parent
IMG = sys.argv[1]
P1 = json.load(open(HERE / "prompts.json"))
P2 = json.load(open(HERE / "prompts-r2.json"))
C = json.load(open(HERE / "clips.json"))
research = (HERE / "research.md").read_text() + "\n" + (HERE / "research-r2.md").read_text()
jack = (HERE / "jack.md").read_text()

VERDICT = """# What Jack said about the first clips, word for word

Rejected:
- "looks like ai slop, so many barrels fall and morph and change alonside other objects, please just keep this one simple."
- "ai slop please change it, the refernce image is the problem"
- "ai slop the cars teleport, maybe make the refence image where the cars are facing the same directiion"
- "ai slop everything is so exaggerated please make it simple"
- "ai slop there are cars on the river fix it"
- "it looks like a modern car please make it look like the prohabition era"
- "ai slop lets just remove this one" (bottles sliding off a tipping bar shelf and dropping through a hatch)

Approved, for scale: a red sedan pulling away under an elevated railway with sparks falling, then a pillar crossing the lens; a teal sedan and a police motorcycle on river ice; a view from a stopped car of a policeman and a theatre crowd, ending on a whip pan; a view back over a seat as a crimson sheet falls on the lens; a racing road seen from a water tower; a hot rod on a city street coming at the camera until its headlamp flares; a safe dragged on a chain with sparks.

What the rejected ones share: too many moving objects, things that change shape, cars that jump or point the wrong way, and everything turned up too high. So: one thing happens, it happens plainly, and everything else stays still."""

STILL_TASK = """# Your task

Write one still-image prompt per shot below for Google Flow's Nano Banana 2.1 (16:9). Each still will be the start frame of an 8-second video, and Jack judged the last one by how it moved, so build a frame that can move simply: few moving objects, cars already pointing the way they'll travel, nothing piled up or balanced that would have to change shape.

Rules:
- Read nothing on this computer apart from this brief and the images it lists. You may search the web.
- Prohibition-era cars must be unmistakably period: tall upright bodies, separate mudguards, running boards, spoked wheels, upright windscreens.
- Never name a TV show, game, film, director, artist or real person. No children. No readable words anywhere. Weapons stay out of frame.
- The picture fills the frame edge to edge. Narrative prose. No quality buzzwords. Keep the colourful noir: saturated colour in paint, clothes and practical lights, with deep shadow, not everything turned up.

Write your output to `{out}`, exactly in this format and nothing else:

=== SHOT <id> ===
<the prompt>
WHY: <one sentence>

Then reply with one line saying it is done.

# The shots
{shots}
"""

CLIP_TASK = """# Your task

Write one image-to-video prompt per shot for Google Flow's Omni Flash, from one start frame, 8 seconds, 16:9. Jack picked every start frame. Look at each before writing and describe only what moves.

Rules:
- Read nothing on this computer apart from this brief and the images it lists. You may search the web.
- Be simple and restrained. One plain action per clip; everything else holds still and keeps its shape. Don't add objects, people or cars that aren't in the frame.
- The song replaces the sound. Nobody sings or speaks: mouths stay closed, and musicians can play with small natural movement. No readable words. Weapons stay out of frame. Faces and masks stay exactly as they are in the frame.
- Single continuous shot, no cuts, no morphing. Where it's natural, end on a realistic way out for the editor, like something passing the lens or a small whip pan. A clip may also simply end.
- Short plain prose. Each prompt should differ in approach from the others in your batch.

Write your output to `{out}`, exactly in this format and nothing else:

=== SHOT <id> ===
<the prompt>
ENDS ON: <one line>
WHY: <one sentence>

Then reply with one line saying it is done.

# The shots
{shots}
"""

MASK = "The mask, a fact of this film: a hand-knitted wool balaclava over the whole head with no eye or mouth holes; a thin wool ring stitched around the face; one small solid red felt triangle with rounded corners sewn high inside the ring, over where one eye would be."


def still(key, note, prompt, images):
    return f"\n## {key}\nJack's note: {note}\nImages of what he saw: {', '.join(f'{IMG}/{i}.jpg' for i in images)}\nLast prompt: {prompt}\n"


STILLS = {
    "n1": [("pov1", '"looks like ai slop, so many barrels fall and morph and change alonside other objects, please just keep this one simple." A new start frame: the driver\'s-eye view from behind the wheel of a 1930s car at night (oxblood leather gloves, a mustard check cuff, a period dashboard), on an open road ahead with nothing falling. Keep it simple.', P1["pov1"]["prompt"], ["pov1-b"]),
           ("pov3", '"ai slop please change it, the refernce image is the problem". A new idea for a driver\'s-eye shot, same gloves and cuff, keeping it believable and grounded, with no jumping car.', P1["pov3"]["prompt"], ["pov3-b"])],
    "n2": [("rods1", '"ai slop the cars teleport, maybe make the refence image where the cars are facing the same directiion". Old-school hot rods racing on a dry lake: every vehicle faces the same way, travelling the same way.', P1["rods1"]["prompt"], ["rods1-b"]),
           ("rods4", '"ai slop everything is so exaggerated please make it simple". Old-school hot rods at dusk in a concrete flood channel: calm, believable, no car up a wall, no big wings of spray.', P1["rods4"]["prompt"], ["rods4-b"])],
    "n3": [("safe3", '"ai slop there are cars on the river fix it". The car dragging a thread of sparks, seen from far above: the road and the water must be clearly separate, and everything that moves stays on a road. A view where no road crosses water is safest.', P1["safe3"]["prompt"], ["safe3-a"]),
           ("safe1", f'"the logo is in the wrong place on the balaclava otherwise its perfect". Keep the whole scene exactly. Fix only the mask: {MASK} The approved image r2-mask1-b shows where the logo sits. The face must be turned far enough toward the camera to show it.', P2["safe1"]["prompt"], ["r2-safe1-a", "r2-safe1-b", "r2-mask1-b"])],
}
for name, shots in STILLS.items():
    (HERE / f"brief-{name}.md").write_text("# What Jack said\n\n" + jack + "\n" + VERDICT + "\n\n# Web research\n\n" + research + "\n" + STILL_TASK.format(out=HERE / f"{name}.md", shots="".join(still(*s) for s in shots)))

BAND_FRAMES = {"den1": "b", "den4": "b", "bridge1": "a", "bridge2": "a", "bridge3": "b", "bridge4": "a"}
MASK_FRAMES = {"mask1": "b", "mask3": "b", "mask4": "a", "safe4": "b"}
c1 = "".join(f"\n## {k}\nStart frame: {IMG}/r2-{k}-{x}.jpg\n" for k, x in BAND_FRAMES.items())
c2 = "".join(f"\n## {k}\nStart frame: {IMG}/r2-{k}-{x}.jpg\n" for k, x in MASK_FRAMES.items())
c2 += f"\n## chase2\nStart frame: {IMG}/chase2-b.jpg\nJack's note on the last clip of this frame: \"it looks like a modern car please make it look like the prohabition era\". The tiny yellow car is a 1920s roadster with separate mudguards, running boards and spoked wheels and must stay exactly that. It was asked last time to: \"{C['chase2']['motion']}\"\n"
for name, shots in {"c1": c1, "c2": c2}.items():
    (HERE / f"brief-{name}.md").write_text("# What Jack said\n\n" + jack + "\n" + VERDICT + "\n\n# Web research\n\n" + research + "\n" + CLIP_TASK.format(out=HERE / f"{name}.md", shots=shots))
print("ok")
