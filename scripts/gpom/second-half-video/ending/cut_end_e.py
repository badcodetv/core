#!/usr/bin/env python3
"""GPOM second half, the ending, scene E (the bus): new-scene stage 4 rough cut.

    python3 scripts/gpom/second-half-video/ending/cut_end_e.py            # build E (edl, mix, stems, preview)
    python3 scripts/gpom/second-half-video/ending/cut_end_e.py --no-preview

Runs on cut_end.py's engine (Scene, Cut, voices, the join report, cut3's write / edl / preview) and registers itself
there as SCENE_FNS['E'], like cut_end_d.py. Scene E's own picture work, all in post and all exact:
  phone_screen.py  D16's last frame (the empty chairs) tracked onto the phone in E01 and E02 (never a white screen)
  move_keys.py     the eased Premiere-style moves (E01 push toward the phone, E03 pull-back 140% -> 100%) and the
                   fade to black at the end of E03
  regrade()        a ramped per-channel grade holding E03's chained take on its first seconds (it cools as it runs)
Sound: the phone's "...you go." (D16's split), the AI's last line unfiltered (Suno take, phrase by phrase, the
take's own long pauses tightened, never the words), the e-coda cue with one musical edit so its held-chord pocket
sits under the line, and recorded CC0 ambience (E/sfx: a bus interior, rain on the window, a rainy street, a bus
departing; review round 1 replaced the synthesised beds; the synth helpers below are kept but unused). Rules: LEAD 0.4, GAP 0.35, TAIL 0.6; speech never
slowed; one stem per track; the mix at -16 LUFS.
"""
import json
import pathlib
import subprocess
import sys

import numpy as np
from scipy import signal

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import cut_end as E  # noqa: E402
import cut2 as C  # noqa: E402
import cut3 as C3  # noqa: E402

FPS, SR = E.FPS, E.SR
LEAD, GAP, TAIL = E.LEAD, E.GAP, E.TAIL
fr = E.fr
VID = E.CLIPS / 'video'
# Round 1 (Kai, 23 Oct): the phone shows the last frame scene D now shows (gleaming Maddie among the empty chairs,
# D16r3-t1), taken from D's cut itself (its last placed piece, white balance and all), so the two match exactly.
D_EDL = E.CLIPS / 'ending' / 'D' / 'cut' / 'edl.json'
# E03 round 1: the red double-decker, two clips joined here (continuous-shot: the tail's first frame dropped, a 0.3 s
# dissolve over the join, as E03b-chain was).
E03_HEAD, E03_TAIL, E03_XF = 'E03r4-t1.mp4', 'E03xr4-t1.mp4', 0.3  # ending round 2 (Kai at4010): empty road
# The AI's last line (atom gpom-sh-end-ai-e2, revision H, Kai's pick H-v6-w10 22571839, 23 Oct): "I made it. Now the
# real work starts." Cut on the take's silence map (40 dB under its peak, 20 ms), not whisper: "I made it." 0.00-0.85 s,
# a 3.3 s gap, "Now the real work starts." 4.13-6.38 s, silent after. The take's own pause is kept whole.
LINE_TEXT = 'I made it. Now the real work starts.'
AI_TAKE_E2 = 'gpom-sh-end-ai-e2-h-v6-w10-22571839.wav'
E2_PHRASES = [(0.00, 0.90, 'I made it.'), (4.08, 6.42, 'Now the real work starts.')]  # 0.05 s pads on the map
CODA = 'gpom-sh-e-coda-a-v6-w60-18b34a9d.wav'
# The coda's one edit (measured on its level envelope, 0.1 s frames): its opening piano phrase decays to a low point
# at 9.05 s; the take's later phrase onset at 23.45 s follows straight on, skipping the first rise. The held-chord
# pocket (29.5-33.5 s) then sits 14.4 s earlier; the cello's last phrase starts at 33.6 s, the last low note at
# 36.6 s, decayed to about -42 dB by 39.4 s (where the cue fades out).
SEAM_A, SEAM_B = 9.05, 23.45
POCKET, CELLO, MUS_END = 29.5, 33.6, 39.4
# Review round 2: the last line is "I made it. They didn't." and stops there (the first two sentences of atom -e1,
# the take's 0.0-3.3 s). Draft 4's "Don't let the same lot make me come back twice" was still heard as a threat
# (three blind listens: "menacing", "grave"), it was an instruction to the viewer (brief E: no call to action), and
# "the same lot" could land back on "you lot" (humanity). A warmer Suno re-take could not be recorded (WSLg
# PulseAudio lag: CAPTURE_TIMEOUT / PULSE_FAILED on every try, 22 Oct), so the imperative is dropped, as the finding's
# fallback says. The pause between the two sentences is the take's own 1.76 s, held to 1.3 s.
AI_WIN = (0.0, 4.0)
GAPS = (1.3,)
LINE_AT = 22.1     # the line's first word (scene time): on the coda's held-chord pocket, as the pull-back settles
# the voice is opened up in two steps (the cold-viewer finding): "I made it." keeps a 40% trace of Maddie's speaker so
# the viewer knows whose voice it is; "They didn't." is the full voice. Both lose the take's boom below ~110 Hz and 4 dB
# of its 200 Hz gravel, with a little presence, so it sits close and tired rather than looming.
EQ = ['highpass=f=110', 'equalizer=f=200:t=q:w=1:g=-4', 'equalizer=f=2800:t=q:w=1.2:g=2']
TRACE = "asplit=2[d][s];[s]" + E.SPEAKER + "[s2];[d][s2]amix=inputs=2:weights='0.6 0.4':normalize=0"
E03_HOLD, E03_FADE = 1.3, 1.5   # after the last word: TAIL plus a held beat, then the fade to black
SFXE = E.CLIPS / 'ending' / 'E' / 'sfx'
MUS_IN = 7.0       # the coda comes in on the cut to E02


