// Napkin sketches, sheet 2: weights, small sizes, colder eye, colours.
import { createRequire } from 'node:module'
import { writeFileSync } from 'node:fs'
const require = createRequire('/home/kai/projects/badcode/badcode/package.json')
const sharp = require('sharp')
const RED = '#e1251b', INK = '#f2f4f5', BG = '#050607', DIM = '#59626b', ACID = '#BADC0D'

function word(r, w, opts = {}) {
  const { ink = INK, red = RED, oMode = 'disc', gap = 0.42, asc = 1.55, oScale = 1 } = opts
  const step = 2 * r + w + r * gap
  const cy = -r, base = 0, top = -2 * r * asc
  const L = []
  const ring = (cx, col = ink) => `<circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="${col}" stroke-width="${w}"/>`
  const stem = (x, y1, y2, col = ink) => `<line x1="${x}" y1="${y1}" x2="${x}" y2="${y2}" stroke="${col}" stroke-width="${w}"/>`
  const arc = (cx, a1, a2, col = ink) => {
    const p = a => [cx + r * Math.cos(a * Math.PI / 180), cy + r * Math.sin(a * Math.PI / 180)]
    const [x1, y1] = p(a1), [x2, y2] = p(a2)
    return `<path d="M${x1} ${y1} A${r} ${r} 0 1 1 ${x2} ${y2}" fill="none" stroke="${col}" stroke-width="${w}"/>`
  }
  let oCx = 0
  'badcode'.split('').forEach((ch, i) => {
    const cx = r + w / 2 + i * step
    if (ch === 'b') L.push(ring(cx), stem(cx - r, top, base + w / 2))
    if (ch === 'a') L.push(ring(cx), stem(cx + r, cy - r - w / 2, base + w / 2))
    if (ch === 'd') L.push(ring(cx), stem(cx + r, top, base + w / 2))
    if (ch === 'c') L.push(arc(cx, 42, -42))
    if (ch === 'e') L.push(arc(cx, 38, 0), `<line x1="${cx - r}" y1="${cy}" x2="${cx + r + w / 2}" y2="${cy}" stroke="${ink}" stroke-width="${w}"/>`)
    if (ch === 'o') {
      oCx = cx
      if (oMode === 'disc') L.push(`<circle cx="${cx}" cy="${cy}" r="${(r + w / 2) * oScale}" fill="${red}"/>`)
      if (oMode === 'side') L.push(ring(cx), `<circle cx="${cx + r * 0.36}" cy="${cy - r * 0.2}" r="${r * 0.4}" fill="${red}"/>`)
    }
  })
  return { svg: L.join(''), width: 7 * step - r * gap, oCx, cy, top }
}

const C = 420, cells = []
const cell = (label, body, bg = BG) => cells.push({ label, body, bg })
const place = (m, y, extra = '') => { const x = (C - m.width) / 2; return { x, g: `${extra}<g transform="translate(${x},${y})">${m.svg}</g>` } }

// weights with blade
for (const [label, r, w, bw] of [['1 hairline', 21, 2.2, 2.2], ['2 regular', 20, 7, 2.5], ['3 heavy', 18, 13, 3]]) {
  const m = word(r, w, { gap: w > 10 ? 0.5 : 0.42 }); const x = (C - m.width) / 2
  cell(label, `<line x1="${x + m.oCx}" y1="0" x2="${x + m.oCx}" y2="${300 + m.cy}" stroke="${INK}" stroke-width="${bw}"/><g transform="translate(${x},300)">${m.svg}</g>`)
}
// hairline + bigger dot
{ const m = word(21, 2.2, { oScale: 1.18 }); const x = (C - m.width) / 2
  cell('4 hairline, heavy lamp', `<line x1="${x + m.oCx}" y1="0" x2="${x + m.oCx}" y2="${300 + m.cy}" stroke="${INK}" stroke-width="2.2"/><g transform="translate(${x},300)">${m.svg}</g>`) }

// the drop at real sizes: 128, 64, 32, 16 (rendered big then shown scaled) 
function drop(size, lineW, rDot, yDot) {
  return `<rect width="${size}" height="${size}" fill="#000"/><line x1="${size / 2}" y1="0" x2="${size / 2}" y2="${yDot}" stroke="${INK}" stroke-width="${lineW}"/><circle cx="${size / 2}" cy="${yDot}" r="${rDot}" fill="${RED}"/>`
}
cell('5 drop: 128 / 64 / 32 / 16 px',
  `<svg x="20" y="40" width="128" height="128" viewBox="0 0 128 128">${drop(128, 4, 17, 80)}</svg>` +
  `<svg x="170" y="40" width="64" height="64" viewBox="0 0 64 64">${drop(64, 3, 9, 40)}</svg>` +
  `<svg x="260" y="40" width="32" height="32" viewBox="0 0 32 32">${drop(32, 2, 5, 20)}</svg>` +
  `<svg x="320" y="40" width="16" height="16" viewBox="0 0 16 16">${drop(16, 2, 3, 10)}</svg>` +
  // circle-cropped versions
  `<clipPath id="c1"><circle cx="84" cy="284" r="64"/></clipPath><g clip-path="url(#c1)"><svg x="20" y="220" width="128" height="128" viewBox="0 0 128 128">${drop(128, 4, 17, 80)}</svg></g><circle cx="84" cy="284" r="64" fill="none" stroke="${DIM}"/>` +
  `<clipPath id="c2"><circle cx="202" cy="252" r="32"/></clipPath><g clip-path="url(#c2)"><svg x="170" y="220" width="64" height="64" viewBox="0 0 64 64">${drop(64, 3, 9, 40)}</svg></g><circle cx="202" cy="252" r="32" fill="none" stroke="${DIM}"/>` +
  `<clipPath id="c3"><circle cx="276" cy="236" r="16"/></clipPath><g clip-path="url(#c3)"><svg x="260" y="220" width="32" height="32" viewBox="0 0 32 32">${drop(32, 2, 5, 20)}</svg></g><circle cx="276" cy="236" r="16" fill="none" stroke="${DIM}"/>`, '#14171a')

