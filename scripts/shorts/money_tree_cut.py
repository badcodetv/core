#!/usr/bin/env python3
"""Magic Money Tree (BadCode Short #36): rough cut (2026-11-11).

    python3 scripts/shorts/money_tree_cut.py

9:16. 01 shakes the HOSPITALS tree, nothing falls → 02 close-up shrug, "We can't afford it." (lip-synced) →
03 shakes the BANKS tree, money pours → 04 deadpan to camera, "Different tree." (lip-synced) → logo.
Captions HOSPITALS / BANKS are hand-lettered (Ink Free) at the top, laid in here, never by Flow.
A1 = minister dub (Schedar, fitted per clip by scripts/lipsync/place-dub.py, dub/*.json), A2 = clip sound (Omni speech muted).
Writes <media>/cut/edl.json (timeline format), stems, overlay.mov and preview.mp4.
"""
# style-lint: story=short-magic-money-tree (this cut script belongs to one short)
import json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-magic-money-tree/scenes/magic-money-tree'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID, AUD = MEDIA / 'video', MEDIA / 'audio'
CUT = MEDIA / 'cut'; CUT.mkdir(parents=True, exist_ok=True)
LOGO = REPO / 'docs/brand/logo/badcode-lockup-reversed.svg'
LOGO_PNG = CUT / 'logo-lockup.png'
FONT = '/mnt/c/Windows/Fonts/Inkfree.ttf'
W, H, FPS = 1080, 1920, 24
SFX_LUFS = -32

# (beat, clip, in, dur, caption, dub-or-None, mute-ranges in clip time)
SHOTS = [('hospitals', 'mt-01-HO1-b.mp4', 0.0, 4.5, 'HOSPITALS', None, [(3.0, 4.5)]),
         ('afford', 'mt-02-CU1-a.mp4', 0.8, 2.2, None, AUD / 'dub/mt-02-dub.wav', [(0, 8)]),
         ('banks', 'mt-03-BK2-a.mp4', 0.0, 4.0, 'BANKS', None, []),
         ('button', 'mt-04-BT3-a.mp4', 1.6, 2.6, None, AUD / 'dub/mt-04-dub.wav', [(0, 8)])]
starts, t = [], 0.0
for s in SHOTS: starts.append(round(t, 3)); t += s[3]
TOTAL = round(t, 3)
T_LOGO = TOTAL - 0.9
SEE = {'hospitals': 'The minister shakes the HOSPITALS tree; nothing falls; he slumps.',
       'afford': 'Close-up, a little shrug: "We can\'t afford it."',
       'banks': 'He shakes the BANKS tree; money pours down.',
       'button': 'Deadpan, to camera: "Different tree."'}
TITLES = {'hospitals': 'A. The hospitals tree', 'afford': 'A2. "We can\'t afford it."', 'banks': 'B. The banks tree', 'button': 'C. "Different tree."'}
LINES = {'afford': "We can't afford it.", 'button': 'Different tree.'}


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']


