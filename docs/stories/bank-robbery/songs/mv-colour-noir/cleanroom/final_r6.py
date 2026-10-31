"""Point the sung rows of cut-r6.json at the chosen lip-sync take (ls-choice-r6.json), check every row has a file, and write build-r6.json for Premiere."""
import json, os, pathlib
HERE = pathlib.Path(__file__).parent
rows = json.load(open(HERE / "cut-r6.json")); use = json.load(open(HERE / "ls-choice-r6.json"))
out = []
for r in rows:
    f = r.get("file") or r["src"]
    if r["lip"]:
        name = f"{r['n']:03d}-{r['clip']}"
        if use.get(name) == "v2": f = f"{os.path.dirname(f)}/v2/{name}.mp4"
    assert os.path.exists(f), f
    out.append(dict(n=r["n"], start=r["start"], end=r["end"], clip=r["clip"], lip=r["lip"], path=f, inPoint=r["inPoint"]))
json.dump(out, open(HERE / "build-r6.json", "w"), indent=0)
print(len(out), "rows,", len({o['path'] for o in out}), "files; gaps:", [(a['n'], round(b['start'] - a['end'], 3)) for a, b in zip(out, out[1:]) if abs(b['start'] - a['end']) > .001])
