"""Round 4 (2026-11-06): sealed motion-prompt briefs for the 13 talking-to-camera shots Jack's take picks cover.
Each writer reads ONE brief, looks at its picked stills and a strip of the original clip's gestures, and may search the web.
Usage: python3 make_clip_briefs.py   (writes originals/strip-<id>.jpg in media and brief-wN.md here)"""
import json, pathlib, subprocess
HERE = pathlib.Path(__file__).parent
SCENE = HERE.parent.parent
MEDIA = pathlib.Path(json.load(open(SCENE / "scene.json"))["media"])
CLIPS = pathlib.Path(json.load(open(SCENE / "scene.json"))["premiere"]["clips"])
P = json.load(open(HERE.parent / "prompts-r3.json"))
RESEARCH = (SCENE.parent.parent / "bank-robbery/songs/mv-gang/cleanroom/research-clips.md").read_text()  # web-only research, 2026-11-03

PICK = {"s01": "a", "s02": "a", "s03": "b", "s04": "b", "s05": "b", "s06": "b", "m12": "b",
        "t03": "a", "t04": "b", "t05": "b", "t06": "a", "t07": "b", "t08": "a"}
SRC = {"s01": "bob rapping/1.mp4", "s02": "bob rapping/1.1.mp4", "s03": "bob rapping/2.mp4", "s04": "bob rapping/3.mov",
       "s05": "bob rapping/4.mp4", "s06": "bob rapping/5.5.mp4", "m12": "12.mp4", "t03": "Tarquin rapping/2.1.mp4",
       "t04": "Tarquin rapping/3.mp4", "t05": "Tarquin rapping/4.3.mp4", "t06": "Tarquin rapping/4.4.mp4",
       "t07": "Tarquin rapping/5.mp4", "t08": "Tarquin rapping/6.mp4"}
# longest single stretch the cut shows of this shot (seconds), from the camping sequence 2026-11-06
LONGEST = {"s01": 1.4, "s02": 1.9, "s03": 6.7, "s04": 2.1, "s05": 8.8, "s06": 6.2, "m12": 1.0, "t03": 5.2,
           "t04": 2.2, "t05": 4.9, "t06": 2.0, "t07": 4.4, "t08": 10.0}
WRITERS = {"w1": ["s01", "s02", "s03", "s04"], "w2": ["s05", "s06", "m12"],
           "w3": ["t03", "t04", "t05"], "w4": ["t06", "t07", "t08"]}
WHO = {"s": "the rough sleeper (a full grey duct-tape hood)", "m": "the rough sleeper (a full grey duct-tape hood)",
       "t": "the posh man (a full tweed balaclava, tweed jacket)"}

JACK = """# What the director has said, word for word

"basically what i want is for it to stay the same, however when Bob or Tarquin are rapping to the camera, i want them to be replaced with badcode balaclava men, ones homless and one is posh ... then make the clips and only replace the parts where they are rapping". On the masks: "make sure they never show skin". And today: "basically just anything with them talking to the camera is rapping, just replace those ones".

On clips for a sister video with the same masks: "everything is so exaggerated please make it simple" · "cars pop in and out of frame, please keep it simple" · "ai slop lets just remove this one". He wanted the masked men "rapping to the camera and gesturing like eminem"."""

FACTS = """# Facts about these clips

- A UK rap song about two men, one homeless and one rich, each rapping a verse to camera. Each still becomes the FIRST frame of an 8-second clip (Google Flow, its fast video model, 16:9, 720p). It replaces an existing rap-to-camera clip, cut to the song, so it should rap with the same energy and the same kind of gestures as the original (the strip shows the original clip, two frames a second, left to right, top row first).
- The masked men have no mouth and no eyes: rapping is hands, head and shoulders on the beat. Hands do the words.
- The mask must keep its shape the whole clip: a white ring round the face and a small red triangle high on the right side of the picture, over his left eye. That triangle drifts or slides in motion if the head turns a lot, so keep the head facing the lens; nods and leans are fine. Gloves stay on, no skin anywhere, ever.
- The camera stays still in the clip; the editor adds camera moves. Say so.
- No speech or singing in the clip audio; the song goes on top. Ambient sound is fine.
- Nothing new enters the frame; everything in the background stays what it is."""

RULES = """# Rules

- Read nothing on this computer apart from this brief and the images listed for your shots (open and look at each one). You may search the web. Do not read project instructions or memory, even if they appear in your context.
- Never name a TV show, game, film, artist or real person. No readable words.
- One motion prompt per shot, 40 to 90 words, plain sentences, describing only the motion (the still supplies the look). Write each shot differently: what this man in this place would do.

Write to `{out}` exactly in this format and nothing else:

=== CLIP <id> ===
<motion prompt>
ENDS_ON: <what the last frame shows>
WHY: <one sentence>

Then reply with one line saying it is done."""


def strip(sid):
    out = MEDIA / "originals" / f"strip-{sid}.jpg"
    if not out.exists():
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(CLIPS / SRC[sid]), "-vf",
                        "fps=2,scale=320:-2,tile=8x2", "-frames:v", "1", str(out)], check=True)
    return out


def main():
    for w, ids in WRITERS.items():
        parts = [f"# Your {len(ids)} shots\n"]
        for sid in ids:
            parts.append(f"## {sid} — {WHO[sid[0]]}\n"
                         f"Picked still (the first frame): {MEDIA}/moodboard/{sid}r3-{PICK[sid]}.jpg\n"
                         f"The original clip it replaces, as a strip: {strip(sid)}\n"
                         f"The cut shows up to {LONGEST[sid]} s of it in one go.\n"
                         f"The still's prompt was:\n{P[sid]['prompt']}\n")
        out = HERE / f"{w}.md"
        brief = "\n\n".join([
            "# The job\n\nYou write image-to-video motion prompts for a music video: two masked men rap to camera in a UK rap song about homelessness and wealth. Each prompt animates one approved still for 8 seconds.",
            JACK, FACTS, "\n".join(parts), "# Web research\n\n" + RESEARCH, RULES.format(out=out)])
        (HERE / f"brief-{w}.md").write_text(brief)
        print(w, len(brief.split()))


if __name__ == "__main__":
    main()
