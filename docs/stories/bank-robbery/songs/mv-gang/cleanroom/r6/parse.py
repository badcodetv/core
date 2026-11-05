"""Parse round-6 writers (r6/wN.md) into cleanroom/prompts-r6.json and the scene's moodboard.json rows."""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
from shots import FAMILIES
meta = {s[0]: (w, *s[1:]) for w, shots in FAMILIES.items() for s in shots}
out = HERE.parent / "prompts-r6.json"
prompts, rows = {}, []
for w in FAMILIES:
    f = HERE / f"{w}.md"
    if not f.exists(): continue
    parts = re.split(r"^=== SHOT (\S+) ===\s*$", f.read_text(), flags=re.M)
    for sid, body in zip(parts[1::2], parts[2::2]):
        m = re.split(r"^WHY:\s*", body.strip(), flags=re.M)
        prompt, why = m[0].strip(), (m[1].strip() if len(m) > 1 else "")
        _, t, line, who, place = meta[sid]
        prompts[sid] = {"writer": w, "t": t, "line": line, "who": who, "place": place, "prompt": prompt, "why": why, "run": prompt + "\n\nThanks."}
        for k in "ab":
            rows.append(["rap", f"{sid}r6-{k}", f"{sid} · {t} · {who} · {place} · “{line}”", prompt])
out.write_text(json.dumps(prompts, indent=1, ensure_ascii=False))
(HERE.parents[1] / "moodboard.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False))
print(len(prompts), "prompts,", len(rows), "rows; missing:", sorted(set(meta) - set(prompts)))
