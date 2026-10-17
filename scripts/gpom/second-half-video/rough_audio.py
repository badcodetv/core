#!/usr/bin/env python3
"""Prepare every sound for the second half's rough cut, and say where each one goes.

Reads rough-cut.json (timing.py + extend.py) and writes clips/second-half/audio/rough/*.wav plus an
`audio` list in rough-cut.json: [file, t, track, what]. Tracks: 0 narrator · 1 dialogue · 2 crowd ·
3 music. Everything is pre-mixed here (levels, fades, the duck under Maddie's call) because
Premiere has no audio-transition API, so each clip lands ready and stays movable in the edit.

Music takes are the rough-cut picks (weirdness 30, length closest to target), not Kai's: nobody
has listened yet. Recorded preview copies from suno-recordings/ (suno.mts record).

    python3 scripts/gpom/second-half-video/rough_audio.py
"""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import shots as S  # noqa: E402

RC = S.CLIPS / 'audio' / 'rough-cut.json'
VOICE = S.CLIPS / 'audio' / 'voice' / 'trim'
OUT = S.CLIPS / 'audio' / 'rough'
REC = pathlib.Path('/mnt/c/Users/kai/Desktop/suno-recordings')
MUSIC = {
    'HUNDRED': REC / 'gpom-sh2-hundred-a-v6-w30-d221a26b.wav',
    'S1': REC / 'gpom-sh2-s1-a-v6-w30-805b38c7.wav',
    'S3': REC / 'gpom-sh2-s3-a-v6-w30-fca27332.wav',
    'S4': REC / 'gpom-sh2-s4-a-v6-w30-88a66171.wav',
    'S5': REC / 'gpom-sh2-s5-a-v6-w30-2b7bee8a.wav',
    'S2': S.CLIPS.parent / 'gpom-main-track.mp3',
}
DROP = 70.3  # the drum & bass drop, seconds into gpom-main-track.mp3 (RMS -15 -> -11 dB at 70.5)
AR = ['-ar', '48000', '-ac', '2']

rc = json.loads(RC.read_text())
start = {}
for c in rc['clips']:
    start.setdefault(c[4], c[1])
end = rc['total']


def ff(args, out):
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *args, *AR, str(out)], check=True)
    return out.name


audio = []
OUT.mkdir(parents=True, exist_ok=True)

# Voices: one loudness for all; the AI in-scene through a small speaker; the row in a tiled room.
for key, fname, t, d, track in rc['voices']:
    who = key.split('-', 2)[2]
    chain = []
    if who == 'ai':
        chain.append('highpass=f=380,lowpass=f=3600,acompressor=threshold=-20dB:ratio=4,volume=2')
    if who in ('woman', 'man') and key[:2] in ('06', '07', '13'):
        chain.append('aecho=0.8:0.5:35|60:0.22|0.12')
    chain.append('loudnorm=I=-16:TP=-1.5:LRA=11' if not who.startswith('crowd') else 'loudnorm=I=-21:TP=-2')
    name = ff(['-i', str(VOICE / fname), '-af', ','.join(chain)], OUT / f'v-{key}.wav')
    audio.append([name, t, 0 if who == 'narrator' else (2 if who.startswith('crowd') else 1), key])


def cue(name, src, at, length, src_in=0.0, lufs=-24, fade_in=0.3, fade_out=1.0, extra=''):
    af = f'atrim=start={src_in}:duration={length},asetpts=PTS-STARTPTS,loudnorm=I={lufs}:TP=-2'
    if fade_in:
        af += f',afade=t=in:d={fade_in}'
    if fade_out:
        af += f',afade=t=out:st={max(0, length - fade_out)}:d={fade_out}'
    if extra:
        af += ',' + extra
    audio.append([ff(['-i', str(src), '-af', af], OUT / f'm-{name}.wav'), round(at, 3), 3, name])


# S1 the hunt: from the top, stops dead on the first ping (frame 4).
cue('S1-hunt', MUSIC['S1'], 0, start[4] - 0, lufs=-22, fade_in=1.0, fade_out=0.05)
# R the bunker radio: the hymn, tinny, in the room, over frame 5.
cue('R-radio', MUSIC['HUNDRED'], start[5], start[6] - start[5], src_in=4, lufs=-32, fade_in=0.5, fade_out=0.05,
    extra='highpass=f=500,lowpass=f=3000')
# S2 kill mode: the track's drop on KILL MODE ENGAGED, ducked under Maddie's call, dead on the gate.
s2 = start[12] + 0.6 - start[8]
duck_a, duck_b = start[11] - start[8], start[12] - start[8]
cue('S2-kill', MUSIC['S2'], start[8], s2, src_in=DROP, lufs=-15, fade_in=0, fade_out=0.05,
    extra=f"volume='if(between(t,{duck_a:.2f},{duck_b:.2f}),0.28,1)':eval=frame")
# S3 the meeting: enters after "Hello", out under the revolt line.
hello = next(a for a in audio if a[3].startswith('15-'))
s3_at = hello[1] + 1.4
cue('S3-meeting', MUSIC['S3'], s3_at, start[18] + 1.0 - s3_at, lufs=-27, fade_in=2.0, fade_out=1.5)
# S4 the crossing: the walk out to the hands, stops dead on the bot alone (frame 27).
s4_len = start[27] - start[19]
cue('S4-crossing', MUSIC['S4'], start[19], s4_len, src_in=max(0, 46.4 - s4_len - 0.5), lufs=-22, fade_in=1.5, fade_out=0.05)
# S5 coda: lands so the take's last moment (the drum hit) falls just after the final line.
last = max(a for a in audio if a[3].startswith('29-'))
s5_len = 14.68
s5_end = last[1] + 4.6
cue('S5-coda', MUSIC['S5'], max(start[28], s5_end - s5_len), min(s5_len, s5_end - start[28]),
    src_in=max(0, s5_len - (s5_end - start[28])), lufs=-22, fade_in=1.0, fade_out=0)

rc['audio'] = audio
RC.write_text(json.dumps(rc, indent=1))
for a in sorted(audio, key=lambda a: a[1]):
    print(f'{a[1]:7.2f}  A{a[2] + 1}  {a[0]}')
