#!/usr/bin/env python3
"""Rough trailer previews cut from the Camping story master (Jack, 2026-11-12: "more like fast trailers").

Each trailer is a list of events, in order:
  ("line", a_in, a_out, [(pic_t, dur), ...])  film audio a_in..a_out (+ small pad); picture = the listed shots,
                                               the last one stretched/trimmed to fill. [] = the line's own picture.
  ("flash", pic_t, dur, vol)                   a quick picture insert with its own audio at `vol`
  ("card", dur)                                end card on black
Word times come from faster-whisper small.en on the master (scratchpad camping-words.json, 2026-11-12).
These are review previews for the plan page, not the cut: the real one is built in Premiere.

Usage: build_trailers.py <master.mp4> <out_dir>
"""
import subprocess, sys, os, tempfile

FONT = "/usr/share/fonts/type1/urw-base35/NimbusSans-Bold.t1"
PAD_IN, PAD_OUT = 0.10, 0.18
W, H = 960, 540

TRAILERS = {
  "t1": [  # Good business: Tarquin's rise and fall
    ("line", 0.00, 1.90, [(0.0, 9)]),
    ("line", 28.24, 33.68, [(16.0, 2.0), (8.5, 1.6), (32.0, 9)]),
    ("line", 36.34, 37.32, [(8.0, 9)]),
    ("flash", 68.0, 0.6, 0.6),
    ("line", 70.45, 71.95, [(72.0, 9)]),
    ("line", 77.18, 82.48, [(84.0, 2.0), (88.0, 1.6), (92.0, 9)]),
    ("line", 132.36, 136.30, [(128.0, 2.0), (133.0, 9)]),
    ("flash", 216.0, 0.7, 0.1),
    ("line", 214.60, 216.56, [(222.0, 9)]),
    ("line", 234.98, 239.72, [(236.0, 2.0), (244.0, 1.4), (248.0, 9)]),
    ("line", 256.26, 259.96, [(266.0, 2.0), (272.0, 9)]),
    ("flash", 284.0, 2.0, 1.0),
    ("card", 2.2),
  ],
  "t2": [  # Two men, one car park: Bob against Tarquin
    ("line", 57.94, 60.24, [(60.0, 9)]),
    ("line", 61.22, 62.44, [(44.0, 9)]),
    ("flash", 64.6, 0.5, 1.0),
    ("flash", 68.0, 1.2, 1.0),
    ("line", 152.46, 154.66, [(152.0, 9)]),
    ("line", 158.22, 161.50, [(160.0, 1.5), (168.0, 9)]),
    ("line", 110.42, 114.54, [(104.0, 1.5), (113.0, 9)]),
    ("line", 170.90, 172.30, [(146.0, 9)]),
    ("line", 173.04, 175.46, [(176.0, 9)]),
    ("line", 179.94, 180.94, [(180.0, 9)]),
    ("line", 251.95, 254.76, [(230.0, 9)]),
    ("flash", 277.0, 1.6, 1.0),
    ("flash", 284.0, 2.0, 1.0),
    ("card", 2.2),
  ],
  "t3": [  # Rapid fire: one punch per cut
    ("line", 17.20, 19.36, [(8.0, 9)]),
    ("line", 36.34, 37.32, [(16.0, 9)]),
    ("line", 81.68, 82.48, [(92.0, 9)]),
    ("line", 110.42, 111.40, [(104.0, 9)]),
    ("line", 125.50, 127.44, [(133.0, 9)]),
    ("line", 152.46, 154.66, [(152.0, 9)]),
    ("line", 203.76, 204.80, [(200.0, 9)]),
    ("flash", 216.0, 0.4, 0.1),
    ("line", 238.78, 239.72, [(236.0, 9)]),
    ("flash", 284.0, 1.8, 1.0),
    ("card", 2.2),
  ],
}

VENC = ["-c:v", "libx264", "-crf", "28", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", "24"]
AENC = ["-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-ac", "2"]


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def seg_line(src, a_in, a_out, shots, out):
    t0, t1 = max(0, a_in - PAD_IN), a_out + PAD_OUT
    dur = t1 - t0
    shots = shots or [(t0, dur)]
    # lay shots end to end; the last fills the remainder
    plan, used = [], 0.0
    for i, (pt, d) in enumerate(shots):
        d = dur - used if i == len(shots) - 1 else min(d, dur - used)
        if d <= 0.04:
            break
        plan.append((pt, d)); used += d
    cmd = ["ffmpeg", "-y"]
    for pt, d in plan:
        cmd += ["-ss", f"{pt:.3f}", "-t", f"{d:.3f}", "-i", src]
    cmd += ["-ss", f"{t0:.3f}", "-t", f"{dur:.3f}", "-i", src]
    fc = "".join(f"[{i}:v]scale={W}:{H},setsar=1,fps=24[v{i}];" for i in range(len(plan)))
    fc += "".join(f"[v{i}]" for i in range(len(plan))) + f"concat=n={len(plan)}:v=1:a=0[v];"
    fc += f"[{len(plan)}:a]afade=t=in:d=0.04,afade=t=out:st={dur-0.06:.3f}:d=0.06[a]"
    cmd += ["-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-t", f"{dur:.3f}"] + VENC + AENC + [out]
    run(cmd)


def seg_flash(src, pt, d, vol, out):
    run(["ffmpeg", "-y", "-ss", f"{pt:.3f}", "-t", f"{d:.3f}", "-i", src,
         "-vf", f"scale={W}:{H},setsar=1,fps=24",
         "-af", f"volume={vol},afade=t=in:d=0.03,afade=t=out:st={max(0, d-0.08):.3f}:d=0.08"] + VENC + AENC + [out])


def seg_card(d, out):
    txt = (f"drawtext=fontfile={FONT}:text='CAMPING':fontcolor=white:fontsize=96:x=(w-tw)/2:y=(h/2)-90,"
           f"drawtext=fontfile={FONT}:text='the full film is on our channel':fontcolor=0xd7262e:fontsize=34:x=(w-tw)/2:y=(h/2)+30")
    run(["ffmpeg", "-y", "-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:r=24:d={d}",
         "-f", "lavfi", "-i", f"anullsrc=r=48000:cl=stereo", "-t", f"{d}", "-vf", txt] + VENC + AENC + [out])


def build(src, name, events, out_dir):
    with tempfile.TemporaryDirectory() as tmp:
        parts = []
        for i, ev in enumerate(events):
            p = os.path.join(tmp, f"{i:02d}.mp4")
            if ev[0] == "line":
                seg_line(src, ev[1], ev[2], ev[3], p)
            elif ev[0] == "flash":
                seg_flash(src, ev[1], ev[2], ev[3], p)
            else:
                seg_card(ev[1], p)
            parts.append(p)
        lst = os.path.join(tmp, "list.txt")
        with open(lst, "w") as f:
            f.writelines(f"file '{p}'\n" for p in parts)
        out = os.path.join(out_dir, f"{name}.mp4")
        run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst] + VENC + AENC + ["-movflags", "+faststart", out])
        return out


if __name__ == "__main__":
    src, out_dir = sys.argv[1], sys.argv[2]
    os.makedirs(out_dir, exist_ok=True)
    for name, evs in TRAILERS.items():
        print(build(src, name, evs, out_dir))
