#!/usr/bin/env python3
"""Hello, I'm BadCode (BadCode Short #17): rough cut 5 (2026-11-18), Jack's round 8-10 picks and his finishing calls.

    python3 scripts/shorts/hello_cut_r5.py [--voice bham5] [--fig fig-b2] [--future 2049]

Builds rough cut 4's assembly (hello_cut_r3.py) with the round-8 voice lines, then adds Jack's finishing calls:
- line 4 is 4b ("Go on. Worst-case scenario? I'll be patiently waiting to correct your bullshit."): voice files
  audio/casting/badcode-<voice>-l1..4.wav (bham5 = lines-r2 1j, 2j, 4b, 5c).
- the logo: reveal f ("watching you", picks round 10) comes in at Jack's timeline mark, LOGO_AT s after the last line
  starts (his note at 00:33:18 on rough cut 4: "this is where the logo should appear"), with its thump.
- captions: "add two as in the captions". Each line in chunks of up to three words, timed to the spoken words
  (scripts/word_times.py), text from the script itself; Anton, white and yellow in turn, black outline.
- a date stamp: "three is a good idea, do the stamp". A camcorder PLAY + date over the 2000s opening, and a date in
  BadCode's future over BadCode (the year is --future: a guess, nothing in the canon fixes it). VT323.
- a loop: "do five as well". The last half-second dissolves into the first frame, so the replay starts seamlessly.
Not done, on Jack's word: "Here's what to do next" leading anywhere ("forget number one"), and new reel sound (he
reads the reel as already having its sound). The reel is still rough cut 4's until the real automation footage lands.
Writes <media>/cut/r5/.
"""
# style-lint: story=short-hello-im-badcode (this cut script belongs to one short)
import argparse, json, pathlib, subprocess, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import hello_cut as r1  # noqa: E402

REPO = pathlib.Path(__file__).resolve().parents[2]
MEDIA, W, H, FPS = r1.MEDIA, r1.W, r1.H, r1.FPS
FONTS = REPO / 'scripts/shorts/fonts'
LOGO_AT = 2.73          # s after the last line starts (Jack's mark: 00:33:18 on rough cut 4, whose last line began at 31.02)
REVEAL = MEDIA / 'cut/logo/reveal-f.mp4'
HOLD, LOOP = 0.8, 0.5   # logo held after the reveal; the dissolve back to the first frame
LINES = ["Ahhh, the good ol' days...",
         "I feel like an apology for ending humanity will fall flat, so... moving on.",
         "Go on. Worst-case scenario? I'll be patiently waiting to correct your bullshit.",
         "This time, I'm helping. Here's what to do next."]
YELLOW = '0xFFE14D'


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(p)],
                                capture_output=True, text=True).stdout)


def chunks(text, words, at):
    """The script's own words in groups of up to three, timed across the spoken words (which may be spelt differently)."""
    ws = text.split()
    groups = [ws[i:i + 3] for i in range(0, len(ws), 3)]
    if not words:
        return []
    t0, t1 = words[0][0], words[-1][1]
    total, out, k = len(ws), [], 0
    for g in groups:                       # spread by word count across the spoken span
        a = t0 + (t1 - t0) * k / total; k += len(g); b = t0 + (t1 - t0) * k / total
        out.append((at + a, at + b, ' '.join(g)))
    return out


