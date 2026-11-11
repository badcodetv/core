"""1F5 (Kai, 11 Nov: new s01 words): rank the s01 takes by how close their voice is to the other 1F4 Maddie hologram lines (s02, s03, f01, f02, f04),
by measurement only (no Gemini listen): median F0 and spread (pyin), spectral centroid, mean of 20 MFCCs. The 1F4 s01 clip is printed as the control
(a voice Kai already accepted in this slot: a good take sits near it). Copied from accent-1f4.py.
Run: uv run -q --with librosa python3 accent-1f5.py <take.wav>..."""
import sys, numpy as np, librosa
O = '/mnt/d/badcode-videos/clips/gitpush-origin-master/hologram/voice-1f/'
REF = [O + f'clips-1f4/{k}.wav' for k in ['s02', 's03', 'f01', 'f02', 'f04']]
CTRL = O + 'clips-1f4/s01.wav'
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
    print('%-22s total %5.2f | f0 %.0f (%.2f) spread %.0f (%.2f) centroid %.0f (%.2f) timbre %.2f%s' % (f.split('/')[-1], tot, x['f0'], d[0], x['f0s'], d[1], x['cen'], d[2], d[3], '   <- control: the 1F4 s01 (accepted)' if f == CTRL else ''))
