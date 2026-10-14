#!/usr/bin/env python3
"""Money For Something 2026: the television's stat cards, fourth style (14 Oct 2026).
Jack on cut 3: "the font of the graphics and overall style when showing stats, gets a bit boring please make that more
exciting and sleeker". October's third style (Inter Tight on a dark photo, a number that counts up) was liked as sleek but
every card looked the same, and the count-up showed wrong numbers on screen ("£177m" for half a second).
This style keeps it clean and adds punch:
- colour: each card is one loud field. Yellow = a plain fact, red = money lost or people killed, green = who did well.
  A photo card is a two-tone print of its photo in that colour (shadows ink, highlights colour), not a darkened photo.
- type: Archivo Expanded Black for the number (wide and heavy, not the condensed poster capitals Jack called old),
  Space Mono Bold in a white tag for the label, Archivo for the small lines.
- motion: a two-frame "transmission" glitch on entry (the host is from the future), the label slides in, the number
  slams in (scale overshoot) with a small camera shake, a marker bar sweeps under the sub-line. No counting: the right
  number is on screen from its first frame.
Writes <root>/screen/cards4/<id>.mp4, cards4-photos.tsv and cards4-boxes.json (the box round the type, so the cut
builder can fill the television with it).
usage: ~/.cache/badcode-whisper/venv/bin/python build-cards4-2026.py [--still SECONDS DIR] [id ...]"""
import os,subprocess,sys,json,random
from multiprocessing import Pool
from PIL import Image,ImageDraw,ImageFont,ImageFilter,ImageOps,ImageChops
H=os.path.dirname(os.path.abspath(__file__))
OCT='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/october/screen'
O='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/2026/screen/cards4'; os.makedirs(O,exist_ok=True)
FD=H+'/../fonts/'; ARC=FD+'Archivo.ttf'; MONO=FD+'SpaceMono-Bold.ttf'
W,Hh,FPS,D=1280,720,24,12
L,MAXW=150,980
INK=(12,12,16); WHT=(255,255,255)
PAL={'yel':dict(bg=(250,204,21),fg=INK,acc=INK,tag=INK,tagfg=(250,204,21)),
     'red':dict(bg=(232,44,48),fg=WHT,acc=(255,214,0),tag=WHT,tagfg=INK),
     'grn':dict(bg=(30,215,96),fg=INK,acc=INK,tag=INK,tagfg=(30,215,96)),
     'ink':dict(bg=INK,fg=WHT,acc=(250,204,21),tag=(250,204,21),tagfg=INK)}
_f={}
def arc(size,wght=900,wdth=125):
    k=('a',int(size),wght,wdth)
    if k not in _f:
        f=ImageFont.truetype(ARC,max(8,int(size))); f.set_variation_by_axes([wght,wdth]); _f[k]=f
    return _f[k]
def mono(size):
    k=('m',int(size))
    if k not in _f: _f[k]=ImageFont.truetype(MONO,int(size))
    return _f[k]
def ease(t,at,dur=0.45):
    p=min(1.0,max(0.0,(t-at)/dur)); return 1-(1-p)**3
def back(t,at,dur=0.32,s=2.2):
    """Ease-out-back: overshoots and settles (the slam)."""
    p=min(1.0,max(0.0,(t-at)/dur)); p-=1; return 1+(s+1)*p**3+s*p**2
def photo(path,col):
    im=Image.open(path).convert('L'); s=max(1360/im.width,766/im.height)
    im=im.resize((round(im.width*s)+1,round(im.height*s)+1),Image.LANCZOS); x=(im.width-1360)//2; y=(im.height-766)//2
    im=ImageOps.autocontrast(im.crop((x,y,x+1360,y+766)),cutoff=1)
    return ImageOps.colorize(im,black=(8,8,12),white=col,mid=tuple(int(c*0.55) for c in col))
