"""edit-plan.json → premiere_eval bodies that lay the cut on V1 (clip sound on A2) of the ACTIVE sequence, in batches.
    python3 premiere_place.py <seq name> [batch size] [--only key,key]   → writes place-N.js"""
import json, pathlib, sys
HERE = pathlib.Path(__file__).parent
seq = sys.argv[1]; size = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 16
PLAN = sys.argv[sys.argv.index('--plan') + 1] if '--plan' in sys.argv else 'edit-plan.json'
only = sys.argv[sys.argv.index('--only') + 1].split(',') if '--only' in sys.argv else None
VID = pathlib.Path(json.load(open(HERE.parent / 'scene.json'))['media']) / 'video'
WIN = 'C:\\Users\\jackt\\OneDrive\\Desktop\\Youtube Vids\\animation\\songs\\bank robbery\\'
NOIR = VID.parent.parent / 'noir' / 'video'
rows, missing = [], []
for r in json.load(open(HERE.parent / PLAN)):
    if only and r['clip'] not in only: continue
    f = [NOIR / (r['clip'][3:] + '.mp4')] if r['clip'].startswith('cn:') else sorted(VID.glob(f"bg-{r['clip']}-*.mp4"))
    if not f or not f[0].exists(): missing.append((r['start'], r['clip'])); continue
    rel = ('noir\\video\\' if r['clip'].startswith('cn:') else 'gang\\video\\') + f[0].name
    rows.append([rel, r['start'], round(min(r['dur'], 6.0) + (0.05 if r['dur'] < 6 else 0), 3), r.get('in', 0)])
BODY = r"""const V=__V__; const S=__S__; const PRE=__PRE__;
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
"""
batches = [rows[i:i + size] for i in range(0, len(rows), size)]
for i, b in enumerate(batches):
    (HERE / f'place-{i}.js').write_text(BODY.replace('__V__', json.dumps(b)).replace('__S__', json.dumps(seq)).replace('__PRE__', json.dumps(WIN)))
print(len(rows), 'cuts in', len(batches), 'batches; missing clips:', missing)
