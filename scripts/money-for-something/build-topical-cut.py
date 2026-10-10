#!/usr/bin/env python3
"""Money For Something, the topical monologue (10 Oct 2026): first cut, built in ffmpeg.
For every clip in PLAN: trim to the speech (clips are made longer than the line on purpose), put a picture or a card
inside the host's television (fixed mask, the camera never moves), optionally cut to the same card full screen while he
keeps talking, level the voice, then join everything and add a credits card for every picture that owes one.
Per-clip files go to <root>/clips/ so the cut can be rebuilt by hand in Premiere; the joined cut goes to <root>/renders/.
usage: python3 build-topical-cut.py "MFS topical cut 3"     (the last word of the name becomes the clip prefix, c3-)
Before it: topical-words.py (word timings). After it: topical-verify.py "<name>" (every script line heard?)."""
import os,re,subprocess,sys,json,tempfile
H=os.path.dirname(os.path.abspath(__file__))
P='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something'
V=P+'/videos'; SC=P+'/screen'; CL=P+'/clips/'+(sys.argv[1].replace(' ','-') if len(sys.argv)>1 else 'cut2'); RN=P+'/renders'
for d in (CL,RN): os.makedirs(d,exist_ok=True)
TAG='c'+(sys.argv[1].split()[-1] if len(sys.argv)>1 else '2')
K=H+'/topical-screen'; X,Y,W,Hh=map(int,open(K+'/bbox.txt').read().split())
MAN=os.path.join(H,'..','..','docs','stories','magic-money-tree','money-for-something-screen-sources.md')
F='/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
ENC=['-r','24','-c:v','libx264','-crf','17','-preset','medium','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv','-c:a','aac','-b:a','192k','-ar','48000','-ac','2']
# clip: (what is in the television or None, (full-screen card, from, to as fractions of the trimmed clip) or None)
PLAN={
 't-01a':('cards2/c01a.mp4',None),
 't-01b':('b01/b01-burnham-arrives-no10.jpg',('cards2/c01b.mp4',.50,.95)),
 't-01c':('b01/b01-google-homepage-1998.png',None),
 't-02a':('b02/b02-clap-street-budd.jpg',('cards2/c02a.mp4',.55,.88)),
 't-03a':('b03/b03-thaad-launch-video.mp4',('cards2/c03a.mp4',.30,.62)),
 't-03b':('b02/b02-nurse-donna-wood-dfid.jpg',None),
 't-03c':('b03/b03-st-thomas-hospital-apk.jpg',None),
 't-04a':('b04/b04-trump-oval-office-aug-2026.jpg',('cards2/c04a.mp4',.08,.55)),
 't-04b':('b04/b04-butler-rally-2024-stage.jpg',None),
 't-04c':('b04/b04-bunker-cheyenne-blast-door.jpg',None),
 't-05a':('b05/b05-hsbc-barclays-hailsham.jpg',('cards2/c05a.mp4',.10,.95)),
 't-05b':('cards2/c05b.mp4',None),
 't-06a':('b06/b06-musk-cabinet-meeting.jpg',('cards2/c06a.mp4',.50,.95)),
 't-06b':('b06/b06-musk-oval-office-2025.jpg',None),
 't-06c':('cards2/c99.mp4',None),
 't-07a':('b07/b07-andrew-chatham-house-2017.jpg',('cards2/c07a.mp4',.50,.95)),
 't-07b':('cards2/c07a.mp4',None),
 't-08a':('b08/b08-bezos-laugh-jurvetson.jpg',('cards2/c08a.mp4',.55,.95)),
 't-08b':('b08/b08-marseille-protest-fire-2023.jpg',None),
 't-08c':('cards2/c08c.mp4',None),
 't-09a':('cards2/c09a.mp4',('cards2/c09a.mp4',.05,.42)),
 't-10a':('b10/b10-farage-official-portrait-crop.jpg',('cards2/c10a.mp4',.12,.95)),
 't-10b':('cards2/c10b.mp4',('cards2/c10b.mp4',.55,.95)),
 't-11a':('b11/b11-blackburn-town-hall-green.jpg',('cards2/c11a.mp4',.10,.45)),
 't-12a':('cards2/c12a.mp4',None),
 't-12b':('b12/b12-trump-fast-food-clemson-2019.jpg',None),
 't-12c':(None,None),
 't-12d':(None,None),
}
def run(a): subprocess.run(a,check=True)
def screen_of(src,at):
    """Where the blue television glass is in this clip (the camera is locked, so one frame is enough). Returns x,y,w,h and a mask file.
    Measured per clip, because a clip made in Ingredients mode is re-staged and its television sits somewhere else."""
    import numpy as np
    raw=subprocess.check_output(['ffmpeg','-v','error','-ss',f'{at:.2f}','-i',src,'-frames:v','1','-vf','scale=1280:720','-f','rawvideo','-pix_fmt','rgb24','-'])
    a=np.frombuffer(raw,dtype=np.uint8).reshape(720,1280,3).astype(int); r,g,b=a[...,0],a[...,1],a[...,2]
    m=(b>150)&(b-r>80)&(b-g>30); cx=np.where(m.sum(0)>50)[0]; cy=np.where(m.sum(1)>50)[0]
    if not len(cx) or not len(cy): return None
    x0,x1,y0,y1=cx.min(),cx.max(),cy.min(),cy.max(); mm=np.zeros((720,1280),np.uint8); mm[y0:y1+1,x0:x1+1]=m[y0:y1+1,x0:x1+1]*255
    mf=tempfile.mktemp(suffix='.png')
    subprocess.run(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','gray','-s','1280x720','-i','-','-vf','dilation,gblur=sigma=1.2','-frames:v','1',mf],input=mm.tobytes(),check=True)
    return int(x0),int(y0),int(x1-x0+1),int(y1-y0+1),mf
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).decode())
WORDS={l.split('\t')[0]:l.rstrip('\n').split('\t') for l in open(H+'/topical-words.tsv')} if os.path.exists(H+'/topical-words.tsv') else {}
def speech_window(f,name,words):
    """Where to cut a raw clip. Jack: "make the clips as long as they need to fit the dialogue ... then we can trim them after",
    so this errs long. Start: just before the first sound. End: if the local speech model heard every word of the script line
    (topical-words.tsv), a third of a second after its last word, which also cuts off any crowd noise Flow added after the line.
    If it missed a word, its timings cannot be trusted, so keep everything up to the clip's own closing silence.
    Cut 1 trusted Gemini's "last word" time instead and lost the end of seven lines."""
    d=dur(f)
    if not words: return 0.0,d
    e=subprocess.run(['ffmpeg','-v','info','-i',f,'-af','silencedetect=noise=-36dB:d=0.18','-f','null','-'],capture_output=True,text=True).stderr
    st=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',e)]; en=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',e)]
    begin=max(0.0,en[0]-0.15) if st and st[0]<0.05 and en else 0.0
    tail=st[-1] if len(st)>len(en) else d          # a silence that runs to the end of the clip
    end=min(d,tail+0.35)
    w=WORDS.get(name)
    if w and int(w[3])>=int(w[4]) and float(w[2])>0:
        end=min(d,float(w[2])+0.35); begin=min(begin,max(0.0,float(w[1])-0.15))
    return begin,end
