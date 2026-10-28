#!/usr/bin/env python3
"""Money For Something, the topical monologue (10 Oct 2026): first cut, built in ffmpeg.
For every clip in PLAN: trim to the speech (clips are made longer than the line on purpose), put a picture or a card
inside the host's television (fixed mask, the camera never moves), optionally cut to the same card full screen while he
keeps talking, level the voice, then join everything and add a credits card for every picture that owes one.
Per-clip files go to <root>/clips/ so the cut can be rebuilt by hand in Premiere; the joined cut goes to <root>/renders/.
usage: python3 build-topical-cut.py "MFS topical cut 3"     (the last word of the name becomes the clip prefix, c3-)
Before it: topical-words-json.py (every word's time). After it: topical-verify.py "<name>" (every script line heard?).
Cut 3 (11 Oct): Jack on cut 2, "there is too much dead air, the jokes need to be quick for them to land, only have pauses for
comedic effect, but the sentences have to flow and be natural". So from cut 3 the clip is not one window but a list of kept
ranges: the head and tail are cut close to the speech and every pause inside a line is shortened (see keeps()). The cards are
the third style (build-topical-cards3.py, screen/cards3)."""
import os,re,subprocess,sys,json,tempfile,csv
H=os.path.dirname(os.path.abspath(__file__))
P='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something'
V=P+'/videos'; SC=P+'/screen'; CL=P+'/clips/'+(sys.argv[1].replace(' ','-') if len(sys.argv)>1 else 'cut2'); RN=P+'/renders'
for d in (CL,RN): os.makedirs(d,exist_ok=True)
TAG='c'+(sys.argv[1].split()[-1] if len(sys.argv)>1 else '2')
K=H+'/topical-screen'; X,Y,W,Hh=map(int,open(K+'/bbox.txt').read().split())
MAN=os.path.join(H,'..','..','docs','stories','magic-money-tree','money-for-something-screen-sources.md')
F=H+'/fonts/Inter.ttf'; CARDS='cards3'
ENC=['-r','24','-c:v','libx264','-crf','17','-preset','medium','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv','-c:a','aac','-b:a','192k','-ar','48000','-ac','2']
# clip: (what is in the television or None, (full-screen card, from, to as fractions of the trimmed clip) or None)
PLAN={
 't-01a':(CARDS+'/c01a.mp4',None),
 't-01b':('b01/b01-burnham-arrives-no10.jpg',(CARDS+'/c01b.mp4',.50,.95)),
 't-01c':('b01/b01-google-homepage-1998.png',None),
 't-02a':('b02/b02-clap-street-budd.jpg',(CARDS+'/c02a.mp4',.55,.88)),
 't-03a':('b03/b03-thaad-launch-video.mp4',(CARDS+'/c03a.mp4',.30,.62)),
 't-03b':('b02/b02-nurse-donna-wood-dfid.jpg',None),
 't-03c':('b03/b03-st-thomas-hospital-apk.jpg',None),
 't-04a':('b04/b04-trump-oval-office-aug-2026.jpg',(CARDS+'/c04a.mp4',.08,.55)),
 't-04b':('b04/b04-butler-rally-2024-stage.jpg',None),
 't-04c':('b04/b04-bunker-cheyenne-blast-door.jpg',None),
 't-05a':('b05/b05-hsbc-barclays-hailsham.jpg',(CARDS+'/c05a.mp4',.10,.95)),
 't-05b':(CARDS+'/c05b.mp4',None),
 't-06a':('b06/b06-musk-cabinet-meeting.jpg',(CARDS+'/c06a.mp4',.50,.95)),
 't-06b':('b06/b06-musk-oval-office-2025.jpg',None),
 't-06c':(CARDS+'/c99.mp4',None),
 't-07a':('b07/b07-andrew-chatham-house-2017.jpg',(CARDS+'/c07a.mp4',.50,.95)),
 't-07b':(CARDS+'/c07a.mp4',None),
 't-08a':('b08/b08-bezos-laugh-jurvetson.jpg',(CARDS+'/c08a.mp4',.55,.95)),
 't-08b':('b08/b08-marseille-protest-fire-2023.jpg',None),
 't-08c':(CARDS+'/c08c.mp4',None),
 't-09a':(CARDS+'/c09a.mp4',(CARDS+'/c09a.mp4',.05,.42)),
 't-10a':('b10/b10-farage-official-portrait-crop.jpg',(CARDS+'/c10a.mp4',.12,.95)),
 't-10b':(CARDS+'/c10b.mp4',(CARDS+'/c10b.mp4',.55,.95)),
 't-11a':('b11/b11-blackburn-town-hall-green.jpg',(CARDS+'/c11a.mp4',.10,.45)),
 't-12a':(CARDS+'/c12a.mp4',None),
 't-12b':('b12/b12-trump-fast-food-clemson-2019.jpg',None),
 't-12c':(None,None),
 't-12d':(None,None),
}
# per-clip files carry uncompressed sound: Premiere played two of cut 3's 29 AAC .mp4 clips silent (01b, 06b), and one of cut 1's,
# though every file decodes fine in ffmpeg. The same two clips with PCM sound in a .mov played. Cause not known. The joined render stays AAC.
CLIP=[x if x!='aac' else 'pcm_s16le' for x in ENC if x not in ('-b:a','192k')]
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
    if src.startswith(CARDS+'/'): return ['-i',p]            # an animated card: 12 s long, plays once from the top
    return ['-stream_loop','-1','-i',p] if p.endswith('.mp4') else ['-loop','1','-t',f'{t:.3f}','-i',p]
