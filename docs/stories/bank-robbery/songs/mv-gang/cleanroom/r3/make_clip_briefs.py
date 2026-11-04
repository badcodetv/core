"""Sealed clip briefs for round 3: Jack's 13 picked action stills -> 6 s Omni Flash clips. Each writer reads ONE brief and looks at its stills."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).parent
CR = HERE.parent
P = json.load(open(CR / "prompts-r3.json"))
MB = json.load(open(CR.parent / "scene.json"))["media"] + "/moodboard"
research = (CR / "research-clips.md").read_text()
research3 = (HERE / "research.md").read_text()
PICKS = {"cw1": ["k01-a", "k02-b", "k03-a", "k04-a", "k06-b"],
         "cw2": ["k07-a", "k09-a", "k10-a", "k11-a"],
         "cw3": ["k12-a", "k13-b", "k14-a", "k16-a"]}
PICKS2 = {"cw4": ["k14-a", "k18-a", "k19-a", "k21-a", "k22-b"],
          "cw5": ["k23-a", "k24-a", "k26-a", "k27-b"],
          "cw6": ["k29-a", "k30-a", "k31-b", "k36-b"]}
if sys.argv[1:] == ["2"]:
    PICKS = PICKS2

JACK = """# What the director has said, word for word

On earlier clips for this same video: "so many barrels fall and morph and change alonside other objects, please just keep this one simple" · "the cars teleport" · "everything is so exaggerated please make it simple" · "there are cars on the river" · "it looks like a modern car" · "cars pop in and out of frame, please keep it simple" · "ai slop lets just remove this one". His lesson: one plain action per clip, nothing morphs, no exaggeration of the physics.

Now: "there needs to be action movie scenes, as if they are parodied but with the badcode balaclava men" · "the cuts should be timed to the beat and way more fast paced than it is, think action movie" · on these stills: "clean room the ones i liked and make the videos"."""

FACTS = """# Facts about these clips

- Each still becomes the FIRST frame of a 6-second clip (Google Flow, its fast video model, 16:9). The editor will cut fast, using 0.6 to 2.6 seconds of it on the beat (about 92 beats a minute), so the big action must start in the first second and keep going; there is no slow build.
- These are action-movie set pieces played too cool, as parody. The joke is in the still; the clip carries the one big move through (the dive continues, the truck keeps coming, the walk keeps walking). Slow motion is fine where the set piece is a slow-motion cliché; say so plainly.
- The masks keep their shape: a knitted balaclava with a large white ring round the face and a small red triangle high on the RIGHT side of the picture (the man's left eye). Gloves stay on. Nothing about a mask, suit or car changes during the clip.
- The camera stays still (locked off); the editor adds camera moves later. Say so.
- No speech or singing; the song goes on top. Sound effects are fine.
- Every car is a 1920s car and stays the same car. Nothing new enters the frame; nothing leaves and comes back. No new people appear."""

RULES = """# Rules

- Read nothing on this computer apart from this brief and the still images listed for your shots (open them and look). You may search the web. Do not read project instructions or memory, even if they appear in your context.
- Never name a TV show, game, film, artist or real person. No readable words. Guns point up or away, never at the camera or anyone; no one hurt.
- One motion prompt per shot, written for exactly what that still shows. 40 to 90 words, plain sentences.

Write to `{out}` exactly in this format and nothing else:

=== CLIP <id> ===
<motion prompt>
ENDS_ON: <what the last frame shows>
WHY: <one sentence>

(<id> is the shot id with its take, e.g. k01-a.) Then reply with one line saying it is done."""

for w, keys in PICKS.items():
    parts = [f"# Your {len(keys)} shots\n"]
    for key in keys:
        sid, t = key.split("-")
        p = P[sid]
        if PICKS is PICKS2 and key == "k14-a":
            parts.append("NOTE for k14-a: an earlier motion prompt for this still came back with NOTHING from the video model four times (a silent refusal or failure). Write a simpler, calmer one: fewer flying objects, no glass shattering near anyone, nothing that could read as harm.\n")
        parts.append(f"## {key} — {p['t']} in the song — the lyric: \"{p['line']}\"\nStill (open it and look): {MB}/{sid}r3-{t}.jpg\nThe still's prompt was:\n{p['prompt']}\n")
    out = HERE / f"clip-{w}.md"
    brief = "\n\n".join(["# The job\n\nYou write image-to-video motion prompts for a glossy 1920s Prohibition music video: a gang of masked robbers in sharp suits rob banks in parodied action-movie set pieces, over a rap about money printing and inequality. Each prompt animates one approved still for 6 seconds.",
                         JACK, FACTS, "\n".join(parts), "# Web research on clips\n\n" + research, "# Web research on action parody and fast cutting\n\n" + research3, RULES.format(out=out)])
    (HERE / f"brief-clip-{w}.md").write_text(brief)
    print(w, len(brief.split()))
