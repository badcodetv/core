/* ---------- 1F2: the materialist stack (Kai's timeline note, 10 Nov) ----------
   Six cards on a vertical thread (the same white thread as the string of beads), each a simple emblem with a plain label:
   SOCIETY > INDIVIDUAL > BIOLOGY > CHEMISTRY > PHYSICS (an atom that opens into the standard model) > MATHEMATICS.
   The camera goes down it, each card landing on its word; pulls back to the whole stack; an empty dashed card lands beside
   it on "something missing"; it lights warm on "Consciousness"; then that light drops into the first bead of the string.
   Every number here is on the film clock (EDIT_1D.stack, from make.py), so film mode records it frame-exact. */
const STK=EDIT_1D.stack, SC={w:3.0,h:2.0,gap:2.45,slotX:3.9,slotK:4};
const WARM=new THREE.Color('#ffb347'), COOL=0x9cc0ff, PALE=0xdfe8f0;
const ST={group:null,lgroup:null,lmats:[],layers:[],slot:null};
const rrect=(w,h,r,n=8)=>{const pts=[], cs=[[w/2-r,h/2-r,0],[-w/2+r,h/2-r,Math.PI/2],[-w/2+r,-h/2+r,Math.PI],[w/2-r,-h/2+r,Math.PI*1.5]];
  for(const [cx,cy,a0] of cs) for(let i=0;i<=n;i++){const a=a0+i/n*Math.PI/2; pts.push(cx+Math.cos(a)*r,cy+Math.sin(a)*r,0)} pts.push(pts[0],pts[1],pts[2]); return pts};
function stackLine(pos,color,px,op,extra={}){const g=new LineGeometry(); g.setPositions(pos);
  const m=new LineMaterial({color,linewidth:px,transparent:true,opacity:op,depthTest:false,...extra}); m.userData={px,op}; ST.lmats.push(m);
  const l=new Line2(g,m); l.computeLineDistances(); l.frustumCulled=false; return l}
function canvasTex(w,h,draw){const c=document.createElement('canvas'); c.width=w; c.height=h; const x=c.getContext('2d'); draw(x,w,h);
  const t=new THREE.CanvasTexture(c); t.colorSpace=THREE.SRGBColorSpace; t.anisotropy=4; return t}
