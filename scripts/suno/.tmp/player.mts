import { chromium } from 'playwright'
const b = await chromium.connectOverCDP('http://127.0.0.1:9222')
const p = b.contexts()[0].pages().find(p => p.url().includes('suno.com'))!
console.log(await p.evaluate(`(()=>{const a=document.querySelector('audio');return a?{src:a.src.slice(0,30),t:a.currentTime,d:a.duration,paused:a.paused,muted:a.muted,vol:a.volume,rs:a.readyState,err:a.error&&a.error.code}:null})()`))
await b.close()
