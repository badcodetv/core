const V=[["gang\\video\\bg-k29-a-k29r3-a.mp4", 202.78, 0.7, 1.55], ["gang\\video\\bg-k30-a-k30r3-a.mp4", 203.43, 0.7, 1.55], ["gang\\video\\bg-k31-b-k31r3-b.mp4", 204.08, 0.97, 1.82], ["gang\\video\\bg-k01-a-k01r3-a.mp4", 205.0, 4.65, 0.7]]; const S="Balaclava Gang 3"; const PRE="C:\\Users\\jackt\\OneDrive\\Desktop\\Youtube Vids\\animation\\songs\\bank robbery\\";
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
