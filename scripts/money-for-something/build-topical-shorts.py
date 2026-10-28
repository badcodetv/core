#!/usr/bin/env python3
"""Money For Something, the topical monologue: vertical shorts cut from cut 3 (12 Oct 2026). No new footage, no new words.
Jack: "chop it up into shorts"; the old shorts folder was emptied because the last batch was "plain awful and ai slop"
(silent single stills). These are the host talking, with the picture he is talking about, and every word on screen.

One 1080x1920 frame, three things in it:
  top     the picture or stat card that was on his television, at full quality (the television is too small to read on a phone)
  middle  one thin line: who took the photo, when a credit is owed (CC BY needs it on the clip itself)
  bottom  the host, cropped in from the locked wide shot
Words: two or three at a time over the table, Inter Tight like the cards, numbers in the cards' yellow. Timed from
topical-words.json (the local speech model), spelt from the joke bank where the two agree.
Pacing is cut 3's exactly: the kept ranges are read from renders/MFS topical cut 3.tsv.
Sound: each clip levelled to -14 LUFS (the social standard; cut 3 itself is -16).

usage: ~/.cache/badcode-whisper/venv/bin/python build-topical-shorts.py [name ...]      (no names: all of them)
Writes <animation>/shorts/money-for-something/<name>.mp4 and a contact sheet beside each one."""
import os,re,sys,json,csv,subprocess,tempfile,difflib
from PIL import Image,ImageDraw,ImageFont,ImageFilter
H=os.path.dirname(os.path.abspath(__file__))
A='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation'
P=A+'/money for something'; V=P+'/videos'; SC=P+'/screen'; OUT=A+'/shorts/money-for-something'; os.makedirs(OUT,exist_ok=True)
DOCS=os.path.join(H,'..','..','docs','stories','magic-money-tree')
FONT=H+'/fonts/InterTight.ttf'; YEL=(250,204,21); WHT=(255,255,255)
W,HH=1080,1920; TOP_Y=130; TOP_H=608; STRIP_H=34; HOST_Y=TOP_Y+TOP_H+STRIP_H; HOST=1080      # 130 + 608 + 34 + 1080 = 1852
CROP=(600,600,110,50)                                    # w,h,x,y of the host inside the 1280x720 wide shot (locked camera, one crop fits all)
CAP_Y=1525                                               # centre line of the words: over the table, clear of his face and of the apps' own buttons
SHORTS={                                                 # name: clips, in cut 3's order
 '01-nurses-and-missiles':['t-02a','t-03a','t-03b','t-03c'],
 '02-the-banks':['t-05a','t-05b'],
 '03-palantir':['t-09a'],
 '04-expat':['t-10a','t-10b'],
 '05-fartgate':['t-11a'],
 '06-the-budget-and-the-tree':['t-12a','t-12b','t-12c','t-12d'],
 '07-no-money-run':['t-02a','t-03a','t-03b','t-03c','t-05a','t-05b','t-09a'],
 '08-the-episode-clean':['t-01a','t-01b','t-01c','t-02a','t-03a','t-03b','t-03c','t-05a','t-05b','t-09a','t-10a','t-10b','t-11a','t-12a','t-12b','t-12c','t-12d'],
}
# what the television showed, and the card that took the full screen, per clip: the same table as build-topical-cut.py
C='cards3'
PLAN={'t-01a':(C+'/c01a.mp4',None),'t-01b':('b01/b01-burnham-arrives-no10.jpg',(C+'/c01b.mp4',.50)),'t-01c':('b01/b01-google-homepage-1998.png',None),
 't-02a':('b02/b02-clap-street-budd.jpg',(C+'/c02a.mp4',.55)),'t-03a':('b03/b03-thaad-launch-video.mp4',(C+'/c03a.mp4',.30)),
 't-03b':('b02/b02-nurse-donna-wood-dfid.jpg',None),'t-03c':('b03/b03-st-thomas-hospital-apk.jpg',None),
 't-05a':('b05/b05-hsbc-barclays-hailsham.jpg',(C+'/c05a.mp4',.10)),'t-05b':(C+'/c05b.mp4',None),'t-09a':(C+'/c09a.mp4',None),
 't-10a':('b10/b10-farage-official-portrait-crop.jpg',(C+'/c10a.mp4',.12)),'t-10b':('b10/b10-farage-official-portrait-crop.jpg',(C+'/c10b.mp4',3.0,'s')),
 't-11a':('b11/b11-blackburn-town-hall-green.jpg',(C+'/c11a.mp4',.10)),'t-12a':(C+'/c12a.mp4',None),
 't-12b':('b12/b12-trump-fast-food-clemson-2019.jpg',None),'t-12c':(None,None),'t-12d':(None,None)}
