#!/usr/bin/env python3
"""File a flow_generate_batch run into a short's mood board (2026-11-15, shorts #83-85 round 1).

    python3 scripts/shorts/file-batch.py <scene-dir> <prompts.json> <batch-dir>

prompts.json is a clean-room writer's file ({"stills": [{beat, id, look, prompt}]}, in batch order). Each <batch-dir>/NN.jpg (NN from 00, the batch index)
(and its .prov.json recipe card, if any) is moved to <media>/moodboard/<id>.jpg, and a row [beat, id, look, prompt] is
added to the scene's moodboard.json (missing images stay as rows, shown "not generated" on the page)."""
import json, pathlib, shutil, subprocess, sys
scene, prompts, batch = pathlib.Path(sys.argv[1]), json.load(open(sys.argv[2]))['stills'], pathlib.Path(sys.argv[3])
cfg = json.loads((scene / 'scene.json').read_text())
media = pathlib.Path(subprocess.run(['python3', pathlib.Path(__file__).parents[1] / 'drive/localmap.py', 'path', cfg['media']],
                                    capture_output=True, text=True, check=True).stdout.strip())
mb = scene / 'moodboard.json'; rows = json.loads(mb.read_text()) if mb.exists() else []
have = {r[1] for r in rows}
for i, s in enumerate(prompts):
    src = next((p for p in (batch / f'{i:02d}.jpg', batch / f'{i:02d}-a.jpg') if p.exists()), None)
    dst = media / 'moodboard' / f"{s['id']}.jpg"
    if src:
        shutil.move(src, dst)
        card = src.with_name(src.name + '.prov.json')
        if card.exists():
            c = json.loads(card.read_text()); c['file'] = str(dst); dst.with_name(dst.name + '.prov.json').write_text(json.dumps(c, indent=1)); card.unlink()
    if s['id'] not in have:
        rows.append([s['beat'], s['id'], s['look'], s['prompt']])
    print(s['id'], 'ok' if dst.exists() else 'MISSING', src.name if src else '')
mb.write_text(json.dumps(rows, indent=1, ensure_ascii=False) + '\n')