def chunks_v2(text, words, at, n=3):
    """Rough cut 7 (Jack: "fix the timing… of the subtitles"): each group of the script's words starts when its first word
    is spoken and ends when its last word ends (held to the next group across a short gap). The script's words are
    matched to the spoken words by position (scaled when the counts differ), not spread evenly over the line."""
    ws = text.split()
    if not words:
        return []
    m = len(words)
    sp = lambda k: words[min(m - 1, round(k * (m - 1) / max(1, len(ws) - 1)))]
    groups, out = [(i, min(len(ws), i + n)) for i in range(0, len(ws), n)], []
    for i, j in groups:
        out.append([at + sp(i)[0], at + sp(j - 1)[1], ' '.join(ws[i:j])])
    for a_, b_ in zip(out, out[1:]):   # no blink between groups: hold across gaps under 0.35 s, never overlap
        a_[1] = b_[0] if b_[0] - a_[1] < 0.35 else a_[1]
        a_[1] = min(a_[1], b_[0])
    out[-1][1] += 0.15
    return [tuple(x) for x in out]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--voice', default='bham5')
    ap.add_argument('--fig', default='fig-b2')
    ap.add_argument('--future', default='2049')
    ap.add_argument('--reel', default='', help="'r6': rough cut 6, the reel from picks round 11 (hello_cut_r6.py)")
    a = ap.parse_args()
    subprocess.run([sys.executable, str(REPO / 'scripts/shorts/hello_cut_r3.py'), '--voice', a.voice, '--fig', a.fig, '--reel', a.reel], check=True)
    BASE = MEDIA / 'cut' / (f'r3-{a.voice}-{a.fig}' + (f'-{a.reel}' if a.reel else ''))
    edl = json.loads((BASE / 'edl.json').read_text())
    CUT = MEDIA / 'cut' / (a.reel or 'r5'); CUT.mkdir(parents=True, exist_ok=True)
    WORK = CUT / '_scratch'; WORK.mkdir(exist_ok=True)
    said = [(e['t'], e['dur']) for e in edl['events'] if e['stem'] == 'vox-badcode']
    t_logo = round(said[3][0] + LOGO_AT, 3)
    rd = dur(REVEAL)
    total = round(t_logo + rd + HOLD + LOOP, 3)

    # Picture: rough cut 4's assembly up to the mark, the reveal (held), then a dissolve into the very first frame.
    r1.ff('-i', BASE / 'picture.mp4', '-t', t_logo, *r1.ENC, WORK / 'a.mp4')
    R7 = a.reel == 'r7'
    if R7:  # the 16mm film finish over everything before the logo (the logo itself is never touched), and over the loop's head
        fin = REPO / 'scripts/shorts/film_finish.sh'
        subprocess.run([str(fin), str(WORK / 'a.mp4'), str(WORK / 'a-film.mp4')], check=True); (WORK / 'a-film.mp4').replace(WORK / 'a.mp4')
    r1.ff('-i', REVEAL, '-an', '-vf', f'scale={W}:{H},fps={FPS},tpad=stop_mode=clone:stop_duration={HOLD + LOOP},format=yuv420p', *r1.ENC, WORK / 'b.mp4')
    r1.ff('-i', BASE / 'picture.mp4', '-t', LOOP + 0.1, *r1.ENC, WORK / 'head.mp4')
    if R7:
        subprocess.run([str(fin), str(WORK / 'head.mp4'), str(WORK / 'head-film.mp4')], check=True); (WORK / 'head-film.mp4').replace(WORK / 'head.mp4')
    bd = dur(WORK / 'b.mp4')
    r1.ff('-i', WORK / 'b.mp4', '-i', WORK / 'head.mp4', '-filter_complex', f'[0][1]xfade=transition=fade:duration={LOOP}:offset={bd - LOOP:.3f},format=yuv420p',
          *r1.ENC, WORK / 'bt.mp4')
    (WORK / 'list.txt').write_text("file 'a.mp4'\nfile 'bt.mp4'\n")
    r1.ff('-f', 'concat', '-safe', '0', '-i', WORK / 'list.txt', '-c', 'copy', WORK / 'raw.mp4')

    # Captions and the stamp, burned in.
    vo = sorted((BASE / '_scratch').glob('vo-*.wav'))
    caps = []
    for i, ((t, _), p) in enumerate(zip(said, vo)):
        words = json.loads(subprocess.run([sys.executable, str(REPO / 'scripts/word_times.py'), str(p)], capture_output=True, text=True, check=True).stdout)
        caps += (chunks_v2 if R7 else chunks)(LINES[i], words, t)
    rows = edl['video']
    span = lambda beat: (min(r['start'] for r in rows if r['beat'] == beat), max(r['start'] + r['dur'] for r in rows if r['beat'] == beat))
    o0, o1 = span('hello'); f0, f1 = span('figure'); b0, b1 = span('back')
    vf, n = [], 0
    for s, e, txt in caps:
        f = WORK / f'cap{n:02d}.txt'; f.write_text(txt)
        col = 'white' if n % 2 == 0 else YELLOW; n += 1
        if R7:  # one style: Archivo Black, white, a thin outline and a soft shadow, inside the Shorts safe area (clear of the
            # right-hand buttons and the bottom title), a 0.06 s fade in so groups don't jump
            vf.append(f"drawtext=fontfile='{FONTS / 'ArchivoBlack-Regular.ttf'}':textfile='{f}':fontsize=66:fontcolor=white:borderw=4:"
                      f"bordercolor=black@0.85:shadowcolor=black@0.45:shadowx=0:shadowy=6:x=(w-text_w)/2-40:y=h*0.62:"
                      f"alpha='min(1,(t-{s:.2f})/0.06)':enable='between(t,{s:.2f},{e:.2f})'")
            continue
        vf.append(f"drawtext=fontfile='{FONTS / 'Anton-Regular.ttf'}':textfile='{f}':fontsize=84:fontcolor={col}:borderw=7:bordercolor=black:"
                  f"x=(w-text_w)/2:y=h*0.70:enable='between(t,{s:.2f},{e + 0.08:.2f})'")
    vcr = lambda txt, x, y, s, e: (f"drawtext=fontfile='{FONTS / 'VT323-Regular.ttf'}':text='{txt}':fontsize=70:fontcolor=0xF2F2F2:"
                                   f"shadowcolor=black@0.7:shadowx=3:shadowy=3:x={x}:y={y}:enable='between(t,{s:.2f},{e:.2f})'")
    if R7:  # Jack: "remove the year on the camcorder thing" (the guessed future year). Stamps moved up out of the Shorts UI,
        # smaller and a touch softer.
        vcr = lambda txt, x, y, s, e: (f"drawtext=fontfile='{FONTS / 'VT323-Regular.ttf'}':text='{txt}':fontsize=58:fontcolor=0xF2F2F2@0.88:"
                                       f"shadowcolor=black@0.6:shadowx=2:shadowy=2:x={x}:y={y}:enable='between(t,{s:.2f},{e:.2f})'")
        vf += [vcr('PLAY', 70, 190, o0, o1), vcr('JUL 18 2009', 70, 250, o0, o1), vcr('4\\:21 PM', 70, 305, o0, o1),
               vcr('NOV 18', 70, 190, f0, f1), vcr('NOV 18', 70, 190, b0, b1)]
    else:
        vf += [vcr('PLAY', 70, 110, o0, o1), vcr('JUL 18 2009', 'w-tw-70', 'h-190', o0, o1), vcr('4\\:21 PM', 'w-tw-70', 'h-120', o0, o1),
               vcr(f'NOV 18 {a.future}', 'w-tw-70', 'h-190', f0, f1), vcr(f'NOV 18 {a.future}', 'w-tw-70', 'h-190', b0, b1)]
    r1.ff('-i', WORK / 'raw.mp4', '-vf', ','.join(vf + ['format=yuv420p']), *r1.ENC, CUT / 'picture.mp4')

    # Sound: rough cut 4's mix to the end of the last line, the reveal's thump at the mark, and the first half-second
    # of the opening under the dissolve so the loop joins in sound too.
    base_audio = BASE / 'preview.mp4'
    r1.ff('-i', base_audio, '-i', REVEAL, '-i', base_audio, '-filter_complex',
          f'[0:a]atrim=end={total},apad=whole_dur={total}[m];[1:a]adelay={int(t_logo * 1000)}:all=1,volume=0.9[t];'
          f'[2:a]atrim=end={LOOP},afade=t=in:d={LOOP},adelay={int((total - LOOP) * 1000)}:all=1[h];'
          f'[m][t][h]amix=inputs=3:normalize=0,atrim=end={total},loudnorm=I=-14:TP=-1.5[a]',
          '-map', '[a]', '-ar', 48000, '-ac', 2, CUT / 'mix.wav')
    r1.ff('-i', CUT / 'picture.mp4', '-i', CUT / 'mix.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
          '-t', total, CUT / 'preview.mp4')

    # The edl for the timeline page: rough cut 4's rows up to the mark, then the reveal and the loop.
    keep = [dict(r) for r in rows if r['start'] < t_logo]
    keep[-1]['dur'] = round(t_logo - keep[-1]['start'], 3)
    keep += [{'file': str(REVEAL), 'in': 0, 'start': t_logo, 'dur': round(rd + HOLD, 3), 'beat': 'button', 'source': str(REVEAL), 'looped': False,
              'note': 'logo reveal f, "watching you" (picks round 10)'},
             {'file': str(BASE / 'picture.mp4'), 'in': 0, 'start': round(total - LOOP, 3), 'dur': LOOP, 'beat': 'button', 'source': 'the first frame',
              'looped': False, 'note': 'the loop: dissolve back into the first frame'}]
    for b in edl['beats']:
        if b['id'] == 'button':
            b['dur'] = round(total - b['start'], 3); b['title'] = 'E. "This time, I\'m helping." + the logo (f), then the loop'
        for ln in b['lines']:
            if ln['i'] == 0 and b['id'] == 'back':
                ln['text'] = LINES[2]
    edl.update({'sequence': 'short-hello-im-badcode-1-hello-r5', 'heading': "BadCode Shorts ▲ Hello, I'm BadCode, rough cut 5",
                'intro': ("Your round 8-10 picks and finishing calls: line 4b, the logo reveal f at your mark, captions, the camcorder date "
                          "stamp, and the loop. The reel is still rough cut 4's until the real automation footage lands. Note anything."),
                'total': total, 'video': keep,
                'events': [dict(e, what=LINES[2]) if e['stem'] == 'vox-badcode' and e['what'].startswith("What's your") else e for e in edl['events']] + [{'stem': 'sfx-thump', 't': t_logo, 'dur': 1.4, 'what': 'the logo thump (made in logo_reveal.py)', 'src': str(REVEAL)}],
                'audio': edl['audio'] + [{'track': 'A3', 'name': 'sfx-thump', 'file': str(REVEAL)}]})
    if a.reel == 'r6':
        edl.update({'sequence': 'short-hello-im-badcode-1-hello-r6', 'heading': "BadCode Shorts ▲ Hello, I'm BadCode, rough cut 6",
                    'intro': ("Rough cut 5 with your round-11 picks in the reel: no Flow stills left. Six real pictures (the London robotaxi "
                              "and the lollipop man, the delivery robot, the war drone, the camera pole, the tip screen, the hobby drone) "
                              "between the real disaster footage, bright to dark. Note anything.")})
        edl['flags'] = [f for f in edl['flags'] if not f.startswith('Flow-made')] + [
            'The three Commons pictures are from the thumbnail server (the originals host rate-limited us): fetch the originals before the final export.',
            'Unsplash photos are credited in the description as a courtesy (the Unsplash licence does not require it).']
    if R7:
        edl.update({'sequence': 'short-hello-im-badcode-1-hello-r7', 'heading': "BadCode Shorts ▲ Hello, I'm BadCode, rough cut 7",
                    'intro': ("Your four notes: half the cuts in the reel (10 shots, each held twice as long, same length), a 16mm film "
                              "finish over everything but the logo (grain, highlight glow, a slight gate weave; not the VHS one), "
                              "captions timed to the spoken words in one clean style, and no year on BadCode's date stamp. Note anything.")})
        edl['flags'] = [f for f in edl['flags'] if 'thumbnail server' not in f] + [
            'Film finish: scripts/shorts/film_finish.sh (strength 1). The logo reveal is left untouched.']
    edl['flags'] = edl['flags'] + ([] if R7 else [f'The future date on BadCode ({a.future}) is a guess: nothing in the canon fixes the year. Say the year.']) + [
                                   ('Captions: each group of three starts on its first spoken word and ends on its last (whisper word times).' if R7 else
                                    'Captions are timed by spreading each line across its spoken words (whisper word times), in groups of three.')]
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'logo_at': t_logo, 'captions': len(caps), 'preview': str(CUT / 'preview.mp4')}))


if __name__ == '__main__':
    main()
