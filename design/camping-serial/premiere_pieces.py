#!/usr/bin/env python3
"""Cut one Camping trailer (spec in build_trailers.py) into Premiere pieces for a vertical 1080x1920 short.

Jack 2026-11-12: Trailer 2 kept; film's own audio + hits; letterbox + text; project in the shorts folder.
  V1  picture shots, each its own file, letterboxed (1080x608 centred on black), no audio
  V2  title "CAMPING" in the top band, whole trailer (alpha .mov)
  V3  one caption per line in the bottom band, the film's own words (alpha .mov)
  A1  the line audio + flash audio, each its own .wav (gain baked)
  A2  synthesised sub hits on the big cuts
The end card is a V1 piece. Writes <out>/plan.json and <out>/place.js (the premiere_eval body).

Usage: premiere_pieces.py <master.mp4> <trailer id> <out dir> <sequence name>
"""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_trailers import TRAILERS, PAD_IN, PAD_OUT
from PIL import Image, ImageDraw, ImageFont

W, H, PW, PH = 1080, 1920, 1080, 608
FPS = 24
PY = (H - PH) // 2
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
RED = (215, 38, 46, 255)

# the film's own words, per line event (a_in -> caption); profanity in full
CAPTIONS = {
    57.94: "She wanted to leave early to miss the traffic.",
    61.22: "I said there was no rush.",
    152.46: "Get a job, you fuckwit.",
    158.22: "Even if I give you money, you'll shoot it up your arm.",
    110.42: "Couldn't give a fuck, mate. I just wanted a sandwich, for Christ's sake.",
    170.90: "Fucking wank tanks.",
    173.04: "Different car. Different fella.",
    179.94: "Just the one man.",
    251.95: "That's not greed. That's foresight.",
}
HIT_ON = {"flash": [68.0, 277.0, 284.0], "card": True}  # sub hit at the start of these


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def snap(t):
    return round(t * FPS) / FPS


def win(p):
    p = os.path.abspath(p)
    assert p.startswith("/mnt/"), p
    return p[5].upper() + ":\\" + p[7:].replace("/", "\\")


def vpiece(src, t, d, out):
    run(["ffmpeg", "-y", "-ss", f"{t:.3f}", "-t", f"{d:.4f}", "-i", src, "-an",
         "-vf", f"scale={PW}:{PH},pad={W}:{H}:0:{PY}:black,setsar=1,fps={FPS}",
         "-c:v", "libx264", "-crf", "14", "-preset", "medium", "-pix_fmt", "yuv420p", "-r", str(FPS), out])


def apiece(src, t, d, vol, out):
    run(["ffmpeg", "-y", "-ss", f"{t:.3f}", "-t", f"{d:.4f}", "-i", src, "-vn",
         "-af", f"volume={vol},afade=t=in:d=0.03,afade=t=out:st={max(0, d - 0.06):.3f}:d=0.06",
         "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", out])


def hit(out):
    # a 1.2 s sub drop: 70 -> 38 Hz sine with a fast attack and exponential tail, plus a short noise thump
    run(["ffmpeg", "-y", "-f", "lavfi", "-i",
         "aevalsrc='0.9*sin(2*PI*(38*t+32*(1-exp(-6*t))/6))*exp(-3.2*t)+0.25*(random(0)*2-1)*exp(-40*t)':s=48000:d=1.2",
         "-af", "lowpass=f=180,afade=t=in:d=0.004,volume=0.9", "-ac", "2", "-c:a", "pcm_s16le", out])


def text_png(lines, size, color, y_center, path, stroke=6):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(BOLD, size)
    lh = int(size * 1.22)
    y = y_center - lh * len(lines) // 2
    for ln in lines:
        w = d.textlength(ln, font=f)
        d.text(((W - w) / 2, y), ln, font=f, fill=color, stroke_width=stroke, stroke_fill=(0, 0, 0, 255))
        y += lh
    img.save(path)


def wrap(text, size, maxw=W - 140):
    f = ImageFont.truetype(BOLD, size)
    d = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    out, cur = [], ""
    for w in text.split():
        nxt = (cur + " " + w).strip()
        if d.textlength(nxt, font=f) > maxw and cur:
            out.append(cur); cur = w
        else:
            cur = nxt
    return out + [cur]


def still_mov(png, d, out):
    run(["ffmpeg", "-y", "-loop", "1", "-framerate", str(FPS), "-t", f"{d:.4f}", "-i", png,
         "-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le", "-r", str(FPS), out])


