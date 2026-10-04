#!/usr/bin/env python3
"""Money For Something, cut 2: the media the timeline is laid from. Everything is 1280x720 / 24 fps.
- clips/_cut2/: archive pictures with the year burned into one fixed slot, round title cards, the May quote card.
- videos/leveled/L-<clip>.mp4: each room clip with its sound lifted so its peak sits at -3 dB (picture untouched).
- clips/_cut2/roomtone.wav: the studio hum, looped, to lie under the whole film.
Skips what exists."""
import os,subprocess,re,tempfile
P='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something'
C=P+'/clips'; O=C+'/_cut2'; V=P+'/videos'; L=V+'/leveled'
for d in (O,L): os.makedirs(d,exist_ok=True)
B='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'; R='/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'
ENC=['-an','-r','24','-c:v','libx264','-crf','16','-preset','medium','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv']
T=tempfile.mkdtemp()
def tf(s):
    p=f'{T}/{abs(hash(s))}.txt'; open(p,'w').write(s); return p
def dt(text,size,x,y,font=B,box=True):
    b=":box=1:boxcolor=black@0.55:boxborderw=14" if box else ""
    return f"drawtext=fontfile={font}:textfile={tf(text)}:fontcolor=white:fontsize={size}:x={x}:y={y}{b}"
YEAR=lambda t: dt(t,34,48,'h-96')            # the one fixed slot: bottom left
def run(vf,out,inp,n=None,pre=[]):
    cmd=['ffmpeg','-y','-loglevel','error']+pre+['-i',inp,'-vf',vf]+(['-frames:v',str(n)] if n else [])+ENC+[out]
    subprocess.run(cmd,check=True)
def still(name,src,dur,year,ybias=0.5):
    out=f'{O}/{name}.mp4'
    if os.path.exists(out): return
    n=int(round(dur*24))
    vf=(f"scale=2560:1440:force_original_aspect_ratio=increase,crop=2560:1440:(iw-2560)/2:(ih-1440)*{ybias},"
        f"zoompan=z='1+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1280x720:fps=24,{YEAR(year)},format=yuv420p")
    run(vf,out,f'{C}/{src}',n); print('still',name)
def film(name,src,ss,dur,year,ybias=0.35):
    out=f'{O}/{name}.mp4'
    if os.path.exists(out): return
    # the conformed masters are 4:3 pictures inside a wider frame: take the middle 4:3, then fill 16:9
    vf=f"scale='trunc(iw*sar/2)*2':ih,setsar=1,crop='min(iw,ih*4/3)':ih,scale=1280:-2,crop=1280:720:0:(ih-720)*{ybias},setsar=1,fps=24,{YEAR(year)},format=yuv420p"
    run(vf,out,f'{C}/{src}',pre=['-ss',str(ss),'-t',str(dur)]); print('film',name)
def card(name,dur,lines,src=None,dim=-0.42):
    out=f'{O}/{name}.mp4'
    if os.path.exists(out): return
    d=','.join(dt(t,sz,'(w-text_w)/2',y,font=f,box=False) for t,sz,y,f in lines)
    if src:
        vf=f"scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,eq=brightness={dim}:saturation=0.25,{d},format=yuv420p"
        run(vf,out,f'{C}/{src}',pre=['-loop','1','-t',str(dur)])
    else:
        subprocess.run(['ffmpeg','-y','-loglevel','error','-f','lavfi','-i',f'color=c=black:s=1280x720:r=24:d={dur}','-vf',d+',format=yuv420p']+ENC+[out],check=True)
    print('card',name)
MAY='s01-cold-open/Theresa May 2017 election speech outside 10 Downing Street.jpg'
card('g01-may-quote',5.0,[('“There isn’t a magic money tree.”',62,250,B),('THERESA MAY, PRIME MINISTER',26,360,B),('to a nurse asking about her pay  ·  2 June 2017',26,400,R)],src=MAY)
still('g01-may-2016','s01-cold-open/Theresa May (2016).jpg',4.7,'2017',ybias=0.12)
for n,t in [('r1','ROUND 1'),('r2','ROUND 2'),('r3','ROUND 3'),('qf','QUICK-FIRE'),('sp','THE STAR PRIZE'),('so','SOUND OFF'),('fs','FINAL SCORES')]:
    card(f'c-{n}',1.2,[(t,84,300,B)])
