"""Sealed clip briefs (round 2 stills → 6 s Omni Flash clips). Each writer reads ONE brief and looks at its stills."""
import json, pathlib, sys
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from shots import FAMILIES

P = json.load(open(HERE / "prompts-r2.json"))
MB = json.load(open(HERE.parent / "scene.json"))["media"] + "/moodboard"
research = (HERE / "research-clips.md").read_text()

JACK = """# What the director has said about clips, word for word

On earlier clips for this same video: "so many barrels fall and morph and change alonside other objects, please just keep this one simple" · "the cars teleport" · "everything is so exaggerated please make it simple" · "there are cars on the river" · "it looks like a modern car" · "cars pop in and out of frame, please keep it simple" · "ai slop lets just remove this one". His lesson: one plain action per clip, nothing morphs, no exaggeration.

For this video, word for word: "we want those people rapping throughout the whole thing, as in a bunch of different badcode balaclava gang members robbing banks and rapping to the camera and gesturing like eminem. i also want the lyrics to match whats happeing on screen, like grandma freezing should show exactly that." And on the stills: "i like all of them, make videos out of them"."""

FACTS = """# Facts about these clips

- Each still becomes the FIRST frame of a 6-second clip (Google Flow, its fast video model, 16:9). The editor will use 2 to 4 seconds of it, cut to the song, so the action must read from the first second.
- The masked men have no mouth: their rapping is hands, head and shoulders, bobbing on the beat (about 92 beats a minute, a steady head-nod groove). Hands do the words: pointing into the lens, chopping the beat, counting on fingers, fist to chest, leaning in.
- The masks must keep their shape: a knitted balaclava with a large white ring round the face and a small red triangle high on the right side of the picture. Gloves stay on. Nothing about a mask changes during the clip.
- The camera stays still in the clip; the editor adds camera moves later. Say so.
- No speech or singing in the clip audio; the song goes on top. Sound effects are fine.
- Every car is a 1920s car and stays the same car. Nothing new enters the frame; nothing leaves and comes back."""

RULES = """# Rules

- Read nothing on this computer apart from this brief and the still images listed for your shots (open them and look). You may search the web. Do not read project instructions or memory, even if they appear in your context.
- Never name a TV show, game, film, artist or real person. No readable words. Guns point up or away, never at the camera or anyone; no one hurt.
- One motion prompt per shot; it is used on both takes (a and b), so write for what both share. 40 to 90 words, plain sentences.

Write to `{out}` exactly in this format and nothing else:

=== CLIP <id> ===
<motion prompt>
ENDS_ON: <what the last frame shows>
WHY: <one sentence>

Then reply with one line saying it is done."""


def main():
    for w, (theme, shots) in FAMILIES.items():
        parts = [f"# Your four shots (theme: {theme})\n"]
        for sid, t, line, pic, rap in shots:
            parts.append(f"## {sid} — at {t} in the song — the lyric: \"{line}\"{'  — RAP shot' if rap else ''}\n"
                         f"Stills (look at both): {MB}/{sid}r2-a.jpg and {MB}/{sid}r2-b.jpg\n"
                         f"The still's prompt was:\n{P[sid]['prompt']}\n")
        out = HERE / f"clip-{w}.md"
        brief = "\n\n".join([
            "# The job\n\nYou write image-to-video motion prompts for a stylised 1920s Prohibition music video: a gang of masked robbers rob banks and rap to the camera over a song about money printing and inequality. Each prompt animates one approved still for 6 seconds.",
            JACK, FACTS, "\n".join(parts), "# Web research\n\n" + research, RULES.format(out=out)])
        (HERE / f"brief-clip-{w}.md").write_text(brief)
        print(w, len(brief.split()))


if __name__ == "__main__":
    main()
