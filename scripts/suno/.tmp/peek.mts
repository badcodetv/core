import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const pages = b.contexts().flatMap(c => c.pages())
for (const p of pages) console.log('TAB', p.url())
const p = pages.find(p => p.url().includes('suno.com'))
if (p) {
  await p.waitForTimeout(4000)
  console.log('NOW', p.url())
  await p.screenshot({ path: '/tmp/claude-1000/-home-jackt-projects-badcode-badcode/5fb6be40-425f-43b6-9aac-91f94e615d6f/scratchpad/suno.png' })
  console.log(await p.evaluate(() => (window as any).Clerk?.user?.primaryEmailAddress?.emailAddress ?? 'no-clerk-user'))
}
await b.close()
