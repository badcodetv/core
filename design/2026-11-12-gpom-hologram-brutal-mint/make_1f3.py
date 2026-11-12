# The 1F3 page changes (Kai's round 23 timeline notes, 10 Nov). Run by make.py with its namespace (sub, p, json, H) just before
# the page is written, so every 1F2 substitution has already happened and each `sub` below asserts its target exists exactly once.

# ---- at2746: two pictured nodes in the cloud (a cat alive in a box, a cat dead in a box), on the camera side of the ball ----
p = sub("  const EXI=[near(new THREE.Vector3(1.2,1.2,1.0)),near(new THREE.Vector3(2.9,-1.1,-.6)),near(new THREE.Vector3(1.6,.2,-1.5))];",
        "  const EXI=[near(new THREE.Vector3(1.35,.75,1.05)),near(new THREE.Vector3(2.35,-.7,1.15))];   // 1F3: the live cat, the dead cat (front of the ball, apart)", p)

# the visits: closer in (the node fills the frame), and how far in we are is kept for the blur and the cat discs
p = sub("  if(t>TA&&W.EXI) for(let j=0;j<EXC.length;j++){const [a,b]=EXC[j]; if(t<=a||t>=b) continue; const m=(a+b)/2, wv=t<m?ease(clamp((t-a)/((m-a)*.75))):ease(clamp((b-t)/((b-m)*.75)));\n"
        "    const pp=W.basePos[W.iH+NA].clone().addScaledVector(W.fanOff[W.EXI[j]],P.fanSpread*ss(S.open,S.open+D.open,t)); out.tgt.lerp(pp,wv); out.pos.lerp(pp.addScaledVector(OFF,1.6),wv)}",
        "  VISIT=[0,0]; if(t>TA&&W.EXI) for(let j=0;j<EXC.length;j++){const [a,b]=EXC[j]; if(t<=a||t>=b) continue; const m=(a+b)/2, wv=t<m?ease(clamp((t-a)/((m-a)*.75))):ease(clamp((b-t)/((b-m)*.75))); VISIT[j]=wv;\n"
        "    const pp=W.basePos[W.iH+NA].clone().addScaledVector(W.fanOff[W.EXI[j]],P.fanSpread*ss(S.open,S.open+D.open,t)); out.tgt.lerp(pp,wv); out.pos.lerp(pp.addScaledVector(OFF,1.05),wv)}", p)
p = sub("let orbiting=false, showSubs=true;", "let orbiting=false, showSubs=true, VISIT=[0,0];", p)

# at3125: the pull-back from the cloud to the one string is done early in f04b, then it holds there
p = sub("back=ss(tPick0,S.toRiver,t);", "back=ss(tPick0,Math.min(S.toRiver,tPick0+EDIT_1D.cam.back),t);", p)

# at2746 artefacts: (1) the depth-of-field pass blurs the cloud's beads (they write no depth, so it reads them as far away and tears
# their edges at close range): the aperture closes as the camera goes in; (2) a bead closer to the lens than its own width fades out
p = sub("  bokeh.uniforms.aperture.value=lerp(lerp(.028,t<TC?.0003:.0008,trunk),.0025,inside);",
        "  const vis=Math.max(VISIT[0],VISIT[1]), inCloud=t>TA&&t<TB?ss(S.open,S.open+D.open,t)*(1-ss(tPick0,tPick0+1.1,t)):0;\n"
        "  bokeh.uniforms.aperture.value=lerp(lerp(.028,t<TC?.0003:.0008,trunk),.0025,inside)*(1-.6*inCloud)*(1-.98*vis);", p)
p = sub("const s=i===W.CH?0:P.fanSize*P.bead*tw*1.6; m4.compose(tmp,q,sv.setScalar(s));",
        "const near=ss(.2,.7,tmp.distanceTo(camera.position)), s=(i===W.CH||(CATS.length&&W.EXI.includes(i)))?0:P.fanSize*P.bead*tw*1.6*near; m4.compose(tmp,q,sv.setScalar(s));", p)

# ---- at3500 + at3722: one resting place, square-on to the strands at the cut-off; the camera rises for the time machine ----
p = sub("const ac=A.clone().lerp(B,.5).add(new THREE.Vector3(0,H*.45,0)); W.ARC={pos:ac.clone().add(new THREE.Vector3(-2,1,R*2.3+7)),tgt:ac};",
        "const c0=riverPt(0,0,XGREY+4.5,new THREE.Vector3()), DC=R*2.3+7; W.CUT={pos:c0.clone().add(new THREE.Vector3(0,.6,DC)),tgt:c0.clone()};   // 1F3: square-on, perpendicular to the strands\n"
        "  const ac=c0.clone().add(new THREE.Vector3(0,H*.78,0)); W.ARC={pos:ac.clone().add(new THREE.Vector3(0,.6,DC*1.22)),tgt:ac};   // risen straight up (and a touch back) so the arc has room", p)
