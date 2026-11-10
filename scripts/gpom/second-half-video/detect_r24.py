#!/usr/bin/env python3
"""GPOM scene A: the "kill bot detects the row" bridge between the lavatory row (ends 182.42 s in cut3/A-d21)
and cut3-V8 (the pack racing down the motorway). Kai's picks (feedback/detect-picks-r24): VENT c, then TURRET c
(lamp recoloured white), then HUD a.

    python3 scripts/gpom/second-half-video/detect_r24.py              # round 24 (Kai at4401): 1 + 1 + 1 s
    python3 scripts/gpom/second-half-video/detect_r24.py --round 25   # round 25 (Kai at5176): 1 + 2 + 2 s; the HUD's
                                                                      # status line reads CONTACT // LOCK at the lock

Writes into /mnt/d/badcode-videos/gitpush-origin-master/clips/second-half/cut3/detect-r<round>/:
  video/   the three shots, 1280x720 24 fps, silent
  audio/   the row bed (muffled, then the bot's feed), each sfx placed, and bridge-mix.wav
  detect-spec.json, preview-detect.mp4 (the bridge with its mix), preview-context.mp4 (the last 3 s of the row,
  the bridge, the first 3 s of V8, from the A-d21 preview)
Times in the spec are bridge-relative: 0.0 = the cut point after the row (182.42 s in A-d21). Both rounds cut from
the same two Flow takes in cut3/detect-r24/raw/ (no new Flow video for round 25).
"""
import argparse
import json
import pathlib
import subprocess

D = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/second-half')
RAW = D / 'cut3/detect-r24/raw'   # the Flow takes (both rounds cut from these)
A21 = D / 'cut3/A-d21'
SFX = D / 'audio/sfx'
STILL = D / 'storyboard/detect/work'
HUD_PY = pathlib.Path(__file__).resolve().parent / 'hud.py'
CUT_AT = 182.41666666666666   # A-d21: cut3-lip-7d-1 ends, cut3-V8 starts
SR = 48000
TAIL = 0.6                    # the row's feed runs on under V8 and fades
ENC = ['-r', '24', '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p',
       '-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']

# the row under the bridge starts on the dry vox stems at 171.5 s (Derek's 7d-0 tail over Sandra's "Five years
# underground, and you still can't put a seat down", then Derek's 7d-1), muffled past recognition
ROW_FROM = 171.5

# per round: shot lengths, in-points, where the turret's jolt lands in its shot, the HUD's lock time
ROUNDS = {
    24: dict(vent=(0.60, 1.0), turret=(0.25, 1.0), hud=1.0, jolt=0.35, lock=0.3, lock_status=None,
             note='Kai at4401: picks vent c, turret c, HUD a, ~1 s each'),
    25: dict(vent=(0.60, 1.0), turret=(0.10, 2.0), hud=2.0, jolt=0.50, lock=0.5, lock_status='CONTACT  //  LOCK',
             note="Kai at5176: 'spend a little bit longer on this … a whole new second', and longer on the HUD"),
}


def run(cmd):
    subprocess.run([str(c) for c in cmd], check=True)