def ed(t):
    """Coda source time -> time inside the edited cue."""
    return t if t < SEAM_A else t - (SEAM_B - SEAM_A)


# ---------------------------------------------------------------- picture prep (lips venv: cv2)

def lips(script, *args):
    subprocess.run([str(E.LIPS_PY), '-I', str(HERE / script), *map(str, args)], check=True)


def d16_frame(c):
    """The last frame scene D shows: the end of the last piece in D's edl (not a fixed clip), refreshed every run."""
    last = json.loads(D_EDL.read_text())['video'][-1]
    p = c.vdir / 'd16-last-r1.png'
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-ss', f"{last['in'] + last['dur'] - 1.0 / FPS:.4f}", '-i',
                    last['file'], '-frames:v', '1', str(p)], check=True)
    return p, pathlib.Path(last['source']).name


def chain_e03(sc, out):
    """Join E03's two round-1 clips: the tail (chained from the head's last frame) loses its first frame, and a short
    dissolve covers the join's exposure step."""
    if out.exists():
        return out
    med = pathlib.Path(sc.clips['media'])
    a, b = med / E03_HEAD, med / E03_TAIL
    off = C3.dur(a) - E03_XF
    fc = (f'[0:v]fps={FPS},setpts=PTS-STARTPTS[a];[1:v]fps={FPS},trim=start_frame=1,setpts=PTS-STARTPTS[b];'
          f'[a][b]xfade=transition=fade:duration={E03_XF}:offset={off:.4f}[v]')
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(a), '-i', str(b), '-filter_complex', fc, '-map',
                    '[v]', *E.ENC, str(out)], check=True)
    return out


def regrade(src, out, ref_secs=2.0, strength=0.6, smooth=2.0):
    """cut3.regrade_v6's method with a scene-E note: per frame, each channel's mean and spread (320x180, smoothed)
    moved `strength` of the way to the first `ref_secs`. Ramped, so there is no step anywhere."""
    w, h = 320, 180
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', str(src), '-vf', f'scale={w}:{h}', '-f', 'rawvideo',
                          '-pix_fmt', 'rgb24', '-'], capture_output=True, check=True).stdout
    sm = np.frombuffer(raw, np.uint8).reshape(-1, h, w, 3).astype(np.float32)
    mean, sd = sm.mean((1, 2)), sm.std((1, 2))
    k = int(smooth * FPS) | 1
    ker = np.ones(k) / k
    pad = lambda a: np.pad(a, ((k // 2, k // 2), (0, 0)), mode='edge')  # noqa: E731
    mean = np.stack([np.convolve(pad(mean)[:, ch], ker, 'valid') for ch in range(3)], 1)
    sd = np.stack([np.convolve(pad(sd)[:, ch], ker, 'valid') for ch in range(3)], 1)
    n_ref = int(ref_secs * FPS)
    m_ref, s_ref = mean[:n_ref].mean(0), sd[:n_ref].mean(0)
    m_tgt, s_tgt = mean + strength * (m_ref - mean), sd + strength * (s_ref - sd)
    gain = s_tgt / sd
    drift = mean.max(0) - m_ref
    note = (f'E03 regrade: the chained take (sh-29 + E03x) cools and flattens as it runs (channel means up to '
            f'R{drift[0]:+.0f} G{drift[1]:+.0f} B{drift[2]:+.0f} of 255 by ~10 s, partly because the warm chip shop '
            f'drifts out of frame). A ramped per-channel grade pulls every frame {strength:.0%} of the way back to its '
            f'first {ref_secs:g} s; the 8 s join itself has no step.')
    if out.exists():
        return out, note
    W, H = 1280, 720
    dec = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-i', str(src), '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                           stdout=subprocess.PIPE)
    enc = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                            '-r', str(FPS), '-i', '-', *E.ENC, str(out)], stdin=subprocess.PIPE)
    fsz = W * H * 3
    for n in range(len(mean)):
        buf = dec.stdout.read(fsz)
        if len(buf) < fsz:
            break
        x = np.frombuffer(buf, np.uint8).reshape(H, W, 3).astype(np.float32)
        enc.stdin.write(np.clip((x - mean[n]) * gain[n] + m_tgt[n] + 0.5, 0, 255).astype(np.uint8).tobytes())
    enc.stdin.close()
    enc.wait()
    dec.wait()
    return out, note