WJ=json.load(open(H+'/topical-words.json')) if os.path.exists(H+'/topical-words.json') else {}
HEAD=0.07; TAIL=0.14; TAIL_BEAT=0.32      # air before the first word, after the last, and after the last word of a beat
SENT=0.30; COMMA=0.17                     # the longest pause left after a full stop, and anywhere else inside a line
# pauses kept longer on purpose, because the pause is the joke or the turn: (clip, the word before the pause) -> seconds
PAUSE={('t-01a','out.'):0.50,('t-02a','week.'):0.50,('t-04a','way.'):0.60,('t-04a','something.'):0.42,('t-05b','flourishing.'):0.60,
       ('t-06c','job.'):0.40,('t-07a','nonces.'):0.45,('t-07b','bill?'):0.65,('t-07b','please.'):0.45,('t-11a','joke.'):0.45,('t-12a','economics.'):0.70}
HISS={'t-05a','t-05b'}                     # measured 11 Oct; not applied to every clip because it would shave soft first words (01a, 07b)
WHOLE={'t-12d':(1.6,10.01)}               # the silent ending: he sits for a second and a half before anything happens
def keeps(f,name,beat_end):
    """The ranges of a raw clip to keep, in source seconds. Silence is measured (silencedetect); the speech model's word list says
    which silence is the end of the line (so crowd noise Flow added after it goes) and what kind of pause each one is.
    A pause is only shortened, never removed, and it is cut out of its middle so no word loses its start or its tail."""
    d=dur(f); J=WJ.get(name)
    if name in WHOLE: return [(WHOLE[name][0],min(d,WHOLE[name][1]))]
    if not J or not J['words']: return [(0.0,d)]
    e=subprocess.run(['ffmpeg','-v','info','-i',f,'-af','silencedetect=noise=-34dB:d=0.2','-f','null','-'],capture_output=True,text=True).stderr
    st=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',e)]; en=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',e)]
    sil=list(zip(st,en+[d]*(len(st)-len(en)))); ws=J['words']; lastw=ws[-1][2]
    begin=max(0.0,sil[0][1]-HEAD) if sil and sil[0][0]<0.05 else 0.0
    if name in HISS: begin=max(begin,onset(f)-0.09)   # these open on a second of faint hiss that silencedetect does not call silence
    end=d
    for a,b in sil:
        if a>=lastw-0.30: end=min(d,a+(TAIL_BEAT if beat_end else TAIL)); break
    out=[]; cur=begin
    for a,b in sil:
        if a<=begin+0.1 or b>=end-0.05: continue
        prev=[w for w in ws if w[1]<a+0.1]; pw=prev[-1][0] if prev else ''
        allow=PAUSE.get((name,pw),SENT if pw[-1:] in '.?!' else COMMA)
        if b-a>allow+0.06: out.append((cur,a+allow*0.4)); cur=b-allow*0.6
    out.append((cur,end)); return out
