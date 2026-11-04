"""GPOM music-video ending, rough cut 1: the 17 locked clips over the song from 161.96s to the stop.

Page time 0 = film (sequence) time LEAD_FROM. The main track sits in the film with a 7s in-point,
so track time = film time + 7. Cut points are snapped to the song's detected beats (174 BPM).
Writes <media>/cut/edl.json (timeline format, scripts/scene/timeline.py) and <media>/cut/preview.mp4.

  python3 scripts/gpom/mv-ending/cut1.py
"""
import json, pathlib, subprocess
import librosa, numpy as np

M = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips')
SCENE = M / 'mv-ending'
CUT = SCENE / 'cut'
TRACK = M / 'gpom-main-track.mp3'
E07 = M / 'downfall/cut/e07-swindon.mp4'      # the story's last war shot, ends at film 161.96
OFFSET = 7.0                                  # track time = film time + OFFSET
LEAD_FROM, START, END = 157.96, 161.96, 230.5
TAIL = 1.0

# (beat, locked clip, source in-point, film time the shot should END near; None = END)
PLAN = [
    ('swindon', '01-me-01-SW1-a-b', 2.0, 167.5),     # Kai: drop the first 2s, open on smoke
    ('swindon', '02-me-03-SW1-c-a', 0.0, 173.0),
    ('land',    '03-me-04-LD1-d-a', 0.0, 178.1),
    ('land',    '04-me-05-LD1-c-b', 0.0, 183.2),
    ('land',    '05-me-06-LD1-b-c', 0.0, 188.4),
    ('land',    '06-me-07-LD1-e-b', 0.0, 193.5),     # the dip ~191-194
    ('sky',     '07-me-08-SK1-b-b', 0.0, 196.3),
    ('sky',     '08-me-09-SK1-d-a', 0.0, 199.1),
    ('sky',     '09-me-10-SK1-a-a', 0.0, 201.8),
    ('country', '10-me-11-CT2-h-a', 0.0, 203.7),     # the cutting speeds up as the scale climbs
    ('country', '11-me-12-CT2-d-b', 0.0, 205.6),
    ('country', '12-me-14-CT2-a-a', 0.0, 207.5),
    ('country', '13-me-15-CT2-b-b', 0.0, 209.4),     # the music drops out ~209: into space
    ('orbit',   '14-me-16-OR1-c-a', 0.0, 214.6),     # the last drop lands ~214.6
    ('orbit',   '15-me-17-r2-OR1-a-b', 0.0, 218.6),  # Kai: cut ~4s, before the red fades
    ('orbit',   '16-me-18-r2e-OR3-a-a', 0.0, 224.5),
    ('orbit',   '17-me-20-r3d-OR4-a-b', 0.0, None),
]
BEATS = [
    ('lead', 'Lead-in: the story\'s last shot', 'e07, the Swindon sign and the explosion, as it ends the war scene in the film.'),
    ('swindon', 'Out of Swindon', 'Out of the explosion into night: the robes march over the wreckage, the eye lit above.'),
    ('land', 'The land', 'The army fills Britain: motorways, valleys, empty towns, rows past the horizon.'),
    ('sky', 'The sky', 'Fleets of ships, layer on layer, a weather system over England at night.'),
    ('country', 'The country', 'Whole cities, counties and coastlines from airliner height, red. Cut faster as the scale climbs.'),
    ('orbit', 'Orbit', 'The satellite; Earth turns red beneath it; pull back past the Moon; Earth alone in black.'),
]


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


def beat_grid():
    y, sr = librosa.load(TRACK, sr=22050, offset=LEAD_FROM + OFFSET - 4, duration=END - LEAD_FROM + 8)
    _, fr = librosa.beat.beat_track(y=y, sr=sr, start_bpm=174, tightness=400)
    return librosa.frames_to_time(fr, sr=sr) + LEAD_FROM - 4


