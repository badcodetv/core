"""1F4 (Kai at3872: the 1F3 f06 "is a totally different accent, we've lost the Maddy accent"): rank f06 takes by how close their voice is to
f01 + f02 (the 1F3 clips Kai is happy with), by measurement only (no Gemini listen). Per file: median F0 and its spread (pyin), spectral
centroid, and the mean of 20 MFCCs (timbre, which carries much of an accent's vowel colour). Distance = z-scored feature gap to the reference.
The rejected 1F3 f06 (take-f06n-2) is printed as a control: a good measure puts it far from the reference.
Run: uv run -q --with librosa python3 accent-1f4.py <take.wav>..."""
import sys, numpy as np, librosa
O = '/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/voice-1f/'
REF = [O + 'clips-1f3/f01.wav', O + 'clips-1f3/f02.wav']
CTRL = O + 'take-f06n-2.wav'
def feats(f):
    y, sr = librosa.load(f, sr=24000); y, _ = librosa.effects.trim(y, top_db=35)
    f0, v, _ = librosa.pyin(y, fmin=90, fmax=600, sr=sr, frame_length=1024); f0 = f0[~np.isnan(f0)]
    mf = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20); cen = librosa.feature.spectral_centroid(y=y, sr=sr)
    voiced = librosa.feature.rms(y=y)[0] > .02
    return dict(f0=np.median(f0), f0s=np.percentile(f0, 90) - np.percentile(f0, 10), cen=np.median(cen[0][voiced[:cen.shape[1]]]),
                mfcc=mf[:, voiced[:mf.shape[1]]].mean(1))
R = [feats(f) for f in REF]; ref = {k: np.mean([r[k] for r in R], 0) for k in R[0]}
def dist(x):
    d = [abs(np.log(x['f0'] / ref['f0'])) / .05, abs(np.log(x['f0s'] / ref['f0s'])) / .15, abs(np.log(x['cen'] / ref['cen'])) / .05,
         np.linalg.norm(x['mfcc'][1:] - ref['mfcc'][1:]) / 8]
    return sum(d), d
print('ref  f0 %.0f Hz  spread %.0f  centroid %.0f' % (ref['f0'], ref['f0s'], ref['cen']))
for f in [CTRL] + sys.argv[1:]:
    x = feats(f); tot, d = dist(x)
    print('%-22s total %5.2f | f0 %.0f (%.2f) spread %.0f (%.2f) centroid %.0f (%.2f) timbre %.2f%s' % (f.split('/')[-1], tot, x['f0'], d[0], x['f0s'], d[1], x['cen'], d[2], d[3], '   <- control: the rejected 1F3 f06' if f == CTRL else ''))
