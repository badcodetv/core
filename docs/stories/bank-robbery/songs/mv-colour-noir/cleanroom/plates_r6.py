"""Round 6: Claude's take picks (no picks page, Jack asked for the sequence), copied to named plates. A singing shot whose main face is under 30% of frame height is cropped in, at most 1.6x, for lip sync."""
import json, os, pathlib, shutil, sys
import cv2, mediapipe as mp
from mediapipe.tasks import python as P
from mediapipe.tasks.python import vision as V
N = pathlib.Path("/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/bank robbery/noir")
ST = N / "r6/stills"; OUT = pathlib.Path.home() / ".cache/badcode-scenes/mv-colour-noir/plates/r6"; OUT.mkdir(parents=True, exist_ok=True)
SRC = {}
for k, t in dict(d1="00-b", d2="01-a", d3="02-b", d4="03-a").items(): SRC[k] = ST / f"band1/{t}.jpg"
for k, t in dict(d5="00-a", d6="01-b", b1="02-b", b2="03-a", b3="04-b", b4="05-a", b5="06-a", b6="07-a").items(): SRC[k] = ST / f"band2/{t}.jpg"
for k, t in dict(l01="00-a", l02="01-a", f1="02-b").items(): SRC[k] = ST / f"recast/{t}.jpg"
for s in "f2-b e3-a c1-b l03-b l04-a f3-a f4-a e4-b c2-a c3-b c4-a c5-b e1-a e2-a f7-a f8-b n01-b n02-a n03-a n04-a n05-a n06-a n07-b n08-a n09-b n10-a n11-b n12-a n13-b n14-b n15-a n16-a n17-b n18-a safe1-b rods4-a a1-a a2-a a3-b a4-a a5-a a6-a a7-a a8-a a9-a a10-b a11-a a12-b a13-a a14-a".split():
    SRC[s.rsplit("-", 1)[0]] = ST / f"{s}.jpg"
SRC["den3"] = N / "moodboard/r4-den3-mask4/00-a.jpg"; SRC["mask4"] = N / "moodboard/r4-den3-mask4/01-b.jpg"
det = V.FaceLandmarker.create_from_options(V.FaceLandmarkerOptions(base_options=P.BaseOptions(model_asset_path=str(pathlib.Path.home() / ".cache/badcode-lips/face_landmarker.task")), num_faces=5, min_face_detection_confidence=0.3))
rows = {}
for k, src in SRC.items():
    dst = OUT / f"{k}.jpg"
    img = cv2.imread(str(src)); h, w = img.shape[:2]
    singing = not (k in ("safe1", "rods4", "den3", "mask4") or (k[0] == "a" and k[1:].isdigit()))
    if not singing:
        shutil.copyfile(src, dst); rows[k] = dict(src=str(src), plate=str(dst)); continue
    res = det.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))
    best = None
    for f in res.face_landmarks:
        xs = [p.x for p in f]; ys = [p.y for p in f]
        box = (min(xs), min(ys), max(xs), max(ys))
        if best is None or box[3] - box[1] > best[3] - best[1]: best = box
    if best is None:
        shutil.copyfile(src, dst); rows[k] = dict(src=str(src), plate=str(dst), face=None); print(k, "NO FACE"); continue
    fh = best[3] - best[1]
    zoom = min(1.6, max(1.0, 0.30 / fh))
    if zoom > 1.03:
        cw, ch = int(w / zoom), int(h / zoom)
        cx, cy = (best[0] + best[2]) / 2 * w, (best[1] + best[3]) / 2 * h
        x = int(min(max(0, cx - cw / 2), w - cw)); y = int(min(max(0, cy - ch * 0.42), h - ch))
        cv2.imwrite(str(dst), cv2.resize(img[y:y + ch, x:x + cw], (w, h), interpolation=cv2.INTER_LANCZOS4), [cv2.IMWRITE_JPEG_QUALITY, 95])
    else:
        shutil.copyfile(src, dst)
    rows[k] = dict(src=str(src), plate=str(dst), face=round(fh, 3), zoom=round(zoom, 2))
    print(k, "face", round(fh, 3), "zoom", round(zoom, 2))
json.dump(rows, open(pathlib.Path(__file__).parent / "plates-r6.json", "w"), indent=0)

# Faces the detector missed: centres and zoom read by eye off the contact sheet.
MANUAL = dict(l01=(.50,.17,1.6), f1=(.55,.17,1.6), n05=(.48,.31,1.5), n07=(.23,.35,1.6), n13=(.50,.25,1.6), n17=(.50,.70,1.6), n18=(.34,.22,1.6), n16=(.66,.25,1.4), n03=(.41,.22,1.5), n10=(.50,.30,1.5), e4=(.69,.32,1.4), l03=(.52,.25,1.4))
for k, (fx, fy, zoom) in MANUAL.items():
    img = cv2.imread(str(SRC[k])); h, w = img.shape[:2]
    cw, ch = int(w / zoom), int(h / zoom)
    x = int(min(max(0, fx * w - cw / 2), w - cw)); y = int(min(max(0, fy * h - ch * 0.42), h - ch))
    cv2.imwrite(str(OUT / f"{k}.jpg"), cv2.resize(img[y:y + ch, x:x + cw], (w, h), interpolation=cv2.INTER_LANCZOS4), [cv2.IMWRITE_JPEG_QUALITY, 95])
    rows[k].update(zoom=zoom, by_eye=True)
json.dump(rows, open(pathlib.Path(__file__).parent / "plates-r6.json", "w"), indent=0)
