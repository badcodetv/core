import { connect } from '../suno.mts'
const { browser, page } = await connect()
const wid = new URL(page.url()).searchParams.get('wid')
const out = await page.evaluate(async (wid) => {
  const tok = await (window as any).Clerk.session.getToken()
  const res: any[] = []
  for (let p = 1; p <= 3; p++) {
    const r = await fetch(`https://studio-api.prod.suno.com/api/project/${wid}?hide_disliked=false&page=${p}`, { headers: { Authorization: `Bearer ${tok}` } })
    if (!r.ok) return { status: r.status }
    const j = await r.json()
    const clips = j.project_clips ?? j.clips ?? []
    if (!clips.length) { if (p === 1) return { keys: Object.keys(j), name: j.name }; break }
    for (const c of clips) { const k = c.clip ?? c; res.push([k.title, k.metadata?.duration, k.id]) }
  }
  return res
}, wid)
console.log(wid, JSON.stringify(out))
await browser.close()
