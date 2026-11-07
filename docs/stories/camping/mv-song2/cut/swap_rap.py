"""Swap every old rap-to-camera piece on V1 of `camping song 2 beat 1` for the round-5 stage-rap clip of the same shot.
Same slot, same length; in-point = the old one, pulled back so it fits the 8 s clip. Writes swap-rap.js."""
import json,re,os
ST='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/.bridge/state-camping song 2 beat 1.json'
PRE='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/balaclava/video/premiere/'
picks=json.load(open('/home/jackt/projects/badcode/badcode/docs/stories/camping/mv-balaclava/cleanroom/r5/picks.json'))
s=json.load(open(ST)); rows=[]
for it in s['videoTracks'][0]['items']:
    m=re.match(r'cb-(\w\d\d)-',it['name'])
    if not m: continue
    i=m.group(1); still=picks[i] if len(picks[i])>1 else f'{i}r5-{picks[i]}'
    new=PRE+f'cb-{i}p-{still}.mp4'; d=round(it['end']-it['start'],2)
    USE={'s05':5.0}.get(i,7.5)          # s05p: the jacket changes after ~5.5 s
    if d>4.2:                            # a long hold: split on the beat nearest its middle, second half re-enters
        import bisect
        B=json.load(open('../analysis/beats-new.json'))['beats']; mid=it['start']+d/2
        cut=round(min(B,key=lambda b:abs(b-mid))*25)/25
        d1=round(cut-it['start'],2); d2=round(it['end']-cut,2)
        rows.append([new,it['start'],d1,0.0]); rows.append([new,cut,d2,max(0,min(0.8,USE-d2))])
        continue
    inp=max(0,min(it['inPoint'],round(USE-d,2)))
    rows.append([new,it['start'],d,inp])
win=lambda p:'C:\\'+p.split('/mnt/c/',1)[1].replace('/','\\')
missing=sorted({os.path.basename(r[0]) for r in rows if not os.path.exists(r[0])})
print(len(rows),'rap pieces; new files missing:',missing)
json.dump([[win(r[0])]+r[1:] for r in rows],open('swap-rap.json','w'))
