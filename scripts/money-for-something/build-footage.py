#!/usr/bin/env python3
"""Money For Something: render every narrator-section picture as its own 1280x720 / 24 fps silent clip, so the
Premiere cut is laid from clips of one size. A still gets a slow push-in (a camera-only move is an ffmpeg job);
a film excerpt is cut and cropped to fill. Skips what exists. Output: <project>/clips/_cut/."""
import os,subprocess,sys
P='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something'
C=P+'/clips'; O=C+'/_cut'; os.makedirs(O,exist_ok=True)
ENC=['-an','-r','24','-c:v','libx264','-crf','16','-preset','medium','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv']
def still(name,src,dur,mode='cover',ybias=0.5):
    out=f'{O}/{name}.mp4'
    if os.path.exists(out): return
    n=int(round(dur*24))
    if mode=='cover': pre=f"scale=2560:1440:force_original_aspect_ratio=increase,crop=2560:1440:(iw-2560)/2:(ih-1440)*{ybias}"
    else: pre="scale=2560:1440:force_original_aspect_ratio=decrease,pad=2560:1440:(ow-iw)/2:(oh-ih)/2:black"
    vf=f"{pre},zoompan=z='1+0.05*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1280x720:fps=24,format=yuv420p,scale=out_range=tv"
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{C}/{src}','-vf',vf,'-frames:v',str(n)]+ENC+[out],check=True); print('still',name)
def film(name,src,ss,dur,ybias=0.35):
    out=f'{O}/{name}.mp4'
    if os.path.exists(out): return
    vf=f"scale=1280:-2,crop=1280:720:0:(ih-720)*{ybias},fps=24,format=yuv420p"
    subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',str(ss),'-t',str(dur),'-i',f'{C}/{src}','-vf',vf]+ENC+[out],check=True); print('film',name)
def caption(name,src,dur,lines):
    out=f'{O}/{name}.mp4'
    if os.path.exists(out): return
    n=int(round(dur*24)); F='/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'
    dt=','.join(f"drawtext=fontfile={F}:text='{t}':fontcolor=white:fontsize={sz}:x=(w-text_w)/2:y={y}" for t,sz,y in lines)
    vf=f"scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,eq=brightness=-0.35:saturation=0.3,{dt},format=yuv420p"
    subprocess.run(['ffmpeg','-y','-loglevel','error','-loop','1','-t',str(dur),'-i',f'{C}/{src}','-vf',vf]+ENC+[out],check=True); print('caption',name)
MAY17='s01-cold-open/Theresa May 2017 election speech outside 10 Downing Street.jpg'
still('f01a-may-2017','%s'%MAY17,3.0)
still('f01b-may-2016','s01-cold-open/Theresa May (2016).jpg',4.7,ybias=0.12)
still('f04a-kitchener','s04-how-did-it-start/30a Sammlung Eybl Großbritannien. Alfred Leete (1882–1933) Britons (Kitchener) wants you (Briten Kitchener braucht Euch). 1914 (Nachdruck), 74 x 50 cm. (Slg.Nr. 552).jpg',2.2,'fit')
still('f04b-britain-needs-you','s04-how-did-it-start/Britain Needs You at Once - WWI recruitment poster - Parliamentary Recruiting Committee Poster No. 108.jpg',1.6,'fit')
film('f04c-somme-men-walking','s04-how-did-it-start/111-m-59-r3.picture-only.mov',86,2.6)
still('f04d-trench','s04-how-did-it-start/Lancashire Fusiliers trench Beaumont Hamel 1916.jpg',2.6)
still('f05a-war-loan-poster','s05-can-we-afford-it/The British sovereign will win. Invest in the war loan to-day LCCN2003668435.jpg',2.2,'fit')
still('f05b-shells','s05-can-we-afford-it/12 inch shells at Chilwell 1917 IWM Q 30041.jpg',2.2)
still('f05c-shell-warehouse','s05-can-we-afford-it/Munition workers in a shell warehouse at National Shell Filling Factory No.6, Chilwell, Nottinghamshire in 1917. Q30018.jpg',2.3)
film('f06a-PLACEHOLDER-somme-men-resting','s04-how-did-it-start/111-m-59-r3.picture-only.mov',610,3.0)
film('f06b-PLACEHOLDER-1949-queue','s07-quick-fire/what_a_life_TNA.picture-only.mov',169,2.7)
still('f06c-PLACEHOLDER-1931-unemployed','s07-quick-fire/7-10-31, manifestation des chômeurs à Londres (CNews) - btv1b53249445h.jpg',2.9,ybias=0.35)
still('f07a-berlin-bread-van-1923','s07-quick-fire/Berlin - la foule assiège la voiture d\'un boulanger et se dispute le pain à coup de millions de Marks - btv1b9024458p.jpg',2.0)
still('f07b-london-unemployed-1931','s07-quick-fire/7-10-31, manifestation des chômeurs à Londres (arrestation d\'une femme) (CNews) - btv1b532494442.jpg',2.0,ybias=0.35)
film('f07c-next-war-paratroops','s07-quick-fire/gov.fdr.25.2.picture-only.mov',702,2.8)
film('f08a-new-town-houses','s08-plant/new_town_TNA.picture-only.mov',384,3.0)
still('f08b-guardsmen-building','s08-plant/Post War Planning and Reconstruction in Britain- Grenadier Guardsmen Build Emergency Housing in Windsor D25712.jpg',2.6,'fit')
film('f08c-houses-cartoon','s08-plant/your_very_good_health_TNA.picture-only.mov',30,3.0)
film('f08d-new-town-roads','s08-plant/new_town_TNA.picture-only.mov',440,3.0)
film('f08e-hospital-cartoon','s08-plant/your_very_good_health_TNA.picture-only.mov',376,3.0)
still('f08f-repairing-housing','s08-plant/Post War Planning and Reconstruction in Britain- Repairing Bomb Damaged Housing D24219.jpg',2.2,'fit')
still('f08g-training','s08-plant/Technical School- Training at Tottenham Polytechnic, Middlesex, England, UK, 1944 D21395.jpg',2.4,'fit')
still('f09a-lehman-2008','s09-sound-off/Lehman Brothers-NYC-20080915.jpg',2.4)
still('f09b-budget-2014','s09-sound-off/Budget 2014; Chancellor George Osborne delivering his Budget Statement.jpg',1.7)
still('f09c-press-conference-2020','s09-sound-off/10 Downing Street COVID-19 press conference, 20 March 2020.png',1.3)
still('f10a-may-2017','%s'%MAY17,2.2)
caption('f10b-caption-dup','%s'%MAY17,4.0,[('24 days later',44,270),('£1 billion for the DUP',72,340)])
