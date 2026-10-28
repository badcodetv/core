#!/usr/bin/env python3
"""Money For Something, the topical monologue: exact word timings for every raw talking clip, from a local speech model
(faster-whisper, small.en, word timestamps). Writes topical-words.tsv: name, first word start, last word end, how many of
the script's words were heard in order, the script's word count, and what was heard. build-topical-cut.py trims on this.
Replaces the Gemini timings (topical-trims.tsv), which were out by up to three seconds and cut seven lines short in cut 1.
Run with the venv:  ~/.cache/badcode-whisper/venv/bin/python topical-words.py [name ...]"""
import os,re,sys,subprocess,tempfile,difflib
from faster_whisper import WhisperModel
H=os.path.dirname(os.path.abspath(__file__))
V='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/videos'
BANK=os.path.join(H,'..','..','docs','stories','magic-money-tree','money-for-something-joke-bank.md')
script={f"t-{int(c[:-1]):02d}{c[-1]}":l for c,l in re.findall(r"^\| (\d+[a-d]) \| (.+?) \|$",open(BANK).read(),re.M)}
norm=lambda s:re.findall(r"[a-z0-9']+",s.lower().replace('£','').replace('$','').replace('-',' '))
OUT=os.path.join(H,'topical-words.tsv')
have={l.split('\t')[0]:l.rstrip('\n') for l in open(OUT)} if os.path.exists(OUT) else {}
names=sys.argv[1:] or sorted(f[:-4] for f in os.listdir(V) if re.match(r't-\d\d[a-d]\.mp4$',f))
m=WhisperModel('small.en',device='cpu',compute_type='int8')
for n in names:
    import numpy as np
    w=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',f'{V}/{n}.mp4','-vn','-ac','1','-ar','16000','-f','s16le','-']),dtype=np.int16).astype(np.float32)/32768.0
    segs,_=m.transcribe(w,word_timestamps=True,vad_filter=False,condition_on_previous_text=False,beam_size=5)
    ws=[x for s in segs for x in s.words]
    if not ws: have[n]=f"{n}\t0\t0\t0\t{len(norm(script.get(n,'')))}\t"; print(have[n]); continue
    heard=' '.join(x.word.strip() for x in ws); a,b=norm(script.get(n,'')),norm(heard)
    hit=sum(k.size for k in difflib.SequenceMatcher(None,a,b).get_matching_blocks())
    have[n]=f"{n}\t{ws[0].start:.2f}\t{ws[-1].end:.2f}\t{hit}\t{len(a)}\t{heard}"; print(have[n][:230])
open(OUT,'w').write('\n'.join(have[k] for k in sorted(have))+'\n')