def scr(src,t):
    """Input args + filter for one screen picture (still or video), filling the television's glass."""
    p=SC+'/'+src
    if src.startswith('cards2/'): return ['-i',p]            # an animated card: 12 s long, plays once from the top
    return ['-stream_loop','-1','-i',p] if p.endswith('.mp4') else ['-loop','1','-t',f'{t:.3f}','-i',p]
words={l.split('\t')[0]:int(l.split('\t')[4]) for l in open(H+'/clips-topical.tsv') if l.strip()}
parts=[]; used=[]; log=[]
for name,(tv,full) in PLAN.items():
    src=f'{V}/{name}.mp4'
    if not os.path.exists(src): print('MISSING',name); continue
    b,e=speech_window(src,name,words.get(name,0)); t=e-b; out=f'{CL}/{TAG}-{name}.mp4'   # unique names: Premiere matches items by name
    ins=['-ss',f'{b:.3f}','-t',f'{t:.3f}','-i',src]; fc=[]; last='0:v'; n=1
    sc=screen_of(src,b+min(1.0,t/2)) if tv else None
    if tv and sc:
        X,Y,W,Hh,mf=sc
        ins+=scr(tv,t)+['-i',mf]; used.append(tv)
        fc.append(f"[{n}:v]scale={W}:{Hh}:force_original_aspect_ratio=increase,crop={W}:{Hh},setsar=1,gblur=sigma=0.7,eq=saturation=1.12:contrast=1.04,drawgrid=w={W}:h=3:t=1:c=black@0.16,pad=1280:720:{X}:{Y},format=rgb24[c];[{n+1}:v]format=gray[m];[c][m]alphamerge[ca];[{last}][ca]overlay=shortest=1[v1]")
        last='v1'; n+=2
    if full:
        card,a,z=full; ins+=['-itsoffset',f'{a*t:.3f}','-i',SC+'/'+card]; used.append(card)   # the card's animation starts when the cutaway does
        fc.append(f"[{n}:v]scale=1280:720,setsar=1[fu];[{last}][fu]overlay=enable='between(t,{a*t:.3f},{z*t:.3f})':eof_action=pass[v2]"); last='v2'; n+=1
    fc.append(f"[{last}]fps=24,format=yuv420p[v]")
    af="loudnorm=I=-16:TP=-1.5:LRA=11,afade=t=in:d=0.04,afade=t=out:st=%.3f:d=0.08"%(max(0,t-0.08)) if words.get(name,0) else "volume=0"
    run(['ffmpeg','-v','error','-y']+ins+['-filter_complex',';'.join(fc),'-map','[v]','-map','0:a','-af',af,'-t',f'{t:.3f}']+ENC+[out])
    parts.append(out); log.append(f"{name}\t{b:.2f}\t{e:.2f}\t{t:.2f}\t{tv or '-'}\t{full[0] if full else '-'}"); print(log[-1])
