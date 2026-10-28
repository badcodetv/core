#!/usr/bin/env python3
"""Money For Something, MFS v4 (Jack, 5 Oct, after the review of `MFS v3 full titled`): the graphics and sounds the v4 cut needs.
1280x720 / 24 fps into clips/_v4/, sounds into clips/_v4/sfx/. Same typeface, tag and year slot as build-v3-graphics.py. Skips what exists.

Pictures   t-debt2        the war loan poster without the scanner's colour strips: the poster on the right, the tag on the left
           t-homes        replaces both Round 3 placeholders (soldiers with a mortar stamped 1919; a 1931 photograph stamped 1921):
                          HOMES PROMISED 500,000, then HOMES BUILT 213,000 (the 1919 Housing Act; figures read on the web, 5 Oct)
           reads-cap      the soldier reading the promise, captioned with who said it (the quote card before it is dropped)
           g09a2/b2/c2    the Sound Off stills, held longer, each with a tag that says what it is
           c-fs2          FINAL SCORES: the minister counts up to 7, everyone else stays on 0
           strap-0..7.png the running score, top right, a transparent PNG for V3
           tease          COMING UP: three one-second flashes after the host's first line
           ad-crawl       the advert's four shots as one clip with a fast small-print crawl (every clause is from the Mone guardrails)
           drift-push     the daydream: the push-in on the soldier's eyes that was never made (baked; 2x plate, eased)
           credits        the empty room, a fast roll, the room again for the last chord
Sounds     buzzer, ding, tick (a clock for the quote round), whistle (the trench): all synthesised here, so no licence
           sting          the theme's own final hit, for the round cards
           jingle         "Local Forecast - Elevator", Kevin MacLeod (incompetech.com), CC BY 4.0: credit owed
           reprise        the theme's last eight bars, for the credits"""
import os,subprocess,tempfile
P='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something'
C=P+'/clips'; O=C+'/_v4'; X=O+'/sfx'; SRC=O+'/src'; V3=C+'/_v3'; V=P+'/videos'
for d in (O,X,SRC): os.makedirs(d,exist_ok=True)
B='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'; R='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
IMP='/mnt/c/Windows/Fonts/impact.ttf'; YEL='0xFFD23A'
ENC=['-r','24','-c:v','libx264','-crf','16','-preset','medium','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv']
T=tempfile.mkdtemp(); K=[0]
def tf(s):
    K[0]+=1; p=f'{T}/{K[0]}.txt'; open(p,'w').write(s); return p
def dt(text,size,x,y,font=B,color='white',box=False,en=None,extra=''):
    b=":box=1:boxcolor=black@0.55:boxborderw=14" if box else ""
    e=f":enable='{en}'" if en else ""
    return f"drawtext=fontfile={font}:textfile={tf(text)}:fontcolor={color}:fontsize={size}:x={x}:y={y}{b}{extra}{e}"
YEAR=lambda t,en=None: dt(t,34,48,'h-96',box=True,en=en)
def tag(lines,x,y,size=40,pad=26,gap=12,w=None,en=None):
    hs=[(s or size) for _,s in lines]; h=sum(hs)+gap*(len(lines)-1)+pad*2
    w=w or int(max(len(t)*(s or size)*0.57 for t,s in lines))+pad*2+46
    e=f":enable='{en}'" if en else ""
    f=[f"drawbox=x={x+6}:y={y+8}:w={w}:h={h}:color=black@0.45:t=fill{e}",f"drawbox=x={x}:y={y}:w={w}:h={h}:color=0xC8A46E:t=fill{e}",
       f"drawbox=x={x}:y={y}:w={w}:h={h}:color=0x6B4A22:t=4{e}",f"drawbox=x={x+16}:y={y+h//2-9}:w=18:h=18:color=0x1c130a:t=fill{e}"]
    yy=y+pad
    for (t,s),hh in zip(lines,hs): f.append(dt(t,hh,x+52,yy,color='0x24160a',en=en)); yy+=hh+gap
    return ','.join(f)
def out(n,ext='mp4'): return f'{O}/{n}.{ext}'
def run(a): subprocess.run(['ffmpeg','-y','-loglevel','error']+a,check=True)
def have(n,ext='mp4'):
    return os.path.exists(out(n,ext))
def still(name,src,dur,extra,crop=None,ybias=0.5,zoom=0.05,dim=None):
    if have(name): return
    n=int(round(dur*24)); c=(f"crop={crop}," if crop else ""); e=(f"eq=brightness={dim}:saturation=0.6," if dim else "")
    vf=(f"{c}scale=2560:1440:force_original_aspect_ratio=increase,crop=2560:1440:(iw-2560)/2:(ih-1440)*{ybias},"
        f"zoompan=z='1+{zoom}*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1280x720:fps=24,{e}{extra},format=yuv420p")
    run(['-i',src,'-vf',vf,'-frames:v',str(n),'-an']+ENC+[out(name)]); print('still',name)

