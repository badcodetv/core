"""Build the 1D hologram page from the 1K lookdev page: 1D voice timing + Kai's r19 animation notes (6 Nov)."""
import json, pathlib, re
H = pathlib.Path(__file__).parent
src = (H.parent / '2026-11-05-gpom-meeting/lookdev/index.html').read_text()
L = {l['id']: l for l in json.load(open(H.parent / '2026-11-05-gpom-meeting/voice-1d/lines-1d.json'))}
w = lambda cid, word: next(x[1] for x in L[cid]['words'] if x[0].lower().startswith(word))
# ---- the timing (seconds, hologram clock) ----
st, sg = {}, {}
sg['lead'] = .3; st['d01'] = .35
sg['bead1'] = st['d01'] + L['d01']['dur'] + .05 - .3          # toast pops at .3 (the first thing seen)
sg['bead2'] = .5; sg['bead3'] = .6                            # sorry, married: run past unspoken
t_bead3 = .3 + sg['bead1'] + sg['bead2']
st['d02'] = t_bead3 + .3                                       # "Loads of others" as the cloud blooms on married
sg['open'] = 2.5
S_maybes = t_bead3 + sg['bead3'] + sg['open']
st['d03'] = st['d02'] + L['d02']['dur'] + .3
t_looks = st['d03'] + w('d03', 'yet')
sg['pick'] = 1.8; S_pick = t_looks - .2                        # tPick0 = S.pick + (D.pick - 1.6) = the word "looks"
sg['maybes'] = S_pick - S_maybes
sg['settle'] = .8
S_toRiver = S_pick + sg['pick'] + sg['settle']
st['d04'] = max(S_toRiver + .1, st['d03'] + L['d03']['dur'] + .35)
sg['toRiver'] = 4.5
S_river = S_toRiver + sg['toRiver']
st['d05'] = max(S_river + .1, st['d04'] + L['d04']['dur'] + .35)
st['d06'] = st['d05'] + L['d05']['dur'] + .6                   # "But then you lot went away" as the camera leaves the river
sg['river'] = st['d06'] + w('d06', 'away') + .5 - S_river      # arrive at the cut-off side view on "away"
S_fly = S_river + sg['river']
st['d07'] = st['d06'] + L['d06']['dur'] + .5
S_arc = st['d07'] + w('d07', 'machine') - .3                   # the time machine draws on "time machine"
sg['flyDown'] = S_arc - S_fly
sg['arcDraw'] = 2.5
end = st['d07'] + L['d07']['dur'] + .8
sg['arcHold'] = end - S_arc - sg['arcDraw']
sg['off'] = 1.2
segs = {k: round(sg[k], 3) for k in ['lead','bead1','bead2','bead3','open','maybes','pick','settle','toRiver','river','flyDown','arcDraw','arcHold','off']}
EXC = [[round(st['d02'] + w('d02', 'cartoon') - .4, 2), round(st['d02'] + w('d02', 'strange') - .3, 2)],
       [round(st['d02'] + w('d02', 'strange') - .2, 2), round(st['d03'] - .1, 2)],
       [round(st['d03'] + w('d03', 'alive') - .5, 2), round(t_looks - 2.4, 2)]]
clips = [{'id': k, 'beat': L[k]['beat'], 'text': L[k]['text'], 'dur': L[k]['dur'], 'file': f'voice/{k}.wav'} for k in st]
edit = {'segs': segs, 'clips': {k: {'start': round(v, 3), 'text': L[k]['text'], 'needsVoice': False} for k, v in st.items()}, 'exc': EXC, 'draft': '1D'}
TD = sum(segs.values())
json.dump(edit, open(H / 'edit-1d.json', 'w'), indent=1, ensure_ascii=False)
print(json.dumps(segs)); print('clips', {k: round(v, 2) for k, v in st.items()}); print('yet', round(t_looks, 2), 'EXC', EXC, 'TD', round(TD, 2))

# ---- the page ----
def sub(old, new, s, n=1):
    c = s.count(old); assert c == n, (c, old[:80]); return s.replace(old, new)
