"""The hand-cut workbench for chorus 1 (Kai, 10 Nov: "a sequence that we could use to edit this exact sequence ...
the same way" as 01 GPOM chorus outbreak r3 edit). Writes workbench-r1.js, a premiere_eval body.

Layout of "01 GPOM chorus poverty r1 edit" (24 fps, 1920x1080), sequence 0 = song 65.583 s:
  0-4 s      run-in: the intro's last 4 s ("01 GPOM start r2" 58.583-62.583, picture only)
  4-15.042   the chorus: Kai's pick, sequence A (cut-r1a.json), the 1080p silent clips on V1
  15.042-19.042  the bank downfall's first 4 s ("01 GPOM start r2" 62.583-66.583, picture only)
  A1         the song, unbroken, 65.583-84.625 (in the film, chorus 1 goes back in as an insert, so the song runs on)
  markers    every beat; red CHORUS on the kick, cyan BANKS where the downfall starts
  bin        "chorus poverty options": the 12 clips, named "<subject> | <stem>", in points at their best moment

Run (in the session that holds the Premiere bridge):
  1. premiere_import  paths = <media>/video/1080/*.mp4   bin = "chorus poverty options"
  2. premiere_create_sequence  name = "01 GPOM chorus poverty r1 edit"  fromItems = ["pv-p01-MW1-a2-1080.mp4"]
  3. premiere_eval  code = the contents of workbench-r1.js   (it refuses to run on any other active sequence)
  4. premiere_save
  python3 workbench.py
"""
import json, pathlib

HERE = pathlib.Path(__file__).parent
spec = json.loads((HERE / 'cut-r1a.json').read_text())
FPS, B, PHASE = 24, 60 / 173.975, 30.312
SONG0 = 1574            # song frame at sequence 0 (65.583 s)
RUN = 96                # 4 s run-in
CHORUS = 265            # 32 beats
TAIL = 96               # 4 s of the banks
NAMES = {'MW1-a2': 'motorway drone', 'MW1-b1': 'motorway footbridge', 'QU1-b2': 'queue', 'PK1-a2': 'Hyde Park towers',
         'PK1-b1': 'Primrose Hill bench', 'ST1-a2': 'station', 'ES1-b2': 'tower block', 'HS1-c1': 'promenade',
         'FI1-c2': 'brazier faces', 'FC1-a2': 'warehouse fence', 'FC1-c2': 'data centre', 'GL1-b2': 'Glasgow'}
BEST = {}   # stem -> best in point (s), the first in point sequence A uses
shots, f0, b = [], 0, 0
for s in spec['shots']:
    b += s['beats']; f1 = round(b * B * FPS)
    stem = s['clip'][:-4] + '-1080.mp4'
    shots.append([stem, RUN + f0, round(s['in'] * FPS), f1 - f0])
    BEST.setdefault(stem, round(s['in'] * FPS))
    f0 = f1
assert f0 == CHORUS, f0
media = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/chorus-poverty/video/1080')
for f in sorted(media.glob('pv-p*-1080.mp4')):
    BEST.setdefault(f.name, 72)
opts = {stem: [NAMES[stem.split('-')[2] + '-' + stem.split('-')[3]], fr] for stem, fr in BEST.items()}

