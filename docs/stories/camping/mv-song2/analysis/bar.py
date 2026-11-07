"""Find the quarter-note beat, the snare (2 and 4) and the downbeat (1) by folding the drum envelopes over one bar.
Listening (docs/listening/log/2026-11-07-152100-...): ~86-88 BPM, straight, snare on 2 and 4, kick on 1, the and of 2, and 3.
grid.json's period (0.341 s) is an EIGHTH note; a bar is 8 of them. Writes bars.json: beats (quarters), snares, downbeats."""
import json, numpy as np, librosa
G=json.load(open('grid.json')); E8=G['period']
SONG='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/action/song 2 maybe (audio).wav'
SR,HOP=22050,128
y,_=librosa.load(SONG,sr=SR); _,perc=librosa.effects.hpss(y,margin=2.0)
S=np.abs(librosa.stft(perc,n_fft=2048,hop_length=HOP)); f=librosa.fft_frequencies(sr=SR,n_fft=2048); fps=SR/HOP
def env(lo,hi):
    e=np.maximum(np.diff(np.log1p(S[(f>=lo)&(f<hi)].sum(0)),prepend=0),0); return e/(np.percentile(e,99.5)+1e-9)
kick,snare=env(35,110),env(2000,5000)
T=np.arange(len(kick))/fps
# refine the bar period and phase: kick on 0, 3/8, 4/8 of a bar; snare on 2/8, 6/8 (in eighths: k 0,3,4  s 2,6)
def score(bar,ph,a=21,b=210):
    s=0;n=0
    for t0 in np.arange(ph,b,bar):
        if t0<a: continue
        for k,e,w in ((0,kick,1),(3,kick,.5),(4,kick,1),(2,snare,1.5),(6,snare,1.5)):
            i=int(round((t0+k*bar/8)*fps))
            if i<len(e): s+=w*e[max(0,i-2):i+3].max(); n+=1
    return s/n
best=(0,0,0)
for bar in np.arange(8*E8-0.03,8*E8+0.03,0.0005):
    for ph in np.arange(0,bar,0.004):
        sc=score(bar,ph)
        if sc>best[0]: best=(sc,bar,ph)
_,BAR,PH=best
# report a rival: the same pattern shifted by half a bar (snare on 1 and 3 instead) for a sanity check
print('bar',round(BAR,4),'s =',round(240/BAR,2),'BPM; first downbeat phase',round(PH,3),'score',round(best[0],3),
      '| half-bar shift score',round(score(BAR,PH+BAR/2),3),'| quarter shift',round(score(BAR,PH+BAR/4),3))
# local check: per 4 bars, the offset that best fits
offs=np.arange(-0.06,0.0601,0.003); loc=[]
for t0 in np.arange(PH,T[-1]-4*BAR,4*BAR):
    sc=[]
    for o in offs:
        s=0
        for j in range(4):
            for k,e in ((0,kick),(4,kick),(2,snare),(6,snare)):
                i=int(round((t0+o+j*BAR+k*BAR/8)*fps)); s+=e[max(0,i-2):i+3].max() if i<len(e) else 0
        sc.append(s)
    loc.append((round(t0,2),int(offs[int(np.argmax(sc))]*1000),round(max(sc)/16,2)))
print('offset ms per 4 bars:',[l[1] for l in loc])
q=BAR/4; beats=[round(PH+i*q,4) for i in range(int((T[-1]-PH)/q)+1)] 
down=[round(PH+i*BAR,4) for i in range(int((T[-1]-PH)/BAR)+1)]
# allow negative start (pickup) beats
pre=[round(PH-i*q,4) for i in range(1,int(PH/q)+1)][::-1]
json.dump({'bar':round(BAR,5),'bpm':round(240/BAR,3),'beat':round(q,5),'first_downbeat':round(PH,4),'beats':pre+beats,
           'downbeats':down,'snares':[b for i,b in enumerate(beats) if i%2==1],'local_offset_ms_per_4_bars':loc},open('bars.json','w'),indent=1)