# --- the war loan poster, cropped inside the scan (the poster is x 771..3342, y 530..4560 of a 3999x5000 scan)
if not have('t-debt2'):
    n=int(6.6*24)
    vf=("[0:v]crop=2540:3990:786:550,scale=-2:1340[p];color=c=0x0b0b0b:s=2560x1440:r=24[bg];[bg][p]overlay=x=1560:y=50,"
        f"zoompan=z='1+0.04*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1280x720:fps=24,eq=brightness=-0.04,"
        +tag([('THE NATIONAL DEBT',30),('1914: ABOUT £650 MILLION',40),('1919: ABOUT £7.4 BILLION',40)],70,250)+','+YEAR('1915')+",format=yuv420p[v]")
    run(['-i',f"{C}/s05-can-we-afford-it/The British sovereign will win. Invest in the war loan to-day LCCN2003668435.jpg",'-filter_complex',vf,'-map','[v]','-frames:v',str(n),'-an']+ENC+[out('t-debt2')]); print('t-debt2')

# --- homes promised / homes built: one card for the narrator's whole line (8.58 s)
if not have('t-homes'):
    d=206/24
    vf=(tag([('THE 1919 HOUSING ACT',30),('HOMES PROMISED: 500,000',56)],200,170,w=880)+','
        +tag([('WHEN THE MONEY WAS STOPPED',30),('HOMES BUILT: 213,000',56)],200,390,w=880,en='gte(t,4.2)')+','+YEAR('1919 – 1923')+',format=yuv420p')
    run(['-f','lavfi','-i',f'color=c=black:s=1280x720:r=24:d={d}','-vf',vf,'-an']+ENC+[out('t-homes')]); print('t-homes')

# --- the soldier reads the promise, captioned (video and sound kept; the caption shows while he reads, source 0.6 to 5.2 s)
if not have('reads-cap'):
    en='between(t,0.6,5.2)'
    vf=(dt('DAVID LLOYD GEORGE, PRIME MINISTER',26,48,'h-132',box=True,en=en)+','+dt('Wolverhampton  ·  November 1918',26,48,'h-88',font=R,box=True,en=en)+',format=yuv420p')
    run(['-i',f'{V}/v3/slowed/S-v3-a1-01-british-reads.mp4','-vf',vf,'-c:a','copy']+ENC+[out('reads-cap')]); print('reads-cap')

# --- Sound Off: each still held longer, with a tag (figures: NAO cash outlay; Spending Review 2010; Bank of England asset purchases in 2020)
S9=C+'/s09-sound-off'
still('g09a2',f'{S9}/Lehman Brothers-NYC-20080915.jpg',2.0,tag([('THE BANKS, RESCUED',30),('£133 BILLION IN CASH',52)],60,440)+','+YEAR('2008'),zoom=0.04)
still('g09b2',f'{S9}/Budget 2014; Chancellor George Osborne delivering his Budget Statement.jpg',1.625,tag([('PUBLIC SPENDING, CUT',30),('£81 BILLION',52)],60,440)+','+YEAR('2010'),zoom=0.04)
still('g09c2',f'{S9}/10 Downing Street COVID-19 press conference, 20 March 2020.png',2.0,tag([('NEW MONEY, PRINTED',30),('£450 BILLION',52)],60,440)+','+YEAR('2020'),zoom=0.04)

# --- FINAL SCORES: the minister counts 0..7 over the first 1.4 s
if not have('c-fs2'):
    d=3.5; f=[dt('FINAL SCORES',44,'(w-text_w)/2',120)]
    for k in range(8):
        a=k*0.2; b=(k+1)*0.2 if k<7 else d+1
        f.append(dt(f'THE MINISTER   {k}',120,'(w-text_w)/2',240,font=IMP,color=YEL,en=f'between(t,{a:.2f},{b-0.001:.3f})'))
    f.append(dt('EVERYONE ELSE   0',120,'(w-text_w)/2',420,font=IMP,color='white'))
    run(['-f','lavfi','-i',f'color=c=black:s=1280x720:r=24:d={d}','-vf',','.join(f)+',format=yuv420p','-an']+ENC+[out('c-fs2')]); print('c-fs2')

# --- the running score strap, transparent PNGs
for k in range(8):
    if have(f'strap-{k}','png'): continue
    vf=("format=rgba,drawbox=x=806:y=24:w=450:h=50:color=black@0.72:t=fill:replace=1,drawbox=x=806:y=24:w=450:h=50:color=0xFFD23A@0.9:t=2:replace=1,"
        +dt(f'MINISTER {k}',30,824,33,font=IMP,color=YEL)+','+dt('EVERYONE ELSE 0',30,1020,33,font=IMP,color='white'))
    run(['-f','lavfi','-i','color=c=black@0.0:s=1280x720,format=rgba','-vf',vf,'-frames:v','1',out(f'strap-{k}','png')]); print('strap',k)

