#!/usr/bin/env python3
"""Paraguay short 1 ("Sir, Quick Question"): build the edit's source layers with ffmpeg (no final render; the cut is
made on the Premiere timeline). Every overlay is a full-frame 720x1280 transparent PNG so it stacks 1:1 on its own
track and Jack can swap any text. Text comes from docs/stories/magic-money-tree/scenes/paraguay-s1/cleanroom/script-final.json.
    python3 scripts/paraguay/s1_assets.py
"""
import os, subprocess, tempfile
P = "/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/money for something/Paraguay/short1"
A = f"{P}/assets"; os.makedirs(A, exist_ok=True)
B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
M = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
W, H = 720, 1280
def ff(*a): subprocess.run(["ffmpeg", "-loglevel", "error", "-y", *a], check=True)
def tf(s):
    f = tempfile.NamedTemporaryFile("w", delete=False, suffix=".txt"); f.write(s); f.close(); return f.name
def text_png(name, lines, y, size=46, font=B, box="black@0.85", fg="white", x="(w-text_w)/2"):
    vf = f"drawtext=fontfile={font}:textfile={tf(lines)}:fontsize={size}:fontcolor={fg}:x={x}:y={y}:line_spacing=10:box=1:boxcolor={box}:boxborderw=18"
    ff("-f", "lavfi", "-i", f"color=c=0x00000000:s={W}x{H},format=rgba", "-vf", vf, "-frames:v", "1", f"{A}/{name}.png")

# 1. real opener (6 s cut already made), and the scrum clip with the suit's face pixelated (fixed box: the head stays
#    inside x 210-370, y 370-520 for the whole clip; checked on a 2 fps grid 2026-11-09)
ff("-i", f"{P}/video/scrum-carry.mp4", "-filter_complex",
   "[0]split[a][b];[b]crop=170:160:205:365,scale=12:11,scale=170:160:flags=neighbor[p];[a][p]overlay=205:365",
   "-c:v", "libx264", "-crf", "12", "-c:a", "copy", f"{A}/scrum-carry-pixelated.mp4")
# 2. streamer box: the desk clip shrunk into a framed box, top right, on transparency (ProRes 4444 keeps alpha)
ff("-i", f"{P}/video/box-desk.mp4", "-filter_complex",
   f"[0]scale=216:384,pad=224:392:4:4:color=0x2bb5c7[s];color=c=0x00000000:s={W}x{H}:d=8.04,format=rgba[bg];[bg][s]overlay=480:24:shortest=1,format=yuva444p10le",
   "-c:v", "prores_ks", "-profile:v", "4444", "-an", f"{A}/streamer-box.mov")
# 3. logo bug, top left (the official reversed mark)
subprocess.run(["node", "-e", f"require('sharp')('docs/brand/logo/badcode-mark-reversed.svg',{{density:300}}).resize(110).png().toFile('{A}/logo-110.png')"], check=True)
ff("-f", "lavfi", "-i", f"color=c=0x00000000:s={W}x{H},format=rgba", "-i", f"{A}/logo-110.png", "-filter_complex",
   "[0][1]overlay=24:28", "-frames:v", "1", f"{A}/ov-logo.png")
# 4. text layers
text_png("ov-summary", "THEIR BANK WENT BUST.\nTHEN A POLITICIAN\nSHOWED UP.", 470, size=42)
text_png("ov-credit", "Video: @Raulbogarin on X", 1150, size=22, box="black@0.6", x="24")
text_png("ov-pixelated", "FACE PIXELATED FOR LEGAL REASONS", 1040, size=28, box="0xD62828@0.95")
text_png("ov-4days", "4 DAYS: BANK SEIZED -> PRESIDENT REMOVED", 1040, size=27, box="0x111111@0.92")
text_png("ov-pickone", "BANK OWNER.\nBANK INSPECTOR.\nPICK ONE.", 150, size=56)
# 5. the error box (post graphic): drawn on a solid panel, then laid on the transparent canvas
#    (drawbox on a transparent canvas leaves alpha at 0, so the box came out invisible)
ff("-f", "lavfi", "-i", f"color=c=0x00000000:s={W}x{H},format=rgba", "-f", "lavfi", "-i", "color=c=0xC0C0C0:s=600x230,format=rgba",
   "-filter_complex",
   "[1]drawbox=x=0:y=0:w=600:h=44:color=0x000080@1.0:t=fill,drawbox=x=0:y=0:w=600:h=230:color=0x404040@1.0:t=3,"
   f"drawtext=fontfile={M}:text='Error':fontsize=24:fontcolor=white:x=16:y=10,"
   f"drawtext=fontfile={M}:textfile={tf('PENSIONER_PLAN.EXE\nIS NOT RESPONDING')}:fontsize=28:fontcolor=black:x=30:y=70:line_spacing=8,"
   "drawbox=x=90:y=160:w=170:h=46:color=0xE8E8E8@1.0:t=fill,drawbox=x=340:y=160:w=170:h=46:color=0xE8E8E8@1.0:t=fill,"
   f"drawtext=fontfile={M}:text='WAIT':fontsize=24:fontcolor=black:x=145:y=170,drawtext=fontfile={M}:text='WAIT':fontsize=24:fontcolor=black:x=395:y=170[p];"
   "[0][p]overlay=60:500", "-frames:v", "1", f"{A}/ov-exe.png")
# 6. meme stills, full frame with their text baked in
S = f"{P}/stills"
ff("-i", f"{S}/meme-species-a.jpg", "-vf", f"scale={W}:{H},"
   f"drawtext=fontfile={B}:textfile={tf('OPPORTUNISTUS SUITUS')}:fontsize=40:fontcolor=0x222222:x=(w-text_w)/2:y=h*0.80,"
   f"drawtext=fontfile={B}:textfile={tf('STATUS: NOT ENDANGERED')}:fontsize=30:fontcolor=0xB00000:x=(w-text_w)/2:y=h*0.86",
   f"{A}/meme-species.png")
ff("-i", f"{S}/meme-lilo-a.jpg", "-vf", f"scale={W}:{H},"
   f"drawtext=fontfile={B}:textfile={tf('OUT OF OFFICE')}:fontsize=78:fontcolor=white:borderw=6:bordercolor=black:x=(w-text_w)/2:y=120",
   f"{A}/meme-lilo.png")
print("ok", sorted(os.listdir(A)))
