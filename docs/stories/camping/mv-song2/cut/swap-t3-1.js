const V=[{"file": "cb-s03t3-s03r6-b.mp4", "track": 0, "start": 30.84, "dur": 3.72, "in": 4.16}, {"file": "cb-s04t3-s04r6-b.mp4", "track": 0, "start": 34.56, "dur": 1.04, "in": 1.0}, {"file": "cb-s04t3-s04r6-b.mp4", "track": 0, "start": 36.64, "dur": 2.4, "in": 3.76}, {"file": "cb-s05t3-s05r6-b.mp4", "track": 0, "start": 39.72, "dur": 4.08, "in": 0.0}, {"file": "cb-s05t3-s05r6-b.mp4", "track": 0, "start": 43.8, "dur": 3.84, "in": 4.08}, {"file": "cb-s05t3-s05r6-b.mp4", "track": 0, "start": 47.64, "dur": 0.6, "in": 7.32}, {"file": "cb-s05t3-s05r6-b.mp4", "track": 0, "start": 48.24, "dur": 0.68, "in": 7.24}, {"file": "cb-s06t3-s06r6-b.mp4", "track": 0, "start": 50.28, "dur": 2.4, "in": 1.76}, {"file": "cb-s06t3-s06r6-b.mp4", "track": 0, "start": 53.32, "dur": 2.76, "in": 4.76}, {"file": "cb-t04t3-t04r6-b.mp4", "track": 0, "start": 77.92, "dur": 1.68, "in": 0.0}]; const S="camping song 2 beat 3"; const PRE="C:\\Users\\jackt\\OneDrive\\Desktop\\Youtube Vids\\animation\\songs\\camping vid\\balaclava\\video\\premiere\\"; const BIN='t3 rap clips';
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
