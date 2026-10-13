#!/usr/bin/env python3
"""Money For Something, the topical monologue: the television's stat cards, third style (11 Oct 2026).
Jack on cut 2: "the font for the graphics look old and boring please make a sleeker more modern design". He liked the photos.
Cut 2's cards (build-topical-cards.py) were condensed poster capitals (Anton, Bebas Neue) with hard drop shadows and a yellow slab.
These keep the same photos, numbers and wording and change the dress: Inter Tight, left aligned, sentence case, a small tracked
label with a coloured dot, one big number in the accent colour with its unit set smaller in white, a hairline, the source in small
grey type. The photo is darkened by a soft gradient from the left instead of a flat wash, so no shadows are needed.
Everything eases in (slide up and fade) and the number counts up and settles.
Drawn frame by frame with Pillow and piped to ffmpeg, because drawtext cannot track letters, mix weights on a line or ease.
All type stays inside the middle 860 px, so the same file works full screen and cropped into the television.
Type: Inter Tight (SIL Open Font Licence, fonts/OFL-InterTight.txt).
Writes <root>/screen/cards3/<id>.mp4 and cards3-photos.tsv (which photo sits behind which card, for the credits).
usage: ~/.cache/badcode-whisper/venv/bin/python build-topical-cards3.py [--still SECONDS DIR] [id ...]"""
import os,subprocess,sys
from multiprocessing import Pool
from PIL import Image,ImageDraw,ImageFont,ImageFilter
H=os.path.dirname(os.path.abspath(__file__))
P='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/october/screen'; O='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/2026/screen/cards'; os.makedirs(O,exist_ok=True)
FONT=H+'/../fonts/InterTight.ttf'
W,Hh,FPS,D=1280,720,24,12
L,MAXW=220,850                                   # left edge of all type, and the widest a line may be
YEL=(250,204,21); RED=(255,84,72); GRN=(61,220,132); WHT=(255,255,255); GREY=(255,255,255,150)
_f={}
def font(size,wght):
    k=(int(size),wght)
    if k not in _f:
        f=ImageFont.truetype(FONT,int(size)); f.set_variation_by_axes([wght]); _f[k]=f
    return _f[k]
def ease(t,at,dur=0.55):
    p=min(1.0,max(0.0,(t-at)/dur)); return 1-(1-p)**3
def count(v,dec=0,at=0.25,dur=1.1):
    """A number that counts up to v and settles (eased, so it slows into the figure)."""
    def f(t):
        x=v*ease(t,at,dur)
        return f"{x:.{dec}f}" if dec else f"{int(x):,}"
    return f
def runs_width(runs,size,wght,track,t):
    w=0
    for r in runs:
        s=r[0](t) if callable(r[0]) else r[0]; sc=r[2] if len(r)>2 else 1.0; f=font(size*sc,wght)
        w+=sum(f.getlength(c)+track*size*sc for c in s)
    return w
def draw_runs(d,x,y,runs,size,wght,track,alpha,t):
    for r in runs:
        s=r[0](t) if callable(r[0]) else r[0]; col=r[1]; sc=r[2] if len(r)>2 else 1.0; f=font(size*sc,wght)
        for c in s:
            d.text((x,y),c,font=f,fill=col[:3]+(int(255*alpha*(col[3]/255 if len(col)>3 else 1)),),anchor='ls'); x+=f.getlength(c)+track*size*sc
# one line of a card: kind, runs, size, weight, tracking (em), height of its box (em), gap after (px)
def label(text,col=YEL): return dict(k='label',runs=[(text.upper(),WHT)],size=25,w=650,tr=0.14,box=1.0,gap=30,dot=col)
def big(runs,size=210,gap=30):   return dict(k='big',runs=runs,size=size,w=800,tr=-0.035,box=0.80,gap=gap)
def sub(text,size=46,col=WHT,gap=16): return dict(k='sub',runs=[(text,col)],size=size,w=500,tr=-0.005,box=1.12,gap=gap)
def head(text):                  return dict(k='head',runs=[(text,(255,255,255,200))],size=32,w=500,tr=0.0,box=1.1,gap=10)
def rule(col):                   return dict(k='rule',col=col,size=1,box=3,gap=26)
def gap(px):                     return dict(k='gap',size=1,box=px,gap=0)
def backdrop(bg):
    if bg:
        im=Image.open(f'{P}/{bg}').convert('RGB'); s=max(1408/im.width,792/im.height)
        im=im.resize((round(im.width*s)+1,round(im.height*s)+1),Image.LANCZOS); x=(im.width-1408)//2; y=(im.height-792)//2
        im=im.crop((x,y,x+1408,y+792)).filter(ImageFilter.GaussianBlur(2.2))
        im=Image.blend(im,Image.new('RGB',im.size,(8,10,14)),0.34)
    else:
        im=Image.new('RGB',(1408,792),(10,12,17))
    return im
