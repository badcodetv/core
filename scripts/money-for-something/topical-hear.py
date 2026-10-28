#!/usr/bin/env python3
"""Money For Something, the topical monologue: ask Gemini where the line starts and ends in each talking clip, and whether
there is crowd noise or music. Writes topical-trims.tsv (name, first, last, crowd, music, voice, words) for build-topical-cut.py.
A machine listener only; times are good to about a third of a second. Skips clips already in the file unless named.
usage: python3 topical-hear.py [name ...]"""
import os,sys,json,base64,subprocess,urllib.request,re,time
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.join(H,'..','..')
V='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/videos'
key=next(l.split('=',1)[1].strip().strip('"') for l in open(os.path.join(ROOT,'.env')) if 'GEMINI_API_KEY=' in l)
OUT=os.path.join(H,'topical-trims.tsv')
have={l.split('\t')[0]:l.rstrip('\n') for l in open(OUT)} if os.path.exists(OUT) else {}
names=sys.argv[1:] or sorted(f[:-4] for f in os.listdir(V) if re.match(r't-\d\d[a-d]\.mp4$',f))
Q='Listen to this clip of one man speaking. Reply with JSON only: {"words": exact transcript, "first": seconds (one decimal) when the first word starts, "last": seconds (one decimal) when the last word ends, "crowd": "no" or a short note with times of any applause, laughter or audience sound, "music": "no" or times, "voice": accent and whether flat or animated}'
for n in names:
    if n in have and not sys.argv[1:]: continue
    a=subprocess.check_output(['ffmpeg','-v','error','-i',f'{V}/{n}.mp4','-vn','-ac','1','-ar','16000','-f','mp3','-'])
    body=json.dumps({"contents":[{"parts":[{"inline_data":{"mime_type":"audio/mp3","data":base64.b64encode(a).decode()}},{"text":Q}]}],"generationConfig":{"temperature":0,"responseMimeType":"application/json"}}).encode()
    for model in ('gemini-3.5-flash','gemini-3-flash-preview'):
        try:
            r=json.load(urllib.request.urlopen(urllib.request.Request(f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}',body,{'Content-Type':'application/json'}),timeout=120))
            j=json.loads(r['candidates'][0]['content']['parts'][0]['text']); break
        except Exception as e: j=None; err=str(e)[:80]; time.sleep(2)
    if not j: print(n,'FAILED',err); continue
    if isinstance(j,list): j=j[0]
    have[n]='\t'.join(str(j.get(k,'')).replace('\t',' ').replace('\n',' ') for k in ('first','last','crowd','music','voice','words')); have[n]=n+'\t'+have[n]
    print(have[n][:200])
open(OUT,'w').write('\n'.join(have[k] for k in sorted(have))+'\n')