function stackBuild(){
  if(ST.group){scene.remove(ST.group); lineScene.remove(ST.lgroup); scene.remove(ST.light)}
  ST.lmats=[]; ST.layers=[];
  const B=W.basePos[W.iH], g=new THREE.Group(), lg=new THREE.Group();
  ST.C=B.clone().add(new THREE.Vector3(-1.4,16.5,-3.5)); g.position.copy(ST.C); lg.position.copy(ST.C); ST.group=g; ST.lgroup=lg;
  const reg=(k,m,op)=>{m.transparent=true; m.depthWrite=false; m.userData.op=op; ST.layers[k].mats.push(m); return m};
  const std=(k,color,op=.95,em=.35)=>reg(k,new THREE.MeshStandardMaterial({color,emissive:color,emissiveIntensity:em,roughness:.3,metalness:.1}),op);
  const bas=(k,color,op)=>reg(k,new THREE.MeshBasicMaterial({color,toneMapped:false}),op);
  for(let k=0;k<6;k++){
    const y=-k*SC.gap, card=new THREE.Group(), em=new THREE.Group(); card.position.set(0,y,0); card.add(em); g.add(card);
    const L={k,card,em,mats:[],label:STK.labels[k],t:STK.lay[k]}; ST.layers.push(L);
    L.outline=stackLine(rrect(SC.w,SC.h,.16),0xcfe0ff,1.3,.5); L.outline.position.y=y; lg.add(L.outline);
    if(k<5){L.spine=stackLine([0,y-SC.h/2,0,0,y-SC.gap+SC.h/2,0],0xd1d1d1,1.6,.9); lg.add(L.spine)}
    const fill=new THREE.Mesh(new THREE.ShapeGeometry((()=>{const s=new THREE.Shape(), p=rrect(SC.w,SC.h,.16); s.moveTo(p[0],p[1]); for(let i=3;i<p.length;i+=3) s.lineTo(p[i],p[i+1]); return s})()),bas(k,0x0d1626,.55));
    fill.position.z=-.35; card.add(fill);
    if(k===0){ /* SOCIETY: a crowd as a network */
      const r=rng(31), pts=[]; for(let i=0;i<54;i++){const a=r()*Math.PI*2, d=Math.sqrt(r()); pts.push(new THREE.Vector3(Math.cos(a)*d*1.18,Math.sin(a)*d*.72,(r()-.5)*.5))}
      const dots=new THREE.InstancedMesh(new THREE.SphereGeometry(.055,12,8),std(k,COOL,.95,.5),pts.length); pts.forEach((p,i)=>{m4.compose(p,q,sv.setScalar(.8+((i*7)%5)*.12)); dots.setMatrixAt(i,m4)}); em.add(dots);
      const seg=[]; pts.forEach((p,i)=>{const nb=pts.map((o,j)=>[o.distanceToSquared(p),j]).sort((a,b)=>a[0]-b[0]).slice(1,3); for(const [,j] of nb) seg.push(p.x,p.y,p.z,pts[j].x,pts[j].y,pts[j].z)});
      const sg=new THREE.BufferGeometry(); sg.setAttribute('position',new THREE.Float32BufferAttribute(seg,3)); em.add(new THREE.LineSegments(sg,reg(k,new THREE.LineBasicMaterial({color:0xcfe0ff}),.45)))}
    if(k===1){ /* INDIVIDUAL: one figure */
      const mt=std(k,COOL,.95,.4), cap=(r,l)=>new THREE.CapsuleGeometry(r,l,6,16);
      const head=new THREE.Mesh(new THREE.SphereGeometry(.19,24,16),mt); head.position.y=.6;
      const body=new THREE.Mesh(cap(.2,.42),mt); body.position.y=.07;
      const armL=new THREE.Mesh(cap(.065,.5),mt); armL.position.set(-.31,.05,0); armL.rotation.z=-.16;
      const armR=armL.clone(); armR.position.x=.31; armR.rotation.z=.16;
      const legL=new THREE.Mesh(cap(.08,.5),mt); legL.position.set(-.11,-.6,0); const legR=legL.clone(); legR.position.x=.11;
      em.add(head,body,armL,armR,legL,legR); em.position.y=-.02}
    if(k===2){ /* BIOLOGY: a cell */
      const mem=new THREE.Mesh(new THREE.TorusGeometry(.8,.03,10,96),std(k,COOL,.95,.6)); mem.scale.set(1.32,.92,1); em.add(mem);
      const cyto=new THREE.Mesh(new THREE.CircleGeometry(.8,64),bas(k,0x6d8fd0,.16)); cyto.scale.copy(mem.scale); em.add(cyto);
      const nuc=new THREE.Mesh(new THREE.SphereGeometry(.28,32,20),std(k,0x86a8ff,.85,.35)); nuc.position.set(.22,.06,0); em.add(nuc);
      const nl=new THREE.Mesh(new THREE.SphereGeometry(.1,16,12),std(k,PALE,.95,.6)); nl.position.set(.27,.1,.2); em.add(nl);
      const r=rng(41), mt=std(k,0xb9d0ff,.9,.45);
      for(let i=0;i<6;i++){const m=new THREE.Mesh(new THREE.CapsuleGeometry(.045,.13,4,10),mt); const a=i/6*Math.PI*2+r()*.5, d=.5+r()*.25; m.position.set(Math.cos(a)*d*1.25-.05,Math.sin(a)*d*.8,0); m.rotation.z=r()*3; em.add(m)}
      const dots=new THREE.InstancedMesh(new THREE.SphereGeometry(.022,8,6),mt,22); for(let i=0;i<22;i++){const a=r()*6.283, d=.25+r()*.6; m4.compose(new THREE.Vector3(Math.cos(a)*d*1.2,Math.sin(a)*d*.75,0),q,sv.setScalar(1)); dots.setMatrixAt(i,m4)} em.add(dots)}
    if(k===3){ /* CHEMISTRY: a ball-and-stick molecule (a benzene ring) */
      const cM=std(k,COOL,.97,.35), hM=std(k,PALE,.97,.45), bM=std(k,0xcfe0ff,.9,.3), up=new THREE.Vector3(0,1,0);
      const stick=(a,b,r)=>{const m=new THREE.Mesh(new THREE.CylinderGeometry(r,r,a.distanceTo(b),10),bM); m.position.copy(a).add(b).multiplyScalar(.5); m.quaternion.setFromUnitVectors(up,b.clone().sub(a).normalize()); em.add(m)};
      const C=[], Hh=[]; for(let i=0;i<6;i++){const a=i/6*Math.PI*2+Math.PI/6; C.push(new THREE.Vector3(Math.cos(a)*.5,Math.sin(a)*.5,0)); Hh.push(new THREE.Vector3(Math.cos(a)*.9,Math.sin(a)*.9,0))}
      for(let i=0;i<6;i++){const a=new THREE.Mesh(new THREE.SphereGeometry(.13,24,16),cM); a.position.copy(C[i]); const h=new THREE.Mesh(new THREE.SphereGeometry(.08,16,12),hM); h.position.copy(Hh[i]); em.add(a,h);
        stick(C[i],C[(i+1)%6],i%2?.026:.042); stick(C[i],Hh[i],.022)}
      em.rotation.x=-.45; L.spin=.35}
    if(k===4){ /* PHYSICS: an atom, then the standard model */
      const atom=new THREE.Group(); em.add(atom); L.atom=atom;
      const r=rng(53), pM=std(k,0xff9b8a,.95,.4), nM=std(k,PALE,.95,.35);
      for(let i=0;i<9;i++){const m=new THREE.Mesh(new THREE.SphereGeometry(.075,16,12),i%2?pM:nM); m.position.set((r()-.5)*.2,(r()-.5)*.2,(r()-.5)*.2); atom.add(m)}
      const oM=std(k,0xcfe0ff,.7,.6), eM=bas(k,0xffffff,1); L.el=[];
      for(let i=0;i<3;i++){const o=new THREE.Group(); o.rotation.set(Math.PI/2+(i-1)*.5,0,i*Math.PI/3); o.scale.set(1.25,.85,1);
        o.add(new THREE.Mesh(new THREE.TorusGeometry(.75,.012,6,128),oM)); const e=new THREE.Mesh(new THREE.SphereGeometry(.045,12,8),eM); o.add(e); L.el.push([e,i*2.1,1.1+i*.25]); atom.add(o)}
      /* the standard model: three planes, quarks / leptons / force carriers, each lit on its own word */
      const SYM=[[['u','','up'],['c','','charm'],['t','','top'],['g','','gluon'],['H','','Higgs']],[['d','','down'],['s','','strange'],['b','','bottom'],['γ','','photon']],
                 [['e','','electron'],['μ','','muon'],['τ','','tau'],['Z','','Z boson']],[['ν','e','e neutrino'],['ν','μ','μ neutrino'],['ν','τ','τ neutrino'],['W','','W boson']]];
      const GW=1280, GH=1000, cell=218, gp=22, ox=(GW-(5*cell+4*gp))/2, oy=(GH-(4*cell+3*gp))/2;
      const grp=(i,j)=>j<3?(i<2?0:1):2, COL=['#8fb4ff','#8fe0b8','#ffb0a0'];
      const plane=gi=>{const tex=canvasTex(GW,GH,(x)=>{x.textAlign='center'; x.textBaseline='middle';
          SYM.forEach((row,i)=>row.forEach(([s,sub,name],j)=>{if(grp(i,j)!==gi&&!(gi===2&&j===4)) return; const c=gi===2&&j===4?'#ffd27a':COL[gi], X=ox+j*(cell+gp), Y=oy+i*(cell+gp);
            x.fillStyle=c+'26'; x.strokeStyle=c; x.lineWidth=5; x.beginPath(); x.roundRect(X,Y,cell,cell,26); x.fill(); x.stroke();
            x.fillStyle='#f3efe7'; x.font='500 112px "Schibsted Grotesk", system-ui, sans-serif'; const sw=x.measureText(s).width; x.fillText(s,X+cell/2-(sub?18:0),Y+cell*.44);
            if(sub){x.font='500 58px "Schibsted Grotesk", system-ui, sans-serif'; x.fillText(sub,X+cell/2+sw/2+4,Y+cell*.56)}
            x.fillStyle=c; x.font='400 30px "Schibsted Grotesk", system-ui, sans-serif'; x.fillText(name,X+cell/2,Y+cell*.83)}))});
        const m=new THREE.Mesh(new THREE.PlaneGeometry(2.62,2.05),bas(k,0xffffff,1)); m.material.map=tex; m.material.toneMapped=false; m.position.z=.02; em.add(m); return m};
      L.grid=[plane(0),plane(1),plane(2)]}
    if(k===5){ /* MATHEMATICS: equations on a grid */
      const tex=canvasTex(1280,860,(x,Wd,Hd)=>{x.strokeStyle='rgba(159,186,230,.22)'; x.lineWidth=2; for(let i=0;i<=Wd;i+=64){x.beginPath(); x.moveTo(i,0); x.lineTo(i,Hd); x.stroke()} for(let j=0;j<=Hd;j+=64){x.beginPath(); x.moveTo(0,j); x.lineTo(Wd,j); x.stroke()}
        x.strokeStyle='rgba(207,224,255,.6)'; x.lineWidth=3; x.beginPath(); x.moveTo(0,640); x.lineTo(Wd,640); x.moveTo(128,0); x.lineTo(128,Hd); x.stroke();
        x.strokeStyle='#8fb4ff'; x.lineWidth=6; x.beginPath(); for(let i=128;i<=Wd;i+=4){const v=640-110*Math.sin((i-128)/70); i===128?x.moveTo(i,v):x.lineTo(i,v)} x.stroke();
        x.fillStyle='#f3efe7'; x.textBaseline='alphabetic'; const F=(s,px,X,Y,it)=>{x.font=`${it?'italic ':''}400 ${px}px Georgia, "Young Serif", serif`; x.fillText(s,X,Y); return x.measureText(s).width};
        let X=170; X+=F('e',104,X,190,1); X+=F('iπ',56,X+4,138,1)+10; F(' + 1 = 0',104,X,190);
        X=170; X+=F('a',84,X,350,1); X+=F('2',46,X+4,312); X+=F(' + ',84,X+6,350)+6; X+=F('b',84,X,350,1); X+=F('2',46,X+4,312); X+=F(' = ',84,X+6,350)+6; X+=F('c',84,X,350,1); F('2',46,X+4,312);
        F('∫ f(x) dx',70,820,350,1); F('π = 3.14159…',62,820,190)});
      const m=new THREE.Mesh(new THREE.PlaneGeometry(2.7,1.81),bas(k,0xffffff,1)); m.material.map=tex; em.add(m)}
  }
  /* the slot: an empty dashed card beside the stack, not on its thread; lights warm on "Consciousness" */
  const sl={}; ST.slot=sl; const sy=-SC.slotK*SC.gap;
  sl.dash=stackLine(rrect(SC.w,SC.h,.16),0xdfe8f0,2.6,1,{dashed:true,dashSize:.14,gapSize:.1}); sl.dash.position.set(SC.slotX,sy,0); lg.add(sl.dash);
  sl.solid=stackLine(rrect(SC.w,SC.h,.16),WARM.getHex(),2.6,1); sl.solid.position.set(SC.slotX,sy,0); lg.add(sl.solid);
  sl.fillM=new THREE.MeshBasicMaterial({color:WARM,transparent:true,opacity:0,depthWrite:false,blending:THREE.AdditiveBlending,toneMapped:false});
  sl.fill=new THREE.Mesh(new THREE.PlaneGeometry(SC.w-.12,SC.h-.12),sl.fillM); sl.fill.position.set(SC.slotX,sy,-.05); g.add(sl.fill);
  sl.pos=ST.C.clone().add(new THREE.Vector3(SC.slotX,sy,.1));
  /* the light: a warm ember, the same warm as the people in the river */
  const lt=new THREE.Group(); ST.light=lt; scene.add(lt);
  ST.glow=new THREE.Sprite(new THREE.SpriteMaterial({map:dot(),color:WARM,transparent:true,opacity:0,depthWrite:false,depthTest:false,blending:THREE.AdditiveBlending}));
  ST.core=new THREE.Mesh(new THREE.SphereGeometry(1,24,16),new THREE.MeshBasicMaterial({color:WARM.clone().multiplyScalar(2.2),transparent:true,opacity:0,depthWrite:false,toneMapped:false}));
  lt.add(ST.glow,ST.core); ST.glow.frustumCulled=ST.core.frustumCulled=false;
  scene.add(g); lineScene.add(lg);
  /* the shots */
  const cen=k=>ST.C.clone().add(new THREE.Vector3(0,-k*SC.gap,0)), V=new THREE.Vector3(-1.05,1.05,6.1);
  const pose=(tgt,off)=>({tgt,pos:tgt.clone().add(off)}), lay=k=>pose(cen(k).add(new THREE.Vector3(-.45,0,0)),V), drift=(p,d)=>({tgt:p.tgt.clone().add(d),pos:p.pos.clone().add(d)});
  const ccol=ST.C.clone().add(new THREE.Vector3(SC.slotX/2-.55,-2.5*SC.gap,0)), wide=pose(ccol,new THREE.Vector3(-2.2,2.4,25.5));
  const push=pose(ccol.clone().add(new THREE.Vector3(.9,-1.6,0)),new THREE.Vector3(-2.2,1.9,21));
  const open=pose(cen(0).add(new THREE.Vector3(0,-2.6,0)),new THREE.Vector3(-2.4,6.4,5.4)), T0=STK.lay, K=[];
  const dn=new THREE.Vector3(0,-.14,0);
  K.push([0,drift(open,new THREE.Vector3(0,.8,0))],[T0[0]-1.5,open]);
  for(let k=0;k<6;k++){const arr=T0[k]+(k===5?.2:.18), [lt,lp]=K[K.length-1];
    if(k===5) K.push([STK.under-.1,drift(lp,dn)]);                                   // "And under all that…": the slow drop to the maths
    else if(k>0) K.push([Math.max(lt+.05,arr-Math.min(1.05,(arr-lt)*.85)),drift(lp,dn)]);
    K.push([arr,lay(k)]);
    if(k===4){const g4=pose(cen(4).add(new THREE.Vector3(-.3,0,0)),V.clone().multiplyScalar(.9)); K.push([STK.quarks-.25,drift(lay(4),dn)],[STK.quarks+.45,g4])}}
  K.push([STK.s02-.15,drift(lay(5),dn)],[STK.s02+2.4,wide],[STK.consc-.2,drift(wide,new THREE.Vector3(0,0,-.6))],[STK.consc+3.2,push]);
  K.sort((a,b)=>a[0]-b[0]); ST.K=K;
}
function stackShot(t,out){const K=ST.K; let i=0; while(i<K.length-1&&K[i+1][0]<=t) i++;
  const a=K[i], b=K[Math.min(i+1,K.length-1)], e=b===a||t<=a[0]?(t<a[0]?0:1):ease(clamp((t-a[0])/Math.max(.001,b[0]-a[0])));
  out.tgt.lerpVectors(a[1].tgt,b[1].tgt,e); out.pos.lerpVectors(a[1].pos,b[1].pos,e);
  const d=STK.depart; if(t>d){ /* the bridge: follow the light down, closing to the first-bead shot */
    const u=clamp((t-d)/STK.fly), lp=stackLightPos(t,new THREE.Vector3()); closeShot(S.lead,sA);
    const off0=out.pos.clone().sub(out.tgt), off1=sA.pos.clone().sub(sA.tgt), e2=ease(u);
    const len=Math.exp(lerp(Math.log(off0.length()),Math.log(off1.length()),e2)), dir=off0.normalize().lerp(off1.normalize(),e2).normalize();
    out.tgt.lerp(lp,ss(0,.32,u)).lerp(sA.tgt,ss(.72,1,u)); out.pos.copy(out.tgt).addScaledVector(dir,len)}
  return out}
