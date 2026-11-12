#!/usr/bin/env python3
"""No Master Recording (BadCode Short #52): rough cut (2026-11-12).

    python3 scripts/shorts/no_master_cut.py

9:16, flash-snapshot look (Jack's picks AR1-a, WA2-b, EN1-a-fix-b). 01 two mates hum different tunes in a kebab shop →
02 knee-deep in a studio flooded with seven-inches → 03 the BadCode engineer looks up: "Which one?" → 04 mate 1: "We don't
fucking know, there are a thousand versions." mate 2: "Pick that one..." (clip muted, AI Studio dub fitted to its own speech
times) → black → the stacked logo and name on black, the engineer: "Fuck it." (Jack: the ending "all quite quickly").
A1 = voices (dub), A2 = clip sound (01 humming, 03 room; 02 and 04 muted: 02's own audio said "You", 04 is dubbed).
Writes <media>/cut/edl.json (timeline format), stems and preview.mp4.
"""
# style-lint: story=short-no-master-recording (this cut script belongs to one short)
import json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-no-master-recording/scenes/no-master-recording'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, TAKES = MEDIA / 'video', MEDIA / 'audio/takes'
CUT = MEDIA / 'cut'; CUT.mkdir(parents=True, exist_ok=True)
LOGO = REPO / 'docs/brand/logo/badcode-stacked-reversed-2400.png'
W, H, FPS = 1080, 1920, 24

# (beat, clip or None for black/logo, in, dur, clip-sound LUFS or None to mute)
SHOTS = [('argue', 'nm-01-AR1-a.mp4', 0.0, 3.6, -24),
         ('flood', 'nm-02-WA2-b.mp4', 0.3, 3.0, None),
         ('which', 'nm-03-EN1-a-fix-b.mp4', 0.5, 2.0, -34),
         ('versions', 'nm-04-WA2-b.mp4', 0.6, 4.9, None),
         ('black', None, 0, 0.35, None),
         ('logo', None, 0, 1.5, None)]
starts, t = [], 0.0
for s in SHOTS: starts.append(round(t, 3)); t += s[3]
TOTAL = round(t, 3)
S = dict(zip([s[0] for s in SHOTS], starts))
# (beat, take, at = seconds into the shot where the take file starts, tempo, who, text)
# 04: the clip's own speech runs 0.84-3.57 and 4.64-5.17 (clip time); takes fitted at x0.98 / x1.07 (voices/README in picks.md).
DUBS = [('which', 'eng-which-b.wav', 0.0, 1.0, 'engineer', 'Which one?'),
        ('versions', 'mate1-fast-e.wav', 0.84 - 0.6 + 0.03 - 0.25, 1.0, 'mate1', "We don't fucking know, there are a thousand versions."),
        ('versions', 'mate2-fast-c.wav', 4.64 - 0.6 + 0.03 - 0.26 / 1.07, 1.07, 'mate2', 'Pick that one...'),
        ('logo', 'eng-fuckit-b.wav', 0.12, 1.0, 'engineer', 'Fuck it.')]
NAMES = {'engineer': 'BadCode engineer', 'mate1': 'Mate 1 (red shirt)', 'mate2': 'Mate 2 (grey hoodie)'}
SEE = {'argue': 'Kebab shop, flash snapshot: the two mates hum different tunes at each other, both certain.',
       'flood': 'They have broken into the studio: knee-deep in seven-inch singles, FINAL / FINAL FINAL sleeves.',
       'which': 'The BadCode engineer at the desk looks up: "Which one?"',
       'versions': 'Mate 1: "We don\'t fucking know, there are a thousand versions." Mate 2 points: "Pick that one..."',
       'black': 'Cut to black.',
       'logo': 'The BadCode logo and name on black. The engineer: "Fuck it."'}
TITLES = {'argue': 'A. Two mates argue', 'flood': 'B. The flood of finals', 'which': 'C. "Which one?"',
          'versions': 'C2. "A thousand versions" / "Pick that one..."', 'black': 'D. Black', 'logo': 'D2. Logo, "Fuck it."'}


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']


