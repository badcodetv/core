#!/usr/bin/env python3
"""Build the "Ending" reel: scenes C, D and E end to end, in the timeline format.

    python3 scripts/gpom/second-half-video/ending/reel.py

Reads <ENDING>/<C|D|E>/cut/{edl.json,preview.mp4} and writes <ENDING>/ending-reel/{edl.json,preview.mp4,mix.wav}.
Every time in each scene's edl (beats, lines, clips, events) is shifted by that scene's offset in the reel.
Joins: C -> D is a short dissolve (Maddie goes up into the light; the white changing room comes out of it),
D -> E is a hard cut, because D ends on "...Mind how" and E's phone answers "...you go." (built as a cut on sound).
The audio is the three finished scene mixes joined with the same fades, then loudness-normalised to -16 LUFS
(two-pass loudnorm, true peak -1.5). The picture is re-encoded once, clamped to legal range and tagged BT.709.
"""
import json
import pathlib
import subprocess

ENDING = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/ending')
OUT = ENDING / 'ending-reel'
SCENES = ['C', 'D', 'E']
# Crossfade INTO each scene after the first (seconds). 0 = hard cut.
# C->D 0.4 s: ends before D's first word (AI at 0.417 s) so "Suits on" is never under a fade.
XFADE = {'D': 0.4, 'E': 0.0}
FPS = 24
LUFS, TP = -16.0, -2.5  # -2.5 so the AAC preview stays under -1 dBTP (AAC overshoots ~0.9 dB)


