#!/usr/bin/env python3
"""The Envelope (BadCode Short #85): rough cut (2026-11-15).

    python3 scripts/shorts/envelope_cut.py <track.wav> --voice <line.wav> [--voice-at S] [--round N] [--offset S]

9:16, four painted 1930s chapter cards (Jack's picks 01-a, 02-b, 03-b, 04-b), each with an eased push (ffmpeg stand-in;
Premiere redoes it as Scale keyframes), cut to ONE instrumental Suno track (music and sounds only; Jack 2026-11-15: no dialogue on shorts Suno tracks) with
the line in an AI Studio voice on its own stem ("only dialogue should be ai studio"). The music ducks 7 dB under the
line. The line ends 0.6 s before the end unless --voice-at says where it starts. The clips' own Omni sound is dropped.
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
    ap.add_argument('track'); ap.add_argument('--voice', required=True); ap.add_argument('--voice-at', type=float); ap.add_argument('--round', type=int, default=1); ap.add_argument('--offset', type=float, default=0.0)
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
    # The voice: trimmed to its speech (silencedetect), placed to end 0.6 s before the end, its own stem.
    voice = pathlib.Path(a.voice)
    sil = subprocess.run(['ffmpeg', '-hide_banner', '-i', voice, '-af', 'silencedetect=n=-40dB:d=0.15', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    import re
    vdur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', voice],
                                capture_output=True, text=True).stdout)
    starts_s = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', sil)]
    ends_s = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', sil)]
    sp0 = ends_s[0] if starts_s and starts_s[0] == 0 and ends_s else 0.0
    sp1 = starts_s[-1] if starts_s and len(starts_s) > len(ends_s) else vdur
    speech = round(sp1 - sp0, 3)
    vat = round(a.voice_at if a.voice_at is not None else total - 0.6 - speech, 3)
    vstem = cut / 'vox-badcode.wav'
    ff('-i', voice, '-af', f'atrim=start={sp0}:end={sp1},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={speech - 0.05}:d=0.05,'
       f'loudnorm=I=-15:TP=-1.5,adelay=delays={int(vat * 1000)}:all=1,apad=whole_dur={total},atrim=end={total}', '-ar', 48000, '-ac', 2, vstem)
    # The track: one stem from t=0, trimmed or delayed by --offset, ducked 7 dB under the line, faded out over the last 0.4 s.
    stem = cut / 'mus-track.wav'
    pre = f'atrim=start={a.offset},asetpts=PTS-STARTPTS,' if a.offset > 0 else (f'adelay=delays={int(-a.offset * 1000)}:all=1,' if a.offset < 0 else '')
    d0, d1 = vat - 0.25, vat + speech + 0.2
    duck = f"volume='if(between(t,{d0:.2f},{d1:.2f}),0.447,1)':eval=frame"
    ff('-i', track, '-af', f'{pre}apad=whole_dur={total},atrim=end={total},loudnorm=I=-16:TP=-1.5,{duck},afade=t=out:st={total - 0.4}:d=0.4',
       '-ar', 48000, '-ac', 2, stem)
    mix = cut / 'mix.wav'
    ff('-i', stem, '-i', vstem, '-filter_complex', '[0][1]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-2:LRA=11', '-ar', 48000, '-ac', 2, mix)
    ff('-i', cut / 'picture.mp4', '-i', mix, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
       '-t', total, cut / 'preview.mp4')
    beats = [{'id': s[0], 'title': s[1], 'start': starts[i], 'dur': s[4], 'see': s[8],
              'lines': ([{'i': 0, 'who': 'badcode', 'name': 'BadCode (Iapetus)', 't': vat, 'dur': speech, 'text': LINE, 'by': 'kai'}]
                        if s[0] == 'sting' else [])} for i, s in enumerate(SHOTS)]
    edl = {'sequence': f'short-the-envelope-1-the-envelope-r{a.round}', 'title': 'Envelope Timeline',
           'heading': f'BadCode Shorts ▲ The Envelope, rough cut {a.round}',
           'intro': 'Your four picked cards with light pushes, your picked music (hotclub2, instrumental) and your picked voice for the line (b, Iapetus). Note anything: a beat, a shot, the sound, or a single frame.',
           'fps': FPS, 'total': total, 'beats': beats,
           'video': [{'file': str(VID / s[2]), 'in': s[3], 'start': starts[i], 'dur': s[4], 'beat': s[0], 'source': str(VID / s[2]), 'looped': False}
                     for i, s in enumerate(SHOTS)],
           'audio': [{'track': 'A1', 'name': 'vox-badcode', 'file': str(vstem)}, {'track': 'A2', 'name': 'mus-track', 'file': str(stem)}],
           'events': [{'stem': 'vox-badcode', 't': vat, 'dur': speech, 'what': 'the line (AI Studio, Iapetus)', 'src': str(voice)},
                      {'stem': 'mus-track', 't': 0.0, 'dur': total, 'what': f'Suno track {track.stem} (offset {a.offset:+.2f} s, ducked 7 dB under the line)', 'src': str(track)}],
           'flags': ['The pushes are ffmpeg stand-ins; in Premiere they become eased Scale keyframes.',
                     f'The Suno take is {track.stem}; it runs longer than the cut and is cut off with a 0.4 s fade at the end (no re-edit to land its ending yet).']}
    (cut / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'starts': starts, 'voice_at': vat, 'speech': speech, 'preview': str(cut / 'preview.mp4'), 'edl': str(cut / 'edl.json')}))


if __name__ == '__main__':
    main()
