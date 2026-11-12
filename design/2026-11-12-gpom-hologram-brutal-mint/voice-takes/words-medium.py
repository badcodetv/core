import sys,json
from faster_whisper import WhisperModel
m=WhisperModel('medium.en',device='cpu',compute_type='int8')
out={}
for f in sys.argv[2:]:
    segs,_=m.transcribe(f,word_timestamps=True,beam_size=5)
    out[f]=[(w.word.strip(),round(w.start,3),round(w.end,3)) for s in segs for w in s.words]
json.dump(out,open(sys.argv[1],'w'),indent=0)
