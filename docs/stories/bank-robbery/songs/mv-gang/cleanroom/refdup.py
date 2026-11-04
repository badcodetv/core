"""Find round-2 stills that are really the uploaded reference handed back by Flow (or near copies of it).
    python3 refdup.py <moodboard dir> <reference.jpg> [--delete]"""
import pathlib, sys
from PIL import Image, ImageChops, ImageStat

mb, ref = pathlib.Path(sys.argv[1]), sys.argv[2]
small = lambda p: Image.open(p).convert('L').resize((64, 36))
r = small(ref)
for f in sorted(mb.glob('*r[23]-[ab].jpg')):
    d = ImageStat.Stat(ImageChops.difference(small(f), r)).mean[0]
    if d < 12:
        print(f'{f.name}: diff {d:.1f} = the reference')
        if '--delete' in sys.argv:
            f.unlink()
