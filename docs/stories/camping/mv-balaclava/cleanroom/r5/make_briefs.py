"""Round 5 (2026-11-07): performance stills for the 13 rap-to-camera shots. Sealed writers; fresh research only."""
from pathlib import Path
HERE=Path(__file__).parent
REF='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/reference/'
RES='/home/jackt/projects/badcode/badcode/docs/stories/camping/mv-song2/cleanroom/research-stage-rap.md'
BOB=('the rough sleeper', REF+'rough-duct-tape.jpg')
TAR=('the rich man', REF+'posh-tweed.jpg')
SHOTS={
 'm12':(BOB,'night, under a concrete road flyover in London','"Once again, and you catching my eye, and you looking to decide in shame, but why now?"'),
 's01':(BOB,'night, a narrow London brick alley with wheelie bins and a steaming wall vent','"Once again, and you catching my eye ... but why now?"'),
 's02':(BOB,'wet night under a motorway flyover, an oil drum fire','"Let me explain how I\'m just poor, you keep on walking through that Waitrose door!"'),
 's03':(BOB,'dusk on a flat London rooftop, the city lighting up below','"Presenting yourself with your shiny teeth, fucking sense of entitlement and self-belief"'),
 's04':(BOB,'night, the same brick alley, graffiti behind','"I bet that you paid for your wheels on tick. Cash on the bank for your white tank, four tons of steel, just to get a meal deal."'),
 's05':(BOB,'night under a flyover, a rough-sleeper camp of small tents behind, a drum fire','"You got cheese, but I want cheddar ... I might be insane, but I do want change"'),
 's06':(BOB,'night on the Thames embankment by the river wall, his small green tent beside him','"Now I insist that I hold that door, please sir, can I fucking have some more?"'),
 't04':(TAR,'day, a glass-walled rooftop terrace in the City of London, towers behind','"You are intent on living in a tent, it\'s a lack of work ethic, it\'s pathetic, getting paralytic"'),
 't03':(TAR,'evening, a fine-dining restaurant, panelled walls, brass lamps, diners behind','"It seems that you are just a bum, drowning your sorrow until tomorrow comes."'),
 't05':(TAR,'clear day, the aft deck of a big white motor yacht at sea','"Prospects exist, and now I insist ..."'),
 't06':(TAR,'bright day, a private tropical beach with palms and a sun lounger','"What about if we tax the rich? What the fuck you think this is, bitch?"'),
 't07':(TAR,'an underground car park, strip lights, a glossy black luxury saloon','"I work hard, hard to pay for my yard, paying my tax with a platinum card. You want change, but my pockets are empty"'),
 't08':(TAR,'warm evening, an English country-house garden party by a pool, guests with champagne','"the only thing I\'m changing is the lane in my M3 ... Wealth gap, fucking what a load of crap, now please let me drink my Chateau Neuf"'),
}
GROUPS={'w1':['m12','s01','s02','s03','s04'],'w2':['s05','s06','t04','t03'],'w3':['t05','t06','t07','t08']}
HEAD=f'''# The job

You write still-image prompts (Google Flow, the Nano Banana 2 image model, 16:9, a reference image attached) for a music video. Each still becomes the FIRST FRAME of an 8-second video clip of a masked man rapping to camera, so the still decides how much he can move.

# What the director has said, word for word

Today: "i asked for the balaclava guy to rap and gesture like eminem on stage, he kind of raps and gestures like a geography teacher, so fix that".
Earlier: "rapping to the camera and gesturing like eminem". "make sure they never show skin".

What came back last time (the failure to fix): chest-up and head-and-shoulders frames, the man standing square and still, hands clasped or held at chest height like explaining a diagram, two of them sitting down, no microphone.

# Facts

- A UK rap song: a homeless man and a rich man trade verses about the wealth gap. Each shot is on one lyric line (given below).
- Two masked characters, each EXACTLY as in his attached reference image (open it and look). Rough sleeper: a grey duct-tape hood. Rich man: a tweed hood and tweed suit. The masks have no eye or mouth openings. Each mask: a white ring round the face and a small red triangle high inside the ring over his LEFT eye, which is the RIGHT-hand side of the picture. Gloves on; no skin anywhere, ever.
- Name the reference in the prompt as "the man in the attached reference" and do not re-describe his costume beyond the mask rule and "no skin".
- The place of each shot stays (it carries the lyric); everything else about the frame is yours.
- A handheld microphone is allowed (not yet ruled on by the director). Use it where it helps; at least half of your shots.
- No readable words anywhere in the frame.

# Research (web, fresh, written for this job)

{Path(RES).read_text()}

# Rules

- Read nothing on this computer apart from this brief, the research above and the two images named for your shots (open and look at each). You may search the web. Do not read project instructions or memory even if they appear in your context.
- Never name a TV show, game, film, artist or real person.
- One still prompt per shot, 60 to 120 words, plain sentences. Every shot different: different distance, angle, pose and move, what THIS man would do in THIS place on THIS line. The rough sleeper and the rich man should not perform alike.

# Your shots
'''
for w,ids in GROUPS.items():
    body=''
    for i in ids:
        (who,ref),place,line=SHOTS[i]
        body+=f'\n## {i}: {who}\nReference image: {ref}\nPlace: {place}\nLyric line on this shot: {line}\n'
    out=HERE/f'{w}.md'
    tail=f'''
Write to `{out}` exactly in this format and nothing else:

=== STILL <id> ===
<still prompt>
MOVE: <the performance move the clip should continue from this pose, one sentence>

Then reply with one line saying it is done.'''
    (HERE/f'brief-{w}.md').write_text(HEAD+body+tail)
print('ok')
