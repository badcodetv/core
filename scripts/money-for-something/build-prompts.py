#!/usr/bin/env python3
"""Money For Something: write one Omni prompt file per clip from the list below, and clips.tsv for run-clips.sh.
Rules (docs/google-flow/omni-flash.md): motion only, camera locked, breathing and blinking written in, one small
action, the line after a colon with no quotation marks, the notes named as pounds, the sound named."""
import os
H=os.path.dirname(os.path.abspath(__file__))
HEAD="A locked-off shot from the same early-2000s television studio recording. "
NOTES=" The banknotes on the tree are old British pound notes and they hang still."
TALK=" Nobody else is in the studio and nobody reacts. Audio: only his voice, close and dry, and the faint hum of the empty room. No music."
QUIET=" Audio: only the faint hum of an empty studio. No music and no voices."
HOST,BS,GS,POL="The Host","The British Soldier","The German Soldier","The Politician"
# (name, plate, character or '', notes visible, body, speaking)
C=[
('s02-00-wide','roomv2','',1,"The four men shift in their armchairs, breathe and blink at different times. The standing man lowers his arm and sits down slowly.",0),
('s02-01-host-title','s02b',HOST,1,"The man breathes, blinks, tips his wine glass towards the lens and speaks straight to the lens. He says: Money For Something. The quiz where the rules depend on who's asking. He raises one eyebrow and takes a small sip.",1),
('s03-01-host-card-british','s03a',HOST,1,"The man breathes, blinks and reads aloud from the card in his hand. He says: From Barnsley, a coal miner, killed at the Somme aged nineteen. He lifts his eyes from the card to someone on the right of the frame and holds the look.",1),
('s03-02-british-silent','s03b2','',0,"The man breathes slowly and blinks once. His eyes stay fixed on the same point and his jaw tightens a little. His thumb moves once on the mug.",0),
('s03-03-host-card-german','s03a',HOST,1,"The man breathes, blinks and reads aloud from the card in his hand. He says: From Essen, a coal miner, killed two hundred yards away. He lowers the card a little and looks to the right of the frame.",1),
('s03-04-german-silent','s03c','',0,"The man breathes and blinks. His eyes stay on the man beside him for a moment, then come back to the front. His arms stay folded.",0),
('s03-05-host-card-politician','s03a',HOST,1,"The man breathes, blinks and reads aloud from the card in his hand. He says: And from Westminster. He stops, looks up to the right of the frame, and says: Still with us. He takes a sip of wine.",1),
('s03-06-politician-silent','s03d2','',0,"The man breathes, blinks and gives one small slow nod with his chin up. Two fingers tap his watch chain once.",0),
('s04-01-host-round-one','s02b',HOST,1,"The man breathes, blinks and speaks to someone just to the right of the lens. He says: Round one. How did it start? He waits with his eyebrows up.",1),
('s04-02-british-duke','s03b2',BS,0,"The man breathes, blinks, frowns a little and speaks to someone on the left of the frame. He says: A duke got shot. I think. He looks down at his mug.",1),
('s04-03-german-bosnia','s03c',GS,0,"The man breathes, blinks and speaks flatly to someone on the left of the frame without unfolding his arms. He says: In Bosnia. By a Serb. So we invaded Belgium. He gives a very small shrug.",1),
('s04-04-british-france','s03b2',BS,0,"The man breathes, blinks and speaks to someone on the left of the frame. He says: And that's why I was in France. He takes a sip of tea.",1),
('s04-05-host-who-paid','s02b',HOST,1,"The man breathes, blinks and speaks to someone just to the right of the lens. He says: Lovely. And who paid for it? He waits with his eyebrows up, then slowly lowers his wine glass.",1),
('s04-06-host-lives','s02b',HOST,1,"The man breathes and blinks. He waits a moment in silence, then speaks quietly to someone just to the right of the lens. He says: Other than with your lives. His face goes still.",1),
('s04-07-stare','s04a','',1,"The two men do not move. They breathe slowly and blink at different times, and their eyes stay fixed on the lens. One slow drop of tea falls from the tipped mug.",0),
('s04-08-politician-watch','s03d2','',0,"The man breathes and blinks, looks down at his watch chain, turns it between his fingers and keeps looking at it.",0),
('s05-01-host-afford','s02b',HOST,1,"The man breathes, blinks and speaks to someone just to the right of the lens. He says: A war. Can we afford it? He lifts his glass a little, waiting.",1),
('s05-02-politician-shake','s05a',POL,1,"The man shakes the thin tree hard with one hand, twice. The banknotes come off the twigs and drop out of the bottom of the frame. He looks back at the table and says: Yes. He lets go of the trunk.",1),
('s06-01-host-homes','s02b',HOST,1,"The man breathes, blinks and speaks to someone just to the right of the lens. He says: And the ones who came back. The homes? He waits with his eyebrows up.",1),
('s06-02-politician-no-money','s06a',POL,1,"The man breathes, blinks and tightens both arms round the bucket on his lap. He speaks to someone on the left of the frame. He says: Ah. No money. He gives a small apologetic tilt of the head.",1),
('s06-03-british-some-on-it','s03b2',BS,0,"The man breathes, blinks and turns his eyes to the right of the frame. He says: There's some on it. He keeps looking to the right.",1),
('s06-04-politician-spoken-for','s06a',POL,1,"The man breathes, blinks and glances up at the banknotes beside his head, then back to someone on the left of the frame. He says: Those are spoken for. He pats the side of the bucket once.",1),
('s07-01-host-quickfire','s07a',HOST,1,"The man breathes, blinks and speaks straight to the lens, swinging his open hand. He says: Quick-fire. Shake, Starve or Plant. The wine moves in his glass.",1),
('s07-02-host-rules','s07a',HOST,1,"The man breathes, blinks and speaks quickly straight to the lens, counting on the fingers of his open hand. He says: Shake. Print it and build nothing. Starve. Spend nothing. Plant. Build something.",1),
('s07-03-german-wheelbarrows','s03c',GS,0,"The man breathes, closes his eyes for a moment and lets his head drop back a little. He says: Oh god. Wheelbarrows again. He opens his eyes and looks at the ceiling.",1),
('s08-01-plant','s08a','',1,"The hand presses the folded banknote down until it is almost buried, pats the soil flat twice and slowly draws back out of the frame. A few crumbs of soil roll down the inside of the bucket.",0),
('s09-01-host-dubs','s02b',HOST,1,"The man breathes, blinks and looks past the lens as if watching a screen. He says: Shake. He waits, sips his wine and says: Starve. He waits again and says: Shake again.",1),
('s09-02-politician-catches','s05a','',1,"The man shakes the thin tree with one hand. The banknotes come off the twigs and he catches them against his chest in the open front of his jacket, pressing them in with his forearm.",0),
('s09-03-british-what-build','s03b2',BS,0,"The man breathes, blinks and speaks to someone on the left of the frame. He says: What did they build this time? He waits without moving.",1),
('s09-04-host-house-prices','s02b',HOST,1,"The man breathes, blinks and speaks flatly to someone just to the right of the lens. He says: House prices. He drinks.",1),
('s09-05-politician-pockets','s09b','',1,"The man breathes and blinks slowly. He unfolds one hand, pushes a loose banknote deeper into his breast pocket, pats it and folds his hands again.",0),
('s09-06-host-minds-up','s02b',HOST,1,"The man breathes, blinks, shakes his head a little and speaks straight to the lens. He says: Won't you lot make your minds up. He leans back in his armchair.",1),
('s10-01-soldiers-hands','s10a','',1,"The two men do not speak. They breathe and blink at different times. One of them turns his hands over, looks at his empty palms and lets them rest on his knees.",0),
('s10-02-host-next-time','s02b',HOST,1,"The man breathes, blinks and speaks straight to the lens. He says: Join us next time. He holds the look, then lowers his eyes to his glass.",1),
('s10-03-empty-room','s10b','',1,"Nothing in the room moves except the single banknote on the tree, which turns slowly on its twig. Video noise drifts in the dark areas.",0),
]
os.makedirs(H+'/video-prompts',exist_ok=True); rows=[]
for name,plate,ch,notes,body,talk in C:
    notes_txt=' The banknotes are old British pound notes.' if plate in('s05a','s08a','s09b') else NOTES
    p=HEAD+body+(notes_txt if notes else '')+(TALK if talk else QUIET)
    if plate=='s04a' or plate=='s10a' or plate=='roomv2': p=p.replace('only his voice','only a voice')
    open(f'{H}/video-prompts/{name}.txt','w').write(p+'\n'); rows.append(f'{name}\t{plate}\t{ch}')
open(H+'/clips.tsv','w').write('\n'.join(rows)+'\n'); print(len(rows),'clips')
