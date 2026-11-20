#!/usr/bin/env python3
"""Photosensitive-epilepsy gate. Run before ANY upload that contains a flash, strobe or alarm.

Implements the WCAG 2.3.1 / Harding general-flash and red-flash tests:

  * relative luminance L = 0.2126R + 0.7152G + 0.0722B on LINEARISED sRGB (0..1)
  * a TRANSITION is a change of >= 0.10 in L where the darker state is < 0.80,
    occurring over >= 25% of the frame
  * a FLASH is a pair of opposing transitions (up then down, or down then up)
  * FAIL = more than 3 flashes in any 1-second window
  * the RED test is the same, on the area that changes into or out of saturated red
    (R/(R+G+B) >= 0.8), because saturated red flash is a separate and stricter risk

Simplification, stated honestly: the standard measures the flashing area inside any 10-degree
visual field. This measures it across the whole frame, which is the usual tool simplification
and is CONSERVATIVE for a full-frame flash and PERMISSIVE for a small bright one. A clip that
passes here with a small, intense, localised flash still deserves a human look.

Usage:  photosensitivity-check.py <file.mp4> [more.mp4 ...]
"""
import subprocess, sys
import numpy as np

W, H, FPS_ASSUME = 480, 270, None
THRESH_L, DARK_MAX, AREA_MIN, LIMIT = 0.10, 0.80, 0.25, 3

def decode(path):
    probe = subprocess.run(["ffprobe","-v","error","-select_streams","v:0",
        "-show_entries","stream=r_frame_rate","-of","csv=p=0",path],
        capture_output=True, text=True).stdout.strip()
    num, den = (probe.split("/") + ["1"])[:2]
    fps = float(num)/float(den)
    # Streamed in chunks (2026-11-20, Jack: "things are running slow"): decoding a whole 98 s cut to float RGB at once, plus
    # the copies linearise made, took several GB and swapped the machine for 10+ minutes. Only L and the red mask are kept.
    proc = subprocess.Popen(["ffmpeg","-v","error","-i",path,"-vf",f"scale={W}:{H}",
        "-pix_fmt","rgb24","-f","rawvideo","-"], stdout=subprocess.PIPE)
    frame, Ls, reds = W*H*3, [], []
    while True:
        raw = proc.stdout.read(frame*120)
        n = len(raw)//frame
        if n == 0: break
        rgb = np.frombuffer(raw[:n*frame], np.uint8).reshape(n, H*W, 3).astype(np.float32)/255.0
        lin = linearise(rgb)
        Ls.append((lin[:,:,0]*0.2126 + lin[:,:,1]*0.7152 + lin[:,:,2]*0.0722).astype(np.float32))
        reds.append((rgb[:,:,0]/(rgb.sum(axis=2) + 1e-6)) >= 0.8)   # saturated-red mask, per pixel
    proc.wait()
    return np.concatenate(Ls), np.concatenate(reds), fps

def linearise(c):
    return np.where(c <= 0.04045, c/12.92, ((c+0.055)/1.055)**2.4)

def analyse(path):
    L, red, fps = decode(path)

    def transitions(state_L, state_mask=None):
        """Walk frames, holding the last accepted state as reference."""
        ref_i, out = 0, []
        for i in range(1, len(state_L)):
            d = state_L[i] - state_L[ref_i]
            hit = (np.abs(d) >= THRESH_L) & (np.minimum(state_L[i], state_L[ref_i]) < DARK_MAX)
            if state_mask is not None:
                hit &= (state_mask[i] != state_mask[ref_i])
            area = hit.mean()
            if area >= AREA_MIN:
                out.append((i, 1 if d[hit].mean() > 0 else -1, area))
                ref_i = i
        return out

    def flashes(trs):
        """A flash is a pair of OPPOSING transitions."""
        f = []
        for a, b in zip(trs, trs[1:]):
            if a[1] != b[1]:
                f.append(b[0])
        return f

    def worst_per_second(frame_idxs):
        if not frame_idxs: return 0, None
        best, at = 0, None
        for f in frame_idxs:
            win = [x for x in frame_idxs if f <= x < f + fps]
            if len(win) > best: best, at = len(win), f/fps
        return best, at

    gen = flashes(transitions(L))
    redf = flashes(transitions(L, red))
    g_n, g_at = worst_per_second(gen)
    r_n, r_at = worst_per_second(redf)
    return dict(frames=len(L), fps=fps, general=g_n, general_at=g_at,
                red=r_n, red_at=r_at,
                verdict="FAIL" if (g_n > LIMIT or r_n > LIMIT) else "pass")

if __name__ == "__main__":
    worst = "pass"
    print(f"{'clip':<26} {'frames':>6} {'gen/s':>6} {'red/s':>6}  verdict   worst moment")
    print("-"*78)
    for p in sys.argv[1:]:
        r = analyse(p)
        if r["verdict"] == "FAIL": worst = "FAIL"
        at = f"gen@{r['general_at']:.2f}s" if r["general_at"] is not None else ""
        at += f" red@{r['red_at']:.2f}s" if r["red_at"] is not None else ""
        mark = "🔴" if r["verdict"]=="FAIL" else "✅"
        print(f"{p.split('/')[-1]:<26} {r['frames']:>6} {r['general']:>6} {r['red']:>6}  {mark} {r['verdict']:<6} {at}")
    print("-"*78)
    print(f"LIMIT: more than {LIMIT} flashes in any 1s window fails.   OVERALL: {worst}")
    sys.exit(1 if worst == "FAIL" else 0)
