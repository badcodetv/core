"""Premiere scripts for `camping song 2 beat 5` (a clone of beat 4) from edl-beat5.json: b5-clear.js empties V1-V3 and
A2-A4 (A1, the song, stays), then b5-place-N.js puts every piece back at its new time (clip audio on the muted A2-A4)."""
import json
from pathlib import Path
HERE = Path(__file__).parent
SEQ = 'camping song 2 beat 5'
e = json.load(open(HERE / 'edl-beat5.json'))
win = lambda p: 'C:\\' + p.split('/mnt/c/', 1)[1].replace('/', '\\')
rows = [[win(x['src']), x['start'], round(x['end'] - x['start'], 3), x['in'], vt, vt + 1]
        for vt, tr in enumerate(('V1', 'V2', 'V3')) for x in e[tr] if x['src'] and x['end'] - x['start'] >= 0.08]  # no 1-frame glitches
CLEAR = '''const S=%s; const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!==S) return {error:'wrong sequence',name:seq.name};
await seq.clearSelection(); const sel=await seq.getSelection(); let n=0;
for(const k of [0,1,2]){ const t=await seq.getVideoTrack(k); for(const it of (await t.getTrackItems(ppro.Constants.TrackItemType.CLIP,false))||[]){ if(it){ sel.addItem(it,true); n++; } } }
for(const k of [1,2,3]){ const t=await seq.getAudioTrack(k); for(const it of (await t.getTrackItems(ppro.Constants.TrackItemType.CLIP,false))||[]){ if(it){ sel.addItem(it,true); n++; } } }
const ed=ppro.SequenceEditor.getEditor(seq);
helpers.withTransaction(project,'BadCode: clear for beat 5',ca=>ca.addAction(ed.createRemoveItemsAction(sel,false,ppro.Constants.MediaType.ANY,false)));
return {selected:n};''' % json.dumps(SEQ)
(HERE / 'b5-clear.js').write_text(CLEAR)
JS = '''const P=%s; const R0=%s; const R=R0.map(r=>[P[r[0]],...r.slice(1)]); const S=%s;
const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!==S) return {error:'wrong sequence',name:seq.name};
const map={}; async function walk(f){ for(const it of await f.getItems()){ const fo=ppro.FolderItem.cast(it); if(fo){await walk(fo);continue;} const c=ppro.ClipProjectItem.cast(it); if(c){ try{ const p=await c.getMediaFilePath(); if(p && !map[p.toLowerCase()]) map[p.toLowerCase()]=it; }catch(e){} } } }
await walk(await project.getRootItem());
const ed=ppro.SequenceEditor.getEditor(seq); const tk=s=>helpers.secondsToTick(Math.round(s*25)/25+0.002); let done=0; const fail=[];
for(const [p,st,d,inp,vt,at] of R){ try{ const item=map[p.toLowerCase()]; if(!item) throw 'not in project';
  const clip=ppro.ClipProjectItem.cast(item);
  helpers.withTransaction(project,'BadCode: in/out',ca=>ca.addAction(clip.createSetInOutPointsAction(tk(inp),tk(inp+d))));
  helpers.withTransaction(project,'BadCode: place',ca=>ca.addAction(ed.createOverwriteItemAction(item,tk(st),vt,at)));
  helpers.withTransaction(project,'BadCode: clear',ca=>ca.addAction(clip.createClearInOutPointsAction())); done++; }catch(e){ fail.push([p.split('\\\\').pop(),st,String(e).slice(0,80)]); } }
return {done,fail};'''
for f in HERE.glob('b5-place-*.js'): f.unlink()
N = 45
for k in range(0, len(rows), N):
    ch = rows[k:k + N]; P = sorted({r[0] for r in ch})
    (HERE / f'b5-place-{k // N}.js').write_text(JS % (json.dumps(P), json.dumps([[P.index(r[0])] + r[1:] for r in ch]), json.dumps(SEQ)))
print(len(rows), 'pieces ->', (len(rows) + N - 1) // N, 'place scripts + b5-clear.js')
