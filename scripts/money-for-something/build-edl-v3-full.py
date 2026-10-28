#!/usr/bin/env python3
"""Money For Something, storyboard v3 (the side branch): THE FULL CUT. (build-edl-v3.py is the earlier assembly of the kept scenes only.)
New v3 clips (videos/v3/leveled/L-v3-*.mp4) in storyboard order, with the cut 3 room clips, cards, archive and
narrator takes they play against (in/out copied from edl3.json). The graphics come from build-v3-graphics.py (clips/_v3).
Spoken clips are trimmed to the sound: in 0.15 s before the first sound, out 0.30 s after the last (ffmpeg silencedetect).
SLOW=1 in the environment (Jack, 5 Oct: "people talk and move too fast") also makes a slowed copy of each v3 clip whose line
runs faster than 2.5 words a second (Omni squeezes a long line into its 8 s): speed = 2.5 / rate, never below 0.8, voice
pitch kept (atempo), into videos/v3/slowed/S-<clip>.mp4, and writes edl-v3-slow.json with the trims stretched to match.
Also levels the v3 clips (peak to -3 dB, as build-cut2-media.py does). Writes edl-v3.json. MFS cut 3 is not touched."""
import json,os,re,subprocess
H=os.path.dirname(os.path.abspath(__file__))
V='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/videos/v3'; L=V+'/leveled'; os.makedirs(L,exist_ok=True)
F=24; snap=lambda t: round(t*F)/F
old={}
for it,st,i,d,v,a in json.load(open(H+'/edl3.json'))['entries']: old.setdefault(it,[]).append((i,d))
SIL={'v3-r1-02-british-drift':(0.5,3.5),'v3-r1-03-trench':(1.0,4.0),'v3-p-06-host-drinks':(0.5,4.0),'v3-ad-01-rope':(1.0,5.0),'v3-ad-02-yacht':(1.0,4.5)}
# Hand-set in/out where the sound is not only the line: a synth pad Omni added after the last word (a1-06, a1-10, z-02),
# and the whisper clip, where the lean-in before the words is part of the joke.
OVR={'v3-a1-06-british-in-it':(1.41,3.35),'v3-a1-10-politician-middle-east':(0.84,5.1),'v3-z-02-politician-irresponsible':(2.57,5.5),'v3-q-04-politician-psst':(0.3,3.0),
     'v3-q-02-british-sergeant':(1.83,2.95),'v3-a1-08-politician-as-i-was-saying':(1.36,4.25),'v3-z-04-politician-responsibly':(3.3,5.13)}  # these three: a sip, a pat on the bucket and a noise at the head were read as speech
def prep(n):
    src=f'{V}/{n}.mp4'; out=f'{L}/L-{n}.mp4'
    r=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',src,'-af','volumedetect,silencedetect=noise=-38dB:d=0.2','-vn','-f','null','-'],capture_output=True,text=True).stderr
    mx=float(re.search(r'max_volume: (-?[0-9.]+)',r).group(1))
    if n in SIL:
        if not os.path.exists(out): subprocess.run(['ffmpeg','-y','-loglevel','error','-i',src,'-c:v','copy','-af','volume=0','-c:a','aac',out],check=True)
        return SIL[n]
    g=min(-3.0-mx,14.0)
    if not os.path.exists(out): subprocess.run(['ffmpeg','-y','-loglevel','error','-i',src,'-c:v','copy','-af',f'volume={g:.1f}dB','-c:a','aac','-b:a','192k',out],check=True)
    if n in OVR: return OVR[n]
    # Speech is the loud part; sips, chair creaks and room noise sit well under it. So measure again with the floor set
    # 20 dB under the clip's own peak, and take the first loud start and the last loud end.
    r2=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',src,'-af',f'silencedetect=noise={mx-20:.1f}dB:d=0.45','-vn','-f','null','-'],capture_output=True,text=True).stderr
    ss=[float(x) for x in re.findall(r'silence_start: (-?[0-9.]+)',r2)]; se=[float(x) for x in re.findall(r'silence_end: (-?[0-9.]+)',r2)]
    first=se[0] if ss and ss[0]<=0.05 and se else 0.0
    last=ss[-1] if ss and len(ss)>len(se) else (ss[-1] if ss and se and se[-1]>=7.95 else 8.0)
    if last<=first: last=8.0
    return (max(0,first-0.15),min(8.0,last+0.30))
