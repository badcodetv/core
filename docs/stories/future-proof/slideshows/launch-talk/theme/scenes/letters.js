/* Slide 27: "Same letter, one extra line: 67.5% -> 79% paid." (HMRC, overdue tax)
   step 0: one envelope splits into two and they fan out: PLAIN LETTER / + POSTCODE LINE
           (the second one carries a yellow extra line).
   step 1: the envelopes drop to the floor and two bars rise behind them together,
           to 67.5% and 79%; the tall bar gets the tag about the postcode. */
THEME.scenes.letters=function(mount,slide,H){
  const T=THEME.three,P=THEME.palette;
  const k=T.setup(mount,{cam:[0,2.6,11.5],look:[0,1.75,0],fov:34});
  const vals=slide.values||[67.5,79],FULL=4.2,X=[-2.1,2.1];
  const floor=T.box(9,.24,3,P.win);floor.position.set(0,-.12,0);k.scene.add(floor);
  function tag(text,cls,obj,off){const l=k.label(text,cls,obj,off);l.el.style.opacity=0;return l}
  const bars=vals.map((v,i)=>{const m=T.box(1.9,1,1.3,i?P.ok:0x8b8a83);m.position.set(X[i],0,-.3);k.scene.add(m);
    const lab=tag(v+"%",i?"ok":"",m,[0,.2,0]);lab.el.style.fontSize="36px";lab.el.style.padding="8px 12px";return {m,h:FULL*v/100,lab}});
  const note=tag("MOST IN YOUR POSTCODE PAID","warn",bars[1].m,[0,1.05,0]);
  function envelope(extra){const g=new THREE.Group();
    const body=T.box(2.4,1.5,.1,0xf4f1e6);g.add(body);
    [-1,1].forEach(s=>{const f=T.box(1.45,.07,.04,P.dk);f.position.set(s*.6,.38,.07);f.rotation.z=-s*.55;g.add(f)});
    const addr=T.box(.9,.08,.03,0x9b9a93);addr.position.set(0,-.25,.07);g.add(addr);
    const addr2=T.box(.7,.08,.03,0x9b9a93);addr2.position.set(-.1,-.42,.07);g.add(addr2);
    if(extra){const l=T.box(1.6,.14,.03,P.warn);l.position.set(0,-.6,.07);g.add(l)}
    k.scene.add(g);return g}
  const env=[envelope(false),envelope(true)];
  const envLab=[tag("PLAIN LETTER","",env[0],[0,1.0,0]),tag("+ POSTCODE LINE","warn",env[1],[0,1.0,0])];
  let target=0,t=-1;
  k.loop(dt=>{t=H.reduced?target:T.damp(t,target,2.8,dt);
    const fan=T.ease((t+.85)/.75),rise=T.ease(t),drop=T.ease(t*1.4);
    env.forEach((g,i)=>{const s=i?1:-1;
      const fx=s*.15+(X[i]-s*.15)*fan,fy=1.9,fr=s*-.18*fan;
      g.position.set(fx,fy+(.42-fy)*drop,.4+(1.25-.4)*drop);
      g.rotation.set(-.35*drop,0,fr*(1-drop));
      g.scale.setScalar(1-.45*drop);
      envLab[i].el.style.opacity=String(fan>.9&&drop<.2?1:0);});
    bars.forEach((b,i)=>{const h=Math.max(.001,b.h*rise);b.m.visible=rise>.01;b.m.scale.y=h;b.m.position.y=h/2;
      b.lab.off.y=h/2+.2;b.lab.el.style.opacity=String(rise>.05?1:0);
      b.lab.el.textContent=(Math.round(vals[i]*rise*10)/10).toFixed(vals[i]%1?1:0)+"%";});
    note.off.y=bars[1].h*rise/2+1.0;note.el.style.opacity=String(rise>.95?1:0);
  });
  return {step(n){target=n},stop(){k.stop()}};
};