# a line: kind, text (or list of (text, scale, colour-key)), size, gap after
def tag(text): return dict(k='tag',text=text.upper(),size=24,gap=26)
def big(runs,size=200,gap=30): return dict(k='big',runs=runs if isinstance(runs,list) else [(runs,1.0,'fg')],size=size,gap=gap)
def sub(text,size=46,gap=14,mark=True): return dict(k='sub',text=text,size=size,gap=gap,mark=mark)
def head(text,size=30,gap=6): return dict(k='head',text=text,size=size,gap=gap)
CARDS=[]
def card(cid,pal,lines,bg=None,src='',out=None): CARDS.append(dict(id=cid,pal=pal,lines=lines,bg=bg,src=src,out=out))
def layout(c,size_of):
    """Measure each line (shrink any line wider than MAXW) and stack them, centred vertically."""
    out=[]; y=0
    for l in c['lines']:
        if l['k']=='big':
            w=sum(arc(l['size']*sc).getlength(t)-0.02*l['size']*sc*len(t) for t,sc,_ in l['runs']); s=min(1.0,MAXW/w) if w else 1
            h=l['size']*s*0.76; out.append((l,s,y,h)); y+=h+l['gap']
        elif l['k']=='tag':
            h=l['size']*1.9; out.append((l,1,y,h)); y+=h+l['gap']
        else:
            f=arc(l['size'],700 if l['k']=='sub' else 500,100); w=f.getlength(l['text']); s=min(1.0,MAXW/w)
            h=l['size']*s*1.15; out.append((l,s,y,h)); y+=h+l['gap']
    top=(Hh-y)/2-10
    return [(l,s,top+y0,h) for l,s,y0,h in out]
def frame(c,bgim,t,lay):
    P=PAL[c['pal']]
    if bgim is not None: col=P['bg']; P=dict(bg=col,fg=WHT,acc=col,tag=col,tagfg=INK)   # on a photo: white type, the colour as tag and marker
    fg=lambda k:P[k] if k in P else k
    # background: a slow push on the two-tone photo, or the flat colour
    if bgim is not None:
        z=1+0.05*t/D; w,h=int(1360/z),int(766/z); x,y=(1360-w)//2,(766-h)//2
        im=bgim.crop((x,y,x+w,y+h)).resize((W,Hh),Image.BILINEAR).convert('RGBA')
        g=Image.new('L',(W,1)); g.putdata([int(255*(0.82-0.50*min(1,x/1050))) for x in range(W)])
        im.alpha_composite(Image.merge('RGBA',[Image.new('L',(W,Hh),v) for v in INK]+[g.resize((W,Hh))]))
    else:
        im=Image.new('RGBA',(W,Hh),P['bg']+(255,))
    ov=Image.new('RGBA',(W,Hh),(0,0,0,0)); d=ImageDraw.Draw(ov)    # drawn on its own layer: ImageDraw on the frame itself writes alpha straight through, so nothing faded
    shake=(0,0); at=0.10; slam_at=[]
    for l,s,y,h in lay:
        e=ease(t,at)
        if l['k']=='tag':
            f=mono(l['size']); tw=f.getlength(l['text'])+2*0.12*l['size']*len(l['text'])/len(l['text'])
            x0=L-(1-e)*60; pad=16
            if e>0:
                d.rounded_rectangle([x0,y,x0+tw+2*pad,y+h],radius=h/2,fill=P['tag']+(int(255*e),))
                d.text((x0+pad,y+h/2+1),l['text'],font=f,fill=P['tagfg']+(int(255*e),),anchor='lm')
            at+=0.18
        elif l['k']=='big':
            k=back(t,at); a=min(1.0,max(0.0,(t-at)/0.08)); slam_at.append(at)
            if a>0:
                sc=s*(1.35-0.35*k)          # 1.35x -> overshoots below 1 -> 1
                x=L; base=y+h
                lay_runs=[]
                for txt,r,colk in l['runs']:
                    f=arc(l['size']*sc*r); lay_runs.append((txt,f,fg(colk)))
                # scale about the line's left baseline so the slam lands in place
                for txt,f,col in lay_runs:
                    for ch in txt:
                        d.text((x,base),ch,font=f,fill=col+(int(255*a),),anchor='ls'); x+=f.getlength(ch)-0.02*f.size
            at+=l.get('wait',0.55)
        else:
            f=arc(l['size']*s,700 if l['k']=='sub' else 500,100); x=L-(1-e)*24
            if l['k']=='sub' and l.get('mark'):
                m=ease(t,at+0.12,0.35); tw=f.getlength(l['text'])
                if m>0: d.rectangle([L-8,y+h*0.18,L-8+(tw+16)*m,y+h*0.98],fill=P['acc']+(255,))
                col=INK if P['acc']!=INK else P['bg']       # type knocked out of the marker bar
                d.text((x,y+h*0.82),l['text'],font=f,fill=(col if m>0.5 else fg('fg'))+(int(255*e),),anchor='ls')
            else:
                d.text((x,y+h*0.82),l['text'],font=f,fill=fg('fg')+(int(220*e),),anchor='ls')
            at+=0.22
    # the slam's shake: three frames, decaying
    for sa in slam_at:
        dt=t-sa-0.20
        if 0<=dt<0.16: r=random.Random(int(t*FPS)); amp=7*(1-dt/0.16); shake=(r.uniform(-amp,amp),r.uniform(-amp,amp))
    if c['src']:
        e=ease(t,1.2); d.text((L,Hh-34),c['src'].upper(),font=mono(15),fill=fg('fg')+(int(150*e),),anchor='ls')
    d.text((W-60,44),'MFS/26',font=mono(16),fill=fg('fg')+(110,),anchor='rs')
    im.alpha_composite(ov); im=im.convert('RGB')
    if shake!=(0,0): im=ImageChops.offset(im,int(shake[0]),int(shake[1]))
    # the transmission glitch on entry: sliced rows pushed sideways and the red channel split off
    out=c.get('out')
    if t<0.13 or (out and t>=out):                 # the title also glitches out
        r=random.Random(int(t*FPS)+7); a=im.copy()
        for _ in range(9):
            y0=r.randrange(0,Hh-40); hh=r.randrange(8,60); dx=r.randrange(-90,90)
            a.paste(im.crop((0,y0,W,y0+hh)),(dx,y0))
        R,G,B=a.split(); a=Image.merge('RGB',(ImageChops.offset(R,10,0),G,ImageChops.offset(B,-6,0)))
        im=Image.blend(a,Image.new('RGB',(W,Hh),WHT),0.25 if t<0.05 else 0.0)
        if out and t>=out: im=Image.blend(im,Image.new('RGB',(W,Hh),INK),min(1.0,(t-out)/0.17))
    return im
