"""Turn rough3-plan.json into two premiere_eval bodies (2026-11-02):

  <plan>.place.js   places every clip on its track (V1 brings its linked clip sound to A1), in the ACTIVE sequence only,
                    finding media in the bin named after the sequence
  <plan>.levels.js  sets clip Volume: A1 from plan.a1 (None = 0, muted), A2/A3 from each audio entry's level_db

  python3 scripts/stupidity-optimised/rough3-place.py rough3-plan.json "Optimised rough 3"
"""
import json, sys

plan_path, seq = sys.argv[1:3]
P = json.load(open(plan_path))
V = [[p, t, i, d, tr] for p, t, i, d, tr in P['video']]
A = [[p, t, tr] for p, t, tr, lv in P['audio']]
LV = {f'{tr}:{round(t * 24)}': (None if lv is None else lv) for p, t, tr, lv in P['audio']}
for t, lv in P['a1']:
    LV[f'0:{round(t * 24)}'] = lv

PLACE = r"""const V=__V__; const A=__A__; const S=__S__;
const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!==S) return {error:'wrong sequence',name:seq.name};
const root=await project.getRootItem(); let bin=null; for(const k of await root.getItems()){ if(k.name===S){ try{ const f=ppro.FolderItem.cast(k); if(f) bin=f; }catch(e){} } }
if(!bin) return {error:'no bin named '+S};
const byPath={}; for(const it of await bin.getItems()){ try{ byPath[(await ppro.ClipProjectItem.cast(it).getMediaFilePath()).toLowerCase()]=it; }catch(e){} }
const ed=ppro.SequenceEditor.getEditor(seq); const tk=s=>helpers.secondsToTick(Math.round(s*24)/24+0.002); let done=0; const fail=[];
for(const [p,t,i,d,tr] of V){ try{ const item=byPath[p.toLowerCase()]; if(!item) throw 'not in bin'; const clip=ppro.ClipProjectItem.cast(item);
  const still=/\.(jpg|png)$/i.test(p);
  helpers.withTransaction(project,S+' in/out',ca=>ca.addAction(clip.createSetInOutPointsAction(tk(i),tk(i+d))));
  helpers.withTransaction(project,S+' place',ca=>ca.addAction(ed.createOverwriteItemAction(item,tk(t),tr,0)));
  helpers.withTransaction(project,S+' clear',ca=>ca.addAction(clip.createClearInOutPointsAction())); done++; }catch(e){ fail.push([p,t,String(e).slice(0,100)]); } }
for(const [p,t,tr] of A){ try{ const item=byPath[p.toLowerCase()]; if(!item) throw 'not in bin';
  helpers.withTransaction(project,S+' audio',ca=>ca.addAction(ed.createOverwriteItemAction(item,helpers.secondsToTick(t),0,tr))); done++; }catch(e){ fail.push([p,t,String(e).slice(0,100)]); } }
const counts=[]; for(let k=0;k<await seq.getAudioTrackCount();k++) counts.push((await (await seq.getAudioTrack(k)).getTrackItems(1,false)).length);
const vcounts=[]; for(let k=0;k<await seq.getVideoTrackCount();k++) vcounts.push((await (await seq.getVideoTrack(k)).getTrackItems(1,false)).length);
return {done,fail,vcounts,counts,mapped:Object.keys(byPath).length};
"""

LEVELS = r"""const LV=__LV__; const S=__S__;
const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!==S) return {error:'wrong sequence',name:seq.name};
let set=0; const miss=[]; const fail=[];
for(let k=0;k<3;k++){ const items=await (await seq.getAudioTrack(k)).getTrackItems(1,false);
  for(const it of items){ const t=(await it.getStartTime()).seconds; const key=k+':'+Math.round(t*24);
    if(!(key in LV)){ miss.push(key); continue; }
    const db=LV[key]; const lin=db===null?0:0.17782794*Math.pow(10,db/20);
    try{ const chain=await it.getComponentChain(); let comp=null;
      for(let c=0;c<chain.getComponentCount();c++){ const x=chain.getComponentAtIndex(c); if((await x.getDisplayName())==='Volume') comp=x; }
      let par=null; for(let q=0;q<comp.getParamCount();q++){ const pp=comp.getParam(q); if(pp.displayName==='Level') par=pp; }
      helpers.withTransaction(project,S+' level',ca=>ca.addAction(par.createSetValueAction(par.createKeyframe(lin),true))); set++;
    }catch(e){ fail.push([key,String(e).slice(0,100)]); } } }
return {set,miss:miss.slice(0,20),nmiss:miss.length,fail:fail.slice(0,10)};
"""
# shared folder prefix pulled out so the eval body stays small
PRE = 'C:\\Users\\jackt\\OneDrive\\Desktop\\Youtube Vids\\animation\\optimised stupidity\\clips\\film\\'
for x in V + A:
    if x[0].startswith(PRE):
        x[0] = '~' + x[0][len(PRE):]
body = PLACE.replace('__V__', json.dumps(V)).replace('__A__', json.dumps(A)).replace('__S__', json.dumps(seq))
body = body.replace('const project=', "for(const x of V.concat(A)) x[0]=x[0].replace('~',PRE);\nconst project=", 1)
open(plan_path + '.place.js', 'w').write('const PRE=' + json.dumps(PRE) + ';\n' + body)
open(plan_path + '.levels.js', 'w').write(LEVELS.replace('__LV__', json.dumps(LV)).replace('__S__', json.dumps(seq)))
files = sorted({p for p, *_ in P['video']} | {p for p, *_ in P['audio']})
json.dump(files, open(plan_path + '.files.json', 'w'), indent=0)
print(len(V), 'video', len(A), 'audio', len(LV), 'levels', len(files), 'files')
