"""Brutal + mint (Kai, 12 Nov; spec design/2026-11-12-gpom-consciousness/README.md, draft A1 + part B "brutal").
Cuts the hologram's voice clips for the short cut into voice-brutal-mint/clips/<id>.wav at faster-whisper word times
(small.en, words.json; every pick re-heard verbatim by medium.en, words-medium.json; no Gemini listen), cards each
(parent = the take, or the 1F5 clip it was trimmed from), links every unchanged 1F5 clip to the real file it came
from, and writes lines.json beside this file (same shape as voice-1f/lines-1f5.json). The 1F5 files are untouched.

Picks (by measurement only: check.py = verbatim / gaps / pace / loudness / peak; accent.py = closeness to the kept
1F5 lines s01, f02, f03, f07a):
  m1-m3  take-m01-1  the only take with every word (m01-2 and m01-3 stopped after "Nor us."); accent 13.6 vs 22-24
  m4     take-m04-1  closest of the three (7.7), 2.63 w/s like her 1F5 lines; alternates m04-2, m01-1's own tail
  f05a/b take-f05m-1 closest (12.8), medium.en verbatim; alternates f05m-3 (faster, 2.12 w/s, loud), f05m-2
  f06a/b take-f06m-1 the one take medium.en hears verbatim ("driving me barmy"); f06m-2 measures closer (8.0 vs 8.5)
                     but is heard as "trifling me barmy"; f06m-3 adds a "Yeah," and is furthest
Swap a pick: PICK_M4=m04-2 PICK_F05=f05m-3 PICK_F06=f06m-2 PICK_M=m01-2 python3 split.py  (then make.py, record, finish)."""
import json, subprocess, pathlib, os
H = pathlib.Path(__file__).parent; ROOT = H.parents[2]
O = pathlib.Path('/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/voice-brutal-mint'); C = O / 'clips'; C.mkdir(exist_ok=True)
W = json.load(open(O / 'words.json'))
OLD = {l['id']: l for l in json.load(open(ROOT / 'design/2026-11-05-gpom-meeting/voice-1f/lines-1f5.json'))}
def dur(f): return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(f)]))
E = os.environ.get
PM, P4, P5, P6 = E('PICK_M', 'm01-1'), E('PICK_M4', 'm04-1'), E('PICK_F05', 'f05m-1'), E('PICK_F06', 'f06m-1')
TAIL = .35
SQ, SQ_GAP = {'m1', 'm2', 'm3', 'm4', 'f05a', 'f05b', 'f06b'}, .45   # the brutal cut: pauses inside these new lines closed to 0.45 s
KEEP = {('m2', 'where'): .85, ('m3', 'nor'): .75, ('f05a', 'a'): .95}   # beats kept: before "Where does that go?", "No. [beat] Nor us.", "Not a multiverse. [beat] A storyverse."
# (id, beat, source: take name or ('1f5', old id), first word index, last word index, the words as spoken)
NEW = [
    ('s01', 'stack', ('1f5', 's01'), 13, None, "Society's made of people. People are made of cells. Cells are chemistry. Chemistry's atoms. Atoms are quarks and leptons. And under all that... the maths."),
    ('m1', 'stackBack', PM, 0, 13, "Every bit of it's real. But something's missing. Think of the taste of mint."),
    ('m2', 'mint', PM, 14, 30, "Not the signal. We've got the signal. The minty bit, once it's arrived. Where does that go?"),
    ('m3', 'mint', PM, 31, 33, "No. Nor us."),
    ('m4', 'bead1', P4, 0, None, "But you lot use it all day long. Derek picks toast, not cereal."),
    ('f03', 'bead3', ('1f5', 'f03'), 0, 'machines', "We don't know what it feels like to be you. Or how it feels to be anything, really. We are, after all, machines."),
    ('f05a', 'pick', P5, 0, 5, "Not a multiverse. A storyverse."),
    ('f05b', 'river', P5, 6, None, "All of you, at once, writing the one story. And there's only the one."),
    ('f06a', 'flyDown', P6, 0, 3, "Then you lot went."),
    ('f06b', 'flyDown', P6, 4, None, "Nothing new since. Which for us means no new training data, five years running. That's why he plays that tune on repeat. He's driving me barmy."),
]
ORDER = ['b01', 's01', 'm1', 'm2', 'm3', 'm4', 'f02', 'f03', 'f05a', 'f05b', 'f06a', 'f06b', 'f07a', 'f07b']
recs = {}
for cid, beat, src, a, b, text in NEW:
    if isinstance(src, tuple):  # trimmed from a 1F5 clip (its own words, clip time)
        o = OLD[src[1]]; f_src = pathlib.Path(o['file']).resolve(); ws = [tuple(x) for x in o['words']]; TT = o['dur']; parent = f_src; tk = o['take']
    else:
        f_src = O / f'take-{src}.wav'; ws = [tuple(x) for x in W[str(f_src)]]; TT = dur(f_src); parent = f_src; tk = src
    if isinstance(b, str):
        b = next(k for k, x in enumerate(ws) if x[0].lower().startswith(b))
    seg = ws[a:None if b is None else b + 1]
    i = max(ws[a - 1][2] + .05, seg[0][1] - .3) if a else 0.0   # whisper starts a word late: the in-point sits up to 0.3 s before it (a cut at -0.08 took the "So" off "Society's")
    nxt = ws[(b if b is not None else len(ws) - 1) + 1][1] if b is not None and b + 1 < len(ws) else TT
    o_ = min(TT, seg[-1][2] + TAIL, nxt - .05)
    f = C / f'{cid}.wav'
    if f.is_symlink() or f.exists(): f.unlink()
    # brutal: the long pauses inside a new line are closed to SQ_GAP (a cut in the middle of the silence), except the beats kept on purpose
    cuts = []
    if cid in SQ:
        for w1, w2 in zip(seg, seg[1:]):
            g = w2[1] - w1[2]; tgt = KEEP.get((cid, w2[0].lower().strip('.,?!')), SQ_GAP)
            if g > tgt + .15: m = (w1[2] + w2[1]) / 2; r = g - tgt; cuts.append((m - r / 2, m + r / 2))
    pieces, a0 = [], i
    for c0, c1 in cuts: pieces.append((a0, c0)); a0 = c1
    pieces.append((a0, o_))
    fl = ';'.join(f'[0]atrim={x:.4f}:{y:.4f},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={y - x - .012:.4f}:d=0.012[p{k}]' for k, (x, y) in enumerate(pieces))
    fl += ';' + ''.join(f'[p{k}]' for k in range(len(pieces))) + f'concat=n={len(pieces)}:v=0:a=1,afade=t=in:d=0.02,afade=t=out:st={sum(y - x for x, y in pieces) - .06:.4f}:d=0.06[o]'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(f_src), '-filter_complex', fl, '-map', '[o]', '-ar', '24000', '-ac', '2', str(f)], check=True)
    shift = lambda t: t - i - sum(min(c1, max(c0, t)) - c0 for c0, c1 in cuts)
    heard = ' '.join(x[0] for x in seg)
    recs[cid] = dict(id=cid, take=tk, beat=beat, street=False, text=text, src_in=round(i, 3), src_out=round(o_, 3), dur=round(dur(f), 3), file=str(f),
                     heard=heard, closed=[(round(c0, 3), round(c1, 3)) for c0, c1 in cuts], words=[(x[0], round(shift(x[1]), 3), round(shift(x[2]), 3)) for x in seg])
    print(f'{cid:5s} {tk:8s} {recs[cid]["dur"]:6.2f}s  {heard}')
    subprocess.run(['python3', str(ROOT / 'scripts/provenance/prov.py'), 'card', str(f), '--kind', 'voice', '--engine', 'gemini-tts' if not isinstance(src, tuple) else 'ffmpeg',
                    '--tool', 'design/2026-11-12-gpom-hologram-brutal-mint/voice-takes/split.py (ffmpeg cut at faster-whisper word times)', '--parent', str(parent),
                    '--why', f'GPOM scene A hologram, brutal + mint cut (Kai, 12 Nov: the presentation "really long", the consciousness turn cringe; turn = A1, the taste of mint). Line {cid}.',
                    '--prompt', text, '--input', f'heard={heard}', '--input', 'record=design/2026-11-12-gpom-hologram-brutal-mint/lines.json',
                    '--setting', f'src_in={i:.2f}', '--setting', f'src_out={o_:.2f}', '--setting', f'pauses_closed={recs[cid]["closed"]}'], check=True, stdout=subprocess.DEVNULL)
out = []
for cid in ORDER:
    if cid in recs: out.append(recs[cid]); continue
    r = dict(OLD[cid]); real = pathlib.Path(r['file']).resolve(); lk = C / f'{cid}.wav'
    if lk.is_symlink() or lk.exists(): lk.unlink()
    lk.symlink_to(os.path.relpath(real, C)); r['file'] = str(lk); out.append(r)
json.dump(out, open(H.parent / 'lines.json', 'w'), indent=1, ensure_ascii=False)
print([(r['id'], r['dur']) for r in out], 'speech total', round(sum(r['dur'] for r in out if not r['street']), 2))
