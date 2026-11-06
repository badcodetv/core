import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://localhost:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
console.log(p.url())
console.log('edit vocals btn', await p.locator('button:has-text("Edit vocals")').count())
console.log(JSON.stringify(await p.evaluate(()=>[...document.querySelectorAll('[role="slider"]')].map(s=>[s.getAttribute('aria-label'),s.getAttribute('aria-valuemin'),s.getAttribute('aria-valuemax'),s.getAttribute('aria-valuenow'),s.getAttribute('aria-valuetext')]))))
process.exit(0)