p = src
p = sub("<title>Maddie's Hologram Looks</title>", "<title>Maddie's Hologram 1D</title>", p)
p = re.sub(r'const CLIPS0=\[.*?\];[^\n]*', 'const CLIPS0=' + json.dumps(clips, ensure_ascii=False) + ';   // draft 1D, voiced 6 Nov (Gemini TTS, Aoede)', p, count=1)
p = sub("const MIN={lead:.8,bead1:1.2,bead2:1.2,bead3:1.4,", "const MIN={lead:.2,bead1:1.2,bead2:.4,bead3:.5,", p)
p = sub("const SEG_OF={commits:'bead3'};", "const SEG_OF={};\nconst EDIT_1D=" + json.dumps(edit, ensure_ascii=False) + ";   // the 1D timing (make.py)", p)
p = sub("let ED=defaultEdit(); try{const l=JSON.parse(localStorage.getItem('gpom-holo-edit-1k2')||'null'); if(l) mergeEdit(l)}catch(e){}",
        "let ED=defaultEdit(); try{const l=JSON.parse(localStorage.getItem('gpom-holo-edit-1d')||'null'); if(l) mergeEdit(l)}catch(e){}", p)
p = sub("const SUPERSEDED={", "const SUPERSEDED0={", p)
p = sub("retime();\n\n/* ---------- renderer", "mergeEdit(EDIT_1D); try{const l=JSON.parse(localStorage.getItem('gpom-holo-edit-1d')||'null'); if(l) mergeEdit(l)}catch(e){}\nconst EXC=EDIT_1D.exc;   // Kai at1944: in and out of the cloud, three quick visits\nretime();\n\n/* ---------- renderer", p)
p = p.replace("SUPERSEDED[c.id]", "(typeof SUPERSEDED0!=='undefined'?undefined:undefined)")
p = sub("localStorage.setItem('gpom-holo-edit-1k2'", "localStorage.setItem('gpom-holo-edit-1d'", p)
p = sub("dbDoc=db.doc('edits/current')", "dbDoc=db.doc('edits/1d')", p)
p = sub("draft:'1K',updated", "draft:'1D',updated", p)
p = sub("'Hologram edit, draft 1K: '", "'Hologram edit, draft 1D: '", p)
p = sub("ED=defaultEdit(); window.hologram.ED=ED;", "ED=defaultEdit(); mergeEdit(EDIT_1D); window.hologram.ED=ED;", p)
# the river as a circle (Kai at2190, 1-1A-L8): everyone in a round bundle, your string on its edge
p = sub("return out.set(x,1.6*Math.sin(x*.045)+v*R*.3*e,3.2*Math.sin(x*.03+1)+u*R*e)}", "return out.set(x,1.6*Math.sin(x*.045)+v*R*.62*e,3.2*Math.sin(x*.03+1)+u*R*.62*e)}", p)
# the decision cloud as a round ball (Kai at2692)
p = sub("for(let i=0;i<n;i++){const x=.25+Math.pow(fr(),.7)*3.4, a=fr()*Math.PI*2, rad=(.15+Math.sqrt(fr())*2.6)*(.35+x/3.6);\n      off.push(new THREE.Vector3(x,Math.sin(a)*rad*.8,Math.cos(a)*rad)); par.push(fr()<.1?-1:-2)}",
        "for(let i=0;i<n;i++){const th=Math.acos(2*fr()-1), ph=fr()*Math.PI*2, rad=1.75*Math.cbrt(.04+fr()*.96);\n      off.push(new THREE.Vector3(1.95+rad*Math.cos(th),rad*Math.sin(th)*Math.sin(ph),rad*Math.sin(th)*Math.cos(ph))); par.push(fr()<.1?-1:-2)}", p)
# three places in the cloud to visit, and the flash
p = sub("  g.add(fan,lines,chosen,chosenCore); Object.assign(W,{fan,fanLines:lines,fanOff:off,fanPar:par,CH,chosen,chosenCore});",
        "  const near=v=>{let b=1e9,k=0; off.forEach((o,i)=>{const d=o.distanceToSquared(v); if(d<b){b=d;k=i}}); return k};\n"
        "  const EXI=[near(new THREE.Vector3(1.2,1.2,1.0)),near(new THREE.Vector3(2.9,-1.1,-.6)),near(new THREE.Vector3(1.6,.2,-1.5))];\n"
        "  const flash=new THREE.Sprite(new THREE.SpriteMaterial({map:dot(),color:0xffffff,transparent:true,opacity:0,depthWrite:false,depthTest:false,blending:THREE.AdditiveBlending})); flash.visible=false;\n"
        "  g.add(fan,lines,chosen,chosenCore,flash); Object.assign(W,{fan,fanLines:lines,fanOff:off,fanPar:par,CH,chosen,chosenCore,EXI,flash}); fan.frustumCulled=lines.frustumCulled=flash.frustumCulled=false;", p)
