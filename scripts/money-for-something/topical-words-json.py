#!/usr/bin/env python3
"""Money For Something, the topical monologue: every word of every raw talking clip with its start and end time
(faster-whisper medium.en, word timestamps). Writes topical-words.json: {name: {"script": n, "hit": n, "words": [[word, start, end], ...]}}.
topical-words.tsv (small.en) only kept the first and last word, and small.en stopped early on nine clips, so cut 2 kept
those clips whole. build-topical-cut.py tightens on this file from cut 3 on: head, tail, and the pauses inside a line.
Run with the venv:  ~/.cache/badcode-whisper/venv/bin/python topical-words-json.py [name ...]"""
import os,re,sys,json,subprocess,difflib
import numpy as np
from faster_whisper import WhisperModel
H=os.path.dirname(os.path.abspath(__file__))
V='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/videos'
BANK=os.path.join(H,'..','..','docs','stories','magic-money-tree','money-for-something-joke-bank.md')
script={f"t-{int(c[:-1]):02d}{c[-1]}":l for c,l in re.findall(r"^\| (\d+[a-d]) \| (.+?) \|$",open(BANK).read(),re.M)}
norm=lambda s:re.findall(r"[a-z0-9']+",s.lower().replace('£','').replace('$','').replace('-',' '))
OUT=os.path.join(H,'topical-words.json')
have=json.load(open(OUT)) if os.path.exists(OUT) else {}
names=sys.argv[1:] or sorted(f[:-4] for f in os.listdir(V) if re.match(r't-\d\d[a-d]\.mp4$',f))
m=WhisperModel('medium.en',device='cpu',compute_type='int8',cpu_threads=16)
for n in names:
    w=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',f'{V}/{n}.mp4','-vn','-ac','1','-ar','16000','-f','s16le','-']),dtype=np.int16).astype(np.float32)/32768.0
    line=script.get(n,''); line='' if line.startswith('*(') else line
    segs,_=m.transcribe(w,word_timestamps=True,vad_filter=False,condition_on_previous_text=False,beam_size=5,initial_prompt=line or None)
    ws=[[x.word.strip(),round(x.start,2),round(x.end,2)] for s in segs for x in s.words]
    a,b=norm(line),norm(' '.join(x[0] for x in ws))
    hit=sum(k.size for k in difflib.SequenceMatcher(None,a,b).get_matching_blocks())
    have[n]={'script':len(a),'hit':hit,'words':ws}
    print(n,f'{hit}/{len(a)}',' '.join(f"{x[0]}" for x in ws)[:150],flush=True)
json.dump(have,open(OUT,'w'),indent=0)
