#!/usr/bin/env python3
"""Money For Something, the topical monologue: check a rendered cut against the script, line by line.
Transcribes the cut with Gemini (words only; its timings are not used), then for each script line in the joke bank
reports the words that were not heard, in order. Also reports silences over 1.5 s and any timestamp fault in the file.
A machine check: it catches a cut-off line or a dropped clip, not a bad read.
usage: python3 topical-verify.py "<render stem>" """
import os,sys,json,base64,subprocess,urllib.request,re,difflib
H=os.path.dirname(os.path.abspath(__file__))
R='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/renders/'+sys.argv[1]+'.mp4'
key=next(l.split('=',1)[1].strip().strip('"') for l in open(os.path.join(H,'..','..','.env')) if 'GEMINI_API_KEY=' in l)
p=subprocess.run(['ffmpeg','-v','warning','-i',R,'-vn','-ac','1','-ar','16000','-f','mp3','-'],capture_output=True)
print('timestamp faults in file:',p.stderr.decode().count('non monotonically'))
s=subprocess.run(['ffmpeg','-v','info','-i',R,'-af','silencedetect=noise=-45dB:d=1.5','-f','null','-'],capture_output=True,text=True).stderr
print('silences over 1.5 s:',[(float(a),float(b)) for a,b in re.findall(r'silence_start: ([\d.]+)[\s\S]*?silence_duration: ([\d.]+)',s)] or 'none', '(a,length)')
body=json.dumps({"contents":[{"parts":[{"inline_data":{"mime_type":"audio/mp3","data":base64.b64encode(p.stdout).decode()}},{"text":"Transcribe every spoken word exactly as said, in order, as plain text. Do not tidy and do not add anything that is not said."}]}],"generationConfig":{"temperature":0}}).encode()
t=json.load(urllib.request.urlopen(urllib.request.Request(f'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={key}',body,{'Content-Type':'application/json'}),timeout=400))['candidates'][0]['content']['parts'][0]['text']
num={'twenty five':'25','sixty five':'65','thirty thousand':'30000','five million':'5 million','three day':'3 day','two':'2','four':'4','six':'6','three':'3','one':'1'}
def norm(x):
    x=x.lower().replace('£','').replace('$','').replace('-',' ').replace(',','').replace('pounds','').replace('pound','').replace('dollars','').replace('defense','defence').replace('paychecks','pay cheques').replace('paycheques','pay cheques')
    for k,v in num.items(): x=re.sub(r'\b'+k+r'\b',v,x)
    return re.findall(r"\d+(?:\.\d+)?|[a-z']+",x)
heard=norm(t); bank=open(os.path.join(H,'..','..','docs','stories','magic-money-tree','money-for-something-joke-bank.md')).read()
bad=0; pos=0
for cid,line in re.findall(r"^\| (\d+[a-d]) \| (.+?) \|$",bank,re.M):
    if line.startswith('*('): continue
    want=norm(line); m=difflib.SequenceMatcher(None,want,heard[pos:pos+len(want)+12],autojunk=False); blocks=m.get_matching_blocks()
    got=set(); last=0
    for b in blocks:
        got.update(range(b.a,b.a+b.size)); last=max(last,b.b+b.size) if b.size else last
    miss=[w for i,w in enumerate(want) if i not in got]; pos+=last
    if miss: bad+=1; print(f'{cid}: NOT HEARD -> {" ".join(miss)}')
print('lines with something not heard:',bad,'of 27')
