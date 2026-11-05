/* Slide 3: "Older than the light bulb."
   step 0: close on the left, 1265 / 1832 / 1872 land one at a time.
   step 1: camera moves right, Swan 1878 and Edison 1879 land, the bulb lights,
           a bracket over the first three reads OLDER THAN THE BULB.
   step 2: camera pulls back, the phone lands at 2007 on the far right.
   The track is not to scale: breaks (gaps) mark the long stretches. */
THEME.scenes.timeline=function(mount,slide,H){
  const T=THEME.three,P=THEME.palette;
  const k=T.setup(mount,{cam:[-5.2,2.6,9],look:[-5.2,1.6,0],fov:34});
  [[-9.6,-7.1],[-6.5,5.3],[6.0,9.8]].forEach(([a,b])=>{const m=T.box(b-a,.22,.7,P.win);m.position.set((a+b)/2,-.11,0);k.scene.add(m)});
  const marks=[
    {x:-8.5,y:"1265",n:"PARLIAMENT",h:1.1,at:-.85,c:P.bar2},
    {x:-5,y:"1832",n:"REFORM ACT",h:2.4,at:-.55,c:P.bar2},
    {x:-1.6,y:"1872",n:"SECRET BALLOT",h:1.1,at:-.25,c:P.bar2},
    {x:1.4,y:"1878",n:"SWAN LAMP",h:2.4,at:.15,c:P.warn},
    {x:3.3,y:"1879",n:"EDISON LAMP",h:1.1,at:.4,c:P.warn},
  ];
  function tag(text,cls,obj,off){const l=k.label(text,cls,obj,off);l.el.style.whiteSpace="pre";l.el.style.textAlign="center";l.el.style.lineHeight="1.15";l.el.style.opacity=0;return l}
  marks.forEach(m=>{const g=new THREE.Group();g.position.x=m.x;
    const post=T.box(.16,m.h,.16,P.dk);post.position.y=m.h/2;g.add(post);
    const cap=T.box(.6,.32,.6,m.c);cap.position.y=m.h;g.add(cap);
    k.scene.add(g);m.g=g;m.lab=tag(m.y+"\n"+m.n,m.c===P.warn?"warn":"",cap,[0,.3,0]);});
  /* the bulb: low-poly glass on a screw base, between Swan and Edison */
  const bulb=new THREE.Group();bulb.position.set(2.35,4.45,0);bulb.userData.y=4.45;
  const glassM=new THREE.MeshStandardMaterial({color:0x9b9a93,emissive:P.warn,emissiveIntensity:0,flatShading:true,roughness:.6});
  const glass=new THREE.Mesh(new THREE.IcosahedronGeometry(.5,1),glassM);bulb.add(glass);
  const screw=T.box(.38,.34,.38,P.dk);screw.position.y=-.55;bulb.add(screw);
  const halo=new THREE.Mesh(new THREE.IcosahedronGeometry(.95,1),new THREE.MeshBasicMaterial({color:P.warn,transparent:true,opacity:0,depthWrite:false}));bulb.add(halo);
  const lamp=new THREE.PointLight(P.warn,0,9);bulb.add(lamp);k.scene.add(bulb);
  /* bracket over the first three */
  const br=new THREE.Group();br.position.set(-5.05,4.25,0);
  const bar=T.box(7.4,.14,.14,P.err);br.add(bar);
  [-3.7,3.7].forEach(x=>{const e=T.box(.14,.45,.14,P.err);e.position.set(x,-.22,0);br.add(e)});
  k.scene.add(br);const brLab=tag("OLDER THAN THE BULB","err",bar,[0,.25,0]);
  /* the phone */
  const phone=new THREE.Group();phone.position.set(8,0,0);
  const body=T.box(.95,1.7,.16,P.ink);body.position.y=.85;phone.add(body);
  const scr=T.box(.78,1.4,.04,P.bar2);scr.position.set(0,.88,.09);phone.add(scr);
  k.scene.add(phone);const phLab=tag("2007\nSMARTPHONE","ok",body,[0,1.05,0]);
  const cams=[[-5.2,2.6,9,-5.2,1.6],[-2.4,3,12,-2.4,2.2],[0,3.2,16,0,2.3]];
  let target=0,t=-1;const look=new THREE.Vector3();
  function grow(g,a){g.visible=a>.01;g.scale.setScalar(Math.max(.001,a));g.position.y=(g.userData.y||0)+(1-a)*2.5}
  k.loop(dt=>{t=H.reduced?target:T.damp(t,target,2.6,dt);
    const c=Math.max(0,Math.min(2,t)),i=Math.min(1,Math.floor(c)),f=T.ease(c-i),A=cams[i],B=cams[i+1];
    const q=A.map((v,j)=>v+(B[j]-v)*f);k.camera.position.set(q[0],q[1],q[2]);look.set(q[3],q[4],0);k.camera.lookAt(look);
    marks.forEach(m=>{const a=T.ease((t-m.at)/.3);grow(m.g,a);m.lab.el.style.opacity=String(a>.9?1:0)});
    const lit=T.ease((t-.55)/.4);grow(bulb,T.ease((t-.05)/.3));
    glassM.color.setHex(0x9b9a93).lerp(new THREE.Color(P.warn),lit);glassM.emissiveIntensity=lit*.9;
    halo.material.opacity=lit*.28;lamp.intensity=lit*1.6;
    const b=T.ease((t-.75)/.25);br.visible=b>.01;br.scale.set(Math.max(.001,b),1,1);brLab.el.style.opacity=String(b>.9?1:0);
    const p=T.ease((t-1.3)/.4);grow(phone,p);phLab.el.style.opacity=String(p>.9?1:0);
  });
  return {step(n){target=n},stop(){k.stop()}};
};
