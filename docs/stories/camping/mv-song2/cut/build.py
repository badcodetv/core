"""Write place-N.js for the Premiere bridge: V1 main + hook-3 fill, V2 action, V3 v2 world. Clip audio onto muted A2-A4."""
import json
main=json.load(open('edl-new.json')); ov=json.load(open('overlays.json'))
win=lambda p:'C:\\'+p.split('/mnt/c/',1)[1].replace('/','\\')
rows=[]
for x in main:
    if x['src'] and x['src']!='GAP': rows.append([win(x['src']),x['start'],round(x['end']-x['start'],3),x['in'],0,1])
for x in ov['gap']: rows.append([win(x['src']),x['start'],round(x['end']-x['start'],3),x['in'],0,1])
for x in ov['V2']: rows.append([win(x['src']),x['start'],round(x['end']-x['start'],3),x['in'],1,2])
for x in ov['V3']: rows.append([win(x['src']),x['start'],round(x['end']-x['start'],3),x['in'],2,3])
JS='''const P=%s; const R0=%s; const R=R0.map(r=>[P[r[0]],...r.slice(1)]); const S='camping song 2 beat 1';
const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!==S) return {error:'wrong sequence',name:seq.name};
const map={}; async function walk(f){ for(const it of await f.getItems()){ const fo=ppro.FolderItem.cast(it); if(fo){await walk(fo);continue;} const c=ppro.ClipProjectItem.cast(it); if(c){ try{ const p=await c.getMediaFilePath(); if(p && !map[p.toLowerCase()]) map[p.toLowerCase()]=it; }catch(e){} } } }
await walk(await project.getRootItem());
const ed=ppro.SequenceEditor.getEditor(seq); const tk=s=>helpers.secondsToTick(Math.round(s*25)/25+0.002); let done=0; const fail=[];
for(const [p,st,d,inp,vt,at] of R){ try{ const item=map[p.toLowerCase()]; if(!item) throw 'not in project';
  const clip=ppro.ClipProjectItem.cast(item);
  helpers.withTransaction(project,'BadCode: in/out',ca=>ca.addAction(clip.createSetInOutPointsAction(tk(inp),tk(inp+d))));
  helpers.withTransaction(project,'BadCode: place',ca=>ca.addAction(ed.createOverwriteItemAction(item,tk(st),vt,at)));
  helpers.withTransaction(project,'BadCode: clear',ca=>ca.addAction(clip.createClearInOutPointsAction())); done++; }catch(e){ fail.push([p.split('\\\\').pop(),st,String(e).slice(0,80)]); } }
return {done,fail};'''
N=45
for k in range(0,len(rows),N):
    ch=rows[k:k+N]; P=sorted({r[0] for r in ch})
    open(f'place-{k//N}.js','w').write(JS%(json.dumps(P),json.dumps([[P.index(r[0])]+r[1:] for r in ch])))
print(len(rows),'rows ->',(len(rows)+N-1)//N,'scripts')
