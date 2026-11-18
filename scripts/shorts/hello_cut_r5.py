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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--voice', default='bham5')
    ap.add_argument('--fig', default='fig-b2')
    ap.add_argument('--future', default='2049')
    a = ap.parse_args()
    subprocess.run([sys.executable, str(REPO / 'scripts/shorts/hello_cut_r3.py'), '--voice', a.voice, '--fig', a.fig], check=True)
    BASE = MEDIA / 'cut' / f'r3-{a.voice}-{a.fig}'
    edl = json.loads((BASE / 'edl.json').read_text())
    CUT = MEDIA / 'cut' / 'r5'; CUT.mkdir(parents=True, exist_ok=True)
    WORK = CUT / '_scratch'; WORK.mkdir(exist_ok=True)
    said = [(e['t'], e['dur']) for e in edl['events'] if e['stem'] == 'vox-badcode']
    t_logo = round(said[3][0] + LOGO_AT, 3)
    rd = dur(REVEAL)
    total = round(t_logo + rd + HOLD + LOOP, 3)

    # Picture: rough cut 4's assembly up to the mark, the reveal (held), then a dissolve into the very first frame.
    r1.ff('-i', BASE / 'picture.mp4', '-t', t_logo, *r1.ENC, WORK / 'a.mp4')
    r1.ff('-i', REVEAL, '-an', '-vf', f'scale={W}:{H},fps={FPS},tpad=stop_mode=clone:stop_duration={HOLD + LOOP},format=yuv420p', *r1.ENC, WORK / 'b.mp4')
    r1.ff('-i', BASE / 'picture.mp4', '-t', LOOP + 0.1, *r1.ENC, WORK / 'head.mp4')
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
        caps += chunks(LINES[i], words, t)
    rows = edl['video']
    span = lambda beat: (min(r['start'] for r in rows if r['beat'] == beat), max(r['start'] + r['dur'] for r in rows if r['beat'] == beat))
    o0, o1 = span('hello'); f0, f1 = span('figure'); b0, b1 = span('back')
    vf, n = [], 0
    for s, e, txt in caps:
        f = WORK / f'cap{n:02d}.txt'; f.write_text(txt)
        col = 'white' if n % 2 == 0 else YELLOW; n += 1
        vf.append(f"drawtext=fontfile='{FONTS / 'Anton-Regular.ttf'}':textfile='{f}':fontsize=84:fontcolor={col}:borderw=7:bordercolor=black:"
                  f"x=(w-text_w)/2:y=h*0.70:enable='between(t,{s:.2f},{e + 0.08:.2f})'")
    vcr = lambda txt, x, y, s, e: (f"drawtext=fontfile='{FONTS / 'VT323-Regular.ttf'}':text='{txt}':fontsize=70:fontcolor=0xF2F2F2:"
                                   f"shadowcolor=black@0.7:shadowx=3:shadowy=3:x={x}:y={y}:enable='between(t,{s:.2f},{e:.2f})'")
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
    edl['flags'] = edl['flags'] + [f'The future date on BadCode ({a.future}) is a guess: nothing in the canon fixes the year. Say the year.',
                                   'Captions are timed by spreading each line across its spoken words (whisper word times), in groups of three.']
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': total, 'logo_at': t_logo, 'captions': len(caps), 'preview': str(CUT / 'preview.mp4')}))


if __name__ == '__main__':
    main()
