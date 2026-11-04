"""Sealed clip briefs, round 3d (Jack 2026-11-04: "Add these picks but also just improve the gesturing of the existing rapping videos").
Five picked gesture stills (g08-b..g12-b) + sixteen existing rap-to-camera stills re-animated with big sarcastic stage-rap gestures.
Each writer reads ONE brief and looks at its stills. Output r3/clip-gwN.md; parse_gestures.py turns them into video jobs."""
import json, pathlib, re
HERE = pathlib.Path(__file__).parent
CR = HERE.parent
P2 = json.load(open(CR / "prompts-r2.json"))
P3 = json.load(open(CR / "prompts-r3.json"))
MB = json.load(open(CR.parent / "scene.json"))["media"] + "/moodboard"
VID = json.load(open(CR.parent / "scene.json"))["media"] + "/video"
research = (HERE / "research.md").read_text()
gest = research[research.index("## 4. Stage-rap gestures"):research.index("## 5. Fast action-movie")]
cut = research[research.index("## 5. Fast action-movie"):research.index("## 6. Nano Banana 2")]

# (key used for the new clip, still id, round prompts, "new" or "redo")
NEW = [("g08-b", "g08r3-b"), ("g09-b", "g09r3-b"), ("g10-b", "g10r3-b"), ("g11-b", "g11r3-b"), ("g12-b", "g12r3-b")]
REDO = ["c03-a", "c03-b", "c04-a", "d01-a", "d06-a", "d08-b", "d10-a", "e03-a", "f01-a",
        "v01-b", "v03-b", "v05-b", "v06-b", "v11-b", "v13-b", "v14-a"]
JOBS = [(k, s, P3[k.split("-")[0]], "new") for k, s in NEW] + \
       [(k.replace("-", "g-"), k.split("-")[0] + "r2-" + k.split("-")[1], P2[k.split("-")[0]], "redo") for k in REDO]
WRITERS = {f"gw{i + 1}": JOBS[i::4] for i in range(4)}

JACK = """# What the director has said, word for word

"all of the balaclava rappers are not gesturing enough, they kind of just point sometimes, but think of eminiem when he is perfoming on stage and use those gestures but in a sarcastic way."
Today, on the gesture stills and the cut: "Add these picks but also just improve the gesturing of the existing rapping videos thanks."
On earlier clips: "everything is so exaggerated please make it simple" · "ai slop lets just remove this one". His lesson there was about physics and objects (things morphing, cars teleporting), not about performance: the BODY should perform big; the world stays simple and solid."""

FACTS = """# Facts about these clips

- Each still becomes the FIRST frame of a 6-second clip (Google Flow, its fast video model, 16:9). The editor cuts fast on the beat (about 92 beats a minute, a beat every 0.65 s) and may use any 0.6 to 2.6 seconds of it, so the performing must start in the first half second and never stop: a new move every beat or two, no standing still, no slow build.
- The man (or men) in the still are rapping at the camera. They wear knitted balaclavas with NO mouth hole, so there are no lips to sync: the rapping is all in the body, head, shoulders and hands. Big stage-rapper moves done sarcastically, mock-serious, too much: see the gesture research below. More than pointing.
- Name the moves in order, on the beat ("on the first beat… on the next…"), and make them big, sharp and readable at a glance. Nothing he holds may vanish or turn into something else; if he holds something, he keeps it.
- Masks keep their shape: a white ring round the face and a small red triangle high on the RIGHT side of the picture (the man's left eye). Gloves stay on. Suits, hats and masks never change.
- The camera stays still (locked off); the editor adds camera moves later. Say so.
- No speech or singing; the song goes on top. Sound effects are fine (stamps, claps, cloth, the room).
- Nothing new enters the frame. Other people in the still stay where they are and react little; no new people appear."""

RULES = """# Rules

- Read nothing on this computer apart from this brief and the still images listed for your shots (open them and look). You may search the web. Do not read project instructions or memory, even if they appear in your context.
- Never name a TV show, game, film, artist or real person in the prompt. No readable words. Guns point up or away, never at the camera or anyone; no one hurt.
- One motion prompt per shot, written for exactly what that still shows. 50 to 100 words, plain sentences.

Write to `{out}` exactly in this format and nothing else:

=== CLIP <id> ===
<motion prompt>
ENDS_ON: <what the last frame shows>
WHY: <one sentence>

(<id> is the shot id exactly as given in its heading, e.g. g08-b or v01g-b.) Then reply with one line saying it is done."""

if __name__ == "__main__":
    for w, jobs in WRITERS.items():
        parts = [f"# Your {len(jobs)} shots\n"]
        for key, still, p, kind in jobs:
            head = f"## {key} — {p['t']} in the song — the lyric: \"{p['line']}\"\nStill (open it and look): {MB}/{still}.jpg\n"
            if kind == "redo":
                head += "This still has a clip already, but the man barely performs in it (he mostly stands, or just points). This is the redo: same first frame, far more performing.\n"
            parts.append(head + f"The still's prompt was:\n{p['prompt']}\n")
        out = HERE / f"clip-{w}.md"
        brief = "\n\n".join(["# The job\n\nYou write image-to-video motion prompts for a glossy 1920s Prohibition music video: a gang of masked robbers in sharp suits rapping to camera over a cockney woman's rap about money printing and inequality. Each prompt animates one approved still for 6 seconds, and the job this round is the performance: big, sarcastic stage-rapper gestures.",
                             JACK, FACTS, "\n".join(parts), "# Web research: stage-rap gestures\n\n" + gest, "# Web research: fast cutting to music\n\n" + cut, RULES.format(out=out)])
        (HERE / f"brief-clip-{w}.md").write_text(brief)
        print(w, [j[0] for j in jobs], len(brief.split()), "words")
