#!/usr/bin/env python3
"""Money For Something, storyboard v3 (the side branch): one Omni prompt file per NEW clip, and clips-v3.tsv for run-clips-v3.sh.
Plates ending in f (s02bf, s03af, s03b2f, s03cf, s06af) are frame 0 of a round 11 clip made from that plate: on 5 Oct the
Start-frame picker could no longer find the round 10 uploads by name (FRAME_SOURCE_NOT_FOUND), and nothing larger than a 512 px thumbnail could be pulled back out of Flow.
Same rules as build-prompts.py. The v2 kit (build-prompts.py, clips.tsv, run-clips.sh) is not touched.
Storyboard and plates: docs/stories/magic-money-tree/money-for-something-storyboard-v3.md, rounds 12 and 13."""
import os
H=os.path.dirname(os.path.abspath(__file__))
HEAD="A locked-off shot from the same early-2000s television studio recording. "
# 5 Oct: the plain HEAD was refused four times on the politician's Russia line ("reputational risk or misrepresent current events"); this one passed first time.
# 5 Oct, second change: with "comedy sketch" in it, 7 of 11 politician clips came back with a laugh track (one machine listener). "Period drama" asks for none.
HEAD_POL="A locked-off shot from a scripted television period drama set in the year 1916, filmed on a closed set with no audience: an actor in period costume plays a made-up government minister of that time. "
NOTES=" The banknotes on the tree are old British pound notes and they hang still."
TALK=" Nobody else is in the studio and nobody reacts. Audio: only his voice, close and dry, and the faint hum of the empty room. No music."
QUIET=" Audio: only the faint hum of an empty studio. No music and no voices."
HOST,BS,GS,POL="The Host","The British Soldier","The German Soldier","The Politician"
B="The man breathes, blinks and "
# (name, plate, character or '', notes visible, body, kind)  kind: 1 speaking, 0 silent in the room, 2 own head and sound line
C=[
# Round 1
('v3-r1-01-politician-russia','v301',POL,0,B+"speaks across the table with his open hand raised. He says: We are lucky to have Russia as an ally. I'm sure it will be a fruitful relationship. He lowers his hand and takes a satisfied sip of wine.",1),
('v3-r1-02-british-drift','v302','',0,"The man breathes slowly. His eyes lose their focus and stop moving, and he does not blink. The mug sinks an inch and stops. The steam keeps rising.",0),
('v3-r1-03-trench','v303','',0,"A locked-off shot on old colour film. The four soldiers stand and wait with their backs to the camera; their breath clouds in the cold air and one of them shifts his weight. The hand on the ladder rung tightens. The nearest soldier slowly raises the whistle to his mouth and stops just before it touches his lips. The water on the trench floor trembles. Audio: wind, a few distant birds, wet cloth moving. No music and no voices.",2),
('v3-r1-04-host-snap','v304',HOST,1,"The man snaps his fingers twice, sharply, at someone just out of frame to the right. He says: Oi. Who paid for it? He holds his arm out and waits with his eyebrows up.",1),
# The Price Is War
('v3-p-01-host-rules','v305',HOST,1,B+"speaks straight to the lens, swinging the luggage tag on its string. He says: I show you a thing. You tell me if we can afford it. He raises one eyebrow.",1),
('v3-p-02-host-world-war','v305',HOST,1,B+"holds the luggage tag out towards the lens and speaks straight to the lens. He says: A world war. He keeps the tag held out and waits. The tag stays blank.",1),
('v3-p-03-british-no','s03b2f',BS,0,B+"speaks to someone on the left of the frame without moving his head. He says: No. He looks down at his mug.",1),
('v3-p-04-german-no','s03cf',GS,0,B+"speaks flatly to someone on the left of the frame without unfolding his arms. He says: No. He gives one small shake of the head.",1),
('v3-p-05-politician-capitalism','v301',POL,0,B+"speaks across the table with his open hand raised, in no hurry. He says: Capitalism is new. The kinks had to be worked out. But we have finally nailed it. He gives one small pleased nod.",1),
('v3-p-06-host-drinks','s02bf','',1,"The man says nothing. He breathes, blinks once, looks straight into the lens for a long moment, then takes a slow drink of wine without looking away.",0),
# Round 2, the first argument
('v3-a1-01-british-reads','v307',BS,1,B+"reads aloud from the card, slowly, one finger moving under the words. The sleeves of his tunic are plain khaki cloth. He says: To make Britain a fit country for heroes to live in. He lowers the card, looks at someone out of frame to the right and says: Go on, then.",1),
('v3-a1-02-british-shells','v306',BS,1,"The man breathes hard and jabs his finger down on the table once as he speaks to the man in front of him. He says: You found it for the shells. He stays leaning forward.",1),
('v3-a1-03-politician-different','s06af',POL,1,B+"speaks to someone on the left of the frame, both arms still round the bucket. He says: That was different. He lifts his chin.",1),
('v3-a1-04-british-how','v306',BS,1,"The man breathes hard, blinks and speaks to the man in front of him without moving his finger from the table. He says: How? He waits, staring.",1),
('v3-a1-05-politician-war','s06af',POL,1,B+"speaks to someone on the left of the frame as if explaining something obvious. He says: It was a war. He gives a small shrug with his eyebrows.",1),
('v3-a1-06-british-in-it','v306',BS,1,"The man breathes, blinks and speaks quietly to the man in front of him. He says: I know. I was in it. He slowly sits back in his armchair.",1),
('v3-a1-07-host-card','s02bf',HOST,1,B+"speaks straight to the lens, tipping his head towards the right of the frame. He says: He was. It's on his card. He takes a small sip.",1),
('v3-a1-08-politician-as-i-was-saying','s06af',POL,1,B+"speaks to someone on the left of the frame, calm, both arms round the bucket. He says: As I was saying. No money. He pats the side of the bucket once.",1),
('v3-a1-09-host-spoken-for-what','s02bf',HOST,1,B+"leans forward and speaks to someone just to the right of the lens. He says: Spoken for by what? He waits with his eyebrows up.",1),
('v3-a1-10-politician-middle-east','s06af',POL,1,B+"speaks to someone on the left of the frame, pleased with himself. He says: Peace in the Middle East. They'll be fine. They've all that oil. He gives one small nod.",1),
# Quote, Unquote
('v3-q-01-german-marx','s03cf',GS,0,B+"speaks to someone on the left of the frame without unfolding his arms. He says: Marx. He waits.",1),
('v3-q-02-british-sergeant','s03b2f',BS,0,B+"speaks to someone on the left of the frame. He says: My sergeant. He takes a sip of tea.",1),
('v3-q-03-host-keynes','s03af',HOST,1,B+"reads from the card in his hand, then looks up to the right of the frame. He says: Keynes. Probably. Nobody can find where he said it. He turns the card over, looks at its blank back and shrugs.",1),
('v3-q-04-politician-psst','v308',POL,0,"A locked-off shot from a scripted television period drama set in the year 1916, filmed on a closed set with no audience: two actors in period costume, one playing a made-up government minister and one playing a soldier. The two men breathe and blink at different times. The man on the right leans closer to the man on the left and whispers behind his raised hand. He whispers: Psst. Communist. The man on the left does not move or look at him; he blinks once, slowly. Nobody else is in the studio and nobody reacts. Audio: only the whisper, close and dry, and the faint hum of the empty room. No music.",2),
# Quick-fire, the second argument
('v3-z-01-german-zeppelins','v309',GS,0,B+"speaks brightly to someone out of frame to the right, his finger still raised. He says: We should print more money. To buy more zeppelins. He nods, pleased with the idea, and lowers his finger.",1),
('v3-z-02-politician-irresponsible','v301',POL,0,B+"draws his head back and speaks across the table, shocked. He says: Now that's irresponsible. He shakes his head once.",1),
('v3-z-03-german-you-shook','s03cf',GS,0,B+"turns his eyes to the right of the frame and speaks flatly without unfolding his arms. He says: You shook the tree. He keeps looking to the right.",1),
('v3-z-04-politician-responsibly','v301',POL,0,B+"lays his raised hand flat on his own chest and speaks across the table. He says: I shook it responsibly. He keeps his hand on his chest and lifts his chin.",1),
# Advert two
('v3-ad-01-rope','v310','',0,"A locked-off shot from a cheap early-2000s television advert, recorded on video. Light rain falls through the floodlight and onto the red carpet. The velvet rope sways a little. The people in the queue shuffle, breathe out clouds in the cold and one of them stamps his feet; none of them turns round. The floodlight flickers once. Nobody steps onto the carpet. Audio: rain on tarmac and the hum of the floodlight. No music and no voices.",2),
('v3-ad-02-yacht','v311',''  ,0,"A locked-off shot from a cheap early-2000s television advert, recorded on video. The yacht moves very slightly on its mooring and the gangway creaks. The reflections of its cabin lights break and re-form on the black water. The velvet rope sways a little. Nobody is there. Audio: water lapping against the quay and a rope tapping on the mast. No music and no voices.",2),
# Sound Off
('v3-s-01-politician-house-prices','v301',POL,0,B+"speaks across the table, warm and sure, his open hand turning in the air. He says: At least they'll have learnt what to do when times get tough. Say, if house prices surged for some reason. He smiles with his mouth closed.",1),
('v3-s-02-politician-crypto','v301',POL,0,B+"speaks across the table with his open hand raised, light and confident. He says: Hopefully crypto billionaires don't finance fascists in the future. That would be as crazy as another war. Glad humanity has learnt that lesson. He raises his wine glass an inch.",1),
]
os.makedirs(H+'/video-prompts',exist_ok=True); rows=[]
for name,plate,ch,notes,body,kind in C:
    if kind==2: p=body
    else: p=(HEAD_POL if ch==POL else HEAD)+body+(NOTES if notes else '')+(TALK if kind else QUIET)
    open(f'{H}/video-prompts/{name}.txt','w').write(p+'\n'); rows.append(f'{name}\t{plate}\t{ch}')
open(H+'/clips-v3.tsv','w').write('\n'.join(rows)+'\n'); print(len(rows),'clips')
