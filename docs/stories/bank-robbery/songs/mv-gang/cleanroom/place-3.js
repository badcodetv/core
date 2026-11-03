const V=[["bg-f01-a-f01r2-a.mp4", 154.74, 2.35], ["bg-x07-b-x07r2-b.mp4", 157.04, 2.85], ["bg-f02-a-f02r2-a.mp4", 159.84, 2.75], ["bg-f03-b-f03r2-b.mp4", 162.54, 2.43], ["bg-v12-b-v12r2-b.mp4", 164.92, 5.21], ["bg-v03-b-v03r2-b.mp4", 170.08, 2.67], ["bg-v05-b-v05r2-b.mp4", 175.94, 4.63], ["bg-f08-b-f08r2-b.mp4", 180.52, 4.15], ["bg-v11-b-v11r2-b.mp4", 184.62, 3.89], ["bg-x03-b-x03r2-b.mp4", 188.46, 5.59], ["bg-x01-a-x01r2-a.mp4", 194.0, 5.19], ["bg-x07-b-x07r2-b.mp4", 199.14, 4.91], ["bg-a01-a-a01r2-a.mp4", 204.0, 5.65]]; const S="Balaclava Gang 1"; const PRE="C:\\Users\\jackt\\OneDrive\\Desktop\\Youtube Vids\\animation\\songs\\bank robbery\\gang\\video\\";
const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!==S) return {error:'wrong sequence',name:seq.name};
const root=await project.getRootItem(); let bin=null; for(const k of await root.getItems()){ if(k.name==='Balaclava Gang clips'){ try{ const f=ppro.FolderItem.cast(k); if(f) bin=f; }catch(e){} } }
if(!bin) return {error:'no clips bin'};
const byPath={}; for(const it of await bin.getItems()){ try{ byPath[(await ppro.ClipProjectItem.cast(it).getMediaFilePath()).toLowerCase()]=it; }catch(e){} }
const ed=ppro.SequenceEditor.getEditor(seq); const tk=s=>helpers.secondsToTick(Math.round(s*24)/24+0.002); let done=0; const fail=[];
for(const [n,t,d] of V){ const p=PRE+n; try{ const item=byPath[p.toLowerCase()]; if(!item) throw 'not in bin'; const clip=ppro.ClipProjectItem.cast(item);
  helpers.withTransaction(project,S+' in/out',ca=>ca.addAction(clip.createSetInOutPointsAction(tk(0),tk(d))));
  helpers.withTransaction(project,S+' place',ca=>ca.addAction(ed.createOverwriteItemAction(item,tk(t),0,1)));
  helpers.withTransaction(project,S+' clear',ca=>ca.addAction(clip.createClearInOutPointsAction())); done++; }catch(e){ fail.push([n,t,String(e).slice(0,100)]); } }
const v1=(await (await seq.getVideoTrack(0)).getTrackItems(1,false)).length;
return {done,fail,v1,mapped:Object.keys(byPath).length};
