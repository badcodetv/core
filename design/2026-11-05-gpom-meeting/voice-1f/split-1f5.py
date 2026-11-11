"""1F5 (Kai, 11 Nov): only s01 changes, to the words now in script.json ("Right. Let's start with science, which, as machines, is close to our
heart. ..."; "This is how you lot saw the world" dropped: the point is science AND consciousness). Three takes (take-s01k.txt, Aoede, profile-holo.md,
Bristol), picked by measurement only (no Gemini listen): check-1f3.py on words-1f5.json (s01k-1 the only verbatim take; 2 and 3 heard "close to our
art", 3 also "all that are the maths"), no gap over 1.2 s in any, and accent-1f5.py (s01k-1 closest to its stack neighbours s02/s03).
Cuts the pick into clips-1f5/s01.wav at faster-whisper word times, cards it (parent = the take), links every other clip to the real file it came
from (never through another link), and writes lines-1f5.json. Copied from split-1f4.py."""
import json, subprocess, pathlib, os
H = pathlib.Path(__file__).parent; ROOT = H.parents[2]
O = pathlib.Path('/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/voice-1f'); C = O / 'clips-1f5'; C.mkdir(exist_ok=True)
W = json.load(open(O / 'words-1f5.json'))
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(f)]))
S = json.load(open(ROOT / 'docs/stories/gitpush-origin-master/scenes/second-half-a-killbots/script.json'))
T = {l['id']: l['text'] for l in S['lines'] if 'id' in l and 'replaced' not in l}
PICK = os.environ.get('PICK', 's01k-1')
NEW = [('s01', PICK, 'stack', T['s01'], .35)]
old = {l['id']: l for l in json.load(open(H / 'lines-1f4.json'))}
new = {}
for cid, tk, beat, text, tail in NEW:
    src = O / f'take-{tk}.wav'; ws = W[str(src)]; TT = dur(src)
    i = max(0, ws[0][1] - .08); o = min(TT, ws[-1][2] + tail)
    f = C / f'{cid}.wav'
    if f.is_symlink(): f.unlink()
    subprocess.run(['ffmpeg','-v','error','-y','-ss',f'{i:.3f}','-i',str(src),'-t',f'{o-i:.3f}','-af','afade=t=out:st=%.3f:d=0.06' % (o-i-.06),str(f)], check=True)
    heard = ' '.join(w[0] for w in ws)
    new[cid] = dict(id=cid, take=tk, beat=beat, street=False, text=text, src_in=round(i,3), src_out=round(o,3), dur=round(o-i,3), file=str(f),
                    heard=heard, words=[(w[0], round(w[1]-i,3), round(w[2]-i,3)) for w in ws])
    print(cid, tk, new[cid]['dur'], heard)
    subprocess.run(['python3', str(ROOT / 'scripts/provenance/prov.py'), 'card', str(f), '--kind', 'voice', '--engine', 'gemini-tts',
                    '--tool', 'design/2026-11-05-gpom-meeting/voice-1f/split-1f5.py (ffmpeg cut at faster-whisper word times)', '--parent', str(src),
                    '--why', 'hologram 1F5 line s01 (Kai, 11 Nov: new words, science AND consciousness); take picked as the only whisper-verbatim take, no dead air, closest to s02/s03 by accent-1f5.py',
                    '--prompt', text, '--input', f'heard={heard}', '--input', 'record=design/2026-11-05-gpom-meeting/voice-1f/lines-1f5.json',
                    '--setting', f'src_in={i:.2f}', '--setting', f'src_out={o:.2f}'], check=True, stdout=subprocess.DEVNULL)
ORDER = ['b01', 's01', 's02', 's03', 'f01', 'f02', 'f03', 'f04', 'f04b', 'f05', 'f06', 'f07a', 'f07b']
recs = []
for cid in ORDER:
    if cid in new: recs.append(new[cid]); continue
    r = dict(old[cid]); real = pathlib.Path(r['file']).resolve(); lk = C / f'{cid}.wav'
    if lk.is_symlink() or lk.exists(): lk.unlink()
    lk.symlink_to(os.path.relpath(real, C)); r['file'] = str(lk)
    recs.append(r)
json.dump(recs, open(H / 'lines-1f5.json', 'w'), indent=1, ensure_ascii=False)
print([(r['id'], r['dur']) for r in recs])
