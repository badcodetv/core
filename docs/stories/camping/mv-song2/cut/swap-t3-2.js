const V=[{"file": "cb-t03t3-t03r6-b.mp4", "track": 0, "start": 79.92, "dur": 2.76, "in": 0.0}, {"file": "cb-t04t3-t04r6-b.mp4", "track": 0, "start": 83.68, "dur": 2.44, "in": 5.08}, {"file": "cb-t05t3-t05r6-b.mp4", "track": 0, "start": 86.4, "dur": 3.4, "in": 0.0}, {"file": "cb-t05t3-t05r6-b.mp4", "track": 0, "start": 89.8, "dur": 3.12, "in": 3.4}, {"file": "cb-t06t3-t06r6-b.mp4", "track": 0, "start": 93.92, "dur": 2.36, "in": 0.2}, {"file": "cb-t06t3-t06r6-b.mp4", "track": 0, "start": 96.28, "dur": 1.36, "in": 2.56}, {"file": "cb-t06t3-t06r6-b.mp4", "track": 0, "start": 97.64, "dur": 1.56, "in": 3.92}, {"file": "cb-t07t3-t07r6-a.mp4", "track": 0, "start": 99.72, "dur": 2.36, "in": 0.0}, {"file": "cb-t07t3-t07r6-a.mp4", "track": 0, "start": 102.08, "dur": 2.4, "in": 2.36}, {"file": "cb-t07t3-t07r6-a.mp4", "track": 0, "start": 105.16, "dur": 2.4, "in": 4.36}]; const S="camping song 2 beat 3"; const PRE="C:\\Users\\jackt\\OneDrive\\Desktop\\Youtube Vids\\animation\\songs\\camping vid\\balaclava\\video\\premiere\\"; const BIN='t3 rap clips';
const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!==S) return {error:'wrong sequence',name:seq.name};
const root=await project.getRootItem(); let bin=null; for(const k of await root.getItems()){ if(k.name===BIN){ try{ const f=ppro.FolderItem.cast(k); if(f) bin=f; }catch(e){} } }
if(!bin) return {error:'no bin'};
const byPath={}; for(const it of await bin.getItems()){ try{ byPath[(await ppro.ClipProjectItem.cast(it).getMediaFilePath()).toLowerCase()]=it; }catch(e){} }
const ed=ppro.SequenceEditor.getEditor(seq); const tk=s=>helpers.secondsToTick(Math.round(s*25)/25+0.002); let done=0; const fail=[];
for(const r of V){ const p=PRE+r.file; try{ const item=byPath[p.toLowerCase()]; if(!item) throw 'not in bin'; const clip=ppro.ClipProjectItem.cast(item);
  helpers.withTransaction(project,'BadCode: balaclava in/out',ca=>ca.addAction(clip.createSetInOutPointsAction(tk(r.in),tk(r.in+r.dur))));
  helpers.withTransaction(project,'BadCode: t3 swap',ca=>ca.addAction(ed.createOverwriteItemAction(item,tk(r.start),r.track,0)));
  helpers.withTransaction(project,'BadCode: balaclava clear',ca=>ca.addAction(clip.createClearInOutPointsAction())); done++; }catch(e){ fail.push([r.file,r.start,String(e).slice(0,100)]); } }
return {done,fail,mapped:Object.keys(byPath).length};