still('g04a-kitchener','s04-how-did-it-start/30a Sammlung Eybl Großbritannien. Alfred Leete (1882–1933) Britons (Kitchener) wants you (Briten Kitchener braucht Euch). 1914 (Nachdruck), 74 x 50 cm. (Slg.Nr. 552).jpg',3.0,'1914',ybias=0.22)
film('g04b-somme-men-walking','s04-how-did-it-start/111-m-59-r3.picture-only.mov',86,3.0,'THE SOMME, 1916')
still('g04c-trench','s04-how-did-it-start/Lancashire Fusiliers trench Beaumont Hamel 1916.jpg',3.0,'THE SOMME, 1916')
still('g05a-war-loan-poster','s05-can-we-afford-it/The British sovereign will win. Invest in the war loan to-day LCCN2003668435.jpg',2.2,'1915',ybias=0.45)
still('g05b-shells','s05-can-we-afford-it/12 inch shells at Chilwell 1917 IWM Q 30041.jpg',2.3,'SHELL FACTORY, 1917')
still('g05c-shell-warehouse','s05-can-we-afford-it/Munition workers in a shell warehouse at National Shell Filling Factory No.6, Chilwell, Nottinghamshire in 1917. Q30018.jpg',2.2,'SHELL FACTORY, 1917')
film('g06a-PLACEHOLDER-men-resting','s04-how-did-it-start/111-m-59-r3.picture-only.mov',476,4.3,'1919')
still('g06b-PLACEHOLDER-1931-unemployed','s07-quick-fire/7-10-31, manifestation des chômeurs à Londres (CNews) - btv1b53249445h.jpg',4.3,'1921',ybias=0.35)
still('g07a-berlin-1923','s07-quick-fire/Berlin - la foule assiège la voiture d\'un boulanger et se dispute le pain à coup de millions de Marks - btv1b9024458p.jpg',1.9,'GERMANY, 1923')
still('g07b-london-1931','s07-quick-fire/7-10-31, manifestation des chômeurs à Londres (arrestation d\'une femme) (CNews) - btv1b532494442.jpg',2.0,'BRITAIN, 1931',ybias=0.35)
film('g07c-1939-b','s07-quick-fire/gov.fdr.25.2.picture-only.mov',702,3.0,'1939.  AND THE MONEY WAS FOUND.')
still('g08a-guardsmen-building','s08-plant/Post War Planning and Reconstruction in Britain- Grenadier Guardsmen Build Emergency Housing in Windsor D25712.jpg',4.6,'BRITAIN, 1948',ybias=0.6)
film('g08b-new-town-houses-b','s08-plant/new_town_TNA.picture-only.mov',384,5.0,'BRITAIN, 1948')
film('g08c-hospital-b','s08-plant/your_very_good_health_TNA.picture-only.mov',376,5.0,'BRITAIN, 1948')
film('g08d-houses-b','s08-plant/your_very_good_health_TNA.picture-only.mov',36,4.6,'BRITAIN, 1948')
still('g09a-2008','s09-sound-off/Lehman Brothers-NYC-20080915.jpg',1.6,'2008')
still('g09b-2010','s09-sound-off/Budget 2014; Chancellor George Osborne delivering his Budget Statement.jpg',1.6,'2010')
still('g09c-2020','s09-sound-off/10 Downing Street COVID-19 press conference, 20 March 2020.png',1.8,'2020')
still('g10a-may-2017',MAY,2.0,'2017')
card('g10b-caption-dup',3.6,[('24 days later',40,270,R),('£1 billion for the DUP',72,330,B)],src=MAY)
# room clips, levelled
for l in open(os.path.dirname(os.path.abspath(__file__))+'/clips.tsv'):
    n=l.split('\t')[0].strip()
    if not n: continue
    src=f'{V}/{n}.mp4'; out=f'{L}/L-{n}.mp4'
    if os.path.exists(out): continue
    has=subprocess.run(['ffprobe','-v','error','-select_streams','a','-show_entries','stream=index','-of','csv=p=0',src],capture_output=True,text=True).stdout.strip()
    if not has:
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i',src,'-c','copy',out],check=True); continue
    r=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',src,'-af','volumedetect','-vn','-f','null','-'],capture_output=True,text=True).stderr
    mx=float(re.search(r'max_volume: (-?[0-9.]+)',r).group(1)); g=min(-3.0-mx,12.0) if mx>-30 else 7.0
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',src,'-c:v','copy','-af',f'volume={g:.1f}dB','-c:a','aac','-b:a','192k',out],check=True); print('level',n,f'{g:+.1f} dB')
rt=f'{O}/roomtone.wav'
if not os.path.exists(rt):
    subprocess.run(['ffmpeg','-y','-loglevel','error','-ss','2','-t','4','-i',f'{V}/s04-08-politician-watch.mp4','-af','volume=7dB,afade=t=in:d=0.5,afade=t=out:st=3.5:d=0.5,aloop=loop=60:size=192000,atrim=0:215','-ar','48000','-ac','2',rt],check=True); print('roomtone')
