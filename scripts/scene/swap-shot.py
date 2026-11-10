#!/usr/bin/env python3
"""Swap one shot of a cut for another clip, same slot: a new edl and a spliced preview, nothing else moves.

    python3 scripts/scene/swap-shot.py <from-edl.json> <out-dir> <shot-id> <new-clip> [--in S] [--id ID]
        [--at T] [--why "..."] [--round N] [--heading "..."] [--intro "..."]

For a note like "swap this shot for X" on a cut that is already final (e.g. a Premiere hand edit read back
with premiere-to-edl.py), where re-assembling from a plan would lose the hand edits. The preview keeps the
old preview's picture outside the slot and ALL its sound; the slot gets the new clip from --in, scaled to
the preview's size and frame rate. Paths may be any machine's (scripts/drive/localmap.py): they are read
localized, and the new edl stores the new clip in the same story-home form as the cut's other shots.
Writes <out-dir>/edl.json and <out-dir>/preview.mp4.
"""
import argparse
import json
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'drive'))
from localmap import localize, localize_path, story_relpath, stories  # noqa: E402


def probe(p):
    out = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
                          'stream=width,height,r_frame_rate', '-of', 'json', p], capture_output=True, text=True, check=True)
    s = json.loads(out.stdout)['streams'][0]
    n, d = s['r_frame_rate'].split('/')
    return s['width'], s['height'], round(int(n) / int(d))


def shared_form(new, like):
    """The new clip's path written the way the cut's other paths are (the same story home), so the edl stays
    machine-neutral; falls back to the path as given."""
    story, rest = story_relpath(new)
    lstory, lrest = story_relpath(like)
    if not story or story != lstory:
        return new
    home = like[:len(like) - len(lrest)].rstrip('/') if lrest else like
    return f'{home}/{rest}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('edl'); ap.add_argument('out'); ap.add_argument('shot'); ap.add_argument('clip')
    ap.add_argument('--in', dest='inp', type=float, default=0.0); ap.add_argument('--id')
    ap.add_argument('--at', type=float, help="the shot's start (s), when the same clip is used more than once")
    ap.add_argument('--why', default=''); ap.add_argument('--round'); ap.add_argument('--heading'); ap.add_argument('--intro')
    a = ap.parse_args()

    raw = json.loads(pathlib.Path(localize_path(a.edl)).read_text())
    here = localize(raw)
    idx = [i for i, v in enumerate(raw['video']) if v.get('id') == a.shot and (a.at is None or abs(v['start'] - a.at) < 0.02)]
    if len(idx) != 1:
        sys.exit(f'shot {a.shot!r} found {len(idx)} times in {a.edl}' + (': pass --at <start>' if len(idx) > 1 else ''))
    i = idx[0]
    old = raw['video'][i]
    clip_here = localize_path(a.clip)
    if not pathlib.Path(clip_here).exists():
        sys.exit(f'no clip at {clip_here}')
    stored = shared_form(a.clip if a.clip.startswith('/mnt/d') else clip_here, old['file'])

    new = dict(old, file=stored, source=stored, id=a.id or pathlib.Path(a.clip).stem, looped=False, speed=1,
               why=a.why or f'swapped in for {a.shot}', swapped_from=a.shot)
    new['in'] = a.inp
    raw['video'][i] = new
    for k, v in (('round', a.round), ('heading', a.heading), ('intro', a.intro)):
        if v:
            raw[k] = v
    raw.pop('render', None)  # the old render no longer matches this cut
    out = pathlib.Path(localize_path(a.out))
    out.mkdir(parents=True, exist_ok=True)

    prev = here.get('preview') or str(pathlib.Path(localize_path(a.edl)).parent / 'preview.mp4')
    w, h, fps = probe(prev)
    s0, s1 = round(old['start'] * fps), round((old['start'] + old['dur']) * fps)
    fc = (f"[0:v]split=2[p0][p1];[p0]trim=start_frame=0:end_frame={s0},setpts=PTS-STARTPTS[a];"
          f"[1:v]trim=start={a.inp}:duration={old['dur']},setpts=PTS-STARTPTS,fps={fps},"
          f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},setsar=1,"
          f"trim=end_frame={s1 - s0}[b];"
          f"[p1]trim=start_frame={s1},setpts=PTS-STARTPTS[c];[a][b][c]concat=n=3:v=1:a=0[v]")
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', prev, '-i', clip_here, '-filter_complex', fc, '-map', '[v]',
           '-map', '0:a?', '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p',
           '-r', str(fps), '-c:a', 'copy', '-movflags', '+faststart', str(out / 'preview.mp4')]
    subprocess.run(cmd, check=True)
    n = lambda p: int(json.loads(subprocess.run(['ffprobe', '-v', 'error', '-count_packets', '-select_streams', 'v:0',
                     '-show_entries', 'stream=nb_read_packets', '-of', 'json', p], capture_output=True, text=True,
                     check=True).stdout)['streams'][0]['nb_read_packets'])
    if n(str(out / 'preview.mp4')) != n(prev):
        sys.exit(f'preview came out {n(str(out / "preview.mp4"))} frames, the old one is {n(prev)}: not written as done')
    (out / 'edl.json').write_text(json.dumps(raw, indent=1, ensure_ascii=False) + '\n')
    print(json.dumps({'edl': str(out / 'edl.json'), 'preview': str(out / 'preview.mp4'), 'slot': [old['start'], old['dur']],
                      'old': old['id'], 'new': new['id'], 'stored_as': stored}, indent=1))


if __name__ == '__main__':
    main()