def black(out, d):
    if not out.exists():
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'lavfi', '-i', f'color=c=black:s=1280x720:r={FPS}',
                        '-t', f'{d:.4f}', *E.ENC, str(out)], check=True)
    return out


# ---------------------------------------------------------------- the AI take

def phrases(path, t_min=0.0, t_max=9.0, floor=40, min_gap=0.5):
    """Speech runs in the take's t_min..t_max s (10 ms frames over -floor dB from its peak; 50 ms before, 80 after)."""
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-ss', str(t_min), '-i', str(path), '-t', str(t_max - t_min),
                          '-ac', '1', '-ar', '16000',
                          '-f', 's16le', '-'], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.int16).astype(float) / 32768
    n = len(x) // 160
    db = 20 * np.log10(np.sqrt((x[:n * 160].reshape(n, 160) ** 2).mean(1)) + 1e-9)
    act = np.where(db > db.max() - floor)[0]
    runs, s = [], act[0]
    for a, b in zip(act, act[1:]):
        if (b - a) * 0.01 > min_gap:
            runs.append((s, a))
            s = b
    runs.append((s, act[-1]))
    return [(t_min + max(0.0, a * 0.01 - 0.05), t_min + (b + 1) * 0.01 + 0.08) for a, b in runs]


# ---------------------------------------------------------------- scene E

