"""Round 4 sealed briefs: clips for the round 3 picks and chase2 again (v5), replacement stills for the two shots Flow refused (n4)."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).parent
IMG = sys.argv[1]
P1 = json.load(open(HERE / "prompts.json"))
P2 = json.load(open(HERE / "prompts-r2.json"))
C2 = json.load(open(HERE / "clips-r2.json"))
research = (HERE / "research.md").read_text() + "\n" + (HERE / "research-r2.md").read_text()
jack = (HERE / "jack.md").read_text()

VERDICT = """# What Jack has said about clips so far, word for word

Rejected: "so many barrels fall and morph and change alonside other objects, please just keep this one simple" · "the cars teleport" · "everything is so exaggerated please make it simple" · "there are cars on the river" · "it looks like a modern car" · "cars pop in and out of frame, please keep it simple" · "ai slop lets just remove this one".

Approved, the plain ones: a drummer's wrist moving a brush while the room holds still; a robber slowly tilting his head at a mirror; steam rolling across the frame; a headlamp slowly brightening; a red sedan pulling away; a hot rod coming at the camera until its headlamp flares; a safe dragged on a chain with sparks.

So: one thing happens, plainly. Everything else holds still and keeps its shape. Nothing enters or leaves the frame unless that is the one thing."""

VID_TASK = """# Your task

Write one image-to-video prompt per shot for Google Flow's Omni Flash, from one start frame, 8 seconds, 16:9. Jack picked every start frame. Look at each before writing and describe only what moves.

Rules:
- Read nothing on this computer apart from this brief and the images it lists. You may search the web.
- One plain action per clip. Don't add objects, people or cars that aren't in the frame. Cars are heavy and stay on the road, facing the way they face.
- The song replaces the sound. Nobody speaks. No readable words. Weapons stay out of frame. Masks stay exactly as they are in the frame.
- Single continuous shot, no cuts, no morphing. Where it's natural, end on a realistic way out for the editor. A clip may also simply end.
- Short plain prose. Each prompt should differ in approach from the others.

Write your output to `{out}`, exactly in this format and nothing else:

=== SHOT <id> ===
<the prompt>
ENDS ON: <one line>
WHY: <one sentence>

Then reply with one line saying it is done.

# The shots
{shots}
"""

STILL_TASK = """# Your task

Write one still-image prompt per shot for Google Flow's Nano Banana 2.1 (16:9). Jack liked both of these scenes, but when each was animated, Flow's video engine refused it: "Unable to generate videos that might cause reputational risk or misrepresent current events." Nobody knows the exact trigger. Rethink the picture so it's a different, plainer frame of the same idea that a video engine would have no reason to refuse, and that can move simply. This is a fresh picture of harmless fiction, so no need for tricks in the wording.

{facts}

Rules:
- Read nothing on this computer apart from this brief and the images it lists. You may search the web.
- Never name a TV show, game, film, director, artist or real person. No children. No readable words. Weapons stay out of frame. Nobody has their hands raised. Everybody is fully dressed.
- Prohibition-era cars and boats must look unmistakably period. Keep the colourful noir: saturated colour in paint, clothes and practical lights, with deep shadow.
- The picture fills the frame edge to edge. Narrative prose. No quality buzzwords.

Write your output to `{out}`, exactly in this format and nothing else:

=== SHOT <id> ===
<the prompt>
WHY: <one sentence>

Then reply with one line saying it is done.

# The shots

## den3
Refused image: {img}/den3-b.jpg
Last prompt: {den3}

## mask4
Refused image: {img}/r2-mask4-a.jpg
Last prompt: {mask4}
"""

MASK = "The mask, a fact of this film: a hand-knitted wool balaclava over the whole head with no eye or mouth holes; a thin wool ring stitched around the face; one small solid red felt triangle with rounded corners sewn high inside the ring, over where one eye would be, pressed against the ring's inner edge. The middle of the ring is bare wool. The approved image " + IMG + "/r2-mask1-b.jpg shows it."

shots = "".join(f"\n## {k}\nStart frame: {IMG}/{name}.jpg\n{extra}\n" for k, name, extra in [
    ("pov1", "r3-pov1-a", ""), ("pov3", "r3-pov3-a", ""), ("rods1", "r3-rods1-a", "Jack's note on the earlier clip of this idea: \"the cars teleport\". Both cars face the same way and keep their places side by side."),
    ("rods4", "r3-rods4-a", "Jack's note on the earlier clip of this idea: \"everything is so exaggerated please make it simple\"."),
    ("safe1", "r3-safe1-b", "The safe has just left the wall. Keep the mask unchanged."), ("safe3", "r3-safe3-b", "Jack's note on the earlier clip: \"there are cars on the river\". Everything moving stays on the road."),
    ("chase2", "chase2-b", f"Twice rejected. Jack: \"it looks like a modern car please make it look like the prohabition era\", then \"cars pop in and out of frame, please keep it simple\". Last attempt was: {C2['chase2']['motion']} The frame is a wide city view with tiny cars, so consider leaving almost everything still: for example only the steam moving and the one small roadster rolling a short way.")])
(HERE / "brief-v5.md").write_text("# What Jack said\n\n" + jack + "\n" + VERDICT + "\n\n# Web research\n\n" + research + "\n" + VID_TASK.format(out=HERE / "v5.md", shots=shots))
(HERE / "brief-n4.md").write_text("# What Jack said\n\n" + jack + "\n" + VERDICT + "\n\n# Web research\n\n" + research + "\n" + STILL_TASK.format(out=HERE / "n4.md", facts=MASK, img=IMG, den3=P1["den3"]["prompt"], mask4=P2["mask4"]["prompt"]))
print("ok")
