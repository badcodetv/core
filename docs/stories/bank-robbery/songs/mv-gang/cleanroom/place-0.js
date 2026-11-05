const V=[["gang\\video\\bg-a02m-a-a02r5-a.mp4", 0.0, 4.113, 0.0], ["gang\\video\\bg-a02m-a-a02r5-a.mp4", 51.78, 1.351, 1.7], ["gang\\video\\bg-a03m-a-a03r5-a.mp4", 53.081, 0.7, 0.0], ["gang\\video\\bg-x06-a-x06r2-a.mp4", 53.731, 0.7, 0.0], ["gang\\video\\bg-a03m-a-a03r5-a.mp4", 67.291, 1.328, 1.7], ["gang\\video\\bg-a02m-a-a02r5-a.mp4", 115.055, 0.654, 3.4], ["gang\\video\\bg-a03m-a-a03r5-a.mp4", 115.659, 1.35, 3.4], ["gang\\video\\bg-x06-a-x06r2-a.mp4", 116.959, 1.327, 1.7], ["gang\\video\\bg-x06-a-x06r2-a.mp4", 134.374, 1.327, 3.4]]; const S="Balaclava Gang 9"; const PRE="C:\\Users\\jackt\\OneDrive\\Desktop\\Youtube Vids\\animation\\songs\\bank robbery\\";
const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!==S) return {error:'wrong sequence',name:seq.name};
const root=await project.getRootItem(); let bin=null; for(const k of await root.getItems()){ if(k.name==='Balaclava Gang clips'){ try{ const f=ppro.FolderItem.cast(k); if(f) bin=f; }catch(e){} } }
if(!bin) return {error:'no clips bin'};
const byPath={}; for(const it of await bin.getItems()){ try{ byPath[(await ppro.ClipProjectItem.cast(it).getMediaFilePath()).toLowerCase()]=it; }catch(e){} }
const ed=ppro.SequenceEditor.getEditor(seq); const tk=s=>helpers.secondsToTick(Math.round(s*24)/24+0.002); let done=0; const fail=[];
for(const [n,t,d,i0] of V){ const p=PRE+n; try{ const item=byPath[p.toLowerCase()]; if(!item) throw 'not in bin'; const clip=ppro.ClipProjectItem.cast(item);
  helpers.withTransaction(project,S+' in/out',ca=>ca.addAction(clip.createSetInOutPointsAction(tk(i0||0),tk((i0||0)+d))));
  helpers.withTransaction(project,S+' place',ca=>ca.addAction(ed.createOverwriteItemAction(item,tk(t),0,1)));
  helpers.withTransaction(project,S+' clear',ca=>ca.addAction(clip.createClearInOutPointsAction())); done++; }catch(e){ fail.push([n,t,String(e).slice(0,100)]); } }
const v1=(await (await seq.getVideoTrack(0)).getTrackItems(1,false)).length;
return {done,fail,v1,mapped:Object.keys(byPath).length};
