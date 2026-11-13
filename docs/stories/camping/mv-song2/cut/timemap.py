"""Old song -> song 2 time map from matched lyric words (+ DTW in the instrumental/hook gaps)."""
import json, re, difflib, bisect
A='/home/jackt/projects/badcode/badcode/docs/stories/camping/mv-song2/analysis/'
def words(k):
    out=[]
    for s in json.load(open(A+f'words-{k}.json')):
        for a,b,w in s['words']:
            w=re.sub(r"[^a-z']","",w.lower())
            if w: out.append((a,w))
    return out
o,n=words('old'),words('new')
sm=difflib.SequenceMatcher(a=[w for _,w in o],b=[w for _,w in n],autojunk=False)
anch=[]
for bl in sm.get_matching_blocks():
    if bl.size>=3:
        for k in range(bl.size): anch.append((o[bl.a+k][0],n[bl.b+k][0]))
dtw=json.load(open(A+'dtw-old-new.json'))
# hook/instrumental gaps in the old song where no lyric anchors exist: take DTW points
for lo,hi in [(69.5,89.5),(135,154.5)]:
    for a,b in dtw[::10]:
        if lo<=a<=hi: anch.append((a,b))
anch=[x for x in anch if x[0]<200.9]+[(201.0,183.9)]
anch.sort()
mono=[]
for a,b in anch:
    if not mono or (a>mono[-1][0]+0.05 and b>mono[-1][1]+0.05): mono.append((a,b))
OA=[a for a,_ in mono]; NB=[b for _,b in mono]
def m(t):
    i=bisect.bisect_right(OA,t)
    if i==0: return NB[0]-(OA[0]-t)
    if i>=len(OA): return NB[-1]+(t-OA[-1])
    a0,a1,b0,b1=OA[i-1],OA[i],NB[i-1],NB[i]
    return b0+(t-a0)*(b1-b0)/(a1-a0)
if __name__=='__main__':
    print(len(mono),'anchors')
    for t in [25.5,30,41.7,52.5,58.3,64,69,75,80,90,101,107.4,112.7,118,123.7,129,134,140,148,155.2,161,167.3,178.7,187,195.8,198.9,202,205,210,215]: print(t,'->',round(m(t),2))
