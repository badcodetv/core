"""Cut 10B5 -> an edl premiere-plan.py can build from: each shot is the ORIGINAL clip with its in-point
(Kai 2026-08-24: clips imported individually, never the ffmpeg parts), on the same 24 fps frames assemble.py
used, and the song cut to 187.0 s with the 0.12 s fade baked in (Premiere has no audio-fade API).
In Premiere the A1 clip's Volume > Level is then raised +1.6 dB (Premiere-only, set by hand through the bridge) so the
export lands at YouTube's -14 LUFS: the song alone measures -16.1 LUFS, true peak -3.2.
    python3 premiere-edl.py B5 0.12  ->  /mnt/d/.../gang/cut10B5/premiere/edl.json"""
import json, pathlib, subprocess, sys
HERE = pathlib.Path(__file__).parent
L, FADE = sys.argv[1], float(sys.argv[2])
MEDIA = pathlib.Path('/mnt/d/badcode-videos/bank-robbery-music/gang'); VID, NOIR = MEDIA / 'video', MEDIA.parent / 'noir' / 'video'
SONG = MEDIA.parent / 'the version.wav'; END = 187.0
src = lambda ref: NOIR / (ref[3:] + '.mp4') if ref.startswith('cn:') else sorted(VID.glob(f'bg-{ref}-*.mp4'))[0]
out = MEDIA / f'cut10{L}' / 'premiere'; out.mkdir(parents=True, exist_ok=True)
song = out / f'the version-cut10{L}.wav'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(SONG), '-t', str(END), '-af', f'afade=t=out:st={END - FADE}:d={FADE}',
                '-c:a', 'pcm_s24le', str(song)], check=True)
video = []
for r in json.load(open(HERE / f'plan-{L}.json')):
    fs, fe = round(r['start'] * 24), round(r['end'] * 24)
    video.append({'file': str(src(r['clip'])), 'start': fs / 24, 'dur': (fe - fs) / 24, 'in': r['in'], 'clip': r['clip']})
edl = {'total': END, 'fps': 24, 'video': video, 'audio': [{'name': 'mus-the version', 'file': str(song)}], 'events': []}
(out / 'edl.json').write_text(json.dumps(edl, indent=1))
print(out / 'edl.json', len(video), 'shots')