def run(*a, capture=False):
    r = subprocess.run(list(map(str, a)), check=True, capture_output=capture, text=True)
    return r.stderr if capture else None


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    edls = {s: json.loads((ENDING / s / 'cut' / 'edl.json').read_text()) for s in SCENES}
    # Offsets, frame-snapped.
    offs, t = {}, 0.0
    for s in SCENES:
        x = XFADE.get(s, 0.0) if offs else 0.0
        offs[s] = round((t - x) * FPS) / FPS
        t = offs[s] + edls[s]['total']
    total = t

    beats, video, events, flags, tracks = [], [], [], [], {}
    for s in SCENES:
        e, o = edls[s], offs[s]
        for b in e['beats']:
            beats.append({**b, 'start': b['start'] + o, 'scene': s,
                          'lines': [{**ln, 't': (ln['t'] + o) if ln.get('t') is not None else None}
                                    for ln in b.get('lines', [])]})
        for v in e['video']:
            video.append({**v, 'start': v['start'] + o, 'scene': s})
        for ev in e['events']:
            events.append({**ev, 't': ev['t'] + o, 'scene': s})
        for a in e['audio']:
            tr = tracks.setdefault(a['name'], {'name': a['name'], 'files': []})
            tr['files'].append({'scene': s, 'file': a.get('file'), 'start': a.get('start', 0.0) + o})
        flags += [f'Scene {s}: {f}' for f in e.get('flags', [])]
    # One stem per track: voices first, then music, then sound, as the scene cuts order them.
    order = {'vox': 0, 'mus': 1, 'sfx': 2}
    audio = []
    for k, name in enumerate(sorted(tracks, key=lambda n: (order.get(n.split('-')[0], 3), n)), 1):
        audio.append({'track': f'A{k}', **tracks[name]})

    # Audio: join the finished scene mixes with the same joins, then two-pass loudnorm.
    raw = OUT / 'mix-raw.wav'
    mixes = [ENDING / s / 'cut' / 'mix.wav' for s in SCENES]
    fc, last = [], '[0:a]'
    for i, s in enumerate(SCENES[1:], 1):
        x = offs[SCENES[i - 1]] + edls[SCENES[i - 1]]['total'] - offs[s]
        lbl = f'[a{i}]'
        if x > 1e-3:
            fc.append(f'{last}[{i}:a]acrossfade=d={x:.4f}:c1=tri:c2=tri{lbl}')
        else:
            fc.append(f'{last}[{i}:a]concat=n=2:v=0:a=1{lbl}')
        last = lbl
    run('ffmpeg', '-loglevel', 'error', '-y', *sum((['-i', m] for m in mixes), []),
        '-filter_complex', ';'.join(fc), '-map', last, '-ar', 48000, '-ac', 2, '-c:a', 'pcm_s24le', raw)
    log = run('ffmpeg', '-hide_banner', '-nostats', '-i', raw, '-af',
              f'loudnorm=I={LUFS}:TP={TP}:LRA=20:print_format=json', '-f', 'null', '-', capture=True)
    m = json.loads(log[log.rindex('{'):log.rindex('}') + 1])
    mix = OUT / 'mix.wav'
    run('ffmpeg', '-loglevel', 'error', '-y', '-i', raw, '-af',
        f"loudnorm=I={LUFS}:TP={TP}:LRA=20:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
        f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true",
        '-ar', 48000, '-c:a', 'pcm_s24le', mix)
    raw.unlink()

    # Picture: xfade / concat the three previews, clamp legal, tag BT.709.
    fc, last, vt = [], '[0:v]', edls[SCENES[0]]['total']
    for i, s in enumerate(SCENES[1:], 1):
        x = vt - offs[s]
        lbl = f'[v{i}]'
        if x > 1e-3:
            fc.append(f'{last}[{i}:v]xfade=transition=fade:duration={x:.4f}:offset={offs[s]:.4f}{lbl}')
        else:
            fc.append(f'{last}[{i}:v]concat=n=2:v=1:a=0{lbl}')
        last, vt = lbl, offs[s] + edls[s]['total']
    fc.append(f'{last}fps={FPS},scale=in_range=tv:out_range=tv,lutyuv=y=clip(val\\,16\\,235):u=clip(val\\,16\\,240):'
              f'v=clip(val\\,16\\,240),format=yuv420p[vout]')
    prev = OUT / 'preview.mp4'
    run('ffmpeg', '-loglevel', 'error', '-y', *sum((['-i', ENDING / s / 'cut' / 'preview.mp4'] for s in SCENES), []),
        '-i', mix, '-filter_complex', ';'.join(fc), '-map', '[vout]', '-map', f'{len(SCENES)}:a',
        '-c:v', 'libx264', '-preset', 'slow', '-crf', 18, '-pix_fmt', 'yuv420p',
        '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
        '-c:a', 'aac', '-b:a', '256k', '-t', f'{total:.4f}', '-movflags', '+faststart', prev)

    joins = []
    for s in SCENES[1:]:
        x = XFADE.get(s, 0.0)
        joins.append(f"{s} at {offs[s]:.2f} s: " + (f'{x:.1f} s dissolve' if x else 'hard cut'))
    edl = {
        'sequence': 'gpom-second-half-ending-reel1',
        'title': 'Ending Timeline',
        'heading': 'GPOM second half · the ending · C, D and E end to end',
        'intro': ('The whole ending in one go: the walk out, the clean room and the crossing, the bus. Made '
                  'autonomously (21-22 Oct); every call Kai would make is in the flags, scene by scene. Play it, '
                  'click any beat, clip, line or sound, and leave a note in its yellow slip. Notes save as you type. '
                  "Tell Claude when you're done."),
        'fps': FPS, 'sample_rate': 48000, 'total': total,
        'scenes': [{'scene': s, 'offset': offs[s], 'dur': edls[s]['total'], 'sequence': edls[s].get('sequence'),
                    'edl': str(ENDING / s / 'cut' / 'edl.json'), 'preview': str(ENDING / s / 'cut' / 'preview.mp4'),
                    'xfade_in': XFADE.get(s, 0.0) if s != SCENES[0] else 0.0} for s in SCENES],
        'beats': beats, 'video': video, 'audio': audio, 'mix': str(mix), 'events': events,
        'flags': [
            'Reel joins: ' + '; '.join(joins) + '. C to D dissolves because Maddie goes up into the light and D opens '
            "in a white room; it ends before D's first word. D to E is a hard cut on sound: \"...Mind how\" / "
            '"...you go." was split across the cut for exactly this. **Kai to rule**.',
            f'Reel audio: the three finished scene mixes (each already -16 LUFS) joined with the same fades, then the '
            f'whole reel normalised to {LUFS:g} LUFS, true peak {TP:g} dBTP (two-pass, linear). Nothing was remixed.',
            'Reel audio tracks: one stem per track across the reel; a stem name shared by two scenes (vox-ai, '
            'sfx-room...) is one track carrying both scenes\' files.',
        ] + flags,
        'preview': str(prev),
    }
    (OUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'offsets': offs, 'beats': len(beats), 'clips': len(video),
                      'tracks': len(audio), 'events': len(events), 'loudnorm_in': m['input_i']}))


if __name__ == '__main__':
    main()