E=[]; M=[]; T=0.0
def put(item,i,d,v=0,a=0,at=None):
    global T; d=snap(d); E.append([item,round(snap(T if at is None else at),4),round(snap(i),4),round(d,4),v,a])
    if at is None: T=snap(T+d)
SLOW=bool(os.environ.get('SLOW')); SD=V+'/slowed'; TARGET=2.5; FLOOR=0.8; RATES=[]
def words(n):
    x=open(f'{H}/video-prompts/{n}.txt').read()
    return sum(len(m.split()) for m in re.findall(r'(?:says|whispers): (.*?[.?])(?= He | The man on| Nobody else| The banknotes| The sleeves|$)',x))
def new(n):
    i,o=prep(n); w=words(n); span=max(0.3,(o-i)-0.45); rate=w/span if w else 0; f=1.0
    if SLOW and w>=4 and rate>TARGET: f=max(FLOOR,TARGET/rate)
    RATES.append((n,w,round(rate,2),round(f,2)))
    if f>=0.995: return put('L-'+n+'.mp4',i,o-i)
    os.makedirs(SD,exist_ok=True); out=f'{SD}/S-{n}.mp4'
    if not os.path.exists(out):
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{L}/L-{n}.mp4','-filter_complex',f'[0:v]setpts=PTS/{f:.4f},fps=24[v];[0:a]atempo={f:.4f}[a]','-map','[v]','-map','[a]',
                        '-c:v','libx264','-crf','15','-preset','medium','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv','-c:a','aac','-b:a','192k',out],check=True)
    put('S-'+n+'.mp4',i/f,(o-i)/f)
def room(n,k=0): i,d=old['L-'+n+'.mp4'][k]; put('L-'+n+'.mp4',i,d)
def pic(n,d=None): put(n+'.mp4',0,d or old[n+'.mp4'][0][1])
GX='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/clips/_v3'
def gfx(n,d=None):
    d=d or float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'{GX}/{n}.mp4'],capture_output=True,text=True).stdout)
    put(n+'.mp4',0,d)
def narr(n,at): i,d=old[n+'.wav'][0]; put(n+'.wav',0,d,0,1,at)
mark=lambda n: M.append([round(snap(T),4),n])
# THE FULL CUT (5 Oct, after Jack watched the assembly: "the Theresa May clip needs to be at the beginning … a lot of these clips are in the wrong order").
# Cut 3's whole film with the v3 scenes in it, every round in cut 3's shape: card, the host asks, the record answers (archive + narrator), the room answers.
def c3(names):
    for n in names: room(n)
