"""Mask-fix round (Jack 2026-11-04 on Balaclava Gang 4: "the masks are wrong in a lot of the clips, watch and look for it then replace it").
Checked by eye: in these shots' STILLS the red triangle sits in the middle of the face, on the wrong side, or is missing.
Each prompt is the shot's own picked prompt, run again (a deliberate re-roll, not a new idea), with one sentence added that
points at the enlarged heads now on the reference (~/.cache/badcode-refs/gang/gang-lineup-heads.jpg). -> ../prompts-r5.json
Run: ROUND=-r5 PER_PROJECT=1 REF=$HOME/.cache/badcode-refs/gang/gang-lineup-heads.jpg npx tsx run_stills.mts"""
import json, pathlib
HERE = pathlib.Path(__file__).parent; CR = HERE.parent
P2 = json.load(open(CR / "prompts-r2.json")); P3 = json.load(open(CR / "prompts-r3.json"))
SHOTS = {  # shot -> what was wrong in its still
    "c04": "triangle too small to read", "d01": "triangle in the middle of the face", "d02": "triangle in the middle",
    "d06": "triangle in the middle", "d11": "no triangle", "d12": "triangle left of centre", "f01": "triangle in the middle",
    "f03": "triangle in the middle", "g08": "triangle in the middle", "g09": "triangle in the middle", "v03": "no triangle",
    "v05": "triangle left of centre", "v06": "triangle in the middle", "v07": "no triangle", "v08": "no triangle",
    "v11": "triangle in the middle", "v12": "triangle in the middle", "x02": "triangle on the left", "k09": "triangle on the left",
    "k18": "no triangle", "k30": "triangle in the middle on SILVER",
    # batch 2 (full audit, r3/mask-audit.md)
    "a01": "eye shapes, no triangles", "a02": "red eye/face shapes", "a03": "eye holes, RUST has no ring",
    "x03": "eyes and eye holes", "x07": "SILVER has eye holes", "k01": "no triangles", "k02": "goggles, eye holes",
    "k03": "triangle in the middle", "k04": "eye holes, CRIMSON has none", "k12": "eye and mouth holes", "k13": "red eyes",
    "k19": "red eye marks", "k21": "no triangles", "k22": "triangle in the middle", "k26": "three without a triangle",
    "k27": "PLUM's triangle in the middle", "k29": "two red marks", "k31": "PLUM's triangle in the middle", "k36": "three wrong",
    "g11": "two red eye holes",
}
FIX = ("The bottom half of the attached reference shows each mask's face up close: copy it exactly. On every mask the small red "
       "felt triangle points left and sits in the upper-right part of the face inside the white ring, about halfway between the middle "
       "of the face and the ring, at the position of 1 to 2 o'clock on a clock face; it is on the right-hand side of the picture when the "
       "man faces the camera, and the rest of the face inside the ring is plain knit.")
out = {}
for s, why in SHOTS.items():
    p = (P3 if s[0] in "gk" else P2)[s]
    run = p["run"].rstrip()
    body = run[: -len("Thanks.")].rstrip() if run.endswith("Thanks.") else run
    out[s] = {**p, "fixes": why, "run": body + " " + FIX + "\n\nThanks."}
(CR / "prompts-r5.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
print(len(out), "prompts ->", CR / "prompts-r5.json")
