#!/usr/bin/env python3
"""Karen narration v2: transcribe every take (faster-whisper small.en) and diff it with the script line.
Writes narration-v2-check.tsv: take, seconds, words matched / script words, first word start, last word end, heard.
Run: ~/.cache/badcode-whisper/venv/bin/python scripts/karen/check-narration-v2.py"""
import os,re,subprocess,difflib
import numpy as np
from faster_whisper import WhisperModel
H=os.path.dirname(os.path.abspath(__file__))
V='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/Karen/narration-v2'
norm=lambda s:re.findall(r"[a-z0-9']+",re.sub(r'\[[^]]*\]','',s.lower()).replace('a.i.','ai').replace('h.r.','hr').replace('-',' '))
lines={l.split('\t')[0]:l.rstrip('\n').split('\t')[2] for l in open(os.path.join(H,'narration-v2.tsv'))}
m=WhisperModel('small.en',device='cpu',compute_type='int8')
rows=[]
import sys
for f in sorted(os.listdir(V)):
    if sys.argv[1:] and not any(f.startswith(a) for a in sys.argv[1:]): continue
    if not f.endswith('.wav'): continue
    w=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',f'{V}/{f}','-ac','1','-ar','16000','-f','s16le','-']),dtype=np.int16).astype(np.float32)/32768.0
    segs,_=m.transcribe(w,word_timestamps=True,vad_filter=False,condition_on_previous_text=False,beam_size=5)
    ws=[x for s in segs for x in s.words]; heard=' '.join(x.word.strip() for x in ws)
    a,b=norm(lines[f[:3]]),norm(heard.replace('A.I.','AI'))
    hit=sum(k.size for k in difflib.SequenceMatcher(None,a,b).get_matching_blocks())
    s0,s1=(ws[0].start,ws[-1].end) if ws else (0,0)
    rows.append(f"{f[:-4]}\t{len(w)/16000:.2f}\t{hit}/{len(a)}\t{s0:.2f}\t{s1:.2f}\t{heard}"); print(rows[-1][:200])
if not sys.argv[1:]: open(os.path.join(H,'narration-v2-check.tsv'),'w').write('\n'.join(rows)+'\n')
