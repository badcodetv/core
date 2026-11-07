"""Round 8 (2026-11-07): Jack: "fix the gestures, it still looks strange and boring and ai slop like ... gesture like action
bronson, eminem, rza, wu tang, kendrick lamar, 50 cent, and so on, make like 8 versions". Clean room.

Eight sealed writers, one per reference rapper. Each researches HIS rapper on the web, watches footage frame by frame, writes
what the body does, then writes a new START STILL (the start frame pins the gesture: round 7 finding) and its CLIP prompt.
Four on the rough sleeper (s02, under the flyover), four on the rich man (t06, the beach), so the versions compare like for like.
They read only their brief, the fresh engine research (research-engine.md), Jack's words, the failure list and the images.
No old prompts, no old research, no other video's notes."""
from pathlib import Path
HERE = Path(__file__).parent
MEDIA = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/'
SCRATCH = '/tmp/claude-1000/-home-jackt-projects-badcode-badcode/6fe85c99-0289-4181-bfe7-88d026f24930/scratchpad/r8/ref/'
BOB = ('the rough sleeper (grey duct-tape mask)', MEDIA + 'reference/rough-duct-tape.jpg', 'at night under a wet concrete motorway flyover in London',
       '"Let me explain how I\'m just poor, you keep on walking through that Waitrose door!"', 's02')
TAR = ('the rich man (tweed mask and tweed suit)', MEDIA + 'reference/posh-tweed.jpg', 'on a bright day on a private tropical beach with palms',
       '"What about if we tax the rich? What the fuck you think this is, bitch?"', 't06')
WRITERS = {  # key: (rapper as Jack asked, man)
    'em': ('Eminem', BOB), 'fc': ('50 Cent', BOB), 'mm': ('Method Man (Wu-Tang Clan)', BOB), 'kl': ('Kendrick Lamar', BOB),
    'ab': ('Action Bronson', TAR), 'rz': ('RZA (Wu-Tang Clan)', TAR), 'gf': ('Ghostface Killah (Wu-Tang Clan)', TAR),
    'rr': ('Rick Ross', TAR),
}


def brief(key):
    rapper, (who, ref, place, line, slot) = WRITERS[key]
    rd = lambda n: (HERE / n).read_text()
    out = HERE / f'{key}.md'
    return f'''# The job

A UK rap music video. Two masked men trade verses about the wealth gap, rapping straight to camera. The director says the
rapping gestures look "strange and boring and ai slop like" and wants to see eight versions, each moving like a different real
rapper, so he can pick one style for the whole video. **You are one of eight writers. Your rapper is {rapper}.** The others
are other rappers; you never see their work. Make yours unmistakably {rapper}'s way of moving, translated onto this man.

You write TWO prompts for one shot:
1. a STILL prompt (Google Flow, Nano Banana 2 image model, 16:9; the man's reference image is attached to it), which becomes the
   first frame. The still sets the pose the clip starts from, and the clip mostly continues that pose, so catch him mid-move in
   your rapper's stance and framing, not at rest.
2. a CLIP prompt (Google Flow image-to-video, the "Omni Flash" model, Frames mode: your still is the first frame; 8 seconds,
   720p, 16:9). The editor uses 1 to 4 seconds at a time, so it must be alive from the first second to the last.

# Step 1: watch your rapper (do this before writing anything)

Search the web for how {rapper} performs to camera: music videos where he raps into the lens, live performances, interviews or
articles about his stage presence. Pick one or two music videos where he raps to camera and look at them frame by frame:
`yt-dlp` and `ffmpeg` are installed. Download only short sections (e.g. `yt-dlp -f "bv*[height<=480]" --download-sections
"*0:40-1:00" -o <file> <url>`), make frame sheets (`ffmpeg -i <file> -vf "fps=4,scale=320:-1,tile=4x4" <sheet>.jpg`) and open
them. Work only inside `{SCRATCH}{key}/` (create it). These are private reference, never published.
Write what his body actually does into `{HERE}/{key}-observed.md` (max 40 lines): stance, where the weight is, framing and camera
distance he favours, what each hand does and how big the moves are, head and shoulders on the beat, how a gesture starts and
stops, what he never does, the video(s) and timestamps you watched.

# What the director said, word for word

{rd('jack.md')}

{rd('failures-t3.md')}

# Facts

- Your man: **{who}**. Reference image: {ref} (open it and look). In the still prompt call him "the man in the attached
  reference"; do not re-describe his clothes. In the clip prompt write motion, camera and sound only (the still supplies the look).
- The mask has no eye or mouth openings: a white ring round the face and a small red triangle high inside the ring over his LEFT
  eye (the RIGHT-hand side of the picture). Keep his head mostly towards the lens so the triangle stays visible; a dip or a short
  turn is fine. Gloves on; no skin anywhere, ever.
- The place: {place}. Keep it a real, ordinary place, not a stage. The lyric on this shot: {line}
- The song is 88 BPM, laid on later; the clip has no speech, singing or music. Name the ambient sound.
- A microphone is your choice (only if your rapper would hold one in a to-camera music video).
- On our past clips: feet that travel towards a still camera slide and the body floats; that is the one thing to avoid.
- Never name a TV show, game, film, artist or real person in a prompt (Flow blocks it): describe the movement instead.
  No readable words anywhere.

# Research on the engine (web, fresh, written for this job)

{rd('research-engine.md')}

# Rules

- Read nothing on this computer apart from this brief, the research above and the images named here. You may search the web and
  use yt-dlp/ffmpeg in your scratch folder. Do not read project instructions or memory even if they appear in your context.
- Still prompt 60 to 130 words; clip prompt 50 to 130 words. Plain sentences. End each prompt with "Thanks." on its own line.

Write to `{out}` exactly in this format and nothing else:

=== {slot}{key} ({rapper}) ===
STILL:
<still prompt>
CLIP:
<clip prompt>

Then reply with one line saying it is done.'''


if __name__ == '__main__':
    for k in WRITERS:
        (HERE / f'brief-{k}.md').write_text(brief(k))
    print('briefs:', ', '.join(WRITERS))
