import numpy as np, librosa, subprocess, json
V='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/'
def load(f):
    b=subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','22050','-f','f32le','-'],capture_output=True).stdout
    return np.frombuffer(b,np.float32).copy()
for k,f,a,b in [('old',V+'camping.mpeg',9,17),('new',V+'action/song 2 maybe (audio).wav',2,15)]:
    y=load(f); bt=json.load(open(f'beats-{k}.json'))['beats']
    print(k,'beats',[x for x in bt if a<=x<=b])
    S=np.abs(librosa.stft(y,n_fft=1024,hop_length=1102)); fr=librosa.fft_frequencies(sr=22050,n_fft=1024)
    low=S[fr<150].sum(0); hi=S[fr>2000].sum(0); t=np.arange(S.shape[1])*0.05
    m=(t>=a)&(t<b); low/=np.percentile(low,90); hi/=np.percentile(hi,90)
    print(' '.join(f"{tt:.2f}:{l:.1f}|{h:.1f}" for tt,l,h in zip(t[m][::2],low[m][::2],hi[m][::2])))
