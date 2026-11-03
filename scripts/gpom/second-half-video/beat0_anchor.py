"""anchor.py IN OUT.jpg : grade a chain frame's per-channel mean/sd to the fixed target T; write OUT and OUT.json {gain, off}."""
import json,subprocess,sys,numpy as np
T_M=np.array([97.5,105.0,102.3]); T_S=np.array([53.7,55.9,57.1])  # chain-03's end: the level the extension is held at
W,H=1280,720
src,out=sys.argv[1],sys.argv[2]
x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',src,'-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True,check=True).stdout,np.uint8).reshape(H,W,3).astype(np.float32)
m,s=x.mean((0,1)),x.std((0,1))
gain=T_S/s; off=T_M-gain*m
y=np.clip(x*gain+off,0,255).astype(np.uint8)
subprocess.run(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-i','-','-q:v','1',out],input=y.tobytes(),check=True)
json.dump({'src':src,'mean':m.tolist(),'sd':s.tolist(),'gain':gain.tolist(),'off':off.tolist()},open(out+'.json','w'),indent=1)
print('mean',m.round(1),'sd',s.round(1),'gain',gain.round(3),'off',off.round(1))