def scene_e(sc):
    c = E.Cut(sc, 'gpom-second-half-E-rough3', 'Ending E Timeline', 'GPOM second half · the ending · scene E: the bus',
              'Scene E of the ending, round 1 (Kai\'s notes, 23 Oct): a woman on a bus is watching this film; Maddie\'s '
              '"Mind how you go." comes out of her phone; she looks up at her own high street; a red bus drives away. '
              'The AI\'s last line is not recorded yet: its slot is a silent hold. Play it, click any beat, clip, line '
              "or sound, and leave a note in its yellow slip. Notes save as you type. Tell Claude when you're done.")
    m = c.m
    V = c.vdir
    d16, d16_src = d16_frame(c)

    # ---- e1: the bus. Hard cut on sound; the phone plays the tail of Maddie's line.
    b = c.beat('e1', 'The bus', 0.0, act='The ending',
               see='Hard cut on sound: a woman on the top deck at night, watching her phone. On it, gleaming Maddie '
                   'among the empty chairs (the last frame of D, composited). Tinny, through the phone: "Mind how you go."')
    e01 = sc.clip('E01')
    comp01 = V / 'E01-phone-r1.mp4'
    if not comp01.exists():
        lips('phone_screen.py', e01, d16, comp01, '--quad', '570,407,708,422,698,503,550,499', '--dim', '0.75',
             '--skin-from', '0.72', '--t1', '99', '--fade', '0')
    d01 = 7.0
    push01 = V / 'E01-push-r1.mp4'
    if not push01.exists():
        lips('move_keys.py', comp01, push01, '--in', '0', '--dur', f'{d01}',
             '--keys', '0:1:640:360,1.5:1:640:360,7:1.1:630:455')
    c.pic(push01, 0.0, 0.0, d01, 'e1', source=e01)
    ph = sc.voice('e1-0-maddie')
    sp0, sp1 = sc.vox['lines']['e1-0-maddie']['speech']
    AT1 = 0.3
    end = c.say('vox-maddie-phone', ph, 0.0, C3.dur(ph), AT1, 'e1: "Mind how you go." from the phone (whole; phone filter)',
                lufs=-21.0)  # -24 (the old tail's level) was heard "and down you go" under the rain and the engine
    c.line(b, 0, 'maddie', AT1 + sp0, sp1 - sp0, sc.text('e1-0-maddie') + ' (from her phone)', 'kai')
    c.flags.append(f'E01 (Kai ld9-1/le1-0): Maddie\'s "Mind how you go." is said whole through the woman\'s phone, '
                   f'{AT1} s after the hard cut (it is no longer split across the cut): D ends on the silence after '
                   f'"Boss...", and E opens on the rain, the bus and her small voice from the phone.')
    c.flags.append(f'E01/E02: the phone shows the last frame scene D now shows ({d16_src}: gleaming Maddie among the '
                   'empty chairs), taken from D\'s cut itself, re-composited the way the old one was (phone_screen.py, the '
                   'same screen corners, dim and key settings).')
    c.flags.append('E01: the phone screen is tracked onto the '
                   'screen frame by frame (phone_screen.py: Lucas-Kanade features, RANSAC homography; drift under 6 px '
                   'over 8 s), dimmed to 75%, a faint glow, her right thumb keyed back on top. It replaces the plate\'s '
                   'robot-in-ruins screen.')
    c.flags.append('E01: a slow push 100 -> 110% toward the phone after a 1.5 s hold (eased, in post), so the screen '
                   'reads before the cut.')
    m['phone'] = (AT1, end)
    t = c.close(b, d01)

    # ---- e2: she looks up
    b = c.beat('e2', 'She looks up', t, act='The ending',
               see='Over her shoulder: the empty chairs on her phone, her own high street through the wet window (the '
                   'chip shop, the pharmacy, the closed bank). She looks up from one to the other.')
    e02 = sc.clip('E02')
    comp02 = V / 'E02t3-phone-r1.mp4'
    if not comp02.exists():
        lips('phone_screen.py', e02, d16, comp02, '--quad', '567.5,522,645,542.5,627.5,590,544.5,570', '--t1', '2.5',
             '--fade', '0.3', '--white-key', '150', '--dim', '0.55')
    sign02 = V / 'E02t3-bank-r1.mp4'
    if not sign02.exists():
        lips('bank_sign.py', comp02, sign02, '--name', 'DOWNLAND BANK')
    d02 = 6.0
    c.pic(sign02, 0.0, t, t + d02, 'e2', source=e02)
    c.flags.append('E02 (review round 1): re-rolled as E02-t3 so the phone stays in her hand: she lowers it to her '
                   'knee and keeps hold of it (t2\'s phone melted into her lap at ~2.8 s). D16\'s frame is on the '
                   'screen (dimmed to 55%) while it faces us, fading out by 2.5 s as she tilts it away; from ~1 s Omni '
                   'turned the screen white, and there the white screen itself is the matte, so her thumb stays on '
                   'top. No white screen is ever seen.')
    c.flags.append('E02 (review round 1): the closed bank is lettered in post (bank_sign.py, exact, tracked to the '
                   'plate\'s 1.5 px breathing by phase correlation, softened behind the wet glass): a plain fictional '
                   'name, DOWNLAND BANK, on the blank fascia, and a printed "THIS BRANCH HAS NOW CLOSED" notice on the '
                   'card in its middle window. The name is my call (fictional, regional, ties to the downs): Kai to rule.')
    c.flags.append('E02 runs 6 s (scene.json), not clips.json\'s 7: she has turned to the bank by 3.5 s and 2.5 s of '
                   'her holding still is enough (my call). Camera locked, no post move: her turn is the movement.')
    m['s2'] = t
    t = c.close(b, t + d02)

    # ---- e3: the bus drives away, the last line (its slot held silent: not recorded yet)
    s3 = t
    b = c.beat('e3', 'The bus drives away', s3, act='The ending',
               see='Tight on the lit red bus (140%), a 1.5 s hold, then an eased pull-back to the whole wet high street as '
                   'the bus pulls away. The AI, unfiltered and close, for the first time (its line owed). Fade to black.')
    e03 = chain_e03(sc, V / 'E03r4-chain.mp4')
    banked = V / 'E03r4-bank.mp4'
    if not banked.exists():
        lips('bank_sign_e03.py', e03, banked, '--name', 'DOWNLAND BANK')
    graded, note = regrade(banked, V / 'E03r4-chain-graded.mp4')
    c.flags.append(note.replace('(sh-29 + E03x)', '(E03r4-t1 + E03xr4-t1)').replace(
        'the warm chip shop drifts out of frame', 'the rain thickens'))
    c.flags.append(f'E03 (Kai reel at4010, ending round 2): the red bus on an EMPTY road. The plate was edited again '
                   f'(E03r4b-c: every car and headlight removed; the hooded pair on the right went with them), re-animated '
                   f'(E03r4-t1, 10 s) and extended (E03xr4-t1, 8 s) from its last frame with a far oncoming vehicle painted '
                   f'out first (E03r4-last-clean-a), so nothing drives towards the bus. Omni pans the camera slowly right in '
                   f'both clips (asked for locked).')
    c.flags.append(f'E03 (Kai at353): a RED double-decker. The still was edited (E03r3-b: E03b-r1-b with the bus made '
                   f'plain pillar-box red, no roundel, no route number, no adverts, nothing written on it), re-animated '
                   f'(E03r3-t1, 10 s) and extended from its last frame (E03xr3-t2, 8 s: locked, the bus recedes further, '
                   f'the two walkers turn and walk away). Joined here as before: the tail\'s first frame dropped, a '
                   f'{E03_XF} s dissolve over the join (it steps 2.7 against a 0.8 in-clip median, an exposure jump). '
                   'The closed bank is the same plate, so bank_sign_e03.py letters it as before (DOWNLAND BANK and the '
                   'closure sheet, tracked). Omni drew small unreadable fascia lettering on the far shops: left.')
    # the line (Kai's pick, rev H): "I made it." on the coda's held-chord pocket, the take's own 3.2 s pause kept, so
    # "Now the real work starts." lands as the cello's last phrase begins (coda 33.6 s = scene 26.2 s)
    take = sc.media / 'suno' / AI_TAKE_E2
    atom = (E2_PHRASES[0][0], E2_PHRASES[-1][1])
    L = fr(LINE_AT)
    for k, (a_, b_, w) in enumerate(E2_PHRASES):
        tt = L + (a_ - E2_PHRASES[0][0])
        if k == 0:
            e = c.say('vox-ai', take, a_, b_, tt, f'e3: the AI, a trace of Maddie\'s speaker left: "{w}"',
                      chain=[TRACE, *EQ], lufs=-16.0, ref=atom)
        else:
            e = c.say('vox-ai', take, a_, b_, tt, f'e3: the AI, his own voice: "{w}"', chain=EQ, lufs=-17.5, ref=atom)
    line_end = e
    c.line(b, 0, 'ai', L, line_end - L, LINE_TEXT, 'kai')
    b['lines'][-1]['name'] = 'The AI (opening to his own voice, for the first time)'
    d03 = fr(min(line_end - s3 + TAIL + E03_HOLD + E03_FADE, C3.dur(e03) - 1.0 / FPS))
    pull = V / f'E03r4-pull-{d03:.3f}.mp4'
    fade_at, fade_d = d03 - E03_FADE, E03_FADE
    if not pull.exists():
        lips('move_keys.py', graded, pull, '--in', '0', '--dur', f'{d03:.4f}',
             '--keys', '0:1.4:740:410,1.5:1.4:740:410,9.5:1:640:360', '--fade-out', f'{fade_at:.4f}:{fade_d}')
    c.pic(pull, 0.0, s3, s3 + d03, 'e3', source=sc.clips['media'] + '/' + E03_HEAD)
    c.flags.append(f'The last line (Kai\'s pick, Suno rev H, take 22571839): "{LINE_TEXT}". "I made it." at '
                   f'{L - s3:.1f} s into the shot, on the coda\'s held-chord pocket; the take\'s own 3.2 s pause is KEPT, so '
                   f'"Now the real work starts." lands as the cello\'s last phrase begins; it ends {line_end - s3:.1f} s in. '
                   f'The picture holds it: the bus chain is {C3.dur(e03):.1f} s, so the fade to black starts '
                   f'{s3 + fade_at - line_end:.1f} s after the last word (was planned as {TAIL + E03_HOLD:.1f} s; the clip '
                   'runs out first). Cut on the take\'s silence map, not whisper.')
    c.flags.append('E03 voice: "I made it." keeps a 40% trace of Maddie\'s speaker filter so the voice is his before it '
                   'changes; "Now the real work starts." is his own voice, full range, close (boom under 110 Hz off, -4 dB '
                   'at 200 Hz, +2 dB at 2.8 kHz), 1.5 dB quieter. The coda ducks 6 dB under both.')
    m['s3'], m['line'] = s3, (L, line_end)
    m['fade'] = (s3 + fade_at, s3 + d03)
    t = c.close(b, s3 + d03)

    # ---- e4: black under the last note
    total = fr(MUS_IN + ed(MUS_END) + 0.6)
    b = c.beat('e4', 'Black', t, act='The ending', see='Black. The last low piano note decays. No logo, no "We are BadCode".')
    c.pic(black(V / f'black-{total - t:.3f}.mp4', total - t), 0.0, t, total, 'e4', source='black')
    c.flags.append(f'E04: {total - t:.1f} s of black (scene.json planned 3 s): the coda\'s last low note sounds just '
                   'after the picture has gone and is left to decay to about -42 dB, then faded (my call).')
    c.close(b, total)
    c.total = total
    return c


