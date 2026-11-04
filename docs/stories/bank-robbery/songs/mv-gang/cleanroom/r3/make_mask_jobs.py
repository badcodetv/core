"""Mask-fix clips (Jack 2026-11-04: "please do the all 37"). For each clip in mask-audit.md: its new still (prompts-r5,
the take picked by eye in mask-picks.json) + the SAME motion prompt the old clip used -> a job '<shot>m-<take>' in
../../video-jobs.json 'extra'. Prints the keys to animate. plan_r3.py swaps each old clip for its 'm' clip where it exists."""
import json, pathlib
HERE = pathlib.Path(__file__).parent; SC = HERE.parents[1]
OLD = {  # shot -> the old clips (cut 4) with the wrong mask
    "d01": ["d01g-a"], "d06": ["d06g-a"], "f01": ["f01g-a"], "g11": ["g11-b"], "v03": ["v03g-b"], "v05": ["v05g-b"],
    "v06": ["v06g-b"], "v11": ["v11g-b"], "a01": ["a01-a", "a01-b"], "a02": ["a02-a", "a02-b"], "a03": ["a03-a", "a03-b"],
    "d02": ["d02-b"], "f03": ["f03-b"], "v07": ["v07-b"], "v12": ["v12-b"], "k01": ["k01-a"], "k02": ["k02-b"], "k03": ["k03-a"],
    "k04": ["k04-a"], "k09": ["k09-a"], "k12": ["k12-a"], "k13": ["k13-b"], "k18": ["k18-a"], "k19": ["k19-a"], "k21": ["k21-a"],
    "k22": ["k22-b"], "k26": ["k26-a"], "k27": ["k27-b"], "k29": ["k29-a"], "k30": ["k30-a"], "k31": ["k31-b"], "k36": ["k36-b"],
    "x03": ["x03-b"], "x07": ["x07-b"],
}
if __name__ == "__main__":
    picks = json.load(open(HERE / "mask-picks.json"))
    vj = json.load(open(SC / "video-jobs.json")); jobs = {j["key"]: j for j in vj["extra"]}
    keys, todo = [], []
    for shot, olds in OLD.items():
        take = picks.get(shot)
        if not take: todo.append(shot); continue
        for old in olds:
            new = f"{shot}m-{old.split('-')[1]}"
            if len(olds) > 1 and old != olds[0]:  # two old takes of one shot: the second gets the other new take if it passed, else the same still
                alt = picks.get(shot + "_2") or take
                still = f"{shot}r5-{alt}"
            else:
                still = f"{shot}r5-{take}"
            src = jobs[old]
            vj["extra"] = [j for j in vj["extra"] if j["key"] != new] + [{
                "key": new, "n": 0, "still": still, "motion": src["motion"], "character": None,
                "why": f"mask fix of {old} (r3/mask-audit.md): new still {still}, same motion as {old}"}]
            keys.append(new)
    json.dump(vj, open(SC / "video-jobs.json", "w"), indent=1, ensure_ascii=False)
    print(len(keys), "jobs:", " ".join(keys)); print("still waiting on a passing still:", todo)
