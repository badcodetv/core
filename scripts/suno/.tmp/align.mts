import { connect } from '../suno.mts'
import { writeFileSync } from 'node:fs'
const id = process.argv[2]
const { browser, page } = await connect()
const out = await page.evaluate(async (id) => {
  const tok = (await (window as any).Clerk?.session?.getToken?.()) || (document.cookie.split('; ').find(c=>c.startsWith('__session='))||'').slice(10)
  if (!tok) return { error: 'no token (not signed in?)', url: location.href }
  const r = await fetch(`https://studio-api.prod.suno.com/api/gen/${id}/aligned_lyrics/v2/`, { headers: { Authorization: `Bearer ${tok}` } })
  if (!r.ok) return { status: r.status }
  return await r.json()
}, id)
writeFileSync(process.argv[3], JSON.stringify(out))
console.log(Object.keys(out), (out as any).aligned_words?.length)
await browser.close()