def run(a): subprocess.run(a,check=True)
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).decode())
ROWS={r['clip']:r for r in csv.DictReader(open(P+'/renders/MFS topical cut 3.tsv'),delimiter='\t')}
OLD={r['clip']:(float(r['in']),float(r['length'])) for r in csv.DictReader(open(P+'/renders/MFS topical cut 2.tsv'),delimiter='\t')}
WJ=json.load(open(H+'/topical-words.json'))
BANK=open(DOCS+'/money-for-something-joke-bank.md').read()
SCRIPT={f"t-{int(c[:-1]):02d}{c[-1]}":l for c,l in re.findall(r"^\| (\d+[a-d]) \| (.+?) \|$",BANK,re.M)}
BACK=dict(l.rstrip('\n').split('\t') for l in open(H+'/cards3-photos.tsv') if l.strip())
CRED={}
for row in open(DOCS+'/money-for-something-screen-sources.md'):
    c=[x.strip() for x in row.split('|')]
    if len(c)>8 and c[2].startswith('`'): CRED[c[2].strip('`')]=c[7]
def credit(name):
    tv,full=PLAN[name]; used=[u for u in (tv,full and full[0]) if u]
    used+=[BACK[os.path.basename(u)[:-4]] for u in list(used) if u.startswith(C+'/') and os.path.basename(u)[:-4] in BACK]
    out=[]
    for u in used:
        s=CRED.get(os.path.basename(u),'')
        if s and not s.startswith('None owed') and s not in out: out.append(s)
    return ['Photo: '+re.sub(r'\s+',' ',s).rstrip('.') for s in out]
def at_new(R,t): return sum(max(0.0,min(b,t)-a) for a,b in R)
_f={}
def font(size,wght):
    k=(int(size),wght)
    if k not in _f:
        f=ImageFont.truetype(FONT,int(size)); f.set_variation_by_axes([wght]); _f[k]=f
    return _f[k]
norm=lambda s:''.join(re.findall(r"[a-z0-9]+",s.lower()))
def words(name,R):
    """[(text, start, end)] in the tightened clip's time. Heard words give the times; the script gives the spelling where they agree."""
    ws=[list(w) for w in WJ.get(name,{}).get('words',[])]
    m=[]
    for w in ws:                                             # the speech model splits "£29.2" into "£29" and ".2"
        if m and re.match(r'^[.,]\d',w[0]): m[-1][0]+=w[0]; m[-1][2]=w[2]
        else: m.append(w)
    line=SCRIPT.get(name,''); sw=[] if line.startswith('*(') else line.replace('"','').split()
    sm=difflib.SequenceMatcher(None,[norm(x) for x in sw],[norm(x[0]) for x in m])
    for a,b,n in sm.get_matching_blocks():
        for i in range(n): m[b+i][0]=sw[a+i]
    return [(w[0],at_new(R,w[1]),at_new(R,w[2])) for w in m if at_new(R,w[2])>at_new(R,w[1])]
def chunks(ws):
    """Two or three words at a time; never across a full stop, never more than 17 letters, never across a real pause."""
    out=[]; cur=[]
    for i,w in enumerate(ws):
        cur.append(w); nxt=ws[i+1] if i+1<len(ws) else None
        n=sum(len(x[0]) for x in cur)+len(cur)-1
        if (nxt is None or w[0][-1:] in '.?!,' or len(cur)>=3 or n+1+len(nxt[0])>17 or nxt[1]-w[2]>0.28):
            out.append(cur); cur=[]
    return out
