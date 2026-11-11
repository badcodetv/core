// Sponsor a Chancellor: the opening newspaper insert (Jack's timeline r1 note at 00:00:01:02: "have a newspaper insert
// here illustrating this, only have it on the screen for a bit"). Re-typed in our own lettering with "Outlet, Year"
// (no screenshot, no outlet logo), as Priority Lane. Headline VERBATIM from the ITV News article title and URL
// (itv.com/news/2024-03-22/chancellor-says-100000-salary-is-not-huge-in-his-surrey-constituency), seen in a search listing.
//   node scripts/shorts/sponsor_chancellor_cards.mjs <out-dir>
import sharp from 'sharp'
import { mkdirSync } from 'node:fs'

const OUT = process.argv[2]
mkdirSync(OUT, { recursive: true })
const C = { h: "Chancellor says £100,000 salary is ‘not huge’ in his Surrey constituency", src: 'ITV News, 2024', rot: -3 }
const W = 900, PAD = 48, FS = 66, LH = 76, CH = 22
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
const lines = []; let line = ''
for (const w of C.h.split(' ')) { if ((line + ' ' + w).trim().length > CH) { lines.push(line.trim()); line = w } else line += ' ' + w }
if (line.trim()) lines.push(line.trim())
const H = PAD * 2 + 70 + lines.length * LH + 60
const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}">
  <rect width="${W}" height="${H}" fill="#efebe1"/>
  <text x="${PAD}" y="${PAD + 30}" font-family="Liberation Serif" font-size="30" letter-spacing="6" fill="#444">NEWS · POLITICS</text>
  <rect x="${PAD}" y="${PAD + 48}" width="${W - PAD * 2}" height="4" fill="#222"/>
  ${lines.map((l, k) => `<text x="${PAD}" y="${PAD + 70 + FS + k * LH}" font-family="Liberation Serif" font-weight="700" font-size="${FS}" fill="#111">${esc(l)}</text>`).join('\n  ')}
  <text x="${PAD}" y="${PAD + 70 + lines.length * LH + 48}" font-family="Liberation Serif" font-style="italic" font-size="34" fill="#555">${esc(C.src)}</text>
</svg>`
const card = await sharp(Buffer.from(svg)).png().toBuffer()
const shadow = await sharp({ create: { width: W + 60, height: H + 60, channels: 4, background: { r: 0, g: 0, b: 0, alpha: 0 } } })
  .composite([{ input: await sharp({ create: { width: W, height: H, channels: 4, background: { r: 0, g: 0, b: 0, alpha: 0.6 } } }).png().toBuffer(), left: 38, top: 42 }])
  .blur(14).png().toBuffer()
const flat = await sharp(shadow).composite([{ input: card, left: 30, top: 30 }]).png().toBuffer()
await sharp(flat).rotate(C.rot, { background: { r: 0, g: 0, b: 0, alpha: 0 } }).png().toFile(`${OUT}/news-insert.png`)
console.log(JSON.stringify({ file: `${OUT}/news-insert.png`, src: C.src }))