def box(c,lay):
    """The box round all the type on the settled card (for the television crop)."""
    x1=L; y0=lay[0][2]; y1=lay[-1][2]+lay[-1][3]
    for l,s,y,h in lay:
        if l['k']=='big': w=sum(arc(l['size']*s*r).getlength(t)-0.02*l['size']*s*r*len(t) for t,r,_ in l['runs'])
        elif l['k']=='tag': w=mono(l['size']).getlength(l['text'])+40
        else: w=arc(l['size']*s,700,100).getlength(l['text'])+10
        x1=max(x1,L+w)
    return [L-20,int(y0-20),int(x1+20),int(y1+24)]
def bg_of(c): return photo(c['bg'],PAL[c['pal']]['bg']) if c['bg'] else None
def render(i):
    c=CARDS[i]; bgim=bg_of(c); lay=layout(c,None)
    p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{Hh}','-r',str(FPS),'-i','-','-an','-c:v','libx264','-crf','16','-preset','medium','-pix_fmt','yuv420p',
        '-vf','scale=out_color_matrix=bt709:out_range=tv','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv',f"{O}/{c['id']}.mp4"],stdin=subprocess.PIPE)
    for k in range(D*FPS): p.stdin.write(frame(c,bgim,k/FPS,lay).tobytes())
    p.stdin.close(); p.wait(); return c['id']
