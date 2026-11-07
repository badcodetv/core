const V=[{"file": "cb-m12t3-m12r6-b.mp4", "track": 0, "start": 13.44, "dur": 0.36, "in": 1.32}, {"file": "cb-m12t3-m12r6-b.mp4", "track": 0, "start": 13.8, "dur": 0.32, "in": 1.68}, {"file": "cb-m12t3-m12r6-b.mp4", "track": 0, "start": 14.12, "dur": 0.76, "in": 2.0}, {"file": "cb-m12t3-m12r6-b.mp4", "track": 0, "start": 14.88, "dur": 1.16, "in": 2.76}, {"file": "cb-s01t3-s01r6-b.mp4", "track": 0, "start": 16.04, "dur": 1.36, "in": 3.12}, {"file": "cb-s02t3-s02r6-b.mp4", "track": 0, "start": 18.4, "dur": 1.72, "in": 0.48}, {"file": "cb-s02t3-s02r6-b.mp4", "track": 0, "start": 20.44, "dur": 0.8, "in": 4.72}, {"file": "cb-s02t3-s02r6-b.mp4", "track": 0, "start": 22.68, "dur": 0.76, "in": 6.28}, {"file": "cb-s03t3-s03r6-b.mp4", "track": 0, "start": 26.4, "dur": 1.04, "in": 0.0}, {"file": "cb-s03t3-s03r6-b.mp4", "track": 0, "start": 27.44, "dur": 3.4, "in": 1.04}]; const S="camping song 2 beat 3"; const PRE="C:\\Users\\jackt\\OneDrive\\Desktop\\Youtube Vids\\animation\\songs\\camping vid\\balaclava\\video\\premiere\\"; const BIN='t3 rap clips';
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