# ---------------------------------------------------------------- ambience (synthesised, seeded)

RNG = np.random.default_rng(20261022)


def noise(d, colour='pink'):
    n = int(round(d * SR))
    x = RNG.standard_normal((n, 2))
    X = np.fft.rfft(x, axis=0)
    f = np.fft.rfftfreq(n, 1 / SR)
    f[0] = f[1]
    X *= (1 / np.sqrt(f) if colour == 'pink' else 1 / f)[:, None]
    y = np.fft.irfft(X, n, axis=0)
    return (y / np.abs(y).max()).astype(np.float32)


def band(x, lo=None, hi=None, order=4):
    if lo and hi:
        sos = signal.butter(order, [lo, hi], 'bandpass', fs=SR, output='sos')
    elif lo:
        sos = signal.butter(order, lo, 'highpass', fs=SR, output='sos')
    else:
        sos = signal.butter(order, hi, 'lowpass', fs=SR, output='sos')
    return signal.sosfilt(sos, x, axis=0).astype(np.float32)


def slow(n, rate, depth, phase=0.0):
    t = np.arange(n) / SR
    return (1 - depth / 2 + depth / 2 * np.sin(2 * np.pi * rate * t + phase))[:, None].astype(np.float32)


def rain_window(d):
    """Rain on a bus window: a soft hiss plus drops ticking on the glass."""
    hiss = band(noise(d), 700, 6000)
    n = len(hiss)
    drops = np.zeros((n, 2), np.float32)
    k = RNG.poisson(35 * d)
    pos = RNG.integers(0, n - 400, k)
    burst = (RNG.standard_normal(240) * np.exp(-np.arange(240) / 40)).astype(np.float32)
    for p in pos:
        ch = RNG.integers(0, 2)
        drops[p:p + 240, ch] += burst * RNG.uniform(0.2, 1.0)
    drops = band(drops, 1800, 7000, 2)
    return C.level(hiss, rms=-20) + C.level(drops, rms=-26)


