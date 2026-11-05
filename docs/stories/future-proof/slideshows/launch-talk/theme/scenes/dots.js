/* Slide 37: maps of agreement, not a winner.
   step 0: a field of grey dots scattered over the floor, each one a grumble.
   step 1: the dots drift and clump into four coloured camps.
   step 2: a glowing band forms between them, WHERE WE AGREE; some dots from every camp settle in it,
   the camps pull towards it and four become two (as on vTaiwan's Uber debate). No winner is marked. */
THEME.scenes.dots=function(mount,slide,H){
  const T=THEME.three,P=THEME.palette;
  const k=T.setup(mount,{cam:[0,8.6,9.0],look:[0,-.5,.6],fov:40});
  let seed=7;const rnd=()=>(seed=(seed*16807)%2147483647)/2147483647;
  const floor=T.box(15,.2,7.6,0x1f4a50);floor.position.set(0,-.1,0);k.scene.add(floor);
  const bandMat=new THREE.MeshStandardMaterial({color:P.warn,emissive:new THREE.Color(P.warn),emissiveIntensity:.6,transparent:true,opacity:0,flatShading:true});
  const band=new THREE.Mesh(new THREE.BoxGeometry(1.9,.06,7.2),bandMat);band.position.set(0,.04,0);k.scene.add(band);
  /* four camps (x, z) and where each settles once two pairs merge */
  const camps=[[-4.6,-2],[-4.2,2],[4.4,-2.1],[4.7,1.9]],merged=[[-3.6,0],[-3.6,0],[3.6,0],[3.6,0]];
  const cols=[P.bricks[4],P.err,P.bar2,P.bricks[5]];
  const geo=new THREE.IcosahedronGeometry(.17,0),grey=new THREE.Color(0xb8b7b0);
  const dots=[];
  for(let i=0;i<160;i++){const c=i%4,shared=i%6===0,r=Math.sqrt(rnd())*1.25,a=rnd()*6.283;
    const m=new THREE.Mesh(geo,new THREE.MeshStandardMaterial({color:grey,flatShading:true}));m.position.y=.2;k.scene.add(m);
    const ox=Math.cos(a)*r,oz=Math.sin(a)*r*.85;
    dots.push({m,c,shared,col:new THREE.Color(cols[c]),
      p0:new THREE.Vector3((rnd()-.5)*13.6,.2,(rnd()-.5)*6.6),
      p1:new THREE.Vector3(camps[c][0]+ox,.2,camps[c][1]+oz),
      p2:shared?new THREE.Vector3((rnd()-.5)*1.4,.24,(rnd()-.5)*6.4):new THREE.Vector3(merged[c][0]+ox*1.15,.2,merged[c][1]+oz*1.9),
      ph:rnd()*6.283,delay:rnd()*.25});}
  const anchors=camps.map(([x,z])=>{const o=new THREE.Object3D();o.position.set(x,.3,z);k.scene.add(o);return o});
  const campL=anchors.map((o,i)=>{const l=k.label("CAMP "+(i+1),"",o,[0,0,-1.25]);l.el.style.opacity=0;return l});
  const sides=[[-3.6,0],[3.6,0]].map(([x,z])=>{const o=new THREE.Object3D();o.position.set(x,.3,z);k.scene.add(o);return o});
  const twoL=sides.map((o,i)=>{const l=k.label(["CAMPS 1+2","CAMPS 3+4"][i],"",o,[0,0,-2.35]);l.el.style.opacity=0;return l});
  const agree=k.label("WHERE WE AGREE","warn",band,[0,.3,-3.45]);agree.el.style.opacity=0;agree.el.style.fontSize="30px";
  const noWin=k.label("NO WINNER, NO ALGORITHM CHOOSING","",band,[0,.2,3.9]);noWin.el.style.opacity=0;
  const white=new THREE.Color(P.white);
  let target=0,t=0;
  k.loop((dt,now)=>{t=H.reduced?target:T.damp(t,target,2.6,dt);
    const g=T.ease((t-1)*1.3);
    bandMat.opacity=.8*g;bandMat.emissiveIntensity=.4+.3*g*(1+Math.sin(now*2.2))/2;
    dots.forEach(d=>{const a=T.ease(t*1.3-d.delay),b=T.ease((t-1)*1.4-d.delay);
      const p=d.p0.clone().lerp(d.p1,a).lerp(d.p2,b);
      if(!H.reduced){p.x+=Math.sin(now*.7+d.ph)*.06;p.z+=Math.cos(now*.6+d.ph)*.06;}
      d.m.position.copy(p);
      d.m.material.color.copy(grey).lerp(d.col,a);if(d.shared)d.m.material.color.lerp(white,b*.7);});
    const c1=T.ease(t*1.3-.3);campL.forEach(l=>l.el.style.opacity=String(c1*(1-g)));
    twoL.forEach(l=>l.el.style.opacity=String(g));
    agree.el.style.opacity=String(g);noWin.el.style.opacity=String(T.ease((t-1.5)*2));
  });
  return {step(n){target=n},stop(){k.stop()}};
};
