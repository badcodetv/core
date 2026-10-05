#!/usr/bin/env python3
"""Money For Something, storyboard v3 (the side branch): the graphics the v3 assembly needs. 1280x720 / 24 fps, into clips/_v3/.
Same typeface and year slot as build-cut2-media.py, so they sit beside cut 3's cards. Skips what exists.
Cards (years later, round names, advert bumpers), two quote cards, four pictures with a price tag, two flashes,
and the advert's four text shots cut from the two Flow clips (those need videos/v3/v3-ad-0*.mp4 to exist)."""
import os,subprocess,tempfile
P='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something'
C=P+'/clips'; O=C+'/_v3'; G=C+'/v3-graphics-src'; V=P+'/videos/v3'; os.makedirs(O,exist_ok=True)
B='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'; R='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
ENC=['-an','-r','24','-c:v','libx264','-crf','16','-preset','medium','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv']
T=tempfile.mkdtemp(); K=[0]
def tf(s):
    K[0]+=1; p=f'{T}/{K[0]}.txt'; open(p,'w').write(s); return p
def dt(text,size,x,y,font=B,color='white',box=False):
    b=":box=1:boxcolor=black@0.55:boxborderw=14" if box else ""
    return f"drawtext=fontfile={font}:textfile={tf(text)}:fontcolor={color}:fontsize={size}:x={x}:y={y}{b}"
YEAR=lambda t: dt(t,34,48,'h-96',box=True)
def tag(lines,x,y,size=40,pad=26,gap=12,w=None):
    """A manila luggage tag: a brown card with a darker edge, a punched hole and dark type. lines: [(text, size or None)]."""
    hs=[(s or size) for _,s in lines]; h=sum(hs)+gap*(len(lines)-1)+pad*2
    w=w or int(max(len(t)*(s or size)*0.57 for t,s in lines))+pad*2+46
    f=[f"drawbox=x={x+6}:y={y+8}:w={w}:h={h}:color=black@0.45:t=fill",f"drawbox=x={x}:y={y}:w={w}:h={h}:color=0xC8A46E:t=fill",
       f"drawbox=x={x}:y={y}:w={w}:h={h}:color=0x6B4A22:t=4",f"drawbox=x={x+16}:y={y+h//2-9}:w=18:h=18:color=0x1c130a:t=fill"]
    yy=y+pad
    for (t,s),hh in zip(lines,hs): f.append(dt(t,hh,x+52,yy,color='0x24160a')); yy+=hh+gap
    return ','.join(f)
def out(name): return f'{O}/{name}.mp4'
def card(name,dur,lines):
    if os.path.exists(out(name)): return
    d=','.join(dt(t,sz,'(w-text_w)/2',y,font=f) for t,sz,y,f in lines)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-f','lavfi','-i',f'color=c=black:s=1280x720:r=24:d={dur}','-vf',d+',format=yuv420p']+ENC+[out(name)],check=True); print('card',name)
def still(name,src,dur,extra,crop=None,ybias=0.5,zoom=0.05,dim=None):
    if os.path.exists(out(name)): return
    n=int(round(dur*24)); c=(f"crop={crop}," if crop else "")
    e=(f"eq=brightness={dim}:saturation=0.6," if dim else "")
    vf=(f"{c}scale=2560:1440:force_original_aspect_ratio=increase,crop=2560:1440:(iw-2560)/2:(ih-1440)*{ybias},"
        f"zoompan=z='1+{zoom}*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1280x720:fps=24,{e}{extra},format=yuv420p")
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',src,'-vf',vf,'-frames:v',str(n)]+ENC+[out(name)],check=True); print('still',name)
def over(name,src,ss,dur,extra):
    if os.path.exists(out(name)) or not os.path.exists(src): return
    subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(ss),'-t',str(dur),'-i',src,'-vf',f"scale=1280:720,fps=24,{extra},format=yuv420p"]+ENC+[out(name)],check=True); print('over',name)
