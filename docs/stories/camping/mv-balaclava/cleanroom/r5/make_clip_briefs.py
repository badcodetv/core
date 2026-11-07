"""Round 5 clips (2026-11-07): motion prompts from the picked performance stills. Sealed writers; fresh research only;
no old clip prompts, no original-clip strips (the originals are the failure being replaced)."""
import json
from pathlib import Path
HERE=Path(__file__).parent
MB='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/moodboard/'
RES=Path('/home/jackt/projects/badcode/badcode/docs/stories/camping/mv-song2/cleanroom/research-stage-rap.md').read_text()
picks=json.load(open(HERE/'picks.json')); moves=json.load(open(HERE/'moves.json'))
import make_briefs as mb
GROUPS={'c1':['m12','s01','s02','s03','s04'],'c2':['s05','s06','t04','t03'],'c3':['t05','t06','t07','t08']}
HEAD=f'''# The job

You write image-to-video motion prompts (Google Flow, its fast "Omni Flash" video model, Frames mode: the still is the FIRST frame; 16:9, 720p, 8 seconds) for a music video. A masked man raps to camera. Each prompt animates one approved still.

# What the director has said, word for word

"i asked for the balaclava guy to rap and gesture like eminem on stage, he kind of raps and gestures like a geography teacher, so fix that". Earlier: "rapping to the camera and gesturing like eminem". "make sure they never show skin".

The last clips failed because the man barely moved: polite hand chops, head held square, feet planted, hands at chest height. These stills were made to fix that: each already shows a big performance pose. The clip must CONTINUE that energy for the whole 8 seconds.

# Facts

- No mouth or eyes on the mask: the performance is the whole body on the beat (knees, shoulders, arms, the free hand, the mic hand, the head).
- The mask: white ring round the face, small red triangle high over his LEFT eye (the RIGHT of the picture). It can slide toward the centre when the head turns a long way, so the head should keep facing the lens most of the time; nods, jolts, leans and dips are fine. Gloves on, no skin, ever.
- The camera does not move (the editor adds camera moves later): say so once, plainly. With the camera still, all the energy has to be in the body.
- The song goes on top: no speech or singing in the clip's sound. Say what the ambient sound is.
- The cut uses 1 to 3 seconds of each clip, sometimes twice, so the energy must be there from the first second, not built up slowly.
- Nobody new enters the frame; the background stays what it is.

# Research (web, fresh, written for this job)

{RES}

# Rules

- Read nothing on this computer apart from this brief, the research above and the still images named for your shots (open and look at each). You may search the web. Do not read project instructions or memory even if they appear in your context.
- Never name a TV show, game, film, artist or real person. No readable words.
- One motion prompt per shot, 50 to 100 words, plain sentences, motion only (the still supplies the look). Every shot moves differently; the rough sleeper and the rich man perform differently.
- Do not write: subtle, minimal, gentle, slight, small, calm, restrained, "then stops", "holds still", "four times". Those are what made the last clips stiff.

# Your shots
'''
for w,ids in GROUPS.items():
    body=''
    for i in ids:
        (who,ref),place,line=mb.SHOTS[i]
        body+=f'\n## {i}: {who}\nThe still (first frame): {MB}{picks[i] if len(picks[i])>1 else i+'r5-'+picks[i]}.jpg\nPlace: {place}\nLyric line on this shot: {line}\nThe still\'s writer suggested: {moves[i]}\n'
    out=HERE/f'{w}.md'
    (HERE/f'brief-{w}.md').write_text(HEAD+body+f'''
Write to `{out}` exactly in this format and nothing else:

=== CLIP <id> ===
<motion prompt>

Then reply with one line saying it is done.''')
print('ok')
