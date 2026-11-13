"""Parse the sealed writers' w1-w3.md into ../prompts-r6.json (stills, run verbatim + "Thanks.") and clips-r6.json (motion)."""
import json, re
from pathlib import Path
HERE = Path(__file__).parent
stills, clips = {}, {}
for w in ('w1', 'w2', 'w3'):
    t = (HERE / f'{w}.md').read_text()
    for m in re.finditer(r'=== SHOT (\w+) ===\s*STILL:\s*(.*?)\s*CLIP:\s*(.*?)(?=\n=== SHOT|\Z)', t, re.S):
        i, s, c = m.group(1), m.group(2).strip(), m.group(3).strip()
        stills[i] = {'run': s + '\n\nThanks.', 'writer': w}
        clips[i] = {'motion': c + '\n\nThanks.', 'writer': w}
(HERE.parent / 'prompts-r6.json').write_text(json.dumps(stills, indent=1))
(HERE / 'clips-r6.json').write_text(json.dumps(clips, indent=1))
print(len(stills), sorted(stills))