function stackLightPos(t,out){const u=ease(clamp((t-STK.depart)/STK.fly)), A=ST.slot.pos, B=W.basePos[W.iH], c=A.clone().lerp(B,.25).add(new THREE.Vector3(0,-1.5,2.2));
  return out.copy(A).multiplyScalar((1-u)*(1-u)).addScaledVector(c,2*u*(1-u)).addScaledVector(B,u*u)}
const bump=(t,a,up=.15,dn=.9)=>ss(a,a+up,t)*(1-ss(a+up,a+up+dn,t));
function stackApply(t){
  const live=t<S.lead+.6; ST.group.visible=ST.lgroup.visible=live&&t<STK.depart+STK.fly; ST.light.visible=t>=STK.consc-.05&&t<beadT[0]+.7;
  for(const m of ST.lmats){m.resolution.copy(M.thread.resolution); m.linewidth=m.userData.px*M.thread.linewidth/P.threadPx}
  if(ST.group.visible){
    const fade=1-ss(STK.depart+.25,STK.depart+STK.fly*.8,t), shelf=ss(.3,1.4,t), wide=ss(STK.s02,STK.s02+1.2,t), T0=STK.lay;
    for(const L of ST.layers){const k=L.k, a=ss(L.t,L.t+.35,t), nx=k<5?T0[k+1]:STK.s02, dim=1-.5*ss(nx,nx+.5,t)*(1-wide);
      const pop=backOut(clamp((t-L.t)/.45)); L.em.scale.setScalar(Math.max(.001,pop)); L.em.visible=a>.001;
      for(const m of L.mats) m.opacity=m.userData.op*a*dim*fade;
      let ol=lerp(.32*shelf,.6,a)*dim; if(k===4) ol+=.45*bump(t,STK.quarks3-.1,.2,1.2)*fade; L.outline.material.opacity=Math.min(1,ol)*fade;
      if(L.spine){const b=ss(T0[k+1],T0[k+1]+.4,t); L.spine.material.opacity=lerp(.3*shelf,.8,b)*fade}
      if(L.spin) L.em.rotation.y=Math.sin(t*L.spin)*.6;
      if(L.atom){const g=ss(STK.quarks,STK.quarks+.45,t); L.atom.scale.setScalar(Math.max(.001,1-g)); L.atom.visible=g<.999; L.atom.rotation.y=t*.4;
        for(const [e,ph,sp] of L.el){const an=t*sp*2.4+ph; e.position.set(Math.cos(an)*.75,Math.sin(an)*.75,0)}
        const gq=backOut(clamp((t-STK.quarks)/.45)), gl=ss(STK.leptons,STK.leptons+.35,t), gb=ss(STK.leptons+.5,STK.leptons+1.1,t), echo=1+.6*bump(t,STK.quarks3-.1,.2,1.2);
        L.grid.forEach((m,i)=>{m.visible=t>=STK.quarks; m.scale.setScalar(Math.max(.001,gq)); const lit=i===0?1:i===1?lerp(.25,1,gl):lerp(.25,.75,gb);
          m.material.opacity=Math.min(1,ss(STK.quarks,STK.quarks+.3,t)*lit*dim*fade); m.material.color.setScalar(i<2?echo:1)})}}
    const sl=ST.slot, ap=ss(STK.missing,STK.missing+.4,t), on=ss(STK.consc,STK.consc+.5,t);
    sl.dash.material.opacity=ap*(1-on)*fade; sl.dash.material.dashOffset=-t*.15;
    sl.solid.material.opacity=on*fade; sl.fillM.opacity=on*(.16+.05*Math.sin((t-STK.consc)*2.4))*(1-ss(STK.depart,STK.depart+1,t))}
  if(ST.light.visible){ /* the light: swells in the slot, leaves as she finishes, lands where the first bead will be, and waits for "toast" */
    const on=backOut(clamp((t-STK.consc)/.6)), u=clamp((t-STK.depart)/STK.fly), br=1+.12*Math.sin((t-STK.consc)*2.2), out=1-ss(beadT[0]-.05,beadT[0]+.45,t);
    stackLightPos(t,ST.light.position); const sz=lerp(1.25,.1,ease(u))*br*Math.max(.001,on);
    ST.glow.scale.setScalar(sz*1.9); ST.glow.material.opacity=.95*out; ST.core.scale.setScalar(sz*.16); ST.core.material.opacity=out}
  if(t<S.lead){bokeh.uniforms.aperture.value=lerp(.004,.028,ss(STK.depart+STK.fly*.5,S.lead,t)); bokeh.uniforms.maxblur.value=.012}
}
const wideK=t=>ss(STK.s02,STK.s02+1.6,t);
function stackWords(t,fs){ /* the plain labels, left of each card; CONSCIOUSNESS beside the slot once it lights */
  if(!ST.group||!ST.group.visible) return; camera.updateMatrixWorld();   // this frame's camera, not the last one's (apply() runs before render)
  const cw=txtCanvas.width, chh=txtCanvas.height, f=Math.round(chh*(.034-.008*wideK(t)));
  const fade=1-ss(STK.depart+.1,STK.depart+1.2,t), wide=ss(STK.s02,STK.s02+1.2,t), put=(v,s,col,op,align,dx)=>{if(op<=.01) return; tmp.copy(v).project(camera); if(tmp.z>=1) return;
    const x=(tmp.x*.5+.5)*cw+dx*f, y=(-tmp.y*.5+.5)*chh+f*.35; tctx.globalAlpha=op; tctx.textAlign=align; tctx.fillStyle=col; tctx.fillText(s,x,y)};
  tctx.save(); tctx.font=`600 ${f}px "Schibsted Grotesk", system-ui, sans-serif`; tctx.letterSpacing=Math.round(f*.14)+'px'; tctx.shadowColor='rgba(0,0,0,.9)'; tctx.shadowBlur=f*.5; tctx.textBaseline='alphabetic';
  for(const L of ST.layers){const a=ss(L.t,L.t+.25,t), nx=L.k<5?STK.lay[L.k+1]:STK.s02, dim=1-.45*ss(nx,nx+.5,t)*(1-wide);
    put(ST.C.clone().add(new THREE.Vector3(-SC.w/2,-L.k*SC.gap,0)),L.label,'#f3efe7',a*dim*fade,'right',-.7)}
  put(ST.C.clone().add(new THREE.Vector3(SC.slotX+SC.w/2,-SC.slotK*SC.gap,0)),'CONSCIOUSNESS','#ffcf8a',ss(STK.consc+.1,STK.consc+.6,t)*fade,'left',.7);
  tctx.restore()}