def main():
    subprocess.run(['node', '-e', f"require('sharp')('{LOGO}',{{density:300}}).resize(560).png().toFile('{LOGO_PNG}')"], check=True, cwd=REPO)
    parts, world, dubs = [], [], []
    for i, (beat, clip, tin, d, cap, dub, mutes) in enumerate(SHOTS):
        out = CUT / f'v{i}-{beat}.mp4'
        ff('-ss', tin, '-t', d, '-i', VID / clip, '-an', '-vf',
           f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},scale=in_range=full:out_range=limited,format=yuv420p', *ENC, out)
        parts.append(out)
        mute = ''.join(f",volume=enable='between(t,{a - tin:.2f},{b - tin:.2f})':volume=0" for a, b in mutes)
        sp = CUT / f's{i}-{beat}.wav'
        ff('-ss', tin, '-t', d, '-i', VID / clip, '-vn', '-af', f'loudnorm=I={SFX_LUFS}:TP=-6{mute},afade=t=in:d=0.05,afade=t=out:st={d - 0.05}:d=0.05',
           '-ar', 48000, '-ac', 2, sp)
        world.append(sp)
    (CUT / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', CUT / 'list.txt', '-c', 'copy', CUT / 'picture-raw.mp4')

    caps = []
    for i, s in enumerate(SHOTS):
        if s[4]:
            caps.append(f"drawtext=fontfile='{FONT}':text='{s[4]}':fontsize=150:fontcolor=0x2b3440:box=1:boxcolor=0xEFEBE1@0.9:boxborderw=28:x=(w-text_w)/2:y=150:"
                        f"enable='between(t,{starts[i] + 0.15:.2f},{starts[i] + s[3]:.2f})'")
    capf = ','.join(caps)
    ff('-i', CUT / 'picture-raw.mp4', '-i', LOGO_PNG, '-filter_complex',
       f"[0]{capf}[c];[1]format=rgba[l];[c][l]overlay=(W-w)/2:H-h-220:enable='gte(t,{T_LOGO:.2f})',scale=in_range=full:out_range=limited,format=yuv420p[v]",
       '-map', '[v]', *ENC, CUT / 'picture.mp4')
    ff('-f', 'lavfi', '-i', f'color=c=black@0.0:s={W}x{H}:r={FPS}:d={TOTAL},format=rgba', '-i', LOGO_PNG, '-filter_complex',
       f"[0]{capf}[c];[1]format=rgba[l];[c][l]overlay=(W-w)/2:H-h-220:format=auto:enable='gte(t,{T_LOGO:.2f})'[o]",
       '-map', '[o]', '-t', TOTAL, '-c:v', 'prores_ks', '-profile:v', '4444', '-pix_fmt', 'yuva444p10le', '-alpha_bits', '16', CUT / 'overlay.mov')

    (CUT / 'slist.txt').write_text(''.join(f"file '{p.name}'\n" for p in world))
    wst = CUT / 'sfx-world.wav'
    ff('-f', 'concat', '-safe', '0', '-i', CUT / 'slist.txt', '-af', f'apad=whole_dur={TOTAL}', '-ar', 48000, '-ac', 2, wst)
    vox = CUT / 'vox-minister.wav'
    ins, fc = [], []
    for i, s in enumerate(SHOTS):
        if s[5]:
            k = len(ins) // 2
            ins += ['-i', s[5]]
            fc.append(f'[{k}]atrim={s[2]}:{s[2] + s[3]},asetpts=PTS-STARTPTS,adelay=delays={int(starts[i] * 1000)}:all=1[d{k}]')
    n = len(ins) // 2
    ff(*ins, '-filter_complex', ';'.join(fc) + ';' + ''.join(f'[d{k}]' for k in range(n)) + f'amix=inputs={n}:normalize=0,apad=whole_dur={TOTAL}',
       '-ar', 48000, '-ac', 2, vox)
    ff('-i', CUT / 'picture.mp4', '-i', vox, '-i', wst, '-filter_complex', '[1:a][2:a]amix=inputs=2:normalize=0[a]',
       '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', TOTAL, CUT / 'preview.mp4')

    fit = json.loads((SCENE / 'dub/fit.json').read_text()) if (SCENE / 'dub/fit.json').exists() else {}
    notes = SCENE / 'cut-notes.json'
    rnd = json.loads(notes.read_text()).get('round', 1) if notes.exists() else 1
    beats = []
    for i, s in enumerate(SHOTS):
        ln = []
        if s[0] in LINES:
            on, off = fit.get(s[0], [s[2], s[2] + s[3]])
            ln.append({'i': 0, 'who': 'minister', 'name': 'Minister', 't': round(starts[i] + on - s[2], 2), 'dur': round(off - on, 2), 'text': LINES[s[0]], 'by': 'claude'})
        beats.append({'id': s[0], 'title': TITLES[s[0]], 'start': starts[i], 'dur': s[3], 'see': SEE[s[0]], 'lines': ln})
    edl = {'sequence': f'shorts-36-magic-money-tree-r{rnd}', 'title': 'Magic Money Tree Timeline',
           'heading': f'BadCode Shorts ▲ Magic Money Tree, rough cut {rnd}',
           'intro': 'Four shots in the gouache look you picked, the minister lip-synced (Schedar), HOSPITALS / BANKS captions and the logo. Note anything: a beat, a shot, a line, a sound, or a single frame.',
           'fps': FPS, 'total': TOTAL, 'beats': beats,
           'video': [{'file': str(VID / s[1]), 'in': s[2], 'start': starts[i], 'dur': s[3], 'beat': s[0], 'source': str(VID / s[1]), 'looped': False}
                     for i, s in enumerate(SHOTS)],
           'audio': [{'track': 'A1', 'name': 'vox-minister', 'file': str(vox)}, {'track': 'A2', 'name': 'sfx-world', 'file': str(wst)}],
           'events': [{'stem': 'vox-minister', 't': b['lines'][0]['t'], 'dur': b['lines'][0]['dur'], 'what': b['lines'][0]['text'] + ' (lip-synced)', 'src': str(SHOTS[i][5])}
                      for i, b in enumerate(beats) if b['lines']]
                     + [{'stem': 'sfx-world', 't': starts[i], 'dur': s[3], 'what': f"{s[0]}: clip's own sound" + (' (speech muted)' if s[6] else ''), 'src': str(VID / s[1])} for i, s in enumerate(SHOTS)],
           'flags': ['Picks made by Claude at Jack\'s word ("you pick everything for this one"); look from his HO1-b.', 'No music yet.']}
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': TOTAL, 'starts': starts, 'preview': str(CUT / 'preview.mp4')}))


if __name__ == '__main__':
    main()
