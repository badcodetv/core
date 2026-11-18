#!/usr/bin/env python3
"""Hello, I'm BadCode (BadCode Short #17): rough cut 3 (2026-11-18), the whole thing.
Jack: "cut 2B was way better but we don't know until we have the whole thing so let's finish the whole thing".

    python3 scripts/shorts/hello_cut_r3.py [--voice a-sadaltager] [--fig fig-a]

- Opening: rough cut 2b's real 2000s footage (Marseille bowl at dusk, Darling Harbour fireworks, the Monte Carlo arcade).
- BadCode in the launderette: the FG3-b clip animated on the tab pool (--fig picks which take), and again after the reel,
  closer, for Jack's line.
- Words: dialogue draft 1D (design/2026-11-18-hello-im-badcode-dialogue-script/options.json): 1B's two opening lines,
  Jack's line after the reel, "Here's what to do next." on black. Voice: one of the casting takes (--voice), from
  <media>/audio/casting/badcode-<voice>-l<N>.wav. BadCode's mask has no mouth, so nothing to lip-sync.
- Music: Jack's folktronica pick, dipped under the two opening lines, faded out as the reel slows: the end plays dry.
Writes <media>/cut/r3-<voice>-<fig>/.
"""
# style-lint: story=short-hello-im-badcode (this cut script belongs to one short)
import argparse, json, pathlib, subprocess, sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import hello_cut as r1  # noqa: E402  (the reel, push(), seg(), ff())
import hello_cut_r2 as r2  # noqa: E402  (REAL opening, clip(), MUSIC, FIG)

MEDIA, W, H, FPS = r1.MEDIA, r1.W, r1.H, r1.FPS
LINES = ["Hello. Enjoy this.", "I'm from the future. That was the good part.",
         "What do you think in your mind, what the worst-case scenario is? I'll be patiently waiting to correct your bullshit.",
         "Here's what to do next."]
BY = ['claude', 'claude', 'jack', 'kai']


def dur(p):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p],
                                capture_output=True, text=True).stdout)


