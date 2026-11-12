"""1F5 scissors (12 Nov), copied from the 1F5 finish.py. After record-par.sh (frames-beads/, bead stills from
bead-media-1f5-scissors.json): edit.json, voice.wav (the kept lines at their starts), the 24 fps picture mp4, a muxed
preview, the contact sheet (every kept line and every join), and recipe cards.

    python3 trim.py && python3 make.py
    python3 -m http.server 8751 --bind 127.0.0.1   # in this folder
    bash record-par.sh http://127.0.0.1:8751/index.html <R> frames-beads 4 --media bead-media-1f5-scissors.json
    python3 finish.py
"""
import json, subprocess, pathlib
H = pathlib.Path(__file__).parent; ROOT = H.parents[1]; REL = 'design/2026-11-12-gpom-hologram-1f5-scissors'
R = pathlib.Path('/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/render-1f5-scissors-24'); FR = 'frames-beads'
E = json.load(open(H / 'edit-1f5-scissors.json')); TD = E['marks']['TD']
L = {l['id']: l for l in json.load(open(H / 'lines-1f5-scissors.json'))}
(R / 'edit.json').write_text(json.dumps(E, indent=1, ensure_ascii=False))
# voice: every kept clip placed at its start on the hologram clock (48 kHz stereo, TD long)
ids = list(E['clips']); ins = sum([['-i', L[k]['file']] for k in ids], [])
fl = ';'.join(f"[{i}]aresample=48000,adelay={int(round(E['clips'][k]['start'] * 1000))}:all=1[a{i}]" for i, k in enumerate(ids))
fl += ';' + ''.join(f'[a{i}]' for i in range(len(ids))) + f'amix=inputs={len(ids)}:normalize=0,apad,atrim=0:{TD:.3f}[o]'
vw = R / 'hologram-1f5-scissors-24fps-voice.wav'
subprocess.run(['ffmpeg', '-v', 'error', '-y', *ins, '-filter_complex', fl, '-map', '[o]', '-ac', '2', '-ar', '48000', str(vw)], check=True)
pic = R / 'hologram-1f5-scissors-beads-24fps-picture.mp4'
if not pic.exists():
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', '24', '-i', str(R / FR / '%05d.jpg'), '-c:v', 'libx264', '-crf', '14', '-preset', 'slow', '-pix_fmt', 'yuv420p', str(pic)], check=True)
both = R / 'hologram-1f5-scissors-24fps.mp4'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(pic), '-i', str(vw), '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k', '-shortest', str(both)], check=True)
# contact sheet: the moments that must land (each kept line's first word, every join where words were cut, the visuals)
m = E['marks']; st = E['clips']
def at(cid, word, d=0, n=0):
    return st[cid]['start'] + [x[1] for x in L[cid]['words'] if x[0].lower().startswith(word)][n] + d
SK = E['stack']
K = [(.8, 'opening - outlines, no voice'), (at('s01', 'societ', .3), 's01 JOIN - Society (opener cut)'), *[(t + .45, n.lower() + ' lands') for n, t in zip(SK['labels'][1:5], SK['lay'][1:5])],
     (SK['quarks'] + .55, 'quarks - standard model'), (SK['lay'][5] + .45, 'mathematics lands'), (at('s02', 'every', .3), 's02 every bit of it'),
     (SK['missing'] + .5, 'something missing - empty slot'), (st['s02']['start'] + st['s02']['dur'] + .2, 'slot held empty (s03 cut)'), (m['slot_warms'] + .5, 'slot warms - no label'),
     (m['light_leaves'] + 1.3, 'light falls'), (at('f01', 'derek', .1), 'f01 JOIN - Derek (thesis cut)'), (m['toast'] + .3, 'toast - bead 1'), (m['sorry'] + .3, 'sorry - bead 2'),
     (m['married'] + .3, 'married - bead 3'), (at('f03', 'we', .3), 'f03 we dont know - glow'), (m['label_consciousness'] + 1.0, 'machines - CONSCIOUSNESS'),
     (st['f03']['start'] + st['f03']['dur'] - .05, 'f03 END (qualia cut)'), (m['to_river'] + .1, 'JOIN - beads to river (f04 f04b cut)'), (m['to_river'] + 1.5, 'all of you - river'),
     (at('f05', 'each', .2), 'each of you - inside'), (at('f05', "it's", .2, 2), 'f05 pause 1 closed - storyverse'), (at('f05', 'and', .2, 1), 'f05 pause 2 closed - only one'),
     (m['leave_river'] + 1.2, 'leaving the river'), (m['arrive_square_on'] + .2, 'square-on - the stop'), (at('f06', 'no', .3, 1), 'f06 no new training data'),
     (m['rise'] + 1.6, 'time machine - rising'), (m['arc_draws'] + 1.2, 'it just needs - arc'), (m['arc_draws'] + 3.0, 'arc drawn'), (m['screen_off'] + .5, 'screen off')]
