"""Round 5: my picks of the lip-sync stills, as start frames in the WSL filesystem; a small face gets a crop (cx, cy, zoom as fractions of the frame) so the mouth is big enough for Omni."""
import pathlib
from PIL import Image
SRC = pathlib.Path("/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/bank robbery/noir/lipsync/stills")
OUT = pathlib.Path.home() / ".cache/badcode-scenes/mv-colour-noir/plates/r5"
OUT.mkdir(parents=True, exist_ok=True)
PICKS = {
 "l01": ("p01/00-a", (0.60, 0.33, 2.0)), "l02": ("p01/01-a", None),
 "f1": ("p02/00-b", (0.32, 0.40, 1.4)), "f2": ("p02/01-a", (0.64, 0.45, 1.5)), "e3": ("p02/02-a", (0.72, 0.42, 1.25)), "c1": ("p02/03-a", None),
 "l03": ("p03/00-b", (0.50, 0.42, 1.7)), "l04": ("p03/01-a", (0.60, 0.50, 1.3)), "f3": ("p03/02-a", None), "f4": ("p03/03-a", (0.68, 0.42, 1.4)), "e4": ("p03/04-b", (0.42, 0.34, 1.6)),
 "l05": ("p05/00-b", None), "l06": ("p05/01-a", None), "f5": ("p05/02-a", (0.42, 0.50, 1.2)), "f6": ("p05/03-b", (0.72, 0.52, 1.5)),
 "c3": ("p06/00-b", None), "c4": ("p06/01-a", (0.42, 0.50, 1.5)), "e1": ("p06/02-b", (0.68, 0.50, 1.25)), "e2": ("p06/03-b", (0.62, 0.48, 1.3)),
 "f7": ("p09/f7-a", (0.28, 0.45, 1.4)), "f8": ("p08/00-a", (0.70, 0.55, 1.3)), "c5": ("p08/01-a", (0.48, 0.50, 1.35)), "c2": ("p08/02-a", (0.43, 0.42, 1.6)),
}
for k, (src, crop) in PICKS.items():
    im = Image.open(SRC / (src + ".jpg")).convert("RGB")
    if crop:
        cx, cy, z = crop
        w, h = im.width / z, im.height / z
        x = min(max(cx * im.width - w / 2, 0), im.width - w)
        y = min(max(cy * im.height - h / 2, 0), im.height - h)
        im = im.crop((int(x), int(y), int(x + w), int(y + h))).resize((1376, 768), Image.LANCZOS)
    im.save(OUT / f"{k}.jpg", quality=95)
print(len(PICKS), OUT)
OUTRO = pathlib.Path("/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/songs/bank robbery/noir/outro/stills")
for k, src in {"o1": "o1-b", "o2": "o2-a", "o3": "o3-a", "o4": "o4-b", "o5": "o5-b", "o6": "o6e-b", "o7": "o7e-a"}.items():
    Image.open(OUTRO / (src + ".jpg")).convert("RGB").save(OUT / f"{k}.jpg", quality=95)