markers = []
for n in range(103, 158):
    t = PHASE + n * B - SONG0 / FPS
    if t < 0 or t > (RUN + CHORUS + TAIL) / FPS: continue
    k = n - 114
    if n == 114: name, col = 'CHORUS starts (the drop, bar 1)', 1
    elif n == 146: name, col = 'BANKS start (bank downfall)', 7
    elif n > 146: name, col = ('banks bar %d' % ((n - 146) // 4 + 1) if (n - 146) % 4 == 0 else '·'), 5
    elif k < 0: name, col = ('run-in bar %d' % (k // 4) if k % 4 == 0 else '·'), 5
    else: name, col = ('bar %d' % (k // 4 + 1) if k % 4 == 0 else 'beat %d' % (k % 4 + 1)), (4 if k % 4 == 0 else 5)
    markers.append([name, round(t, 4), col])

js = f"""// built by docs/stories/gitpush-origin-master/scenes/chorus-poverty/workbench.py from cut-r1a.json
const NAME='01 GPOM chorus poverty r1 edit';
const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!==NAME) return {{error:'make '+NAME+' the active sequence first', active:seq.name}};
const F=f=>helpers.secondsToTick(f/24+0.002), T=s=>helpers.secondsToTick(s);
const ed=ppro.SequenceEditor.getEditor(seq);
const SHOTS={json.dumps(shots)}, OPTS={json.dumps(opts)}, MARKS={json.dumps(markers)};
const RUN={RUN}, CHORUS={CHORUS}, TAIL={TAIL}, SONG0={SONG0};
// the bin
const root=await project.getRootItem(); let bin=null, song=null;
for(const k of await root.getItems()){{ if(k.name==='chorus poverty options') bin=ppro.FolderItem.cast(k); if(k.name==='Git Push Origin Master.mp3') song=k; }}
if(!bin) return {{error:'no bin "chorus poverty options": import the 1080 clips first'}};
if(!song) return {{error:'no song item "Git Push Origin Master.mp3" at the project root'}};
const items={{}}; for(const it of await bin.getItems()) items[it.name]=it;
const missing=Object.keys(OPTS).filter(n=>!items[n]); if(missing.length) return {{error:'missing clips',missing}};
async function clearTrack(tr){{ const its=await tr.getTrackItems(1,false); if(!its.length) return 0;
  const sel=await seq.getSelection(); for(const it of await sel.getTrackItems()) sel.removeItem(it); for(const it of its) sel.addItem(it,true);
  helpers.withTransaction(project,'clear',ca=>ca.addAction(ed.createRemoveItemsAction(sel,false,ppro.Constants.MediaType.ANY,false))); return its.length; }}
// 1. empty the sequence (create_sequence laid the first clip down)
for(let k=0;k<await seq.getVideoTrackCount();k++) await clearTrack(await seq.getVideoTrack(k));
for(let k=0;k<await seq.getAudioTrackCount();k++) await clearTrack(await seq.getAudioTrack(k));
// 2. context picture from the film: the intro's last 4 s, and the banks' first 4 s (its audio lands on A2 and is removed)
const film=(await project.getSequences()).find(q=>q.name==='01 GPOM start r2');
let ctx='no 01 GPOM start r2';
if(film){{ const fi=await film.getProjectItem(); const fc=ppro.ClipProjectItem.cast(fi);
  helpers.withTransaction(project,'ctx io',ca=>ca.addAction(fc.createSetInOutPointsAction(F(1502-RUN),F(1502))));
  helpers.withTransaction(project,'ctx intro',ca=>ca.addAction(ed.createOverwriteItemAction(fi,F(0),0,1)));
  helpers.withTransaction(project,'ctx io',ca=>ca.addAction(fc.createSetInOutPointsAction(F(1502),F(1502+TAIL))));
  helpers.withTransaction(project,'ctx banks',ca=>ca.addAction(ed.createOverwriteItemAction(fi,F(RUN+CHORUS),0,1)));
  helpers.withTransaction(project,'ctx clear',ca=>ca.addAction(fc.createClearInOutPointsAction()));
  for(let k=1;k<await seq.getAudioTrackCount();k++) await clearTrack(await seq.getAudioTrack(k)); ctx='ok'; }}
// 3. the song on A1, unbroken
const sc=ppro.ClipProjectItem.cast(song);
helpers.withTransaction(project,'song io',ca=>ca.addAction(sc.createSetInOutPointsAction(F(SONG0),F(SONG0+RUN+CHORUS+TAIL))));
helpers.withTransaction(project,'song',ca=>ca.addAction(ed.createOverwriteItemAction(song,F(0),0,0)));
helpers.withTransaction(project,'song clear',ca=>ca.addAction(sc.createClearInOutPointsAction()));
// 4. sequence A on V1
for(const [stem,at,inF,n] of SHOTS){{ const c=ppro.ClipProjectItem.cast(items[stem]);
  helpers.withTransaction(project,'io',ca=>ca.addAction(c.createSetInOutPointsAction(F(inF),F(inF+n))));
  helpers.withTransaction(project,'shot',ca=>ca.addAction(ed.createOverwriteItemAction(items[stem],F(at),0,0))); }}
// 5. the options bin: in point at each clip's best moment, out at the end; named "<subject> | <stem>"
for(const [stem,[label,inF]] of Object.entries(OPTS)){{ const it=items[stem]; const c=ppro.ClipProjectItem.cast(it);
  helpers.withTransaction(project,'opt io',ca=>ca.addAction(c.createSetInOutPointsAction(F(inF),T(8))));
  helpers.withTransaction(project,'opt name',ca=>ca.addAction(it.createSetNameAction(label+' | '+stem.replace('-1080.mp4','')))); }}
// 6. beat markers
const M=await ppro.Markers.getMarkers(seq); let mk=0, merr=null;
for(const [name,t,col] of MARKS){{ try{{ helpers.withTransaction(project,'marker',ca=>ca.addAction(M.createAddMarkerAction(name,'Comment',T(t),T(0),''))); mk++; }}catch(e){{ merr=String(e); break; }} }}
let colored=0; try{{ for(const m of await M.getMarkers()){{ const nm=await m.getName(); const e=MARKS.find(x=>x[0]===nm); if(e){{ helpers.withTransaction(project,'colour',ca=>ca.addAction(m.createSetColorByIndexAction(e[2]))); colored++; }} }} }}catch(e){{ merr=merr||String(e); }}
// report
const out={{ctx,markers:mk,colored,merr}};
for(const [lab,tr] of [['V1',await seq.getVideoTrack(0)],['A1',await seq.getAudioTrack(0)]]){{ out[lab]=[];
  for(const it of await tr.getTrackItems(1,false)) out[lab].push([(await it.getName()).slice(0,28),+(await it.getStartTime()).seconds.toFixed(3),+(await it.getEndTime()).seconds.toFixed(3),+(await it.getInPoint()).seconds.toFixed(3)]); }}
return out;
"""
(HERE / 'workbench-r1.js').write_text(js)
print(len(shots), 'shots,', len(markers), 'markers ->', HERE / 'workbench-r1.js')
