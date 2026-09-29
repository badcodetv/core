// Direction sheet: napkin-quality sketches for choosing a direction. NOT finished design.
// Run from anywhere: node direction-sheet.mjs   (needs the repo's `sharp`)
import { createRequire } from 'node:module'
import { writeFileSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'
const here = dirname(fileURLToPath(import.meta.url))
const require = createRequire(join(here, '../../../../package.json'))
const sharp = require('sharp')

const LAMP = '#e6291c', INK = '#eef3f6', BG = '#050607', DIM = '#59626b', GOLD = '#e8c98a', ACID = '#BADC0D'
const C = 480, CAP = 64, HEAD = 96, cols = 4
const cells = []
const cell = (title, note, body, bg = BG) => cells.push({ title, note, body, bg })
const CAPS = 'Liberation Sans Narrow'

function capsMark(cx, y, size, tracking = 1, ink = INK) {
  const capH = 0.72, d = size * capH
  return { cx, cy: y - size * capH / 2, svg:
    `<text x="${cx - d / 2 - size * 0.07}" y="${y}" text-anchor="end" font-family="${CAPS}" font-weight="700" font-size="${size}" letter-spacing="${tracking}" fill="${ink}">BADC</text>` +
    `<circle cx="${cx}" cy="${y - size * capH / 2}" r="${d / 2}" fill="${LAMP}"/>` +
    `<text x="${cx + d / 2 + size * 0.07}" y="${y}" text-anchor="start" font-family="${CAPS}" font-weight="700" font-size="${size}" letter-spacing="${tracking}" fill="${ink}">DE</text>` }
}
function ring(cx, cy, r, w, ink = INK) { return `<circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="${ink}" stroke-width="${w}"/>` }
function roundWord(x0, base, r, w) {
  const step = 2 * r + w + r * 0.42, cy = base - r, top = base - 2 * r * 1.55, L = []
  const stem = (x, y1, y2) => `<line x1="${x}" y1="${y1}" x2="${x}" y2="${y2}" stroke="${INK}" stroke-width="${w}"/>`
  const arc = (cx, a1, a2) => { const p = a => [cx + r * Math.cos(a * Math.PI / 180), cy + r * Math.sin(a * Math.PI / 180)]; const [x1, y1] = p(a1), [x2, y2] = p(a2); return `<path d="M${x1} ${y1} A${r} ${r} 0 1 1 ${x2} ${y2}" fill="none" stroke="${INK}" stroke-width="${w}"/>` }
  let oCx = 0
  'badcode'.split('').forEach((ch, i) => {
    const cx = x0 + r + w / 2 + i * step
    if (ch === 'b') L.push(ring(cx, cy, r, w), stem(cx - r, top, base + w / 2))
    if (ch === 'a') L.push(ring(cx, cy, r, w), stem(cx + r, cy - r - w / 2, base + w / 2))
    if (ch === 'd') L.push(ring(cx, cy, r, w), stem(cx + r, top, base + w / 2))
    if (ch === 'c') L.push(arc(cx, 42, -42))
    if (ch === 'e') L.push(arc(cx, 38, 0), `<line x1="${cx - r}" y1="${cy}" x2="${cx + r + w / 2}" y2="${cy}" stroke="${INK}" stroke-width="${w}"/>`)
    if (ch === 'o') { oCx = cx; L.push(`<circle cx="${cx}" cy="${cy}" r="${r + w / 2}" fill="${LAMP}"/>`) }
  })
  return { svg: L.join(''), oCx, cy, width: 7 * step - r * 0.42 }
}
function lampBadge(size) {
  const s = size / 100
  return `<g transform="scale(${s})"><circle cx="50" cy="50" r="50" fill="#000"/><rect x="${50 - 2.6}" y="0" width="5.2" height="60" fill="${INK}"/><circle cx="50" cy="62" r="10.5" fill="${LAMP}"/></g>`
}

// ---------- ROW 1: the recommended direction
cell('A · THE MARK', 'A line from the top edge, ending in one red lamp.',
  `<line x1="240" y1="0" x2="240" y2="292" stroke="${INK}" stroke-width="3.2"/><circle cx="240" cy="318" r="29" fill="${LAMP}"/>`)
{ const m = capsMark(286, 372, 84, 1)
  cell('A · THE NAME', 'One rule: the O is the lamp. The line lands in it.',
    `<line x1="${m.cx}" y1="0" x2="${m.cx}" y2="${m.cy}" stroke="${INK}" stroke-width="3.2"/>${m.svg}`) }
{ let s = `<rect width="480" height="240" fill="#0f0f0f"/><rect y="240" width="480" height="240" fill="#fff"/>`
  let x = 30; for (const z of [128, 64, 40, 28, 16]) { for (const yy of [120, 360]) s += `<svg x="${x}" y="${yy - z / 2}" width="${z}" height="${z}" viewBox="0 0 ${z} ${z}">${lampBadge(z)}</svg>`; x += z + 34 }
  cell('A · SMALL SIZES', 'Profile pictures at 128 to 16 pixels, dark and light apps.', s) }
{ const f = (x, y, body) => `<g transform="translate(${x},${y})"><rect width="400" height="130" fill="#000" stroke="#2a3138"/>${body}</g>`
  const w = capsMark(212, 108, 34, 0.5)
  cell('A · THE IDENT (2 seconds)', '1 line drops · 2 silence · 3 lamp lights on the bass drop.',
    f(40, 22, `<line x1="212" y1="0" x2="212" y2="46" stroke="${INK}" stroke-width="1.6"/><text x="14" y="120" font-family="monospace" font-size="13" fill="${DIM}">1</text>`) +
    f(40, 172, `<line x1="212" y1="0" x2="212" y2="96" stroke="${INK}" stroke-width="1.6"/><text x="14" y="120" font-family="monospace" font-size="13" fill="${DIM}">2</text>`) +
    f(40, 322, `<line x1="${w.cx}" y1="0" x2="${w.cx}" y2="${w.cy}" stroke="${INK}" stroke-width="1.6"/>${w.svg}<text x="14" y="120" font-family="monospace" font-size="13" fill="${DIM}">3</text>`), '#0b0d0f') }

// ---------- ROW 2: the system
cell('A · THE WAY OUT', 'On the site the line forks: gold dashes leave before the lamp.',
  `<line x1="220" y1="0" x2="220" y2="332" stroke="${INK}" stroke-width="3.2"/><path d="M220 150 C220 215 330 200 330 270 L330 480" fill="none" stroke="${GOLD}" stroke-width="3.2" stroke-dasharray="11 10"/><circle cx="220" cy="358" r="29" fill="${LAMP}"/>`)
cell('A · THE DOT DOES JOBS', 'It lands on things as a SOLD sticker: names what was sold.',
  `<rect x="80" y="100" width="320" height="220" fill="#1b2026" stroke="#3a424a"/><path d="M120 280 L190 190 L240 250 L280 212 L350 280 Z" fill="#2a3138"/><text x="80" y="356" font-family="${CAPS}" font-weight="700" font-size="22" fill="#aab3bb" letter-spacing="2">YOUR WATER COMPANY</text><circle cx="380" cy="300" r="25" fill="${LAMP}"/>`)
{ const a = capsMark(250, 190, 70, 1); const b = roundWord(0, 0, 17, 6.5); const bx = (C - b.width) / 2
  cell('DECISION · THE VOICE OF THE NAME', 'Top: blunt caps (recommended). Bottom: round lowercase.',
    `${a.svg}<line x1="60" y1="250" x2="420" y2="250" stroke="#2a3138"/><g transform="translate(${bx},372)">${b.svg}</g>`) }
cell('A · DRAWN BADLY', 'Two strokes with a marker pen. Still reads.',
  `<path d="M233 6 C243 70 228 140 239 205 C245 245 234 270 238 298" fill="none" stroke="${INK}" stroke-width="10" stroke-linecap="round"/><path d="M238 302 m-38 4 c-5 -34 34 -50 59 -32 c30 21 18 68 -18 73 c-27 3 -39 -16 -41 -41 z" fill="${LAMP}"/>`)

// ---------- ROW 3: alternates, parked, and what it replaces
cell('B · THE LOOK', 'A machine eye that glances instead of stares. Most character.',
  `<circle cx="240" cy="240" r="160" fill="#0b0d10" stroke="${INK}" stroke-width="11"/><circle cx="328" cy="206" r="43" fill="${LAMP}"/>`)
cell('C · THE NOTICE', 'No symbol. Plain type, a red full stop, numbered like paperwork.',
  `<text x="52" y="230" font-family="${CAPS}" font-weight="700" font-size="84" letter-spacing="1" fill="${INK}">BADCODE</text><circle cx="426" cy="219" r="11" fill="${LAMP}"/><line x1="52" y1="268" x2="428" y2="268" stroke="${INK}" stroke-width="1.5"/><text x="52" y="304" font-family="monospace" font-size="21" fill="#aab3bb" letter-spacing="2">BC-004   ·   8 BC   ·   RECEIVED</text>`)
{ const b = capsMark(262, 270, 84, 1, '#0a0a0a')
  cell('PARKED · THE NAME IS A COLOUR', '#BADC0D is a real colour code. Loud. Sticker use only.', b.svg.replace(LAMP, '#0a0a0a') + `<text x="56" y="330" font-family="monospace" font-size="22" fill="#0a0a0a">#BADC0D</text>`, ACID) }
cell('WHAT IT REPLACES', 'The current logo: a curly bracket as the C, red and blue tips.',
  `<svg x="130" y="120" width="220" height="220" viewBox="-22.03 -9.73 79.46 79.46"><g fill="none" stroke="#fff" stroke-width="8.5" stroke-linecap="round" stroke-linejoin="round"><path d="M35.4 0C26.44 0 19.12 8.06 19.12 14.66V20.4C19.12 25.68 8.6 30 0 30"/><path d="M35.4 60C26.44 60 19.12 51.94 19.12 45.34V39.6C19.12 34.32 8.6 30 0 30"/></g><circle cx="35.4" cy="0" r="4.25" fill="#cc2b37"/><circle cx="35.4" cy="60" r="4.25" fill="#2696d4"/></svg>`)

const rows = Math.ceil(cells.length / cols), W = cols * C, H = HEAD + rows * (C + CAP)
let out = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}"><rect width="100%" height="100%" fill="#15181b"/>`
out += `<text x="24" y="44" font-family="${CAPS}" font-weight="700" font-size="34" fill="${INK}" letter-spacing="1">BADCODE LOGO — DIRECTION SKETCHES</text>`
out += `<text x="24" y="76" font-family="monospace" font-size="18" fill="#aab3bb">2026-09-29 · napkin quality, for choosing a direction · A = recommended · B, C = alternatives · nothing here is finished design</text>`
cells.forEach((c, i) => {
  const x = (i % cols) * C, y = HEAD + Math.floor(i / cols) * (C + CAP)
  out += `<g transform="translate(${x},${y})"><rect x="5" y="5" width="${C - 10}" height="${C - 10}" fill="${c.bg}"/><svg x="5" y="5" width="${C - 10}" height="${C - 10}" viewBox="0 0 ${C} ${C}" overflow="hidden">${c.body}</svg>` +
    `<text x="14" y="${C + 24}" fill="${INK}" font-family="${CAPS}" font-weight="700" font-size="20" letter-spacing="1">${c.title}</text>` +
    `<text x="14" y="${C + 48}" fill="#aab3bb" font-family="Nimbus Sans" font-size="16">${c.note}</text></g>`
})
out += '</svg>'
writeFileSync(join(here, 'direction-sheet.svg'), out)
await sharp(Buffer.from(out)).png().toFile(join(here, 'direction-sheet.png'))
console.log('ok', cells.length, W, H)