p = sub("  else {const e=ease(clamp((t-(S.arcDraw-2.2))/4.2)), a=1-e; shot.pos.set(0,0,0).addScaledVector(W.CUT.pos,a*a).addScaledVector(W.MID,2*a*e).addScaledVector(W.ARC.pos,e*e); shot.tgt.lerpVectors(W.CUT.tgt,W.ARC.tgt,e); trunk=1}",
        "  else {const e=ease(clamp((t-EDIT_1D.cam.rise0)/EDIT_1D.cam.rised)); shot.pos.lerpVectors(W.CUT.pos,W.ARC.pos,e); shot.tgt.lerpVectors(W.CUT.tgt,W.ARC.tgt,e); trunk=1}", p)

# ---- at3372: into the river at once, among the strands by "Each of you writing" ----
p = sub("const r0=S.river, r1=S.flyDown, outAt=Math.max(r0+5,r1-4.5), pin=ease(clamp((t-(r0+1.2))/3.5)),",
        "const r0=S.river, r1=S.flyDown, outAt=EDIT_1D.cam.out0, pin=ease(clamp((t-EDIT_1D.cam.pin0)/EDIT_1D.cam.pind)),", p)

# ---- the cat discs: like the bead media (feathered disc facing the camera), sitting on the two cloud nodes ----
p = sub("function mediaInit(){for(const [j,m] of Object.entries(BEAD_MEDIA)){if(!m||!m.src) continue; let tex, el=null, ready;",
        "const CATS=[];\n"
        "function catInit(){for(const [k,m] of Object.entries(BEAD_MEDIA)){if(!/^c\\d$/.test(k)||!m||!m.src) continue; const o={j:+k.slice(1),m}; let tex;\n"
        "    o.ready=new Promise(r=>{tex=new THREE.TextureLoader().load(m.src,t=>{fitCover(t,t.image.width,t.image.height); r()},undefined,()=>{console.error('cat media failed',m.src); r()})});\n"
        "    tex.colorSpace=THREE.SRGBColorSpace; tex.minFilter=THREE.LinearFilter; tex.generateMipmaps=false; o.tex=tex;\n"
        "    o.mat=new THREE.MeshBasicMaterial({map:tex,alphaMap:feather(),transparent:true,opacity:0,depthWrite:false,depthTest:false,toneMapped:false}); o.mesh=new THREE.Mesh(new THREE.CircleGeometry(1,64),o.mat);\n"
        "    o.mesh.visible=false; o.mesh.frustumCulled=false; o.mesh.renderOrder=10; scene.add(o.mesh); CATS.push(o)}}\n"
        "function catApply(t){for(const o of CATS){const on=t>TA&&t<tPick0+1.2&&W.EXI; o.mesh.visible=!!on; if(!on) continue;\n"
        "    const sp=ss(S.open,S.open+D.open,t), wv=VISIT[o.j]||0; o.mesh.position.copy(W.basePos[W.iH+NA]).addScaledVector(W.fanOff[W.EXI[o.j]],P.fanSpread*sp); o.mesh.quaternion.copy(camera.quaternion);\n"
        "    o.mesh.scale.setScalar(Math.max(.001,sp*lerp(o.m.scale||.2,o.m.near||.34,wv)));\n"
        "    o.mat.opacity=ss(S.open+.6,S.open+D.open,t)*(1-ss(tPick0,tPick0+1.1,t))*lerp(.85,1,wv); pushIn(o.tex,1+(o.m.push??.04)*wv)}}\n"
        "function mediaInit(){catInit(); for(const [j,m] of Object.entries(BEAD_MEDIA)){if(!m||!m.src||/^c/.test(j)) continue; let tex, el=null, ready;", p)
p = sub("  stackApply(t); mediaApply(t); drawWords(t);\n}", "  stackApply(t); mediaApply(t); catApply(t); drawWords(t);\n}", p)
p = sub("mediaReady(){return Promise.all(MEDIA.map(o=>o.ready)).then(()=>MEDIA.length)},",
        "mediaReady(){return Promise.all([...MEDIA,...CATS].map(o=>o.ready)).then(()=>MEDIA.length+CATS.length)},", p)