// cold side-eye: thin ring, small pupil tangent
cell('6 cold side-eye', `<circle cx="210" cy="210" r="130" fill="none" stroke="${INK}" stroke-width="4"/><circle cx="283" cy="163" r="36" fill="${RED}"/>`)
// eye-roll: pupil at top
cell('7 eye-roll', `<circle cx="210" cy="210" r="130" fill="none" stroke="${INK}" stroke-width="4"/><circle cx="210" cy="122" r="36" fill="${RED}"/>`)
// no ring: avatar circle is the eye
cell('8 avatar is the eye', `<circle cx="210" cy="210" r="180" fill="#000" stroke="${DIM}" stroke-width="1"/><circle cx="292" cy="150" r="40" fill="${RED}"/>`, '#14171a')

// drop + glance combined: lamp hanging off-centre? (pendulum mid-swing)
cell('9 mid-swing', `<line x1="210" y1="0" x2="300" y2="262" stroke="${INK}" stroke-width="3"/><circle cx="308" cy="284" r="24" fill="${RED}"/>`)
// acid colour tests
{ const m = word(20, 7, { ink: ACID }); const p = place(m, 235); cell('10 #BADC0D ink + red o', p.g) }
{ const m = word(20, 7, { ink: '#0a0a0a' }); const p = place(m, 235); cell('11 black on #BADC0D', p.g, ACID) }
{ const m = word(20, 7, { ink: INK, red: ACID }); const p = place(m, 235); cell('12 acid o', p.g) }
// hazard sign with the drop
cell('13 hazard sign', `<path d="M210 60 L380 350 L40 350 Z" fill="${ACID}" stroke="#0a0a0a" stroke-width="18" stroke-linejoin="round"/><line x1="210" y1="120" x2="210" y2="262" stroke="#0a0a0a" stroke-width="14"/><circle cx="210" cy="300" r="20" fill="${RED}"/>`, '#14171a')
// wordmark stacked bad / code with drop
{ const r = 30, w = 10
  cell('14 lockup on sleeve corner', `<rect x="0" y="0" width="420" height="420" fill="#0b0d0f"/><g transform="translate(250,0) scale(0.42)">${(() => { const m = word(20, 7); return `<line x1="${m.oCx}" y1="0" x2="${m.oCx}" y2="${820 + m.cy}" stroke="${INK}" stroke-width="3"/><g transform="translate(0,820)">${m.svg}</g>` })()}</g>`) }
// uppercase system-font test with red O
cell('15 caps grotesque', `<text x="210" y="235" text-anchor="middle" font-family="Liberation Sans, Arial, Helvetica, DejaVu Sans, sans-serif" font-weight="700" font-size="62" letter-spacing="2" fill="${INK}">BADC<tspan fill="${RED}">●</tspan>DE</text>`)
// seven rings no stems? pure abstraction of the word
{ let s = ''; for (let i = 0; i < 7; i++) s += i === 4 ? `<circle cx="${66 + i * 48}" cy="210" r="21" fill="${RED}"/>` : `<circle cx="${66 + i * 48}" cy="210" r="17" fill="none" stroke="${INK}" stroke-width="7"/>`
  cell('16 seven rings', s) }

const cols = 4, rows = Math.ceil(cells.length / cols)
let out = `<svg xmlns="http://www.w3.org/2000/svg" width="${cols * C}" height="${rows * (C + 40)}"><rect width="100%" height="100%" fill="#1a1d20"/>`
cells.forEach((c, i) => {
  const x = (i % cols) * C, y = Math.floor(i / cols) * (C + 40)
  out += `<g transform="translate(${x},${y})"><rect x="4" y="4" width="${C - 8}" height="${C - 8}" fill="${c.bg}"/><svg x="0" y="0" width="${C}" height="${C}" viewBox="0 0 ${C} ${C}" overflow="hidden">${c.body}</svg><text x="14" y="${C + 26}" fill="#aab3bb" font-family="monospace" font-size="20">${c.label}</text></g>`
})
out += '</svg>'
writeFileSync('sheet2.svg', out)
await sharp(Buffer.from(out)).png().toFile('sheet2.png')
console.log('ok', cells.length)
