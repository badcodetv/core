/* Future Proof · "Update Available" layouts. Field reference: LAYOUTS.md beside this file.
   Every layout returns HTML for the 1600x900 stage. H = engine helpers {esc, t, slot, reduced}. */
(function(){
const L=THEME.layouts;
const S=(s,f)=>s.reveal&&s.reveal[f]!=null?` data-step="${s.reveal[f]}"`:"";   // reveal a field on step n
const task=(s,H)=>`<div class="task"><span class="start"><i></i>BRITAIN</span><span class="tab">${H.esc(s.task||s.title||"")}</span>${s.clockTo?`<span class="clock" data-until="${s.clockTo.step}">${H.esc(s.clock||"1872")}</span><span class="clock tick" data-step="${s.clockTo.step}">${H.esc(s.clockTo.text)}</span>`:`<span class="clock">${H.esc(s.clock||"1872")}</span>`}</div>`;
const caps=(s,H)=>(s.top?`<div class="cap top${s.top.length>70?" sm":""}"${S(s,"top")}>${H.t(s.top)}</div>`:"")+(s.bottom?`<div class="cap bottom${s.bottom.length>70?" sm":""}"${S(s,"bottom")}>${H.t(s.bottom)}</div>`:"");
const win=(H,{title,x,y,w,h,body,buttons,cls="",attr="",battr=""})=>`<div class="win ${cls}" style="left:${x}px;top:${y}px;width:${w}px;${h?`height:${h}px`:""}"${attr}><div class="tb"><span>${H.esc(title||"")}</span><span class="x"><span>_</span><span>□</span><span>×</span></span></div><div class="wb">${body||""}</div>${buttons&&buttons.length?`<div class="btns"${battr}>${buttons.map((b,i)=>{const off=b.startsWith("~"),gone=b.startsWith("~~");return `<span class="btn${i===0?" def":""}${off?" off":""}${gone?" gone":""}">${H.esc(b.replace(/^~+/,""))}</span>`}).join("")}</div>`:""}</div>`;
const icon=k=>k?`<div class="ico ${k}">${{error:"×",warn:"!",question:"?",ok:"✓",info:"i"}[k]||"i"}</div>`:"";
const prog=(p,H)=>{if(!p)return"";return `<div class="prog${p.err?" err":""}"><i style="width:${Math.max(3,Math.min(100,p.pct||0))}%"></i></div>${p.label?`<div class="plabel">${H.t(p.label)}</div>`:""}`};
const sticky=(s,H)=>s.sticky?`<div class="sticky" style="right:70px;top:${s.top?190:80}px;max-width:420px"${S(s,"sticky")}>${H.t(s.sticky)}</div>`:"";
const frame=(s,H,inner)=>`<div class="desk${s.dark?" dark":""}"></div>${inner}${sticky(s,H)}${caps(s,H)}${task(s,H)}`;
const box=s=>{const top=s.top?(s.top.length>70?200:170):70,bot=s.bottom?(s.bottom.length>70?250:220):90;return {y:top,h:900-top-bot}};

L.dialog=(s,H)=>{const b=box(s),w=s.w||(s.image?1360:1120),x=(1600-w)/2;
  const text=`<div class="row">${icon(s.icon)}<div style="display:flex;flex-direction:column;gap:16px;min-width:0">${s.heading?`<h3>${H.t(s.heading)}</h3>`:""}${s.text?`<div${S(s,"text")}>${H.t(s.text)}</div>`:""}${s.small?`<div class="small">${H.t(s.small)}</div>`:""}</div></div>`;
  const body=s.image?`<div style="display:grid;grid-template-columns:1fr 1fr;gap:26px;height:100%;min-height:0"><div style="min-height:0">${H.slot(s.image)}</div><div style="display:flex;flex-direction:column;gap:18px">${text}${prog(s.progress,H)}</div></div>`:text+prog(s.progress,H);
  return frame(s,H,win(H,{title:s.title,x,y:b.y,w,h:s.image?b.h:null,body,buttons:s.buttons,attr:S(s,"window"),battr:S(s,"buttons")}))};

L.picture=(s,H)=>{const b=box(s),w=Math.round(b.h*1.55)+40,x=(1600-w)/2;
  const side=s.side?win(H,{title:s.side.title,x:Math.min(x+w-260,1600-660),y:b.y+b.h-260,w:620,body:`<div class="row">${icon(s.side.icon)}<div>${H.t(s.side.text||"")}</div></div>`,buttons:s.side.buttons,attr:S(s,"side")}):"";
  return frame(s,H,win(H,{title:s.title||(s.image&&s.image.file)||"picture.jpg",x,y:b.y,w,h:b.h,body:`<div style="flex:1;min-height:0;margin:-14px -18px">${H.slot(s.image)}</div>`})+side)};

L.split=(s,H)=>{const b=box(s),w=700,g=60,x0=(1600-2*w-g)/2;
  const pane=(p,x,f)=>p?win(H,{title:p.title,x,y:b.y,w,h:b.h,attr:S(s,f),body:`${p.label?`<div class="plab">${H.esc(p.label)}</div>`:""}${p.image?`<div style="flex:1;min-height:0">${H.slot(p.image)}</div>`:""}${p.heading?`<h3 style="font-size:44px">${H.t(p.heading)}</h3>`:""}${p.text?`<div>${H.t(p.text)}</div>`:""}${p.lines?`<div class="lines">${p.lines.map(l=>`<div>${Array.isArray(l)?`<span>${H.esc(l[0])}</span><span>${H.esc(l[1])}</span>`:`<span>${H.esc(l)}</span>`}</div>`).join("")}</div>`:""}`,buttons:p.buttons}):"";
  return frame(s,H,pane(s.left,x0,"left")+pane(s.right,x0+w+g,"right"))};

L.release=(s,H)=>{const b=box(s),w=s.image?1080:1180,x=s.image?60:(1600-w)/2;
  const pic=s.image?win(H,{title:s.image.file||"photo.jpg",x:1160,y:b.y+40,w:400,h:Math.min(520,b.h-40),body:`<div style="flex:1;min-height:0;margin:-14px -18px">${H.slot(s.image)}</div>`}):"";
  return frame(s,H,pic+win(H,{title:s.title||"Release notes",x,y:b.y,w,h:b.h,buttons:s.buttons,body:`${s.heading?`<h3>${H.t(s.heading)}</h3>`:""}<div class="lines">${(s.lines||[]).map((l,i)=>`<div${s.reveal&&s.reveal.lines!=null?` data-step="${s.reveal.lines+i}"`:""}>${Array.isArray(l)?`<span>${H.esc(l[0])}</span><span>${H.esc(l[1])}</span>`:`<span>${H.t(l)}</span>`}</div>`).join("")}</div>${s.footer?`<div class="small"${S(s,"footer")}>${H.t(s.footer)}</div>`:""}`}))};

L.ticket=(s,H)=>{const b=box(s),w=s.image?1400:1120,x=(1600-w)/2;
  const f=`<dl class="fields">${(s.fields||[]).map(([k,v])=>`<dt>${H.esc(k)}</dt><dd${k===s.highlight?S(s,"highlight"):""}>${k===s.highlight?`<span class="hl">${H.t(v)}</span>`:H.t(v)}</dd>`).join("")}</dl>`;
  const body=`${s.heading?`<h3>${H.t(s.heading)}</h3>`:""}${s.image?`<div style="display:grid;grid-template-columns:2fr 3fr;gap:26px;flex:1;min-height:0"><div style="min-height:0">${H.slot(s.image)}</div>${f}</div>`:f}`;
  return frame(s,H,win(H,{title:s.title||"Issue tracker",x,y:b.y,w,h:b.h,body,buttons:s.buttons}))};

L.list=(s,H)=>{const b=box(s),w=s.image?1400:900,x=(1600-w)/2;
  const lines=`<div class="lines">${s.heading?`<div style="justify-content:center;font-weight:700">${H.t(s.heading)}</div>`:""}${(s.rows||[]).map(r=>`<div><span>${H.esc(r[0])}</span><span>${H.esc(r[1]??"")}</span></div>`).join("")}${s.total?`<div class="tot"${S(s,"total")}><span>${H.esc(s.total[0])}</span><span>${H.esc(s.total[1]??"")}</span></div>`:""}${s.footer?`<div style="display:block;text-align:center;margin-top:10px"${S(s,"footer")}>${H.t(s.footer)}</div>`:""}</div>`;
  const body=s.image?`<div style="display:grid;grid-template-columns:1fr 1fr;gap:26px;flex:1;min-height:0"><div style="min-height:0">${H.slot(s.image)}</div>${lines}</div>`:lines;
  return frame(s,H,win(H,{title:s.title||"Order summary",x,y:b.y,w,h:b.h,body,buttons:s.buttons}))};

L.toasts=(s,H)=>{const ts=s.toasts||[];
  const wall=s.wall?`<div class="wall">${H.t(s.wall.heading||"")}${s.wall.small?`<small>${H.t(s.wall.small)}</small>`:""}</div>`:"";
  const img=s.image?win(H,{title:s.image.file||"photo.jpg",x:80,y:s.wall?430:90,w:720,h:s.wall?380:720,body:`<div style="flex:1;min-height:0;margin:-14px -18px">${H.slot(s.image)}</div>`}):"";
  const gap=Math.min(190,Math.floor(680/Math.max(1,ts.length)));
  return frame(s,H,wall+img+ts.map((x,i)=>`<div class="toast" style="bottom:${80+(ts.length-1-i)*gap}px"${s.reveal?` data-step="${i}"`:""}><div class="tb"><span>${H.esc(x.title||"Notification")}</span><span class="x"><span>×</span></span></div><div class="wb">${H.t(x.text||"")}</div></div>`).join(""))};

L.title=(s,H)=>`<div class="boot"><h1>${H.t(s.heading||"")}</h1>${s.sub?`<p${S(s,"sub")}>${H.t(s.sub)}</p>`:""}${s.progress?`<div class="prog"><i style="width:${Math.max(3,Math.min(100,s.progress.pct||0))}%"></i></div>${s.progress.label?`<p style="font-size:26px">${H.t(s.progress.label)}</p>`:""}`:""}${s.image?`<div style="width:280px;height:280px;position:absolute;right:60px;bottom:60px">${H.slot(s.image)}</div>`:""}</div>`;

L.link=(s,H)=>{const img=s.image?win(H,{title:s.image.file||"photo.jpg",x:90,y:110,w:760,h:600,body:`<div style="flex:1;min-height:0;margin:-14px -18px">${H.slot(s.image)}</div>`}):"";
  return frame(s,H,`<div class="icon" style="left:1430px;top:700px"><i>${H.esc((s.name||"?")[0])}</i><span>${H.esc(s.name||"")}</span></div>`+img+win(H,{title:"Open web page?",x:s.image?700:300,y:s.image?330:220,w:820,buttons:["Open","Remind me in 5 years"],body:`<div class="row">${icon("question")}<div style="display:flex;flex-direction:column;gap:10px;min-width:0"><h3 style="font-size:46px">${H.esc(s.name||"")}</h3><div style="font:400 30px var(--mono);overflow-wrap:anywhere">${H.esc(s.url||"")}</div>${s.line?`<div>${H.t(s.line)}</div>`:""}</div></div>`})+(s.n?`<div class="sticky" style="right:60px;top:60px">${H.esc(s.n)}</div>`:""))};

L.card=(s,H)=>{const b=box(s),w=1000,x=s.image?120:(1600-w)/2;
  return frame(s,H,win(H,{title:s.title||"Tip of the day",x,y:b.y,w,buttons:s.buttons||["Close"],body:`<div class="row">${icon(s.icon||"info")}<div style="display:flex;flex-direction:column;gap:22px">${s.heading?`<h3>${H.t(s.heading)}</h3>`:""}${(s.lines||[]).map((l,i)=>`<div style="font:700 52px/1.1 var(--sans)" data-step="${i}">${H.t(l)}</div>`).join("")}</div></div>`})+(s.image?`<div style="position:absolute;right:60px;bottom:80px;width:300px;height:300px">${H.slot(s.image)}</div>`:""))};

L.fatal=(s,H)=>`<div class="fatal"><div class="hd">${H.esc(s.code||"BRITAIN")}</div><div class="big">${H.t(s.big||"")}</div>${s.text?`<div${S(s,"text")}>${H.t(s.text)}</div>`:""}${s.footer?`<div style="margin-top:auto"${S(s,"footer")}>${H.t(s.footer)}</div>`:""}</div>`;

L.diagram=(s,H)=>{const w=1460,x=70;
  return frame(s,H,win(H,{title:s.title||"diagram.exe",x,y:30,w,h:790,body:`${s.caption?`<div class="dcap">${H.t(s.caption)}</div>`:""}<div class="scene-mount"></div>${s.small?`<div class="dsmall">${H.t(s.small)}</div>`:""}`}))};

L.fallback=(s,H)=>frame(s,H,win(H,{title:"slide "+s.id,x:200,y:100,w:1200,body:`<h3>${H.t(s.onscreen||"")}</h3><div class="small">${H.t(s.visual||"")}</div>`}));
})();
