"""1F5 (Kai, 11 Nov): copied from design/2026-11-10-gpom-hologram-1f4 with nothing changed but the voice record: s01 re-voiced to its new words
("Let's start with science, which, as machines, is close to our heart"), lines-1f5.json. Every stack time is measured from s01's words, so the cards re-land by themselves.
Build the 1F4 hologram page (Kai's round 24 notes, 10 Nov): copied from design/2026-11-10-gpom-hologram-1f3 (every 1F3 change kept), re-timed to the
round 25 voice (f02 tail fixed, f03/f05/f06/f07a re-voiced). f07a's new words have no "go back": the arc now draws on "It just needs".
Build the 1F3 hologram page (Kai's round 23 timeline notes, 10 Nov), copied from design/2026-11-10-gpom-hologram-1f2/make.py (every 1F2 fix kept).
1F3: new words f01/f03/f05/f07a, f02 re-voiced, a new line f04b; brighter stack outlines (at1044); a better INDIVIDUAL figure (at1097);
no blur artefacts inside the cloud (at2746); two pictured cat nodes visited alive-then-dead from "Did you know" (at2746, at2912);
the one timeline under f04b (at3125); into the river sooner (at3372); one square-on final view, rising for the time machine (at3500, at3722)."""
import json, pathlib, re
H = pathlib.Path(__file__).parent
src = (H.parent / '2026-11-05-gpom-meeting/lookdev/index.html').read_text()
L = {l['id']: l for l in json.load(open(H.parent / '2026-11-05-gpom-meeting/voice-1f/lines-1f5.json')) if not l['street']}
def w(cid, word, n=0):   # the start of the n-th word (0-based) in a clip that starts with `word`
    return [x[1] for x in L[cid]['words'] if x[0].lower().replace('’', "'").startswith(word)][n]
