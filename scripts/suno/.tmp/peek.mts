import { connect } from '../suno.mts'
const { browser, page } = await connect()
await page.screenshot({ path: process.argv[2] })
const info = await page.evaluate(() => ({ clerk: typeof (window as any).Clerk, keys: Object.keys(window).filter(k=>/clerk|suno|auth/i.test(k)).slice(0,20), cookies: document.cookie.split(';').map(c=>c.split('=')[0].trim()).filter(n=>/session|clerk|client/i.test(n)) }))
console.log(JSON.stringify(info))
await browser.close()
