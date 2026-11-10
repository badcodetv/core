// built by docs/stories/gitpush-origin-master/scenes/chorus-poverty/workbench.py from cut-r1a.json
const NAME='01 GPOM chorus poverty r1 edit';
const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!==NAME) return {error:'make '+NAME+' the active sequence first', active:seq.name};
const F=f=>helpers.secondsToTick(f/24+0.002), T=s=>helpers.secondsToTick(s);
const ed=ppro.SequenceEditor.getEditor(seq);
const SHOTS=[["pv-p01-MW1-a2-1080.mp4", 96, 72, 17], ["pv-p02-MW1-b1-1080.mp4", 113, 72, 16], ["pv-p03-QU1-b2-1080.mp4", 129, 72, 17], ["pv-p06-ST1-a2-1080.mp4", 146, 60, 16], ["pv-p07-ES1-b2-1080.mp4", 162, 72, 17], ["pv-p08-HS1-c1-1080.mp4", 179, 48, 16], ["pv-p10-FC1-a2-1080.mp4", 195, 2, 9], ["pv-p11-FC1-c2-1080.mp4", 204, 72, 16], ["pv-p12-GL1-b2-1080.mp4", 220, 72, 17], ["pv-p05-PK1-b1-1080.mp4", 237, 12, 16], ["pv-p09-FI1-c2-1080.mp4", 253, 72, 25], ["pv-p04-PK1-a2-1080.mp4", 278, 96, 83]], OPTS={"pv-p01-MW1-a2-1080.mp4": ["motorway drone", 72], "pv-p02-MW1-b1-1080.mp4": ["motorway footbridge", 72], "pv-p03-QU1-b2-1080.mp4": ["queue", 72], "pv-p06-ST1-a2-1080.mp4": ["station", 60], "pv-p07-ES1-b2-1080.mp4": ["tower block", 72], "pv-p08-HS1-c1-1080.mp4": ["promenade", 48], "pv-p10-FC1-a2-1080.mp4": ["warehouse fence", 2], "pv-p11-FC1-c2-1080.mp4": ["data centre", 72], "pv-p12-GL1-b2-1080.mp4": ["Glasgow", 72], "pv-p05-PK1-b1-1080.mp4": ["Primrose Hill bench", 12], "pv-p09-FI1-c2-1080.mp4": ["brazier faces", 72], "pv-p04-PK1-a2-1080.mp4": ["Hyde Park towers", 96]}, MARKS=[["\u00b7", 0.251, 5], ["\u00b7", 0.5959, 5], ["\u00b7", 0.9408, 5], ["run-in bar -2", 1.2856, 5], ["\u00b7", 1.6305, 5], ["\u00b7", 1.9754, 5], ["\u00b7", 2.3203, 5], ["run-in bar -1", 2.6652, 5], ["\u00b7", 3.01, 5], ["\u00b7", 3.3549, 5], ["\u00b7", 3.6998, 5], ["CHORUS starts (the drop, bar 1)", 4.0447, 1], ["beat 2", 4.3895, 5], ["beat 3", 4.7344, 5], ["beat 4", 5.0793, 5], ["bar 2", 5.4242, 4], ["beat 2", 5.769, 5], ["beat 3", 6.1139, 5], ["beat 4", 6.4588, 5], ["bar 3", 6.8037, 4], ["beat 2", 7.1486, 5], ["beat 3", 7.4934, 5], ["beat 4", 7.8383, 5], ["bar 4", 8.1832, 4], ["beat 2", 8.5281, 5], ["beat 3", 8.8729, 5], ["beat 4", 9.2178, 5], ["bar 5", 9.5627, 4], ["beat 2", 9.9076, 5], ["beat 3", 10.2524, 5], ["beat 4", 10.5973, 5], ["bar 6", 10.9422, 4], ["beat 2", 11.2871, 5], ["beat 3", 11.632, 5], ["beat 4", 11.9768, 5], ["bar 7", 12.3217, 4], ["beat 2", 12.6666, 5], ["beat 3", 13.0115, 5], ["beat 4", 13.3563, 5], ["bar 8", 13.7012, 4], ["beat 2", 14.0461, 5], ["beat 3", 14.391, 5], ["beat 4", 14.7359, 5], ["BANKS start (bank downfall)", 15.0807, 7], ["\u00b7", 15.4256, 5], ["\u00b7", 15.7705, 5], ["\u00b7", 16.1154, 5], ["banks bar 2", 16.4602, 5], ["\u00b7", 16.8051, 5], ["\u00b7", 17.15, 5], ["\u00b7", 17.4949, 5], ["banks bar 3", 17.8397, 5], ["\u00b7", 18.1846, 5], ["\u00b7", 18.5295, 5], ["\u00b7", 18.8744, 5]];
const RUN=96, CHORUS=265, TAIL=96, SONG0=1574;
// the bin
const root=await project.getRootItem(); let bin=null, song=null;
for(const k of await root.getItems()){ if(k.name==='chorus poverty options') bin=ppro.FolderItem.cast(k); if(k.name==='Git Push Origin Master.mp3') song=k; }
if(!bin) return {error:'no bin "chorus poverty options": import the 1080 clips first'};
if(!song) return {error:'no song item "Git Push Origin Master.mp3" at the project root'};
const items={}; for(const it of await bin.getItems()) items[it.name]=it;
const missing=Object.keys(OPTS).filter(n=>!items[n]); if(missing.length) return {error:'missing clips',missing};
async function clearTrack(tr){ const its=await tr.getTrackItems(1,false); if(!its.length) return 0;
  const sel=await seq.getSelection(); for(const it of await sel.getTrackItems()) sel.removeItem(it); for(const it of its) sel.addItem(it,true);
  helpers.withTransaction(project,'clear',ca=>ca.addAction(ed.createRemoveItemsAction(sel,false,ppro.Constants.MediaType.ANY,false))); return its.length; }