def onset(f):
    """When the voice starts: the first 20 ms of the clip at -30 dBFS or louder that is followed by another."""
    import numpy as np
    x=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',f,'-vn','-ac','1','-ar','16000','-f','s16le','-']),dtype=np.int16).astype(float)/32768
    n=len(x)//320; r=20*np.log10(np.sqrt((x[:n*320].reshape(n,320)**2).mean(1))+1e-9); hot=np.where((r[:-1]>-30)&(r[1:]>-30))[0]
    return float(hot[0])*0.02 if len(hot) else 0.0
def at_new(ranges,src_t):
    """A time in the raw clip -> the time in the tightened clip."""
    return sum(max(0.0,min(b,src_t)-a) for a,b in ranges)
OLD={r['clip']:(float(r['in']),float(r['length'])) for r in csv.DictReader(open(RN+'/MFS topical cut 2.tsv'),delimiter='\t')} if os.path.exists(RN+'/MFS topical cut 2.tsv') else {}
words={l.split('\t')[0]:int(l.split('\t')[4]) for l in open(H+'/clips-topical.tsv') if l.strip()}
parts=[]; used=[]; log=[]; order=list(PLAN)
for name,(tv,full) in PLAN.items():
    src=f'{V}/{name}.mp4'
    if not os.path.exists(src): print('MISSING',name); continue
    nxt=order[order.index(name)+1] if order.index(name)+1<len(order) else None
    R=keeps(src,name,nxt is None or nxt[:4]!=name[:4]); b,e=R[0][0],R[-1][1]; t=sum(z-a for a,z in R); out=f'{CL}/{TAG}-{name}.mov'   # unique names: Premiere matches items by name. .mov with PCM sound: see CLIP
    ins=['-i',src]; k=len(R)
    fc=[f"[0:v]split={k}"+''.join(f'[sv{i}]' for i in range(k)),f"[0:a]asplit={k}"+''.join(f'[sa{i}]' for i in range(k))]
    for i,(a,z) in enumerate(R):
        fc.append(f"[sv{i}]trim=start={a:.3f}:end={z:.3f},setpts=PTS-STARTPTS[kv{i}]")
        fc.append(f"[sa{i}]atrim=start={a:.3f}:end={z:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={max(0,z-a-0.012):.3f}:d=0.012[ka{i}]")
    fc.append(''.join(f'[kv{i}][ka{i}]' for i in range(k))+f"concat=n={k}:v=1:a=1[bv][ba]"); last='bv'; n=1
    sc=screen_of(src,b+min(1.0,t/2)) if tv else None
    if tv and sc:
        X,Y,W,Hh,mf=sc
        ins+=scr(tv,t)+['-i',mf]; used.append(tv)
        fc.append(f"[{n}:v]scale={W}:{Hh}:force_original_aspect_ratio=increase,crop={W}:{Hh},setsar=1,gblur=sigma=0.7,eq=saturation=1.12:contrast=1.04,drawgrid=w={W}:h=3:t=1:c=black@0.16,pad=1280:720:{X}:{Y},format=rgb24[c];[{n+1}:v]format=gray[m];[c][m]alphamerge[ca];[{last}][ca]overlay=shortest=1[v1]")
        last='v1'; n+=2
    if full:
        card,a,z=full; used.append(card)
        if name in OLD:      # the fractions were set against cut 2's window; keep each cutaway on the same words
            a,z=at_new(R,OLD[name][0]+a*OLD[name][1]),min(t-0.04,at_new(R,OLD[name][0]+z*OLD[name][1]))
        else: a,z=a*t,z*t
        ins+=['-itsoffset',f'{a:.3f}','-i',SC+'/'+card]                                         # the card's animation starts when the cutaway does
        fc.append(f"[{n}:v]scale=1280:720,setsar=1[fu];[{last}][fu]overlay=enable='between(t,{a:.3f},{z:.3f})':eof_action=pass[v2]"); last='v2'; n+=1
    fc.append(f"[{last}]fps=24,format=yuv420p[v]")
    af="loudnorm=I=-16:TP=-1.5:LRA=11,afade=t=in:d=0.04,afade=t=out:st=%.3f:d=0.08"%(max(0,t-0.08)) if words.get(name,0) else "volume=0"
    fc.append(f"[ba]{af}[a]")
    run(['ffmpeg','-v','error','-y']+ins+['-filter_complex',';'.join(fc),'-map','[v]','-map','[a]','-t',f'{t:.3f}']+CLIP+[out])
    parts.append(out); log.append(f"{name}\t{b:.2f}\t{e:.2f}\t{t:.2f}\t{tv or '-'}\t{full[0] if full else '-'}\t{' '.join(f'{a:.2f}-{z:.2f}' for a,z in R)}"); print(log[-1])
