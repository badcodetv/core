/* Shared 3D helpers for this theme's diagram scenes (three.js r128, global THREE).
   A scene is THEME.scenes[name] = (mount, slide, H) => ({ step(n), stop() }).
   - mount: the .scene-mount div (position:relative). Put the canvas and any labels inside it.
   - step(n): called on every step change (0 .. slide.steps-1). Animate towards that state.
   - stop(): cancel the frame loop, dispose the renderer, remove listeners.
   Look: flat, low-poly, chunky, in the theme palette below; labels are HTML tags (.tag3d). */
(function(){
const P={desk:0x3b7f86,win:0xd4d3cc,dk:0x4e4d48,bar:0x1f3070,bar2:0x3c55a8,ok:0x2d9a4c,warn:0xffd43b,err:0xd22d2d,ink:0x141618,white:0xffffff,
  bricks:[0x2d9a4c,0xffd43b,0xd22d2d,0x3c55a8,0xe58a2e,0x8a6fd1]};
THEME.palette=P;
THEME.three={
  /* setup(mount,{bg,fov,cam:[x,y,z],look:[x,y,z]}) -> {renderer,scene,camera,render(),loop(fn),stop(),label(text,cls),place(label,vec3)} */
  setup(mount,o={}){
    const renderer=new THREE.WebGLRenderer({antialias:true});
    renderer.setPixelRatio(Math.min(2,window.devicePixelRatio||1));
    mount.appendChild(renderer.domElement);
    const scene=new THREE.Scene();scene.background=new THREE.Color(o.bg??P.desk);
    const camera=new THREE.PerspectiveCamera(o.fov||35,16/9,.1,200);
    camera.position.set(...(o.cam||[0,4,12]));const look=new THREE.Vector3(...(o.look||[0,1,0]));camera.lookAt(look);
    scene.add(new THREE.HemisphereLight(0xffffff,0x6a6a6a,.8));
    const sun=new THREE.DirectionalLight(0xffffff,.75);sun.position.set(5,10,7);scene.add(sun);
    const labels=[];
    function size(){const w=mount.clientWidth,h=mount.clientHeight;if(!w||!h)return;renderer.setSize(w,h,false);camera.aspect=w/h;camera.updateProjectionMatrix()}
    const ro=new ResizeObserver(size);ro.observe(mount);size();
    const v=new THREE.Vector3();
    function place(el,pos){v.copy(pos).project(camera);el.style.left=((v.x+1)/2*mount.clientWidth)+"px";el.style.top=((1-v.y)/2*mount.clientHeight)+"px";el.style.display=v.z>1?"none":""}
    function render(){labels.forEach(l=>l.obj&&place(l.el,l.obj.getWorldPosition(new THREE.Vector3()).add(l.off)));renderer.render(scene,camera)}
    let raf=0,last=performance.now(),fn=null;
    function tick(now){const dt=Math.min(.05,(now-last)/1000);last=now;if(fn)fn(dt,now/1000);render();raf=requestAnimationFrame(tick)}
    return {renderer,scene,camera,render,
      loop(f){fn=f;last=performance.now();raf=requestAnimationFrame(tick)},
      /* label(text,cls,obj,offset): an HTML tag that follows a 3D object */
      label(text,cls="",obj=null,off=[0,0,0]){const el=document.createElement("div");el.className="tag3d "+cls;el.textContent=text;mount.appendChild(el);const l={el,obj,off:new THREE.Vector3(...off)};labels.push(l);return l},
      stop(){cancelAnimationFrame(raf);ro.disconnect();renderer.dispose();scene.traverse(o=>{o.geometry&&o.geometry.dispose();o.material&&(Array.isArray(o.material)?o.material.forEach(m=>m.dispose()):o.material.dispose())});mount.innerHTML=""}};
  },
  box(w,h,d,color,o={}){return new THREE.Mesh(new THREE.BoxGeometry(w,h,d),new THREE.MeshStandardMaterial({color,roughness:o.rough??.85,flatShading:true}))},
  /* ease toward a target: x += (to-x)*k, frame-rate independent */
  damp(x,to,rate,dt){return x+(to-x)*(1-Math.exp(-rate*dt))},
  ease(x){x=Math.min(1,Math.max(0,x));return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2}
};
})();
