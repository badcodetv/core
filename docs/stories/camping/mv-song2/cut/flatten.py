"""Flatten a Premiere sequence state to the topmost visible clip at every frame -> edl-old.json (25 fps)."""
import json,sys
ST='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/.bridge/state-camping balaclava 1.json'
s=json.load(open(ST)); FPS=25
end=int(round(215.28*FPS))
top=[None]*end
for t in s['videoTracks']:  # low to high; later overwrites
    for it in t['items']:
        if it['disabled']: continue
        a=int(round(it['start']*FPS)); b=int(round(it['end']*FPS))
        for f in range(a,min(b,end)): top[f]=(it['mediaPath'],it['start'],it['inPoint'],t['label'])
edl=[];f=0
while f<end:
    k=top[f]; g=f
    while g<end and top[g]==k: g+=1
    if k is None: edl.append({'start':f/FPS,'end':g/FPS,'src':None})
    else: edl.append({'start':f/FPS,'end':g/FPS,'src':k[0],'in':round(k[2]+(f/FPS-k[1]),3),'track':k[3]})
    f=g
json.dump(edl,open('docs/stories/camping/mv-song2/cut/edl-old.json','w'),indent=0)
print(len(edl),'segments;',sum(1 for e in edl if e['src'] is None),'black')