def main():
    parts, world = [], []
    for i, (beat, clip, tin, d, lufs) in enumerate(SHOTS):
        out = CUT / f'v{i}-{beat}.mp4'
        if clip:
            ff('-ss', tin, '-t', d, '-i', VID / clip, '-an', '-vf',
               f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},scale=in_range=full:out_range=limited,format=yuv420p', *ENC, out)
        elif beat == 'logo':
            ff('-f', 'lavfi', '-i', f'color=c=black:s={W}x{H}:r={FPS}:d={d}', '-i', LOGO, '-filter_complex',
               f'[1]scale=640:-1[l];[0][l]overlay=(W-w)/2:(H-h)/2,format=yuv420p', '-t', d, *ENC, out)
        else:
            ff('-f', 'lavfi', '-i', f'color=c=black:s={W}x{H}:r={FPS}:d={d}', '-vf', 'format=yuv420p', '-t', d, *ENC, out)
        parts.append(out)
        sp = CUT / f's{i}-{beat}.wav'
        if clip and lufs is not None:
            ff('-ss', tin, '-t', d, '-i', VID / clip, '-vn', '-af', f'loudnorm=I={lufs}:TP=-6,afade=t=in:d=0.05,afade=t=out:st={d - 0.05}:d=0.05',
               '-ar', 48000, '-ac', 2, sp)
        else:
            ff('-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-t', d, sp)
        world.append(sp)
    (CUT / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', CUT / 'list.txt', '-c', 'copy', CUT / 'picture.mp4')
    (CUT / 'slist.txt').write_text(''.join(f"file '{p.name}'\n" for p in world))
    wst = CUT / 'sfx-world.wav'
    ff('-f', 'concat', '-safe', '0', '-i', CUT / 'slist.txt', '-af', f'apad=whole_dur={TOTAL}', '-t', TOTAL, '-ar', 48000, '-ac', 2, wst)

    vox = CUT / 'vox.wav'
    ins, fc, events = [], [], []
    for k, (beat, take, at, tempo, who, text) in enumerate(DUBS):
        t0 = S[beat] + at
        ins += ['-i', TAKES / take]
        fc.append(f'[{k}]aresample=48000,atempo={tempo},loudnorm=I=-18:TP=-2,adelay=delays={int(t0 * 1000)}:all=1[d{k}]')
        dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', TAKES / take],
                                   capture_output=True, text=True).stdout) / tempo
        events.append({'stem': 'vox', 't': round(t0, 2), 'dur': round(dur, 2), 'what': f'{NAMES[who]}: {text}', 'src': str(TAKES / take),
                       'beat': beat, 'who': who, 'text': text})
    n = len(DUBS)
    ff(*ins, '-filter_complex', ';'.join(fc) + ';' + ''.join(f'[d{k}]' for k in range(n)) + f'amix=inputs={n}:normalize=0,apad=whole_dur={TOTAL}',
       '-t', TOTAL, '-ar', 48000, '-ac', 2, vox)
    ff('-i', CUT / 'picture.mp4', '-i', vox, '-i', wst, '-filter_complex', '[1:a][2:a]amix=inputs=2:normalize=0[a]',
       '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', TOTAL, CUT / 'preview.mp4')

    notes = SCENE / 'cut-notes.json'
    rnd = json.loads(notes.read_text()).get('round', 1) if notes.exists() else 1
    beats = []
    for i, s in enumerate(SHOTS):
        ln = [{'i': j, 'who': e['who'], 'name': NAMES[e['who']], 't': e['t'], 'dur': e['dur'], 'text': e['text'], 'by': 'jack'}
              for j, e in enumerate(x for x in events if x['beat'] == s[0])]
        beats.append({'id': s[0], 'title': TITLES[s[0]], 'start': starts[i], 'dur': s[3], 'see': SEE[s[0]], 'lines': ln})
    edl = {'sequence': f'short-no-master-recording-1-no-master-recording-r{rnd}', 'title': 'No Master Recording Timeline',
           'heading': f'BadCode Shorts ▲ No Master Recording, rough cut {rnd}',
           'intro': 'Your picks in the flash look, your lines, the ending quick. Voices are my picks (AI Studio), unheard by you. Note anything: a beat, a shot, a line, a sound, or a single frame.',
           'fps': FPS, 'total': TOTAL, 'beats': beats,
           'video': [{'file': str(VID / s[1]) if s[1] else str(CUT / f'v{i}-{s[0]}.mp4'), 'in': s[2], 'start': starts[i], 'dur': s[3], 'beat': s[0],
                      'source': str(VID / s[1]) if s[1] else str(CUT / f'v{i}-{s[0]}.mp4'), 'looped': False} for i, s in enumerate(SHOTS)],
           'audio': [{'track': 'A1', 'name': 'vox', 'file': str(vox)}, {'track': 'A2', 'name': 'sfx-world', 'file': str(wst)}],
           'events': [{k: e[k] for k in ('stem', 't', 'dur', 'what', 'src')} for e in events]
                     + [{'stem': 'sfx-world', 't': starts[i], 'dur': s[3], 'what': f"{s[0]}: clip's own sound" + ('' if s[4] is not None else ' (muted)'),
                         'src': str(VID / s[1])} for i, s in enumerate(SHOTS) if s[1]],
           'flags': ['Voices picked by Claude (Iapetus engineer, Fenrir mate 1, Zubenelgenubi mate 2), unheard by Jack.',
                     'The mates are small in the wide, so the dub is fitted to the clip\'s own speech times, not a measured mouth.',
                     'Shot 2 is silent (its own audio said "You"). No music yet.']}
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': TOTAL, 'starts': starts, 'preview': str(CUT / 'preview.mp4')}))


if __name__ == '__main__':
    main()
