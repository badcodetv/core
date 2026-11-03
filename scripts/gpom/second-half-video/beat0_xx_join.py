#!/usr/bin/env python3
"""Beat 0 continuous shot, extended (2026-11-02): cut3-beat0-continuous-x.mp4 + chain-09..16 -> -xx.mp4.

    python3 scripts/gpom/second-half-video/beat0_xx_join.py 16

x.mp4 is passed through frame for frame (it ends on chain-08's last frame). Each new clip drops its first frame
(the start frame it was given). chain-11..15 were started from frame 179 of the clip before (the last-frame grab
landed 0.5 s early), so chain-10..14 end at frame 179 here and every join is exact. From chain-10 on, start frames
were re-anchored (graded to chain-03's end level) to stop the brightness drift; at each join a per-channel gain +
offset, measured so the clip's first kept frame matches the frame before the join, eases out over RAMP s
(smoothstep), so there is no colour step anywhere. Clips and rejects: video/cut3-beat0/ and cut3-beat0/alt/."""
import json,subprocess,sys,numpy as np
V='/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/video'
C=V+'/cut3-beat0'
W,H,FPS=1280,720,24; RAMP=6.0; END={k:179 for k in range(10,15)};  # chain-11..15 were started from frame 179 of the clip before (last-frame grab landed 0.5 s early)
FSZ=W*H*3
ENC=['-an','-r','24','-c:v','libx264','-crf','14','-preset','medium','-pix_fmt','yuv420p','-color_range','tv',
     '-colorspace','bt709','-color_primaries','bt709','-color_trc','bt709']
last=int(sys.argv[1]); out=sys.argv[2] if len(sys.argv)>2 else V+'/cut3-beat0-continuous-xx.mp4'
enc=subprocess.Popen(['ffmpeg','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r','24','-i','-',*ENC,out],stdin=subprocess.PIPE)
def frames(p):
    d=subprocess.Popen(['ffmpeg','-loglevel','error','-i',p,'-an','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
    while True:
        b=d.stdout.read(FSZ)
        if len(b)<FSZ: break
        yield b
n=0
for b in frames(V+'/cut3-beat0-continuous-x.mp4'): enc.stdin.write(b); n+=1; lastb=b
prev=np.frombuffer(lastb,np.uint8).reshape(H,W,3).astype(np.float32)
print('original frames',n,'ends at',n/FPS)
def stats(x): return x.mean((0,1)), x.std((0,1))
for k in range(9,last+1):
    g=None; m=0
    for i,b in enumerate(frames(f'{C}/chain-{k:02d}.mp4')):
        if i==0: continue
        if i>END.get(k,191): break
        x=np.frombuffer(b,np.uint8).reshape(H,W,3).astype(np.float32)
        if g is None:  # measured match: this clip's first kept frame -> the frame before the join (per channel mean/sd)
            (mp,sp),(mx,sx)=stats(prev),stats(x); ga=sp/sx; g=(ga,mp-ga*mx)
            print(f'chain-{k:02d} join match gain',ga.round(3),'off',g[1].round(1))
        t=min(1.0,(i-1)/(RAMP*FPS)); w=1-(t*t*(3-2*t))
        if w>0:
            x=np.clip(np.rint(x+w*((x*g[0]+g[1])-x)),0,255)
            b=x.astype(np.uint8).tobytes()
        prev=x; enc.stdin.write(b); m+=1
    n+=m; print(f'chain-{k:02d}',m,'frames, ends at',round(n/FPS,3))
enc.stdin.close(); enc.wait()
