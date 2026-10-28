#!/usr/bin/env python3
"""Money For Something, 26 Oct: mock-ups of the BadCode news overlay over real footage (25 Oct 2026).
Jack: "i worried just footage of stuff/news would be boring, can we have like a badcode overlay over it like a bbc
news banner or a badcode version". Stills only, to pick a direction before any motion is built.
A = BROADCAST: a news channel's furniture, ours (top strip with a 2054 clock, chyron, crawling ticker of future headlines).
B = TRANSMISSION: a received signal (ring bug, mono timecode, red-triangle tag for the chyron, scanlines).
Safe areas from docs/marketing/shorts-factory.md: nothing in the bottom 350 px or the right 150 px.
usage: ~/.cache/badcode-whisper/venv/bin/python build-overlay-mock.py PHOTO OUTDIR"""
import os,sys
from PIL import Image,ImageDraw,ImageFont,ImageOps
H=os.path.dirname(os.path.abspath(__file__))
FD=H+'/../fonts/'; ARC=FD+'Archivo.ttf'; MONO=FD+'SpaceMono-Bold.ttf'
MARK=H+'/../../../docs/brand/logo/avatar-1024.png'
W,Hh=1080,1920; SAFE_B=1920-350; SAFE_R=1080-150; L=60
INK=(6,7,9); WHT=(236,242,244); RED=(201,43,56); YEL=(250,204,21)
def arc(size,wght=900,wdth=125):
    f=ImageFont.truetype(ARC,size); f.set_variation_by_axes([wght,wdth]); return f
def mono(size): return ImageFont.truetype(MONO,size)
def bg(photo):
    im=ImageOps.fit(Image.open(photo).convert('RGB'),(W,Hh),centering=(0.5,0.45))
    return im
def mark(size):
    m=Image.open(MARK).convert('RGB').resize((size,size),Image.LANCZOS)
    mask=Image.new('L',(size,size),0); ImageDraw.Draw(mask).ellipse((0,0,size-1,size-1),fill=255)
    return m,mask

def broadcast(photo,o):
    im=bg(photo); d=ImageDraw.Draw(im,'RGBA')
    # top strip: bug + channel name + future clock
    d.rectangle((0,110,W,210),fill=INK+(235,))
    m,mk=mark(76); im.paste(m,(L,122),mk)
    d.text((L+96,133),'BADCODE NEWS',font=arc(40),fill=WHT)
    d.rectangle((SAFE_R-250,128,SAFE_R,192),fill=RED)
    d.text((SAFE_R-236,138),'LIVE · 2054',font=mono(34),fill=WHT)
    # chyron: kicker tag + two-line headline; the joke rides on line 2
    y=1190
    d.rectangle((L,y,L+300,y+64),fill=RED); d.text((L+18,y+10),'BREAKING',font=mono(38),fill=WHT)
    d.rectangle((L+300,y,L+560,y+64),fill=WHT); d.text((L+316,y+10),'(AGAIN)',font=mono(38),fill=INK)
    d.rectangle((L,y+64,SAFE_R,y+250),fill=WHT+(250,))
    d.text((L+24,y+80),'GOVERNMENT TELLS YOU',font=arc(46),fill=INK)
    d.text((L+24,y+142),'TO STOCKPILE 3 DAYS',font=arc(46),fill=INK)
    d.rectangle((L,y+250,SAFE_R,y+310),fill=YEL)
    d.text((L+24,y+262),'Day four: not their department',font=arc(32,600,100),fill=INK)
    # ticker: future headlines, one joke per item
    d.rectangle((0,SAFE_B-80,W,SAFE_B-12),fill=INK+(240,))
    d.rectangle((0,SAFE_B-80,170,SAFE_B-12),fill=RED); d.text((22,SAFE_B-68),'LATER',font=mono(34),fill=WHT)
    d.text((190,SAFE_B-68),'2031: TINNED CUSTARD BECOMES LEGAL TENDER  ●  2033: GOGGLE',font=mono(34),fill=WHT)
    im.save(o)

def transmission(photo,o):
    im=bg(photo)
    # cold grade + scanlines: it is a received signal, not a channel
    im=Image.blend(im,ImageOps.colorize(ImageOps.grayscale(im),INK,(214,228,236)),0.55)
    d=ImageDraw.Draw(im,'RGBA')
    for y in range(0,Hh,4): d.line((0,y,W,y),fill=(0,0,0,40))
    d.rectangle((0,0,W,Hh),outline=None)
    m,mk=mark(110); im.paste(m,(L,130),mk)
    d.text((L+130,140),'RECEIVED 25.10.2026',font=mono(30),fill=WHT)
    d.text((L+130,182),'SENT 2054 · SIGNAL 71%',font=mono(30),fill=WHT+(170,))
    # corner brackets: the viewfinder of something that already saw it
    for (x,y,sx,sy) in ((L,300,1,1),(SAFE_R,300,-1,1),(L,1100,1,-1),(SAFE_R,1100,-1,-1)):
        d.line((x,y,x+60*sx,y),fill=WHT,width=5); d.line((x,y,x,y+60*sy),fill=WHT,width=5)
    y=1230
    d.rectangle((L,y-8,L+500,y+68),fill=INK+(225,))
    d.polygon([(L+16,y+6),(L+70,y+6),(L+43,y+52)],fill=RED)
    d.text((L+90,y+8),'ARCHIVE · ITEM 0412',font=mono(34),fill=WHT)
    d.rectangle((L,y+80,SAFE_R,y+250),fill=INK+(225,))
    d.text((L+28,y+98),'"KEEP THREE DAYS',font=arc(54),fill=WHT)
    d.text((L+28,y+162),'OF TINS."',font=arc(54),fill=WHT)
    d.rectangle((L,y+250,SAFE_R,y+320),fill=YEL)
    d.text((L+28,y+262),'› it was not three days.',font=mono(36),fill=INK)
    im.save(o)

if __name__=='__main__':
    photo,out=sys.argv[1],sys.argv[2]; os.makedirs(out,exist_ok=True)
    broadcast(photo,out+'/overlay-A-broadcast.jpg'); transmission(photo,out+'/overlay-B-transmission.jpg')
    print(out)
