import numpy as np, librosa, subprocess, json
V='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/'
def load(f):
    b=subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','22050','-f','f32le','-'],capture_output=True).stdout
    return np.frombuffer(b,np.float32).copy()
for k,f in [('old',V+'camping.mpeg'),('new',V+'action/song 2 maybe (audio).wav')]:
    y=load(f); S=np.abs(librosa.stft(y,n_fft=2048,hop_length=512))
    fr=librosa.fft_frequencies(sr=22050,n_fft=2048)
    low=S[fr<120].sum(0); full=S.sum(0)
    t=librosa.frames_to_time(np.arange(S.shape[1]),sr=22050,hop_length=512)
    beats=json.load(open(f'beats-{k}.json'))['beats']
    # per bar (4 beats): low-band energy
    bars=beats[::4]
    out=[]
    for a,b in zip(bars,bars[1:]):
        m=(t>=a)&(t<b); out.append((a,low[m].mean(),full[m].mean()))
    L=np.array([o[1] for o in out]); F=np.array([o[2] for o in out])
    L/=np.median(L); F/=np.median(F)
    print('==',k)
    print(' '.join(f"{o[0]:.0f}:{l:.1f}/{f_:.1f}" for o,l,f_ in zip(out,L,F)))
