#!/usr/bin/env python3
"""GPOM scene A round 28 (Kai, 19 Nov: build the lip-sync picks into the film): the row (beats 6-7) from Kai's final
lip-sync picks (feedback/lipsync-picks-2026-11-18-r3.json). Each line is its picked Omni clip with its picked take placed
WHOLE exactly as on the picks page (one start, one tempo 0.97-1.15, never chopped; the picture never sped). Lines follow each
other like d26a (Kai's pick, 12 Nov): 0.10 s between one line's last sound and the next one's first.

Writes /mnt/d/.../cut3/row-r28/row-spec.json (the row-r24 format) and one placed voice wav per line (clip time 0 = file time 0).
cut3.py A --tag d28 reads it (row_r28)."""
import json, os, subprocess, sys
REPO = '/home/kai/projects/badcode/badcode'
PICKS = f'{REPO}/docs/stories/gitpush-origin-master/scenes/second-half-a-killbots/feedback/lipsync-picks-2026-11-18-r3.json'
LS = '/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/lipsync-2026-11-18/A'
OUT = '/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/cut3/row-r28'
ORDER = [('6-0', 'Sandra', 'vox-sandra', "Derek. You've left the seat up. Again.", '6'),
         ('7d-0', 'Derek', 'vox-derek', "I'm really sorry, love.", '7'),
         ('7-0', 'Sandra', 'vox-sandra', "Five years underground, and you still can't put a seat down.", '7'),
         ('7d-1', 'Derek', 'vox-derek', 'But the world ended, Sandra!', '7'),
         ('7-2', 'Sandra', 'vox-sandra', "Yeah, the world ended. Doesn't mean you get to stop having manners.", '7')]
FPS, GAP, LEAD, TAIL = 24, 0.10, 0.06, 0.4
fr = lambda t: round(t * FPS) / FPS
dur = lambda p: float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                                     capture_output=True, text=True).stdout)


def main():
    os.makedirs(OUT, exist_ok=True)
    picks = json.load(open(PICKS))['picks']
    shots, voices, T = [], [], 0.0
    for n, (ln, who, stem, text, beat) in enumerate(ORDER, 1):
        p = picks[ln]
        clip, take = f'{LS}/video/{p["clip"]}', f'{LS}/voices/{p["take"]}'
        clen = dur(clip)
        at = max(0.0, p['at'])  # the page's render clamps a slightly early start to 0 (render_pair): same here
        vlen = (p['to'] - p['frm']) / p['tempo']
        s, e = at + 0.03, at + vlen - 0.05  # first and last sound, clip time
        wav = f'{OUT}/r28-line{n}-{who.lower()}-{ln}.wav'
        d = int(round(at * 1000))
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', take, '-af',
                        f'atrim={p["frm"]}:{p["to"]},asetpts=PTS-STARTPTS,atempo={p["tempo"]},adelay={d}|{d},apad',
                        '-t', str(clen), '-ar', '48000', wav], check=True)
        subprocess.run([sys.executable, f'{REPO}/scripts/provenance/prov.py', 'card', wav, '--kind', 'voice', '--engine', 'ffmpeg',
                        '--tool', 'row-r28/build_row.py', '--parent', take, '--parent', clip,
                        '--why', f'scene A d28 row line {n} ({ln}): Kai\'s lip-sync pick {p["option"]} ({p["round"]}), whole take at '
                                 f'{at} s x{p["tempo"]}'], check=True, capture_output=True)
        i0 = fr(max(0.0, s - (0.08 if n == 1 else LEAD)))
        last = n == len(ORDER)
        out = fr(min(clen - 1 / FPS, e + (TAIL if last else GAP - LEAD)))
        shots.append(dict(n=n, who=who, line=ln, file=clip, **{'in': i0}, out=out, offset=round(T, 4), beat=beat,
                          dur=round(out - i0, 4), clip_len=clen))
        voices.append(dict(line=n, who=who, stem=stem, file=wav, **{'in': i0}, dur=round(out - i0, 4), offset=round(T, 4),
                           text=text, pick=dict(p), speech=[round(s, 3), round(e, 3)]))
        T += out - i0
    spec = dict(about='GPOM scene A round 28 (Kai 19 Nov): the row from Kai\'s final lip-sync picks (r3 picks page). Each voice is '
                      'its whole picked take placed on its picked clip exactly as on the picks page (file time = clip time); '
                      'lines 0.10 s apart. Built by scripts/gpom/second-half-video/row-r28/build_row.py.',
                fps=FPS, total=round(T, 4), beat7_start=shots[1]['offset'], gap_between_lines=GAP, tail=TAIL,
                chain=['aecho=0.8:0.5:35|60:0.22|0.12'], lufs=-16,
                room_tone=dict(file='/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/audio/sfx/fs767306-room-tiled-public-bathroom.mp3',
                               src_in=10, rms=-42),
                shots=shots, voices=voices)
    json.dump(spec, open(f'{OUT}/row-spec.json', 'w'), indent=1)
    for sh in shots:
        print(sh['n'], sh['line'], 'clip', round(sh['in'], 3), '->', sh['out'], 'at row', round(sh['offset'], 2), 'of', round(sh['clip_len'], 2))
    print('total', round(T, 2))


main()
