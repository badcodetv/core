/* Slide 32: "No policy without its experiment."
   step 0: two identical towns; the left one is the TRIAL and gets the new (green) bus timetable.
           A gauge between them has a green GO band and a red STOP band; the ALL 40 TOWNS lever is locked.
   step 1: the number rises into GO; the padlock falls off, the lever swings down, the other town gets the new bus.
   step 2: a second run: the number falls into STOP; the lever drops away and the other town keeps the old bus. */
THEME.scenes.towns=function(mount,slide,H){
  const T=THEME.three,P=THEME.palette;
  const k=T.setup(mount,{cam:[0,6.2,12.4],look:[0,1.5,0],fov:34});
  const add=(m,x,y,z)=>{m.position.set(x,y,z);k.scene.add(m);return m};
  const OLD=new THREE.Color(P.warn),NEW=new THREE.Color(P.ok);
  function town(cx,trial){
    const g=new THREE.Group();g.position.x=cx;k.scene.add(g);
    if(trial){const ring=T.box(4.6,.16,4,P.warn);ring.position.y=-.1;g.add(ring)}
    const ground=T.box(4.2,.2,3.6,0x9fc58a);g.add(ground);
    const road=[[0,1.25,3.4,.5],[0,-1.25,3.4,.5],[1.5,0,.5,3],[-1.5,0,.5,3]];
    road.forEach(([x,z,w,d])=>{const r=T.box(w,.06,d,P.dk);r.position.set(x,.12,z);g.add(r)});
    [[-.55,-.35,P.bar2,1.1],[.5,-.4,P.err,.8],[-.5,.45,0xe58a2e,.7],[.55,.4,P.win,1.3]].forEach(([x,z,c,h])=>{
      const b=T.box(.75,h,.6,c);b.position.set(x,.1+h/2,z);g.add(b)});
    const stop=T.box(.12,.9,.12,P.ink);stop.position.set(1.95,.55,1.55);g.add(stop);
    const sign=T.box(.4,.3,.08,trial?P.ok:P.warn);sign.position.set(1.95,1.05,1.55);g.add(sign);
    const bus=T.box(.75,.4,.38,P.warn,{rough:.6});bus.position.y=.35;g.add(bus);
    return {g,bus,sign,u:trial?0:.5};
  }
  const A=town(-5.4,true),B=town(5.4,false);
  k.label("TRIAL","warn",A.g,[0,2.2,0]);
  /* gauge: STOP band at the bottom, GO band at the top, the number rides a marker */
  const GX=-2.15,LO=.2,HI=4.2;
  add(T.box(.9,.2,.9,P.dk),GX,.1,0);
  add(T.box(.55,1.2,.55,P.err),GX,.2+.6,0);
  add(T.box(.55,1.6,.55,0x9b9a93),GX,1.4+.8,0);
  add(T.box(.55,1.2,.55,P.ok),GX,3+.6,0);
  const goT=k.label("GO","ok",null);const stT=k.label("STOP","err",null);
  const marker=add(T.box(1.1,.14,.8,P.ink),GX,2.2,0);
  const num=k.label("50","",marker,[-.95,.25,0]);
  /* lever: base + padlock + handle that swings on a pivot */
  const LX=1.6,lever=new THREE.Group();lever.position.set(LX,0,0);k.scene.add(lever);
  const base=T.box(2.2,.5,1.4,P.bar);base.position.y=.25;lever.add(base);
  const pivot=new THREE.Group();pivot.position.set(0,.55,0);lever.add(pivot);
  const arm=T.box(.22,2.2,.22,P.win);arm.position.y=1.1;pivot.add(arm);
  const knob=T.box(.55,.55,.55,P.err);knob.position.y=2.3;pivot.add(knob);
  const lock=T.box(.6,.5,.25,P.warn);lock.position.set(0,.8,.72);lever.add(lock);
  const shack=T.box(.36,.32,.1,P.dk);shack.position.set(0,1.15,.72);lever.add(shack);
  const anchor=add(new THREE.Object3D(),LX,3.4,0);
  const all=k.label("ALL 40 TOWNS","",anchor,[0,.35,0]);
  const state=k.label("LOCKED","err",anchor,[0,-.25,0]);
  const vtmp=new THREE.Vector3();
  let target=0,t=0;
  k.loop((dt)=>{t=H.reduced?target:T.damp(t,target,2.4,dt);
    const a=T.ease(t),b=T.ease(t-1);
    const val=50+38*a-70*b;
    marker.position.y=LO+(HI-LO)*val/100;
    num.el.textContent=String(Math.round(val));
    num.el.className="tag3d "+(val>=70?"ok":val<=30?"err":"");
    /* band tags sit on the band, to the left of the gauge */
    k.camera.updateMatrixWorld();
    [[goT,3.6],[stT,.8]].forEach(([l,y])=>{vtmp.set(GX+.5,y,0).project(k.camera);
      l.el.style.left=((vtmp.x+1)/2*mount.clientWidth+40)+"px";l.el.style.top=((1-vtmp.y)/2*mount.clientHeight+14)+"px"});
    const un=T.ease((50+38*a-66)/8);           /* unlocks only once the number is in GO */
    lock.position.y=.8-un*1.2;shack.position.y=1.15-un*1.2;lock.rotation.z=shack.rotation.z=un*.9;
    lock.visible=shack.visible=un<.95;
    pivot.rotation.z=-un*1.1;
    lever.position.y=-6*b;lever.rotation.z=-.6*b;lever.visible=b<.97;
    state.el.textContent=b>.5?"STOPPED":un>.5?"UNLOCKED":"LOCKED";
    state.el.className="tag3d "+(b>.5?"err":un>.5?"ok":"err");
    A.bus.material.color.copy(OLD).lerp(NEW,Math.min(1,t*3));
    const on=un*(1-b);B.bus.material.color.copy(OLD).lerp(NEW,on);B.sign.material.color.copy(OLD).lerp(NEW,on);
    [A,B].forEach((tw,i)=>{const fast=i?on:1;if(!H.reduced)tw.u=(tw.u+Math.max(0,dt)*(.07+.07*fast))%1;
      const s=tw.u*4,q=Math.floor(s),f=s-q,rx=1.5,rz=1.25;
      const pts=[[-rx,rz],[rx,rz],[rx,-rz],[-rx,-rz],[-rx,rz]];
      const p0=pts[q],p1=pts[q+1];
      tw.bus.position.x=p0[0]+(p1[0]-p0[0])*f;tw.bus.position.z=p0[1]+(p1[1]-p0[1])*f;
      tw.bus.rotation.y=q%2?Math.PI/2:0;});
  });
  return {step(n){target=n},stop(){k.stop()}};
};
