/* Slide 35: "A suggestion box with no wire."
   step 0: the street: a bright suggestion box, a plain DECISION building, a pipe from the box
           that stops short of the building (a gap), two gauges on the pipe (10,000 / 100,000), needles at rest.
   step 1: ideas drop into the box, the needles swing up, ideas spill out of the pipe end onto the
           pavement and pile up; "NO WIRE" lights over the gap. */
THEME.scenes.pipe=function(mount,slide,H){
  const T=THEME.three,P=THEME.palette;
  const k=T.setup(mount,{cam:[0,4.1,15.8],look:[.4,2.75,0],fov:30});
  const add=(m,x,y,z=0)=>{m.position.set(x,y,z);k.scene.add(m);return m};
  const mat=c=>new THREE.MeshStandardMaterial({color:c,roughness:.8,flatShading:true});
  add(T.box(26,.2,8,0x2f6a70),0,-.1,0);                 // road
  add(T.box(26,.24,3,0xb9b7ae),0,.12,.6);                // pavement
  /* suggestion box: bright, striped, on a post */
  const BX=-6.4,BY=2.3,PY=2.6,END=1.1,BLD=6.2;
  add(T.box(.35,1.4,.35,P.dk),BX,.9);
  add(T.box(2,1.8,1.6,P.bricks[4]),BX,BY);
  [P.bricks[0],P.bricks[1],P.bricks[3]].forEach((c,i)=>add(T.box(2.04,.22,1.64,c),BX,BY-.55+i*.55));
  add(T.box(1.1,.12,.5,P.ink),BX,BY+.92);                // slot
  k.label("YOUR IDEAS","warn",null).obj=add(new THREE.Object3D(),BX,BY+1.35);
  /* DECISION: big, plain, door shut */
  add(T.box(4.2,6,3,0xa9a8a1),BLD,3.1,-.6);
  add(T.box(1.2,2,.1,P.dk),BLD,1.15,.95);
  for(let r=0;r<3;r++)for(let c=0;c<3;c++)add(T.box(.7,.7,.1,0x7d7c76),BLD-1.3+c*1.3,2.9+r*1.15,.95);
  k.label("DECISION","",null).obj=add(new THREE.Object3D(),BLD,6.4,-.6);
  /* the pipe: box side → END, then nothing */
  const pipe=new THREE.Mesh(new THREE.CylinderGeometry(.32,.32,END-BX-1,10),mat(0x8a8f96));
  pipe.rotation.z=Math.PI/2;add(pipe,(BX+1+END)/2,PY);
  add(new THREE.Mesh(new THREE.CylinderGeometry(.4,.4,.25,10),mat(0x6d727a)),END,PY).rotation.z=Math.PI/2;
  [-4.3,-1.6,.6].forEach(x=>add(T.box(.18,PY-.2,.18,P.dk),x,(PY-.2)/2+.2));
  const gapTag=k.label("NO WIRE","err",null);gapTag.obj=add(new THREE.Object3D(),(END+BLD-2.1)/2,PY+.35);gapTag.el.style.opacity=0;
  /* gauges on top of the pipe */
  const gauges=[[-4.3,"10,000: A REPLY"],[-1.6,"100,000: CONSIDERED FOR DEBATE"]].map(([x,t],i)=>{
    add(T.box(.15,.5,.15,P.dk),x,PY+.5);
    const face=new THREE.Mesh(new THREE.CylinderGeometry(.62,.62,.16,16),mat(P.white));face.rotation.x=Math.PI/2;add(face,x,PY+1.35,.1);
    add(new THREE.Mesh(new THREE.TorusGeometry(.62,.07,5,16),mat(P.ink)),x,PY+1.35,.18);
    const n=new THREE.Group();add(n,x,PY+1.35,.24);const nd=T.box(.08,.5,.04,P.err);nd.position.y=.25;n.add(nd);
    const lab=k.label(t,"",null);lab.obj=add(new THREE.Object3D(),x+(i?1.1:0),PY+(i?2.95:2.15));
    return {n,lab};
  });
  /* ideas: a few in flight, a heap that grows on the pavement under the gap */
  const N=10,HEAP=34,HX=(END+BLD-2.1)/2+.1;
  const cube=c=>{const m=T.box(.34,.34,.34,c);m.visible=false;k.scene.add(m);return m};
  const fly=[...Array(N)].map((_,i)=>({m:cube(P.bricks[i%6]),o:i/N}));
  const heap=[...Array(HEAP)].map((_,i)=>{const m=cube(P.bricks[(i*5)%6]);
    const layer=i<16?0:i<26?1:i<32?2:3,ring=[16,10,6,2][layer],j=i-[0,16,26,32][layer],r=[1.15,.8,.45,.15][layer];
    const a=j/ring*Math.PI*2+layer;m.position.set(HX+Math.cos(a)*r*1.3,.41+layer*.3,.6+Math.sin(a)*r*.7);m.rotation.y=a*1.7;return m});
  let target=0,t=0,clock=0;
  k.loop(dt=>{
    t=H.reduced?target:T.damp(t,target,4,dt);
    const on=target>=1;clock=on?clock+dt:0;
    gauges.forEach((g,i)=>{g.n.rotation.z=1.1-t*(i?1.6:2.1)+(on&&!H.reduced?Math.sin(clock*9+i)*.05:0)});
    gapTag.el.style.opacity=String(T.ease((t-.4)*2));
    const shown=H.reduced?(on?HEAP:0):Math.min(HEAP,Math.floor(clock*16));
    heap.forEach((m,i)=>m.visible=i<shown);
    fly.forEach(f=>{const u=on&&!H.reduced?(clock*.8+f.o)%1:-1;f.m.visible=u>=0&&!(u>.32&&u<.62);
      if(u<0)return;
      if(u<=.32){const e=u/.32;f.m.position.set(BX+(f.o-.5)*.5,BY+3.4-e*2.4,.2)}           // posted into the box
      else{const e=(u-.62)/.38;f.m.position.set(END+.3+e*(HX-END+(f.o-.5)*1.4),PY-e*e*(PY-.6)+e*.4,.6*e)} // out of the end, onto the heap
      f.m.rotation.set(u*6,u*4,0);});
  });
  return {step(n){target=n;if(!n)clock=0},stop(){k.stop()}};
};