for n,t in [('y1','ONE YEAR LATER'),('y7','SEVEN YEARS LATER'),('y10','TEN YEARS LATER')]: card(f'c-{n}',1.0,[(t,72,310,B)])
for n,t in [('pw','THE PRICE IS WAR'),('qu','QUOTE, UNQUOTE')]: card(f'c-{n}',1.2,[(t,84,300,B)])
# 5 Oct, the full cut: the Price Is War card carries its round number (the old one sat between ROUND 1 and ROUND 3),
# and the Keynes card that opens the round does not give the answer away.
card('c-r2-pw',1.4,[('ROUND 2',44,262,B),('THE PRICE IS WAR',84,330,B)])
card('q-keynes-ask',5.0,[('“Capitalism is the extraordinary belief',40,190,B),('that the nastiest of men, for the nastiest of motives,',40,244,B),('will somehow work together',40,298,B),('for the benefit of all.”',40,352,B),('WHO SAID IT?',26,446,B)])
card('c-ad-in',0.9,[('BACK AFTER THIS',64,315,B)]); card('c-ad-out',0.9,[('AND WE’RE BACK',64,315,B)])
card('q-lloyd-george',3.6,[('“What is our task? To make Britain',46,236,B),('a fit country for heroes to live in.”',46,296,B),('DAVID LLOYD GEORGE, PRIME MINISTER',26,396,B),('Wolverhampton  ·  November 1918',26,436,R)])
card('q-keynes',5.0,[('“Capitalism is the extraordinary belief',40,190,B),('that the nastiest of men, for the nastiest of motives,',40,244,B),('will somehow work together',40,298,B),('for the benefit of all.”',40,352,B),('ATTRIBUTED TO J. M. KEYNES',26,446,B)])
still('g-petrograd-1917',f'{G}/petrograd-1917-july-days-bulla.png',2.0,YEAR('PETROGRAD, 1917'),crop='iw-80:ih-60:40:30')
still('t-debt',f"{C}/s05-can-we-afford-it/The British sovereign will win. Invest in the war loan to-day LCCN2003668435.jpg",6.6,
      tag([('THE NATIONAL DEBT',30),('1914: ABOUT £650 MILLION',40),('1919: ABOUT £7.4 BILLION',40)],590,440)+','+YEAR('1915'),ybias=0.45,zoom=0.04,dim=-0.12)
still('f-northern-rock',f'{C}/s09-sound-off/Northern Rock Queue.jpg',1.0,YEAR('NORTHERN ROCK, 2007'),ybias=0.38,zoom=0.03)
still('t-iraq',f'{G}/times-atlas-1920-asia-minor-syria-mesopotamia.jpg',8.5,
      tag([('IRAQ, 1920',30),('£40 MILLION',56)],90,120)+','+YEAR('MESOPOTAMIA, 1920'),crop='1640:922:2150:1150',zoom=0.10)
still('f-farage',f'{G}/farage-official-portrait-2024-crop1.jpg',1.5,
      tag([('NIGEL FARAGE’S PARTY',30),('£72 MILLION',56),('TWO BUYERS. ONE DAY.',30)],700,400)+','+YEAR('2026'),crop='1820:1024:0:120',ybias=0.5,zoom=0.03)
AD1=f'{V}/v3-ad-01-rope.mp4'; AD2=f'{V}/v3-ad-02-yacht.mp4'
over('ad-a-headline',AD1,0.5,2.4,dt('KNOW A MINISTER?',70,'(w-text_w)/2',250,box=True)+','+dt('SKIP THE QUEUE.',70,'(w-text_w)/2',350,box=True))
over('ad-b-gowns',AD1,2.9,2.4,tag([('25 MILLION GOWNS THE NHS COULD NOT USE',26),('£122 MILLION',56)],60,470))
over('ad-c-profit',AD1,5.3,2.4,tag([('PROFIT, AS REPORTED BY THE GUARDIAN',26),('£65 MILLION',56)],60,470))
over('ad-d-yacht',AD2,1.0,2.6,tag([('ONE YACHT',26),('ABOUT £6 MILLION',56)],60,470))
print(sorted(os.listdir(O)))
