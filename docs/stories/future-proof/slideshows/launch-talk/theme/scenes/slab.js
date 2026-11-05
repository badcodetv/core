/* Slide 11: "A party is a slab. An issue is a brick."
   step 0: one grey slab labelled PARTY. step 1: it cracks into six labelled bricks.
   step 2: Mel's picks are lifted one at a time onto a plain base on the right. */
THEME.scenes.slab=function(mount,slide,H){
  const T=THEME.three,P=THEME.palette;
  const k=T.setup(mount,{cam:[0,4.6,12.5],look:[0,1.1,0],fov:34});
  const names=(slide.bricks||["Buses","Bins","Bills","Housing","Schools","Water"]);
  const picks=slide.picks||[0,1,3];
  const base=T.box(5.6,.3,2,P.win);base.position.set(4.5,-.15,0);k.scene.add(base);
  const plinth=T.box(6.2,.3,2.4,P.bar);plinth.position.set(-2.4,-.15,0);k.scene.add(plinth);
  const bricks=names.map((n,i)=>{const c=i%3,r=Math.floor(i/3);
    const m=T.box(1.6,.9,1.6,0x9b9a93);k.scene.add(m);
    const home=new THREE.Vector3(-2.4+(c-1)*1.6,.45+r*.9,0);
    const crack=new THREE.Vector3(-2.4+(c-1)*2.05,.55+r*1.35,(r?-.3:.3));
    const pi=picks.indexOf(i);const pick=pi<0?null:new THREE.Vector3(4.5+(pi-1)*1.75,.45,0);
    m.position.copy(home);
    const lab=k.label(n.toUpperCase(),"",m,[0,.75,0]);lab.el.style.opacity=0;
    return {m,home,crack,pick,lab,col:new THREE.Color(P.bricks[i%P.bricks.length]),grey:new THREE.Color(0x9b9a93),delay:i*.06};
  });
  const party=k.label("PARTY","err",bricks[4].m,[0,1.0,0]);
  let target=0,t=0;
  k.loop(dt=>{t=H.reduced?target:T.damp(t,target,3.2,dt);
    bricks.forEach(b=>{const a=T.ease(Math.min(1,t)*1.25-b.delay),c=T.ease((t-1)*1.6-b.delay*3);
      const p=b.home.clone().lerp(b.crack,a);if(b.pick&&t>1)p.lerp(b.pick,c);
      b.m.position.copy(p);b.m.rotation.y=(b.delay-.15)*a*1.4*(1-(b.pick?c:0));
      b.m.material.color.copy(b.grey).lerp(b.col,a);
      b.lab.el.style.opacity=String(a);});
    party.el.style.opacity=String(1-T.ease(t*1.6));
  });
  return {step(n){target=n},stop(){k.stop()}};
};