def ff(*a):
    run(['ffmpeg', '-v', 'error', '-y', *a])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--round', type=int, default=24, choices=sorted(ROUNDS))
    R = ROUNDS[ap.parse_args().round]
    rnd = ap.parse_args().round
    OUT = D / f'cut3/detect-r{rnd}'
    for sub in ('video', 'audio', 'work'):
        (OUT / sub).mkdir(parents=True, exist_ok=True)
    W, AU = OUT / 'work', OUT / 'audio'

    (vi, vd), (ti, td), hd = R['vent'], R['turret'], R['hud']
    T_TUR, T_HUD = vd, vd + td            # bridge times the turret and the HUD start
    TOTAL = vd + td + hd
    BED = TOTAL + TAIL
    LOCK = R['lock']
    shots = [
        dict(id='vent', src=RAW / 'detect-vent-t1.mp4', i=vi, d=vd, at=0.0, plate=STILL / 'vent-p2-a.jpg',
             what='VENT c: the grille on the down; a warm breath shimmers out, the cobweb trembles (the row is under it)'),
        dict(id='turret', src=RAW / 'detect-turret-t1.mp4', i=ti, d=td, at=T_TUR, plate=STILL / 'turret-p2-b-white.jpg',
             what=f'TURRET c (white lamp): the turret jolts, the lamp flares, the lenses snap focus (jolt {R["jolt"]:.2f} s in)'
                  + (', then it holds, staring' if td > 1.0 else '')),
        dict(id='hud', src=None, i=0.0, d=hd, at=T_HUD, plate=STILL / 'hud-p1-a.jpg',
             what=f"HUD a: KB-07's view down the motorway, teal PATROL; SIGNAL SEARCH, then ORGANIC SIGNAL - LOCK at "
                  f"{LOCK} s" + (f" and the status line turns to {R['lock_status'].replace('  ', ' ')}" if R['lock_status'] else '')
                  + '; the meter is the row'),
    ]

    # --- the row bed: the dry stems, two treatments
    ff('-ss', ROW_FROM, '-t', BED, '-i', A21 / 'stems/02-vox-derek.wav', '-ss', ROW_FROM, '-t', BED, '-i',
       A21 / 'stems/04-vox-sandra.wav',
       '-filter_complex', f'[0][1]amix=inputs=2:normalize=0,aresample={SR},pan=mono|c0=c0', W / 'row-dry.wav')
    # through rock and a vent: dark, roomy, low
    ff('-i', W / 'row-dry.wav', '-af', 'highpass=f=110,lowpass=f=420,lowpass=f=420,aecho=0.8:0.5:35|60:0.35|0.2,volume=6dB',
       W / 'row-muffled.wav')
    # the bot's audio feed: band-limited, a little crushed, clearer than through the rock
    ff('-i', W / 'row-dry.wav', '-af', 'highpass=f=320,lowpass=f=2600,acrusher=bits=10:mix=0.35,volume=-2dB',
       W / 'row-feed.wav')
    # bed: muffled until the HUD, 60 ms crossfade into the feed, the feed runs TAIL s past the cut and fades
    ff('-i', W / 'row-muffled.wav', '-i', W / 'row-feed.wav', '-filter_complex',
       f'[0]atrim=0:{T_HUD + 0.06},asetpts=N/SR/TB[a];[1]atrim={T_HUD}:{BED},asetpts=N/SR/TB[b];'
       f'[a][b]acrossfade=d=0.06:c1=tri:c2=tri,afade=t=out:st={TOTAL + 0.1}:d={TAIL - 0.1}', AU / 'row-bed.wav')
    # the HUD meter reads the feed from the HUD's start
    ff('-ss', T_HUD, '-i', W / 'row-feed.wav', '-t', hd + TAIL, W / 'hud-meter.wav')

    # --- sfx, each a bridge-length (BED) track with its event placed
    def place(name, src_args, at, chain=''):
        ff(*src_args, '-af', f'{chain}{"," if chain else ""}aresample={SR},pan=mono|c0=c0,adelay={int(at * 1000)},'
           f'apad=whole_dur={BED},atrim=0:{BED}', AU / f'sfx-{name}.wav')
    # vent: a low mains hum with a little air (ffmpeg synth)
    place('vent-hum', ['-f', 'lavfi', '-i',
                       'aevalsrc=0.30*sin(2*PI*50*t)+0.16*sin(2*PI*100*t)+0.07*sin(2*PI*150*t)+0.03*sin(2*PI*250*t):'
                       f's={SR}:d={vd + 0.25}'], 0.0,
          f'afade=t=in:d=0.08,afade=t=out:st={vd}:d=0.25,volume=-14dB')
    place('vent-air', ['-ss', 2, '-t', vd + 0.25, '-i', SFX / 'synth-cctv-hiss-20s.wav'], 0.0,
          f'lowpass=f=900,afade=t=in:d=0.1,afade=t=out:st={vd}:d=0.25,volume=-12dB')
    # turret: servo whir (fs824121, CC0, the burst at 15.55 s) on the jolt, then a lens click (synth)
    j = T_TUR + R['jolt']
    place('turret-servo', ['-ss', 15.55, '-t', 0.5, '-i', SFX / 'fs824121-killbot-servo.mp3'], j - 0.05,
          'asetrate=44100*0.85,aresample=44100,afade=t=out:st=0.35:d=0.15,volume=-4dB')
    place('turret-click', ['-f', 'lavfi', '-i', f'anoisesrc=d=0.03:c=white:a=0.9:r={SR}'], j + 0.17,
          'highpass=f=2500,afade=t=out:d=0.03,volume=-6dB')
    # HUD: the lock blip at the lock, CCTV hiss under the whole HUD shot
    place('hud-blip', ['-i', SFX / 'synth-hud-blip.wav'], T_HUD + LOCK, 'volume=-6dB')
    place('hud-blip2', ['-i', SFX / 'synth-hud-blip.wav'], T_HUD + LOCK + 0.12, 'volume=-9dB')
    place('hud-hiss', ['-ss', 5, '-t', hd + 0.1, '-i', SFX / 'synth-cctv-hiss-20s.wav'], T_HUD,
          f'afade=t=in:d=0.03,afade=t=out:st={hd - 0.1}:d=0.2,volume=-18dB')
    sfx = [
        ('vent-hum', 0.0, 'vent hum (ffmpeg synth 50 Hz + harmonics)'),
        ('vent-air', 0.0, 'air through the grille (synth hiss, low-passed)'),
        ('turret-servo', round(j - 0.05, 3), 'servo whir on the jolt (fs824121, CC0, derjuli)'),
        ('turret-click', round(j + 0.17, 3), 'lens click as the focus snaps (synth)'),
        ('hud-blip', round(T_HUD + LOCK, 3), 'lock blip (synth-hud-blip)'),
        ('hud-blip2', round(T_HUD + LOCK + 0.12, 3), 'second blip, quieter'),
        ('hud-hiss', T_HUD, 'feed hiss under the HUD (synth-cctv-hiss)'),
    ]

    # --- pictures
    v = {}
    for s in shots[:2]:
        out = OUT / 'video' / f'detect-{s["id"]}.mp4'
        ff('-ss', s['i'], '-i', s['src'], '-t', s['d'], '-an', '-vf', 'scale=1280:720,fps=24', *ENC, out)
        v[s['id']] = out
    # HUD a: the still with a barely-there push (1.000 -> 1.006 per second) and moving grain, then hud.py over it
    plate = W / 'hud-plate.mp4'
    pl = hd + TAIL
    frames = int(round(pl * 24))
    ff('-loop', 1, '-i', STILL / 'hud-p1-a.jpg', '-t', pl, '-vf',
       f"scale=2560:1440,zoompan=z='1+{0.012 * pl / 1.6:.4f}*on/{frames}':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d=1:"
       f's=1280x720:fps=24,noise=alls=6:allf=t', *ENC, plate)
    hud_full = W / 'hud-full.mp4'
    hud_cmd = ['python3', HUD_PY, plate, hud_full, '--state', 'patrol', '--audio', W / 'hud-meter.wav', '--lock', str(LOCK),
               '--no-audio-out']
    if R['lock_status']:
        hud_cmd += ['--lock-status', R['lock_status']]
    run(hud_cmd)
    v['hud'] = OUT / 'video/detect-hud.mp4'
    ff('-i', hud_full, '-t', hd, '-an', *ENC, v['hud'])

    # --- mix and previews
    tracks = ['row-bed'] + [f'sfx-{n}' for n, _, _ in sfx]
    ins = sum([['-i', AU / f'{t}.wav'] for t in tracks], [])
    ff(*ins, '-filter_complex', f'amix=inputs={len(tracks)}:normalize=0,alimiter=limit=0.89,atrim=0:{TOTAL}',
       AU / 'bridge-mix.wav')
    lst = W / 'concat.txt'
    lst.write_text(''.join(f"file '{v[k]}'\n" for k in ('vent', 'turret', 'hud')))
    ff('-f', 'concat', '-safe', 0, '-i', lst, '-i', AU / 'bridge-mix.wav', '-map', '0:v', '-map', '1:a', *ENC,
       '-c:a', 'aac', '-b:a', '192k', '-shortest', OUT / 'preview-detect.mp4')
    # in context: 3 s of the row, the bridge, 3 s of V8 (both from the A-d21 preview, with its mix)
    ff('-ss', CUT_AT - 3, '-t', 3, '-i', A21 / 'preview.mp4', '-i', OUT / 'preview-detect.mp4',
       '-ss', CUT_AT, '-t', 3, '-i', A21 / 'preview.mp4', '-filter_complex',
       '[0:v]scale=1280:720,fps=24,setsar=1[v0];[1:v]setsar=1[v1];[2:v]scale=1280:720,fps=24,setsar=1[v2];'
       f'[0:a]aresample={SR}[a0];[1:a]aresample={SR}[a1];[2:a]aresample={SR}[a2];'
       '[v0][a0][v1][a1][v2][a2]concat=n=3:v=1:a=1[v][a]', '-map', '[v]', '-map', '[a]', *ENC, '-c:a', 'aac',
       '-b:a', '192k', OUT / 'preview-context.mp4')

    spec = {
        'what': f'GPOM A round {rnd}: the bridge between the lavatory row and cut3-V8. A kill bot hears the row.',
        'round': rnd,
        'note': R['note'],
        'picks': 'feedback/detect-picks-r24 (vent c, turret c, HUD a)',
        'insert_at': {'edl': str(A21 / 'edl.json'), 'after': 'cut3-lip-7d-1 (beat 7)', 'before': 'cut3-V8 (beat 9a)',
                      'cut_point_s': CUT_AT, 'adds_s': TOTAL},
        'shots': [
            {'id': s['id'], 'file': str(v[s['id']]), 'source': str(s['src'] or hud_full), 'in': s['i'], 'dur': s['d'],
             'at': s['at'], 'plate': str(s['plate']), 'what': s['what']} for s in shots],
        'audio': {
            'row-bed': {'file': str(AU / 'row-bed.wav'), 'at': 0.0, 'dur': BED,
                        'what': f'the row continues: dry vox stems {ROW_FROM}-{ROW_FROM + BED:.1f} s of A-d21, muffled through '
                                f"rock to {T_HUD} s, then the bot's band-limited feed under the HUD; {TAIL} s tail fades under V8"},
            'sfx': [{'file': str(AU / f'sfx-{n}.wav'), 'at': at, 'what': w} for n, at, w in sfx],
            'note': f'every sfx file is already padded to {BED} s with its event at the "at" time, so lay each at bridge 0.0',
            'mix': str(AU / 'bridge-mix.wav'),
        },
        'previews': {'bridge': str(OUT / 'preview-detect.mp4'), 'in_context': str(OUT / 'preview-context.mp4')},
        'rebuild': f'python3 scripts/gpom/second-half-video/detect_r24.py --round {rnd}',
    }
    spec['shots'][2]['hud'] = (f'hud.py --state patrol --lock {LOCK}'
                               + (f" --lock-status '{R['lock_status']}'" if R['lock_status'] else '')
                               + f', meter = work/row-feed from bridge {T_HUD} s')
    (OUT / 'detect-spec.json').write_text(json.dumps(spec, indent=1))
    print(json.dumps({'spec': str(OUT / 'detect-spec.json'), 'preview': str(OUT / 'preview-detect.mp4'), 'total': TOTAL}))


if __name__ == '__main__':
    main()
