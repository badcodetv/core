#!/usr/bin/env python3
"""Money For Something, the topical monologue (10 Oct 2026): one Omni prompt file per talking clip, and clips-topical.tsv
(name, plate, character, seconds) for run-clips-topical.sh. Lines are read from the joke bank's episode table, so the
script file stays the one place a line is written. Talking clips are FRAMES on plate B with The Host attached: Jack picked plate B, and Ingredients re-staged it (plain wall, no tree, no table). Frames held it.
10 Oct, later: five of the first ten clips came back with applause after the line although the prompt said 'no laughter and no applause' and 'no audience'. Those words are now out altogether (naming a sound seems to summon it).
'comedy' is out of HEAD: with it, the first Frames clip came back with audience laughter after the line.
HEAD is the wording that passed Flow's "reputational risk" filter on 10 Oct; "newsreader" and "television studio recording" were refused.
Seconds: about 3 words a second were heard on the probe, plus a second of air; Flow offers 4, 6, 8 and 10."""
import os,re
H=os.path.dirname(os.path.abspath(__file__))
BANK=os.path.join(H,'..','..','docs','stories','magic-money-tree','money-for-something-joke-bank.md')
HEAD="A locked-off shot from a scripted television drama, filmed on a closed set: an actor plays a made-up character, a tired man in a back room. The man sits still, breathes and blinks, and speaks straight to the lens in a low, flat, bored monotone with a London English accent, like a man reading out a shopping list, his face still, with no smile and no raised eyebrows. He says: "
TAIL=" He stops talking, closes his mouth and keeps looking at the lens. The television screen stays plain flat blue. He is alone in the room, and after he stops there is only quiet. Audio: only his voice, close and dry, and the faint hum of the empty room. No music."
rows=re.findall(r"^\| (\d+[a-d]) \| (.+?) \|$",open(BANK).read(),re.M)
os.makedirs(os.path.join(H,'video-prompts'),exist_ok=True)
out=[]
for cid,line in rows:
    if line.startswith('*('): continue
    n=len(line.split()); need=n/2.8+1.2
    sec=next(s for s in (4,6,8,10) if s>=need) if need<=10 else 10
    name=f"t-{int(cid[:-1]):02d}{cid[-1]}"
    open(os.path.join(H,'video-prompts',name+'.txt'),'w').write(HEAD+line+TAIL)
    out.append(f"{name}\tB\tThe Host\t{sec}\t{n}")
# 12d, the silent ending (Jack: "He looks at the dying tree, shrugs, and walks off. No words. so keep that")
open(os.path.join(H,'video-prompts','t-12d.txt'),'w').write("A locked-off shot from a scripted television drama, filmed on a closed set. The man says nothing. He turns his head slowly to look at the bare tree behind him and holds the look. He looks back at the lens and lifts both shoulders in a small shrug. Then he stands up and walks out of the left side of the frame, leaving his wine glass on the table. The television screen stays plain flat blue. Audio: only the faint hum of the empty room and his footsteps. No music and no voices.")
out.append("t-12d\tB\tThe Host\t10\t0")
open(os.path.join(H,'clips-topical.tsv'),'w').write('\n'.join(out)+'\n')
print(len(out),'clips'); print('\n'.join(out))
