#!/usr/bin/env python3
"""Money For Something, 26 Oct: one vertical short's pieces, from a spec in shorts/<name>.json (26 Oct 2026).
Jack: "lets just make the shorts with what we have so far". The words are the locked lines in
docs/stories/magic-money-tree/money-for-something-2026-10-26-shorts-script.md; the voice is voice/*.wav (mfs-voice.py),
timed by voice/words.json (words.py). Everything is built as layers for Premiere, which does the final export:

  <out>/<name>/voice.wav        the takes joined, 0.35 s apart
  <out>/<name>/graphics.mov     ProRes 4444 with alpha: overlay B (signal box, tag, chyron, yellow line), burnt-in captions,
                                headline slams / stat cards / quote cards, the two-frame glitch on the turn
  <out>/<name>/pic-NN-<key>.mp4 one clip per picture, cold-graded and slowly pushed in, cut to its word
  <out>/<name>/tail.mp4         plate H1 then the logo (the host's silent tail; a Flow move replaces the still later)
  <out>/<name>/edl.json         where every piece sits, for the Premiere build
  <out>/<name>/sheet.jpg        a contact sheet of the graphics over the pictures, for checking
Safe areas (docs/marketing/shorts-factory.md): nothing in the bottom 350 px or the right 150 px.
usage: ~/.cache/badcode-whisper/venv/bin/python build-short.py shorts/<name>.json [more.json ...]"""
import os,sys,json,re,math,random,difflib,subprocess,tempfile,importlib.util,csv
from PIL import Image,ImageDraw,ImageFont,ImageOps,ImageFilter
H=os.path.dirname(os.path.abspath(__file__))
spec_=importlib.util.spec_from_file_location('slams',H+'/build-headline-slams.py'); S=importlib.util.module_from_spec(spec_); spec_.loader.exec_module(S)
FD=H+'/../fonts/'; MARK=H+'/../../../docs/brand/logo/avatar-1024.png'
A='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/2026-10-26'
VOICE=A+'/voice'; OUT=A+'/shorts'; PLATE=A+'/stills/plate-H1-a.jpg'
W,Hh,FPS=1080,1920,24; L=60; SAFE_R=1080-150
INK,WHT,RED,YEL=S.INK,S.WHT,S.RED,S.YEL
GAP=0.35; TAIL=2.6; CAP_Y=1150; TAG_Y=1240
arc,mono=S.arc,S.mono
def run(a): subprocess.run(['ffmpeg','-loglevel','error','-y']+a,check=True)
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).decode())
norm=lambda w: re.sub(r"[^a-z0-9']","",w.lower())

def words_for(parts):
    """Transcript words (Jack's spelling) with times from the speech model, the parts laid end to end."""
    WJ=json.load(open(H+'/voice/words.json')); out=[]; t0=0.0
    for p in parts:
        tx=open(f'{H}/voice/{p}.txt').read().split(); ws=WJ[p]
        a=[norm(w) for w in tx]; b=[norm(w[0]) for w in ws]; tm=[None]*len(tx)
        for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
            if op=='equal':
                for k in range(i2-i1): tm[i1+k]=(ws[j1+k][1],ws[j1+k][2])
            elif op=='replace' or (op=='delete' and j1>0):
                s=ws[j1][1] if j2>j1 else ws[j1-1][2]; e=ws[j2-1][2] if j2>j1 else s+0.2; n=i2-i1
                for k in range(n): tm[i1+k]=(s+(e-s)*k/n,s+(e-s)*(k+1)/n)
        for i in range(len(tm)):                                    # anything still empty: borrow the neighbour
            if tm[i] is None: tm[i]=(tm[i-1][1],tm[i-1][1]+0.15) if i else (0,0.15)
        out+=[(w,s+t0,e+t0) for w,(s,e) in zip(tx,tm)]
        t0+=dur(f'{VOICE}/{p}.wav')+GAP
    return out,t0-GAP

