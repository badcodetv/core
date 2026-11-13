"""Song 2 beat re-cut (2026-11-07). edl-old.json (flattened camping balaclava 1) -> edl-new.json on song 2.
Cuts mapped by lyric words (timemap.py), snapped to song 2's beat grid; stutters rebuilt on eighth notes landing on a beat;
the intro trick (Jack's 14 s black + flashes) moved to song 2's first drop (808 at 13.44 s)."""
import json, bisect, subprocess
from timemap import m
A='/home/jackt/projects/badcode/badcode/docs/stories/camping/mv-song2/analysis/'
FPS=25; F=1/FPS
beats=json.load(open(A+'beats-new.json'))['beats']
eighths=sorted(beats+[(a+b)/2 for a,b in zip(beats,beats[1:])])
def near(grid,t):
    i=bisect.bisect_left(grid,t); c=[g for g in grid[max(0,i-1):i+1]]; return min(c,key=lambda g:abs(g-t))
def snap(t):
    b=near(beats,t)
    if abs(b-t)<=0.18: return b
    e=near(eighths,t)
    return e if abs(e-t)<=0.12 else t
fr=lambda t: round(t*FPS)/FPS
E_=near(eighths,20)-near(eighths,19.9)  # placeholder
EIGHTH=(beats[-1]-beats[0])/(len(beats)-1)/2
old=json.load(open('edl-old.json'))
SONG_END=220.72
# ---- group stutters: runs of short pieces containing a 1-3 frame black
units=[];i=0
while i<len(old):
    j=i
    while j<len(old) and (old[j]['end']-old[j]['start'])<=0.245: j+=1
    run=old[i:j]
    if len(run)>=3 and any(x['src'] is None for x in run):
        units.append({'kind':'stutter','pieces':run,'land':run[-1]['end']}); i=j
    else:
        units.append({'kind':'seg','seg':old[i]}); i+=1
INTRO_OLD_END=12.44; TRICK_BLACK=11.05; DROP=13.44
OUTRO_OLD=212.32; END_CARD_NEW=SONG_END-(215.28-OUTRO_OLD)
def tmap(t):
    if t<=INTRO_OLD_END: return t*TRICK_BLACK/INTRO_OLD_END
    if t>=OUTRO_OLD: return END_CARD_NEW+(t-OUTRO_OLD)
    if t>=201.68: return 183.647+(t-201.68)            # Jack's hook-3 drop shot (35.mp4) on song 2's drop
    if t>=196.12 and t<198.84: return 180.21+(t-196.12)*(181.557-180.21)/(198.84-196.12)
    if t>=198.84: return 181.557+(t-198.84)*(183.647-181.557)/(201.68-198.84)  # his black on "by the time it hits"
    return m(t)
new=[]
def add(start,src,inp,kind='seg',note=''):
    new.append({'start':fr(start),'src':src,'in':inp,'kind':kind,'note':note})
for u in units:
    if u['kind']=='seg':
        s=u['seg']
        if INTRO_OLD_END<=s['start']<25.5: continue        # old intro tail: replaced by the trick
        t=tmap(s['start'])
        if s['start']>=25.5 and t<DROP:                      # verse picture that maps under the trick
            if s['end']>25.5 and tmap(s['end'])>DROP: add(DROP,s['src'],(s['in'] or 0)+(DROP-t) if s['src'] else None,note='lands on drop')
            continue
        st=snap(t) if s['start']>0 else 0
        if s['end']-s['start']<0.25: st=t        # a flick (under 6 frames) keeps its place before the cut it leads into
        if new and new[-1]['kind']=='seg' and abs(new[-1]['start']-fr(st))<0.02: st=near(eighths,t) if abs(near(eighths,t)-st)>0.02 else st+EIGHTH
        add(st,s['src'],s.get('in'))
    else:
        if u["land"]<26: continue                          # intro stutters: replaced by the trick below
        L=near(beats,tmap(u['land']))
        flashes=[p for p in u['pieces'] if p['src']]
        n=len(flashes)
        for k,p in enumerate(flashes):
            st=L-(n-k)*EIGHTH
            add(st,p['src'],p['in'],'flash')
            add(fr(st+EIGHTH)-F,None,None,'flash-black')
# the hole song 2's longer hook 3 leaves before the end card: filled by the action montage
add(183.647+(OUTRO_OLD-201.68),'GAP',None,'gap')
# the intro trick: black, then four flashes of clip 2 on eighths, landing on the drop
TR=[0,1.96,3.52,8.44]; src2='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/clips/2.mp4'
add(TRICK_BLACK,None,None,'trick-black')
for k,ip in enumerate(TR):
    st=DROP-(4-k)*EIGHTH; add(st,src2,ip,'trick'); add(fr(st+EIGHTH)-F,None,None,'trick-black')
new.sort(key=lambda x:(x['start'],0 if x['kind'].startswith(('flash','trick')) else 1))
# de-dup: when two pieces share a start, the stutter/trick piece wins; drop pieces swallowed by a later stutter window
out=[]
for x in new:
    if out and abs(out[-1]['start']-x['start'])<F/2:
        if x['kind']=='seg': continue
        out.pop()
    out.append(x)
for a,b in zip(out,out[1:]): a['end']=b['start']
out[-1]['end']=SONG_END
out=[x for x in out if x['end']-x['start']>=F-1e-6]
# source length guard
dur={}
for x in out:
    if x['src'] and x['src']!='GAP' and x['src'] not in dur:
        dur[x['src']]=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',x['src']],capture_output=True,text=True).stdout or 0)
for x in out:
    if x['src'] and x['src']!='GAP':
        d=x['end']-x['start']
        if x['in']+d>dur[x['src']]-0.02: x['in']=max(0,round(dur[x['src']]-d-0.04,2)); x['note']+=' in pulled back'
        if d>dur[x['src']]: x['note']+=' TOO LONG'
# a piece longer than its media: split, second part re-enters 2 s in (as in camping balaclava 1)
fixed=[]
for x in out:
    if x['src'] and x['src']!='GAP' and x['end']-x['start']>dur[x['src']]-0.05:
        cut=fr(x['start']+dur[x['src']]-x['in']-0.08); y=dict(x); x=dict(x); x['end']=cut; y['start']=cut; y['in']=2.0; y['note']='split re-entry'
        fixed+= [x,y]
    else: fixed.append(x)
out=fixed
# the hole left between the old outro and the end card (song 2's longer hook 3): mark for the action montage
GAP=[(x['start'],x['end']) for x in out if x['start']>190 and x['end']-x['start']>6]
json.dump(out,open('edl-new.json','w'),indent=0)
print('long holds after 190 s:',GAP)
blk=[x for x in out if not x['src']]
print(len(out),'pieces;',len(blk),'black;','too long:',[ (x['start'],x['src'].split('/')[-1]) for x in out if 'TOO LONG' in x['note']])
