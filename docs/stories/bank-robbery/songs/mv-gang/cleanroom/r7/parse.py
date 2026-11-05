"""r7/wN.md -> cleanroom/prompts-r7.json + the scene's moodboard.json rows (beats 'fixes', 'rap')."""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from shots import FIXES, RAP
meta = {s[0]: (w, s) for d in (FIXES, RAP) for w, shots in d.items() for s in shots}
prompts, rows = {}, []
for w in list(FIXES) + list(RAP):
    f = HERE / f"{w}.md"
    if not f.exists(): continue
    parts = re.split(r"^=== SHOT (\S+) ===\s*$", f.read_text(), flags=re.M)
    for sid, body in zip(parts[1::2], parts[2::2]):
        m = re.split(r"^WHY:\s*", body.strip(), flags=re.M)
        prompt, why = m[0].strip(), (m[1].strip() if len(m) > 1 else "")
        s = meta[sid][1]
        d = {"writer": w, "t": s[1], "line": s[2], "prompt": prompt, "why": why, "run": prompt + "\n\nThanks."}
        if sid[0] == "z": d["what"] = s[3]
        else: d["who"], d["place"] = s[3], s[4]
        prompts[sid] = d
        beat = "fixes" if sid[0] == "z" else "rap"
        label = f"{sid} · {s[1]} · " + (s[3].split(':')[0] if sid[0] == "z" else f"{s[3]} · {s[4]}") + f" · “{s[2]}”"
        for k in "ab": rows.append([beat, f"{sid}r7-{k}", label, prompt])
(HERE.parent / "prompts-r7.json").write_text(json.dumps(prompts, indent=1, ensure_ascii=False))
(HERE.parents[1] / "moodboard.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False))
print(len(prompts), "prompts,", len(rows), "rows; missing:", sorted(set(meta) - set(prompts)))