def at(words,phrase,which='start'):
    """Time of the first word of `phrase` in the transcript (phrase matched on normalised words)."""
    p=[norm(x) for x in phrase.split()]; n=[norm(w[0]) for w in words]
    for i in range(len(n)-len(p)+1):
        if n[i:i+len(p)]==p: return words[i][1] if which=='start' else words[i+len(p)-1][2]
    raise SystemExit(f'phrase not in transcript: {phrase!r}')

def captions(words):
    """Two or three words at a time, broken after punctuation, never more than 22 characters."""
    groups=[[]]
    for w in words:
        g=groups[-1]; txt=' '.join(x[0] for x in g+[w])
        if g and (len(txt)>22 or len(g)>=3): groups.append([w]); g=groups[-1]
        else: g.append(w)
        if re.search(r'[.,!?:;]$',w[0]): groups.append([])
    groups=[g for g in groups if g]
    return [(' '.join(x[0] for x in g),g[0][1],(groups[i+1][0][1] if i+1<len(groups) else g[-1][2]+0.3)) for i,g in enumerate(groups)]

def wrap(d,text,font,width):
    lines=[[]]
    for w in text.split():
        if lines[-1] and d.textlength(' '.join(lines[-1]+[w]),font=font)>width: lines.append([w])
        else: lines[-1].append(w)
    return [' '.join(l) for l in lines]

def card_img(c):
    """A slam: a paper cutting (real headline, verbatim), a stat card or a quote card. RGBA."""
    t=c.get('type','headline')
    if t=='headline': return S.cutting(c,1.0)
    d0=ImageDraw.Draw(Image.new('RGB',(1,1))); cw=880; pad=48
    if t=='stat':
        f=arc(c.get('size',112)); lines=wrap(d0,c['text'],f,cw-2*pad); lh=int(f.size*1.05)
        sub=c.get('sub',''); sf=mono(30); ch=pad*2+lh*len(lines)+(56 if sub else 0)
        im=Image.new('RGBA',(cw,ch),INK+(245,)); d=ImageDraw.Draw(im)
        d.rectangle((0,0,cw-1,ch-1),outline=tuple(c.get('edge',YEL))+(255,),width=6)
        for i,l in enumerate(lines): d.text((pad,pad+i*lh-10),l,font=f,fill=c.get('ink',WHT))
        if sub: d.text((pad,ch-pad-34),sub.upper(),font=sf,fill=WHT+(170,))
        return im
    if t=='quote':
        f=S.serif(62); lines=wrap(d0,'“'+c['text']+'”',f,cw-2*pad); lh=76; ch=pad*2+lh*len(lines)+60
        im=Image.new('RGBA',(cw,ch),S.PAPER+(255,)); d=ImageDraw.Draw(im)
        for i,l in enumerate(lines): d.text((pad,pad+i*lh),l,font=f,fill=INK)
        d.text((pad,ch-pad-30),'— '+c['who'],font=arc(28,800,100),fill=(90,90,90)); return im
    raise SystemExit(f'card type {t}')

