"""Action shots on song 2 (2026-11-07): lyric hits + hook montages (V2), the v2-world shots (V3), and the hook-3 gap (main track)."""
import json,bisect
A='/home/jackt/projects/badcode/badcode/docs/stories/camping/mv-song2/analysis/'
V='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/'
CA=V+'action/video/premiere/'; J=V+'clips/'; W2='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/Camping Comic/music video/'
beats=json.load(open(A+'beats-new.json'))['beats']; B=(beats[-1]-beats[0])/(len(beats)-1); fr=lambda t:round(t*25)/25
def beat_at(t):  # the beat nearest t (the picture arrives with the word)
    i=bisect.bisect_left(beats,t); return min([beats[j] for j in (i-1,i) if 0<=j<len(beats)],key=lambda b:abs(b-t))
def ca(k):
    import glob; return glob.glob(CA+f'ca-{k}-*.mp4')[0]
main=json.load(open('edl-new.json'))
protect=[]
for x in main:
    rap=x['src'] and '/balaclava/' in x['src']
    if x['kind'] not in ('seg','gap'): protect.append((x['start'],x['end']))
    elif rap and x['end']-x['start']<2.5: protect.append((x['start'],x['end']))
    elif rap: protect+= [(x['start'],x['start']+1.0),(x['end']-1.0,x['end'])]   # a long rap shot may cut away mid-line
def free(a,b,taken): return all(b<=p or a>=q for p,q in protect+taken)
V2,V3,taken2,taken3,skipped=[],[],[],[],[]
def place(lst,taken,src,t,nb,inp,why):
    s=beat_at(t)
    for shift in [0,-1,1,-2,2,-4,4]:
        a=fr(s+shift*B); b=fr(a+nb*B)
        if free(a,b,taken):
            lst.append({'start':a,'end':b,'src':src,'in':inp,'why':why}); taken.append((a,b)); return
    skipped.append((why,round(t,2)))
# lyric hits
for src,t,nb,inp,why in [
 (J+'5.mp4',22.42,4,1.0,'Waitrose door: the trolley out of Waitrose'),
 (ca('x6'),36.32,4,0.2,'white tank: the BAD CODE X8'),
 (ca('x5'),79.72,4,0.2,'living in a tent'),
 (ca('u25'),95.92,4,0.2,'tax the rich: money off the balcony'),
 (ca('t2'),110.22,4,0.2,'the lane in my M3: the speedboat'),
 (J+'27.mp4',115.60,4,1.5,'resent me: the smug red wine'),
 (ca('x2'),119.78,4,0.2,'my Chateau: the wine pour'),
 (ca('b23'),145.88,8,0.2,'living in a car park, rained on in the dark'),
 (ca('t21'),151.32,4,0.2,'then I got the sack: the trading floor'),
 (J+'31.mp4',154.70,4,1.0,'the AI does the fast part: the wrecked future'),
 (J+'32.mp4',166.16,4,1.0,'the robots replaced us'),
 (J+'31.mp4',169.36,4,7.5,'when the government debased us'),
]: place(V2,taken2,src,t,nb,inp,why)
# hook montages: a 4-beat action shot on every other bar, Jack's picture between
def montage(t0,t1,items,label):
    b0=beat_at(t0); k=0; a=b0
    while a+4*B<=t1 and k<len(items):
        src,inp=items[k]
        if free(fr(a),fr(a+4*B),taken2):
            V2.append({'start':fr(a),'end':fr(a+4*B),'src':src,'in':inp,'why':label}); taken2.append((fr(a),fr(a+4*B))); k+=1
            a+=8*B
        else: a+=4*B
montage(56.0,77.6,[(ca('b1'),0.2),(ca('b2'),0.2),(ca('b22'),0.2),(ca('b24'),0.2),(ca('b25'),0.2),(ca('b26'),0.2),(ca('b6'),0.2),(J+'17.mp4',1.0)],'hook 1: Bob\'s life')
montage(121.6,143.3,[(ca('t23'),0.2),(ca('t24'),0.2),(ca('t25'),0.2),(ca('t3'),0.2),(ca('t4'),0.2),(ca('t6'),0.2),(ca('u23'),0.2),(J+'29.mp4',1.0),(J+'7.mp4',1.0)],'hook 2: Tarquin\'s life')
# v2 world (its own track, mute V3 to lose them all)
for src,t,nb,inp,why in [
 (W2+'videos-tarquin/tq-shout-back.mp4',99.0,4,4.2,'what the fuck you think this is: Tarquin shouts at Bob (v2)'),
 (W2+'videos-gap/gp-w9.mp4',148.42,4,1.0,'rained on in the dark: both under the multi-storey (v2)'),
 (W2+'videos/05.mp4',173.04,4,0.5,'back to that time when we very first met (v2)'),
 (W2+'videos/24.mp4',175.10,4,2.6,'I do regret that I judged you: Tarquin five years on (v2)'),
 (W2+'videos/25.mp4',178.96,4,0.5,'the same side all along: their cards meet over the fire (v2)'),
 (W2+'videos/09.mp4',51.0,4,0.5,'I hold that door, please sir (v2)'),
]: place(V3,taken3,src,t,nb,inp,why)
# hook-3 gap on the main track: 4-beat cuts to the end of the hook, then 8-beat holds into the end card
gap=[x for x in main if x['kind']=='gap'][0]
fill=[(ca('x3'),0.2),(ca('x4'),0.2),(J+'16.mp4',4.5),(J+'29.mp4',5.0),(ca('x5'),0.2),(J+'25.mp4',4.5),(J+'18.mp4',7.5),(ca('t4'),3.0)]
hold=[(ca('u25'),0.2),(J+'17.mp4',7.2),(ca('x6'),0.2),(J+'32.mp4',5.5)]
GAPFILL=[];a=beat_at(gap['start']);
for src,inp in fill:
    if a+4*B>205.0: break
    GAPFILL.append({'start':fr(a),'end':fr(a+4*B),'src':src,'in':inp,'why':'hook 3: both worlds'}); a+=4*B
for src,inp in hold:
    e=min(a+8*B,gap['end'])
    if e-a<1: break
    GAPFILL.append({'start':fr(a),'end':fr(e),'src':src,'in':inp,'why':'outro hold'}); a=e
if GAPFILL: GAPFILL[-1]['end']=gap['end']; GAPFILL[0]['start']=gap['start']
import os
for x in V3:
    x['src_orig']=x['src']; x['src']=V+'action/v2-1080/v2-'+os.path.basename(os.path.dirname(x['src']))+'-'+os.path.basename(x['src'])
    assert os.path.exists(x['src']),x['src']
json.dump({'V2':sorted(V2,key=lambda x:x['start']),'V3':sorted(V3,key=lambda x:x['start']),'gap':GAPFILL,'skipped':skipped},open('overlays.json','w'),indent=1)
print('V2',len(V2),'V3',len(V3),'gap',len(GAPFILL),'skipped',skipped)
for x in sorted(V2+V3,key=lambda x:x['start']): print(f"{x['start']:7.2f} {x['end']-x['start']:.2f} {x['src'].split('/')[-1][:20]:20} {x['why']}")
for x in GAPFILL: print(f"GAP {x['start']:7.2f} {x['end']-x['start']:.2f} {x['src'].split('/')[-1][:20]}")
