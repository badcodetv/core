"""Round 2 sealed briefs: stills fixes (s1..s4, Jack's notes) and clips for the clean picks (v1..v4)."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).parent
IMG = sys.argv[1]  # folder holding <shot>-<take>.jpg
P = json.load(open(HERE / "prompts.json"))
PICKS = {f.name.split("__")[0]: (lambda d: d.get("data", d))(json.load(open(f))) for f in (HERE.parent / "feedback/moodboard-r1/picks").glob("*.json")}
research = (HERE / "research-r2.md").read_text()
research1 = (HERE / "research.md").read_text()
jack = (HERE / "jack.md").read_text()

BAND = """The band (the same people wherever they appear): five musicians in sharp 1930s gangster clothes: a very tall thin man on upright bass, a stout older man on trumpet, a young man on clarinet, a grey-haired woman on a small drum kit, and fronting them at a period microphone, the singer: a broad man in his forties with black hair going silver at one temple, a broken nose and heavy eyebrows. Jack: "it needs to be a male singer, since the song itself is a man singing." Any wide-open singing mouth gets refused by the engine, so his mouth is closed or he is mid-breath."""

MASK = """The masks are BadCode's own, from its show. Facts: the whole head is in a hand-knitted wool balaclava with no eye holes and no mouth hole, so no skin and no eyes show; collars up and gloves on, so no skin shows anywhere on a robber. The logo is the face: one thin ring stitched in wool around the face, and high inside that ring, over where one eye would be, one small solid red felt triangle with rounded corners, sewn on, pushed up near the ring's edge and well away from the centre. In the show it is cream wool, a black ring and red felt. The two faults so far: the triangle drifts to the centre, and it sometimes comes back as an outline instead of solid. Nobody could wear a logo on the forehead: that was the mistake in the last round.

Jack on this round: "it needs to be like the actaul badcode balaclavas with the logo over the eye, but i like the different coloured ones keep that" and "make it look like it fits the time and have different coloured ones". So every robber's balaclava is a different period wool dye, the ring in a colour that reads against it, and everything hand-made and 1920s, using the research below."""

STILL_TASK = """# Your task

Rewrite these still-image prompts for Google Flow's Nano Banana 2.1 (16:9), one each. Jack liked each scene: keep its place, vantage, light and colours, and make only the change he asked for, written properly into the picture. The last round's prompt and an image are shown so you can keep what worked, and you are free to reword all of it.

{facts}

Rules:
- Read nothing on this computer apart from this brief and the images it lists. You may search the web.
- Never name a TV show, game, film, director, artist or real person. No children. No readable words: don't write a colour name right beside the word for a sign, because the engine printed "RUBY RED" on a sign last round. Weapons stay out of frame.
- The picture fills the frame edge to edge. Narrative prose. No quality buzzwords.

Write your output to `{out}`, exactly in this format and nothing else:

=== SHOT <id> ===
<the prompt>
WHY: <one sentence>

Then reply with one line saying it is done.

# The shots
{shots}
"""

VID_TASK = """# Your task

Write one image-to-video prompt per shot for Google Flow's Omni Flash, from one start frame, 8 seconds, 16:9. Each start frame is a still Jack picked, so keep the place, people and light. Describe what moves and what the camera does.

What Jack wants, in his words, is at the top of this brief. Fast, real, heavy cars; realistic transitions rather than trippy ones.

Rules:
- Read nothing on this computer apart from this brief and the images it lists. You may search the web. Look at every start frame before writing.
- The song replaces the clip's sound, so nobody speaks or sings. Physical sound is optional.
- One clear action, single continuous shot, no scene cuts, no morphing. Cars move like heavy machines and don't teleport. No readable words. Weapons stay out of frame.
- End each clip on a realistic way out for the editor, starting from the suggestion given. Your own is fine if better.
- Plain prose, as short as does the job. No quality buzzwords. Each prompt must be different in approach from the others in your batch.

Write your output to `{out}`, exactly in this format and nothing else:

=== SHOT <id> ===
<the prompt>
ENDS ON: <one line>
WHY: <one sentence>

Then reply with one line saying it is done.

# The shots
{shots}
"""


def shot_text(key, note=""):
    pick = PICKS.get(key, {}).get("pick", "")
    imgs = [f"{IMG}/{key}-{pick}.jpg"] if pick else [f"{IMG}/{key}-a.jpg", f"{IMG}/{key}-b.jpg"]
    n = PICKS.get(key, {}).get("note", "").strip() or note
    return f"\n## {key}\nImage(s): {', '.join(imgs)}\nJack's note: {n or '(none)'}\nLast round's prompt: {P[key]['prompt']}\n"


STILLS = {"s1": (["den1", "den4", "bridge1"], BAND), "s2": (["bridge2", "bridge3", "bridge4"], BAND),
          "s3": (["mask1", "mask3", "mask4"], MASK), "s4": (["safe1", "safe4"], MASK)}
for name, (keys, facts) in STILLS.items():
    (HERE / f"brief-{name}.md").write_text("# What Jack said\n\n" + jack + "\n# Web research on the engine\n\n" + research1 + "\n# Web research for this round\n\n" + research + "\n" +
        STILL_TASK.format(facts=facts, out=HERE / f"{name}.md", shots="".join(shot_text(k) for k in keys)))

CLIPS = {"v1": ["chase1", "chase2", "chase3", "chase4"], "v2": ["pov1", "pov2", "pov3", "pov4"],
         "v3": ["rods1", "rods2", "rods3", "rods4"], "v4": ["den2", "den3", "city1", "safe2", "safe3"]}
for name, keys in CLIPS.items():
    shots = "".join(f"\n## {k}\nStart frame: {IMG}/{k}-{PICKS[k]['pick']}.jpg\nSuggested way out: {P[k]['way_out']}\n" for k in keys)
    (HERE / f"brief-{name}.md").write_text("# What Jack said\n\n" + jack + "\n# Web research\n\n" + research + "\n" + VID_TASK.format(out=HERE / f"{name}.md", shots=shots))
print("ok")
