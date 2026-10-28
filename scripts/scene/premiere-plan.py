#!/usr/bin/env python3
"""Turn a stage-4 edl.json into a Premiere build plan: picture on V1 with in/out, one audio track per
stem, voices as one clip per line.

Each voice line is cut out of its stem (so gain, filters and lip-sync stretches baked into the stem
come along) into <cut dir>/premiere/lines/NN-<stem>.wav. Music and sfx stems go in whole, from 0.
Video files that carry their own audio get a silent copy beside them (<name>-noaudio.mp4), so placing
picture never drops sound onto a voice track. Stems in --skip are left out (e.g. Kai's own music).

Track order: vox-* stems first, then mus-*, then sfx-*, in edl order within each group.

    python3 scripts/scene/premiere-plan.py <edl.json> <out plan.json> [--skip mus-M0-radio] [--tag rough2]
                                           [--seq <sequence name>]

--seq also writes <out>.place.js beside the plan: the premiere_eval body that places every clip of the
plan on the ACTIVE sequence (it refuses to run on any other), finding media in the bin named after the
sequence. The build is then: premiere_import(files, bin=<seq>) -> premiere_create_sequence(<seq>,
fromItems=[first V1 clip's item]) -> premiere_eval(place.js) -> premiere_get_sequence -> export a frame
and look. See the scene-timeline skill, "Premiere sync".

--tag puts the line files under premiere/<tag>/lines/, so a later build never overwrites the files an
earlier sequence (rough1) still plays.

The plan is {"files": [...], "video": [[file, t, in, dur]], "audio": [[file, t, track]], "tracks": [names]}.
"""
import json
import pathlib
import subprocess
import sys

PAD_IN, PAD_OUT = 0.05, 0.12


PLACE_JS = r"""const V=__V__;
const A=__A__;
const S=__S__;
const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!==S) return {error:'wrong sequence',name:seq.name};
const root=await project.getRootItem(); let bin=null; for(const k of await root.getItems()){ if(k.name===S){ let fo=null; try{ fo=ppro.FolderItem.cast(k); }catch(e){} if(fo) bin=fo; } }
if(!bin) return {error:'no bin named '+S};
const byPath={}; for(const it of await bin.getItems()){ try{ byPath[(await ppro.ClipProjectItem.cast(it).getMediaFilePath()).toLowerCase()]=it; }catch(e){} }
const ed=ppro.SequenceEditor.getEditor(seq); const tk=s=>helpers.secondsToTick(Math.round(s*24)/24+0.002); let done=0; const fail=[];
for(const [p,t,i,d] of V){ try{ const item=byPath[p.toLowerCase()]; const clip=ppro.ClipProjectItem.cast(item);
  helpers.withTransaction(project,S+' in/out',ca=>ca.addAction(clip.createSetInOutPointsAction(tk(i),tk(i+d))));
  helpers.withTransaction(project,S+' place',ca=>ca.addAction(ed.createOverwriteItemAction(item,tk(t),0,0)));
  helpers.withTransaction(project,S+' clear',ca=>ca.addAction(clip.createClearInOutPointsAction())); done++; }catch(e){ fail.push([p,String(e).slice(0,100)]); } }
for(const [p,t,tr] of A){ try{ const item=byPath[p.toLowerCase()];
  helpers.withTransaction(project,S+' audio',ca=>ca.addAction(ed.createOverwriteItemAction(item,helpers.secondsToTick(t),0,tr))); done++; }catch(e){ fail.push([p,t,String(e).slice(0,100)]); } }
const counts=[]; const n=await seq.getAudioTrackCount(); for(let k=0;k<n;k++){ counts.push((await (await seq.getAudioTrack(k)).getTrackItems(1,false)).length); }
const vc=(await (await seq.getVideoTrack(0)).getTrackItems(1,false)).length;
return {done,fail,vc,counts,mapped:Object.keys(byPath).length};
"""


def win(p):
    """/mnt/d/x/y -> D:\\x\\y, the form getMediaFilePath() reports."""
    p = str(p)
    return p[5].upper() + ':' + p[6:].replace('/', '\\') if p.startswith('/mnt/') else p


def has_audio(f):
    return bool(subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'a', '-show_entries',
                                'stream=index', '-of', 'csv=p=0', f], capture_output=True, text=True).stdout.strip())


def main(argv):
    edl_path, out_path = pathlib.Path(argv[0]), pathlib.Path(argv[1])
    skip = set(argv[argv.index('--skip') + 1].split(',')) if '--skip' in argv else set()
    edl = json.loads(edl_path.read_text())
    tag = argv[argv.index('--tag') + 1] if '--tag' in argv else ''
    lines_dir = edl_path.parent / 'premiere' / tag / 'lines'
    lines_dir.mkdir(parents=True, exist_ok=True)

    stems = [a for a in edl['audio'] if a['name'] not in skip]
    order = [a for g in ('vox-', 'mus-', 'sfx-') for a in stems if a['name'].startswith(g)]
    order += [a for a in stems if a not in order]
    track = {a['name']: k for k, a in enumerate(order)}

    video = []
    for c in edl['video']:
        f = c['file']
        if has_audio(f):
            quiet = str(pathlib.Path(f).with_name(pathlib.Path(f).stem + '-noaudio.mp4'))
            if not pathlib.Path(quiet).exists():
                subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f, '-an', '-c:v', 'copy', quiet], check=True)
            f = quiet
        video.append([f, c['start'], c['in'], c['dur']])

    audio, n = [], 0
    for a in order:
        name = a['name']
        if not name.startswith('vox-'):
            audio.append([a['file'], 0.0, track[name]])
            continue
        ev = sorted((e for e in edl['events'] if e['stem'] == name), key=lambda e: e['t'])
        for i, e in enumerate(ev):
            t0 = max(0.0, e['t'] - PAD_IN)
            t1 = e['t'] + e['dur'] + PAD_OUT
            if i + 1 < len(ev):
                t1 = min(t1, ev[i + 1]['t'] - 0.01)
            out = lines_dir / ('%02d-%s.wav' % (n, name))
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', '%.4f' % t0, '-to', '%.4f' % t1,
                            '-i', a['file'], '-c:a', 'pcm_s24le', str(out)], check=True)
            audio.append([str(out), round(t0, 4), track[name]])
            n += 1

    files = sorted({v[0] for v in video} | {x[0] for x in audio})
    out_path.write_text(json.dumps({'sequence_total': edl['total'], 'fps': edl['fps'], 'files': files,
                                    'video': video, 'audio': audio,
                                    'tracks': [a['name'] for a in order]}, indent=1))
    if '--seq' in argv:
        seq = argv[argv.index('--seq') + 1]
        js = (PLACE_JS.replace('__V__', json.dumps([[win(f), t, i, d] for f, t, i, d in video]))
              .replace('__A__', json.dumps([[win(f), t, k] for f, t, k in audio]))
              .replace('__S__', json.dumps(seq)))
        out_path.with_suffix('.place.js').write_text(js)
    print(out_path, len(video), 'shots', len(audio), 'audio clips', len(order), 'tracks')


if __name__ == '__main__':
    main(sys.argv[1:])
