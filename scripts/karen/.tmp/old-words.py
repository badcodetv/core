# Timeline word times of the old narration on A3 (sequence seconds), from faster-whisper on each source.
import json,subprocess,numpy as np
from faster_whisper import WhisperModel
items=json.load(open('scripts/karen/.tmp/old-a3.json'))
m=WhisperModel('small.en',device='cpu',compute_type='int8'); cache={}
out=[]
for it in items:
    p=it['mediaPath']
    if 'narrator' not in p: continue
    if p not in cache:
        w=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',p,'-ac','1','-ar','16000','-f','s16le','-']),dtype=np.int16).astype(np.float32)/32768.0
        segs,_=m.transcribe(w,word_timestamps=True,vad_filter=False,condition_on_previous_text=False,beam_size=5)
        cache[p]=[(x.start,x.end,x.word.strip()) for s in segs for x in s.words]
    for s,e,wd in cache[p]:
        if s>=it['inPoint']-0.05 and e<=it['outPoint']+0.05:
            out.append((round(it['start']+s-it['inPoint'],2),round(it['start']+e-it['inPoint'],2),wd,it['ref']))
json.dump(out,open('scripts/karen/.tmp/old-words.json','w'))
line=[];t0=None
for s,e,w,r in out:
    if t0 is None: t0=s
    line.append(w)
    if w.endswith(('.','?','!')): print(f"{t0:7.2f} {e:7.2f} {r} {' '.join(line)}"); line=[];t0=None
if line: print(f"{t0:7.2f} {r} {' '.join(line)}")