// 1. empty the sequence (create_sequence laid the first clip down)
for(let k=0;k<await seq.getVideoTrackCount();k++) await clearTrack(await seq.getVideoTrack(k));
for(let k=0;k<await seq.getAudioTrackCount();k++) await clearTrack(await seq.getAudioTrack(k));
// 2. context picture from the film: the intro's last 4 s, and the banks' first 4 s (its audio lands on A2 and is removed)
const film=(await project.getSequences()).find(q=>q.name==='01 GPOM start r2');
let ctx='no 01 GPOM start r2';
if(film){ const fi=await film.getProjectItem(); const fc=ppro.ClipProjectItem.cast(fi);
  helpers.withTransaction(project,'ctx io',ca=>ca.addAction(fc.createSetInOutPointsAction(F(1502-RUN),F(1502))));
  helpers.withTransaction(project,'ctx intro',ca=>ca.addAction(ed.createOverwriteItemAction(fi,F(0),0,1)));
  helpers.withTransaction(project,'ctx io',ca=>ca.addAction(fc.createSetInOutPointsAction(F(1502),F(1502+TAIL))));
  helpers.withTransaction(project,'ctx banks',ca=>ca.addAction(ed.createOverwriteItemAction(fi,F(RUN+CHORUS),0,1)));
  helpers.withTransaction(project,'ctx clear',ca=>ca.addAction(fc.createClearInOutPointsAction()));
  for(let k=1;k<await seq.getAudioTrackCount();k++) await clearTrack(await seq.getAudioTrack(k)); ctx='ok'; }
// 3. the song on A1, unbroken
const sc=ppro.ClipProjectItem.cast(song);
helpers.withTransaction(project,'song io',ca=>ca.addAction(sc.createSetInOutPointsAction(F(SONG0),F(SONG0+RUN+CHORUS+TAIL))));
helpers.withTransaction(project,'song',ca=>ca.addAction(ed.createOverwriteItemAction(song,F(0),0,0)));
helpers.withTransaction(project,'song clear',ca=>ca.addAction(sc.createClearInOutPointsAction()));
// 4. sequence A on V1
for(const [stem,at,inF,n] of SHOTS){ const c=ppro.ClipProjectItem.cast(items[stem]);
  helpers.withTransaction(project,'io',ca=>ca.addAction(c.createSetInOutPointsAction(F(inF),F(inF+n))));
  helpers.withTransaction(project,'shot',ca=>ca.addAction(ed.createOverwriteItemAction(items[stem],F(at),0,0))); }
// 5. the options bin: in point at each clip's best moment, out at the end; named "<subject> | <stem>"
for(const [stem,[label,inF]] of Object.entries(OPTS)){ const it=items[stem]; const c=ppro.ClipProjectItem.cast(it);
  helpers.withTransaction(project,'opt io',ca=>ca.addAction(c.createSetInOutPointsAction(F(inF),T(8))));
  helpers.withTransaction(project,'opt name',ca=>ca.addAction(it.createSetNameAction(label+' | '+stem.replace('-1080.mp4','')))); }
// 6. beat markers
const M=await ppro.Markers.getMarkers(seq); let mk=0, merr=null;
for(const [name,t,col] of MARKS){ try{ helpers.withTransaction(project,'marker',ca=>ca.addAction(M.createAddMarkerAction(name,'Comment',T(t),T(0),''))); mk++; }catch(e){ merr=String(e); break; } }
let colored=0; try{ for(const m of await M.getMarkers()){ const nm=await m.getName(); const e=MARKS.find(x=>x[0]===nm); if(e){ helpers.withTransaction(project,'colour',ca=>ca.addAction(m.createSetColorByIndexAction(e[2]))); colored++; } } }catch(e){ merr=merr||String(e); }
// report
const out={ctx,markers:mk,colored,merr};
for(const [lab,tr] of [['V1',await seq.getVideoTrack(0)],['A1',await seq.getAudioTrack(0)]]){ out[lab]=[];
  for(const it of await tr.getTrackItems(1,false)) out[lab].push([(await it.getName()).slice(0,28),+(await it.getStartTime()).seconds.toFixed(3),+(await it.getEndTime()).seconds.toFixed(3),+(await it.getInPoint()).seconds.toFixed(3)]); }
return out;