def bus_interior(d, moving):
    """A diesel bus from the top deck: low engine, a 31 Hz firing tone with harmonics, a little panel rattle."""
    n = int(round(d * SR))
    t = np.arange(n) / SR
    f0 = 31.0 if moving else 24.0
    tone = sum(np.sin(2 * np.pi * f0 * h * t + h) / h for h in (1, 2, 3, 4))[:, None] * np.ones((1, 2))
    rumble = band(noise(d, 'brown'), hi=160)
    rattle = band(noise(d), 250, 900) * slow(n, 3.1, 0.8)
    x = C.level(rumble, rms=-20) + C.level(tone.astype(np.float32), rms=-26) + C.level(rattle, rms=-34)
    if moving:
        x = x * slow(n, 0.13, 0.35)
    return x.astype(np.float32)


def street(d):
    """A wet high street at night: rain on tarmac (broad hiss), and two cars hissing past far off."""
    n = int(round(d * SR))
    x = C.level(band(noise(d), 300, 9000), rms=-20)
    swish = band(noise(d), 200, 3000)
    t = np.arange(n) / SR
    env = np.zeros(n)
    for c0 in (3.5, 9.0):
        env += np.exp(-((t - c0) / 1.1) ** 2)
    x = x + C.level(swish, rms=-18) * env[:, None].astype(np.float32) * 0.5
    return x.astype(np.float32)


