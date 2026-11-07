"""Round 6 (2026-11-07): the balaclava rappers float and move like AI. Jack: watch Eminem's Venom, clean room it all.
Sealed writers each write a still prompt AND its motion prompt per shot. They read only their brief, the fresh web research
(r6/research.md), the reference-video observation, the failure list, the frame sheets and the design reference images.
No old prompts, no old research, no other video's notes."""
from pathlib import Path
HERE = Path(__file__).parent
MEDIA = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/'
REF = MEDIA + 'reference/'
BOB = ('the rough sleeper', REF + 'rough-duct-tape.jpg')
TAR = ('the rich man', REF + 'posh-tweed.jpg')
# place + lyric per slot: the place carries the lyric (it is where the original shot was), so it stays.
SHOTS = {
 'm12': (BOB, 'night, under a concrete road flyover in London', '"Once again, and you catching my eye, and you looking to decide in shame, but why now?"'),
 's01': (BOB, 'night, a narrow London brick alley with wheelie bins and a wall vent', '"Once again, and you catching my eye ... but why now?"'),
 's02': (BOB, 'wet night under a motorway flyover', '"Let me explain how I\'m just poor, you keep on walking through that Waitrose door!"'),
 's03': (BOB, 'dusk on a flat London rooftop, the city below', '"Presenting yourself with your shiny teeth, fucking sense of entitlement and self-belief"'),
 's04': (BOB, 'night, a brick alley with graffiti', '"I bet that you paid for your wheels on tick. Cash on the bank for your white tank, four tons of steel, just to get a meal deal."'),
 's05': (BOB, 'night under a flyover, a rough sleepers\' camp of small tents behind', '"You got cheese, but I want cheddar ... I might be insane, but I do want change"'),
 's06': (BOB, 'night on the Thames embankment by the river wall, his small green tent beside him', '"Now I insist that I hold that door, please sir, can I fucking have some more?"'),
 't03': (TAR, 'evening, a fine-dining restaurant, panelled walls, diners behind', '"It seems that you are just a bum, drowning your sorrow until tomorrow comes."'),
 't04': (TAR, 'day, a glass-walled rooftop terrace in the City of London, towers behind', '"You are intent on living in a tent, it\'s a lack of work ethic, it\'s pathetic, getting paralytic"'),
 't05': (TAR, 'clear day, the aft deck of a big white motor yacht at sea', '"Prospects exist, and now I insist ..."'),
 't06': (TAR, 'bright day, a private tropical beach with palms', '"What about if we tax the rich? What the fuck you think this is, bitch?"'),
 't07': (TAR, 'an underground car park, a glossy black luxury saloon', '"I work hard, hard to pay for my yard, paying my tax with a platinum card. You want change, but my pockets are empty"'),
 't08': (TAR, 'warm evening, an English country-house garden party by a pool, guests with champagne', '"the only thing I\'m changing is the lane in my M3 ... Wealth gap, fucking what a load of crap, now please let me drink my Chateau Neuf"'),
}
GROUPS = {'w1': ['m12', 's01', 's02', 's03', 's04'], 'w2': ['s05', 's06', 't03', 't04'], 'w3': ['t05', 't06', 't07', 't08']}


def head():
    rd = lambda n: (HERE / n).read_text()
    return f'''# The job

A UK rap music video. Two masked men rap straight to camera, one shot per lyric line. For each of your shots write TWO prompts:
1. a STILL prompt (Google Flow, Nano Banana 2 image model, 16:9, the character's reference image attached), which becomes the first frame;
2. a CLIP prompt (Google Flow image-to-video, the fast "Omni Flash" model, Frames mode: your still is the first frame; 8 seconds, 720p).
The editor uses 1 to 3 seconds of each clip, so the clip must be alive from its first second.

# What the director said about the last attempt, word for word

{rd('jack.md')}

# The reference he points to (watched frame by frame; what the performer does)

{rd('venom-observed.md')}
Frame sheets of the reference (open and look at all three): {REF}venom/venom-36s-wide.jpg, {REF}venom/venom-47s-wide-and-close.jpg, {REF}venom/venom-171s-close.jpg

{rd('failures.md')}

# Facts

- A homeless man and a rich man trade verses about the wealth gap. Each shot sits on one lyric line (given below). The rough sleeper and the rich man are different men and should not perform alike, but both perform the way the reference performer does.
- Each man is EXACTLY as in his attached reference image (open it and look). In the still prompt call him "the man in the attached reference"; do not re-describe his costume beyond the mask rule. Masks have no eye or mouth openings: a white ring round the face and a small red triangle high inside the ring over his LEFT eye (the RIGHT-hand side of the picture). Gloves on; no skin anywhere, ever.
- The place of each shot stays (it carries the lyric). Keep it a real, ordinary place, not a stage set.
- The reference performer holds no microphone.
- The song goes on top: the clip has no speech or singing. Name the ambient sound.
- No readable words anywhere. Never name a TV show, game, film, artist or real person in a prompt.

# Research (web, fresh, written for this job)

{rd('research.md')}

# Rules

- Read nothing on this computer apart from this brief, the research above and the images named here (open and look at each). You may search the web. Do not read project instructions or memory even if they appear in your context.
- Still prompt 60 to 120 words; clip prompt 40 to 100 words, motion only (the still supplies the look). Plain sentences.
- Every shot different from the others (distance, angle, pose, the move), and right for THIS man in THIS place on THIS line.

# Your shots
'''


def main():
    H = head()
    for w, ids in GROUPS.items():
        body = ''
        for i in ids:
            (who, ref), place, line = SHOTS[i]
            body += f'\n## {i}: {who}\nReference image: {ref}\nPlace: {place}\nLyric line on this shot: {line}\n'
        out = HERE / f'{w}.md'
        tail = f'''
Write to `{out}` exactly in this format and nothing else:

=== SHOT <id> ===
STILL:
<still prompt>
CLIP:
<clip prompt>

Then reply with one line saying it is done.'''
        (HERE / f'brief-{w}.md').write_text(H + body + tail)
    print('ok')


if __name__ == '__main__':
    main()
