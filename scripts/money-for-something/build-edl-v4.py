#!/usr/bin/env python3
"""Money For Something, MFS v4 (Jack, 5 Oct, after the review of `MFS v3 full titled`): the plan for the new sequence.
Reads the saved state of `MFS v3 full titled` (.bridge/state-MFS v3 full titled.json: every clip, exactly as placed), applies the
changes below as list edits, re-flows the times, and writes edl-v4.json: entries [item, start, in, dur, vtrack, atrack] as the
earlier kits, plus `strap` (the score PNGs for V3) and `events` (the sounds). It also mixes the one music-and-effects stem
(clips/_v4/MFS-v4-music-sfx-stem.wav) that goes on A4 at 0: the title music where it was, and every sting, buzzer, ding and bed.
`MFS v3 full titled` is not touched. Media: build-v4-media.py.

Changes: the tease after the host's first line; the push-in on the daydream; room after each soldier's "No." for the buzzer;
the poster without the scanner strips; one card (homes promised / built) in place of the two Round 3 placeholders; the Lloyd
George card dropped and the soldier captioned; a cutaway after "all that oil" and after "I shook it responsibly"; the advert as
one clip with small print; the Sound Off stills held longer with tags; FINAL SCORES with the score; the host's new line
(if videos/v4/v4-end-01-host-empty-handed.mp4 exists); the credits."""
import json,os,re,subprocess
H=os.path.dirname(os.path.abspath(__file__))
P='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something'
O=P+'/clips/_v4'; X=O+'/sfx'; F=24; snap=lambda t: round(t*F)/F
st=json.load(open(P+'/.bridge/state-MFS v3 full titled.json'))
tr=lambda kind,i: st[kind][i]['items']
V1=tr('videoTracks',0); A1={round(c['start'],2) for c in tr('audioTracks',0)}; A2=tr('audioTracks',1)
S=[]
for n,c in enumerate(V1):
    S.append(dict(n=n,item=c['name'],i=c['inPoint'],d=c['duration'],a=round(c['start'],2) in A1,t0=c['start'],kids=[],ev=[]))
for c in A2:   # a narrator take belongs to the picture it starts under
    s=[x for x in S if x['t0']-0.001<=c['start']<x['t0']+x['d']][0]; s['kids'].append((c['name'],c['start']-s['t0'],0,c['duration'],0,1))
by=lambda n: [x for x in S if x['n']==n][0]
def seg(item,i,d,a=False,ev=None,tag=None): return dict(n=tag,item=item,i=i,d=d,a=a,kids=[],ev=ev or [])
def after(n,s): S.insert(S.index(by(n))+1,s)
def swap(n,item,i=None,d=None,a=None):
    s=by(n); s['item']=item
    if i is not None: s['i']=i
    if d is not None: s['d']=d
    if a is not None: s['a']=a
    return s
def drop(n): S.remove(by(n))
E=lambda s,name,off,gain=0: s['ev'].append((name,off,gain))
# --- the edits (n is the clip's index on V1 in `MFS v3 full titled`)
after(3,seg('tease.mp4',0,3.0,ev=[('sting',0,-2),('sting',1.0,-6),('sting',2.0,-6)],tag='tease'))
swap(22,'drift-push.mp4',0,3.0,False)
E(by(23),'whistle',1.2,18)
swap(31,'L-v3-p-03-british-no.mp4',d=1.125); E(by(31),'buzzer',0.62,4)
swap(32,'german-no-loud.mp4',d=1.125); E(by(32),'buzzer',0.62,4)
E(by(33),'ding',0.6,4)                                   # the minister shakes the tree: 1
swap(34,'t-debt2.mp4',0,158/24)
swap(40,'t-homes.mp4',0,206/24); drop(41)
drop(42); swap(43,'reads-cap.mp4')
E(by(53),'buzzer',1.15,4)                                # "There's some on it."
after(56,seg('L-s04-07-stare.mp4',0.5,1.5,True,tag='stare2'))
E(by(57),'ding',0.3,4)                                   # Iraq: 2
E(by(59),'tick',0.0,5)
after(70,seg('L-v3-p-06-host-drinks.mp4',2.0,1.5,True,tag='drinks2'))
E(by(75),'ding',0.4,4)                                   # 1939: 3
E(by(83),'jingle',0.0,2)
swap(84,'ad-crawl.mp4',0,238/24); drop(85); drop(86); drop(87)
for n,g,d in [(90,'g09a2',2.0),(91,'g09b2',1.625),(92,'g09c2',2.0)]:
    s=swap(n,by(n)['item'],d=d); s['kids'].append((g+'.mp4',0,0,d,1,0)); E(s,'ding',0.9,4)   # 4, 5, 6
