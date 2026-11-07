"""Fold the kick / snare / hat onset envelopes over 8 grid steps (from grid.json) to see the groove, per song section."""
import json, numpy as np, librosa
G=json.load(open('grid.json')); P,PH=G['period'],G['phase']
SONG='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/song 2 maybe (audio).wav'
SR,HOP=22050,128
y,_=librosa.load(SONG,sr=SR); _,perc=librosa.effects.hpss(y,margin=2.0)
S=np.abs(librosa.stft(perc,n_fft=2048,hop_length=HOP)); f=librosa.fft_frequencies(sr=SR,n_fft=2048); fps=SR/HOP
def env(lo,hi):
    e=np.maximum(np.diff(np.log1p(S[(f>=lo)&(f<hi)].sum(0)),prepend=0),0); return e/(np.percentile(e,99.5)+1e-9)
E_={'kick':env(35,110),'snare':env(180,280),'clap/snare top':env(2000,5000),'hat':env(8000,11000)}
def fold(e,a,b,steps=8,bins=4):
    out=np.zeros(steps*bins); c=np.zeros(steps*bins)
    for i in range(int(a*fps),int(b*fps)):
        t=i/fps-PH; ph=(t/P)%steps; k=int(ph*bins)%(steps*bins); out[k]+=e[i]; c[k]+=1
    return out/np.maximum(c,1)
for name,(a,b) in {'verse1 12-56':(12,56),'hook1 56-77':(56,77.6),'verse2 78-121':(77.7,121),'bridge 144-183':(143.6,183.7),'hook3 184-205':(183.7,205)}.items():
    print('==',name,'(columns = grid steps 0..7, 4 bins each; # = strength)')
    for k,e in E_.items():
        v=fold(e,a,b); m=v.max()
        print(f'{k:15s}','|'.join(''.join(' .:-=+*#'[min(7,int(x/m*7.99))] for x in v[s*4:s*4+4]) for s in range(8)))
