"""Offline watch copy of a Premiere sequence from the bridge state file: V1 picture at 640x360, A1-A3 mixed with clip Volume. Also writes per-track stems."""
import json,sys,subprocess,math,os,numpy as np
st=json.load(open(sys.argv[1])); out=sys.argv[2]; os.makedirs(out,exist_ok=True)
SR=48000; END=st['sequence'].get('end') or max(c['end'] for t in st['videoTracks'] for c in t['items'])
def lvl(c):
    for comp in c.get('components',[]):
        if comp['displayName']=='Volume':
            for p in comp['params']:
                if p['name']=='Level': return 20*math.log10(max(p['value'],1e-6)/0.17782794)
    return 0.0
def dec(path,ss,dur,speed=1):
    cmd=['ffmpeg','-v','error','-ss',str(ss),'-t',str(dur*speed),'-i',path,'-ac','2','-ar',str(SR)]
    if speed!=1: cmd+=['-af',f'atempo={speed}']
    cmd+=['-f','f32le','-']
    b=subprocess.run(cmd,capture_output=True).stdout
    return np.frombuffer(b,np.float32).reshape(-1,2)
N=int(END*SR)+SR
mix=np.zeros((N,2),np.float32)
for t in st['audioTracks']:
    buf=np.zeros((N,2),np.float32)
    if t.get('muted'): continue
    for c in t['items']:
        if c.get('disabled'): continue
        a=dec(c['mediaPath'],c['inPoint'],c['end']-c['start'],c.get('speed',1))*(10**(lvl(c)/20))
        i=int(c['start']*SR); a=a[:N-i]; buf[i:i+len(a)]+=a
    np.save if False else None
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','2','-i','-',f'{out}/{t["label"]}.wav'],input=buf.tobytes())
    mix+=buf
subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','2','-i','-',f'{out}/mix.wav'],input=mix.tobytes())
# picture
lst=open(f'{out}/v.txt','w')
for k,c in enumerate(st['videoTracks'][0]['items']):
    seg=f'{out}/seg{k:03d}.mp4'; d=c['end']-c['start']
    if c['mediaPath'].lower().endswith(('.jpg','.png')):
        cmd=['ffmpeg','-v','error','-y','-loop','1','-t',str(d),'-i',c['mediaPath']]
    else:
        cmd=['ffmpeg','-v','error','-y','-ss',str(c['inPoint']),'-t',str(d),'-i',c['mediaPath']]
    cmd+=['-an','-vf','scale=640:360,fps=24,setsar=1','-c:v','libx264','-preset','veryfast','-crf','26','-frames:v',str(round(d*24)),seg]
    subprocess.run(cmd); lst.write(f"file '{seg}'\n")
lst.close()
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',f'{out}/v.txt','-i',f'{out}/mix.wav','-c:v','copy','-c:a','aac','-b:a','160k','-shortest',f'{out}/watch.mp4'])
print('done',END)