# ---- the timing (seconds, hologram clock) ----
st, sg = {}, {}
# the materialist stack (1F2). Each layer pops .1 s before its word; the camera lands on it on the word.
st['s01'] = .35
LAYERS = [('SOCIETY', 'societ', 0), ('INDIVIDUAL', 'people', 0), ('BIOLOGY', 'cells', 0), ('CHEMISTRY', 'chemistry', 0), ('PHYSICS', 'atoms', 0), ('MATHEMATICS', 'maths', 0)]
lay = [round(st['s01'] + w('s01', wd, n) - .1, 3) for _, wd, n in LAYERS]
t_quarks = st['s01'] + w('s01', 'quarks') - .1                 # the atom opens into the standard model grid
t_leptons = st['s01'] + w('s01', 'leptons') - .1               # the lepton rows light
t_under = st['s01'] + w('s01', 'under')                        # "And under all that…": the slow drop to the maths
st['s02'] = st['s01'] + L['s01']['dur'] + .45                  # pull back: the whole stack
t_missing = st['s02'] + w('s02', 'something') - .1             # the empty outlined slot lands beside it
st['s03'] = st['s02'] + L['s02']['dur'] + .45
t_consc = st['s03'] + w('s03', 'conscious') - .1               # the slot lights warm
t_quarks3 = st['s03'] + w('s03', 'quarks')                     # "as fundamental as quarks and leptons": the physics card answers
E3 = st['s03'] + L['s03']['dur']                               # (each clip ends .35 s after its last word)
depart = E3 - .3; FLY = 3.0                                    # the light leaves the slot as she finishes and drops into bead 1
TS = depart + FLY
st['f01'] = E3 + .45                                           # f01 starts while the light falls (the old 11.56 s black lead goes)
t_toast = st['f01'] + w('f01', 'toast')
st['f02'] = st['f01'] + L['f01']['dur'] + .3
t_sorry = st['f02'] + w('f02', 'sorry'); t_married = st['f02'] + w('f02', 'married')
st['f03'] = st['f02'] + L['f02']['dur'] + .5                   # qualia: the three beads glow (GLOW below)
st['f04'] = st['f03'] + L['f03']['dur'] + .5
S_open = st['f04'] + w('f04', 'multiverse') - .15              # the cloud blooms on "multiverse malarkey" (a reveal; no visits until "Did you know")
t_yet = st['f04'] + w('f04', 'yet')
S_pick = t_yet - .2                                            # tPick0 = S.pick + (D.pick - 1.6) = the word "yet": flash + collapse
st['f04b'] = st['f04'] + L['f04']['dur'] + .5                  # 1F3 (at3125): "...settle into what really happens" over the one timeline
st['f05'] = st['f04b'] + L['f04b']['dur'] + .5
sg['stack'] = TS
sg['lead'] = (t_toast - .1) - TS                               # bead 1 (Derek's toast) pops on "toast"
sg['bead1'] = t_sorry - t_toast                                # bead 2 (Sandra) on "sorry"
sg['bead2'] = t_married - t_sorry                              # bead 3 (the wedding) on "married"
sg['bead3'] = S_open - (t_married - .1)
sg['open'] = 2.5
sg['pick'] = 1.8
sg['maybes'] = S_pick - (S_open + sg['open'])
S_toRiver = st['f05'] - .25                                    # 1F3: the settle holds the one string under the whole of f04b
sg['settle'] = S_toRiver - (S_pick + sg['pick'])
BACK_D = 2.6                                                   # the pull-back from the cloud to the one string is done ~1 s into f04b
sg['toRiver'] = 3.0                                            # 1F3 (at3372): "It's all of you" = everybody's strings, quicker
S_river = S_toRiver + sg['toRiver']
t_each = st['f05'] + w('f05', 'each')
PIN0 = S_river + .05; PIND = max(2.2, t_each + .9 - PIN0)      # straight on in, no pause: inside among the strands by "Each of you writing"
OUT0 = st['f05'] + L['f05']['dur'] - 1.4                       # leave on "...really important", every strand at the cut-off as we go
S_fly = OUT0 + 2.6                                             # 1F3 (at3500): land square-on at the cut-off, once, and rest there
st['f06'] = S_fly + 1.0                                        # f06 (1C): a second of silence on the dead stop and the empty run before she speaks
sg['river'] = S_fly - S_river
st['f07a'] = st['f06'] + L['f06']['dur'] + .7
t_tm = st['f07a'] + w('f07a', 'time')                          # "a time machine": the camera rises (at3722)
RISE0 = t_tm - .4; RISED = 3.2
S_arc = st['f07a'] + w('f07a', 'just') - .1                    # 1F4: the arc draws on "It just needs consciousness", below the risen camera
sg['flyDown'] = S_arc - S_fly
sg['arcDraw'] = 2.5
sg['arcHold'] = max(2.0, st['f07a'] + L['f07a']['dur'] + .6 - (S_arc + sg['arcDraw']))
sg['off'] = 1.2
SEGK = ['stack','lead','bead1','bead2','bead3','open','maybes','pick','settle','toRiver','river','flyDown','arcDraw','arcHold','off']
segs = {k: round(sg[k], 3) for k in SEGK}
f4 = lambda word, d, n=0: round(st['f04'] + w('f04', word, n) + d, 2)
# 1F3 (at2746, at2912): two visits, from "Did you know": into the live cat, out; into the dead cat, out; clear of the cloud before "yet"
EXC = [[f4('did', -.15), f4('to', .1)], [f4('to', .35), min(f4("it's", 1.1), round(t_yet - 1.0, 2))]]
GLOW = [round(st['f03'] - .2, 2), round(S_open, 2)]
clips = [{'id': k, 'beat': L[k]['beat'], 'text': L[k]['text'], 'dur': L[k]['dur'], 'file': f'voice/{k}.wav'} for k in st]
TD = sum(segs.values())
f07b = round(TD + .5, 2)
STACK = {'labels': [n for n, _, _ in LAYERS], 'lay': lay, 'quarks': round(t_quarks, 3), 'leptons': round(t_leptons, 3), 'under': round(t_under, 3),
         's02': round(st['s02'], 3), 'missing': round(t_missing, 3), 's03': round(st['s03'], 3), 'consc': round(t_consc, 3), 'quarks3': round(t_quarks3, 3),
         'depart': round(depart, 3), 'fly': FLY}
