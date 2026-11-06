const V=[{"file": "cb-t06-t06r3-a.mp4", "track": 4, "start": 109.8, "dur": 1.32, "in": 2.72, "was": "Tarquin rapping/4.4.mp4"}, {"file": "cb-t06-t06r3-a.mp4", "track": 4, "start": 111.12, "dur": 1.28, "in": 4.72, "was": "Tarquin rapping/4.4.mp4"}, {"file": "cb-t07-t07r3-b.mp4", "track": 3, "start": 113.2, "dur": 4.36, "in": 0.0, "was": "Tarquin rapping/5.mp4"}, {"file": "cb-t07-t07r3-b.mp4", "track": 3, "start": 118.24, "dur": 2.28, "in": 4.36, "was": "Tarquin rapping/5.mp4"}, {"file": "cb-t08-t08r3-a.mp4", "track": 2, "start": 123.6, "dur": 7.92, "in": 0.0, "was": "Tarquin rapping/6.mp4"}, {"file": "cb-t08-t08r3-a.mp4", "track": 2, "start": 131.52, "dur": 2.08, "in": 2.0, "was": "Tarquin rapping/6.mp4"}]; const S="camping balaclava 1"; const PRE="C:\\Users\\jackt\\OneDrive\\Desktop\\Youtube Vids\\animation\\songs\\camping vid\\balaclava\\video\\premiere\\"; const BIN='balaclava clips';
const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!==S) return {error:'wrong sequence',name:seq.name};
const root=await project.getRootItem(); let bin=null; for(const k of await root.getItems()){ if(k.name===BIN){ try{ const f=ppro.FolderItem.cast(k); if(f) bin=f; }catch(e){} } }
if(!bin) return {error:'no bin'};
const byPath={}; for(const it of await bin.getItems()){ try{ byPath[(await ppro.ClipProjectItem.cast(it).getMediaFilePath()).toLowerCase()]=it; }catch(e){} }
const ed=ppro.SequenceEditor.getEditor(seq); const tk=s=>helpers.secondsToTick(Math.round(s*25)/25+0.002); let done=0; const fail=[];
for(const r of V){ const p=PRE+r.file; try{ const item=byPath[p.toLowerCase()]; if(!item) throw 'not in bin'; const clip=ppro.ClipProjectItem.cast(item);
  helpers.withTransaction(project,'BadCode: balaclava in/out',ca=>ca.addAction(clip.createSetInOutPointsAction(tk(r.in),tk(r.in+r.dur))));
  helpers.withTransaction(project,'BadCode: balaclava swap',ca=>ca.addAction(ed.createOverwriteItemAction(item,tk(r.start),r.track,0)));
  helpers.withTransaction(project,'BadCode: balaclava clear',ca=>ca.addAction(clip.createClearInOutPointsAction())); done++; }catch(e){ fail.push([r.file,r.start,String(e).slice(0,100)]); } }
return {done,fail,mapped:Object.keys(byPath).length};
