// Builds the shared marketing board page from the repo: docs/marketing/chief-of-staff/board.md (+ the goal from plan.md §2).
// Usage: node scripts/marketing/build-board.mjs   → writes docs/marketing/chief-of-staff/board.html
// Then publish that file to https://claude.ai/artifact/3uuL8QzYF47wPCVyJVLNZ9 (the Artifact tool, same url).
// The page is read-only on purpose (Kai, 2026-10-15): decisions and changes are made by talking to Claude in the repo.
import { readFileSync, writeFileSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'
const dir = join(dirname(fileURLToPath(import.meta.url)), '../../docs/marketing/chief-of-staff')
const board = readFileSync(join(dir, 'board.md'), 'utf8')
const plan = readFileSync(join(dir, 'plan.md'), 'utf8')

const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
// inline markdown: `code`, **bold**, *em*, [text](url) — relative links become plain text (the repo is private)
const inline = s => esc(s)
  .replace(/`([^`]+)`/g, '<code>$1</code>')
  .replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>')
  .replace(/\*([^*]+)\*/g, '<em>$1</em>')
  .replace(/\[([^\]]+)\]\((https?:[^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>')
  .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '$1')
  .replace(/(^|[\s(])(https?:\/\/[^\s)<]+)/g, '$1<a href="$2" target="_blank" rel="noopener">$2</a>')

// split board.md into ## sections; each section → { title, paras: [], items: [] }
const sections = []
let updated = ''
for (const line of board.split('\n')) {
  if (line.startsWith('## ')) { sections.push({ title: line.slice(3).trim(), paras: [], items: [] }); continue }
  const s = sections[sections.length - 1]
  if (!s) { if (/^Updated /.test(line)) updated = line.trim(); continue }
  const li = line.match(/^\s*(?:\d+\.|-)\s+(.*)$/)
  if (li) s.items.push(li[1])
  else if (line.trim() && s.items.length && /^\s{2,}/.test(line)) s.items[s.items.length - 1] += ' ' + line.trim()
  else if (line.trim()) s.paras.push(line.trim())
}
const goal = (plan.match(/^> \*\*(.+?)\*\*/m) || [, 'Get finished work in front of people, keep it going out, and start a mailing list.'])[1]

// one item → { who, text, why } — "**Jack: open the accounts.** rest *Why: …*"
const split = item => {
  const m = item.match(/^\*\*(Kai or Jack|Kai|Jack|Claude|Both):\s*(.+?)\*\*\s*(.*)$/)
  let who = m ? m[1] : '', head = m ? cap(m[2]) : '', rest = m ? m[3] : item
  const why = (rest.match(/\*(Why[^*]+)\*/) || [])[1] || ''
  rest = rest.replace(/\*(Why[^*]+)\*/, '').trim().replace(/^[:.,]\s*/, '')
  return { who, head, rest, why }
}
const cap = s => s ? s[0].toUpperCase() + s.slice(1) : s
const whoTag = w => w ? `<span class="who ${w.split(' ')[0]}">${esc(w)}</span>` : ''

const render = {
  'Do next': s => `<div class="donext">${s.items.map((it, n) => { const x = split(it)
    return `<article class="dn${n ? '' : ' first'}"><div class="k"><span class="label">${n ? 'Then' : 'First'}</span>${whoTag(x.who)}</div>
      <div class="what">${inline(x.head || x.rest)}</div>${x.head && x.rest ? `<div class="more">${inline(x.rest)}</div>` : ''}${x.why ? `<div class="why">${inline(x.why)}</div>` : ''}</article>` }).join('')}</div>`,
  'Then': s => `<ol class="list" start="${4}">${s.items.map(it => { const x = split(it)
    return `<li><div>${x.head ? `<b>${inline(x.head)}</b> ${inline(x.rest)}` : inline(x.rest)}</div>${whoTag(x.who)}</li>` }).join('')}</ol>`,
  "What we're not doing, and should be": s => `<div class="gaps">${s.items.map(it => `<div class="gap">${inline(it)}</div>`).join('')}</div>`,
  'Waiting on you': s => `${s.paras.map(p => `<p class="lede">${inline(p)}</p>`).join('')}<div class="decs">${s.items.map(it => {
    const m = it.match(/^\*\*(.+?)\*\*\s*(.*)$/), q = m ? m[1] : it, rest = m ? m[2] : ''
    const who = (q.match(/^(Kai or Jack|Kai|Jack|Both):/) || [])[1] || ''
    return `<article class="dec">${whoTag(who)}<h3>${inline(cap(who ? q.slice(who.length + 1).trim() : q))}</h3>${rest ? `<p>${inline(rest)}</p>` : ''}</article>` }).join('')}</div>`,
  'Gone out': s => s.items.length ? `<ul class="out">${s.items.map(it => `<li>${inline(it)}</li>`).join('')}</ul>` : `<p class="empty">${inline(s.paras.join(' ') || 'Nothing yet.')}</p>`,
}
const heads = { 'Do next': 'do next', 'Then': 'then', "What we're not doing, and should be": "what we're not doing, and should be", 'Waiting on you': 'waiting on you', 'Gone out': "what's gone out" }
const body = sections.map(s => {
  const r = render[s.title] || (x => `${x.paras.map(p => `<p>${inline(p)}</p>`).join('')}${x.items.length ? `<ul>${x.items.map(i => `<li>${inline(i)}</li>`).join('')}</ul>` : ''}`)
  return `<section><h2>${esc(heads[s.title] || s.title.toLowerCase())}</h2>${r(s)}</section>`
}).join('\n')

// the logo's triangle (docs/brand, bench save b0dhojp15efdyw7rboj6)
const tri = (() => {
  const R = 100, w = 8, r = .36 * R, rc = .55 * r / 2, room = R - w / 2 - (r - rc) - R * .02, d = .61 * room, a = 55 * Math.PI / 180, x = d * Math.sin(a), y = -d * Math.cos(a), f = n => Math.round(n * 100) / 100
  const V = [0, 1, 2].map(k => { const t = (55 + k * 120) * Math.PI / 180; return [x + r * Math.sin(t), y - r * Math.cos(t)] }), q = rc / r, L = (A, B) => [A[0] + (B[0] - A[0]) * q, A[1] + (B[1] - A[1]) * q].map(f).join(' ')
  let p = ''; for (let k = 0; k < 3; k++) { const Vk = V[k], P = V[(k + 2) % 3], N = V[(k + 1) % 3]; p += `${k ? 'L' : 'M'}${L(Vk, P)}A${f(rc)} ${f(rc)} 0 0 1 ${L(Vk, N)}` }
  return p + 'Z'
})()

const html = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>BadCode Marketing Board</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700&family=Figtree:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap">
<style>
/* Generated by scripts/marketing/build-board.mjs from docs/marketing/chief-of-staff/board.md — do not edit by hand. Read-only by design. */
:root{--bg:#0d0e10;--panel:#16181b;--panel2:#1d2024;--line:#2a2e33;--fg:#ecebe8;--muted:#9a9a96;--faint:#5f625f;--red:#ff3b2f;--red-soft:rgba(255,59,47,.14);--warn:#f2b84b;
  --display:"Unbounded",ui-rounded,system-ui,sans-serif;--body:"Figtree",system-ui,-apple-system,"Segoe UI",sans-serif;--mono:"JetBrains Mono",ui-monospace,Menlo,Consolas,monospace;color-scheme:dark}
@media (prefers-color-scheme: light){:root:not([data-theme="dark"]){--bg:#f5f4f1;--panel:#fff;--panel2:#efeeea;--line:#dcdad4;--fg:#141517;--muted:#62645f;--faint:#9b9c96;--red:#e0261b;--red-soft:rgba(224,38,27,.10);--warn:#a86a00;color-scheme:light}}
:root[data-theme="light"]{--bg:#f5f4f1;--panel:#fff;--panel2:#efeeea;--line:#dcdad4;--fg:#141517;--muted:#62645f;--faint:#9b9c96;--red:#e0261b;--red-soft:rgba(224,38,27,.10);--warn:#a86a00;color-scheme:light}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 var(--body)}
.wrap{max-width:1040px;margin:0 auto;padding-block:28px 64px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:flex;flex-direction:column;gap:36px}
h1,h2,h3{margin:0;text-wrap:balance}
h2{font:700 13px/1.2 var(--display);letter-spacing:.08em;color:var(--muted);display:flex;align-items:center;gap:10px}
h2::before{content:"";border-left:5px solid transparent;border-right:5px solid transparent;border-bottom:9px solid var(--red)}
section{display:flex;flex-direction:column;gap:14px;min-width:0}
.label{font:600 11px/1.2 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--faint)}
code{font:13px var(--mono);background:var(--panel2);padding:1px 5px;border-radius:5px;overflow-wrap:anywhere}
a{color:inherit}
header{display:flex;flex-wrap:wrap;justify-content:space-between;gap:20px;align-items:flex-end}
.brand{display:flex;align-items:center;gap:14px}
.mark{width:40px;height:40px;flex:none}
.word{font:700 22px/1 var(--display);letter-spacing:-.01em}
.sub{font-size:13px;color:var(--muted);margin-top:4px}
.goal{max-width:500px}
.goal strong{display:block;font:500 18px/1.35 var(--display);margin-top:6px}
.donext{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:12px}
.dn{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px;display:flex;flex-direction:column;gap:8px;min-width:0}
.dn.first{border-color:var(--red);background:var(--red-soft)}
.k{display:flex;justify-content:space-between;align-items:center;gap:8px}
.what{font:600 18px/1.35 var(--body);overflow-wrap:anywhere}
.more{font-size:14px}
.why{font-size:13px;color:var(--muted)}
.who{font:600 11px var(--mono);letter-spacing:.06em;text-transform:uppercase;padding:3px 8px;border-radius:99px;border:1px solid var(--line);white-space:nowrap;align-self:start}
.who.Kai{color:var(--red);border-color:var(--red)}
.who.Jack{color:var(--warn);border-color:var(--warn)}
.who.Claude{color:var(--muted)}
ol.list{margin:0;padding:0;list-style:none;counter-reset:n 3;background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden}
ol.list li{counter-increment:n;display:grid;grid-template-columns:28px minmax(0,1fr) auto;gap:10px;padding:12px 16px;border-top:1px solid var(--line)}
ol.list li:first-child{border-top:0}
ol.list li::before{content:counter(n);font:600 12px var(--mono);color:var(--faint);padding-top:3px}
.gaps{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:10px}
.gap{background:var(--panel);border:1px dashed var(--line);border-radius:12px;padding:12px 14px;font-size:14px;color:var(--muted)}
.gap b{color:var(--fg);display:block;font-size:15px;margin-bottom:2px}
.lede{margin:0;color:var(--muted)}
.decs{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr));gap:12px}
.dec{background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--red);border-radius:12px;padding:16px;display:flex;flex-direction:column;gap:8px}
.dec h3{font:600 16px/1.35 var(--body)}
.dec p{margin:0;font-size:14px;color:var(--muted)}
.out{margin:0;padding-left:20px}
.empty{margin:0;color:var(--muted)}
.talk{background:var(--panel2);border:1px solid var(--line);border-radius:14px;padding:16px 18px;display:flex;flex-direction:column;gap:6px}
.talk b{font:600 15px var(--body)}
footer{font-size:13px;color:var(--faint);border-top:1px solid var(--line);padding-top:16px}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <div class="brand">
      <svg class="mark" viewBox="-100 -100 200 200" aria-hidden="true"><circle r="96" fill="none" stroke="currentColor" stroke-width="8"/><path d="${tri}" fill="#cc2b37"/></svg>
      <div><div class="word">badcode marketing</div><div class="sub">What to do next, in Claude's opinion</div></div>
    </div>
    <div class="goal"><span class="label">The goal</span><strong>${inline(goal)}</strong></div>
  </header>
${body}
  <div class="talk"><b>To change anything, tell Claude.</b><span>Open the repo in Claude Code and say <code>/chief-of-staff</code>, then what you've done, what you've decided, or what you'd change. Claude updates the plan in the repo and republishes this page. Nothing typed here is saved: this page is for reading.</span></div>
  <footer>${esc(updated || '')} · built from <code>docs/marketing/chief-of-staff/board.md</code></footer>
</div>
</body>
</html>
`
writeFileSync(join(dir, 'board.html'), html)
console.log(join(dir, 'board.html'))