def main(src, tid, out, seq):
    for sub in ("video", "audio", "text"):
        os.makedirs(os.path.join(out, sub), exist_ok=True)
    V, A, T = [], [], []  # [path, start, dur, track]
    t = 0.0
    n = 0
    hit_wav = os.path.join(out, "audio", "hit.wav"); hit(hit_wav)
    for ev in TRAILERS[tid]:
        n += 1
        if ev[0] == "line":
            a0, a1 = max(0, ev[1] - PAD_IN), ev[2] + PAD_OUT
            dur = snap(a1 - a0)
            ap = os.path.join(out, "audio", f"{n:02d}-line-{ev[1]:.0f}.wav"); apiece(src, a0, dur, 1.0, ap)
            A.append([ap, t, dur, 0])
            used, shots = 0.0, ev[3] or [(a0, dur)]
            for i, (pt, d) in enumerate(shots):
                d = dur - used if i == len(shots) - 1 else snap(min(d, dur - used))
                if d <= 0.04: break
                vp = os.path.join(out, "video", f"{n:02d}{chr(97 + i)}-shot-{pt:.0f}.mp4"); vpiece(src, pt, d, vp)
                V.append([vp, t + used, d, 0]); used += d
            if ev[1] in CAPTIONS:
                png = os.path.join(out, "text", f"{n:02d}-caption.png")
                text_png(wrap(CAPTIONS[ev[1]], 58), 58, (255, 255, 255, 255), PY + PH + 170, png)
                mov = png[:-4] + ".mov"; still_mov(png, dur, mov); T.append([mov, t, dur, 2])
            t = snap(t + dur)
        elif ev[0] == "flash":
            d = snap(ev[2])
            vp = os.path.join(out, "video", f"{n:02d}-flash-{ev[1]:.0f}.mp4"); vpiece(src, ev[1], d, vp)
            ap = os.path.join(out, "audio", f"{n:02d}-flash-{ev[1]:.0f}.wav"); apiece(src, ev[1], d, ev[3], ap)
            V.append([vp, t, d, 0]); A.append([ap, t, d, 0])
            if ev[1] in HIT_ON["flash"]: A.append([hit_wav, t, 1.2, 1])
            t = snap(t + d)
        else:  # end card
            d = snap(ev[1] + 0.8)
            png = os.path.join(out, "text", "end-card.png")
            img = Image.new("RGBA", (W, H), (0, 0, 0, 255)); img.save(png)
            text_png(["CAMPING"], 150, (255, 255, 255, 255), H // 2 - 70, png + ".a.png", stroke=0)
            text_png(["the full film is", "on our channel"], 62, RED, H // 2 + 120, png + ".b.png", stroke=0)
            base = Image.open(png); base.alpha_composite(Image.open(png + ".a.png")); base.alpha_composite(Image.open(png + ".b.png"))
            base.convert("RGB").save(png); os.remove(png + ".a.png"); os.remove(png + ".b.png")
            vp = os.path.join(out, "video", f"{n:02d}-end-card.mp4")
            run(["ffmpeg", "-y", "-loop", "1", "-framerate", str(FPS), "-t", f"{d:.4f}", "-i", png,
                 "-c:v", "libx264", "-crf", "14", "-pix_fmt", "yuv420p", "-r", str(FPS), vp])
            V.append([vp, t, d, 0])
            if HIT_ON["card"]: A.append([hit_wav, t, 1.2, 1])
            t = snap(t + d)
    card_start = V[-1][1]
    title_png = os.path.join(out, "text", "title.png")
    text_png(["CAMPING"], 120, (255, 255, 255, 255), PY - 230, title_png, stroke=0)
    tmov = title_png[:-4] + ".mov"; still_mov(title_png, card_start, tmov); T.insert(0, [tmov, 0.0, card_start, 1])
    plan = {"sequence": seq, "duration": t, "video": V, "overlays": T, "audio": A}
    json.dump(plan, open(os.path.join(out, "plan.json"), "w"), indent=1)
    vids = [[win(p), s, d, tr] for p, s, d, tr in V + T]
    auds = [[win(p), s, d, tr] for p, s, d, tr in A]
    js = PLACE_JS.replace("__V__", json.dumps(vids)).replace("__A__", json.dumps(auds)).replace("__S__", json.dumps(seq))
    open(os.path.join(out, "place.js"), "w").write(js)
    files = sorted({win(p) for p, *_ in V + T + A})
    print(json.dumps({"duration": t, "video": len(V), "overlays": len(T), "audio": len(A), "files": len(files)}))


PLACE_JS = r"""const V=__V__;
const A=__A__;
const S=__S__;
const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!==S) return {error:'wrong sequence',name:seq.name};
const root=await project.getRootItem(); let bin=null; for(const k of await root.getItems()){ if(k.name===S){ let fo=null; try{ fo=ppro.FolderItem.cast(k); }catch(e){} if(fo) bin=fo; } }
if(!bin) return {error:'no bin named '+S};
const byPath={}; for(const it of await bin.getItems()){ try{ byPath[(await ppro.ClipProjectItem.cast(it).getMediaFilePath()).toLowerCase()]=it; }catch(e){} }
const ed=ppro.SequenceEditor.getEditor(seq); const tk=s=>helpers.secondsToTick(Math.round(s*24)/24+0.002); let done=0; const fail=[];
for(const [p,t,d,tr] of V){ try{ const item=byPath[p.toLowerCase()]; if(!item) throw 'not in bin';
  helpers.withTransaction(project,S+' picture',ca=>ca.addAction(ed.createOverwriteItemAction(item,tk(t),tr,0))); done++; }catch(e){ fail.push([p,t,String(e).slice(0,100)]); } }
for(const [p,t,d,tr] of A){ try{ const item=byPath[p.toLowerCase()]; if(!item) throw 'not in bin';
  helpers.withTransaction(project,S+' audio',ca=>ca.addAction(ed.createOverwriteItemAction(item,tk(t),0,tr))); done++; }catch(e){ fail.push([p,t,String(e).slice(0,100)]); } }
const vc=[]; const nv=await seq.getVideoTrackCount(); for(let k=0;k<nv;k++){ vc.push((await (await seq.getVideoTrack(k)).getTrackItems(1,false)).length); }
const ac=[]; const na=await seq.getAudioTrackCount(); for(let k=0;k<na;k++){ ac.push((await (await seq.getAudioTrack(k)).getTrackItems(1,false)).length); }
return {done,fail,vc,ac,mapped:Object.keys(byPath).length};
"""

if __name__ == "__main__":
    main(*sys.argv[1:5])