def cap_png(ch,path):
    """One caption: white, heavy, a dark soft edge so it reads over the table and his shirt; any figure in the cards' yellow."""
    size=92; f=font(size,800); sp=f.getlength(' ')
    while sum(f.getlength(w[0]) for w in ch)+sp*(len(ch)-1)>W-120: size-=4; f=font(size,800); sp=f.getlength(' ')
    tw=sum(f.getlength(w[0]) for w in ch)+sp*(len(ch)-1)
    def draw(im,fill_of,stroke):
        d=ImageDraw.Draw(im); x=(W-tw)/2
        for w in ch:
            d.text((x,150),w[0],font=f,fill=fill_of(w[0]),anchor='ls',stroke_width=stroke,stroke_fill=(0,0,0,255)); x+=f.getlength(w[0])+sp
    sh=Image.new('RGBA',(W,220),(0,0,0,0)); draw(sh,lambda s:(0,0,0,255),10); sh=sh.filter(ImageFilter.GaussianBlur(7))
    im=Image.new('RGBA',(W,220),(0,0,0,0)); draw(im,lambda s:(YEL if re.search(r'[\d£$]',s) else WHT)+(255,),5)
    Image.alpha_composite(sh,im).save(path)
def furniture(name,path):
    """Everything that does not move: the black card, the show's name, the photo credit."""
    im=Image.new('RGBA',(W,HH),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.rectangle((0,0,W,TOP_Y),fill=(7,9,11,255)); d.rectangle((0,TOP_Y+TOP_H,W,HOST_Y),fill=(7,9,11,255)); d.rectangle((0,HOST_Y+HOST,W,HH),fill=(7,9,11,255))
    f=font(30,650); x=74; d.ellipse((48,66,62,80),fill=YEL+(255,))
    for ch in 'MONEY FOR SOMETHING': d.text((x,84),ch,font=f,fill=WHT+(255,),anchor='ls'); x+=f.getlength(ch)+30*0.14
    cr=' · '.join(credit(name))
    if cr:
        s=19; f=font(s,450)
        while f.getlength(cr)>W-96 and s>12: s-=1; f=font(s,450)
        d.text((48,TOP_Y+TOP_H+STRIP_H/2+1),cr,font=f,fill=(255,255,255,150),anchor='lm')
    im.save(path)
def clip(name,T):
    """One clip of cut 3, rebuilt upright. Returns the file."""
    out=f'{T}/{name}.mkv'
    if os.path.exists(out): return out
    R=[tuple(map(float,x.split('-'))) for x in ROWS[name]['kept'].split()]; t=sum(z-a for a,z in R); k=len(R); src=f'{V}/{name}.mp4'
    tv,full=PLAN[name]; ins=['-i',src]; n=1
    fc=[f"[0:v]split={k}"+''.join(f'[sv{i}]' for i in range(k)),f"[0:a]asplit={k}"+''.join(f'[sa{i}]' for i in range(k))]
    for i,(a,z) in enumerate(R):
        fc.append(f"[sv{i}]trim=start={a:.3f}:end={z:.3f},setpts=PTS-STARTPTS[kv{i}]")
        fc.append(f"[sa{i}]atrim=start={a:.3f}:end={z:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={max(0,z-a-0.012):.3f}:d=0.012[ka{i}]")
    fc.append(''.join(f'[kv{i}][ka{i}]' for i in range(k))+f"concat=n={k}:v=1:a=1[cv][ca];[cv]fps=24,split=2[wide][hsrc]")
    cw,ch,cx,cy=CROP
    fc.append(f"[hsrc]crop={cw}:{ch}:{cx}:{cy},scale={HOST}:{HOST}:flags=lanczos,unsharp=5:5:0.5[host]")
    N=int(t*24)+2
    if tv is None:                                           # nothing on the television: the wide shot goes on top, so the walk-off is seen
        fc.append(f"[wide]scale={W}:{TOP_H}:flags=lanczos[top]")
    else:
        fc.append("[wide]nullsink"); p=SC+'/'+tv
        if tv.startswith(C+'/'): ins+=['-i',p]; fc.append(f"[{n}:v]scale={W}:{TOP_H}:flags=lanczos,setsar=1,fps=24[top0]")
        elif p.endswith('.mp4'): ins+=['-stream_loop','-1','-i',p]; fc.append(f"[{n}:v]scale={W}:{TOP_H}:force_original_aspect_ratio=increase,crop={W}:{TOP_H},setsar=1,fps=24[top0]")
        else:                                                # a still: a slow push in, so nothing on screen is ever frozen
            ins+=['-i',p]; fc.append(f"[{n}:v]scale={W*3}:{TOP_H*3}:force_original_aspect_ratio=increase,crop={W*3}:{TOP_H*3},zoompan=z='1+0.07*on/{N}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={N}:s={W}x{TOP_H}:fps=24,setsar=1[top0]")
        n+=1
        if full:
            card,a=full[:2]; a=a if len(full)>2 else at_new(R,OLD[name][0]+a*OLD[name][1]) if name in OLD else a*t   # the card arrives on the same word as in cut 3; 's' = a time in seconds instead (10b: 'Expat' must not show before he says it)
            ins+=['-itsoffset',f'{a:.3f}','-i',SC+'/'+card]
            fc.append(f"[{n}:v]scale={W}:{TOP_H}:flags=lanczos,setsar=1,fps=24[cd];[top0][cd]overlay=enable='gte(t,{a:.3f})':eof_action=pass[top]"); n+=1
        else: fc.append("[top0]null[top]")
    fp=f'{T}/{name}-f.png'; furniture(name,fp); ins+=['-i',fp]
    fc.append(f"color=c=0x07090B:s={W}x{HH}:r=24:d={t:.3f}[bg];[bg][top]overlay=0:{TOP_Y}:shortest=0:eof_action=pass[b1];[b1][host]overlay=0:{HOST_Y}:eof_action=pass[b2];[b2][{n}:v]overlay=0:0[c0]"); n+=1; last='c0'
    CH=chunks(words(name,R))
    for j,chk in enumerate(CH):
        cp=f'{T}/{name}-c{j}.png'; cap_png(chk,cp); ins+=['-i',cp]
        s=max(0,chk[0][1]-0.04); e=min(chk[-1][2]+0.10,CH[j+1][0][1]-0.045) if j+1<len(CH) else chk[-1][2]+0.25   # one caption at a time, never two
        fc.append(f"[{last}][{n}:v]overlay=0:{CAP_Y-150+35}:enable='between(t,{s:.3f},{e:.3f})'[c{j+1}]"); last=f'c{j+1}'; n+=1
    fc.append(f"[{last}]format=yuv420p[v]")
    spoken=bool(WJ.get(name,{}).get('words'))
    fc.append("[ca]"+("loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000" if spoken else "volume=0")+"[a]")
    run(['ffmpeg','-v','error','-y']+ins+['-filter_complex',';'.join(fc),'-map','[v]','-map','[a]','-t',f'{t:.3f}','-r','24',
         '-c:v','libx264','-crf','12','-preset','fast','-pix_fmt','yuv420p','-c:a','pcm_s16le','-ar','48000','-ac','2',out])
    return out
def build(short,T):
    parts=[clip(n,T) for n in SHORTS[short]]; final=f'{OUT}/{short}.mp4'; ins=[]
    for p_ in parts: ins+=['-i',p_]
    n=len(parts); fc=''.join(f'[{i}:v][{i}:a]' for i in range(n))+f'concat=n={n}:v=1:a=1[v][a]'
    run(['ffmpeg','-v','error','-y']+ins+['-filter_complex',fc,'-map','[v]','-map','[a]','-r','24','-c:v','libx264','-profile:v','high','-level','4.1','-crf','18','-preset','slow',
         '-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv','-c:a','aac','-b:a','192k','-ar','48000','-ac','2','-movflags','+faststart',final])
    d=dur(final); cols=6; rows=max(1,min(6,round(d/2.5/cols+0.5)))
    run(['ffmpeg','-v','error','-y','-i',final,'-vf',f"fps={cols*rows}/{d:.2f},scale=270:480,tile={cols}x{rows}",'-frames:v','1',f'{OUT}/sheets/{short}.jpg'])
    print(f'{short}\t{d:.1f} s\t{len(parts)} clips',flush=True)
if __name__=='__main__':
    os.makedirs(OUT+'/sheets',exist_ok=True); T=os.path.expanduser('~/.cache/badcode-mfs-shorts'); os.makedirs(T,exist_ok=True)
    for s in (sys.argv[1:] or list(SHORTS)): build(s,T)
