#!/usr/bin/env python3
"""Cut r4 voices: trim edge silence (-55 dB, 0.12 s) and level each take to -18 LUFS (the v2 narration's level).
    python3 scripts/karen/finish-voice-r4.py <take.wav> ...   -> lvl_<take>.wav beside it, plus a recipe card."""
import json, pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
for f in map(pathlib.Path, sys.argv[1:]):
    tmp = f.with_name('trim_' + f.name)
    sr = 'silenceremove=start_periods=1:start_threshold=-55dB:start_silence=0.12'
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', f, '-af',
                    f'{sr},areverse,{sr},areverse', '-ar', '48000', '-ac', '2', tmp], check=True)
    st = subprocess.run(['ffmpeg', '-hide_banner', '-i', tmp, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    lufs = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', st)[-1])
    out = f.with_name('lvl_' + f.name)
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', tmp, '-af', f'volume={-18 - lufs:.2f}dB,alimiter=limit=0.95',
                    '-ar', '48000', '-ac', '2', out], check=True)
    tmp.unlink()
    subprocess.run(['python3', str(ROOT / 'scripts/provenance/prov.py'), 'card', str(out), '--kind', 'voice', '--engine', 'ffmpeg', '--tool',
                    'scripts/karen/finish-voice-r4.py', '--parent', str(f), '--why',
                    f'trimmed -55 dB/0.12 s, levelled {lufs:.1f} -> -18 LUFS'], capture_output=True)
    print(out.name, f'{lufs:.1f} -> -18')