P26='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/2026/screen/photos/'
u=lambda t,r=0.42,col='fg':(t,r,col)
card('ident','yel',[tag('A transmission'),big('Money for',150,gap=8),big('something',150,gap=22),sub('2026',40)])
card('title','yel',[tag('A transmission from the future'),dict(big('Money for',190,gap=6),wait=0.18),big('something',190,gap=26),sub('2026',54)],out=2.45)   # the sting after the cold open (Jack, 14 Oct: "add this")
card('pod','ink',[tag('Now streaming'),big([('The biggest',1.0,'fg')],120,gap=8),big([('podcast of 2026',1.0,'acc')],120)],out=2.45)   # round 2: into the podcast parody
card('c00','yel',[tag('The year'),big('2026',330)])
card('c01','ink',[tag('Two dates'),head('Epstein files released'),big([('30 Jan',1.0,'fg')],150,gap=26),dict(head('First strikes on Iran'),),dict(big([('28 Feb',1.0,'acc')],150))])
card('c03','red',[tag('Diesel, 2 October'),big([('£2.00',1.0,'fg')],250),sub('a litre. A record.')],bg=OCT+'/b04/b04-esso-forecourt-empty.jpg')
card('c04','yel',[tag('Iran, since'),big('1953',330)],bg=P26+'p-iran-1953-tehran-rally.jpg')
card('c05','yel',[tag('D. Trump, 7 April'),big('“A whole',120,gap=4),big('civilisation',120,gap=4),big('will die tonight”',120,gap=34),dict(sub('“I don’t want that to happen, but it probably will.”',38),wait=0.9)],bg=OCT+'/b04/b04-trump-oval-office-aug-2026.jpg')   # cut 4 fix (Jack): the whole quote is on the card, so the second sentence is not read as the host's
card('c07','grn',[tag('Who did well'),head('The Pentagon asked for'),big([('+$200',1.0,'fg'),u('bn')],140,gap=20),head('Lockheed missile contract'),dict(big([('$58.6',1.0,'fg'),u('bn')],140))],bg=OCT+'/b03/b03-patriot-launch-balikatan.jpg')
card('c08','red',[tag("America's wars since 9/11"),big([('$8',1.0,'fg'),u(' trillion',0.36)],260),sub('About 900,000 people killed')],bg=P26+'p-helmand-patrol-2011.jpg',src='Brown University, Costs of War')
card('c10','yel',[tag('Afghanistan, 2021'),big('Taliban',200),sub('Back in charge')],bg=P26+'p-taliban-humvee-kabul-2021.png')
card('c11','red',[tag('Nuclear weapons, the world'),big('$3,768',250),sub('Every. Single. Second.')],bg=P26+'p-nuclear-baker-1946.jpg')
card('c14','yel',[tag('3 January'),big('Venezuela',190)])
card('c15','yel',[tag('Clacton by-election'),head('N. Farage'),big('22,239',140,gap=20),head('Count Binface, a bin'),big([('9,455',1.0,'fg')],140)],bg=OCT+'/b10/b10-farage-official-portrait-crop.jpg')
card('c16','yel',[tag('Voted to leave the UK'),big('Piddington',180),sub('285 to 26')])
card('c18','grn',[tag('Asylum housing, 2019 to 2024'),big([('£380',1.0,'fg'),u('m')],250),sub('Clearsprings · Serco · Mears')],src='Profit, three firms, Sept 2019 to Aug 2024')
card('c19','ink',[tag('£380m ÷ £3.85'),big([('98.7',1.0,'acc'),u(' million',0.34)],230),sub('meal deals')])
card('c20','red',[tag('PPE wasted'),big([('£9.9',1.0,'fg'),u('bn')],250),sub('= 2.5 billion meal deals')],src='Covid inquiry, July 2026')
card('c22','yel',[tag('A Sunday night'),big('9 May 2010',170)],bg=P26+'p-euro-notes.jpg')
card('c23','red',[tag('HS2'),head('Up to'),big([('£102.7',1.0,'fg'),u('bn')],210),sub('Opening: 2036 to 2039')],bg=P26+'p-hs2-wendover-2026.jpg',src='Department for Transport, May 2026')
card('c25','red',[tag('Written off in one year'),big([('£6.6',1.0,'fg'),u('bn')],260)],bg=P26+'p-parliament-2022.jpg',src='Public Accounts Committee, May 2026')
if __name__=='__main__':
    a=sys.argv[1:]
    if a and a[0]=='--still':
        t=float(a[1]); out=a[2]; os.makedirs(out,exist_ok=True)
        for c in CARDS:
            if a[3:] and c['id'] not in a[3:]: continue
            frame(c,bg_of(c),t,layout(c,None)).save(f"{out}/{c['id']}.jpg",quality=90)
        sys.exit()
    todo=[i for i,c in enumerate(CARDS) if not a or c['id'] in a]
    with Pool(6) as pool:
        for cid in pool.imap_unordered(render,todo): print('card',cid,flush=True)
    json.dump({c['id']:box(c,layout(c,None)) for c in CARDS},open(H+'/cards4-boxes.json','w'))
    if not a: open(H+'/cards4-photos.tsv','w').write('\n'.join(f"{c['id']}\t{c['bg']}" for c in CARDS if c['bg'])+'\n')
