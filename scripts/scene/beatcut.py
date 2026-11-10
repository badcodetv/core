#!/usr/bin/env python3
"""Preview cut of a scene to the song (plus <out dir>/edl.json in the timeline format, for build-timeline.py), from a cut json (song, song_in, bpm, fps, shots[{clip, beats, in}]).
Shot boundaries are rounded to whole frames from the beat grid, so the cut never drifts off the beat.
  python3 scripts/scene/beatcut.py <scene-dir> <cut.json> <out.mp4>
Preview only: the deliverable is per-beat clips on a Premiere timeline."""
import json, pathlib, subprocess, sys
import os as _os, sys as _sys  # cut files written on another machine open on this one (scripts/drive/localmap.py)
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'drive'))
from localmap import localize  # noqa: E402
scene, spec, out = pathlib.Path(sys.argv[1]), localize(json.loads(pathlib.Path(sys.argv[2]).read_text())), sys.argv[3]
media = pathlib.Path(localize(json.loads((scene / 'scene.json').read_text()))['media']) / 'video'
beat, fps = 60 / spec['bpm'], spec['fps']
args, parts, b, f0 = ['ffmpeg', '-v', 'error', '-y'], [], 0, 0
names = {x['key']: x for x in json.loads((scene / 'scene.json').read_text()).get('beats', [])}
beats, video = [], []
for i, s in enumerate(spec['shots']):
    b += s['beats']; f1 = round(b * beat * fps); n = f1 - f0
    k0 = s.get('beat', str(i)); info = names.get(k0, {})
    beats.append({'id': k0, 'title': info.get('name', s['clip']), 'start': f0 / fps, 'dur': n / fps,
                  'see': s.get('why', ''), 'act': f"beats {b - s['beats'] + 1}-{b}", 'lines': []})
    video.append({'file': str(media / s['clip']), 'source': str(media / s['clip']), 'start': f0 / fps, 'dur': n / fps,
                  'beat': k0, 'in': s['in']})
    f0 = f1
    args += ['-ss', str(s['in']), '-i', str(media / s['clip'])]
    parts.append(f"[{i}:v]fps={fps},scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,trim=end_frame={n},setpts=PTS-STARTPTS[v{i}]")
    print(f"{s['clip']:24} beats {b - s['beats'] + 1:2}-{b:2}  {n} frames  in {s['in']}")
k = len(spec['shots']); dur = f0 / fps
args += ['-ss', str(spec['song_in']), '-t', f'{dur:.4f}', '-i', spec['song']]
fc = ';'.join(parts) + ';' + ''.join(f'[v{i}]' for i in range(k)) + f'concat=n={k}:v=1:a=0[v];[{k}:a]afade=t=out:st={dur - 0.02:.3f}:d=0.02[a]'
subprocess.run(args + ['-filter_complex', fc, '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '256k', out], check=True)
print(f'{dur:.3f}s -> {out}')
edl = {'sequence': spec.get('sequence', scene.name), 'fps': fps, 'total': dur, 'beats': beats, 'video': video,
       'audio': [{'track': 'A1', 'name': 'mus-song'}],
       'events': [{'stem': 'mus-song', 't': 0, 'dur': dur, 'what': f"song from {spec['song_in']} s", 'src': spec['song']}],
       'flags': spec.get('flags', [])}
pathlib.Path(out).with_name('edl.json').write_text(json.dumps(edl, indent=1))
