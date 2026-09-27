import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
const r = await p.evaluate(`(async () => {
  const tok = await window.Clerk?.session?.getToken()
  const h = { Authorization: 'Bearer ' + tok }
  const out = { hasTok: !!tok, pinEls: [...document.querySelectorAll('[aria-label*="in" i]')].map(e=>e.getAttribute('aria-label')).filter(a=>/pin/i.test(a)).slice(0,20) }
  for (const u of ['https://studio-api.prod.suno.com/api/project/a54391b0-9ad8-499f-b0d4-6de914bfd557?page=1',
                   'https://studio-api.prod.suno.com/api/project/a54391b0-9ad8-499f-b0d4-6de914bfd557/pinned-clips',
                   'https://studio-api.prod.suno.com/api/project/a54391b0-9ad8-499f-b0d4-6de914bfd557']) {
    try { const res = await fetch(u, { headers: h }); const t = await res.text(); out[u] = res.status + ' ' + t.slice(0, 1500) } catch (e) { out[u] = 'ERR ' + e }
  }
  return out
})()`)
console.log(JSON.stringify(r, null, 1))
await b.close()
