#!/usr/bin/env python3
"""Money For Something, 26 Oct: headline slams, real headlines popping on screen like press cuttings (25 Oct 2026).
Jack: "have headlines flash on screen like memes, that is a common format used nowadays on youtube videos".
The format: a real headline, verbatim, as a tilted paper cutting that punches in (overshoot + shake), a highlighter
swipes the words that matter, the next one lands on top of the pile. Sits inside overlay B (Transmission): the signal
box stays up, each cutting wears a red-triangle checklist tag, the yellow `›` line closes the run.
Headlines are quoted exactly with outlet and date; the outlet is plain type, never its logo.
Writes <out>/slams-<name>.mov (ProRes 4444 with alpha, to lay over footage in Premiere) and <out>/slams-<name>-preview.mp4.
usage: ~/.cache/badcode-whisper/venv/bin/python build-headline-slams.py SPEC.json OUTDIR [BACKGROUND.jpg]"""
import os,sys,json,math,random,subprocess,tempfile
from PIL import Image,ImageDraw,ImageFont,ImageOps,ImageFilter
H=os.path.dirname(os.path.abspath(__file__))
FD=H+'/../fonts/'; ARC=FD+'Archivo.ttf'; MONO=FD+'SpaceMono-Bold.ttf'
SERIF='/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf'
MARK=H+'/../../../docs/brand/logo/avatar-1024.png'
W,Hh,FPS=1080,1920,24; L=60; SAFE_R=1080-150; SAFE_B=1920-350
INK=(6,7,9); WHT=(236,242,244); RED=(201,43,56); YEL=(250,204,21); PAPER=(250,248,242)
def arc(s,w=900,wd=125):
    f=ImageFont.truetype(ARC,s); f.set_variation_by_axes([w,wd]); return f
def mono(s): return ImageFont.truetype(MONO,s)
def serif(s): return ImageFont.truetype(SERIF,s)
def ease(t): return 1-(1-t)**3

def cutting(c,sweep):
    """One paper cutting as RGBA. sweep 0..1 = how far the highlighter has run."""
    cw=880; pad=44; hf=serif(64); of=arc(28,800,100); df=mono(24); tf=mono(28)
    words=c['headline'].split(); hl=set()
    hw=c.get('highlight','').split()
    for i in range(len(words)):                      # mark the highlighted run of words
        if hw and [w.strip('\'"‘’“”,.') for w in words[i:i+len(hw)]]==[w.strip('\'"‘’“”,.') for w in hw]:
            hl.update(range(i,i+len(hw)))
    lines=[[]]; d0=ImageDraw.Draw(Image.new('RGB',(1,1)))
    for i,w in enumerate(words):
        test=' '.join(words[j] for j in lines[-1]+[i])
        if lines[-1] and d0.textlength(test,font=hf)>cw-2*pad: lines.append([i])
        else: lines[-1].append(i)
    lh=78; top=pad+44+26; ch=top+lh*len(lines)+pad+8
    im=Image.new('RGBA',(cw,ch),PAPER+(255,)); d=ImageDraw.Draw(im)
    d.text((pad,pad-6),c['outlet'].upper(),font=of,fill=INK)
    d.text((cw-pad-d.textlength(c['date'],font=df),pad-2),c['date'],font=df,fill=(110,110,110))
    d.line((pad,pad+40,cw-pad,pad+40),fill=INK,width=3)
    # highlighter first (under the ink), swept across all highlighted words in reading order
    spans=[]
    for li,ln in enumerate(lines):
        x=pad
        for i in ln:
            w=words[i]; tw=d.textlength(w,font=hf); sp=d.textlength(' ',font=hf)
            if i in hl: spans.append((x-6,top+li*lh+8,x+tw+6,top+li*lh+lh-2))
            x+=tw+sp
    tot=sum(s[2]-s[0] for s in spans); run=tot*sweep
    for x0,y0,x1,y1 in spans:
        if run<=0: break
        d.rectangle((x0,y0,x0+min(x1-x0,run),y1),fill=YEL+(255,)); run-=x1-x0
    for li,ln in enumerate(lines):
        d.text((pad,top+li*lh),' '.join(words[i] for i in ln),font=hf,fill=INK)
    # torn-ish bottom edge
    rnd=random.Random(c['headline'])
    for x in range(0,cw,6): d.rectangle((x,ch-rnd.randint(0,7),x+6,ch),fill=(0,0,0,0))
    return im

def tag(c,n,N):
    s=f"{n}/{N}  {c['tag']}  · DONE" if c.get('tag') else ''
    if not s: return None
    f=mono(32); w=int(ImageDraw.Draw(Image.new('RGB',(1,1))).textlength(s,font=f))+110
    im=Image.new('RGBA',(w,64),INK+(235,)); d=ImageDraw.Draw(im)
    d.polygon([(16,14),(60,14),(38,50)],fill=RED); d.text((78,12),s,font=f,fill=WHT)
    return im

