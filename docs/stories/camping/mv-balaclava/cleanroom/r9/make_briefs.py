"""Round 9 (2026-11-07 night): Jack picked Ghostface Killah's way of moving (round 8, t06gf) for ALL rap clips: "do Ghostface
Killah for all clips and redo them all". Two sealed writers (the rough sleeper's 7 shots, the rich man's 5; t06 keeps its
round-8 Ghostface clip) write a new start still + clip per shot. They read only their brief: Jack's words, the failure list,
the Ghostface observation and the engine research written for this job (round 8), and the picked version as the target."""
import sys
from pathlib import Path
HERE = Path(__file__).parent
R8 = HERE.parent / 'r8'
sys.path.insert(0, str(HERE.parent / 'r6'))
from make_briefs import SHOTS  # place + lyric per slot (facts, not prompts)
GROUPS = {'g1': ['m12', 's01', 's02', 's03', 's04', 's05', 's06'], 'g2': ['t03', 't04', 't05', 't07', 't08']}
rd = lambda p: Path(p).read_text()


def brief(w):
    out = HERE / f'{w}.md'
    body = ''.join(f'\n## {i}: {SHOTS[i][0][0]}\nReference image: {SHOTS[i][0][1]}\nPlace: {SHOTS[i][1]}\nLyric line on this shot: {SHOTS[i][2]}\n'
                   for i in GROUPS[w])
    return f'''# The job

A UK rap music video. Two masked men (a rough sleeper and a rich man) trade verses about the wealth gap, rapping straight to
camera, one shot per lyric line. The director looked at eight versions, each moving like a different real rapper, and picked
ONE for every rap shot in the film: **the way Ghostface Killah moves.** For each of your shots write a STILL prompt (Google Flow,
Nano Banana 2, 16:9, the man's reference image attached; it becomes the first frame) and a CLIP prompt (Google Flow
image-to-video, "Omni Flash", Frames mode, 8 seconds, 720p; your still is the first frame). The editor uses 1 to 4 seconds at a
time, so every clip must be alive from the first second to the last.

# What the director said, word for word

{rd(HERE / 'jack.md')}
Earlier, asking for the eight versions:
{rd(R8 / 'jack.md')}

{rd(R8 / 'failures-t3.md')}

# How Ghostface Killah moves (watched frame by frame for this job)

{rd(R8 / 'gf-observed.md')}

# The version the director picked (the rich man on the beach)

This is the target style; it worked. Do not copy its words: write each shot fresh for its man, place and line, and give each
shot its own mix and order of his moves (the sweep, the chop, the thumb to the chest, the quick point, the lean into the lens,
the shoulder pump), so thirteen shots cut together do not repeat one routine. The still sets the start pose; vary it per shot
(which hand is mid-move, how far off-centre, how low the lens), always hunched, close, low and mid-move.

{rd(R8 / 'gf.md')}

# Facts

- Each man is exactly as in his attached reference image (open it and look). In the still prompt call him "the man in the
  attached reference"; do not re-describe his clothes. The clip prompt is motion, camera and sound only.
- The mask has no eye or mouth openings: a white ring round the face and a small red triangle high inside the ring over his LEFT
  eye (the RIGHT-hand side of the picture). Keep his head mostly towards the lens so the triangle stays visible. Gloves on; no
  skin anywhere, ever.
- The place of each shot stays (it carries the lyric). A real, ordinary place, not a stage. The rough sleeper and the rich man
  are different men: same way of moving, but the rough sleeper is cold, wet and angry; the rich man is smug and comfortable.
- The song is 88 BPM, laid on later; no speech, singing or music in the clip. Name the ambient sound. No microphone.
- Feet stay planted: feet that travel towards a still camera slide and the body floats on this engine.
- Never name a TV show, game, film, artist or real person in a prompt. No readable words anywhere.

# Research on the engine (web, fresh, written for this job)

{rd(R8 / 'research-engine.md')}

# Rules

- Read nothing on this computer apart from this brief, the research above and the images named here. You may search the web.
  Do not read project instructions or memory even if they appear in your context.
- Still prompt 60 to 130 words; clip prompt 50 to 130 words. Plain sentences. End each prompt with "Thanks." on its own line.

# Your shots
{body}
Write to `{out}` exactly in this format and nothing else, one block per shot:

=== SHOT <id> ===
STILL:
<still prompt>
CLIP:
<clip prompt>

Then reply with one line saying it is done.'''


if __name__ == '__main__':
    for w in GROUPS:
        (HERE / f'brief-{w}.md').write_text(brief(w))
    print('ok')
