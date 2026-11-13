"""Place the 24 action clips on V7 of `camping song 2` (a new top track; mute V7 and the cut underneath is the old one).
Song 2 grid: 176 BPM, first downbeat 0.122 s. One two-bar clip every 6 bars from bar 11 (15.1 s) to ~206 s.
Order follows the cut: Bob's clips first (his verse), Tarquin's in the middle, the mirrored pairs back to back at the end.
In point 0.2 s (the action peaks in the first 2-3 s). Files: 1080p silent copies in <media>/video/premiere/.
    python3 place.py → plan.json + place-N.js (premiere_eval bodies)"""
import json, pathlib
HERE = pathlib.Path(__file__).parent
BAR, T0, FPS = 60 / 176 * 4, 0.122, 25
fr = lambda s: round(s * FPS) / FPS
ORDER = 'b1 b2 b6 b22 b23 b24 b25 b26 t2 t3 t4 t6 t21 t22 t23 t24 t25 u23 u25 x3 x4 x5 x6 x2'.split()
pick = {p.split('r')[0]: p for p in json.load(open(HERE.parent / 'scene.json'))['picked']}
WIN = 'C:\\Users\\jackt\\OneDrive\\Desktop\\Youtube Vids\\animation\\songs\\camping vid\\action\\video\\premiere\\'
rows = []
for n, k in enumerate(ORDER):
    s = fr(T0 + (11 + 6 * n) * BAR)
    rows.append({'key': k, 'file': f'ca-{k}-{pick[k]}.mp4', 'start': s, 'dur': fr(2 * BAR), 'in': 0.2, 'track': 6})
json.dump(rows, open(HERE / 'plan.json', 'w'), indent=1)
BODY = r"""const V=__V__; const S='camping song 2';
const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!==S) return {error:'wrong sequence',name:seq.name};
const ed=ppro.SequenceEditor.getEditor(seq); const tk=s=>helpers.secondsToTick(Math.round(s*25)/25+0.002); let done=0; const fail=[];
for(const r of V){ try{ const item=await helpers.resolveProjectItem(project,r.file); if(!item) throw 'not found';
  const clip=ppro.ClipProjectItem.cast(item);
  helpers.withTransaction(project,'BadCode: action in/out',ca=>ca.addAction(clip.createSetInOutPointsAction(tk(r.in),tk(r.in+r.dur))));
  helpers.withTransaction(project,'BadCode: action place',ca=>ca.addAction(ed.createOverwriteItemAction(item,tk(r.start),r.track,0)));
  helpers.withTransaction(project,'BadCode: action clear',ca=>ca.addAction(clip.createClearInOutPointsAction())); done++; }catch(e){ fail.push([r.file,r.start,String(e).slice(0,100)]); } }
return {done,fail};
"""
for f in HERE.glob('place-*.js'): f.unlink()
for n, i in enumerate(range(0, len(rows), 12)):
    (HERE / f'place-{n}.js').write_text(BODY.replace('__V__', json.dumps(rows[i:i + 12])))
for r in rows: print(r['key'], r['start'], r['dur'])