CAM = {'back': BACK_D, 'pin0': round(PIN0, 3), 'pind': round(PIND, 3), 'out0': round(OUT0, 3), 'rise0': round(RISE0, 3), 'rised': RISED}
edit = {'segs': segs, 'clips': {k: {'start': round(v, 3), 'text': L[k]['text'], 'needsVoice': False} for k, v in st.items()}, 'exc': EXC, 'glow': GLOW, 'draft': '1F5', 'stack': STACK, 'cam': CAM,
        'placeholder': {'f06': 'the 1F2 f06 clip; Kai is picking new words'} if L['f06'].get('placeholder') else {},
        'street': {'b01': 'before the hologram, on the street (ends "Please, let me show you what we found."; the hologram cuts in as it finishes)',
                   'b02': 'CUT in 1F2 (Kai, 10 Nov)',
                   'f07b': {'after_hologram_ends': f07b, 'note': 'back on the street; not on the hologram clock or in voice.wav'}},
        'marks': {**{'layer_' + n.lower(): round(t + .1, 2) for (n, _, _), t in zip(LAYERS, lay)}, 'quarks_grid': round(t_quarks + .1, 2), 'slot_appears': round(t_missing + .1, 2),
                  'slot_lights': round(t_consc + .1, 2), 'light_leaves': round(depart, 2), 'light_lands': round(TS, 2),
                  'toast': round(t_toast, 2), 'sorry': round(t_sorry, 2), 'married': round(t_married, 2), 'cloud_blooms': round(S_open, 2),
                  'did_you_know': f4('did', 0), 'cat_alive': round(sum(EXC[0]) / 2, 2), 'cat_dead': round(sum(EXC[1]) / 2, 2), 'yet_flash': round(S_pick + sg['pick'] - 1.6, 2),
                  'one_timeline_f04b': round(st['f04b'], 2), 'to_river': round(S_toRiver, 2), 'inside_river': round(PIN0 + PIND, 2), 'leave_river': round(OUT0, 2),
                  'arrive_square_on': round(S_fly, 2), 'rise': round(RISE0, 2), 'arc_draws': round(S_arc, 2), 'screen_off': round(TD - sg['off'], 2), 'TD': round(TD, 3)}}
json.dump(edit, open(H / 'edit-1f5.json', 'w'), indent=1, ensure_ascii=False)
print(json.dumps(segs)); print('clips', {k: round(v, 2) for k, v in st.items()}); print('marks', edit['marks']); print('EXC', EXC, 'GLOW', GLOW)

# ---- the page ----
def sub(old, new, s, n=1):
    c = s.count(old); assert c == n, (c, old[:80]); return s.replace(old, new)
p = '<meta charset="utf-8">\n' + src   # 1F2: the stack draws non-ASCII (ν, π, …) into textures; served without a charset they came out as mojibake
p = sub("<title>Maddie's Hologram Looks</title>", "<title>Maddie's Hologram 1F5</title>", p)
p = re.sub(r'const CLIPS0=\[.*?\];[^\n]*', 'const CLIPS0=' + json.dumps(clips, ensure_ascii=False) + ';   // draft 1F5: round 25 voice (f03, f05, f06, f07a re-voiced; f02 tail fixed); rest as 1F3 (Gemini TTS, Aoede)', p, count=1)
p = sub("const MIN={lead:.8,bead1:1.2,bead2:1.2,bead3:1.4,", "const MIN={lead:.2,bead1:1.2,bead2:.4,bead3:.5,", p)
p = sub("const SEG_OF={commits:'bead3'};", "const SEG_OF={stackBack:'stack',slot:'stack'};\nconst EDIT_1D=" + json.dumps(edit, ensure_ascii=False) + ";   // the 1F5 timing (make.py)", p)
p = sub("let ED=defaultEdit(); try{const l=JSON.parse(localStorage.getItem('gpom-holo-edit-1k2')||'null'); if(l) mergeEdit(l)}catch(e){}",
        "let ED=defaultEdit(); try{const l=JSON.parse(localStorage.getItem('gpom-holo-edit-1f5')||'null'); if(l) mergeEdit(l)}catch(e){}", p)
