"""Send a video to Gemini (Files API) and ask a question. Usage: gwatch.py video.mp4 prompt.txt out.md [model]"""
import json,os,sys,time,urllib.request,re
key=re.search(r'GEMINI_API_KEY=(\S+)',open('/home/jackt/projects/badcode/badcode/.env').read()).group(1).strip('"\'')
vid,promptf,outf=sys.argv[1:4]; model=sys.argv[4] if len(sys.argv)>4 else 'gemini-3.5-flash'
data=open(vid,'rb').read()
req=urllib.request.Request(f'https://generativelanguage.googleapis.com/upload/v1beta/files?key={key}',method='POST',
  headers={'X-Goog-Upload-Protocol':'resumable','X-Goog-Upload-Command':'start','X-Goog-Upload-Header-Content-Length':str(len(data)),'X-Goog-Upload-Header-Content-Type':'video/mp4','Content-Type':'application/json'},
  data=json.dumps({'file':{'display_name':os.path.basename(vid)}}).encode())
url=urllib.request.urlopen(req).headers['X-Goog-Upload-URL']
req=urllib.request.Request(url,method='POST',data=data,headers={'X-Goog-Upload-Command':'upload, finalize','X-Goog-Upload-Offset':'0'})
f=json.load(urllib.request.urlopen(req))['file']
while f.get('state')=='PROCESSING':
    time.sleep(5); f=json.load(urllib.request.urlopen(f"https://generativelanguage.googleapis.com/v1beta/{f['name']}?key={key}"))
body={'contents':[{'parts':[{'file_data':{'mime_type':'video/mp4','file_uri':f['uri']}},{'text':open(promptf).read()}]}]}
for attempt in range(4):
    try:
        req=urllib.request.Request(f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}',data=json.dumps(body).encode(),headers={'Content-Type':'application/json'})
        r=json.load(urllib.request.urlopen(req,timeout=600)); break
    except urllib.error.HTTPError as e:
        print('HTTP',e.code,e.read()[:300]); time.sleep(20)
        if e.code==429: model='gemini-3-flash-preview'
txt=''.join(p.get('text','') for p in r['candidates'][0]['content']['parts'])
open(outf,'w').write(txt); print(txt)