E(by(98),'ding',0.3,4)                                   # 7
s=swap(100,'c-fs2.mp4',0,3.5); E(s,'sting',0,0)
for k in range(1,8): E(s,'ding',0.2*k,0)
for n in (10,28,38,58,64,76,89): E(by(n),'sting',0,0)    # the round cards (the two advert bumpers sit under the jingle)
s=swap(106,'credits.mp4',0,12.5); E(s,'reprise',-0.3,0)
# --- the host's new line, cut round the minister's pockets and the soldiers' hands (only if the clip has been made)
NEW=P+'/videos/v4/v4-end-01-host-empty-handed.mp4'; LV=P+'/videos/v4/leveled/L-v4-end-01-host-empty-handed.mp4'
if os.path.exists(NEW):
    os.makedirs(os.path.dirname(LV),exist_ok=True)
    r=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',NEW,'-af','volumedetect','-vn','-f','null','-'],capture_output=True,text=True).stderr
    mx=float(re.search(r'max_volume: (-?[0-9.]+)',r).group(1))
    if not os.path.exists(LV): subprocess.run(['ffmpeg','-y','-loglevel','error','-i',NEW,'-c:v','copy','-af',f'volume={min(-3-mx,14):.1f}dB','-c:a','aac','-b:a','192k',LV],check=True)
    r=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',NEW,'-af',f'silencedetect=noise={mx-20:.1f}dB:d=0.35','-vn','-f','null','-'],capture_output=True,text=True).stderr
    ss=[float(x) for x in re.findall(r'silence_start: (-?[0-9.]+)',r)]; se=[float(x) for x in re.findall(r'silence_end: (-?[0-9.]+)',r)]
    print('new line: silences',list(zip(ss,se)),'max',mx)
    SPLIT=json.loads(os.environ.get('SPLIT','[0.4583,3.25,3.5833,5.5833]'))   # [in1,out1,in2,out2], set by hand after listening (5 Oct take)
    if SPLIT:
        a,b,c,d=SPLIT; nm='L-v4-end-01-host-empty-handed.mp4'
        after(102,seg(nm,a,b-a,True,tag='line-a')); after(103,seg(nm,c,d-c,True,tag='line-b'))
# --- re-flow
T=0.0; ENT=[]; EV=[('title-music-hot-swing',8.2917,0)]; AT={}
for s in S:
    s['d']=snap(s['d']); s['t']=snap(T); AT[s['n']]=s['t']
    ENT.append([s['item'],round(s['t'],4),round(snap(s['i']),4),round(s['d'],4),0,0])
    for name,off,i,d,v,a in s['kids']: ENT.append([name,round(snap(s['t']+off),4),round(i,4),round(snap(d),4),v,a])
    for name,off,g in s['ev']: EV.append((name,round(s['t']+off,3),g))
    T=snap(T+s['d'])
RT=170.0
for k in range(int(T//RT)+1): ENT.append(['roomtone.wav',round(k*RT,4),0.0,round(snap(min(RT,T-k*RT)),4),0,2])
# --- the strap: [png, start, end]. It is hidden for the cold open and titles, the star prize and the advert.
dings=sorted(t for n,t,g in EV if n=='ding' and not (AT[100]-0.01<=t<AT[100]+3.5))
def run(a,b,k0):
    out=[]; cur=a; k=k0
    for t in [x for x in dings if a<x<b]: out.append([f'strap-{k}.png',round(snap(cur),4),round(snap(t),4)]); cur=t; k+=1
    out.append([f'strap-{k}.png',round(snap(cur),4),round(snap(b),4)]); return out,k
s1,k=run(AT[4],AT[76],0); s2,k=run(AT[82],AT[83],k); s3,k=run(AT[89],AT[100],k)
MARK=[[AT[0],'0 Cold open'],[AT[2],'1 Titles'],[AT['tease'],'Coming up'],[AT[4],'2 Meet the panel'],[AT[10],'3 Round 1'],[AT[28],'4 Round 2: The Price Is War'],[AT[38],'5 Round 3'],
      [AT[58],'6 Quote, Unquote'],[AT[64],'7 Quick-fire'],[AT[76],'8 The star prize'],[AT[83],'9 Advert'],[AT[89],'10 Sound Off'],[AT[100],'11 Final scores'],[AT[106],'12 Credits']]
json.dump(dict(entries=ENT,strap=s1+s2+s3,events=EV,markers=MARK,total=T),open(H+'/edl-v4.json','w'),indent=0)
# --- the stem
stem=O+'/MFS-v4-music-sfx-stem.wav'; src=lambda n: (P+'/clips/_v3/title-music-hot-swing.wav') if n.startswith('title') else f'{X}/{n}.wav'
ins=[]; fc=[]
for k,(n,t,g) in enumerate(EV):
    ins+=['-i',src(n)]; fc.append(f"[{k}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={g}dB,adelay={int(round(max(t,0)*1000))}:all=1[a{k}]")
fc.append(''.join(f'[a{k}]' for k in range(len(EV)))+f"amix=inputs={len(EV)}:normalize=0:dropout_transition=0,atrim=0:{T},afade=t=out:st={T-0.35}:d=0.35[m]")
subprocess.run(['ffmpeg','-y','-loglevel','error']+ins+['-filter_complex',';'.join(fc),'-map','[m]','-ar','48000','-c:a','pcm_s16le',stem],check=True)
print(len(ENT),'placements',round(T,2),'s;',len(s1+s2+s3),'strap pieces;',len(EV),'sounds; final score',k)
for m in MARK: print(f'{m[0]:7.2f}',m[1])
