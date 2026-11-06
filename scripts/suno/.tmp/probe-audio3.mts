import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://localhost:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
await p.getByText('Browse', { exact: true }).first().click()
await p.waitForTimeout(2500)
await p.screenshot({path:'/tmp/claude-1000/-home-jackt-projects-badcode-badcode/d9d776a5-228c-4281-8d71-39ccb4e66a6b/scratchpad/suno3.png'})
process.exit(0)
