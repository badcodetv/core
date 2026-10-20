#!/usr/bin/env python3
"""Print the premiere_eval body that places entries [A:B] of the rough cut on `gpom-second-half-rough`.

Picture on V1 (with in/out), then sound: A1 narrator · A2 dialogue · A3 music and the crowd (the four
crowd voices are pre-mixed into v-14-crowd-mix.wav, because clips on one track cannot overlap).
Items are addressed by Premiere id (the extended clips share filenames with the originals); the id
map is <scratch>/premiere-ids.json, written from the import results. About ten placements an eval
(docs/premiere/api-notes.md, 2026-10-04).

    python3 scripts/gpom/second-half-video/rough_place.py count
    python3 scripts/gpom/second-half-video/rough_place.py eval 0 10
"""
import json
import os
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import shots as S  # noqa: E402

if '--cut2' in sys.argv:  # cut 2 part 1 on gpom-second-half-rough2: picture on V1, one stem per audio track
    import cut2  # noqa: E402
    cut2.place([a for a in sys.argv[1:] if a != '--cut2'])
    sys.exit()

SEQ = 'gpom-second-half-rough'
IDS = json.loads((pathlib.Path(os.environ['HOME']) / '.cache/badcode-gpom-second-half/premiere-ids.json').read_text())
IDS['audio']['v-14-crowd-mix.wav'] = 'c3df1d19-4fc1-4f72-bbb5-5dfc0c787499'
rc = json.loads((S.CLIPS / 'audio' / 'rough-cut.json').read_text())

plan = []
for name, t, i, d, n, ext in rc['clips']:
    item = IDS['rt'][name[3:]] if name.startswith('rt/') else IDS['orig'][name]
    plan.append([item, t, i, d, 'v', 0])
crowd_done = False
for fname, t, track, key in rc['audio']:
    if '-crowd' in key:
        if crowd_done:
            continue
        fname, track, crowd_done = 'v-14-crowd-mix.wav', 2, True
    plan.append([IDS['audio'][fname], t, 0, 0, 'a', min(track, 2)])

if sys.argv[1] == 'count':
    print(len(plan))
    sys.exit()
a, b = int(sys.argv[2]), int(sys.argv[3])
print("""const plan=%s;
const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!=='%s') return {error:'wrong sequence',name:seq.name};
const ed=ppro.SequenceEditor.getEditor(seq); const tk=s=>helpers.secondsToTick(Math.round(s*24)/24+0.002);
let done=0; const fail=[];
for(const [id,t,i,d,kind,tr] of plan){ try{
  const item=await helpers.resolveProjectItem(project,id); const clip=ppro.ClipProjectItem.cast(item);
  if(kind==='v'){
    helpers.withTransaction(project,'rough in/out',ca=>ca.addAction(clip.createSetInOutPointsAction(tk(i),tk(i+d))));
    helpers.withTransaction(project,'rough place',ca=>ca.addAction(ed.createOverwriteItemAction(item,tk(t),0,0)));
    helpers.withTransaction(project,'rough clear',ca=>ca.addAction(clip.createClearInOutPointsAction()));
  } else {
    helpers.withTransaction(project,'rough place audio',ca=>ca.addAction(ed.createOverwriteItemAction(item,helpers.secondsToTick(t),0,tr)));
  }
  done++; }catch(e){ fail.push([id,t,String(e&&e.message||e).slice(0,120)]); } }
const saved=await project.save();
return {done,fail,saved,range:[%d,%d]};""" % (json.dumps(plan[a:b], separators=(',', ':')), SEQ, a, min(b, len(plan))))