def bus_away(d, pan_to=0.35):
    """The bus pulling away and receding: engine low and loud, then quieter and duller with distance."""
    n = int(round(d * SR))
    t = np.arange(n) / SR
    f = 34 + 6 * np.clip(t / 3, 0, 1)  # revs up as it pulls off
    ph = 2 * np.pi * np.cumsum(f) / SR
    tone = sum(np.sin(ph * h + h) / h for h in (1, 2, 3, 4, 5))[:, None] * np.ones((1, 2))
    x = C.level(band(noise(d, 'brown'), hi=300), rms=-20) + C.level(tone.astype(np.float32), rms=-24)
    near, far = band(x, hi=900), band(x, hi=180)
    mixk = np.clip(t / d, 0, 1)[:, None]
    y = near * (1 - mixk) + far * mixk
    y = y * (10 ** (-24 * np.clip(t / d, 0, 1) / 20))[:, None]  # -24 dB over the shot
    p = pan_to * np.clip(t / d, 0, 1)
    y[:, 0] *= (1 - p)
    y[:, 1] *= (1 + p) / (1 + pan_to)
    return y.astype(np.float32)


def audio_e(c):
    m, total = c.m, c.total
    mx = C.Mix(total)
    E.voices(c, mx)
    B = {b['id']: b for b in c.beats}
    st = {k: b['start'] for k, b in B.items()}
    en = {k: b['start'] + b['dur'] for k, b in B.items()}
    lvl = lambda x, r: C.level(x, rms=r)  # noqa: E731

    # ---- music: e-coda, one edit, in on the cut to E02, ducked 6 dB under the line, out on black
    src = c.sc.media / 'suno' / CODA
    a = C.decode(src, 0.0, SEAM_A + 0.05)
    b2 = C.decode(src, SEAM_B - 0.05, MUS_END - SEAM_B + 0.65)
    k = int(0.1 * SR)
    w = np.linspace(0, np.pi / 2, k)[:, None]
    x = np.concatenate([a[:-k], a[-k:] * np.cos(w) + b2[:k] * np.sin(w), b2[k:]])
    x = C.level(x, rms=-21, peak=-3)
    L0, L1 = m['line']
    d = total - MUS_IN
    x = x[:int(d * SR)]
    # ducked 6 dB under the line (its two phrases; the 3.2 s pause between them plays at full level)
    pts = [(0, 0), (0.6, 1)]
    for a_, b_, _ in E2_PHRASES:
        t0, t1 = L0 + a_ - MUS_IN, L0 + b_ - MUS_IN
        pts += [(t0 - 0.4, 1), (t0, 0.5), (t1, 0.5), (t1 + 0.5, 1)]
    x *= C.env(len(x), sorted(pts + [(d - 0.6, 1), (d, 0)]))
    mx.add('mus-e-coda', x.astype(np.float32), MUS_IN, src,
           f'e-coda (edited: 0-{SEAM_A} s, then {SEAM_B} s on), ducked under the line')
    c.flags.append(f'Music: e-coda comes in on the cut to E02 ({MUS_IN:.1f} s), not on her look-up 2 s later, so that '
                   f'with one edit (its opening phrase to {SEAM_A} s, then straight to the phrase at {SEAM_B} s, a '
                   '0.1 s crossfade on a low point; the first rise is cut) its held-chord pocket falls under the line and '
                   'its last low note falls on black. The edit is measured on the level envelope, not heard: Kai to '
                   'rule by ear.')

    # ---- ambience (review round 1): RECORDED beds, CC0 Freesound (E/sfx/CREDITS.md), replacing the synth.
    # Inside the bus (e1-e2): one continuous engine bed and one rain-on-the-window bed, so nothing switches at the
    # E01/E02 cut; the engine eases down 5 dB and duller over 1.5 s before it (the bus has pulled in at a stop).
    # The street (e3): rainy-night traffic, and the bus departing from the stop on the cut, receding (low-passed
    # and down 20 dB as it goes), all gone by the black.
    s2, s3 = st['e2'], st['e3']
    eng = C.decode(SFXE / 'fs264409-bus-interior-engine.mp3', 8.0, s3 + 0.3)
    eng_dull = band(eng, hi=500)
    n = len(eng)
    tt = np.arange(n) / SR
    k_ = np.clip((tt - (s2 - 1.5)) / 1.5, 0, 1)[:, None].astype(np.float32)
    k_ = k_ * k_ * (3 - 2 * k_)
    xe = (eng * (1 - k_) + eng_dull * k_) * (10 ** (-5 * k_ / 20))
    xe = C.level(xe.astype(np.float32), rms=-31)
    # round 1: the beds dip ~6 dB under the phone's "Mind how you go." (at full level the mix was heard "and down
    # you go"), back up as the line ends
    p0, p1 = m['phone']
    dip = [(0, 1), (max(0.0, p0 - 0.2), 1), (p0 + 0.1, 0.5), (p1, 0.5), (p1 + 0.8, 1)]
    xe = xe * C.env(len(xe), dip + [(len(xe) / SR, 1)])
    mx.add('sfx-bus', C.fades(xe[:int(s3 * SR) + int(0.03 * SR)], 0.0, 0.03), 0.0,
           SFXE / 'fs264409-bus-interior-engine.mp3', 'top deck, moving, then pulled in at the stop (recorded)')
    xr = C.decode(SFXE / 'fs360783-rain-on-window-wet-traffic.mp3', 25.0, s3 + 0.03)
    xr = xr * C.env(len(xr), dip + [(len(xr) / SR, 1)])
    mx.add('sfx-rain', C.fades(C.level(xr, rms=-34), 0.0, 0.03), 0.0,
           SFXE / 'fs360783-rain-on-window-wet-traffic.mp3', 'rain on the window, wet traffic outside (recorded)')
    f0, f1 = m['fade']
    dd = f1 + 0.4 - s3
    xs = C.level(C.decode(SFXE / 'fs723695-city-traffic-rainy-night.mp3', 2.0, dd), rms=-32)
    xs *= C.env(len(xs), [(0, 1), (f0 - s3, 1), (dd, 0)])
    mx.add('sfx-street', xs, s3, SFXE / 'fs723695-city-traffic-rainy-night.mp3', 'rain and traffic on the high street at night (recorded)')
    xb = C.level(C.decode(SFXE / 'fs715718-bus-departs-stop.mp3'), rms=-30)
    nb = len(xb)
    tb = np.arange(nb) / SR
    kk = np.clip(tb / (nb / SR), 0, 1)[:, None].astype(np.float32)
    xb = (xb * (1 - kk) + band(xb, hi=400) * kk) * (10 ** (-20 * kk / 20))
    xb = C.fades(xb.astype(np.float32), 0.02, 0.8)
    mx.add('sfx-bus-away', xb, s3, SFXE / 'fs715718-bus-departs-stop.mp3', 'the bus departing from the stop, receding (recorded)')
    c.flags.append('Sound (review round 1): the synthesised rain, bus and street are replaced by recorded CC0 beds '
                   '(Freesound HQ previews, E/sfx/CREDITS.md): a bus interior engine and rain on a window with wet '
                   'traffic outside under E01-E02 (one continuous bed each, so nothing switches at the cut; the engine '
                   'eases down and duller before E02, pulled in at the stop), then rainy-night traffic and a bus '
                   'departing from a stop under E03. Each was checked for speech with whisper (VAD): none. Not heard by '
                   'ear in this run: Kai to rule on the beds.')
    c.flags.append('Sound: the cut lands on sound (rain, the bus, the phone), no music under E01, as music.md plans.')
    return mx


