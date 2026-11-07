"""Actual drum hits (not a grid): kick and snare/clap onsets picked from the percussive part, 5.8 ms resolution."""
import json, numpy as np, librosa
SONG='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/song 2 maybe (audio).wav'
SR,HOP=22050,128
y,_=librosa.load(SONG,sr=SR); _,perc=librosa.effects.hpss(y,margin=2.0)
S=np.abs(librosa.stft(perc,n_fft=2048,hop_length=HOP)); f=librosa.fft_frequencies(sr=SR,n_fft=2048); fps=SR/HOP
def env(lo,hi):
    e=np.maximum(np.diff(np.log1p(S[(f>=lo)&(f<hi)].sum(0)),prepend=0),0); return e/(np.percentile(e,99.5)+1e-9)
out={}
for name,(lo,hi,d) in {'kick':(35,110,0.6),'snare':(1500,5000,0.6)}.items():
    e=env(lo,hi)
    pk=librosa.util.peak_pick(e,pre_max=8,post_max=8,pre_avg=40,post_avg=40,delta=d*np.std(e)+0.05,wait=int(0.12*fps))
    t=pk/fps; out[name]=[round(float(x),4) for x in t]
    ioi=np.diff(t); h,edges=np.histogram(ioi,bins=np.arange(0.1,1.5,0.02))
    top=sorted(zip(h,edges),reverse=True)[:5]
    print(name,len(t),'hits; top inter-onset intervals (s):',[(round(e_,2),int(n)) for n,e_ in top])
json.dump(out,open('hits.json','w'))