def build(path):
    sp=json.load(open(path)); name=sp['name']; o=f'{OUT}/{name}'; os.makedirs(o,exist_ok=True)
    words,vend=words_for(sp['voice'])
    # the voice, joined
    ins=sum((['-i',f'{VOICE}/{p}.wav'] for p in sp['voice']),[])
    fl=''.join(f'[{i}:a]apad=pad_dur={GAP}[a{i}];' if i<len(sp['voice'])-1 else f'[{i}:a]anull[a{i}];' for i in range(len(sp['voice'])))
    run(ins+['-filter_complex',fl+''.join(f'[a{i}]' for i in range(len(sp['voice'])))+f'concat=n={len(sp["voice"])}:v=0:a=1[o]','-map','[o]','-ar','48000','-ac','2',f'{o}/voice.wav'])
    turn=at(words,sp['turn']) if sp.get('turn') else words[-1][1]   # the yellow line lands on the last phrase
    end=vend+0.9                                                   # a beat of air after the last word, then the tail
    # slam schedule: each card from its word until the next "clear" (or the end)
    sched=[]; pile=[]
    for c in sp.get('slams',[]):
        if 'clear' in c:
            t=at(words,c['clear']); [s.__setitem__(1,t) for s in pile]; pile=[]; continue
        s=[at(words,c['at']),end,c,card_img(c)]; sched.append(s); pile.append(s)
    rnd=random.Random(name)
    for s in sched: s+= [rnd.uniform(-4,4),rnd.randint(-40,40),rnd.randint(-30,30)]
    caps=captions(words); sig0,sig1=sp['signal']; nf=int(end*FPS)
    furn=Image.new('RGBA',(W,Hh),(0,0,0,0)); d=ImageDraw.Draw(furn)
    m=Image.open(MARK).convert('RGB').resize((110,110)); mk=Image.new('L',(110,110),0); ImageDraw.Draw(mk).ellipse((0,0,109,109),fill=255)
    d.rounded_rectangle((L-14,116,L+560,254),radius=14,fill=INK+(170,))   # a plate, so the signal box reads over a white sky
    furn.paste(m,(L,130),mk); d.text((L+130,140),'RECEIVED 26.10.2026',font=mono(30),fill=WHT)
    for (x,y,sx,sy) in ((L,300,1,1),(SAFE_R,300,-1,1),(L,1060,1,-1),(SAFE_R,1060,-1,-1)):   # viewfinder corners
        d.line((x,y,x+60*sx,y),fill=WHT+(200,),width=5); d.line((x,y,x,y+60*sy),fill=WHT+(200,),width=5)
    # tag + chyron: on from frame one, it's the hook
    # the block sits on the bottom safe line and grows upwards: tag, chyron, yellow line; the captions sit above the tag
    cf=arc(sp.get('chyron_size',54)); yf=mono(34)
    nc=len(wrap(d,sp['chyron'],cf,SAFE_R-L-56)); ny=len(wrap(d,'› '+sp['payoff'],yf,SAFE_R-L-48))
    TAG_Y=min(1240,1560-24-ny*48-(36+nc*64)-72); CAP_Y=TAG_Y-90
    tf=mono(34); tw=int(d.textlength(f'ARCHIVE · ITEM {sp["item"]}',font=tf))
    d.rectangle((L,TAG_Y-8,L+tw+110,TAG_Y+60),fill=INK+(225,)); d.polygon([(L+16,TAG_Y+6),(L+70,TAG_Y+6),(L+43,TAG_Y+52)],fill=RED)
    d.text((L+90,TAG_Y+6),f'ARCHIVE · ITEM {sp["item"]}',font=tf,fill=WHT)
    cf=arc(sp.get('chyron_size',54)); cl=wrap(d,sp['chyron'],cf,SAFE_R-L-56); cy=TAG_Y+72; chh=36+len(cl)*64
    d.rectangle((L,cy,SAFE_R,cy+chh),fill=INK+(230,))
    for i,l in enumerate(cl): d.text((L+28,cy+14+i*64),l,font=cf,fill=WHT)
    ybar=cy+chh; yf=mono(34); yl=wrap(d,'› '+sp['payoff'],yf,SAFE_R-L-48)
    yel=Image.new('RGBA',(W,Hh),(0,0,0,0)); dy=ImageDraw.Draw(yel)
    dy.rectangle((L,ybar,SAFE_R,ybar+24+len(yl)*48),fill=YEL+(255,))
    for i,l in enumerate(yl): dy.text((L+24,ybar+12+i*48),l,font=yf,fill=INK)
    assert ybar+24+len(yl)*48<=1570, f'{name}: chyron runs into the bottom safe area'
    assert CAP_Y>1000, f'{name}: chyron and yellow line too tall'
    capf=arc(66,900,110); tmp=tempfile.mkdtemp(prefix=f'mfs-{name}-'); frames=[]
    for f in range(nf):
        now=f/FPS; ov=furn.copy(); dd=ImageDraw.Draw(ov)
        sig=int(sig0+(sig1-sig0)*min(1,now/max(turn,0.1)))
        dd.text((L+130,182),f'SENT 2054 · SIGNAL {sig}%',font=mono(30),fill=WHT+(170,))
        live=[s for s in sched if s[0]<=now<s[1]]
        for k,(s0,s1,c,full,rot,dx,dyy) in enumerate(live):
            a=now-s0; img=S.cutting(c,min(1,max(0,(a-0.12)/0.35))) if c.get('type','headline')=='headline' and a<0.5 else full
            sc=1.0+0.28*(1-S.ease(min(1,a/0.14)))-0.03*math.sin(min(1,a/0.14)*math.pi)
            if k<len(live)-1: sc*=0.94
            img=img.rotate(rot,expand=True,resample=Image.BICUBIC); img=img.resize((int(img.width*sc),int(img.height*sc)),Image.BICUBIC)
            sh=Image.new('RGBA',img.size,(0,0,0,0)); sh.putalpha(img.getchannel('A').point(lambda v:int(v*0.45))); sh=sh.filter(ImageFilter.GaussianBlur(10))
            jit=random.Random(f*7+k); shk=(jit.randint(-10,10),jit.randint(-10,10)) if a<0.2 else (0,0)
            cx=(L+SAFE_R)//2+dx+shk[0]; cyy=700+dyy+shk[1]
            ov.alpha_composite(sh,(cx-img.width//2+10,cyy-img.height//2+16)); ov.alpha_composite(img,(cx-img.width//2,cyy-img.height//2))
            if c.get('tag') and k==len(live)-1:
                tagged=[x[2] for x in sched if x[2].get('tag')]
                ov.alpha_composite(S.tag(c,tagged.index(c)+1,len(tagged)),(L,1020))
        cap=[c for c in caps if c[1]<=now<c[2]]
        if cap and now<vend+0.3:
            ws_=cap[0][0].split(); sp_=28; tw=sum(dd.textlength(w,font=capf) for w in ws_)+sp_*(len(ws_)-1); x=(L+SAFE_R-tw)/2
            for w in ws_:                                          # word by word: the wide face's own space is too tight under a stroke
                dd.text((x,CAP_Y-40),w,font=capf,fill=WHT,stroke_width=7,stroke_fill=INK); x+=dd.textlength(w,font=capf)+sp_
        if now>=turn: ov.alpha_composite(yel)
        if abs(now-turn)<0.09:                                     # two-frame glitch on the turn: the signal tears
            g=ov.copy(); r=random.Random(f)
            for _ in range(7):
                y=r.randint(100,1500); h=r.randint(10,60); band=g.crop((0,y,W,y+h)); ov.paste(band,(r.randint(-60,60),y))
            for y in range(0,Hh,9): dd.line((0,y,W,y),fill=(255,255,255,30))
        p=f'{tmp}/a{f:05d}.png'; ov.save(p,compress_level=1); frames.append(p)
    run(['-framerate',str(FPS),'-i',f'{tmp}/a%05d.png','-c:v','prores_ks','-profile:v','4444','-pix_fmt','yuva444p10le',f'{o}/graphics.mov'])
    # pictures: each cut to its word, held to the next one
    PIC={}                                                         # key -> [(path, credit), ...]; a key used twice takes its next photo
    if os.path.exists(H+'/pictures.tsv'):
        for r in csv.reader(open(H+'/pictures.tsv'),delimiter='\t'):
            if r and r[0]!='key' and not r[0].startswith('#'): PIC.setdefault(r[0],[]).append((r[1],r[2] if len(r)>2 else ''))
    pics=[]; ps=sp['pictures']; used={}
    for i,p in enumerate(ps):
        t0=0.0 if i==0 else at(words,p['at']); t1=at(words,ps[i+1]['at']) if i+1<len(ps) else end
        k=p['key']; n_=used.get(k,0); used[k]=n_+1
        src,cred=PIC[k][(p.get('pick',n_+1)-1)%len(PIC[k])] if k in PIC else (None,'')
        if not src: print(f'  {name}: no picture for {k}, black')
        fn=f'pic-{i+1:02d}-{p["key"]}.mp4'; d_=max(0.5,t1-t0); pics.append({'file':fn,'key':k,'src':src,'start':round(t0,3),'end':round(t1,3),'credit':cred})
        n=int(d_*FPS)+2; z=p.get('zoom',0.06)
        if src:
            vf=(f"scale={W*2}:{Hh*2}:force_original_aspect_ratio=increase,crop={W*2}:{Hh*2},"
                f"zoompan=z='1+{z}*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s={W}x{Hh}:fps={FPS},"
                "hue=s=0.55,colorbalance=bs=0.10:bm=0.06:rs=-0.04,eq=contrast=1.06:brightness=-0.04,"   # overlay B's cold grade
                "drawgrid=w=iw:h=4:t=1:c=black@0.16,format=yuv420p")
            run(['-loop','1','-i',src,'-vf',vf,'-t',f'{d_:.3f}','-c:v','libx264','-crf','16','-r',str(FPS),f'{o}/{fn}'])
        else:
            run(['-f','lavfi','-i',f'color=c=0x060709:s={W}x{Hh}:r={FPS}','-t',f'{d_:.3f}','-c:v','libx264','-pix_fmt','yuv420p',f'{o}/{fn}'])
    # the tail: plate H1, then the logo
    hn=int(1.6*FPS)
    run(['-loop','1','-t','1.6','-i',PLATE,'-loop','1','-t','1.0','-i',H+'/../../../docs/brand/logo/avatar-1024.png','-filter_complex',
         f"[0:v]scale={W*2}:{Hh*2}:force_original_aspect_ratio=increase,crop={W*2}:{Hh*2},zoompan=z='1.08-0.06*on/{hn}':d={hn}:s={W}x{Hh}:fps={FPS},format=yuv420p,trim=duration=1.6[h];"
         f"color=c=0x060709:s={W}x{Hh}:r={FPS}:d=1.0[bk];[1:v]scale=460:460,format=yuva420p[lg];[bk][lg]overlay=(W-w)/2:(H-h)/2-120,format=yuv420p[l];"
         "[h][l]concat=n=2:v=1[o]",'-map','[o]','-t',str(TAIL),'-c:v','libx264','-crf','16','-r',str(FPS),f'{o}/tail.mp4'])
    edl={'name':name,'fps':FPS,'size':[W,Hh],'voice_end':round(vend,3),'graphics_end':round(end,3),'tail':{'file':'tail.mp4','start':round(end,3),'length':TAIL},
         'turn':round(turn,3),'pictures':pics,'slams':[{'at':round(s[0],3),'until':round(s[1],3),'card':s[2]} for s in sched],
         'words':' '.join(w[0] for w in words)}
    json.dump(edl,open(f'{o}/edl.json','w'),indent=1)
    # contact sheet: graphics over the pictures at six moments
    shots=[]
    for t in [0.5]+[s[0]+0.6 for s in sched][:3]+[turn+0.2,end-0.3]:
        pc=[p for p in pics if p['start']<=t<p['end']] or pics[-1:]
        bg=subprocess.run(['ffmpeg','-v','error','-ss',f'{max(0,t-pc[0]["start"]):.2f}','-i',f'{o}/{pc[0]["file"]}','-frames:v','1','-f','image2pipe','-vcodec','png','-'],capture_output=True).stdout
        im=Image.open(__import__('io').BytesIO(bg)).convert('RGBA'); im.alpha_composite(Image.open(frames[min(len(frames)-1,int(t*FPS))])); shots.append(im.convert('RGB').resize((360,640)))
    sh=Image.new('RGB',(360*len(shots),640)); [sh.paste(s,(i*360,0)) for i,s in enumerate(shots)]; sh.save(f'{o}/sheet.jpg',quality=88)
    subprocess.run(['rm','-rf',tmp]); print(f'{o}  voice {vend:.1f}s  + tail = {end+TAIL:.1f}s  ({len(pics)} pictures, {len(sched)} slams)')

if __name__=='__main__':
    for p in sys.argv[1:]: build(p)
