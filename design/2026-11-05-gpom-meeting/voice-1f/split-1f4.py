"""1F4 (Kai's round 24 notes, 10 Nov): f02 re-split from the same take (f02n-4) with the whole tail, so the final "d" of "married!" finishes
(at2210); f03, f05, f06 and f07a re-voiced with the words in script.json (at2370, at3588, at3963 + at3872, at4326). Cuts the picks into
clips-1f4/<id>.wav at faster-whisper word times (no Gemini listen), cards each (parent = the take), links every unchanged clip to the real
file it came from (never through another link), and writes lines-1f4.json. Picks are set in PICKS below, from check-1f3.py on words-1f4*.json
and the f06 accent measurement (accent-1f4.py)."""
import json, subprocess, pathlib, re, os
H = pathlib.Path(__file__).parent; ROOT = H.parents[2]
O = pathlib.Path('/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/voice-1f'); C = O / 'clips-1f4'; C.mkdir(exist_ok=True)
W = {}
for j in ['words-1f3.json', 'words-1f3b.json', 'words-1f4.json', 'words-1f4b.json']:
    if (O / j).exists(): W.update(json.load(open(O / j)))
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(f)]))
S = json.load(open(ROOT / 'docs/stories/gitpush-origin-master/scenes/second-half-a-killbots/script.json'))
T = {l['id']: l['text'] for l in S['lines'] if 'id' in l}
PICKS = json.loads(os.environ['PICKS'])   # e.g. {"f03": "f03r-1", "f05": "f05r-2", "f06": "f06r-3", "f07a": "f07r-1"}
f07a_text = T['f07'].split('[beat]')[0].strip()
NEW = [('f02', 'f02n-4', 'bead2', T['f02'], .85),            # the tail: the hard "d" of "married!" rings on past whisper's word end
       ('f03', PICKS['f03'], 'bead3', T['f03'], .35), ('f05', PICKS['f05'], 'river', T['f05'], .35),
       ('f06', PICKS['f06'], 'flyDown', T['f06'], .35), ('f07a', PICKS['f07a'], 'arcDraw', f07a_text, .35)]
old = {l['id']: l for l in json.load(open(H / 'lines-1f3.json'))}
new = {}
for cid, tk, beat, text, tail in NEW:
    src = O / f'take-{tk}.wav'; ws = W[str(src)]; TT = dur(src)
    i = max(0, ws[0][1] - .08); o = min(TT, ws[-1][2] + tail)
    f = C / f'{cid}.wav'
    if f.is_symlink(): f.unlink()   # never write through a link into another round's clips
    subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{i:.3f}','-i',str(src),'-t',f'{o-i:.3f}','-af','afade=t=out:st=%.3f:d=0.06' % (o-i-.06),str(f)], check=True)
    heard = ' '.join(w[0] for w in ws)
    new[cid] = dict(id=cid, take=tk, beat=beat, street=False, text=text, src_in=round(i,3), src_out=round(o,3), dur=round(o-i,3), file=str(f),
                    heard=heard, words=[(w[0], round(w[1]-i,3), round(w[2]-i,3)) for w in ws])
    print(cid, tk, new[cid]['dur'], heard)
    subprocess.run(['python3', str(ROOT / 'scripts/provenance/prov.py'), 'card', str(f), '--kind', 'voice', '--engine', 'gemini-tts',
                    '--tool', 'design/2026-11-05-gpom-meeting/voice-1f/split-1f4.py (ffmpeg cut at faster-whisper word times)', '--parent', str(src),
                    '--why', f'hologram 1F4 line {cid} (Kai round 24 notes, 10 Nov); take picked as whisper-verbatim, no dead air' + (', f06 picked closest to f01/f02 accent by measurement' if cid == 'f06' else '') + (', re-split with the full tail so the final d of married finishes' if cid == 'f02' else ''),
                    '--prompt', text, '--input', f'heard={heard}', '--input', 'record=design/2026-11-05-gpom-meeting/voice-1f/lines-1f4.json',
                    '--setting', f'src_in={i:.2f}', '--setting', f'src_out={o:.2f}'], check=True, stdout=subprocess.DEVNULL)
ORDER = ['b01', 's01', 's02', 's03', 'f01', 'f02', 'f03', 'f04', 'f04b', 'f05', 'f06', 'f07a', 'f07b']
recs = []
for cid in ORDER:
    if cid in new: recs.append(new[cid]); continue
    r = dict(old[cid]); real = pathlib.Path(r['file']).resolve(); lk = C / f'{cid}.wav'
    if lk.is_symlink() or lk.exists(): lk.unlink()
    lk.symlink_to(os.path.relpath(real, C)); r['file'] = str(lk); r.pop('placeholder', None)
    recs.append(r)
json.dump(recs, open(H / 'lines-1f4.json', 'w'), indent=1, ensure_ascii=False)
print([(r['id'], r['dur']) for r in recs])