mark('0 Cold open'); pic('g01-may-quote'); s=T; pic('g01-may-2016'); narr('line-s01-nice-try',s+0.15)
mark('1 Titles'); c3(['s02-00-wide','s02-01-host-title'])
mark('2 Meet the panel'); c3(['s03-01-host-card-british','s03-02-british-silent','s03-03-host-card-german','s03-04-german-silent','s03-05-host-card-politician','s03-06-politician-silent'])
mark('3 Round 1: How did it start?'); pic('c-r1'); room('s04-01-host-round-one'); s=T; pic('g04a-kitchener'); pic('g04b-somme-men-walking'); pic('g04c-trench'); narr('line-s04-nineteen-fourteen',s+0.15)
c3(['s04-02-british-duke','s04-03-german-bosnia','s04-04-british-france']); new('v3-r1-01-politician-russia'); gfx('c-y1'); gfx('g-petrograd-1917')
room('s04-05-host-who-paid'); new('v3-r1-02-british-drift'); new('v3-r1-03-trench'); new('v3-r1-04-host-snap'); c3(['s04-06-host-lives','s04-07-stare','s04-08-politician-watch'])
mark('4 Round 2: The Price Is War'); gfx('c-r2-pw'); new('v3-p-01-host-rules'); new('v3-p-02-host-world-war'); new('v3-p-03-british-no'); new('v3-p-04-german-no'); room('s05-02-politician-shake')
s=T; gfx('t-debt'); narr('line-s05-nobody-asked-take3',s+0.15); new('v3-p-05-politician-capitalism'); gfx('f-northern-rock'); new('v3-p-06-host-drinks')
mark('5 Round 3: What happened next? (the first argument)'); pic('c-r3'); room('s06-01-host-homes'); s=T; pic('g06a-PLACEHOLDER-men-resting'); pic('g06b-PLACEHOLDER-1931-unemployed'); narr('line-s06-despite-the-debt',s+0.15)
gfx('q-lloyd-george',2.5); new('v3-a1-01-british-reads'); room('s06-02-politician-no-money')
for n in ['v3-a1-02-british-shells','v3-a1-03-politician-different','v3-a1-04-british-how','v3-a1-05-politician-war','v3-a1-06-british-in-it','v3-a1-07-host-card']: new(n)
gfx('c-y10'); new('v3-a1-08-politician-as-i-was-saying'); room('s06-03-british-some-on-it'); room('s06-04-politician-spoken-for'); new('v3-a1-09-host-spoken-for-what'); new('v3-a1-10-politician-middle-east'); gfx('t-iraq',3.0)
mark('6 Quote, Unquote'); gfx('c-qu'); gfx('q-keynes-ask')
for n in ['v3-q-01-german-marx','v3-q-02-british-sergeant','v3-q-03-host-keynes','v3-q-04-politician-psst']: new(n)
mark('7 Quick-fire (the second argument)'); pic('c-qf'); room('s07-01-host-quickfire'); room('s07-02-host-rules')
for n in ['v3-z-01-german-zeppelins','v3-z-02-politician-irresponsible','v3-z-03-german-you-shook','v3-z-04-politician-responsibly']: new(n)
gfx('c-y7'); s=T; pic('g07a-berlin-1923'); narr('line-s07a-shake',s+0.25); room('s07-03-german-wheelbarrows'); s=T; pic('g07b-london-1931'); narr('line-s07b-starve-take2',s+0.25); pic('g07c-1939-b')
mark('8 The star prize'); pic('c-sp'); s=T
for n in ['g08a-guardsmen-building','g08b-new-town-houses-b','g08c-hospital-b','g08d-houses-b']: pic(n)
t=s+0.15; 
for n in ['line-s08a-nineteen-forty-eight','line-s08b-built-the-houses','line-s08c-done-once']: narr(n,t); t+=old[n+'.wav'][0][1]+0.35
room('s08-01-plant'); new('v3-s-01-politician-house-prices')
mark('9 Advert'); gfx('c-ad-in'); gfx('ad-a-headline'); gfx('ad-b-gowns'); gfx('ad-c-profit'); gfx('ad-d-yacht'); gfx('c-ad-out')
mark('10 Sound Off'); pic('c-so')
for k,g in enumerate(['g09a-2008','g09b-2010','g09c-2020']): s=T; room('s09-01-host-dubs',k); put(g+'.mp4',0,old[g+'.mp4'][0][1],1,0,s)
c3(['s09-02-politician-catches','s09-03-british-what-build','s09-04-host-house-prices']); room('s09-05-politician-pockets',0); new('v3-s-02-politician-crypto'); gfx('f-farage'); room('s09-06-host-minds-up')
mark('11 Final scores'); pic('c-fs'); s=T; pic('g10a-may-2017'); narr('line-s10-what-happened-next',s+0.15); pic('g10b-caption-dup'); room('s09-05-politician-pockets',1); c3(['s10-01-soldiers-hands','s10-02-host-next-time','s10-03-empty-room'])
put('roomtone.wav',0,min(T,old['roomtone.wav'][0][1]),0,2,0)
if T>old['roomtone.wav'][0][1]: put('roomtone.wav',0,T-old['roomtone.wav'][0][1],0,2,old['roomtone.wav'][0][1])
json.dump(dict(entries=E,markers=M,total=T),open(H+('/edl-v3-full.json'),'w'),indent=0)
for r in RATES:
    if r[3]<1: print('slow',*r)
print(len(E),'placements',round(T,2),'s',len(M),'markers')
for e in E:
    pass
