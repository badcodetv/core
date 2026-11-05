/* Slide 13: the Ostrogorski pub. Five people, the Sun party's three policies.
   Opinions (1 = for): three Sun voters each like two policies and dislike a different one,
   two Moon voters dislike all three. So every policy loses 3-2, and the party wins 3-2.
   step 0: the table, five people, a pint each, the Sun and Moon beer mats, three policy cards.
   step 1: vote on each policy: everyone's opinions light up, each card gets 2 for / 3 against, LOSES 3-2.
   step 2: vote for a party: the cards go, each person drops a token on a mat, SUN WINS 3-2.
   The opinion lights stay on in step 2: same people, same opinions. */
THEME.scenes.pub=function(mount,slide,H){
  const T=THEME.three,P=THEME.palette;
  const k=T.setup(mount,{cam:[0,4.6,12.6],look:[0,2.1,0],fov:38});
  const glow=(m,c,i)=>{m.material.emissive=new THREE.Color(c);m.material.emissiveIntensity=i;return m};
  const add=(m,x,y,z)=>{m.position.set(x,y,z);k.scene.add(m);return m};
  /* seats, left to right: name, opinion on policies 1-3 */
  const people=[["MEL",[0,1,1]],["",[0,0,0]],["",[1,0,1]],["",[0,0,0]],["",[1,1,0]]];
  const shirts=[P.bricks[4],P.bricks[5],P.bar2,P.dk,P.ok];
  add(T.box(13.4,.3,3.2,0x7a5232),0,-.15,.3);
  add(T.box(13.4,.7,.25,0x5e3f26),0,-.6,1.8);
  const sunMat=add(glow(new THREE.Mesh(new THREE.CylinderGeometry(.85,.85,.08,8),new THREE.MeshStandardMaterial({color:P.warn,flatShading:true})),P.warn,.35),-5.6,.04,.6);
  const moonMat=add(glow(new THREE.Mesh(new THREE.CylinderGeometry(.85,.85,.08,8),new THREE.MeshStandardMaterial({color:P.bar2,flatShading:true})),P.bar2,.45),5.6,.04,.6);
  k.label("SUN PARTY","warn",sunMat,[0,-.2,1.25]);k.label("MOON PARTY","",moonMat,[0,-.2,1.25]);
  const seat=[-3.6,-1.8,0,1.8,3.6];
  const tok=new THREE.CylinderGeometry(.42,.42,.18,8);let sunN=0,moonN=0;
  const folk=people.map(([name,op],i)=>{const x=seat[i];
    add(T.box(1.1,1.5,.8,shirts[i]),x,.75,-1);
    const head=add(T.box(.72,.72,.72,0xe2b48c),x,1.92,-1);
    add(T.box(.36,.62,.36,0xe5a62e),x+.55,.31,0);add(T.box(.38,.12,.38,P.white),x+.55,.66,0);
    if(name)k.label(name,"",head,[0,.55,0]);
    const lights=op.map((o,j)=>{const m=add(glow(T.box(.3,.3,.3,o?P.ok:P.err),o?P.ok:P.err,.5),x-.45+j*.42,.15,.95);m.scale.setScalar(.001);return m});
    const sun=op.some(o=>o);const n=sun?sunN++:moonN++;
    const t=add(new THREE.Mesh(tok,new THREE.MeshStandardMaterial({color:sun?P.warn:P.bar2,flatShading:true})),x,.1,.3);t.visible=false;
    return {op,lights,t,from:new THREE.Vector3(x,2.6,.3),to:new THREE.Vector3(sun?-5.6:5.6,.17+n*.2,.6),delay:i*.08};
  });
  const cards=[0,1,2].map(j=>{const x=(j-1)*3.4;
    const c=add(T.box(2.5,1.25,.14,P.win),x,4.35,-.6);
    const lab=k.label("POLICY "+(j+1),"",c,[0,.22,0]);
    const chips=folk.map((f,i)=>{const m=add(T.box(.34,.34,.34,f.op[j]?P.ok:P.err),x-.84+i*.42,3.45,-.4);m.scale.setScalar(.001);return m});
    const res=k.label("LOSES 3-2","err",c,[0,1.15,0]);res.el.style.opacity=0;
    return {c,lab,chips,res,home:c.position.clone(),grey:new THREE.Color(P.win),red:new THREE.Color(0xe8a3a3),delay:j*.15};
  });
  const hold=new THREE.Object3D();hold.position.set(0,4.6,0);k.scene.add(hold);
  const win=k.label("SUN WINS 3-2","ok",hold);win.el.style.opacity=0;win.el.style.fontSize="34px";
  const sunT=k.label("3","warn",sunMat,[0,1.25,0]),moonT=k.label("2","",moonMat,[0,1.05,0]);
  [sunT,moonT].forEach(l=>{l.el.style.opacity=0;l.el.style.fontSize="34px"});
  let target=0,t=0;
  k.loop(dt=>{t=H.reduced?target:T.damp(t,target,3,dt);
    const a=T.ease(t*1.2),b=T.ease((t-1)*1.25);
    folk.forEach(f=>{f.lights.forEach(m=>m.scale.setScalar(Math.max(.001,a)));
      const c=T.ease((t-1)*1.6-f.delay);f.t.visible=c>.01;
      const p=f.from.clone().lerp(f.to,c);p.y+=Math.sin(c*Math.PI)*1.2;f.t.position.copy(p);});
    cards.forEach(cd=>{const s=T.ease(t*1.4-cd.delay);
      cd.chips.forEach(m=>m.scale.setScalar(Math.max(.001,s*(1-b))));
      cd.c.material.color.copy(cd.grey).lerp(cd.red,s);
      cd.c.position.copy(cd.home);cd.c.position.y+=b*3;cd.c.scale.setScalar(Math.max(.001,1-b));
      cd.res.el.style.opacity=String(s*(1-b));cd.lab.el.style.opacity=String(1-b);});
    const w=T.ease((t-1.4)*1.8);win.el.style.opacity=String(w);sunT.el.style.opacity=moonT.el.style.opacity=String(w);
  });
  return {step(n){target=n},stop(){k.stop()}};
};