def main():
    CUT.mkdir(parents=True, exist_ok=True)
    seg = CUT / 'seg'
    seg.mkdir(exist_ok=True)
    grid = beat_grid()
    snap = lambda t: float(grid[np.abs(grid - t).argmin()])
    rel = lambda t: round(t - LEAD_FROM, 3)
    vf = 'scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,fps=24,format=yuv420p'

    video, parts = [], []
    lead = START - LEAD_FROM
    p = seg / '00-lead.mp4'
    ff('-ss', 6.0 - lead, '-t', lead, '-i', E07, '-an', '-vf', vf, '-c:v', 'libx264', '-crf', '18', p)
    video.append({'file': str(p), 'source': str(E07), 'start': 0.0, 'dur': lead, 'beat': 'lead', 'in': 6.0 - lead})
    parts.append(p)

    t = START
    for i, (beat, name, src_in, end) in enumerate(PLAN, 1):
        e = END if end is None else snap(end)
        dur = round(e - t, 3)
        src = SCENE / 'locked' / f'{name}.mp4'
        assert src_in + dur <= 8.04, (name, dur)
        p = seg / f'{i:02d}-{name}.mp4'
        ff('-ss', src_in, '-t', dur, '-i', src, '-an', '-vf', vf, '-c:v', 'libx264', '-crf', '18', p)
        video.append({'file': str(p), 'source': str(src), 'start': rel(t), 'dur': dur, 'beat': beat, 'in': src_in})
        parts.append(p)
        t = e

    total = round(END + TAIL - LEAD_FROM, 3)
    lst = seg / 'list.txt'
    lst.write_text(''.join(f"file '{q}'\n" for q in parts))
    pic = seg / 'picture.mp4'
    ff('-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', pic)
    stem = CUT / 'stems'
    stem.mkdir(exist_ok=True)
    mus = stem / 'mus-track.wav'
    ff('-ss', LEAD_FROM + OFFSET, '-t', total, '-i', TRACK, '-af', f'afade=t=out:st={total - 0.8}:d=0.8', mus)
    ff('-i', pic, '-i', mus, '-vf', 'tpad=stop_mode=add:stop_duration=2:color=black', '-t', total,
       '-c:v', 'libx264', '-crf', '20', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart',
       CUT / 'preview.mp4')

    beats = []
    for bid, title, see in BEATS:
        vs = [v for v in video if v['beat'] == bid]
        b0 = vs[0]['start']
        film = LEAD_FROM + b0
        beats.append({'id': bid, 'title': f'{title} · film {int(film // 60)}:{film % 60:05.2f}', 'start': b0,
                      'dur': round(sum(v['dur'] for v in vs), 3), 'see': see, 'lines': []})
    edl = {
        'sequence': 'gpom-mv-ending-rough1', 'title': 'GPOM Ending Timeline',
        'heading': 'GitPush Origin Master ▲ music-video ending, rough cut 1',
        'intro': (f'The music-video ending, cut to the song. The page starts 4s early (page 0:00 = film '
                  f'{int(LEAD_FROM // 60)}:{LEAD_FROM % 60:05.2f}) so you see the cut out of the story\'s last war shot; '
                  'the ending proper starts at page 0:04 (film 2:41.96). Cuts sit on the beat. Click any beat, clip or the '
                  'track and leave a note in its yellow slip, or pin one to a frame. Tell Claude when you\'re done.'),
        'fps': 24, 'total': total, 'beats': beats, 'video': video,
        'audio': [{'track': 'A1', 'name': 'mus-track'}],
        'events': [{'stem': 'mus-track', 't': 0.0, 'dur': total, 'what': f'main track, track time {LEAD_FROM + OFFSET:.2f} to the end',
                    'src': str(TRACK)}],
        'flags': [
            'The lead-in uses the last 4s of e07-swindon.mp4; where it sits in your Premiere cut was not re-read, so the cut point is approximate.',
            'Section changes (from loudness, not listened to): dips at ~171, ~191-194, ~209-214; the last drop ~214.6; the song stops ~230.',
            'Shot 01 starts 2s in (your note); shot 17 is cut at 4s (your note). Every other clip starts at its first frame.',
        ],
        'round': 1,
    }
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    # The Premiere edl: the ending alone (no lead-in), 0 = film START, original clips with handles,
    # the song from track time START+OFFSET to its natural end (no fade), so it follows the opening directly.
    shift = START - LEAD_FROM
    mus_p = stem / 'mus-track-ending.wav'
    ff('-ss', START + OFFSET, '-i', TRACK, '-c:a', 'pcm_s24le', mus_p)
    pv = [{**v, 'file': v['source'], 'start': round(v['start'] - shift, 3)} for v in video if v['beat'] != 'lead']
    ped = {**edl, 'sequence': 'gpom-1b-mv-ending-r1', 'total': round(END - START, 3), 'video': pv,
           'audio': [{'track': 'A1', 'name': 'mus-track', 'file': str(mus_p)}],
           'events': [{'stem': 'mus-track', 't': 0.0, 'dur': round(END - START, 3), 'what': 'main track from film 161.96',
                       'src': str(TRACK)}]}
    (CUT / 'edl-premiere.json').write_text(json.dumps(ped, indent=1, ensure_ascii=False))
    for v in video:
        print(f"{v['start']:7.2f} {v['dur']:5.2f}  {pathlib.Path(v['source']).name}")
    print('total', total)


if __name__ == '__main__':
    main()
