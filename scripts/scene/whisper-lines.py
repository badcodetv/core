import sys,subprocess,os,numpy as np
from faster_whisper import WhisperModel
m=WhisperModel(os.environ.get('WM','small'),device='cpu',compute_type='int8')
def load(f):
    b=subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout
    return np.frombuffer(b,np.float32).copy()
seg=os.environ.get('SEG')
for f in sys.argv[1:]:
    a=load(f)
    segs,_=m.transcribe(a,language='en',vad_filter=bool(seg))
    if seg:
        for s in segs: print(f"{s.start:7.1f} {s.end:7.1f} {s.avg_logprob:5.2f} {s.no_speech_prob:4.2f} {s.text}",flush=True)
    else:
        print(os.path.basename(f),round(len(a)/16000,2),'|',' '.join(s.text.strip() for s in segs),flush=True)
