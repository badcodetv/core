"""GPOM chorus (the people): Kai's picked Veo clips cut to the beat over the first pass of chorus 2.

One chorus now (decisions #42): the first 32 beats of chorus 2 (01 GPOM start 106.917 s, song 113.917 s,
174 BPM), 265 frames at 24 fps, ending on black. Writes <media>/cut/: per-shot clips, edl.json (the timeline
format in scripts/scene/timeline.py), mix.wav and preview.mp4.

  python3 scripts/gpom/choruses/cut_humans.py
"""
import json
import pathlib
import subprocess

MEDIA = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/choruses-humans')
SONG = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/choruses-humans/cut-r1/music-pass.wav')
FPS, BPM, FRAMES = 24, 174, 265
# Veo baked white pillarbox bars into HE1-a-b (x 0-95 and 1186-1279): crop inside them and scale back up.
CROP = {'HE1-a-b': 'crop=1080:608:100:56,'}
BEAT = 60 / BPM * FPS  # 8.276 frames

# (clip, beats, in-point s, beat id, what) in story order; in-points at each clip's motion peak (frame difference).
SHOTS = [
    ('TR1-b-c', 2, 2.70, 'money', 'van sprays the shelter; he flinches over his box'),
    ('TR2-a',   2, 1.30, 'money', 'wide: the van blurs past the trader'),
    ('BD1-b-c', 2, 2.85, 'money', 'shop lights go off behind her'),
    ('BD2-c',   2, 2.20, 'money', 'the shop window across the street, rain'),
    ('CA1-a-a', 2, 3.10, 'cash',  'the cash machine dies; the queue presses in'),
    ('SH1-b-a', 2, 0.40, 'shops', 'the last pump bagged; drivers stare'),
    ('GR1-a-a', 4, 0.90, 'flight', 'camera rises: the jam goes on for miles'),
    ('GR2-d',   2, 2.40, 'flight', 'two walkers drag suitcases past'),
    ('GR2-f',   2, 2.40, 'flight', 'the line of walkers on the hard shoulder'),
    ('BS1-a-a', 2, 2.25, 'flight', 'the back seat: glow pulses on the clouds'),
    ('BS2-f',   2, 2.50, 'flight', "the dog's ears prick; it turns to the window"),
    ('HE1-a-b', 2, 2.30, 'sky',   'the helicopter spirals down behind the roofs'),
    ('LO2-e',   2, 0.55, 'dark',  'the man on the hill as the lights go out below'),
    ('EM1-b-a', 2, 2.60, 'gone',  'down the lane of abandoned cars'),
    ('BLACK',   2, 0.0,  'gone',  'black, into the war'),
]
BEATS = [('money', 'The money goes'), ('cash', 'The money stops'), ('shops', 'Nothing to buy'),
         ('flight', 'Everyone leaves'), ('sky', 'Something in the sky'), ('dark', 'The lights go out'),
         ('gone', 'Gone')]


def ff(*a):
    subprocess.run(['ffmpeg', '-nostdin', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def main():
    out = MEDIA / 'cut'
    (out / 'shots').mkdir(parents=True, exist_ok=True)
    assert sum(s[1] for s in SHOTS) == 32
    video, beat_at, b = [], {}, 0
    for k, (clip, n, ip, beat, what) in enumerate(SHOTS):
        f0, f1 = round(b * BEAT), (FRAMES if k == len(SHOTS) - 1 else round((b + n) * BEAT))
        nf = f1 - f0
        dst = out / 'shots' / f'{k:02d}-{clip}.mp4'
        if clip == 'BLACK':
            ff('-f', 'lavfi', '-i', f'color=black:s=1280x720:r={FPS}', '-frames:v', nf, '-c:v', 'libx264',
               '-pix_fmt', 'yuv420p', dst)
            src = None
        else:
            src = MEDIA / 'video' / f'{clip}.mp4'
            ip = min(ip, 3.92 - nf / FPS - 0.01)
            ff('-ss', f'{ip:.3f}', '-i', src, '-frames:v', nf, '-an', '-vf', f"{CROP.get(clip, '')}fps={FPS},scale=1280:720",
               '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', dst)
        # Premiere gets the Veo source with its in-point (handles to slide); cropped and black shots use the shot file.
        pr = str(src) if src and clip not in CROP else str(dst)
        video.append({'file': pr, 'shot': str(dst), 'start': f0 / FPS, 'dur': nf / FPS, 'beat': beat,
                      'source': str(src) if src else 'black', 'in': round(ip, 3) if pr == str(src) else 0.0,
                      'what': what})
        beat_at.setdefault(beat, [f0 / FPS, f1 / FPS])[1] = f1 / FPS
        b += n
    (out / 'list.txt').write_text(''.join(f"file 'shots/{pathlib.Path(v['shot']).name}'\n" for v in video))
    ff('-f', 'concat', '-safe', '0', '-i', out / 'list.txt', '-c', 'copy', out / 'picture.mp4')
    total = FRAMES / FPS
    ff('-i', SONG, '-t', f'{total:.4f}', '-c:a', 'pcm_s16le', out / 'mus-chorus.wav')
    ff('-i', out / 'picture.mp4', '-i', out / 'mus-chorus.wav', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
       '-shortest', out / 'preview.mp4')
    edl = {
        'sequence': '01 GPOM chorus r2', 'title': 'Chorus Timeline',
        'heading': 'GPOM chorus: the people (round 2)',
        'intro': ('Your 14 picked clips, cut to the beat over the first half of chorus 2 (32 beats, 11.04 s; '
                  '01 GPOM start 106.92 s), ending on black into the war. Each clip enters at its biggest movement. '
                  'Play it, click any shot and leave a note in its yellow slip.'),
        'fps': FPS, 'total': total,
        'beats': [{'id': k, 'title': t, 'start': beat_at[k][0], 'dur': beat_at[k][1] - beat_at[k][0],
                   'see': '; '.join(v['what'] for v in video if v['beat'] == k), 'lines': []} for k, t in BEATS],
        'video': video,
        'audio': [{'track': 'A1', 'name': 'mus-chorus', 'file': str(out / 'mus-chorus.wav')}],
        'events': [{'stem': 'mus-chorus', 't': 0.0, 'dur': total,
                    'what': 'gpom-main-track, chorus 2 first pass (song 113.917 s, 32 beats)', 'src': str(SONG)}],
        'flags': ['Cuts land on the 174 BPM grid from Kai\'s chorus marker; the chorus downbeat is ~0.2 s ambiguous, so the whole cut may want a nudge.',
                  'HE1-a-b came back from Veo with white bars at the sides; it is cropped in and scaled up 18%, a little softer.',
                  'Missing clip: TR2-c (the trader over the shoulder) never animated.'],
    }
    (out / 'edl.json').write_text(json.dumps(edl, indent=1))
    print(json.dumps([(pathlib.Path(v['file']).name, round(v['start'], 3), round(v['dur'], 3)) for v in video]))


if __name__ == '__main__':
    main()
