/* Appendix A6: "Tokens, not just votes" (quadratic voting).
   step 0: one voter's 100 tokens in a single pile in front of a row of bills ("ALL ON ONE?").
   step 1: the tokens fly out and spread across the bills; no stack holds more than a handful. */
THEME.scenes.tokens=function(mount,slide,H){
  const T=THEME.three,P=THEME.palette;
  const k=T.setup(mount,{cam:[0,8.5,19],look:[0,.7,.4],fov:25});
  const counts=slide.counts||[8,5,9,6,7,4,8,9,6,7,5,9,8,9];   /* sums to 100 */
  const n=counts.length,GAP=1.1,TH=.2;
  const bx=i=>(i-(n-1)/2)*GAP;
  /* the row of bills: paper sheets with printed lines, on a long desk */
  const desk=T.box(n*GAP+.8,.3,2.2,P.bar);desk.position.set(0,-.15,-1);k.scene.add(desk);
  for(let i=0;i<n;i++){
    const s=T.box(.9,.06,1.2,P.white);s.position.set(bx(i),.03,-1.1);k.scene.add(s);
    for(let j=0;j<3;j++){const l=T.box(j?.55:.7,.02,.07,j?0x9b9a93:P.ink);l.position.set(bx(i)-(j?.07:0),.07,-1.55+j*.18);k.scene.add(l)}
    const seal=T.box(.2,.03,.2,P.err);seal.position.set(bx(i)+.25,.07,-.65);k.scene.add(seal);
  }
  const wallet=T.box(3.4,.3,2,P.dk);wallet.position.set(0,-.15,2.6);k.scene.add(wallet);
  /* 100 tokens, one shared geometry and material */
  const geo=new THREE.CylinderGeometry(.34,.34,TH*.9,10);
  const mat=new THREE.MeshStandardMaterial({color:P.warn,roughness:.6,flatShading:true});
  const tokens=[];let id=0;
  counts.forEach((c,b)=>{for(let h=0;h<c;h++){
    const m=new THREE.Mesh(geo,mat);k.scene.add(m);
    const g=id++,gx=g%5,gz=Math.floor(g/5)%4,gy=Math.floor(g/20);
    const pile=new THREE.Vector3(-1.2+gx*.6,TH/2+gy*TH,2.05+gz*.37);
    const bill=new THREE.Vector3(bx(b),.06+TH/2+h*TH,-1.1);
    tokens.push({m,pile,bill,delay:(b/n)*.4+h*.01});
  }});
  const pileAnchor=new THREE.Object3D();pileAnchor.position.set(0,1.3,2.6);k.scene.add(pileAnchor);
  const top=counts.indexOf(Math.max(...counts));
  const highAnchor=new THREE.Object3D();highAnchor.position.set(bx(top),.06+counts[top]*TH+.35,-1.1);k.scene.add(highAnchor);
  const hundred=k.label("100 TOKENS","warn",pileAnchor,[2.9,-.6,0]);
  const q=k.label("ALL ON ONE?","err",pileAnchor,[-2.9,-.6,0]);
  const bills=k.label(n+" BILLS","",desk,[-n*GAP/2+1.2,-.3,1.2]);
  const spread=k.label("A HANDFUL EACH","ok",highAnchor,[0,.2,0]);
  let target=0,t=0;
  k.loop(dt=>{t=H.reduced?target:T.damp(t,target,3.6,dt);
    tokens.forEach(o=>{const a=T.ease((t-o.delay)/.5);
      o.m.position.copy(o.pile).lerp(o.bill,a);o.m.position.y+=Math.sin(Math.PI*a)*2.2;
      o.m.rotation.x=a>.98?0:Math.sin(Math.PI*a)*1.2;});
    const f=T.ease(t*1.8),g=T.ease((t-.7)/.3);
    hundred.el.style.opacity=q.el.style.opacity=String(1-f);
    spread.el.style.opacity=String(g);
  });
  return {step(s){target=s},stop(){k.stop()}};
};