# credits owed by the pictures used, including the photo behind each card
if os.path.exists(H+f'/{CARDS}-photos.tsv'):
    back=dict(l.rstrip('\n').split('\t') for l in open(H+f'/{CARDS}-photos.tsv') if l.strip())
    used+=[back[os.path.basename(u)[:-4]] for u in list(used) if u.startswith(CARDS+'/') and os.path.basename(u)[:-4] in back]
cred=[]
if os.path.exists(MAN):
    for row in open(MAN):
        c=[x.strip() for x in row.split('|')]
        if len(c)>8 and any(os.path.basename(u)==c[2].strip('`') for u in used):
            s=c[7]
            if s and not s.startswith('None owed') and s not in cred: cred.append(s)
T=tempfile.mkdtemp(); lines=['PICTURES']+[re.sub(r'\s+',' ',c)[:92] for c in cred]+['','Contains public sector information licensed','under the Open Government Licence v3.0.','','A BADCODE transmission. Made with AI.']
tfp=T+'/cr.txt'; open(tfp,'w').write('\n'.join(lines))
crd=f'{CL}/{TAG}-t-99-credits.mov'
run(['ffmpeg','-v','error','-y','-f','lavfi','-i','color=black:s=1280x720:d=6','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-vf',f"drawtext=fontfile={F}:textfile={tfp}:fontcolor=white@0.85:fontsize=17:line_spacing=8:x=60:y=50",'-t','6']+CLIP+[crd]); parts.append(crd)
stem=sys.argv[1] if len(sys.argv)>1 else 'MFS topical cut 2'; final=f'{RN}/{stem}.mp4'
ins=[]; 
for p_ in parts: ins+=['-i',p_]
n_=len(parts); fc_=''.join(f'[{i}:v][{i}:a]' for i in range(n_))+f'concat=n={n_}:v=1:a=1[v][a]'
run(['ffmpeg','-v','error','-y']+ins+['-filter_complex',fc_,'-map','[v]','-map','[a]']+ENC+['-movflags','+faststart',final])
open(f'{RN}/{stem}.tsv','w').write('clip\tin\tout\tlength\ttelevision\tfull screen\tkept\n'+'\n'.join(log)+'\n')
print('CUT',final,'%.1f s'%dur(final),'parts',len(parts),'credits',len(cred))
