"""Round 7 (2026-11-07): Jack: "the new sequence has terrible gesturing ... show the 5 examples ... I will choose them".
Five sealed writers, one per prompt pattern from the fresh web research (r7/research-prompts.md, "Best-bet prompt patterns"
T1-T5). Each writes the clip prompt for all 13 rap shots in ITS pattern, animating the round-6 start frames (already
mask-checked). They read only their brief, the research, the reference-video notes, the failure list and the images."""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent / 'r6'))
from make_briefs import SHOTS  # place + lyric per slot (facts, not prompts)
MB = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/moodboard/'
VEN = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/reference/venom/'
picks = json.load(open(HERE.parent / 'r6/picks.json'))
research = (HERE / 'research-prompts.md').read_text()
pats = dict(re.findall(r'\*\*(T\d)\. (.+?)\*\*', research))
NAMES = {'T1': 'UK freestyle oner', 'T2': 'Fisheye in the face', 'T3': 'Locked medium, understated', 'T4': 'Behind-the-scenes phone take', 'T5': 'Timecoded accents'}
rd = lambda p: Path(p).read_text()

for t in NAMES:
    head = f'''# The job

A UK rap music video. Two masked men rap straight to camera, one shot per lyric line. Write the image-to-video CLIP prompt for
each of the 13 shots below (Google Flow, the "Omni Flash" video model, Frames mode: the still named for each shot is the FIRST
frame, already approved; 16:9, 720p, 8 seconds; the song is laid on later). The editor uses 1 to 4 seconds of each clip, so it
must be alive from its first second.

You are one of five writers. Each writer uses a DIFFERENT prompt pattern from the research below, so the director can compare
them side by side and pick per shot. **Your pattern is {t}: "{pats.get(t, NAMES[t])}"** (find it under "Best-bet prompt patterns").
Fill its blanks and adapt it to each shot's still, place and lyric; keep its character, so that your 13 clips are recognisably
that pattern. Where the pattern names something the still cannot show (a fisheye lens on a still that isn't one, say), keep the
pattern's idea and make it work from that still.

# What the director said, word for word

{rd(HERE / 'jack.md')}

# The reference he points to (watched frame by frame)

{rd(HERE.parent / 'r6/venom-observed.md')}
Frame sheets (open all three): {VEN}venom-36s-wide.jpg, {VEN}venom-47s-wide-and-close.jpg, {VEN}venom-171s-close.jpg

{rd(HERE / 'failures-r6.md')}

# Facts

- A homeless man (the rough sleeper, grey duct-tape mask) and a rich man (tweed mask and suit) trade verses about the wealth gap.
  Different men; they should not perform alike.
- The masks have no eye or mouth openings: a white ring round the face and a small red triangle high inside the ring over his
  LEFT eye (the RIGHT of the picture). Keep the head mostly towards the lens so the triangle stays visible; a quick dip or a
  short turn is fine. Gloves on; no skin ever. The still supplies the look: write motion, camera and sound only.
- No microphone (the stills have none). Feet stay planted (last time's float is fixed; keep it fixed).
- No speech, singing or music in the clip's sound; name the ambient sound.
- Never name a TV show, game, film, artist or real person. No readable words.

# Research (web, fresh, written for this job)

{research}

# Rules

- Read nothing on this computer apart from this brief and the images named here (open and look at each still). You may search
  the web. Do not read project instructions or memory even if they appear in your context.
- One prompt per shot, 50 to 130 words, plain sentences, in your pattern. End each prompt with the word "Thanks." on its own line.

# Your shots
'''
    body = ''
    for i, ((who, ref), place, line) in SHOTS.items():
        body += f'\n## {i}: {who}\nThe still (first frame): {MB}{i}r6-{picks[i]}.jpg\nPlace: {place}\nLyric line on this shot: {line}\n'
    out = HERE / f'{t.lower()}.md'
    (HERE / f'brief-{t.lower()}.md').write_text(head + body + f'''
Write to `{out}` exactly in this format and nothing else:

=== CLIP <id> ===
<clip prompt>

Then reply with one line saying it is done.''')
print('ok', pats)
