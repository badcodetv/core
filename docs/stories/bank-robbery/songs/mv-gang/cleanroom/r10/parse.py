"""r10/wN.md -> ../prompts-r10.json + moodboard rows (beat 'crew'); round-9 board rows kept in moodboard-r10-prev.json."""
import json, pathlib, re, sys, shutil
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from shots import SHOTS
meta = {s[0]: (w, s) for w, shots in SHOTS.items() for s in shots}
prompts, rows = {}, []
for w in SHOTS:
    f = HERE / f"{w}.md"
    if not f.exists(): continue
    parts = re.split(r"^=== SHOT (\S+) ===\s*$", f.read_text(), flags=re.M)
    for sid, body in zip(parts[1::2], parts[2::2]):
        m = re.split(r"^WHY:\s*", body.strip(), flags=re.M)
        prompt, why = m[0].strip(), (m[1].strip() if len(m) > 1 else "")
        s = meta[sid][1]
        prompts[sid] = {"writer": w, "place": s[1], "adjust": s[2], "prompt": prompt, "why": why, "run": prompt + "\n\nThanks."}
        label = f"{sid} · the whole gang at the lens · {s[1].split(',')[0]}"
        for k in "ab": rows.append(["crew", f"{sid}r10-{k}", label, prompt])
(HERE.parent / "prompts-r10.json").write_text(json.dumps(prompts, indent=1, ensure_ascii=False))
mb = HERE.parents[1] / "moodboard.json"
prev = HERE.parents[1] / "moodboard-r10-prev.json"
if not prev.exists(): shutil.copy(mb, prev)
mb.write_text(json.dumps(rows, indent=1, ensure_ascii=False))
print(len(prompts), "prompts,", len(rows), "rows; missing:", sorted(set(meta) - set(prompts)))
