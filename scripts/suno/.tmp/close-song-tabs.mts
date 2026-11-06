import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://localhost:9222')
for (const p of b.contexts()[0].pages()) if (/suno\.com\/song\//.test(p.url())) { console.log('closing', p.url()); await p.close() }
console.log(b.contexts()[0].pages().map(p => p.url()))
process.exit(0)