p = sub("const SUPERSEDED={", "const SUPERSEDED0={", p)
p = sub("retime();\n\n/* ---------- renderer", "mergeEdit(EDIT_1D); try{const l=JSON.parse(localStorage.getItem('gpom-holo-edit-1f5')||'null'); if(l) mergeEdit(l)}catch(e){}\nconst EXC=EDIT_1D.exc;   // 1F3 (Kai at2746, at2912): from \"Did you know\", into the live cat and out, into the dead cat and out\nretime();\n\n/* ---------- renderer", p)
p = p.replace("SUPERSEDED[c.id]", "(typeof SUPERSEDED0!=='undefined'?undefined:undefined)")
p = sub("localStorage.setItem('gpom-holo-edit-1k2'", "localStorage.setItem('gpom-holo-edit-1f5'", p)
p = sub("dbDoc=db.doc('edits/current')", "dbDoc=db.doc('edits/1f5')", p)
p = sub("draft:'1K',updated", "draft:'1F5',updated", p)
p = sub("'Hologram edit, draft 1K: '", "'Hologram edit, draft 1F5: '", p)
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
p = sub("function riverCommits(t){", "function riverOut(){return EDIT_1D.cam.out0}\nfunction riverCommits(t){", p)
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
        "/* 1F3: W.CUT is set beside W.ARC (square-on) */", p)
# a cold open: the telly comes on fast, straight onto the first bead (Kai at971)
p = sub("screen.uniforms.power.value=Math.min(ss(0,.7,t),1-ss(S.off,S.off+.7,t));", "screen.uniforms.power.value=Math.min(ss(0,.35,t),1-ss(S.off,S.off+.7,t));", p)
# ---- 1F: the three beads glow under f03 (qualia), from just before the line until the cloud blooms ----
p = sub("function reveal(lo,hi,pop){ // your string: show decisions lo..hi, the last one popping in\n  const k=lo+'|'+hi+'|'+pop.toFixed(3)+'|'+P.bead+'|'+P.ember;",
        "let GLOW=1;   // 1F: >1 swells the embers of beads 1-3 (f03, qualia)\nfunction reveal(lo,hi,pop){ // your string: show decisions lo..hi, the last one popping in\n  const k=lo+'|'+hi+'|'+pop.toFixed(3)+'|'+P.bead+'|'+P.ember+'|'+GLOW.toFixed(3);", p)
p = sub("m4.compose(W.basePos[i],q,sv.setScalar(s*P.bead*P.ember)); W.core.setMatrixAt(i,m4)}",
        "m4.compose(W.basePos[i],q,sv.setScalar(s*P.bead*P.ember*(i>=W.iH&&i<W.iH+NA?GLOW:1))); W.core.setMatrixAt(i,m4)}", p)
p = sub("  /* your string */\n  const iH=W.iH;",
        "  {const [g0,g1]=EDIT_1D.glow; GLOW=1+.85*ss(g0,g0+1.2,t)*(1-ss(g1-.6,g1+.4,t))*(.8+.2*Math.sin((t-g0)*2.4))}\n  /* your string */\n  const iH=W.iH;", p)