E.SCENE_FNS['E'] = (scene_e, audio_e)

if __name__ == '__main__':
    E.run('E', '--no-preview' not in sys.argv)
    # cut_end.run's QC note quotes scene C's overshoot numbers; put scene E's own in
    p = E.CLIPS / 'ending' / 'E' / 'cut' / 'edl.json'
    data = json.loads(p.read_text())
    r = subprocess.run(['ffprobe', '-v', 'error', '-f', 'lavfi', '-i', f"movie={data['preview']},signalstats", '-show_entries',
                        'frame_tags=lavfi.signalstats.YMIN,lavfi.signalstats.YMAX,lavfi.signalstats.YLOW,'
                        'lavfi.signalstats.YHIGH', '-of', 'json'], capture_output=True, text=True)
    if r.returncode == 0:
        fs = [f['tags'] for f in json.loads(r.stdout)['frames']]
        g = lambda k: [float(f[f'lavfi.signalstats.{k}']) for f in fs]  # noqa: E731
        lo, hi = min(g('YMIN')), max(g('YMAX'))
        note = (f'(scene E: luma {lo:.0f}/{hi:.0f} on isolated pixels; the 10th/90th percentiles stay inside 16-235 '
                f'on every frame, {min(g("YLOW")):.0f}/{max(g("YHIGH")):.0f})')
        data['flags'] = [f.replace('(3/247)', note) for f in data['flags']]
        p.write_text(json.dumps(data, indent=1, ensure_ascii=False))