# credits owed by the pictures used, including the photo behind each card
if os.path.exists(H+'/cards2-photos.tsv'):
    back=dict(l.rstrip('\n').split('\t') for l in open(H+'/cards2-photos.tsv') if l.strip())
    used+=[back[os.path.basename(u)[:-4]] for u in list(used) if u.startswith('cards2/') and os.path.basename(u)[:-4] in back]
cred=[]
if os.path.exists(MAN):
    for row in open(MAN):
        c=[x.strip() for x in row.split('|')]
        if len(c)>8 and any(os.path.basename(u)==c[2].strip('`') for u in used):
            s=c[7]
            if s and not s.startswith('None owed') and s not in cred: cred.append(s)
T=tempfile.mkdtemp(); lines=['PICTURES']+[re.sub(r'\s+',' ',c)[:92] for c in cred]+['','Contains public sector information licensed','under the Open Government Licence v3.0.','','A BADCODE transmission. Made with AI.']
tfp=T+'/cr.txt'; open(tfp,'w').write('\n'.join(lines))
crd=f'{CL}/{TAG}-t-99-credits.mp4'
run(['ffmpeg','-v','error','-y','-f','lavfi','-i','color=black:s=1280x720:d=6','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-vf',f"drawtext=fontfile={F}:textfile={tfp}:fontcolor=white:fontsize=17:line_spacing=7:x=60:y=50",'-t','6']+ENC+[crd]); parts.append(crd)
stem=sys.argv[1] if len(sys.argv)>1 else 'MFS topical cut 2'; final=f'{RN}/{stem}.mp4'
ins=[]; 
for p_ in parts: ins+=['-i',p_]
n_=len(parts); fc_=''.join(f'[{i}:v][{i}:a]' for i in range(n_))+f'concat=n={n_}:v=1:a=1[v][a]'
run(['ffmpeg','-v','error','-y']+ins+['-filter_complex',fc_,'-map','[v]','-map','[a]']+ENC+['-movflags','+faststart',final])
open(f'{RN}/{stem}.tsv','w').write('clip\tin\tout\tlength\ttelevision\tfull screen\n'+'\n'.join(log)+'\n')
print('CUT',final,'%.1f s'%dur(final),'parts',len(parts),'credits',len(cred))
