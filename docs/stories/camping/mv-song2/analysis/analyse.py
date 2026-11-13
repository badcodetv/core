"""Song 2 re-cut analysis (2026-11-07): word timestamps + beat grid for the old song and song 2."""
import sys, json, subprocess, numpy as np, librosa
from faster_whisper import WhisperModel
V='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/camping vid/'
SONGS={'old':V+'camping.mpeg','new':V+'action/song 2 maybe (audio).wav'}
OUT='docs/stories/camping/mv-song2/analysis/'
m=WhisperModel('medium',device='cpu',compute_type='int8')
for k,f in SONGS.items():
    b=subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar','22050','-f','f32le','-'],capture_output=True).stdout
    y=np.frombuffer(b,np.float32).copy()
    tempo,beats=librosa.beat.beat_track(y=y,sr=22050,units='time',start_bpm=176)
    on=librosa.onset.onset_strength(y=y,sr=22050)
    json.dump({'tempo':float(np.atleast_1d(tempo)[0]),'beats':[round(float(x),3) for x in beats]},open(OUT+f'beats-{k}.json','w'))
    y16=librosa.resample(y,orig_sr=22050,target_sr=16000)
    segs,_=m.transcribe(y16,language='en',word_timestamps=True,vad_filter=False)
    rows=[]
    for s in segs:
        rows.append({'start':round(s.start,2),'end':round(s.end,2),'text':s.text.strip(),'words':[[round(w.start,2),round(w.end,2),w.word.strip()] for w in (s.words or [])]})
        print(k,f"{s.start:7.2f} {s.end:7.2f} {s.text}",flush=True)
    json.dump(rows,open(OUT+f'words-{k}.json','w'),indent=0)
print('DONE')