def scrim(plain):
    """Dark on the left where the type sits, clear on the right where the face usually is; a little at the foot for the source."""
    g=Image.new('L',(W,1)); g.putdata([int(255*(0.20 if plain else 0.86-0.62*min(1,x/980)**1.3)) for x in range(W)]); a=g.resize((W,Hh))
    v=Image.new('L',(1,Hh)); v.putdata([int(255*0.55*max(0,(y-470)/250)**1.5) for y in range(Hh)]); a2=v.resize((W,Hh))
    from PIL import ImageChops
    s=Image.new('RGBA',(W,Hh),(6,8,12,0)); s.putalpha(ImageChops.lighter(a,a2)); return s
def frame(c,bgim,sc,t):
    dx,dy=64*t/D,36*t/D
    im=bgim.crop((int(dx),int(dy),int(dx)+W,int(dy)+Hh)).convert('RGBA'); im.alpha_composite(sc)
    ov=Image.new('RGBA',(W,Hh),(0,0,0,0)); d=ImageDraw.Draw(ov)
    lines=c['lines']; total=sum(l['size']*l['box']+l['gap'] for l in lines)-lines[-1]['gap']
    y=(Hh-36-total)/2+8; at=0.10
    for l in lines:
        h=l['size']*l['box']; e=ease(t,at); rise=(1-e)*26
        if l['k']=='gap': y+=h; continue
        if l['k']=='rule':
            d.rectangle([L,y+rise,L+int(120*ease(t,at,0.7)),y+rise+3],fill=l['col']+(int(255*e),))
        else:
            size=l['size']; full=runs_width(l['runs'],size,l['w'],l['tr'],D)
            x=L
            if l['k']=='label':
                r=7; cy=y+h*0.5+rise; d.ellipse([L,cy-r,L+2*r,cy+r],fill=l['dot']+(int(255*e),)); x=L+2*r+14
            if full>MAXW-(x-L): size=size*(MAXW-(x-L))/full
            base=y+rise+(h+size*0.72)/2 if l['k']!='big' else y+rise+l['size']*l['box']-(l['size']*l['box']-size*0.727)/2
            draw_runs(d,x,base,l['runs'],size,l['w'],l['tr'],e,t)
        y+=h+l['gap']; at+=l.get('wait',0.22)
    if c.get('src'):
        e=ease(t,1.5,0.6); f=font(21,450)
        d.rectangle([L,650,L+MAXW,650],fill=(255,255,255,int(46*e)))
        d.text((L,680),c['src'],font=f,fill=(255,255,255,int(150*e)),anchor='ls')
    im.alpha_composite(ov); return im.convert('RGB')
CARDS=[]
def card(cid,bg,lines,src=''): CARDS.append(dict(id=cid,bg=bg,lines=lines,src=('Source: '+src) if src else ''))
def render(i):
    c=CARDS[i]; bgim=backdrop(c['bg']); sc=scrim(not c['bg'])
    p=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{Hh}','-r',str(FPS),'-i','-','-an','-c:v','libx264','-crf','16','-preset','medium','-pix_fmt','yuv420p',
        '-vf','scale=out_color_matrix=bt709:out_range=tv','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv',f"{O}/{c['id']}.mp4"],stdin=subprocess.PIPE)
    for i in range(D*FPS): p.stdin.write(frame(c,bgim,sc,i/FPS).tobytes())
    p.stdin.close(); p.wait(); return c['id']
