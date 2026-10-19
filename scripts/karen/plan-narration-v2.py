#!/usr/bin/env python3
"""Karen v2 narration (superseded numbers: the final plan is narration-v2-plan.json, built from final/ = tight edges + atempo 1.12, lines may start 1 s before the old anchor): where each new line goes on `Karen v2 narration` (A2).
Anchor = where the old line started on the original cut (whisper word times of A3), +16 s after 98.04
(the Susan insert). A line is pushed later only if the one before has not finished (0.3 s gap). Never trimmed."""
import json,subprocess
D='/mnt/c/Users/jackt/OneDrive/Desktop/Youtube Vids/animation/Karen/narration-v2/tight/'
plan=[('n01-b',3.25),('n02-b',12.25),('n03-b',18.17),('n04-a',24.13),('n05-b',37.21),('n06-a',44.43),
('n38-a',49.79),('n39-a',53.81),('n40-a',58.88),('n41-b',63.58),('n07-a',71.78),('n08-a',75.79),('n09-a',83.41),
('n10-a',85.51),('n11-a',94.37),('n12-a',96.01),('n13lie-b',None),('n14-a',100.21),('n15-a',114.93),('n16-b',116.55),
('n17-a',121.53),('n18-a',129.58),('n19-a',138.48),('n20-a',144.50),('n21-b',153.02),('n22-b',161.96),('n23-a',179.54),
('n24-a',190.82),('n25-a',194.52),('n26-a',196.88),('n27-a',204.55),('n28-b',207.39),('n29-a',213.77),('n30-b',220.17),
('n31-a',232.81),('n32-a',239.53),('n33-b',243.40),('n34-a',252.99),('n35-b',260.15),('n36-a',264.12),('n37-a',267.60),
('p01-president-a',None),('t01-tarquin-a',None)]
fixed={'n13lie-b':98.30,'p01-president-a':290.46,'t01-tarquin-a':299.21}
dur=lambda n:float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+n+'.wav']))
out=[];prev=0
for n,a in plan:
    want=fixed.get(n, a+16 if a is not None and a>=98.04 else a)
    t=max(want,prev+0.35); t=round(t*24)/24; d=dur(n)
    out.append({'name':n+'.wav','t':t,'want':round(want,2),'late':round(t-want,2),'end':round(t+d,2)}); prev=t+d
json.dump(out,open('scripts/karen/narration-v2-plan.json','w'),indent=0)
for o in out: print(f"{o['name']:22} {o['t']:7.2f} -> {o['end']:7.2f}  late {o['late']}")
