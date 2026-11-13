"""Swap plan for the Camping MV balaclava cut: every rap-to-camera item on the `camping` sequence is overwritten, on its
own track and over its own span, by the balaclava clip for that shot (1080p silent copy in <media>/video/premiere/).
In point = the original item's in point, pulled back so the piece ends inside the 8 s clip. A span longer than 8 s is
filled with a second piece (a jump cut back into the clip). The 12.mp4 item at 57.60 on V3 is under V4 and stays.

    python3 swap.py <state-camping.json> <sequence name>    → swap-plan.json + place-N.js (premiere_eval bodies, ≤10 each)
"""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).parent
state = json.load(open(sys.argv[1])); SEQ = sys.argv[2]
SHOT = {'bob rapping/1.mp4': 'cb-s01-s01r3-a', 'bob rapping/1.1.mp4': 'cb-s02-s02r3-a', 'bob rapping/2.mp4': 'cb-s03-s03r3-b',
        'bob rapping/3.mov': 'cb-s04-s04r3-b', 'bob rapping/4.mp4': 'cb-s05-s05r3-b', 'bob rapping/5.5.mp4': 'cb-s06-s06r3-b',
        'clips/12.mp4': 'cb-m12-m12r3-b', 'Tarquin rapping/2.1.mp4': 'cb-t03-t03r3-a', 'Tarquin rapping/3.mp4': 'cb-t04-t04r3-b',
        'Tarquin rapping/4.3.mp4': 'cb-t05-t05r3-b', 'Tarquin rapping/4.4.mp4': 'cb-t06-t06r3-a', 'Tarquin rapping/5.mp4': 'cb-t07-t07r3-b',
        'Tarquin rapping/6.mp4': 'cb-t08-t08r3-a'}
CLIP, FPS = 8.0, 25
WIN = 'C:\\Users\\jackt\\OneDrive\\Desktop\\Youtube Vids\\animation\\songs\\camping vid\\balaclava\\video\\premiere\\'
fr = lambda s: round(s * FPS) / FPS
rows = []
for t in state['videoTracks']:
    for c in t.get('items', []):
        if c.get('start') is None: continue
        key = next((k for k in SHOT if c.get('mediaPath', '').endswith('/' + k)), None)
        if not key or (key == 'clips/12.mp4' and t['index'] != 1): continue
        start, end = fr(c['start']), fr(c['end'])
        pos, i0 = start, c['inPoint']
        while end - pos > 0.01:
            d = min(end - pos, CLIP - 0.08)
            i = max(0.0, min(i0, CLIP - 0.04 - d))
            rows.append({'file': SHOT[key] + '.mp4', 'track': t['index'], 'start': pos, 'dur': fr(d), 'in': fr(i), 'was': key})
            pos = fr(pos + d); i0 = 2.0  # a second piece jumps back to 2 s in
rows.sort(key=lambda r: r['start'])
json.dump(rows, open(HERE / 'swap-plan.json', 'w'), indent=1)
BODY = r"""const V=__V__; const S=__S__; const PRE=__PRE__; const BIN='balaclava clips';
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
"""
for f in HERE.glob('place-*.js'): f.unlink()
for n, i in enumerate(range(0, len(rows), 10)):
    (HERE / f'place-{n}.js').write_text(BODY.replace('__V__', json.dumps(rows[i:i + 10])).replace('__S__', json.dumps(SEQ)).replace('__PRE__', json.dumps(WIN)))
print(len(rows), 'pieces;', (len(rows) + 9) // 10, 'evals')
for r in rows: print(r)