def furniture(im,sig,glitch=False):
    d=ImageDraw.Draw(im,'RGBA')
    m=Image.open(MARK).convert('RGB').resize((110,110)); mk=Image.new('L',(110,110),0)
    ImageDraw.Draw(mk).ellipse((0,0,109,109),fill=255); im.paste(m,(L,130),mk)
    d.text((L+130,140),'RECEIVED 26.10.2026',font=mono(30),fill=WHT)
    d.text((L+130,182),f'SENT 2054 · SIGNAL {sig}%',font=mono(30),fill=WHT+(170,))
    if glitch:
        for y in range(0,Hh,9): d.line((0,y,W,y),fill=(255,255,255,30))

def render(spec,out,bg=None):
    name=spec['name']; cards=spec['cards']; N=sum(1 for c in cards if c.get('tag'))
    rnd=random.Random(name); t=0.0; sched=[]
    for c in cards: sched.append((t,c)); t+=c.get('hold',1.4)
    end=t+spec.get('tail',2.2); nf=int(end*FPS)
    if bg:
        base=ImageOps.fit(Image.open(bg).convert('RGB'),(W,Hh)).filter(ImageFilter.GaussianBlur(14))
        base=Image.blend(base,ImageOps.colorize(ImageOps.grayscale(base),INK,(214,228,236)),0.6)
        base=Image.blend(base,Image.new('RGB',(W,Hh),INK),0.35)
    pre={id(c):(cutting(c,1.0),rnd.uniform(-4,4),rnd.randint(-40,40),rnd.randint(-30,30)) for _,c in sched}
    tmp=tempfile.mkdtemp(prefix='slams-'); sig0,sig1=spec.get('signal',(84,31))
    for f in range(nf):
        now=f/FPS; ov=Image.new('RGBA',(W,Hh),(0,0,0,0))
        live=[(s,c) for s,c in sched if s<=now]
        for k,(s,c) in enumerate(live):
            a=now-s; full,rot,dx,dy=pre[id(c)]
            sw=min(1,max(0,(a-0.12)/0.35)); img=cutting(c,sw) if sw<1 else full
            sc=1.0+0.28*(1-ease(min(1,a/0.14)))-0.03*math.sin(min(1,a/0.14)*math.pi)  # punch in, overshoot
            if k<len(live)-1: sc*=0.94                                              # buried under the next one
            img=img.rotate(rot,expand=True,resample=Image.BICUBIC)
            img=img.resize((int(img.width*sc),int(img.height*sc)),Image.BICUBIC)
            sh=Image.new('RGBA',img.size,(0,0,0,0)); sh.putalpha(img.getchannel('A').point(lambda v:int(v*0.45)))
            sh=sh.filter(ImageFilter.GaussianBlur(10))
            shake=(rnd.randint(-10,10),rnd.randint(-10,10)) if a<0.2 else (0,0)
            cx=(L+SAFE_R)//2+dx+shake[0]; cy=860+dy+shake[1]
            ov.alpha_composite(sh,(cx-img.width//2+10,cy-img.height//2+16))
            if k<len(live)-1: img=Image.blend(img,Image.new('RGBA',img.size,(30,30,30,0)),0.0)
            ov.alpha_composite(img,(cx-img.width//2,cy-img.height//2))
            if k==len(live)-1:
                tg=tag(c,1+sum(1 for _,x in live[:k] if x.get('tag')),N)
                if tg: ov.alpha_composite(tg,(L,1300))
        if now>=t and spec.get('payoff'):                                            # the yellow line closes it
            d=ImageDraw.Draw(ov); y=1400
            d.rectangle((L,y,SAFE_R,y+76),fill=YEL+(255,)); d.text((L+24,y+16),'› '+spec['payoff'],font=mono(34),fill=INK)
        ov.save(f'{tmp}/a{f:05d}.png')
        if bg:
            sig=int(sig0+(sig1-sig0)*min(1,now/max(t,0.1)))
            fr=base.copy().convert('RGBA'); g=Image.new('RGBA',(W,Hh),(0,0,0,0))
            furniture(g,sig,glitch=abs(now-t)<0.09); fr.alpha_composite(g); fr.alpha_composite(ov)
            fr.convert('RGB').save(f'{tmp}/p{f:05d}.jpg',quality=92)
    run=lambda a: subprocess.run(['ffmpeg','-loglevel','error','-y']+a,check=True)
    run(['-framerate',str(FPS),'-i',f'{tmp}/a%05d.png','-c:v','prores_ks','-profile:v','4444','-pix_fmt','yuva444p10le',f'{out}/slams-{name}.mov'])
    if bg: run(['-framerate',str(FPS),'-i',f'{tmp}/p%05d.jpg','-c:v','libx264','-pix_fmt','yuv420p','-crf','18',f'{out}/slams-{name}-preview.mp4'])
    subprocess.run(['rm','-rf',tmp]); print(f'{out}/slams-{name}.mov', f'{nf/FPS:.1f}s')

if __name__=='__main__':
    spec=json.load(open(sys.argv[1])); out=sys.argv[2]; os.makedirs(out,exist_ok=True)
    render(spec,out,sys.argv[3] if len(sys.argv)>3 else None)
