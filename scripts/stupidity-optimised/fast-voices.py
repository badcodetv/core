"""Faster voices for Stupidity Optimised rough 4 (Jack, 2 Nov 2026: "they talk too slowly").

Each line: pauses inside it longer than PAUSE_MAX are shortened to PAUSE_MAX (cut in the silence, short crossfade),
then the whole line is time-stretched with ffmpeg's rubberband (pitch and formants kept) so its words per second
reach TARGET, with the stretch clamped to [LO, HI]. One- and two-word lines get FLAT. Originals are not touched;
output goes to a new folder.

  python3 scripts/stupidity-optimised/fast-voices.py wps.json OUT_DIR [--only 001-narrator,...] [--tag x]

wps.json: [[wps, name, words, dur, folder], ...] from the rough 3 audio list. Writes OUT_DIR/<name>.wav and
OUT_DIR/fast.json {name: {src, tempo, pauses_cut, dur_in, dur_out}}.
"""
import json, os, subprocess, sys
import numpy as np
import soundfile as sf

TARGET, LO, HI, FLAT = 3.0, 1.08, 1.3, 1.2
PAUSE_MAX, WIN = 0.22, 0.01
# per line: (tempo, squeeze pauses). 009 is meant to be halting; 021 sounded chipmunky at 1.3 (Gemini, 2 Nov, unverified)
OVERRIDE = {'009-brandon': (1.0, False), '021-prophet5': (1.15, True)}
ROOT = '/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/optimised stupidity/clips/film/voices'

rows = json.load(open(sys.argv[1]))
out = sys.argv[2]
only = None
if '--only' in sys.argv:
    only = set(sys.argv[sys.argv.index('--only') + 1].split(','))
for a in ('--target', '--hi'):
    if a in sys.argv:
        v = float(sys.argv[sys.argv.index(a) + 1])
        if a == '--target': TARGET = v
        else: HI = v
os.makedirs(out, exist_ok=True)
man_path = os.path.join(out, 'fast.json')
man = json.load(open(man_path)) if os.path.exists(man_path) else {}


def squeeze_pauses(x, sr):
    """Shorten silent runs inside the line (not at the ends) to PAUSE_MAX."""
    mono = x.mean(axis=1) if x.ndim > 1 else x
    w = int(sr * WIN)
    n = len(mono) // w
    rms = np.sqrt((mono[:n * w].reshape(n, w) ** 2).mean(axis=1) + 1e-12)
    db = 20 * np.log10(rms)
    quiet = db < max(db.max() - 38, -55)
    voiced = np.where(~quiet)[0]
    if len(voiced) == 0:
        return x, 0
    first, last = voiced[0], voiced[-1]
    keep = np.ones(len(mono), bool)
    cut = 0
    i = first
    fade = int(0.008 * sr)
    while i <= last:
        if quiet[i]:
            j = i
            while j <= last and quiet[j]:
                j += 1
            run = (j - i) * WIN
            if run > PAUSE_MAX:
                drop = run - PAUSE_MAX
                a = int((i * WIN + PAUSE_MAX / 2) * sr)
                b = a + int(drop * sr)
                keep[a:b] = False
                cut += drop
            i = j
        else:
            i += 1
    y = x[keep]
    # soften each join
    idx = np.where(np.diff(keep.astype(int)) == 1)[0]
    pos = np.cumsum(keep) - 1
    for k in idx:
        p = pos[k + 1]
        lo, hi = max(0, p - fade), min(len(y), p + fade)
        ramp = np.abs(np.linspace(-1, 1, hi - lo))
        y[lo:hi] = (y[lo:hi].T * ramp).T
    return y, cut


for wps, name, words, dur, folder in rows:
    if only and name not in only:
        continue
    src = f'{ROOT}/{folder}/{name}.wav'
    x, sr = sf.read(src)
    ov = OVERRIDE.get(name)
    y, cut = squeeze_pauses(x, sr) if (ov is None or ov[1]) else (x, 0)
    d2 = len(y) / sr
    tempo = ov[0] if ov else FLAT if words <= 2 else min(HI, max(LO, TARGET / (words / d2)))
    tmp = os.path.join(out, f'.{name}.sq.wav')
    sf.write(tmp, y, sr)
    dst = os.path.join(out, f'{name}.wav')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', tmp, '-af',
                    f'rubberband=tempo={tempo:.4f}:pitchq=quality:formant=preserved:transients=mixed', dst], check=True)
    os.remove(tmp)
    d3 = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', dst],
                              capture_output=True, text=True).stdout)
    man[name] = {'src': src, 'tempo': round(tempo, 3), 'pauses_cut': round(cut, 2), 'dur_in': round(dur, 2),
                 'dur_out': round(d3, 2)}
    print(f'{name:<16} {dur:5.1f}s -> {d3:5.1f}s  pauses -{cut:.1f}  x{tempo:.2f}', flush=True)
json.dump(man, open(man_path, 'w'), indent=1)
