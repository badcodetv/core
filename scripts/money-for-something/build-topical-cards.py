#!/usr/bin/env python3
"""Money For Something, the topical monologue: the television's stat cards, second style (10 Oct 2026, evening).
Jack on cut 1: "the graphics on the tv screen looks really boring, please change the style, as in when it says stats."
Cut 1's cards were static teletext pages on black. These are 12-second animated cards, 1280x720 at 24 fps:
a real photo of the subject behind (darkened, drifting), a yellow label that slides in, one huge number that counts up,
a second line that fades in, and the source small at the bottom. One idea a card, readable in about three seconds.
All type stays inside the middle 860 px, so the same file works full screen and cropped into the television.
Type: Anton and Bebas Neue (SIL Open Font Licence, fonts/OFL.txt). Our own graphics; no broadcaster's furniture is copied.
Writes <root>/screen/cards2/<id>.mp4 and cards2-photos.tsv (which photo sits behind which card, for the credits).
usage: python3 build-topical-cards.py [id ...]"""
import os,subprocess,sys,tempfile
H=os.path.dirname(os.path.abspath(__file__))
P='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/screen'; O=P+'/cards2'; os.makedirs(O,exist_ok=True)
AN=H+'/fonts/Anton-Regular.ttf'; BB=H+'/fonts/BebasNeue-Regular.ttf'
YEL='0xFFD400'; RED='0xFF3B30'; GRN='0x35E06F'; WHT='white'
T=tempfile.mkdtemp(); K=[0]; D=12
def tf(s):
    K[0]+=1; p=f'{T}/{K[0]}.txt'; open(p,'w').write(s); return p
def up(v,dec=0,dur=0.9,at=0.25):
    """drawtext expansion for a number counting up to v, starting at `at` seconds."""
    V=f"min({v},{v}*max(0,t-{at})/{dur})"
    if dec: return f"%{{eif:trunc({V}):d}}.%{{eif:mod(trunc({V}*10),10):d}}"
    return f"%{{eif:trunc({V}):d}}"
def txt(text,font,size,y,col=WHT,at=0.0,x='(w-text_w)/2',fade=0.22,shadow=4,box=None):
    a=f"if(lt(t\\,{at})\\,0\\,min(1\\,(t-{at})/{fade}))"
    b=f":box=1:boxcolor={box}:boxborderw=18" if box else ""
    return f"drawtext=fontfile={font}:textfile={tf(text)}:fontcolor={col}:fontsize={size}:x={x}:y={y}:alpha='{a}':shadowcolor=black@0.85:shadowx={shadow}:shadowy={shadow}{b}"
def label(text,y=70,at=0.0):
    """The yellow label: black type on a yellow slab, sliding in from the left."""
    x=f"230-520*max(0\\,1-(t-{at})/0.28)"
    return f"drawtext=fontfile={BB}:textfile={tf(text)}:fontcolor=black:fontsize=58:x='{x}':y={y}:box=1:boxcolor={YEL}:boxborderw=16:enable='gte(t\\,{at})'"
def bar(y,frac,col,at):
    """A short rule under a number, appearing with it. Not a chart: the two figures on a card are often different currencies or periods."""
    return f"drawbox=x=230:y={y}:w=160:h=10:color={col}:t=fill:enable='gte(t\\,{at})'"
def card(cid,bg,layers,src=''):
    if only and cid not in only: return
    f=[]
    if bg:
        ins=['-loop','1','-t',str(D),'-i',f'{P}/{bg}']
        f.append(f"scale=1408:792:force_original_aspect_ratio=increase,crop=1408:792,crop=1280:720:x='64*t/{D}':y='36*t/{D}',eq=saturation=0.9:brightness=-0.07:contrast=1.06,gblur=sigma=1.6,drawbox=x=0:y=0:w=1280:h=720:color=black@0.30:t=fill,vignette=PI/4.5")
        photos.append(f"{cid}\t{bg}")
    else:
        ins=['-f','lavfi','-t',str(D),'-i',f"gradients=s=1280x720:c0=0x2A0606:c1=0x050508:x0=0:y0=0:x1=1280:y1=720:d={D}:speed=0.01"]
        f.append("vignette=PI/3.4")
    f+=layers
    if src: f.append(f"drawtext=fontfile={BB}:textfile={tf('SOURCE: '+src.upper())}:fontcolor=white@0.72:fontsize=26:x=(w-text_w)/2:y=664:shadowcolor=black:shadowx=2:shadowy=2")
    f.append("fps=24,format=yuv420p")
    subprocess.run(['ffmpeg','-v','error','-y']+ins+['-vf',','.join(f),'-an','-c:v','libx264','-crf','17','-preset','medium','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv',f'{O}/{cid}.mp4'],check=True)
    print('card',cid)
