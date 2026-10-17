#!/usr/bin/env python3
"""The second half's first assembly: story order, first-pass durations, picture only.

Durations are the animation options' "seconds in the cut" (midpoint), rounded to whole frames at
24 fps. They are a starting length for the picture before the audio exists; once voices and score
are made, the cut slides to them. Takes: the Bot-cast 9-c and 20-c; 15-r2 from 1.0 s (its first
second shrinks the bot); both speakers of the row.

    python3 scripts/gpom/second-half-video/edl.py            # JSON: [name, t, in, dur, frame, note]
    python3 scripts/gpom/second-half-video/edl.py eval A B   # premiere_eval body placing entries [A:B]
"""
import json
import sys

FPS = 24
SEQ = 'gpom-second-half'
# (frame, file, in-point, seconds, what it is)
CUT = [
    (1, 'sh-01-P1-roundabout.mp4', 0, 4, 'Roundabout: kill bots everywhere'),
    (2, 'sh-02-P1-patrol-blockbuster.mp4', 0, 4.5, 'Patrol rolls over the lens'),
    (3, 'sh-03-P1-pov-cctv-hud-patrol.mp4', 0, 3, 'Their eyes: CCTV patrol'),
    (4, 'sh-04-post.mp4', 0, 3, 'Ping: organic signal'),
    (5, 'sh-05-B1-lived-tunnel-threads.mp4', 0, 3.5, 'The bunker'),
    (6, 'sh-06-B5-the-lavatory.mp4', 0, 3.5, 'The lavatory'),
    (7, 'sh-07-1-SB07a.mp4', 0, 4, 'The row: her'),
    (7, 'sh-07-2-SB07c.mp4', 0, 3, 'The row: him'),
    (8, 'sh-08-K5-pov-red-race-hud-kill.mp4', 0, 3, 'KILL MODE ENGAGED'),
    (9, 'sh-09-c-SB09a.mp4', 0, 3, 'The bot in their wake'),
    (10, 'sh-10-K9-downs-aerial.mp4', 0, 4, 'Across the downs'),
    (11, 'sh-11-post.mp4', 0, 9, 'The bot calls upstairs'),
    (12, 'sh-12-SB12a.mp4', 0, 4.5, 'Self-destruct at the gate'),
    (13, 'sh-13-post.mp4', 0, 3, 'The row carries on'),
    (14, 'sh-14-SBDOORa.mp4', 0, 6, 'The doors open'),
    (15, 'sh-15-r2-SBHELLOa.mp4', 1.0, 4, 'Hello'),
    (16, 'sh-16-post.mp4', 0, 10, 'The apology'),
    (17, 'sh-17-M3-old-lady-blockbuster.mp4', 0, 4, 'The old lady'),
    (18, 'sh-18a-post.mp4', 0, 2.5, 'Revolt'),
    (18, 'sh-18b-post.mp4', 0, 6, 'Trust: the CCTV of the self-destruct'),
    (19, 'sh-19-SBEMERb.mp4', 0, 3.5, 'Out into daylight'),
    (20, 'sh-20-c-SB20a.mp4', 0, 4, 'The hundred walk in'),
    (21, 'sh-21-post.mp4', 0, 2.5, 'Bunny suits'),
    (22, 'sh-22-L2-white-hall.mp4', 0, 4, 'The white hall'),
    (23, 'sh-23-post.mp4', 0, 5, 'The wafer'),
    (24, 'sh-24-post.mp4', 0, 4, 'A hundred chairs like a wafer'),
    (25, 'sh-25-SB23a.mp4', 0, 4, 'The chairs from the floor'),
    (26, 'sh-26-L17-mud-on-white.mp4', 0, 3, 'Visible cost'),
    (27, 'sh-27-post.mp4', 0, 6, 'After: the bot alone'),
    (28, 'sh-28-Y2-bus.mp4', 0, 5, 'On the phone, on the bus'),
    (29, 'sh-29-SB27a.mp4', 0, 6, 'The bus drives away'),
]


def frames(s):
    return round(s * FPS) / FPS


def entries():
    t, out = 0.0, []
    for n, name, i, d, note in CUT:
        out.append([name, frames(t), frames(i), frames(d), n, note])
        t = frames(t + d)
    return out


def eval_body(a, b):
    plan = [[e[0], e[1], e[2], e[3], 0, 0] for e in entries()[a:b]]
    return """const plan=%s;
const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!=='%s') return {error:'wrong sequence',name:seq.name};
const ed=ppro.SequenceEditor.getEditor(seq); const tk=s=>helpers.secondsToTick(Math.round(s*24)/24+0.002);
let done=0; const fail=[];
for(const [name,t,i,d,v,a] of plan){ try{
  const item=await helpers.resolveProjectItem(project,name); const clip=ppro.ClipProjectItem.cast(item);
  helpers.withTransaction(project,'2nd half in/out',ca=>ca.addAction(clip.createSetInOutPointsAction(tk(i),tk(i+d))));
  helpers.withTransaction(project,'2nd half place '+name,ca=>ca.addAction(ed.createOverwriteItemAction(item,tk(t),v,a)));
  helpers.withTransaction(project,'2nd half clear',ca=>ca.addAction(clip.createClearInOutPointsAction()));
  done++; }catch(e){ fail.push([name,t,String(e&&e.message||e).slice(0,120)]); } }
const saved=await project.save();
return {done,fail,saved,range:[%d,%d]};""" % (json.dumps(plan, separators=(',', ':')), SEQ, a, min(b, len(CUT)))


if __name__ == '__main__':
    if sys.argv[1:2] == ['eval']:
        print(eval_body(int(sys.argv[2]), int(sys.argv[3])))
    else:
        e = entries()
        json.dump(e, sys.stdout, indent=0)
        print(f'\n// {len(e)} shots, {e[-1][1] + e[-1][3]:.2f}s', file=sys.stderr)
