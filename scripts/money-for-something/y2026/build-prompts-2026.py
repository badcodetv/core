#!/usr/bin/env python3
"""Money For Something 2026 (the year in news), 14 Oct 2026: one Omni prompt per clip and clips-2026.tsv for run-clips-2026.sh.
Lines are the FINAL lines of docs/stories/magic-money-tree/money-for-something-2026-script.md ("THE SHOOTING SCRIPT"), written
here as they are SPOKEN (numbers in words) so the voice does not guess. SCREEN is what the television shows (used by the cut builder).
HEAD and TAIL are the October wording that passed Flow and kept crowd noise out (see build-prompts-topical.py); one addition from
October's "worth trying" list: 'He does not move his head'. Frames on plate P1 (pint on the table) with The Host attached.
Silent clips start on plate P2 (pint already at his lips): Omni continues a state better than it reaches one."""
import os
H=os.path.dirname(os.path.abspath(__file__))
HEAD="A locked-off shot from a scripted television drama, filmed on a closed set: an actor plays a made-up character, a tired man in a back room. The man sits still, does not move his head, breathes and blinks, and speaks straight to the lens in a low, flat, bored monotone with a London English accent, like a man reading out a shopping list, his face still, with no smile and no raised eyebrows. He says: "
TAIL=" He stops talking, closes his mouth and keeps looking at the lens. The pint of lager stays on the table untouched. The television screen stays plain flat blue. He is alone in the room, and after he stops there is only quiet. Audio: only his voice, close and dry, and the faint hum of the empty room. No music."
L=[
('00',"I'm from the future. Weird year, this one. Don't ask me how it ends, it doesn't matter. Moving on.",'2026'),
('01',"On the thirtieth of January, three million pages of Epstein files came out. Four weeks later, America bombed Iran. Unrelated...",'dates'),
('02',"Trump bombed Iran, got nominated for the Nobel Peace Prize, then bombed them again. Fingers crossed. Hope you placed your bets on Polymarket.",''),
('03',"The only reason your petrol isn't a fiver is Xi Jinping. Who would have thought.",'diesel'),
('04',"America has been bringing peace to Iran since nineteen fifty-three. They simply can't get enough of it. Oil, I mean.",'1953'),
('05',"Trump said: A whole civilisation will die tonight. I don't want that to happen, but it probably will.",'post'),
('06',"His anti-war campaign is looking better on Polymarket. For some.",''),
('07',"The Pentagon asked for two hundred billion more. Lockheed got fifty-eight billion for missiles. Somewhere, Dick Cheney got rigor mortis in his pants.",'pentagon'),
('08',"Brown University added up America's wars since nine eleven. Only about eight trillion dollars. Only about nine hundred thousand people killed.",'8trillion'),
('09',"That money would have ended world hunger for thirty years.",'8trillion'),
('10',"At least Lockheed's shareholders didn't go hungry, and the Taliban are gone.",'taliban'),
('11',"The world spends three thousand seven hundred and sixty-eight dollars a second on nuclear bombs. Maybe they should budget better. Cancel the Netflix.",'counter'),
('12',"Pull themselves up by their blood-soaked bootstraps.",'counter'),
('13',"Where I'm from, the energy's free. We got it the year we stopped paying for these. I'm not telling you which year.",''),
('14',"Same thing in Venezuela. Oil, blah, blah, blah. Same shit, different toilet. I'm not doing this twice. Next topic.",'venezuela'),
('15',"Oh yeah. Farage beat a bin. Whatever. The clown show goes on.",'clacton'),
('16',"In September the village of Piddington voted to leave the UK. The government wants to put twelve hundred and fifty male asylum seekers next door.",'piddington'),
('17a',"They're from Afghanistan and Iran, among others. You'll remember those from earlier.",''),
('17b',"Planes, Trains and Automobiles, except it's a dinghy and nobody gets home for Thanksgiving.",''),
('18',"Anyway. People are angry. The only ones who got home rich were three companies. Three hundred and eighty million.",'380m'),
('19',"Quick question: how many meal deals can that buy? Asking for a friend.",'380m'),
('20',"The P P E they wasted would have bought two and a half billion. Next.",'ppe'),
('21a',"Some people got through the pandemic on furlough. One baroness got through it on sixty million and a yacht.",''),
('21b',"It doesn't have heated flooring, though. Moving on.",''),
('22',"A British minister is reported to have told Jeffrey Epstein a five-hundred-billion-euro bailout would be announced that night. Nothing silly.",'bailout'),
('23',"H S 2. A one hundred and two billion pound train that does not exist. It may arrive in the near future: twenty thirty-nine is the latest estimate.",'hs2'),
('24',"How do they get away with wasting a hundred and two billion pounds? Local man is concerned about how this links to migrants.",'hs2'),
('25',"The government wrote off 6.6 billion pounds in one year. How did we not know?",'6.6bn'),
('26',"It came out the Friday before a bank holiday, in a heatwave, on England squad day. You were at a barbecue. They were counting on it.",'6.6bn'),
('27',"Thirty-eight degrees. The government banned barbecues. We drank half a billion pints. The oil companies made forty-seven billion dollars. Cheers.",''),
('29',"So that year was full of nonsensical shit, huh? What to do about it? Well, I'll tell you. You just have to listen...",''),
]
SILENT={
'28':("P2",8,"A locked-off shot from a scripted television drama, filmed on a closed set. The man says nothing. He tips the pint glass up and drinks the whole pint of lager in one long go, swallowing steadily, until the glass is empty. He lowers the empty glass to the table, breathes out through his nose and looks at the lens. The television screen stays plain flat blue. Audio: only swallowing, the glass set down on wood, and the faint hum of the empty room. No music and no voices."),
'30':("P2",10,"A locked-off shot from a scripted television drama, filmed on a closed set. The man says nothing. He tips the pint glass up and drinks the whole pint of lager in one long go until the glass is empty. He sets the empty glass down on the table, stands up and walks out of the left side of the frame. His chair stays empty. The television screen stays plain flat blue. Audio: only swallowing, the glass set down on wood, his footsteps going away, and the faint hum of the empty room. No music and no voices."),
}
os.makedirs(os.path.join(H,'prompts'),exist_ok=True)
out=[]
for cid,line,screen in L:
    n=len(line.split()); need=n/2.8+1.2
    sec=next((s for s in (4,6,8,10) if s>=need),10)
    name=f"y-{cid}"
    open(os.path.join(H,'prompts',name+'.txt'),'w').write(HEAD+line+TAIL)
    out.append(f"{name}\tP1\tThe Host\t{sec}\t{n}\t{screen}\t{line}")
for cid,(pl,sec,p) in SILENT.items():
    open(os.path.join(H,'prompts',f"y-{cid}.txt"),'w').write(p)
    out.append(f"y-{cid}\t{pl}\tThe Host\t{sec}\t0\t\t")
out.sort()
open(os.path.join(H,'clips-2026.tsv'),'w').write('\n'.join(out)+'\n')
print(len(out),'clips'); print('\n'.join(o[:40] for o in out))