def moving(src, tin, out, d, z0, z1):
    """A piece of the animated clip, with a slow eased push; held on its last frame if the clip runs out."""
    n = max(2, round(d * FPS))
    vf = (f'{r1.FILL},fps={FPS},tpad=stop_mode=clone:stop_duration={d + 1},scale={W * 2}:{H * 2},'
          f"zoompan=z='{z0}+({z1}-{z0})*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},format=yuv420p")
    r1.ff('-ss', tin, '-i', src, '-an', '-vf', vf, '-frames:v', n, *r1.ENC, out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--voice', default='a-sadaltager')
    ap.add_argument('--fig', default='fig-a')
    a = ap.parse_args()
    CUT = MEDIA / 'cut' / f'r3-{a.voice}-{a.fig}'; CUT.mkdir(parents=True, exist_ok=True)
    WORK = CUT / '_scratch'; WORK.mkdir(exist_ok=True)
    raw = [MEDIA / f'audio/casting/badcode-{a.voice}-l{i}.wav' for i in range(1, 5)]
    vo = []
    for i, p in enumerate(raw):  # the takes come with silence at both ends: trim it, keep 0.05 s of air
        o = WORK / f'vo-{i + 1}.wav'
        sr = 'silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05'
        r1.ff('-i', p, '-af', f'{sr},areverse,{sr},areverse', o); vo.append(o)
    vd = [dur(p) for p in vo]
    clipf = next((MEDIA / 'video').glob(f'*-{a.fig}-FG3-b.mp4'))
    cdur = dur(clipf)

    parts, rows, said, t = [], [], [], 0.0

    def add(path, d, beat, src, see):
        nonlocal t
        parts.append(path); rows.append({'file': str(path), 'in': 0, 'start': round(t, 3), 'dur': round(d, 3), 'beat': beat,
                                         'source': str(src), 'looped': False, 'note': see}); t += d

    def say(i, at):
        said.append((i, round(at, 3)))

    say(0, 0.6)
    for i, (src, d, see, tin) in enumerate(r2.REAL):
        out = WORK / f'p0{i}-open.mp4'
        r2.clip(src, tin, out, d) if tin is not None else r1.push(src, out, d, 1.0, 1.07, grade=False)
        add(out, d, 'hello', src, see)
    fig_d = round(max(2.9, vd[1] + 0.9), 2)
    say(1, t + 0.4)
    out = WORK / 'p10-fig.mp4'; moving(clipf, 0.3, out, fig_d, 1.0, 1.05); add(out, fig_d, 'figure', clipf, f'BadCode in the launderette ({a.fig}, animated)')
    reel_start = t
    for i, (key, kind, src, tin, credit) in enumerate(r1.SHOTS):
        last = i >= len(r1.SHOTS) - 3
        d = r1.REEL + (r1.SLOW / 3 if last else 0)
        out = WORK / f'p{i + 20:02d}-{key}.mp4'
        r1.seg(src, tin, out, d, speed=0.5 if last else 1.0) if kind == 'v' else r1.push(src, out, d, 1.0, 1.10)
        add(out, d, 'horror', src, 'AI-made (Flow) still' if kind == 'f' else f'real footage, {credit}')
    reel_end = t
    back_d = round(vd[2] + 1.0, 2)
    say(2, t + 0.4)
    out = WORK / 'p80-back.mp4'; moving(clipf, min(2.0, max(0.0, cdur - 2)), out, back_d, 1.15, 1.28)
    add(out, back_d, 'back', clipf, "back to BadCode, closer: Jack's line")
    black_d = round(max(r1.BLACK_D, vd[3] + 1.2), 2)
    say(3, t + 0.5)
    r1.ff('-f', 'lavfi', '-i', f'color=c=black:s={W}x{H}:r={FPS}:d={black_d}', *r1.ENC, WORK / 'p90-black.mp4')
    add(WORK / 'p90-black.mp4', black_d, 'button', 'black', 'black: "Here\'s what to do next."')
    r1.ff('-f', 'lavfi', '-i', f'color=c=black:s={W}x{H}:r={FPS}:d={r1.LOGO_D}', '-loop', 1, '-t', r1.LOGO_D, '-i', r1.LOGO, '-filter_complex',
          '[1]scale=640:-1[l];[0][l]overlay=(W-w)/2:(H-h)/2,fade=t=in:d=0.4,format=yuv420p', *r1.ENC, '-t', r1.LOGO_D, WORK / 'p91-logo.mp4')
    add(WORK / 'p91-logo.mp4', r1.LOGO_D, 'button', r1.LOGO, 'the BadCode logo')
    TOTAL = round(t, 3)

    (WORK / 'list.txt').write_text(''.join(f"file '{p.name}'\n" for p in parts))
    r1.ff('-f', 'concat', '-safe', '0', '-i', WORK / 'list.txt', '-c', 'copy', CUT / 'picture.mp4')

    # Voice: every line at its time on one track. Music: dipped under the opening lines, gone by the end of the reel.
    vox = CUT / 'vox-badcode.wav'
    ins = sum([['-i', p] for p in vo], [])
    mix = ''.join(f'[{i}]loudnorm=I=-16:TP=-2,aresample=48000,adelay={int(at * 1000)}:all=1[v{i}];' for i, at in said)
    r1.ff(*ins, '-filter_complex', mix + ''.join(f'[v{i}]' for i, _ in said) + f'amix=inputs={len(said)}:normalize=0,apad=whole_dur={TOTAL},atrim=end={TOTAL}', '-ac', 2, vox)
    mdur = dur(r2.MUSIC)
    fade_at = max(0.0, min(mdur, reel_end) - 1.5)
    dips = '+'.join(f'between(t,{at - 0.2:.2f},{at + vd[i] + 0.2:.2f})' for i, at in said if at < reel_start)
    mus = CUT / 'mus-track.wav'
    r1.ff('-i', r2.MUSIC, '-af', f"loudnorm=I=-15:TP=-2,volume='if({dips},0.4,1)':eval=frame,afade=t=out:st={fade_at:.2f}:d=1.5,"
          f'apad=whole_dur={TOTAL},atrim=end={TOTAL}', '-ar', 48000, '-ac', 2, mus)
    r1.ff('-i', CUT / 'picture.mp4', '-i', vox, '-i', mus, '-filter_complex', '[1][2]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5[a]',
          '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-ar', 48000, '-t', TOTAL, CUT / 'preview.mp4')

    beat = lambda b: [r for r in rows if r['beat'] == b]
    span = lambda b: (beat(b)[0]['start'], round(sum(r['dur'] for r in beat(b)), 3))
    ln = lambda i: {'i': 0, 'who': 'badcode', 'name': f'BadCode ({a.voice})', 't': dict(said)[i], 'dur': round(vd[i], 3), 'text': LINES[i], 'by': BY[i]}
    beats = [{'id': 'hello', 'title': 'A. "Hello. Enjoy this."', 'start': span('hello')[0], 'dur': span('hello')[1], 'see': 'Real 2000s footage: the skatepark at dusk, harbour fireworks, the neon arcade.', 'lines': [ln(0)]},
             {'id': 'figure', 'title': 'B. "I\'m from the future."', 'start': span('figure')[0], 'dur': span('figure')[1], 'see': 'BadCode in the launderette, moving.', 'lines': [ln(1)]},
             {'id': 'horror', 'title': 'C. The horror reel', 'start': span('horror')[0], 'dur': span('horror')[1], 'see': 'Real footage and Flow gap stills; the music dies.', 'lines': []},
             {'id': 'back', 'title': "D. Jack's line", 'start': span('back')[0], 'dur': span('back')[1], 'see': 'Back to BadCode, closer, no music.', 'lines': [ln(2)]},
             {'id': 'button', 'title': 'E. "Here\'s what to do next." + logo', 'start': span('button')[0], 'dur': span('button')[1], 'see': 'Black, the line, the logo.', 'lines': [ln(3)]}]
    credits = sorted({r['note'].split('real footage, ')[1] for r in rows if 'real footage, ' in r['note']} |
                     {s.split('(')[-1].rstrip(')') for _, _, s, _ in r2.REAL})
    edl = {'sequence': f'short-hello-im-badcode-1-hello-r3-{a.voice}-{a.fig}', 'title': 'Hello Im BadCode Timeline',
           'heading': "BadCode Shorts ▲ Hello, I'm BadCode, rough cut 3 (the whole thing)",
           'intro': ("The whole short: cut 2b's real opening, BadCode moving in the launderette, the words (draft 1D: your line after "
                     "the reel), a cast voice, the music dying into the end. Note anything."),
           'fps': FPS, 'total': TOTAL, 'beats': beats, 'video': rows,
           'audio': [{'track': 'A1', 'name': 'vox-badcode', 'file': str(vox)}, {'track': 'A2', 'name': 'mus-track', 'file': str(mus)}],
           'events': [{'stem': 'vox-badcode', 't': at, 'dur': round(vd[i], 3), 'what': LINES[i], 'src': str(vo[i])} for i, at in said] +
                     [{'stem': 'mus-track', 't': 0, 'dur': round(min(mdur, TOTAL), 3), 'what': "Suno folktronica take 1 (Jack's pick), dips under the voice, dies with the reel", 'src': str(r2.MUSIC)}],
           'flags': ['Footage credits owed in the description: ' + '; '.join(credits) + '.',
                     'Flow-made pictures (BadCode, the reel gap stills) are cut between real footage, never composited into it.',
                     'The arcade photo is a 960 px preview: fetch the original before the final export.']}
    (CUT / 'edl.json').write_text(json.dumps(edl, indent=1, ensure_ascii=False))
    print(json.dumps({'total': TOTAL, 'lines': said, 'preview': str(CUT / 'preview.mp4')}))


if __name__ == '__main__':
    main()
