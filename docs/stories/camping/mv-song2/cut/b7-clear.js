const S="camping song 2 beat 7"; const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!==S) return {error:'wrong sequence',name:seq.name};
await seq.clearSelection(); const sel=await seq.getSelection(); let n=0;
for(const k of [0,1,2]){ const t=await seq.getVideoTrack(k); for(const it of (await t.getTrackItems(ppro.Constants.TrackItemType.CLIP,false))||[]){ if(it){ sel.addItem(it,true); n++; } } }
for(const k of [1,2,3]){ const t=await seq.getAudioTrack(k); for(const it of (await t.getTrackItems(ppro.Constants.TrackItemType.CLIP,false))||[]){ if(it){ sel.addItem(it,true); n++; } } }
const ed=ppro.SequenceEditor.getEditor(seq);
helpers.withTransaction(project,'BadCode: clear for beat 7',ca=>ca.addAction(ed.createRemoveItemsAction(sel,false,ppro.Constants.MediaType.ANY,false)));
return {selected:n};