"""Round 5 lip-sync fit. For each take: the song phrase's span against the mouth's speech span in the clip, a closure/opening
table to read, and the Whisper of the clip's own audio. Song word times are Whisper's, tightened to the local vocal-band energy rise; picture
is the master for the mouth (lip-sync-dub skill). Run with ~/.cache/badcode-lips/venv/bin/python fit_r5.py <video dir> <out dir> <song16.wav>"""
import json, pathlib, subprocess, sys
import numpy as np
import soundfile as sf
HERE = pathlib.Path(__file__).parent
VIDEO, OUT, SONG = sys.argv[1], pathlib.Path(sys.argv[2]), sys.argv[3]
OUT.mkdir(parents=True, exist_ok=True)
REPO = HERE.parents[5]
PHRASES = {  # id: (first word time, last word end, words)
    "l01": (66.50, 70.00, "don't be hating on the credit rating"), "l02": (70.20, 74.30, "or have resistance to the facts I'm stating"),
    "l03": (140.34, 143.50, "it is state level manipulation"), "l04": (143.72, 147.70, "it is the devil with a radio station"),
    "l05": (154.52, 158.10, "Biggie said way back in ninety seven"), "l06": (158.26, 162.20, "don't get high off your own supply"),
    "c1": (177.04, 179.90, "Robbery, robbery"), "c2": (180.04, 183.20, "Call the police, it's a robbery"), "c3": (183.34, 186.00, "Debasement, debasement"),
    "c4": (186.08, 188.00, "It happened in da basement"), "c5": (188.12, 191.15, "Printer is burning, now now what's occurring"),
    "e1": (199.76, 202.35, "stacking up the cash by the grands"), "e2": (202.40, 205.70, "standard plans are for the working man"),
    "e3": (206.10, 209.40, "and this right here is a next level scam"), "e4": (209.50, 213.15, "ill gotten gains, no need to explain"),
    "f1": (220.48, 222.30, "crime is asset inflation"), "f2": (222.38, 225.50, "passive creation of a wealth gap"), "f3": (225.58, 227.75, "that drives the situation"),
    "f4": (227.80, 230.15, "working people get paid in money"), "f5": (230.18, 231.90, "so it's not very funny"), "f6": (231.92, 235.05, "when you print more and expect them not to worry"),
    "f7": (235.12, 238.25, "hungry people feed a revolution"), "f8": (238.32, 241.95, "then it's retribution, perhaps some execution"),
}
y, sr = sf.read(SONG)
rms = lambda a, b: np.sqrt(np.mean(y[int(a * sr):int(b * sr)] ** 2) + 1e-12)
def tighten(t):
    grid = np.arange(t - 0.35, t + 0.25, 0.01)
    env = np.array([rms(g, g + 0.03) for g in grid])
    rise = env[6:] - env[:-6]
    return float(grid[int(np.argmax(rise)) + 6])
rows = {}
for pid, (a, b, words) in PHRASES.items():
    onset = tighten(a)
    rows[pid] = {"words": words, "song_on": round(onset, 2), "song_off": b, "song_len": round(b - onset, 2), "takes": {}}
    for tag in "abcd":
        clip = f"{VIDEO}/{pid}-{tag}.mp4"
        if not pathlib.Path(clip).exists(): continue
        js = OUT / f"{pid}-{tag}.jpg"
        r = subprocess.run([sys.executable, str(REPO / "scripts/lipsync/mouth-track.py"), clip, str(js)], capture_output=True, text=True)
        info = {"opens": "", "strip": str(js), "log": r.stdout[-900:]}
        data = json.load(open(str(js) + ".json")) if pathlib.Path(str(js) + ".json").exists() else None
        g = np.array([np.nan if x is None else x for x in (data.get("gap") if isinstance(data, dict) else data or [])], float) if data else np.array([])
        if len(g):
            fps = 24.0
            d = np.abs(np.diff(np.nan_to_num(g, nan=0)))
            th = max(np.nanpercentile(d, 70), 1e-3)
            mov = np.convolve(d > th, np.ones(5), "same") >= 3
            idx = np.where(mov)[0]
            if len(idx):
                info["speech_on"] = round(idx[0] / fps, 2)
                info["speech_off"] = round(idx[-1] / fps, 2)
                info["speech_len"] = round((idx[-1] - idx[0]) / fps, 2)
                info["ratio"] = round(rows[pid]["song_len"] / max(info["speech_len"], .1), 2)
            info["face_missing"] = int(np.isnan(g).sum())
        rows[pid]["takes"][tag] = info
json.dump(rows, open(OUT / "fit.json", "w"), indent=1)
for pid, r in rows.items():
    print(pid, r["song_on"], r["song_len"], {t: (i.get("speech_on"), i.get("speech_len"), i.get("ratio"), i.get("face_missing")) for t, i in r["takes"].items()})
