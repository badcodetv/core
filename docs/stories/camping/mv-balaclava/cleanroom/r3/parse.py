"""Parse round-3 writers into ../prompts-r3.json and put the per-shot rows on the board (beats rough-shots / posh-shots)."""
import json, pathlib, re

HERE = pathlib.Path(__file__).parent
CR = HERE.parent
shots = json.load(open(HERE / "shots.json"))


def main():
    prompts, rows = {}, []
    for w in ("w1", "w2", "w3"):
        f = HERE / f"{w}.md"
        if not f.exists():
            print("missing", w); continue
        parts = re.split(r"^=== SHOT (\S+) ===\s*$", f.read_text(), flags=re.M)
        for sid, body in zip(parts[1::2], parts[2::2]):
            m = re.split(r"^WHY:\s*", body.strip(), flags=re.M)
            prompt, why = m[0].strip(), (m[1].strip() if len(m) > 1 else "")
            s = shots[sid]
            prompts[sid] = {**s, "prompt": prompt, "why": why, "run": prompt + "\n\nThanks."}
            beat = "rough-shots" if s["who"] == "rough" else "posh-shots"
            for k in "ab":
                rows.append([beat, f"{sid}r3-{k}", f"{sid} · replaces {s['clip']}", prompt])
    json.dump(prompts, open(CR / "prompts-r3.json", "w"), indent=1, ensure_ascii=False)
    mb = CR.parent / "moodboard.json"
    old = [r for r in json.load(open(mb)) if "r3-" not in r[1]]
    json.dump(rows + old, open(mb, "w"), indent=1, ensure_ascii=False)
    print(len(prompts), "prompts:", sorted(prompts))


if __name__ == "__main__":
    main()
