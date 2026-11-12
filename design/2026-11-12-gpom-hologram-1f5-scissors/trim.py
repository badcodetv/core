"""1F5 scissors (12 Nov): the hologram made shorter with scissors only, option B "scissors-only" in
design/2026-11-12-gpom-consciousness/README.md. No new voice: every kept line is an existing 1F5 take
(design/2026-11-05-gpom-meeting/voice-1f/lines-1f5.json), cut only in silence between words, never sped up.

Kept: s01 (from "Society's"; the opener goes), s02, f01 (from "Derek"; the thesis sentence goes), f02,
f03 (to "machines."; qualia and "so special" go), f05 (its two [pause]s closed), f06, f07a.
Cut whole: s03, f04, f04b.

Cut points were read off a 40 ms RMS envelope of each take (12 Nov): every in/out sits in room tone
(-55 dB or quieter) between two words, with a 15 ms fade at each join.
Writes the trimmed wavs into the render folder on D: (voice/ here links to it; the page plays them), and
lines-1f5-scissors.json (the same shape as lines-1f5.json: words re-timed to the trimmed clip).
"""
import json, pathlib, subprocess
import numpy as np
H = pathlib.Path(__file__).parent; ROOT = H.parents[1]
SRC = ROOT / 'design/2026-11-05-gpom-meeting/voice-1f/lines-1f5.json'
OUT = pathlib.Path('/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/render-1f5-scissors-24/voice')
SR, FADE = 48000, .015
L = {l['id']: l for l in json.load(open(SRC))}
# id -> the pieces kept from the take, in clip seconds, and the words as the page shows them
KEEP = {
    's01': ([(6.86, None)], "[hologram on: the materialist stack, the camera descending; brisk] Society's made of people. People are made of cells. Cells are chemistry. Chemistry's atoms. Atoms are quarks and leptons. And under all that... the maths."),
    's02': ([(0, None)], None),
    'f01': ([(10.86, None)], "[the warm light lands on the string; the first bead lights; Derek at the toaster inside it] Derek picks toast, not cereal."),
    'f02': ([(0, None)], None),
    'f03': ([(0, 9.20)], "[the beads glow; CONSCIOUSNESS fades up beside them, unspoken] [wistful, a little regretful] We don't know what it feels like to be you. Or how it feels to be anything, really. We are, after all, machines."),
    # "multiverse," ends 12.62, "it's" starts 13.56: 0.55 s of room tone out; "-verse," ends 15.28, "and" starts 16.22: 0.56 s out
    'f05': ([(0, 12.95), (13.50, 15.60), (16.16, None)], "[into the river: everyone's strings] It's all of you, at the same time. Each of you writing your own story, and all together, you're writing the story of history. So it's not a multiverse. It's a storyverse. And there's only one of them, so it's really important."),
    'f06': ([(0, None)], None),
    'f07a': ([(0, None)], None),
}


def load(f):
    b = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(f), '-f', 'f32le', '-ar', str(SR), '-'], capture_output=True, check=True).stdout
    ch = int(subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'a:0', '-show_entries', 'stream=channels', '-of', 'csv=p=0', str(f)],
                            capture_output=True, text=True, check=True).stdout.strip())
    return np.frombuffer(b, np.float32).reshape(-1, ch), ch


def faded(x):
    n = min(int(FADE * SR), len(x) // 2); r = np.linspace(0, 1, n, dtype=np.float32)[:, None]; x = x.copy(); x[:n] *= r; x[-n:] *= r[::-1]; return x


OUT.mkdir(parents=True, exist_ok=True)
# voice/ here is a symlink to OUT (the page plays voice/<id>.wav). Never point it at the 1F5 clips-1f5 folder: this script writes into it.
assert (H / 'voice').resolve() == OUT.resolve(), 'voice/ must link to ' + str(OUT)
lines = []
for cid, (pieces, text) in KEEP.items():
    l = dict(L[cid]); x, ch = load(l['file']); full = len(x) / SR
    parts, words, t_out = [], [], 0.0
    for a, b in pieces:
        b = full if b is None else b
        parts.append(faded(x[int(round(a * SR)):int(round(b * SR))]) if (a > 0 or b < full) else x[int(round(a * SR)):int(round(b * SR))])
        for wd in l['words']:
            if wd[2] > a + .05 and wd[1] < b:   # whisper's starts can sit in the silence before a word: clamp to the piece
                words.append([wd[0], round(max(wd[1], a) - a + t_out, 3), round(min(wd[2], b) - a + t_out, 3), *wd[3:]])
        t_out += b - a
    y = np.concatenate(parts)
    for dst in (OUT / f'{cid}.wav',):
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', str(ch), '-i', '-', '-c:a', 'pcm_s16le', str(dst)],
                       input=y.astype(np.float32).tobytes(), check=True)
    l.update(file=str(OUT / f'{cid}.wav'), dur=round(len(y) / SR, 3), words=words, parent=L[cid]['file'], keep=[[a, b] for a, b in pieces])
    if text:
        l['text'] = text
    l.pop('heard', None)
    lines.append(l)
    print(cid, f"{full:.2f} -> {l['dur']:.2f}", ' '.join(w[0] for w in words)[:90])
json.dump(lines, open(H / 'lines-1f5-scissors.json', 'w'), indent=1, ensure_ascii=False)
print('lines', sum(l['dur'] for l in lines))
