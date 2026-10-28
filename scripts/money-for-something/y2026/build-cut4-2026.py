#!/usr/bin/env python3
"""Money For Something 2026, cut 4 (14 Oct 2026): Jack on cut 3 wanted more footage and meme-like pictures on the television,
exciting stat cards, three lines fixed (y-16, y-18, y-20 remade). New here: the television can change picture on a word (TV list),
punch-ins on the deadpan tags (PUNCH), the fourth card style (build-cards4-2026.py, screen/cards4). Otherwise as cut 3.
Money For Something 2026, the year in news (14 Oct 2026): built in ffmpeg. Adapted from ../build-topical-cut.py (same method, 2026 paths, plan and pauses; the silent pint clips keep their sound).
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
P='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/2026'
V=P+'/videos'; SC=P+'/screen'; CL=P+'/clips/'+(sys.argv[1].replace(' ','-') if len(sys.argv)>1 else 'cut2'); RN=P+'/renders'
for d in (CL,RN): os.makedirs(d,exist_ok=True)
TAG='c'+(sys.argv[1].split()[-1] if len(sys.argv)>1 else '2')
MAN=os.path.join(H,'..','..','..','docs','stories','magic-money-tree','money-for-something-screen-sources.md')
F=H+'/../fonts/Inter.ttf'; CARDS='cards4'
ENC=['-r','24','-c:v','libx264','-crf','17','-preset','medium','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv','-c:a','aac','-b:a','192k','-ar','48000','-ac','2']
# clip: (what is in the television or None, (full-screen card, from, to as fractions of the trimmed clip) or None)
C=lambda c:CARDS+'/'+c+'.mp4'; ID=C('ident')
# clip: (what is in the television, (full-screen card, the word it arrives on, the word it leaves on or None for the end of the clip) or None)
# Cut 2: October's lesson from the shorts ("Expat lands on the word and not before it"): a cutaway starts on its word, and
# the face is back for the punchline.
O='../../october/screen/'; N='photos/'       # October's cleared pictures, and the 2026 ones (money-for-something-2026-screen-sources.md)
# Cut 3 (Jack: "add real footage/photos on the tv"): the television shows a real picture or clip wherever a free one exists;
# the stat card arrives full screen on its word, as in October.
PLAN={
 'y-00':(C('c00'),None),
 'y-01':(O+'b06/b06-epstein-mugshot-2019.png',(C('c01'),'thirtieth|30th','unrelated')),
 'y-02':(O+'b04/b04-destroyer-missile-launch-epic-fury-video.mp4',None),
 'y-03':(N+'p-xi-jinping-2025.jpg',(C('c03'),'petrol','xi')),
 'y-04':(N+'p-iran-1953-tehran-rally.jpg',(C('c04'),'nineteen|1953','they')),
 'y-05':(O+'b04/b04-trump-oval-office-aug-2026.jpg',(C('c05'),'whole',None)),       # cut 4 fix (Jack): Trump stays on screen for the whole quote
 'y-06':(O+'b04/b04-trump-situation-room.jpg',None),
 'y-07':(N+'p-cheney-rumsfeld.jpg',(C('c07'),'two|200','somewhere')),
 'y-08':(N+'p-helmand-patrol-2011.jpg',(C('c08'),'eight|8',None)),
 'y-09':(N+'p-helmand-patrol-2011.jpg',None),
 'y-10':(N+'p-taliban-humvee-kabul-2021.png',(C('c10'),'taliban',None)),
 'y-11':(N+'p-nuclear-baker-1946.jpg',(C('c11'),'three|3','maybe')),
 'y-12':(N+'p-nuclear-baker-1946.jpg',None),
 'y-13':(O+'b03/b03-thaad-launch-video.mp4',None),                 # cut 4: "these" = the missiles
 'y-14':([(N+'p-tanker-boarding-jan-2026.mp4',None),(N+'p-oil-pumpjack.jpg','oil'),(N+'p-toilet.jpg','shit'),(N+'p-toilet-2.jpg','different')],(C('c14'),'venezuela','blah')),
 'y-15':([(N+'p-wheelie-bins.jpg',None),(N+'p-clown.jpg','clown')],(C('c15'),'beat','whatever')),
 'y-16':(N+'g-tv-piddington.jpg',(C('c16'),'voted','government')),
 'y-17a':([(N+'p-helmand-patrol-2011.jpg',None),(O+'b04/b04-destroyer-missile-launch-epic-fury-video.mp4','remember')],None),
 'y-17b':(N+'g-tv-piddington.jpg',None),
 'y-18':([(N+'g-tv-piddington.jpg',None),(N+'p-hotel-corridor.jpg','three')],(C('c18'),'made',None)),
 'y-19':(N+'g-tv-mealdeals.jpg',None),
 'y-20':([(N+'p-ppe-mask-in-mud.jpg',None),(N+'p-ppe-warehouse-pallets.jpg','government')],(C('c20'),'ten|10','next')),
 'y-21a':([(N+'p-ppe-mask-in-mud.jpg',None),(N+'p-superyacht-bow.jpg','one')],None),
 'y-21b':(N+'p-superyachts-monaco.jpg',None),
 'y-22':(N+'p-euro-notes.jpg',(C('c22'),'told','would')),
 'y-23':(N+'p-hs2-wendover-2026.jpg',(C('c23'),'one|hundred|102','it')),
 'y-24':(N+'p-hs2-wendover-2026.jpg',None),
 'y-25':(N+'p-parliament-2022.jpg',(C('c25'),'6|six','how')),
 'y-26':(N+'p-disposable-barbecue.jpg',None),
 'y-27':([(N+'p-heat-low-reservoir-2026.jpg',None),(N+'p-disposable-barbecue.jpg','government'),(N+'p-pint.jpg','drank'),(N+'p-oil-tanker.jpg','oil')],None),
 'y-28':(ID,None),
 'y-29':(ID,None),
 'y-30':(ID,None),
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
    m=(b>150)&(b-r>80)&(b-g>30); m[:,:700]=False; m[520:,:]=False   # 2026 plate: the television is in the right half; the windows, the glass and the table carry the same blue
    sx,sy=m.sum(0),m.sum(1); cx=np.where(sx>max(50,0.5*sx.max()))[0]; cy=np.where(sy>max(50,0.5*sy.max()))[0]   # half the peak: the table in the 2026 plate reflects the same blue
    if not len(cx) or not len(cy): return None
    x0,x1,y0,y1=cx.min(),cx.max(),cy.min(),cy.max(); print('  screen',x0,y0,x1-x0+1,y1-y0+1); mm=np.zeros((720,1280),np.uint8); mm[y0:y1+1,x0:x1+1]=m[y0:y1+1,x0:x1+1]*255
    mf=tempfile.mktemp(suffix='.png')
    subprocess.run(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','gray','-s','1280x720','-i','-','-vf','dilation,gblur=sigma=1.2','-frames:v','1',mf],input=mm.tobytes(),check=True)
    return int(x0),int(y0),int(x1-x0+1),int(y1-y0+1),mf
_Z={}; PHOTO=set(l.split('\t')[0] for l in open(H+'/cards4-photos.tsv')) if os.path.exists(H+'/cards4-photos.tsv') else set()
BOX=json.load(open(H+'/cards4-boxes.json')) if os.path.exists(H+'/cards4-boxes.json') else {}
def card_zoom(card,asp):
    """A crop that fills the television with the card's type (October review: second lines were tiny inside the television).
    Measured from the card's last frame: the box round everything bright, padded, widened to the glass's shape. Photo cards are left alone."""
    import numpy as np
    cid=os.path.basename(card)[:-4]
    if cid in PHOTO: return ""
    if cid not in _Z and cid in BOX:
        x0,y0,x1,y1=BOX[cid]; w,h=x1-x0,y1-y0
        if w/h<asp: w2=h*asp; x0-=(w2-w)*0.5; w=w2
        else: h2=w/asp; y0-=(h2-h)/2; h=h2
        x0=max(0,min(1280-w,x0)); y0=max(0,min(720-h,y0)); w=min(w,1280); h=min(h,720)
        _Z[cid]=f"crop={int(w)//2*2}:{int(h)//2*2}:{int(x0)}:{int(y0)},"
    if cid not in _Z:
        raw=subprocess.check_output(['ffmpeg','-v','error','-sseof','-0.3','-i',SC+'/'+card,'-frames:v','1','-f','rawvideo','-pix_fmt','rgb24','-'])
        a=np.frombuffer(raw,dtype=np.uint8).reshape(720,1280,3).max(2)>110; a[640:,:]=False      # the source line at the foot is left out
        ys,xs=np.where(a); x0,x1,y0,y1=xs.min()-36,xs.max()+36,ys.min()-30,ys.max()+30
        w,h=x1-x0,y1-y0
        if w/h<asp: w2=h*asp; x0-=(w2-w)*0.5; w=w2
        else: h2=w/asp; y0-=(h2-h)/2; h=h2
        x0=max(0,min(1280-w,x0)); y0=max(0,min(720-h,y0)); w=min(w,1280); h=min(h,720)
        _Z[cid]=f"crop={int(w)//2*2}:{int(h)//2*2}:{int(x0)}:{int(y0)},"
    return _Z[cid]
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).decode())
WORDS={l.split('\t')[0]:l.rstrip('\n').split('\t') for l in open(H+'/none.tsv')} if os.path.exists(H+'/none.tsv') else {}
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
WJ=json.load(open(H+'/words-2026.json')) if os.path.exists(H+'/words-2026.json') else {}
HEAD=0.10; TAIL=0.16; TAIL_BEAT=0.30      # air before the first word, after the last, and after the last word of a beat
SENT=0.30; COMMA=0.17                     # the longest pause left after a full stop, and anywhere else inside a line
# pauses kept longer on purpose, because the pause is the joke or the turn: (clip, the word before the pause) -> seconds
PAUSE={('y-00','matter.'):0.62,('y-01','Iran.'):0.65,('y-02','again.'):0.45,('y-04','it.'):0.60,('y-06','Polymarket.'):0.55,('y-14','twice.'):0.40,
       ('y-15','bin.'):0.50,('y-20','deals.'):0.40,('y-21b','though.'):0.45,('y-22','night.'):0.55,('y-26','barbecue.'):0.50,('y-27','dollars.'):0.65,('y-29','you.'):0.50}
PUNCH={'y-01':'unrelated','y-06':'for','y-12':None,'y-21b':None,'y-24':'local','y-27':'cheers'}   # cut 4: clip -> the word the punch-in lands on (None: the whole clip)
PX,PY=110,10                              # the punch-in window (984x554) keeps his face on the left third
HISS=set(); SOFT={'y-18'}     # SOFT: opens on a mumbled word quieter than the onset threshold ('Anyway.'), so the head is kept whole                     # measured 11 Oct; not applied to every clip because it would shave soft first words (01a, 07b)
WHOLE={'y-28':(0.0,8.01),'y-30':(0.0,10.01)}               # the silent ending: he sits for a second and a half before anything happens
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
    if begin<0.05 and name not in SOFT: begin=max(0.0,onset(f)-HEAD)   # cut 2: six clips opened on up to 0.7 s of low noise that silencedetect did not call silence (the dead air before HS2)   # these open on a second of faint hiss that silencedetect does not call silence
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
OLD={r['clip']:(float(r['in']),float(r['length'])) for r in csv.DictReader(open(RN+'/none.tsv'),delimiter='\t')} if os.path.exists(RN+'/none.tsv') else {}
words={l.split('\t')[0]:int(l.split('\t')[4]) for l in open(H+'/clips-2026.tsv') if l.strip()}
parts=[]; used=[]; log=[]; order=list(PLAN); GAINS=[]
for name,(tv,full) in PLAN.items():
    src=f'{V}/{name}.mp4'
    if not os.path.exists(src): print('MISSING',name); continue
    nxt=order[order.index(name)+1] if order.index(name)+1<len(order) else None
    R=keeps(src,name,nxt is None or nxt[:4]!=name[:4] or len(name)==4); b,e=R[0][0],R[-1][1]; t=sum(z-a for a,z in R); out=f'{CL}/{TAG}-{name}.mov'   # unique names: Premiere matches items by name. .mov with PCM sound: see CLIP
    ins=['-i',src]; k=len(R)
    fc=[f"[0:v]scale=in_color_matrix=bt601:out_color_matrix=bt709,split={k}"+''.join(f'[sv{i}]' for i in range(k)),f"[0:a]asplit={k}"+''.join(f'[sa{i}]' for i in range(k))]
    for i,(a,z) in enumerate(R):
        fc.append(f"[sv{i}]trim=start={a:.3f}:end={z:.3f},setpts=PTS-STARTPTS[kv{i}]")
        fc.append(f"[sa{i}]atrim=start={a:.3f}:end={z:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={max(0,z-a-0.012):.3f}:d=0.012[ka{i}]")
    fc.append(''.join(f'[kv{i}][ka{i}]' for i in range(k))+f"concat=n={k}:v=1:a=1[bv][ba]"); last='bv'; n=1
    ws=(WJ.get(name) or {}).get('words',[])
    nz=lambda x:re.sub(r"[^a-z0-9']","",x.lower())
    def when(pat,after=0.0):
        for w in ws:
            if w[1]>=after and any(nz(w[0]).startswith(q) for q in pat.split('|')): return w[1]
    sc=screen_of(src,b+min(1.0,t/2)) if tv else None
    if tv and sc:
        X,Y,W,Hh,mf=sc
        segs=tv if isinstance(tv,list) else [(tv,None)]
        starts=[]; srct=0.0
        for src_,w_ in segs:                       # cut 4: the television changes picture on a word (searched after the last change's word)
            tw=when(w_,srct+0.01) if w_ else None
            if w_ and tw is None: print('  WARN no word',w_,'in',name)
            if tw is not None: srct=tw
            starts.append(starts[-1] if (w_ and tw is None) else (0.0 if tw is None else max(0.0,at_new(R,tw)-0.05)))
        ins+=['-i',mf]; mi=n; n+=1
        fc.append(f"[{mi}:v]format=gray,split={len(segs)}"+''.join(f'[m{i}]' for i in range(len(segs))))
        for i,(src_,w_) in enumerate(segs):
            a_=starts[i]; z_=starts[i+1] if i+1<len(segs) else t+1
            used.append(src_)
            if src_.startswith(CARDS+'/'): ins+=['-itsoffset',f'{a_:.3f}','-i',SC+'/'+src_]
            else: ins+=scr(src_,t)
            zoom=card_zoom(src_,W/Hh) if src_.startswith(CARDS+"/") else ""
            fc.append(f"[{n}:v]{zoom}scale={W}:{Hh}:force_original_aspect_ratio=increase,crop={W}:{Hh},setsar=1,gblur=sigma=0.5,eq=saturation=1.12:contrast=1.04,drawgrid=w={W}:h=3:t=1:c=black@0.16,pad=1280:720:{X}:{Y},format=rgb24[c{i}];[c{i}][m{i}]alphamerge[ca{i}];[{last}][ca{i}]overlay=enable='between(t,{a_:.3f},{z_:.3f})':eof_action=pass:shortest=0[tv{i}]")
            last=f'tv{i}'; n+=1
        lx,ly,lw,lh=X+W//2-60,Y+Hh+6,120,34
        fc.append(f"[{last}]split[lg0][lg1];[lg1]crop={lw}:{lh}:{lx}:{ly},gblur=sigma=9[lgb];[lg0][lgb]overlay={lx}:{ly}[v1b]"); last='v1b'
    if name in PUNCH:                             # cut 4: a punch-in on the deadpan tag, from its word to the end of the clip
        pw=PUNCH[name]; tp=when(pw) if pw else None; a_=0.0 if tp is None else max(0.0,at_new(R,tp)-0.04)
        fc.append(f"[{last}]split[pz0][pz1];[pz1]crop=984:554:{PX}:{PY},scale=1280:720,setsar=1[pzc];[pz0][pzc]overlay=enable='gte(t,{a_:.3f})'[vpz]"); last='vpz'
    if full:
        card,w0,w1=full; used.append(card)
        t0=when(w0); t1=when(w1,(t0 or 0)+0.5) if w1 else None
        if t0 is None: print('  WARN no word',w0,'in',name); a,z=0.3*t,0.9*t
        else: a=max(0.0,at_new(R,t0)-0.08); z=min(t-0.04,at_new(R,t1)-0.10) if t1 else t-0.04
        if z-a<1.2: z=min(t-0.04,a+1.2)
        ins+=['-itsoffset',f'{a:.3f}','-i',SC+'/'+card]                                         # the card's animation starts when the cutaway does
        fc.append(f"[{n}:v]scale=1280:720,setsar=1[fu];[{last}][fu]overlay=enable='between(t,{a:.3f},{z:.3f})':eof_action=pass[v2]"); last='v2'; n+=1
    fc.append(f"[{last}]fps=24,format=yuv420p,lutyuv=y='clip(val,20,231)':u='clip(val,20,236)':v='clip(val,20,236)'[v]")
    if words.get(name,0):
        m=subprocess.run(['ffmpeg','-v','info','-y','-i',src,'-filter_complex',';'.join(x for x in fc if '[sa' in x or 'asplit' in x)+';'+''.join(f'[ka{i}]' for i in range(k))+f"concat=n={k}:v=0:a=1,loudnorm=print_format=json[o]",'-map','[o]','-f','null','-'],capture_output=True,text=True).stderr
        gain=max(-6.0,min(14.0,-15.0-float(re.search(r'"input_i"\s*:\s*"([-\d.]+)"',m).group(1)))); GAINS.append(gain)
    else: gain=sorted(GAINS)[len(GAINS)//2] if GAINS else 0.0     # a silent clip gets the usual gain, so the room sounds the same
    pre="volume=0.05:enable='lt(t,4.8)'," if name=='y-30' else ""    # cut 2: this take has a pub murmur under the drinking (heard by Gemini twice); the glass and the footsteps are kept
    af=f"{pre}volume={gain:.2f}dB,alimiter=limit=0.84:level=false,afade=t=in:d=0.03,afade=t=out:st={max(0,t-0.06):.3f}:d=0.06"
    fc.append(f"[ba]{af}[a]")
    run(['ffmpeg','-v','error','-y']+ins+['-filter_complex',';'.join(fc),'-map','[v]','-map','[a]','-t',f'{t:.3f}']+CLIP+[out])
    parts.append(out); log.append(f"{name}\t{b:.2f}\t{e:.2f}\t{t:.2f}\t{tv or '-'}\t{full[0] if full else '-'}\t{' '.join(f'{a:.2f}-{z:.2f}' for a,z in R)}"); print(log[-1])
# the title sting after the cold open (Jack, 14 Oct, cut 4 notes: "add this"): cards4/title.mp4 and its synthesized hit
tt=f'{CL}/{TAG}-y-00t-title.mov'
run(['ffmpeg','-v','error','-y','-i',SC+'/'+CARDS+'/title.mp4','-i',SC+'/'+CARDS+'/title-sting.wav','-filter_complex',
     "[0:v]trim=end=2.625,setpts=PTS-STARTPTS,fps=24,format=yuv420p,lutyuv=y='clip(val,20,231)':u='clip(val,20,236)':v='clip(val,20,236)'[v];[1:a]volume=0dB[a]",'-map','[v]','-map','[a]','-t','2.625']+CLIP+[tt])
parts.insert(1,tt); log.insert(1,'y-00t\t0\t2.62\t2.62\t-\tcards4/title.mp4\ttitle sting')
# credits owed by the pictures used, including the photo behind each card
if os.path.exists(H+'/cards4-photos.tsv'):
    back=dict(l.rstrip('\n').split('\t') for l in open(H+'/cards4-photos.tsv') if l.strip())
    used+=[back[os.path.basename(u)[:-4]] for u in list(used) if u.startswith(CARDS+'/') and os.path.basename(u)[:-4] in back]
cred=[]
MAN2=MAN.replace('money-for-something-screen-sources.md','money-for-something-2026-screen-sources.md')
if os.path.exists(MAN):
    for row in list(open(MAN))+(list(open(MAN2)) if os.path.exists(MAN2) else []):
        c=[x.strip() for x in row.split('|')]
        if len(c)>8 and any(os.path.basename(u)==c[2].strip('`') for u in used):
            s=c[7]
            if s and not s.startswith('None owed') and s not in cred: cred.append(s)
T=tempfile.mkdtemp(); lines=['PICTURES']+[re.sub(r'\s+',' ',c) for c in cred]+(['','Contains public sector information licensed','under the Open Government Licence v3.0.'] if any('Open Government' in c for c in cred) else [])+['','A BADCODE transmission. Made with AI.']   # a credit is never cut short: the licence asks for it whole
tfp=T+'/cr.txt'; open(tfp,'w').write('\n'.join(lines))
crd=f'{CL}/{TAG}-y-99-credits.mov'
run(['ffmpeg','-v','error','-y','-f','lavfi','-i','color=black:s=1280x720:d=4.5','-stream_loop','-1','-ss','0.3','-t','3.2','-i',f'{V}/y-28.mp4','-filter_complex',
     f"[0:v]drawtext=fontfile={F}:textfile={tfp}:fontcolor=white@0.85:fontsize=15:line_spacing=8:x=60:y=50,format=yuv420p,lutyuv=y='clip(val,20,231)':u='clip(val,20,236)':v='clip(val,20,236)'[v];[1:a]volume={(sorted(GAINS)[len(GAINS)//2] if GAINS else 0):.2f}dB,afade=t=in:d=0.2,afade=t=out:st=3.3:d=1.2[a]",'-map','[v]','-map','[a]','-t','4.5']+CLIP+[crd]); parts.append(crd)
stem=sys.argv[1] if len(sys.argv)>1 else 'MFS 2026 cut 1'; final=f'{RN}/{stem}.mp4'
ins=[]; 
for p_ in parts: ins+=['-i',p_]
n_=len(parts); fc_=''.join(f'[{i}:v][{i}:a]' for i in range(n_))+f'concat=n={n_}:v=1:a=1[v0][a0];[{n_}:a]lowpass=f=500,highpass=f=40,volume=-12dB[rt];[a0][rt]amix=inputs=2:duration=first:normalize=0[a];[v0]'+"lutyuv=y='clip(val,20,231)':u='clip(val,20,236)':v='clip(val,20,236)'[v]"   # held inside legal range with room for the encoder's ringing (delivery-qc)
ins+=['-f','lavfi','-i','anoisesrc=color=brown:amplitude=0.05:seed=7:r=48000']   # a faint room tone (about -54 dB) under the whole cut: October's ending was dead silence, and the quiet clips here drop to nothing
run(['ffmpeg','-v','error','-y']+ins+['-filter_complex',fc_,'-map','[v]','-map','[a]']+ENC+['-movflags','+faststart',final])
open(f'{RN}/{stem}.tsv','w').write('clip\tin\tout\tlength\ttelevision\tfull screen\tkept\n'+'\n'.join(log)+'\n')
print('CUT',final,'%.1f s'%dur(final),'parts',len(parts),'credits',len(cred))
