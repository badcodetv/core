import numpy as np, librosa, subprocess, json
V='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/'
def load(f):
    b=subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','22050','-f','f32le','-'],capture_output=True).stdout
    return np.frombuffer(b,np.float32).copy()
o=load(V+'camping.mpeg'); n=load(V+'action/song 2 maybe (audio).wav')
H=2205 # 0.1 s
def feat(y):
    c=librosa.feature.chroma_cqt(y=y,sr=22050,hop_length=H)
    m=librosa.feature.mfcc(y=y,sr=22050,hop_length=H,n_mfcc=13)
    m=(m-m.mean(1,keepdims=True))/(m.std(1,keepdims=True)+1e-6)
    return np.vstack([c*3,m*0.5])
Fo,Fn=feat(o),feat(n)
D,wp=librosa.sequence.dtw(X=Fo,Y=Fn,metric='cosine')
wp=wp[::-1]*0.1
json.dump([[round(a,1),round(b,1)] for a,b in wp],open('dtw-old-new.json','w'))
for t in [0,5,10,12.4,14,15.5,20,25.5,30,41.7,52.5,64,69,75,80,90,101,112,120,129,134,140,150,155,165,175,185,195,202,210,215]:
    i=np.argmin(abs(wp[:,0]-t)); print(t,'->',wp[i,1])
rms=lambda y:librosa.feature.rms(y=y,hop_length=H)[0]
ro,rn=rms(o),rms(n)
print('old rms 10-17:',' '.join(f'{x:.2f}' for x in ro[100:170:2]))
print('new rms 0-17 :',' '.join(f'{x:.2f}' for x in rn[0:170:4]))
