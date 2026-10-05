#!/usr/bin/env python3
"""Print the premiere_eval body that places entries [a:b] of edl-v4.json on `MFS v4` (about ten at a time; see api-notes 2026-10-05).
usage: python3 v4-batch.py 0 10"""
import json,os,sys
H=os.path.dirname(os.path.abspath(__file__)); E=json.load(open(H+'/edl-v4.json'))['entries']; a,b=int(sys.argv[1]),int(sys.argv[2])
print("""const plan=%s;
const project=await helpers.activeProject(); const seq=await helpers.activeSequence(project);
if(seq.name!=='MFS v4') return {error:'wrong sequence',name:seq.name};
const ed=ppro.SequenceEditor.getEditor(seq); const tk=s=>helpers.secondsToTick(Math.round(s*24)/24+0.002);
let done=0; const fail=[];
for(const [name,t,i,d,v,a] of plan){ try{
  const item=await helpers.resolveProjectItem(project,name); const clip=ppro.ClipProjectItem.cast(item);
  helpers.withTransaction(project,'v4 in/out',ca=>ca.addAction(clip.createSetInOutPointsAction(tk(i),tk(i+d))));
  helpers.withTransaction(project,'v4 place '+name,ca=>ca.addAction(ed.createOverwriteItemAction(item,tk(t),v,a)));
  helpers.withTransaction(project,'v4 clear',ca=>ca.addAction(clip.createClearInOutPointsAction()));
  done++; }catch(e){ fail.push([name,t,String(e&&e.message||e).slice(0,120)]); } }
const saved=await project.save();
return {done,fail,saved,range:[%d,%d]};""" % (json.dumps(E[a:b]),a,min(b,len(E))))