# --- COMING UP: falling notes, the yacht, the £72 million tag, a second each
if not have('tease'):
    lab=dt('COMING UP',54,48,40,font=IMP,color=YEL,extra=':borderw=4:bordercolor=black')
    vf=(f"[0:v]trim=1.75:2.75,setpts=PTS-STARTPTS,fps=24,scale=1280:720,{lab}[a];[1:v]trim=1.2:2.2,setpts=PTS-STARTPTS,fps=24,scale=1280:720,{lab}[b];"
        f"[2:v]trim=0:1,setpts=PTS-STARTPTS,fps=24,scale=1280:720,{lab}[c];[a][b][c]concat=n=3:v=1:a=0,format=yuv420p[v]")
    run(['-i',f'{V}/leveled/L-s05-02-politician-shake.mp4','-i',f'{V}/v3/v3-ad-02-yacht.mp4','-i',f'{V3}/f-farage.mp4','-filter_complex',vf,'-map','[v]','-frames:v','72','-an']+ENC+[out('tease')]); print('tease')

# --- the advert as one clip, with the small print. Every clause is from research/michelle-mone-ppe-medpro.md §7; no person and no company is named.
SMALL=("TERMS AND CONDITIONS APPLY.   £122 MILLION IS WHAT THE HIGH COURT ORDERED ONE COMPANY TO REPAY, IN OCTOBER 2025.   £65 MILLION IS THE GUARDIAN’S REPORTING, NOT A COURT’S FINDING.   "
       "NO COURT HAS FOUND THAT ANY YACHT WAS BOUGHT WITH PPE MONEY.   NOBODY HAS BEEN CHARGED WITH ANYTHING.   QUEUE NOT INCLUDED.   MINISTER NOT INCLUDED.   GOWNS MAY NOT BE STERILE.")
if not have('ad-crawl'):
    ins=[];
    for n in ['ad-a-headline','ad-b-gowns','ad-c-profit','ad-d-yacht']: ins+=['-i',f'{V3}/{n}.mp4']
    D=238/24  # 58+58+59+63 frames
    crawl=(f"drawbox=x=0:y=676:w=1280:h=44:color=black@0.8:t=fill,drawtext=fontfile={R}:textfile={tf(SMALL)}:fontcolor=white:fontsize=22:y=687:x=w-(w+text_w)*t/{D-0.3:.3f}")
    vf=f"[0:v][1:v][2:v][3:v]concat=n=4:v=1:a=0,fps=24,{crawl},format=yuv420p[v]"
    run(ins+['-filter_complex',vf,'-map','[v]','-an']+ENC+[out('ad-crawl')]); print('ad-crawl')

# --- the daydream push-in: source 0.5..3.5 s of the drift clip, scale 1.00 -> 1.22, eased, aimed at his eyes
if not have('drift-push'):
    n=72; z="(1+0.22*(0.5-0.5*cos(PI*on/71)))"
    vf=(f"trim=0.5:3.5,setpts=PTS-STARTPTS,fps=24,scale=2560:1440:flags=lanczos,zoompan=z='{z}':x='(iw-iw/zoom)*0.56':y='(ih-ih/zoom)*0.30':d=1:s=1280x720:fps=24,format=yuv420p")
    run(['-i',f'{V}/v3/leveled/L-v3-r1-02-british-drift.mp4','-vf',vf,'-frames:v',str(n),'-an']+ENC+[out('drift-push')]); print('drift-push')

# --- the German soldier's "No." is nearly inaudible in the leveled clip: a louder copy
if not have('german-no-loud'):
    run(['-i',f'{V}/v3/leveled/L-v3-p-04-german-no.mp4','-c:v','copy','-af','volume=8dB,alimiter=limit=0.7','-c:a','aac','-b:a','192k',out('german-no-loud')]); print('german-no-loud')

