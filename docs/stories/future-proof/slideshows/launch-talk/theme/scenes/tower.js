/* Slide 19: "Small. Checked. Undoable." vs "One drop. No ticks."
   step 0: LEFT four bricks land one by one, each lights a green tick; RIGHT a crane holds a monolith up high.
   step 1: a fifth brick lands and lights red; the curved REVERT arm comes down and lifts it off; the tower stands.
   step 2: the crane lets the monolith go: it drops whole, thuds, no ticks anywhere.
   Time runs on a clock s: step(n) jumps s to n (earlier steps finish at once) and plays to n+1. */
THEME.scenes.tower=function(mount,slide,H){
  const T=THEME.three,P=THEME.palette;
  const k=T.setup(mount,{cam:[0,4.6,19.5],look:[0,3.5,0],fov:33});
  const BW=2.2,BH=.62,LX=-4.6,RX=4.4,N=4;
  const add=(m,x,y,z=0)=>{m.position.set(x,y,z);k.scene.add(m);return m};
  add(T.box(24,.2,7,0x2f6a70),0,-.1,0);
  add(T.box(3.4,.3,2.2,P.bar),LX,.15);
  add(T.box(3.8,.3,2.4,P.bar),RX,.15);
  /* left: the small bricks, each with its tick tag */
  const cols=[P.bricks[3],P.bricks[4],P.bricks[5],P.bricks[1]];
  const bricks=[...Array(N+1)].map((_,i)=>{
    const m=add(T.box(BW,BH,1.5,i<N?cols[i]:0x9b9a93),LX,9);
    const home=.3+BH/2+i*BH;
    const tag=k.label(i<N?"✓":"✗",i<N?"ok":"err",m,[BW/2+.45,-.12,0]);tag.el.style.opacity=0;
    return {m,home,tag};
  });
  const red=bricks[N];
  /* the revert arm: a curved claw on a rod that comes down over the top brick */
  const arm=new THREE.Group();k.scene.add(arm);
  const claw=new THREE.Mesh(new THREE.TorusGeometry(1.35,.17,6,14,Math.PI),new THREE.MeshStandardMaterial({color:P.warn,roughness:.8,flatShading:true}));
  arm.add(claw);const rod=T.box(.28,5,.28,P.warn);rod.position.y=1.35+2.5;arm.add(rod);
  const armTag=k.label("REVERT","warn",claw,[-2.3,.2,0]);
  const ARM_UP=new THREE.Vector3(LX-3.4,4.9,0),ARM_DOWN=new THREE.Vector3(LX,red.home-.05,0);
  /* right: crane, cable, monolith */
  add(T.box(.45,7.4,.45,P.warn),RX+3.2,3.7);
  add(T.box(5.4,.35,.45,P.warn),RX+1.1,7.25);
  add(T.box(.9,.6,.9,P.dk),RX+3.2,7.75);
  const cable=add(T.box(.07,1,.07,P.ink),RX,6.5);
  const MH=3.1,HANG=6.95-.9-MH/2,LAND=.3+MH/2;
  const mono=add(T.box(2.8,MH,1.8,0x8d8c86),RX,HANG);
  const yrs=k.label("ONE BIG DROP","",mono,[0,MH/2+.15,0]);
  const noT=k.label("NO TICKS","err",mono,[0,MH/2+.15,0]);noT.el.style.opacity=0;
  const dust=[...Array(8)].map((_,i)=>{const d=add(T.box(.3,.3,.3,0xbdbbb2),RX,.3);d.visible=false;d.a=i/8*Math.PI*2;return d});
  const leftTag=k.label("SMALL. CHECKED. UNDOABLE.","ok",null);
  const rightTag=k.label("ONE DROP. NO TICKS.","err",null);
  leftTag.obj=new THREE.Object3D();leftTag.obj.position.set(LX,-.9,1.2);k.scene.add(leftTag.obj);
  rightTag.obj=new THREE.Object3D();rightTag.obj.position.set(RX,-.9,1.2);k.scene.add(rightTag.obj);
  rightTag.el.style.opacity=0;
  const seg=(s,a,b)=>Math.min(1,Math.max(0,(s-a)/(b-a)));
  let s=0,target=0;
  /* land brick: falls from above with an ease-in, tiny settle */
  function landY(home,u){const e=u*u;return home+(1-e)*7}
  k.loop(dt=>{
    s=H.reduced?target+1:Math.min(target+1,s+dt*.95);
    // step 0: four bricks, staggered
    for(let i=0;i<N;i++){const u=seg(s,i*.2,i*.2+.18),b=bricks[i];
      b.m.position.y=landY(b.home,u);b.tag.el.style.opacity=u>=1?"1":"0";}
    // step 1: red brick lands, lights red, arm grips and lifts it away
    const ur=seg(s,1,1.22),down=seg(s,1.3,1.55),lift=seg(s,1.6,1.95);
    const ap=ARM_UP.clone().lerp(ARM_DOWN,T.ease(down));
    if(lift>0)ap.copy(ARM_DOWN).lerp(ARM_UP,T.ease(lift));
    arm.position.copy(ap);arm.rotation.z=lift>0?T.ease(lift)*.3:(1-T.ease(down))*.3;
    if(lift>0)red.m.position.set(ap.x,ap.y+.05,0);else red.m.position.set(LX,landY(red.home,ur),0);
    red.m.rotation.z=arm.rotation.z*(lift>0?1:0);
    const lit=ur>=1;red.m.material.color.setHex(lit?P.err:0x9b9a93);
    red.tag.el.style.opacity=lit&&lift<.6?"1":"0";
    armTag.el.style.opacity=s>=1?"1":"0";
    leftTag.el.style.opacity=String(seg(s,1.9,2));
    // step 2: the monolith drops whole
    const f=seg(s,2,2.38),e=f*f;
    mono.position.y=HANG+(LAND-HANG)*e;
    cable.position.y=f>0?6.95-.15:6.5;cable.scale.y=f>0?.3:1;
    const thud=seg(s,2.38,2.75);
    dust.forEach(d=>{d.visible=thud>0&&thud<1;const r=1.6+thud*1.8;d.position.set(RX+Math.cos(d.a)*r,.3+Math.sin(thud*Math.PI)*.9,Math.sin(d.a)*r*.5);d.scale.setScalar(1-thud*.7)});
    k.camera.position.y=4.6+(thud>0&&thud<.4?Math.sin(thud*60)*.06:0);
    yrs.el.style.opacity=f>0?"0":"1";
    noT.el.style.opacity=String(seg(s,2.5,2.7));rightTag.el.style.opacity=String(seg(s,2.6,2.8));
  });
  return {step(n){target=n;s=Math.max(Math.min(s,n+1),n)},stop(){k.stop()}};
};
