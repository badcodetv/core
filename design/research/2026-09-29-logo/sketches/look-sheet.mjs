// Look sheet: Kai's pick of 2026-09-29, drawn out so the ring weight can be chosen.
// Napkin quality, NOT finished design. Run from anywhere: node look-sheet.mjs   (needs the repo's `sharp`)
// Also writes clean reference images to ./look/ for the Flow mock-up round.
import { createRequire } from 'node:module'
import { writeFileSync, mkdirSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'
const here = dirname(fileURLToPath(import.meta.url))
const require = createRequire(join(here, '../../../../package.json'))
const sharp = require('sharp')

const LAMP = '#e6291c', INK = '#eef3f6', BG = '#050607', DIM = '#59626b', DARK = '#0a0a0a'
const C = 480, CAP = 64, HEAD = 96, cols = 4
const CAPS = 'Liberation Sans Narrow'
const cells = []
const cell = (title, note, body, bg = BG) => cells.push({ title, note, body, bg })

// The Look exactly as on the direction sheet: ring r160 line 11, red dot r43 sitting at (+88, -34).
const PR = 43 / 160, PX = 88 / 160, PY = -34 / 160
const REF = 21 / 160 // ring weight for lock-ups, mock-ups and Flow references — "thicker 3", Kai 2026-09-29
const LETTER = 6.5 / 17 // line weight of the round letters, as a share of their ring radius

function look(cx, cy, R, w, o = {}) {
  const { ink = INK, red = LAMP, fill = 'none', pr = PR * R, px = PX, py = PY, pupil = true } = o
  // keep the dot inside the ring when the ring gets heavy or the mark gets tiny
  const d = Math.hypot(px, py) * R, max = R - w / 2 - pr - Math.max(0.3, R * 0.03), k = d > max ? max / d : 1
  return `<circle cx="${cx}" cy="${cy}" r="${R}" fill="${fill}" stroke="${ink}" stroke-width="${w}"/>` +
    (pupil ? `<circle cx="${cx + px * R * k}" cy="${cy + py * R * k}" r="${pr}" fill="${red}"/>` : '')
}
function roundWord(x0, base, r, w, o = {}) {
  const { ink = INK, red = LAMP, eye = false } = o
  const step = 2 * r + w + r * 0.42, cy = base - r, top = base - 2 * r * 1.55, L = []
  const ring = cx => `<circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="${ink}" stroke-width="${w}"/>`
  const stem = (x, y1, y2) => `<line x1="${x}" y1="${y1}" x2="${x}" y2="${y2}" stroke="${ink}" stroke-width="${w}"/>`
  const arc = (cx, a1, a2) => { const p = a => [cx + r * Math.cos(a * Math.PI / 180), cy + r * Math.sin(a * Math.PI / 180)]; const [x1, y1] = p(a1), [x2, y2] = p(a2); return `<path d="M${x1} ${y1} A${r} ${r} 0 1 1 ${x2} ${y2}" fill="none" stroke="${ink}" stroke-width="${w}"/>` }
  'badcode'.split('').forEach((ch, i) => {
    const cx = x0 + r + w / 2 + i * step
    if (ch === 'b') L.push(ring(cx), stem(cx - r, top, base + w / 2))
    if (ch === 'a') L.push(ring(cx), stem(cx + r, cy - r - w / 2, base + w / 2))
    if (ch === 'd') L.push(ring(cx), stem(cx + r, top, base + w / 2))
    if (ch === 'c') L.push(arc(cx, 42, -42))
    if (ch === 'e') L.push(arc(cx, 38, 0), `<line x1="${cx - r}" y1="${cy}" x2="${cx + r + w / 2}" y2="${cy}" stroke="${ink}" stroke-width="${w}"/>`)
    if (ch === 'o') L.push(eye ? look(cx, cy, r, w, { ink, red, pr: r * 0.4, px: 0.3, py: -0.12 }) : `<circle cx="${cx}" cy="${cy}" r="${r + w / 2}" fill="${red}"/>`)
  })
  return { svg: L.join(''), width: 7 * step - r * 0.42, top, height: base + w / 2 - top }
}
const wordAt = (cx, base, r, o) => { const w = r * LETTER, m = roundWord(0, base, r, w, o); return `<g transform="translate(${cx - m.width / 2},0)">${m.svg}</g>` }
function badge(z, ratio = REF) {
  const R = z * 0.36, w = Math.max(R * ratio, 1.6), pr = Math.max(PR * R, 2.3)
  return `<circle cx="${z / 2}" cy="${z / 2}" r="${z / 2}" fill="#000"/>` + look(z / 2, z / 2, R, w, { pr })
}
function wobble(cx, cy, R, amp, seed, from = 0, to = 360, n = 72) {
  const pts = []
  for (let i = 0; i <= n; i++) {
    const a = (from + (to - from) * i / n) * Math.PI / 180
    const rr = R + amp * (Math.sin(a * 3 + seed) * 0.6 + Math.sin(a * 7 + seed * 2.3) * 0.25 + Math.sin(a * 1.3 + seed * 0.7) * 0.5) + (i / n) * amp * 0.9
    pts.push(`${(cx + rr * Math.cos(a)).toFixed(1)} ${(cy + rr * Math.sin(a)).toFixed(1)}`)
  }
  return 'M' + pts.join(' L')
}

// ---------- ROW 1: the icon, and how thick the ring line is
const ladder = [[11, 'THE ICON · AS YOU SAW IT', 'The sketch you picked. Ring line as drawn.'],
  [14, 'THICKER · 1', 'Ring line about a quarter thicker.'],
  [17, 'THICKER · 2', 'Ring line about half as thick again.'],
  [21, 'THICKER · 3', 'Ring line nearly twice as thick.']]
for (const [w, t, n] of ladder) cell(t, n, look(240, 240, 160, w, { fill: '#0b0d10' }))

// ---------- ROW 2: the name, and the two together
cell('THE NAME', 'Round lowercase. The o is a full red dot.', wordAt(240, 282, 22))
cell('THE NAME · ON WHITE', 'Same drawing, dark letters on white.', wordAt(240, 282, 22, { ink: DARK }), '#ffffff')
{ const r = 15, w = r * LETTER, m = roundWord(0, 0, r, w), R = 30, gap = 28, total = 2 * R + gap + m.width, x = (C - total) / 2
  const row = (base, ringW) => look(x + R, base - m.height / 2 + w / 2, R - ringW / 2, ringW) + `<g transform="translate(${x + 2 * R + gap},${base})">${m.svg}</g>`
  cell('TOGETHER · SIDE BY SIDE', 'Top: thin ring, as the icon. Bottom: ring as heavy as the letters.',
    row(190, 30 * REF) + `<line x1="60" y1="250" x2="420" y2="250" stroke="#2a3138"/>` + row(360, w)) }
cell('TOGETHER · STACKED', 'The icon over the name, for sleeves and posters.',
  look(240, 170, 105, 105 * REF) + wordAt(240, 408, 14))

// ---------- ROW 3: does it survive
{ let s = `<rect width="480" height="240" fill="#0f0f0f"/><rect y="240" width="480" height="240" fill="#fff"/>`
  let x = 30; for (const z of [128, 64, 40, 28, 16]) { for (const yy of [120, 360]) s += `<svg x="${x}" y="${yy - z / 2}" width="${z}" height="${z}" viewBox="0 0 ${z} ${z}">${badge(z)}</svg>`; x += z + 34 }
  cell('SMALL SIZES · THE ICON', 'Profile pictures at 128 to 16 pixels, dark and light apps.', s) }
cell('SMALL SIZES · THE NAME', 'The name shrinking. The red dot is the last thing to go.',
  wordAt(240, 130, 14) + wordAt(240, 230, 9) + wordAt(240, 310, 6) + wordAt(240, 370, 4) + wordAt(240, 420, 2.6))
cell('FOR THE RECORD · THE EYE AS THE O', 'Top: your first thought. Bottom: the full red dot (your pick).',
  wordAt(240, 200, 20, { eye: true }) + `<line x1="60" y1="250" x2="420" y2="250" stroke="#2a3138"/>` + wordAt(240, 372, 20))
cell('RULE · NEVER IN THE MIDDLE', 'Left: ours. Right: dot in the middle is a record button.',
  look(130, 240, 84, 84 * REF) + look(350, 240, 84, 84 * REF, { px: 0, py: 0, ink: DIM, red: '#7a2a24' }) +
  `<path d="M262 152 L438 328 M438 152 L262 328" stroke="${INK}" stroke-width="3" opacity="0.85"/>`)

// ---------- ROW 4: in use
cell('DRAWN BADLY', 'A circle and a blob with a marker pen. Still reads.',
  `<path d="${wobble(236, 244, 146, 7, 1.7, -80, 296)}" fill="none" stroke="${INK}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>` +
  `<path d="${wobble(322, 204, 40, 5, 4.1, 0, 360, 40)} Z" fill="${LAMP}"/>`)
{ const f = (y, body, n) => `<g transform="translate(40,${y})"><rect width="400" height="130" fill="#000" stroke="#2a3138"/>${body}<text x="14" y="120" font-family="monospace" font-size="13" fill="${DIM}">${n}</text></g>`
  cell('THE IDENT (2 seconds)', '1 the ring · 2 it looks at you, on the bass drop · 3 it gives you the look.',
    f(22, look(200, 65, 46, 46 * REF, { pupil: false }), 1) + f(172, look(200, 65, 46, 46 * REF, { px: 0, py: 0 }), 2) + f(322, look(200, 65, 46, 46 * REF), 3), '#0b0d0f') }
cell('APP ICON AND STICKER', 'Left: phone app icon. Right: white sticker, dark ring.',
  `<rect x="46" y="150" width="180" height="180" rx="42" fill="#000" stroke="#2a3138"/>` + look(136, 240, 62, 62 * REF) +
  `<circle cx="346" cy="240" r="96" fill="#f4f4f1"/>` + look(346, 240, 68, 68 * REF, { ink: DARK }), '#1b1f24')
cell('RECORD SLEEVE', 'Big icon, small name, catalogue number like paperwork.',
  `<rect x="40" y="40" width="400" height="400" fill="#000" stroke="#2a3138"/>` + look(240, 214, 124, 124 * REF) +
  `<g transform="translate(66,412)">${roundWord(0, 0, 8, 8 * LETTER).svg}</g>` +
  `<text x="414" y="412" text-anchor="end" font-family="monospace" font-size="15" fill="#aab3bb" letter-spacing="2">BC-004</text>`, '#15181b')

const rows = Math.ceil(cells.length / cols), W = cols * C, H = HEAD + rows * (C + CAP)
let out = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}"><rect width="100%" height="100%" fill="#15181b"/>`
out += `<text x="24" y="44" font-family="${CAPS}" font-weight="700" font-size="34" fill="${INK}" letter-spacing="1">BADCODE LOGO — THE LOOK (KAI'S PICK)</text>`
out += `<text x="24" y="76" font-family="monospace" font-size="18" fill="#aab3bb">2026-09-29 · napkin quality · icon = the ring with the red dot · name = round lowercase, the o is a full red dot · choose a ring thickness</text>`
cells.forEach((c, i) => {
  const x = (i % cols) * C, y = HEAD + Math.floor(i / cols) * (C + CAP)
  out += `<g transform="translate(${x},${y})"><rect x="5" y="5" width="${C - 10}" height="${C - 10}" fill="${c.bg}"/><svg x="5" y="5" width="${C - 10}" height="${C - 10}" viewBox="0 0 ${C} ${C}" overflow="hidden">${c.body}</svg>` +
    `<text x="14" y="${C + 24}" fill="${INK}" font-family="${CAPS}" font-weight="700" font-size="20" letter-spacing="1">${c.title}</text>` +
    `<text x="14" y="${C + 48}" fill="#aab3bb" font-family="Nimbus Sans" font-size="16">${c.note}</text></g>`
})
out += '</svg>'
writeFileSync(join(here, 'look-sheet.svg'), out)
await sharp(Buffer.from(out)).png().toFile(join(here, 'look-sheet.png'))

// ---------- clean references for the Flow mock-up round (our drawing, so they live in the repo)
mkdirSync(join(here, 'look'), { recursive: true })
const ref = async (name, w, h, body, bg = BG) => {
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}"><rect width="100%" height="100%" fill="${bg}"/>${body}</svg>`
  writeFileSync(join(here, 'look', name + '.svg'), svg)
  await sharp(Buffer.from(svg)).png().toFile(join(here, 'look', name + '.png'))
}
const big = (cx, base, r, o) => { const m = roundWord(0, base, r, r * LETTER, o); return `<g transform="translate(${cx - m.width / 2},0)">${m.svg}</g>` }
await ref('look-icon', 1024, 1024, look(512, 512, 330, 330 * REF))
await ref('look-icon-on-white', 1024, 1024, look(512, 512, 330, 330 * REF, { ink: DARK }), '#ffffff')
await ref('look-name', 1600, 900, big(800, 520, 70))
await ref('look-stacked', 1600, 900, look(800, 330, 210, 210 * REF) + big(800, 800, 40))
console.log('ok', cells.length, W, H)