# --- credits: the empty room (8 s, then its last frame held), dimmed under a fast roll, bright again for the last chord
CRED=[('MONEY FOR SOMETHING',IMP,54,YEL),('',B,20,'white'),
 ('THE MINISTER',B,22,YEL),('still with us',R,26,'white'),('THE SOLDIERS',B,22,YEL),('still waiting',R,26,'white'),('',B,20,'white'),
 ('MUSIC',B,22,YEL),('“Hot Swing” and “Local Forecast – Elevator”',R,26,'white'),('Kevin MacLeod (incompetech.com)',R,26,'white'),
 ('Licensed under Creative Commons: By Attribution 4.0',R,22,'white'),('creativecommons.org/licenses/by/4.0',R,22,'white'),('',B,20,'white'),
 ('PICTURES',B,22,YEL),('Nigel Farage: Laurie Noble / UK Parliament, CC BY 3.0',R,24,'white'),('Northern Rock queue: Dominic Alves, CC BY 2.0',R,24,'white'),
 ('Lehman Brothers, 15 September 2008: Robert Scoble, CC BY 2.0',R,24,'white'),
 ('Theresa May: Andrew Parsons / Prime Minister’s Office; HM Government',R,24,'white'),('The Budget, 2014: HM Treasury.  The briefing, 2020: 10 Downing Street',R,24,'white'),
 ('Contains public sector information licensed under',R,22,'white'),('the Open Government Licence v3.0.',R,22,'white'),('',B,20,'white'),
 ('ARCHIVE',B,22,YEL),('Crown copyright (expired), Central Office of Information, 1948,',R,22,'white'),('via The National Archives and the Internet Archive',R,22,'white'),
 ('Imperial War Museums  ·  Library of Congress',R,22,'white'),('Bibliothèque nationale de France  ·  US National Archives',R,22,'white'),('',B,20,'white'),
 ('BADCODE',IMP,44,YEL)]
if not have('credits'):
    D=12.5; ROLL=10.2; y=0; f=[]
    H=sum(s+14 for _,_,s,_ in CRED); spd=(720+H)/ROLL
    for t,fo,s,col in CRED:
        if t: f.append(dt(t,s,'(w-text_w)/2',f'720+{y}-{spd:.2f}*t',font=fo,color=col,extra=':shadowcolor=black@0.8:shadowx=2:shadowy=2'))
        y+=s+14
    dim="eq=brightness='if(lt(t,0.6),-0.30*t/0.6,if(lt(t,10.2),-0.30,if(lt(t,11.0),-0.30*(11.0-t)/0.8,0)))':eval=frame"
    vf=f"fps=24,tpad=stop_mode=clone:stop_duration=6,trim=0:{D},setpts=PTS-STARTPTS,{dim},"+','.join(f)+',format=yuv420p'
    run(['-i',f'{V}/leveled/L-s10-03-empty-room.mp4','-vf',vf,'-frames:v',str(int(D*24)),'-an']+ENC+[out('credits')]); print('credits')

# ---------------- sounds (48 kHz stereo wav)
def snd(name,args):
    p=f'{X}/{name}.wav'
    if os.path.exists(p): return
    run(args+['-ar','48000','-ac','2','-c:a','pcm_s16le',p]); print('sfx',name)
def synth(name,expr,d,af):
    snd(name,['-f','lavfi','-i',f"aevalsrc='{expr}':s=48000:d={d}",'-af',af])
synth('buzzer',"0.30*(sgn(sin(2*PI*116*t))+0.7*sgn(sin(2*PI*155*t)))",0.42,'lowpass=f=1600,afade=t=in:d=0.01,afade=t=out:st=0.36:d=0.06,volume=-8dB')
synth('ding',"0.5*exp(-4.5*t)*(sin(2*PI*1568*t)+0.45*sin(2*PI*3136*t)+0.2*sin(2*PI*4704*t)+0.1*sin(2*PI*6272*t))",1.1,'afade=t=in:d=0.003,afade=t=out:st=0.9:d=0.2,volume=-9dB')
synth('tick',"0.6*exp(-70*mod(t,0.5))*sin(2*PI*(1500+500*lt(mod(t,1),0.5))*t)",5.0,'highpass=f=700,afade=t=out:st=4.8:d=0.2,volume=-14dB')
synth('whistle',"0.4*sin(2*PI*2850*t+3*sin(2*PI*27*t))*(0.6+0.4*sin(2*PI*27*t))",1.5,'lowpass=f=3600,aecho=0.8:0.6:90|170:0.35|0.2,afade=t=in:d=0.08,afade=t=out:st=1.1:d=0.4,volume=-24dB')
HS=V3+'/src-hot-swing-kevin-macleod.mp3'
snd('sting',['-ss','46.42','-t','1.6','-i',HS,'-af','afade=t=in:d=0.02,afade=t=out:st=0.9:d=0.7,volume=-6dB'])
snd('reprise',['-ss','34.87','-i',HS,'-af','afade=t=in:d=0.4,volume=-3dB'])
EL=SRC+'/Local Forecast - Elevator.mp3'
if os.path.exists(EL): snd('jingle',['-ss','0','-t','11.8','-i',EL,'-af','afade=t=in:d=0.15,afade=t=out:st=11.0:d=0.8,volume=-9dB'])
print(sorted(os.listdir(O)),sorted(os.listdir(X)))
