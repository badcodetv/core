"""Low-res check render of the planned cut (for checking only; Jack watches the Premiere timeline)."""
import json,subprocess,os,sys
S='/tmp/claude-1000/-home-jackt-projects-badcode-badcode/b9746f39-397a-42d9-9fa6-8708205c6ea0/scratchpad/prev/'
os.makedirs(S,exist_ok=True)
main=json.load(open('edl-new.json')); ov=json.load(open('overlays.json'))
FPS=25; N=int(round(220.72*FPS)); top=[None]*N
def lay(items):
    for x in items:
        a=int(round(x['start']*FPS)); b=int(round(x['end']*FPS))
        for f in range(a,min(b,N)): top[f]=(x['src'],round(x['in']-x['start'],3)) if x['src'] else None
lay([x for x in main if x['src']!='GAP']); lay(ov['gap']); lay(ov['V2']); lay(ov['V3'])
pieces=[];f=0
while f<N:
    k=top[f];g=f
    while g<N and top[g]==k: g+=1
    pieces.append((f,g,k)); f=g
lst=open(S+'list.txt','w')
for i,(a,b,k) in enumerate(pieces):
    out=S+f'p{i:04d}.mp4'; d=(b-a)/FPS
    if k is None: cmd=['ffmpeg','-v','error','-y','-f','lavfi','-i',f'color=black:s=640x360:r=25:d={d}']
    else: cmd=['ffmpeg','-v','error','-y','-ss',str(max(0,k[1]+a/FPS)),'-i',k[0],'-t',str(d),'-an','-vf','scale=640:360,fps=25']
    subprocess.run(cmd+['-frames:v',str(b-a),'-c:v','libx264','-preset','ultrafast','-pix_fmt','yuv420p',out])
    lst.write(f"file '{out}'\n")
lst.close()
song='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/song 2 maybe (audio).wav'
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',S+'list.txt','-i',song,'-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-shortest',S+'preview.mp4'])
print(len(pieces),'pieces')
