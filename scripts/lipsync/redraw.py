#!/usr/bin/env python3
"""Redraw talking shots' mouths to the voices already in a cut, with LatentSync 1.6 (local GPU).

The lip-sync-dub skill's "redraw" lane. Shots are found BY NAME in a cut's edl, so nobody types file paths:
a talking shot is a V1 clip whose file is named `...lip-<id>...` (GPOM: 6-0, 7d-0, 7-0, 7d-1, 7-2), and its
speaker is the voice stem whose event mentions that id (so Sandra talking over Derek's shot is left out and his
mouth stays shut).

    redraw.py list  <edl.json>                         # the talking shots and who speaks in each
    redraw.py prep  <edl.json> <dir> [ids...]          # <id>-in.mp4 (picture as cut, muted) + <id>-voice.wav
    redraw.py run   <dir> [ids...]                     # LatentSync on each (calls latentsync-row.sh); needs the
                                                       #   allow rule in .claude/settings.json or a person's `!`
    redraw.py post  <edl.json> <dir> [ids...]          # 25 fps back to 24, exact length -> <id>-ls24.mp4, plus
                                                       #   <dir>/row-before.mp4 and row-after.mp4 with the cut's mix

Install first: scripts/lipsync/latentsync-setup.sh check|install. Card outputs with prov.py card afterwards.
Built 2026-11-06 on GPOM scene A round 19 (Kai at3436).
"""
import json, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
ID = re.compile(r'lip-([0-9]+[a-z]?-[0-9]+)')


def sh(*a):
    subprocess.run([str(x) for x in a], check=True)


def shots(edl):
    e = json.loads(pathlib.Path(edl).read_text())
    stems = {a['name']: a['file'] for a in e['audio']}
    out = []
    for v in e['video']:
        m = ID.search(pathlib.Path(v['file']).name)
        if not m:
            continue
        sid = m.group(1)
        who = [ev['stem'] for ev in e['events'] if ev['stem'].startswith('vox') and re.search(rf'\b{re.escape(sid)}\b', ev.get('what', ''))]
        if not who:  # no event names the shot: the voice that overlaps it most
            ov = lambda ev: min(ev['t'] + ev['dur'], v['start'] + v['dur']) - max(ev['t'], v['start'])
            vox = [ev for ev in e['events'] if ev['stem'].startswith('vox') and ov(ev) > 0]
            if not vox:
                raise SystemExit(f'{sid}: no voice over this shot')
            who = [max(vox, key=ov)['stem']]
        out.append(dict(id=sid, file=v['file'], i=v['in'], d=v['dur'], t=v['start'], stem=who[0], wav=stems[who[0]]))
    return e, out


def pick(all_, ids):
    return [s for s in all_ if not ids or s['id'] in ids]


def main():
    cmd, *a = sys.argv[1:] or ['-h']
    if cmd == 'list':
        for s in shots(a[0])[1]:
            print(f"{s['id']:6} {s['stem']:12} at {s['t']:.2f}s for {s['d']:.2f}s  {pathlib.Path(s['file']).name}")
    elif cmd == 'prep':
        _, ss = shots(a[0]); d = pathlib.Path(a[1]); d.mkdir(parents=True, exist_ok=True)
        for s in pick(ss, a[2:]):
            sh('ffmpeg', '-v', 'error', '-y', '-ss', s['i'], '-i', s['file'], '-t', s['d'], '-an',
               '-c:v', 'libx264', '-crf', '14', '-pix_fmt', 'yuv420p', '-r', 24, d / f"{s['id']}-in.mp4")
            sh('ffmpeg', '-v', 'error', '-y', '-ss', s['t'], '-i', s['wav'], '-t', s['d'], '-ac', 1, '-ar', 16000, d / f"{s['id']}-voice.wav")
            print('prepped', s['id'], s['stem'])
    elif cmd == 'run':
        d = pathlib.Path(a[0]); ids = a[1:] or sorted(p.name[:-7] for p in d.glob('*-in.mp4'))
        sh('bash', ROOT / 'scripts/lipsync/latentsync-row.sh', d, *ids)
    elif cmd == 'post':
        e, ss = shots(a[0]); d = pathlib.Path(a[1]); ss = pick(ss, a[2:])
        for s in ss:
            sh('ffmpeg', '-v', 'error', '-y', '-i', d / f"{s['id']}-ls.mp4", '-an', '-vf', 'fps=24', '-t', s['d'],
               '-c:v', 'libx264', '-crf', '14', '-pix_fmt', 'yuv420p', d / f"{s['id']}-ls24.mp4")
        t0, t1 = ss[0]['t'], ss[-1]['t'] + ss[-1]['d']
        for tag, suf in (('before', '-in.mp4'), ('after', '-ls24.mp4')):
            lst = d / f'row-{tag}.txt'
            lst.write_text(''.join(f"file '{d / (s['id'] + suf)}'\n" for s in ss))
            sh('ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', 0, '-i', lst, '-ss', t0, '-t', t1 - t0, '-i', e['mix'],
               '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-shortest',
               d / f'row-{tag}.mp4')
        print('wrote', d / 'row-before.mp4', 'and', d / 'row-after.mp4')
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
