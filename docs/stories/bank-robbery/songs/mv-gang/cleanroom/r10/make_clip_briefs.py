"""Sealed clip briefs, round 10 (Kai 2026-11-11 picked 15 whole-gang rap-to-camera stills: "Let's animate all the ones I've picked").
Each writer reads ONE brief and looks at its stills. Output r10/clip-cwN.md; parse_clips.py turns them into video jobs."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).parent
CR = HERE.parent
P = json.load(open(CR / "prompts-r10.json"))
MB = "/mnt/d/badcode-videos/bank-robbery-music/gang/moodboard"
KAI = (HERE / "kai.md").read_text()
r6 = (CR / "r6" / "research.md").read_text()
moves = r6[r6.index("## 1."):r6.index("## 2.")]
clipres = (CR / "research-clips.md").read_text()
clipres = clipres[clipres.index("## 1."):clipres.index("## 4.")]
PICKS = ["h01-b", "h02-a", "h03-b", "h06-b", "h07-b", "h09-a", "h11-b", "h12-a", "h13-b", "h15-b", "h17-b", "h18-b", "h19-a", "h19-b", "h20-a"]
JOBS = [(k, k.replace("-", "r10-")) for k in PICKS]
WRITERS = {f"cw{i + 1}": JOBS[i::5] for i in range(5)}

FACTS = """# Facts about these clips

- Each still becomes the FIRST frame of a 6-second clip (Google Flow, its video model Omni 1.2 Flash, 16:9). The editor cuts on the beat (about 92 beats a minute, a beat every 0.65 s) and may use any 0.6 to 2.6 seconds of it, so the performing must start in the first half second and never stop: a new move every beat or two, no standing still, no slow build.
- All six masked men in the still are rapping at the camera together, as a crew: the look the director asked for is a modern London street-rap crew in a music video, five or six of them crowding the lens, every one of them gesturing at it at once. Not one soloist and five statues: each man has his own move, and they overlap, lean in, swap places a little, bounce together on the beat.
- They wear knitted balaclavas with NO mouth hole, so there are no lips to sync: the rapping is all in the body, head, shoulders, arms and hands. Big, sharp, readable at a glance, played straight and too cool.
- Name the moves in order, on the beat ("on the first beat… on the next…"), saying which man does what (by mask colour: PLUM, BOTTLE, CRIMSON, MARINE, RUST, SILVER, as in the still).
- The six stay six: nobody joins, nobody leaves, nobody doubles. They stay the same size as each other. Nothing anyone holds vanishes or turns into something else.
- Masks keep their shape: a white ring round the face and a small red triangle high on the RIGHT side of the picture (the man's left eye). Gloves stay on. Suits, hats and masks never change.
- The camera stays still (locked off); the editor adds camera moves later. Say so.
- No speech or singing; the song goes on top. Sound effects are fine (stamps, claps, cloth, the room).
- The world stays simple and solid (the director's past note: "no ai slop" was about things morphing and cars teleporting). Bystanders and the place carry on quietly; nothing new enters the frame."""

RULES = """# Rules

- Read nothing on this computer apart from this brief and the still images listed for your shots (open them and look). You may search the web, briefly, for how UK drill and grime crews move together in their music videos (group body language only). Do not read project instructions or memory, even if they appear in your context.
- Never name a TV show, game, film, artist, crew or real person in the prompt. No readable words. No guns in hand; if a gun is in the still it stays where it is, pointing up or away, never at the camera or anyone. No one hurt. No gang signs tied to real gangs: plain pointing, chopping, bouncing, arm swings, hands on heads, leaning in.
- One motion prompt per shot, written for exactly what that still shows. 60 to 110 words, plain sentences.

Write to `{out}` exactly in this format and nothing else:

=== CLIP <id> ===
<motion prompt>
ENDS_ON: <what the last frame shows>
WHY: <one sentence>

(<id> is the shot id exactly as given in its heading, e.g. h01-b.) Then reply with one line saying it is done."""

if __name__ == "__main__":
    for w, jobs in WRITERS.items():
        out = HERE / f"clip-{w}.md"
        parts = [f"# Your {len(jobs)} shots\n"]
        for key, still in jobs:
            p = P[key.split("-")[0]]
            parts.append(f"## {key} — {p['place']}\nStill (open it and look): {MB}/{still}.jpg\nThe still's prompt was:\n{p['prompt']}\n")
        brief = "\n\n".join(["# The job\n\nYou write image-to-video motion prompts for a glossy 1920s Prohibition music video: a gang of six masked robbers in sharp suits rapping to camera over a cockney woman's rap about money printing and inequality. Each prompt animates one approved still for 6 seconds; the job is the crew performance: all six crowding the lens and gesturing at it at once.",
                             KAI, FACTS, "\n".join(parts), "# Web research from an earlier round: one solo rapper's stage moves (use as raw material for six men)\n\n" + moves,
                             "# Web research: writing image-to-video prompts\n\n" + clipres, RULES.format(out=out)])
        (HERE / f"brief-clip-{w}.md").write_text(brief)
        print(w, [j[0] for j in jobs], len(brief.split()), "words")