tiles = []
nf = len(list((R / FR).glob('*.jpg')))
for i, (t, lab) in enumerate(K):
    f = R / FR / f'{min(nf - 1, round(t * 24)):05d}.jpg'; o = R / f'_c{i:02d}.jpg'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(f), '-vf', f"scale=480:-1,drawtext=text='{t:.2f}s  {lab.replace(':', ' -')}':fontsize=18:fontcolor=white:box=1:boxcolor=black@0.6:x=8:y=8", str(o)], check=True); tiles.append(o)
cs = R / 'contact-1f5-scissors-beads.jpg'
subprocess.run(['ffmpeg', '-v', 'error', '-y', *sum([['-i', str(t)] for t in tiles], []), '-filter_complex', ''.join(f'[{i}]' for i in range(len(tiles))) + f'xstack=inputs={len(tiles)}:layout=' + '|'.join(f'{(i%4)*480}_{(i//4)*270}' for i in range(len(tiles))), str(cs)], check=True)
for t in tiles: t.unlink()
# recipe cards
why = ('hologram 1F5 SCISSORS (12 Nov, option B scissors-only, design/2026-11-12-gpom-consciousness/README.md): the 1F5 presentation made shorter with '
       'no new voice. s03, f04, f04b cut; s01 from "Society\'s"; f01 from "Derek"; f03 to "machines."; f05 pauses closed. The slot warms unlabelled, '
       'CONSCIOUSNESS fades up unspoken under f03; the cloud is off. 1F5 itself is kept whole.')
P = ['python3', str(ROOT / 'scripts/provenance/prov.py'), 'card']
common = ['--why', why, '--input', f'page={REL}/index.html', '--input', f'builder={REL}/make.py', '--input', f'voice={REL}/lines-1f5-scissors.json',
          '--input', f'trim={REL}/trim.py', '--input', f'stack={REL}/stack.js', '--setting', 'fps=24', '--setting', 'size=1920x1080', '--setting', f'timing={R / "edit.json"}']
media = ['--setting', f'bead_media={REL}/bead-media-1f5-scissors.json', *sum([['--input', f'{k}=' + str((H / v['src']).resolve())] for k, v in json.load(open(H / 'bead-media-1f5-scissors.json')).items()], [])]
subprocess.run(P + [str(pic), '--kind', 'video', '--engine', 'three.js', '--tool', f'{REL}/record-par.sh + record.mjs (headless Chrome, window.hologram.frameAt) + ffmpeg x264, 24 fps', *common, *media], check=True)
subprocess.run(P + [str(vw), '--kind', 'cut', '--engine', 'ffmpeg', '--tool', f'{REL}/finish.py (ffmpeg adelay+amix)', '--parent', str(L['s01']['file']), *common], check=True)
subprocess.run(P + [str(both), '--kind', 'cut', '--engine', 'ffmpeg', '--tool', f'{REL}/finish.py (ffmpeg mux)', '--parent', str(pic), *common], check=True)
subprocess.run(P + [str(cs), '--kind', 'other', '--engine', 'ffmpeg', '--tool', f'{REL}/finish.py (ffmpeg xstack)', '--parent', str(pic), *common], check=True)
for cid, l in L.items():   # the trimmed voice clips: cut from the 1F5 takes in silence, never sped up
    subprocess.run(P + [l['file'], '--kind', 'voice', '--engine', 'gemini-tts', '--tool', f'{REL}/trim.py (numpy cut in room tone, 15 ms fades)', '--parent', str(pathlib.Path(l['parent']).resolve()),
                        '--why', f'hologram 1F5 scissors, line {cid}: the 1F5 take trimmed with scissors only', '--prompt', l['text'],
                        '--setting', 'keep=' + json.dumps(l['keep']), '--input', f'record={REL}/lines-1f5-scissors.json'], check=True, stdout=subprocess.DEVNULL)
print('TD', TD, 'voice', vw, 'pic', pic, 'both', both, 'sheet', cs)
