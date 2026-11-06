"""Slots for the new action clips in `camping song 2`: two-bar windows on song 2's grid (176 BPM, first downbeat 0.122 s)
where no balaclava rap clip is the visible top clip. Regions follow the cut: Bob's verse, Tarquin's verse, the shared verse.
    python3 slots.py <state-camping song 2.json>  → slots.json"""
import json,sys,pathlib
st=json.load(open(sys.argv[1])); BAR=60/176*4; T0=0.122; L=2*BAR
items=[(t['index'],c['start'],c['end'],c.get('mediaPath','')) for t in st['videoTracks'] for c in t.get('items',[]) if c.get('start') is not None]
def top(t):
    v=[i for i in items if i[1]<=t<i[2]]; return max(v,key=lambda i:i[0]) if v else None
def free(s):
    for k in range(0,28):
        tp=top(s+k*L/27)
        if tp and 'balaclava' in tp[3].lower(): return False
    return True
REG={'bob':(22,82),'tarquin':(84,152),'pairs':(152,208)}
out={}
for r,(a,b) in REG.items():
    k=int((a-T0)/BAR)+1; s=[]
    while T0+k*BAR+L<=b:
        t=round(T0+k*BAR,3)
        if free(t): s.append(t); k+=2
        else: k+=1
    out[r]=s
json.dump(out,open(pathlib.Path(__file__).parent/'slots.json','w'),indent=1)
for r,s in out.items(): print(r,len(s),s)