# ---- 1F: the per-bead media hook (EMPTY this render). Stills/clips of Derek at the toaster, Sandra saying sorry
# and the wedding are being made separately; set BEAD_MEDIA here (or pass record.mjs --media <json>) and rebuild.
# bead 0/1/2 -> {"src": path or URL relative to this page, "type": "image"|"video", "fps": 24, "scale": .85 (disc radius in bead radii),
#   "offset": 0 (s into the clip at the pop), "push": .05 (slow push-in over its time on screen)}. Square or wide media is centre-cropped to the disc.
# The disc draws over the bead's ember (depthTest off), feathered at the rim, and brightens with GLOW under f03.
BEAD_MEDIA = {}
p = sub("/* ---------- tags: plain words above the decision ---------- */",
"""/* ---------- 1F: media inside beads 1-3 (a still or a clip on a disc in the glass; empty unless BEAD_MEDIA is set) ---------- */
const BEAD_MEDIA=Object.assign(""" + json.dumps(BEAD_MEDIA) + """,window.BEAD_MEDIA_OVERRIDE||{});
const MEDIA=[]; let featherTex=null;
function feather(){if(featherTex) return featherTex; const c=document.createElement('canvas'); c.width=c.height=256; const x=c.getContext('2d'), g=x.createRadialGradient(128,128,0,128,128,128); g.addColorStop(0,'#fff'); g.addColorStop(.86,'#fff'); g.addColorStop(1,'#000'); x.fillStyle=g; x.fillRect(0,0,256,256); return featherTex=new THREE.CanvasTexture(c)}
function fitCover(tex,w,h){const a=w/h; tex.userData.base=[a>1?1/a:1,a>1?1:a]; tex.repeat.set(...tex.userData.base); tex.offset.set((1-tex.repeat.x)/2,(1-tex.repeat.y)/2); tex.needsUpdate=true}
function pushIn(tex,z){const b=tex.userData.base; if(!b) return; tex.repeat.set(b[0]/z,b[1]/z); tex.offset.set((1-tex.repeat.x)/2,(1-tex.repeat.y)/2)}
function mediaInit(){for(const [j,m] of Object.entries(BEAD_MEDIA)){if(!m||!m.src) continue; let tex, el=null, ready;
    if(m.type==='video'||/\\.(mp4|webm|mov|m4v)$/i.test(m.src)){el=document.createElement('video'); el.muted=true; el.playsInline=true; el.preload='auto'; el.crossOrigin='anonymous';   // fetched whole into a blob: a server without Range support (python http.server) leaves a video unseekable
      fetch(m.src).then(r=>{if(!r.ok) throw new Error(r.status); return r.blob()}).then(bl=>{el.src=URL.createObjectURL(bl)}).catch(e=>{console.error('bead media failed',m.src,e); el.dispatchEvent(new Event('error'))});
      tex=new THREE.VideoTexture(el); ready=new Promise(r=>{const go=()=>{fitCover(tex,el.videoWidth,el.videoHeight); r()}; el.readyState>=2?go():el.addEventListener('loadeddata',go,{once:true}); el.addEventListener('error',()=>{console.error('bead media failed',m.src); r()},{once:true})})}
    else ready=new Promise(r=>{tex=new THREE.TextureLoader().load(m.src,t=>{fitCover(t,t.image.width,t.image.height); r()},undefined,()=>{console.error('bead media failed',m.src); r()})});
    tex.colorSpace=THREE.SRGBColorSpace; tex.minFilter=THREE.LinearFilter; tex.generateMipmaps=false;
    const mat=new THREE.MeshBasicMaterial({map:tex,alphaMap:feather(),transparent:true,opacity:0,depthWrite:false,depthTest:false,toneMapped:false}), mesh=new THREE.Mesh(new THREE.CircleGeometry(1,64),mat);
    mesh.visible=false; mesh.frustumCulled=false; mesh.renderOrder=10; scene.add(mesh); MEDIA.push({j:+j,m,el,tex,mat,mesh,ready})}}
function mediaApply(t){for(const o of MEDIA){const tb=beadT[o.j], on=t>=tb&&t<TB+.5; o.mesh.visible=on; if(!on) continue;
    o.mesh.position.copy(W.basePos[W.iH+o.j]); o.mesh.quaternion.copy(camera.quaternion);
    o.mesh.scale.setScalar(Math.max(.001,backOut(clamp((t-tb)/.45))*BR*P.bead*(o.m.scale||.85)));
    o.mat.opacity=ss(tb,tb+.3,t)*(1-ss(TB-.5,TB+.5,t)); o.mat.color.setScalar(1+.45*(GLOW-1));
    pushIn(o.tex,1+(o.m.push??.05)*clamp((t-tb)/Math.max(1,TB+.5-tb)));
    if(o.el&&!FILM&&o.el.readyState>=1){const want=Math.min(o.el.duration-.001,Math.max(0,(o.m.offset||0)+t-tb)); if(Math.abs(o.el.currentTime-want)>.15) o.el.currentTime=want}}}
async function mediaSeek(t){   // film mode: step each visible clip to the source frame under t, wait for it, then render
  for(const o of MEDIA){if(!o.el||!o.mesh.visible) continue; await o.ready; const fps=o.m.fps||24;
    let want=Math.min(o.el.duration-.5/fps,Math.max(0,(o.m.offset||0)+t-beadT[o.j])); want=(Math.floor(want*fps+1e-6)+.5)/fps;
    if(Math.abs(o.el.currentTime-want)>1e-4) await new Promise(r=>{o.el.addEventListener('seeked',r,{once:true}); o.el.currentTime=want});
    if(o.el.readyState<2) await new Promise(r=>o.el.addEventListener('canplay',r,{once:true}));
    o.tex.needsUpdate=true}}

/* ---------- tags: plain words above the decision ---------- */""", p)
p = sub("  drawWords(t);\n}", "  mediaApply(t); drawWords(t);\n}", p)
p = sub("build(); liveMaterials(); syncInputs(); renderTL(); renderLines();\nlet FILM=false;",
        "build(); liveMaterials(); syncInputs(); renderTL(); renderLines();\nlet FILM=false; mediaInit();", p)
