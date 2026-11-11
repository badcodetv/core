// Priority Lane end-card headlines (2026-11-11, Jack's note: "real life news stories flash on screen in like a meme format").
// Re-typed in our own lettering with "Outlet, Year" (no screenshots, no outlet logos: research/news-stories.md, CDPA s.30).
// Every headline is VERBATIM and was fetched from the article page itself (see research/news-stories.md).
//   node scripts/shorts/priority_lane_cards.mjs <out-dir>
import sharp from 'sharp'
import { mkdirSync } from 'node:fs'

const OUT = process.argv[2]
mkdirSync(OUT, { recursive: true })
export const CARDS = [
  { h: "After viral video, Selangor police clarify priority given to VIP's convoy over ambulance to avoid accidents", src: 'Malay Mail, 2021', rot: -4 },
  { h: 'Ambulance carrying heart attack patient in Kolkata kept waiting for Mamata Banerjee’s convoy', src: 'The News Minute, 2015', rot: 3 },
  { h: 'Investigation Into Moscow Policeman Who Stopped Ambulance for Government Motorcade', src: 'The Moscow Times, 2016', rot: -2 },
  { h: 'Ambulance stuck, this time for Dr G Parameshwar’s convoy', src: 'Deccan Chronicle, 2017', rot: 5 },
  { h: 'Himanta apologises to patient after ambulance stopped to let his convoy pass; 4 policemen suspended', src: 'Daily Excelsior, 2026', rot: -3 },
  { h: 'Social media fumes over \u201cbroken Britain\u201d as police motorcade stops ambulance on blue light emergency to allow VIP to pass through junction', src: 'Deadline News, 2024', rot: 2 },  // UK, LAST so it lands on top and holds; headline from search listing = URL slug, page not opened (403)
]
const W = 880, PAD = 44, FS = 52, LH = 62, CH = 25
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
function wrap(t) {
  const out = []; let line = ''
  for (const w of t.split(' ')) { if ((line + ' ' + w).trim().length > CH) { out.push(line.trim()); line = w } else line += ' ' + w }
  if (line.trim()) out.push(line.trim()); return out
}
for (const [i, c] of CARDS.entries()) {
  const lines = wrap(c.h), H = PAD * 2 + lines.length * LH + 56
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}">
  <rect width="${W}" height="${H}" rx="14" fill="#fbfaf7"/>
  <rect x="0" y="0" width="14" height="${H}" fill="#cc2b37"/>
  ${lines.map((l, k) => `<text x="${PAD + 14}" y="${PAD + FS + k * LH}" font-family="Liberation Sans" font-weight="700" font-size="${FS}" fill="#111">${esc(l)}</text>`).join('\n  ')}
  <text x="${PAD + 14}" y="${PAD + lines.length * LH + 42}" font-family="Liberation Sans" font-size="32" fill="#666">${esc(c.src)}</text>
</svg>`
  const card = await sharp(Buffer.from(svg)).png().toBuffer()
  // drop shadow, then the meme tilt; transparent padding so ffmpeg can overlay it as-is
  const shadow = await sharp({ create: { width: W + 60, height: H + 60, channels: 4, background: { r: 0, g: 0, b: 0, alpha: 0 } } })
    .composite([{ input: await sharp({ create: { width: W, height: H, channels: 4, background: { r: 0, g: 0, b: 0, alpha: 0.55 } } }).png().toBuffer(), left: 38, top: 42 }])
    .blur(12).png().toBuffer()
  const flat = await sharp(shadow).composite([{ input: card, left: 30, top: 30 }]).png().toBuffer()  // sharp rotates BEFORE composite in one pipeline
  await sharp(flat)
    .rotate(c.rot, { background: { r: 0, g: 0, b: 0, alpha: 0 } }).png().toFile(`${OUT}/card-${i}.png`)
}
console.log(JSON.stringify(CARDS.map((c, i) => ({ i, src: c.src, file: `${OUT}/card-${i}.png` }))))