# the probability matrix a little higher (Kai at2692)
p = sub("dpos.push(riverPt(Math.cos(an)*rad,Math.sin(an)*rad,x,new THREE.Vector3()));", "dpos.push(riverPt(Math.cos(an)*rad,Math.sin(an)*rad,x,new THREE.Vector3()).add(new THREE.Vector3(0,2.2,0)));", p)
p = sub("W.draftAnchor=topPt(XTIP+1.5).add(new THREE.Vector3(0,1.2,0));", "W.draftAnchor=topPt(XTIP+1.5).add(new THREE.Vector3(0,3.4,0));", p)
# the in-and-out visits inside the cloud
p = sub("  out.pos.copy(out.tgt).addScaledVector(OFF,zoom); return out}",
        "  out.pos.copy(out.tgt).addScaledVector(OFF,zoom);\n"
        "  if(t>TA&&W.EXI) for(let j=0;j<EXC.length;j++){const [a,b]=EXC[j]; if(t<=a||t>=b) continue; const m=(a+b)/2, wv=t<m?ease(clamp((t-a)/((m-a)*.75))):ease(clamp((b-t)/((b-m)*.75)));\n"
        "    const pp=W.basePos[W.iH+NA].clone().addScaledVector(W.fanOff[W.EXI[j]],P.fanSpread*ss(S.open,S.open+D.open,t)); out.tgt.lerp(pp,wv); out.pos.lerp(pp.addScaledVector(OFF,1.6),wv)}\n"
        "  return out}", p)
# the river: start further back, jump to the front, decisions faster, every lane at the cut-off as the camera leaves (Kai at2407, at2511)
p = sub("const w0=S.toRiver+1, w1=S.flyDown-2,", "const w0=S.toRiver+1, w1=riverOut(),", p)
p = sub("const cr=rng(1000+s), lag=2.5+cr()*12,", "const cr=rng(1000+s), lag=4+cr()*16,", p)
p = sub("function riverCommits(t){", "function riverOut(){const r0=S.river, r1=S.flyDown; return Math.max(r0+5,r1-4.5)}\nfunction riverCommits(t){", p)
p = sub("riverPt(.06,-.08,XGREY-15+6*k,sB.pos); riverPt(0,.06,XGREY-3+2.5*k,sB.tgt);",
        "const jmp=ss(r0+.45*(outAt-r0),r0+.45*(outAt-r0)+1.1,t); riverPt(.06,-.08,XGREY-26+3*k+14*jmp,sB.pos); riverPt(0,.06,XGREY-12+2*k+8*jmp,sB.tgt);", p)
# leave the river in ONE move to the side view at the cut-off, then hold there until the time machine (Kai at2511, at2692)
p = sub("else {const e=ease(clamp((t-TC)/Math.min(TFLY,6))), a=1-e;",
        "else {const e=ease(clamp((t-(S.arcDraw-2.2))/4.2)), a=1-e;", p)
# the ping of light on "looks" (Kai at2070, at1944)
p = sub("  const cOn=show&&t<tPick0+Math.min(1.6,D.pick);",
        "  {const fl=t-tPick0, on=fl>-.02&&fl<.45; W.flash.visible=on; if(on){W.flash.position.copy(pNext).addScaledVector(W.fanOff[W.CH],spread*P.fanSpread); const k=ease(clamp(fl/.14)); W.flash.scale.setScalar(lerp(.2,3.4,k)); W.flash.material.opacity=1-ss(.04,.42,fl)}}\n"
        "  const cOn=show&&t<tPick0+Math.min(1.6,D.pick);", p)
# the end pose at the cut-off: hold the empty string AND the probability matrix in frame (Kai at2692)
p = sub("const cc=riverPt(0,0,XGREY-1,new THREE.Vector3()); W.CUT={pos:cc.clone().add(new THREE.Vector3(-10,R*.8+3,R*1.5)),tgt:cc};",
        "const cc=riverPt(0,0,XGREY+5,new THREE.Vector3()); W.CUT={pos:cc.clone().add(new THREE.Vector3(-12,R*.9+4,R*1.9)),tgt:cc};", p)
# a cold open: the telly comes on fast, straight onto the first bead (Kai at971)
p = sub("screen.uniforms.power.value=Math.min(ss(0,.7,t),1-ss(S.off,S.off+.7,t));", "screen.uniforms.power.value=Math.min(ss(0,.35,t),1-ss(S.off,S.off+.7,t));", p)
(H / 'index.html').write_text(p)
print('page', len(p))
