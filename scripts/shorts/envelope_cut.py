#!/usr/bin/env python3
"""The Envelope (BadCode Short #85): rough cut (2026-11-15).

    python3 scripts/shorts/envelope_cut.py <track.wav|mp3> [--round N] [--offset S]

9:16, four painted 1930s chapter cards (Jack's picks 01-a, 02-b, 03-b, 04-b), each with an eased push (ffmpeg stand-in;
Premiere redoes it as Scale keyframes), cut to ONE Suno track that carries the spoken line, the stings and the music
(Kai's rule for shorts, 2026-11-13). The clips' own Omni sound is dropped. --offset starts the track later or earlier.
Writes <media>/cut/r<N>/edl.json (timeline format, scripts/scene/timeline.py), stems and preview.mp4.
"""
# style-lint: story=short-the-envelope (this cut script belongs to one short)
import argparse, json, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parents[2]
SCENE = REPO / 'docs/stories/short-the-envelope/scenes/the-envelope'
sys.path.insert(0, str(REPO / 'scripts/drive'))
from localmap import localize  # noqa: E402

cfg = localize(json.loads((SCENE / 'scene.json').read_text()))
MEDIA = pathlib.Path(cfg['media'])
VID = MEDIA / 'video'
W, H, FPS = 1080, 1920, 24
LINE = cfg['line']

# (beat, title, clip, in, dur, zoom_to, focus_x, focus_y, what we see)
SHOTS = [('setup', 'S1. The Counter', 'en-01-SU2-b.mp4', 1.5, 3.5, 1.06, 0.5, 0.62,
          'The dealer lays the two envelopes on the counter and smiles: even odds.'),
         ('pick', 'S2. The Pick', 'en-02-b-PK2-b.mp4', 1.0, 3.5, 1.06, 0.55, 0.6,
          'The old man wavers between the two envelopes; the dealer waits, palms open.'),
         ('switch', 'S3. The Switch', 'en-03-b-SW4-c.mp4', 0.5, 3.5, 1.06, 0.5, 0.6,
          'Both bowler hats tip towards us; under them, the one crate, ORDER No. 0417, and the fresh money.'),
         ('sting', 'S4. The Pay-off', 'en-04-b-SG4-b.mp4', 0.5, 4.5, 1.08, 0.62, 0.55,
          'BadCode holds the curtain; the blue tie and the red tie turn round, caught. EVERYTHING ELSE IS A DISTRACTION.')]


def ff(*a):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *map(str, a)], check=True)


ENC = ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-color_range', 'tv',
       '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('track'); ap.add_argument('--round', type=int, default=1); ap.add_argument('--offset', type=float, default=0.0)
    a = ap.parse_args()
    track = pathlib.Path(a.track)
    cut = MEDIA / 'cut' / f'r{a.round}'; cut.mkdir(parents=True, exist_ok=True)
    starts, t = [], 0.0
    for s in SHOTS: starts.append(round(t, 3)); t += s[4]
    total = round(t, 3)
    parts = []
    for i, (beat, _, clip, tin, d, z, fx, fy, _) in enumerate(SHOTS):
        n = int(round(d * FPS))
        zexpr = f"1+({z}-1)*(3*pow(on/{n},2)-2*pow(on/{n},3))"
        out = cut / f'v{i}-{beat}.mp4'
        ff('-ss', tin, '-t', d, '-i', VID / clip, '-an', '-vf',
           f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},'
           f"zoompan=z='{zexpr}':x='{fx}*iw-iw/zoom/2':y='{fy}*ih-ih/zoom/2':d=1:s={W}x{H}:fps={FPS},"
           'scale=in_range=full:out_range=limited,format=yuv420p', *ENC, out)
        parts.append(out)
    (cut / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    ff('-f', 'concat', '-safe', '0', '-i', cut / 'list.txt', '-c', 'copy', cut / 'picture.mp4')
    # The track: one stem from t=0, trimmed or delayed by --offset, faded out over the last 0.4 s, normalised for a short.
    stem = cut / 'mus-track.wav'
    pre = f'atrim=start={a.offset},asetpts=PTS-STARTPTS,' if a.offset > 0 else (f'adelay=delays={int(-a.offset * 1000)}:all=1,' if a.offset < 0 else '')
    ff('-i', track, '-af', f'{pre}apad=whole_dur={total},atrim=end={total},afade=t=out:st={total - 0.4}:d=0.4,loudnorm=I=-14:TP=-1.5',
       '-ar', 48000, '-ac', 2, stem)
    ff('-i', cut / 'picture.mp4', '-i', stem, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
       '-t', total, cut / 'preview.mp4')
    beats = [{'id': s[0], 'title': s[1], 'start': starts[i], 'dur': s[4], 'see': s[8],
              'lines': ([{'i': 0, 'who': 'badcode', 'name': 'BadCode', 't': None, 'dur': 0, 'text': LINE, 'by': 'kai'}]
                        if s[0] == 'sting' else [])} for i, s in enumerate(SHOTS)]
    edl = {'sequence': f'short-the-envelope-1-the-envelope-r{a.round}', 'title': 'Envelope Timeline',
           'heading': f'BadCode Shorts ▲ The Envelope, rough cut {a.round}',
           'intro': 'Your four picked cards with light pushes, cut to one Suno track (line, stings and music in one). Note anything: a beat, a shot, the sound, or a single frame.',
           'fps': FPS, 'total': total, 'beats': beats,
           'video': [{'file': str(VID / s[2]), 'in': s[3], 'start': starts[i], 'dur': s[4], 'beat': s[0], 'source': str(VID / s[2]), 'looped': False}
                     for i, s in enumerate(SHOTS)],
           'audio': [{'track': 'A1', 'name': 'mus-track', 'file': str(stem)}],
           'events': [{'stem': 'mus-track', 't': 0.0, 'dur': total, 'what': f'Suno track {track.stem} (offset {a.offset:+.2f} s)', 'src': str(track)}],
           'flags': ['The pushes are ffmpeg stand-ins; in Premiere they become eased Scale keyframes.',
                     'The line, the stings and the music are one Suno track; the line is where Suno put it, not placed by hand.']}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'starts': starts, 'preview': str(cut / 'preview.mp4'), 'edl': str(cut / 'edl.json')}))


if __name__ == '__main__':
    main()
