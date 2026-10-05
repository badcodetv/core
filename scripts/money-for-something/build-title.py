#!/usr/bin/env python3
"""Money For Something: the title screen (Jack, 5 Oct: "money for something in text over the opening shot of the
studio", with "royalty free jazzy opening talk show music"). 1280x720 / 24 fps, into clips/_v3/. Skips what exists.

title-mfs.mp4        231 frames, no sound. The whole studio wide (videos/s02-00-wide.mp4, 192 frames) slowed to 219
                     (88%: the tune's phrase is longer than the clip, and Jack had said people move too fast), with
                     MONEY / FOR / SOMETHING landing one word a beat from frame 20, then 12 frames of the host's
                     close-up before he speaks (L-s02-01-host-title from 0.4167 s), so the last chord has room.
title-music-hot-swing.wav   "Hot Swing", Kevin MacLeod (incompetech.com), CC BY 4.0. Credit owed, see the storyboard.
                     Cut to the picture: the drum roll (4.157 to 4.99 s), then straight to the tune's own ending,
                     unedited: the last four bars of the theme, the bar of stabs and the final hit (from 38.19 s).
                     Beat 0.415 s, bar 1.66 s, band in at 4.99 s, final hit at 46.5 s: all measured.
                     The band comes in on frame 20 and the final hit lands on frame 219, the cut to the host.
                     (A first edit joined two bars of the opening to the last two bars; a listener heard the join.)
pad-193f.mp4         193 black frames: what the title adds to the cut (231 less the 38 frames of wide it replaces).
                     Inserted at the old wide shot to push every track later, then overwritten."""
import os,subprocess,tempfile,urllib.request
P='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something'
O=P+'/clips/_v3'; WIDE=P+'/videos/s02-00-wide.mp4'; HOST=P+'/videos/leveled/L-s02-01-host-title.mp4'
FONT='/mnt/c/Windows/Fonts/impact.ttf'; YEL='0xFFD23A'
ENC=['-an','-r','24','-c:v','libx264','-crf','16','-preset','medium','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv']
T=tempfile.mkdtemp(); F=24; IN=20; BEAT=0.415; END=219
def word(text,size,y,frame):
    p=f'{T}/{text}.txt'; open(p,'w').write(text)
    return (f"drawtext=fontfile={FONT}:textfile={p}:fontcolor={YEL}:fontsize={size}:x=(w-text_w)/2:y={y}:borderw=7:bordercolor=black"
            f":shadowcolor=black@0.7:shadowx=8:shadowy=8:enable='between(n,{frame},{END-1})'")
def title():
    out=O+'/title-mfs.mp4'
    if os.path.exists(out): return
    f1,f2=IN+round(BEAT*F),IN+round(2*BEAT*F)
    # the plate dims a little when the band comes in, so the words read over four men and a brick wall
    vf=(f"[0:v]setpts=PTS*{END}/192,fps=24,scale=1280:720,trim=start_frame=0:end_frame={END},setpts=PTS-STARTPTS,"
        f"eq=brightness=-0.10:saturation=0.85:enable='gte(n,{IN})',"
        +word('MONEY',200,92,IN)+','+word('FOR',84,300,f1)+','+word('SOMETHING',200,392,f2)+"[a];"
        f"[1:v]fps=24,scale=1280:720,trim=start_frame=0:end_frame=12,setpts=PTS-STARTPTS[b];[a][b]concat=n=2:v=1:a=0,format=yuv420p[v]")
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',WIDE,'-ss','0.4167','-i',HOST,'-filter_complex',vf,'-map','[v]','-frames:v',str(END+12)]+ENC+[out],check=True); print('title')
def music():
    out=O+'/title-music-hot-swing.wav'; src=O+'/src-hot-swing-kevin-macleod.mp3'
    if os.path.exists(out): return
    if not os.path.exists(src): urllib.request.urlretrieve('https://incompetech.com/music/royalty-free/mp3-royaltyfree/Hot%20Swing.mp3',src)
    entry=4.99; a0=entry-IN/F; a1=entry; b0=38.19; x=0.03   # 30 ms crossfade on the bar line
    af=(f"[0:a]atrim={a0}:{a1+x},asetpts=PTS-STARTPTS[a];[0:a]atrim={b0}:49.9,asetpts=PTS-STARTPTS[b];"
        f"[a][b]acrossfade=d={x}:c1=tri:c2=tri,volume=-3dB,afade=t=in:d=0.05[m]")
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',src,'-filter_complex',af,'-map','[m]','-ar','48000','-c:a','pcm_s16le',out],check=True); print('music')
def pad():
    out=O+'/pad-193f.mp4'
    if os.path.exists(out): return
    subprocess.run(['ffmpeg','-y','-loglevel','error','-f','lavfi','-i','color=c=black:s=1280x720:r=24','-frames:v','193','-vf','format=yuv420p']+ENC+[out],check=True); print('pad')
title(); music(); pad()