bn=lambda col=WHT:('bn',col,0.56); m_=lambda col=WHT:('m',col,0.56)
card('ident',None,[label('A transmission'),big([('Money for',WHT)],150,gap=30),big([('something',YEL)],150),rule(YEL),sub('2026',40)])
card('c00',None,[label('The year'),big([('2026',WHT)],330)])
card('c01',None,[label('Two dates'),head('Epstein files released'),big([('30 January',WHT)],120,gap=34),dict(head('First strikes on Iran'),wait=0.9),big([('28 February',WHT)],120)])
card('c03','b04/b04-esso-forecourt-empty.jpg',[label('Diesel, 2 October',RED),big([('£',RED),(count(2.00,2),RED)],260),rule(RED),sub('A litre')])
card('c04','../../2026/screen/photos/p-iran-1953-tehran-rally.jpg',[label('Iran, since'),big([('1953',WHT)],330)])
card('c05','b04/b04-trump-oval-office-aug-2026.jpg',[label('D. Trump, 7 April'),big([('“A whole civilisation',WHT)],92,gap=26),big([('will die tonight”',YEL)],92),rule(YEL)])
card('c07','b03/b03-patriot-launch-balikatan.jpg',[label('Who did well',GRN),head('The Pentagon asked for'),big([('+$',GRN),(count(200),GRN),bn()],130,gap=28),dict(head('Lockheed missile contract, up to'),wait=0.9),big([('$',GRN),(count(58.6,1,at=1.5),GRN),bn()],130)])
card('c08','../../2026/screen/photos/p-helmand-patrol-2011.jpg',[label("America's wars since 9/11",RED),big([('$',RED),(count(8),RED),(' trillion',WHT,0.5)],230),rule(RED),sub('About 900,000 people killed')],'Brown University, Costs of War')
card('c10','../../2026/screen/photos/p-taliban-humvee-kabul-2021.png',[label('Afghanistan'),big([('Taliban',WHT)],190,gap=30),rule(YEL),sub('Back in power, 2021')])
card('c11','../../2026/screen/photos/p-nuclear-baker-1946.jpg',[label('Nuclear weapons, the world',RED),big([('$',RED),(count(3768,at=0.25,dur=2.4),RED)],250),rule(RED),sub('Every second')])
card('c14',None,[label('3 January'),big([('Venezuela',WHT)],190)])
card('c15','b10/b10-farage-official-portrait-crop.jpg',[label('Clacton by-election'),head('N. Farage'),big([('22,239',WHT)],130,gap=28),dict(head('Count Binface, a bin'),wait=0.9),big([('9,455',YEL)],130)])
card('c16',None,[label('Voted to leave the UK'),big([('Piddington',WHT)],170,gap=30),rule(YEL),sub('285 to 26')])
card('c18',None,[label('Asylum housing, three companies',GRN),big([('£',GRN),(count(380),GRN),m_()],230),rule(GRN),sub('Clearsprings · Serco · Mears',40)])
card('c20',None,[label('PPE wasted',RED),big([('£',RED),(count(9.9,1),RED),bn()],240),rule(RED)],'Covid inquiry, July 2026')
card('c22','../../2026/screen/photos/p-euro-notes.jpg',[label('A Sunday night'),big([('9 May 2010',WHT)],170)])
card('c23','../../2026/screen/photos/p-hs2-wendover-2026.jpg',[label('HS2',RED),head('Up to'),big([('£',RED),(count(102.7,1),RED),bn()],210),rule(RED),sub('Opening: 2036 to 2039')],'Department for Transport, May 2026')
card('c25','../../2026/screen/photos/p-parliament-2022.jpg',[label('Written off in one year',RED),big([('£',RED),(count(6.6,1),RED),bn()],250),rule(RED)],'Public Accounts Committee, May 2026')
if __name__=='__main__':
    a=sys.argv[1:]
    if a and a[0]=='--still':
        t=float(a[1]); out=a[2]; os.makedirs(out,exist_ok=True)
        for c in CARDS:
            if a[3:] and c['id'] not in a[3:]: continue
            frame(c,backdrop(c['bg']),scrim(not c['bg']),t).save(f"{out}/{c['id']}.jpg",quality=90)
        sys.exit()
    todo=[i for i,c in enumerate(CARDS) if not a or c['id'] in a]   # indices: the count-up closures do not pickle
    with Pool(6) as pool:
        for cid in pool.imap_unordered(render,todo): print('card',cid,flush=True)
    if not a: open(H+'/cards-photos.tsv','w').write('\n'.join(f"{c['id']}\t{c['bg']}" for c in CARDS if c['bg'])+'\n')
