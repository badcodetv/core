"""Brutal + mint (12 Nov; copied from the 1F5 finish.py). After record-par.sh (frames-beads/, bead stills from bead-media.json):
voice.wav (the kept lines + the mint turn at their starts on the hologram clock), edit.json, the 24 fps picture mp4, picture+voice mp4,
a contact sheet at every line start, line end and the mint turn's beats, recipe cards. Never writes into render-1f5-24."""
import json, subprocess, pathlib
H = pathlib.Path(__file__).parent; ROOT = H.parents[1]
R = pathlib.Path('/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/render-1f5-brutal-mint-24'); FR = 'frames-beads'
E = json.load(open(H / 'edit.json')); TD = E['marks']['TD']
L = {l['id']: l for l in json.load(open(H / 'lines.json'))}
(R / 'edit.json').write_text(json.dumps(E, indent=1, ensure_ascii=False))
ids = list(E['clips']); ins = sum([['-i', L[k]['file']] for k in ids], [])
fl = ';'.join(f"[{i}]aresample=48000,adelay={int(round(E['clips'][k]['start']*1000))}:all=1[a{i}]" for i, k in enumerate(ids))
fl += ';' + ''.join(f'[a{i}]' for i in range(len(ids))) + f'amix=inputs={len(ids)}:normalize=0,apad,atrim=0:{TD:.3f}[o]'
vw = R / 'hologram-bm-24fps-voice.wav'
subprocess.run(['ffmpeg', '-v', 'error', '-y', *ins, '-filter_complex', fl, '-map', '[o]', '-ac', '2', '-ar', '48000', str(vw)], check=True)
pic = R / 'hologram-bm-beads-24fps-picture.mp4'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', '24', '-i', str(R / FR / '%05d.jpg'), '-c:v', 'libx264', '-crf', '14', '-preset', 'slow', '-pix_fmt', 'yuv420p', str(pic)], check=True)
both = R / 'hologram-bm-24fps.mp4'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(pic), '-i', str(vw), '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k', '-shortest', str(both)], check=True)
# contact sheet: every line's first and last word, and the mint turn's beats
m = E['marks']; st = E['clips']
K = [(1.0, 'opening: outlines')]
for k in ids:
    ws = L[k]['words']; s = st[k]['start']
    K += [(s + ws[0][1] + .1, f'{k} starts - {ws[0][0]}'), (s + ws[-1][2] - .1, f'{k} ends - {ws[-1][0]}')]
K += [(m['mint_spark'] + .5, 'MINT - spark in the molecule'), (m['signal_stops'] + .2, 'signal stops at INDIVIDUAL'), (m['slot_flickers'] + .5, 'WHERE - slot flickers'),
      (m['slot_warms'] + .7, 'slot warms (no label)'), (m['light_lands'], 'light lands'), (m['cloud_blooms'] + .8, 'multiverse - bloom'), (m['storyverse_flash'] + .1, 'STORYVERSE - flash'),
      (m['inside_river'], 'inside the river'), (m['arrive_square_on'] + .2, 'square-on - the stop'), (m['arc_draws'] + 1.5, 'arc draws'), (m['screen_off'] + .5, 'screen off')]
K.sort()
tiles = []
for i, (t, lab) in enumerate(K):
    f = R / FR / f'{min(round(t * 24), int(TD * 24) - 1):05d}.jpg'; o = R / f'_c{i:02d}.jpg'
    lab = lab.replace(':', ' ').replace("'", '').replace(',', '')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(f), '-vf', f"scale=480:-1,drawtext=text='{t:.2f}s  {lab}':fontsize=18:fontcolor=white:box=1:boxcolor=black@0.6:x=8:y=8", str(o)], check=True); tiles.append(o)
cs = R / 'contact-bm.jpg'
subprocess.run(['ffmpeg', '-v', 'error', '-y', *sum([['-i', str(t)] for t in tiles], []), '-filter_complex', ''.join(f'[{i}]' for i in range(len(tiles))) + f'xstack=inputs={len(tiles)}:layout=' + '|'.join(f'{(i%6)*480}_{(i//6)*270}' for i in range(len(tiles))), str(cs)], check=True)
for t in tiles: t.unlink()
why = ('GPOM scene A hologram, brutal + mint (Kai, 12 Nov: the 1F5 presentation "really good, just really long", its consciousness turn cringe; '
       'turn = draft A1, the taste of mint; spec design/2026-11-12-gpom-consciousness/README.md part B). Only the kept lines + the mint turn, every beat re-timed to its word.')
P = ['python3', str(ROOT / 'scripts/provenance/prov.py'), 'card']
B = 'design/2026-11-12-gpom-hologram-brutal-mint'
common = ['--why', why, '--input', f'page={B}/index.html', '--input', f'builder={B}/make.py', '--input', f'voice={B}/lines.json', '--input', f'stack={B}/stack.js',
          '--setting', 'fps=24', '--setting', 'size=1920x1080', '--setting', f'timing={R / "edit.json"}', '--setting', f'bead_media={B}/bead-media.json',
          '--input', 'derek=/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/bead-stills/derek-a.jpg', '--input', 'sandra=/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/bead-stills/sandra-a.jpg',
          '--input', 'wedding=/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/bead-stills/wedding-a.jpg']
subprocess.run(P + [str(pic), '--kind', 'video', '--engine', 'three.js', '--tool', f'{B}/record-par.sh + record.mjs (headless Chrome, window.hologram.frameAt) + ffmpeg x264, 24 fps', *common], check=True)
subprocess.run(P + [str(vw), '--kind', 'cut', '--engine', 'ffmpeg', '--tool', f'{B}/finish.py (ffmpeg adelay+amix)', '--parent', str(pathlib.Path(L['m1']['file']).resolve()), *common], check=True)
subprocess.run(P + [str(both), '--kind', 'cut', '--engine', 'ffmpeg', '--tool', f'{B}/finish.py (ffmpeg mux)', '--parent', str(pic), *common], check=True)
subprocess.run(P + [str(cs), '--kind', 'other', '--engine', 'ffmpeg', '--tool', f'{B}/finish.py (ffmpeg xstack)', '--parent', str(pic), *common], check=True)
print('TD', TD, 'voice', vw, 'pic', pic, 'sheet', cs)