p = sub("  frameAt(t,type){T=t; orbiting=false; apply(t);", "  get MEDIA(){return MEDIA}, mediaReady(){return Promise.all(MEDIA.map(o=>o.ready)).then(()=>MEDIA.length)},\n  async frameAt(t,type){T=t; orbiting=false; apply(t); if(MEDIA.length) await mediaSeek(t);", p)
# the bead tags ride above a media disc instead of across it (only when a bead has media)
for j in range(3):
    p = sub("{a:()=>W.basePos[W.iH" + ("+%d" % j if j else "") + "],", "{a:()=>mediaLift(W.basePos[W.iH" + ("+%d" % j if j else "") + "].clone()," + str(j) + "),", p)
p = sub("async function mediaSeek(t){", "function mediaLift(v,j){const o=MEDIA.find(o=>o.j===j); if(!o) return v; return v.add(new THREE.Vector3(0,1,0).applyQuaternion(camera.quaternion).multiplyScalar(BR*P.bead*(o.m.scale||.85)*.75))}\nasync function mediaSeek(t){", p)
# ---- 1F2: the materialist stack in front of the string (stack.js, inlined) ----
p = sub("const SEGS=[['lead','Black'],", "const SEGS=[['stack','The stack'],['lead','Black'],", p)
p = sub("const MIN={lead:.2,", "const MIN={stack:1,lead:.2,", p)
p = sub("/* ---------- tags: plain words above the decision ---------- */", (H / 'stack.js').read_text() + "\n/* ---------- tags: plain words above the decision ---------- */", p)
p = sub("scene.add(g); revealKey='';", "scene.add(g); revealKey=''; stackBuild();", p)
p = sub("  if(t<TB) closeShot(t,shot);", "  if(t<S.lead) stackShot(t,shot);\n  else if(t<TB) closeShot(t,shot);", p)
p = sub("  mediaApply(t); drawWords(t);\n}", "  stackApply(t); mediaApply(t); drawWords(t);\n}", p)
p = sub("  tctx.globalAlpha=1; txtTex.needsUpdate=true}", "  tctx.globalAlpha=1; stackWords(t,fs); txtTex.needsUpdate=true}", p)
exec(open(H / 'make_1f3.py').read())   # the 1F3 changes to the page
(H / 'index.html').write_text(p)
print('page', len(p))