only=sys.argv[1:]; photos=[]
card('c01a','../stills/plate-B.jpg',[txt('MONEY FOR',AN,150,150,YEL,0.15),txt('SOMETHING',AN,150,320,YEL,0.45),txt("THE NEWS, FROM A MAN WHO'S ALREADY SEEN IT",BB,44,540,WHT,1.1)])
card('c01b','b01/b01-burnham-arrives-no10.jpg',[label('WHAT BRITAIN PAYS TO BORROW'),txt('HIGHEST',AN,210,170,WHT,0.3),txt('SINCE 1998',AN,150,410,YEL,0.9)],'several outlets, October 2026')
card('c01c','b01/b01-google-page-brin-2003.jpg',[label('ALSO THAT YEAR'),txt('1998',AN,300,150,WHT,0.25),txt('GOOGLE IS FOUNDED',BB,84,520,YEL,0.9)])
card('c02a','b02/b02-clap-street-budd-2.jpg',[label("NURSES' PAY RISE"),txt('NO',AN,360,150,RED,0.55,fade=0.06,shadow=8),txt('SIGNED BY THE PRIME MINISTER AND THE CHANCELLOR',BB,44,570,WHT,1.3)],'The Times; GB News')
card('c03a','b03/b03-patriot-launch-balikatan.jpg',[label('EXTRA FOR DEFENCE'),txt('+£'+up(25)+'bn',AN,270,150,GRN),txt('EVERY YEAR, BY 2035',BB,84,520,WHT,1.3)],'Institute for Fiscal Studies, June 2026')
card('c04a','b04/b04-trump-oval-office-aug-2026.jpg',[label('NO NEW ATTACK ON IRAN'),txt('“PRIOR TO THE',AN,120,190,WHT,0.3),txt('MIDTERM ELECTIONS”',AN,120,340,YEL,0.7),txt('D. TRUMP, 8 OCTOBER 2026',BB,56,540,WHT,1.4)],'CNN; Washington Post')
card('c05a','b05/b05-barclays-hsbc-london.jpg',[label('WHO IS UP'),
    txt('BIG FOUR BANKS · SIX MONTHS',BB,50,170,WHT,0.2,x='230'),txt('£'+up(29.2,1)+'bn',AN,150,220,GRN,0.2,x='230'),bar(392,1.0,GRN,0.25),
    txt('SHELL · THREE MONTHS',BB,50,430,WHT,1.2,x='230'),txt('$'+up(10.8,1,at=1.25)+'bn',AN,150,480,GRN,1.2,x='230'),bar(650,0.37,GRN,1.25)],'')
card('c05b','b04/b04-esso-forecourt-empty.jpg',[label('YOUR ENERGY BILL'),txt('+£'+up(60),AN,300,140,RED),txt('PRICE CAP, FROM 1 OCTOBER',BB,76,530,WHT,1.3)],'Ofgem')
card('c06a','b06/b06-musk-cabinet-meeting.jpg',[label('ONE MONDAY'),txt('+$'+up(65)+'bn',AN,270,150,GRN),txt('IN A SINGLE DAY',BB,88,520,WHT,1.3)],'Bloomberg, 5 October 2026')
card('c07a','b07/b07-andrew-chatham-house-2017.jpg',[label('ROYAL LODGE · 30 ROOMS'),txt('£'+up(1.8,1)+'m',AN,290,140,RED),txt('THE BILL FOR THE STATE HE LEFT IT IN',BB,62,530,WHT,1.3)],'ITV News; AFP')
card('c08a','b08/b08-bezos-laugh-jurvetson.jpg',[label('J. BEZOS PROMISES'),txt('A THREE-DAY',AN,170,150,WHT,0.3),txt('WEEK',AN,230,330,YEL,0.7)],'Fox News interview, 7 October 2026')
card('c08c','b08/b08-amazon-swindon-warehouse-2.jpg',[label('AMAZON OFFICE JOBS'),txt('−'+f"%{{eif:trunc(min(30,30*max(0,t-0.25)/0.9)):d}}"+',000',AN,270,150,RED),txt('CUT. “NOT BECAUSE OF AI.”',BB,80,520,WHT,1.3)],'Fast Company; Forbes')
card('c09a','b09/b09-ward-computer-station-seattle.jpg',[label('YOUR NHS RECORDS'),txt('£'+up(330)+'m',AN,270,150,YEL),txt('TO PALANTIR, A US SPY-TECH FIRM',BB,70,520,WHT,1.3)],'several outlets, October 2026')
card('c10a','b10/b10-farage-official-portrait-crop.jpg',[label('REFORM UK'),
    txt('DONATIONS TO THE PARTY',BB,50,170,WHT,0.2,x='230'),txt('£'+up(72)+'m',AN,150,220,GRN,0.2,x='230'),bar(392,1.0,GRN,0.25),
    txt('GIFT TO N. FARAGE, NOT DECLARED',BB,50,425,WHT,1.2,x='230'),txt('£'+up(5,at=1.25)+'m',AN,130,470,GRN,1.2,x='230'),
    txt('UNDER INVESTIGATION. HE DENIES WRONGDOING.',BB,34,622,WHT,1.9)],'')
card('c10b',None,[label('VOCABULARY'),txt('POOR, AND MOVED ABROAD',BB,60,170,WHT,0.2),txt('IMMIGRANT',AN,170,230,RED,0.5,fade=0.08),txt('RICH, AND MOVED ABROAD',BB,60,440,WHT,1.6),txt('EXPAT',AN,190,500,GRN,1.9,fade=0.08)])
card('c11a','b11/b11-blackburn-town-hall-green.jpg',[label('BLACKBURN COUNCIL'),txt('FARTGATE',AN,250,160,YEL,0.3),txt('HE DENIES AIMING IT',BB,84,500,WHT,1.2)],'PA, via Yahoo News UK')
card('c12a','b12/b12-hunt-budget-box-2023.jpg',[label('COMING UP'),txt('THE BUDGET',AN,200,150,WHT,0.3),txt('28 OCTOBER',AN,200,380,YEL,0.8)])
card('c99',None,[txt('NO SIGNAL',AN,150,280,WHT,0.0)])
if not only: open(H+'/cards2-photos.tsv','w').write('\n'.join(photos)+'\n')
