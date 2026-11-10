#!/usr/bin/env python3
"""words.py out.json audio... : faster-whisper word times for voice takes (cached by path). Round 24 row."""
import json, os, re, subprocess, sys
WPY = os.path.expanduser('~/.cache/badcode-whisper/venv/bin/python')
out_p, files = sys.argv[1], sys.argv[2:]
out = json.load(open(out_p)) if os.path.exists(out_p) else {}
todo = [f for f in files if f not in out]
if todo:
    code = ("import json,sys,subprocess,numpy as np;from faster_whisper import WhisperModel;m=WhisperModel('small',device='cpu',compute_type='int8');r=[]\n"
            "for p in sys.argv[1:]:\n"
            " a=np.frombuffer(subprocess.run(['ffmpeg','-loglevel','error','-i',p,'-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout,np.int16).astype(np.float32)/32768\n"
            " s,_=m.transcribe(a,word_timestamps=True,language='en');r.append([[w.word,w.start,w.end] for x in s for w in x.words])\n"
            "print(json.dumps(r))")
    res = json.loads(subprocess.run([WPY, '-c', code, *todo], capture_output=True, text=True, check=True).stdout)
    for f, w in zip(todo, res):
        out[f] = [[re.sub(r"[^a-z']", '', a.lower()), round(s, 3), round(z, 3)] for a, s, z in w]
    json.dump(out, open(out_p, 'w'), indent=0)
for f in files:
    w = out[f]
    print(os.path.basename(f), f'{w[0][1]:.2f}-{w[-1][2]:.2f}', ' '.join(f'{x}@{s:.2f}' for x, s, _ in w))
