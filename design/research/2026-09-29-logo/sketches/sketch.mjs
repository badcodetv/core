// Napkin sketches: thinking with a pencil, not design. Geometry only.
import { createRequire } from 'node:module'
import { writeFileSync } from 'node:fs'
const require = createRequire('/home/kai/projects/badcode/badcode/package.json')
const sharp = require('sharp')

const RED = '#e1251b', INK = '#f2f4f5', BG = '#050607', DIM = '#59626b'

// round-letter wordmark built from one ring and one stem
function word(x0, base, r, w, opts = {}) {
  const { ink = INK, red = RED, oMode = 'disc', gap = 0.42, asc = 1.55 } = opts
  const step = 2 * r + w + r * gap
  const xh = 2 * r            // ring centre sits r above baseline (stroke centred)
  const cy = base - r
  const top = base - 2 * r * asc
  const L = []
  const ring = (cx, col = ink) => `<circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="${col}" stroke-width="${w}"/>`
  const stem = (x, y1, y2, col = ink) => `<line x1="${x}" y1="${y1}" x2="${x}" y2="${y2}" stroke="${col}" stroke-width="${w}" stroke-linecap="butt"/>`
  const arc = (cx, a1, a2, col = ink) => {
    const p = a => [cx + r * Math.cos(a * Math.PI / 180), cy + r * Math.sin(a * Math.PI / 180)]
    const [x1, y1] = p(a1), [x2, y2] = p(a2)
    return `<path d="M${x1} ${y1} A${r} ${r} 0 1 1 ${x2} ${y2}" fill="none" stroke="${col}" stroke-width="${w}" stroke-linecap="butt"/>`
  }
  const letters = 'badcode'.split('')
  let oCx = 0
  letters.forEach((ch, i) => {
    const cx = x0 + r + w / 2 + i * step
    if (ch === 'b') { L.push(ring(cx), stem(cx - r, top, base + w / 2)) }
    if (ch === 'a') { L.push(ring(cx), stem(cx + r, cy - r - w / 2, base + w / 2)) }
    if (ch === 'd') { L.push(ring(cx), stem(cx + r, top, base + w / 2)) }
    if (ch === 'c') { L.push(arc(cx, 42, -42)) }
    if (ch === 'e') { L.push(arc(cx, 38, 0), `<line x1="${cx - r}" y1="${cy}" x2="${cx + r + w / 2}" y2="${cy}" stroke="${ink}" stroke-width="${w}"/>`) }
    if (ch === 'o') {
      oCx = cx
      if (oMode === 'disc') L.push(`<circle cx="${cx}" cy="${cy}" r="${r + w / 2}" fill="${red}"/>`)
      if (oMode === 'pupil') L.push(ring(cx), `<circle cx="${cx}" cy="${cy}" r="${r * 0.42}" fill="${red}"/>`)
      if (oMode === 'side') L.push(ring(cx), `<circle cx="${cx - r * 0.38}" cy="${cy - r * 0.18}" r="${r * 0.4}" fill="${red}"/>`)
      if (oMode === 'plain') L.push(ring(cx))
    }
  })
  const width = 7 * step - r * gap
  return { svg: L.join(''), width, oCx, cy, top }
}

const cells = []
const C = 420
function cell(label, body, bg = BG) {
  cells.push({ label, body, bg })
}

// 1 red o wordmark
{ const r = 19, w = 9; const m = word(0, 0, r, w); const x = (C - m.width) / 2
  cell('1  red o', `<g transform="translate(${x},235)">${m.svg}</g>`) }
// 2 pupil o
{ const r = 19, w = 9; const m = word(0, 0, r, w, { oMode: 'pupil' }); const x = (C - m.width) / 2
  cell('2  lens o', `<g transform="translate(${x},235)">${m.svg}</g>`) }
// 3 lamp / plumb line
cell('3  the lamp', `<line x1="210" y1="0" x2="210" y2="250" stroke="${INK}" stroke-width="3"/><circle cx="210" cy="272" r="24" fill="${RED}"/>`)
// 4 bang
cell('4  the bang', `<line x1="210" y1="70" x2="210" y2="262" stroke="${INK}" stroke-width="5"/><circle cx="210" cy="312" r="24" fill="${RED}"/>`)
// 5 midnight
cell('5  midnight', `<circle cx="210" cy="210" r="150" fill="none" stroke="${DIM}" stroke-width="2"/><line x1="210" y1="60" x2="210" y2="210" stroke="${INK}" stroke-width="4"/><circle cx="210" cy="210" r="20" fill="${RED}"/>`)
// 6 side-eye
cell('6  side-eye', `<circle cx="210" cy="210" r="120" fill="none" stroke="${INK}" stroke-width="16"/><circle cx="262" cy="176" r="46" fill="${RED}"/>`)
// 7 standby
cell('7  standby', `<circle cx="338" cy="338" r="11" fill="${RED}"/>`)
// 8 seven lights
{ let s = ''; for (let i = 0; i < 7; i++) s += `<circle cx="${84 + i * 42}" cy="210" r="13" fill="${i === 4 ? RED : INK}"/>`
  cell('8  seven lights', s) }
// 9 lockup: blade into red o
{ const r = 19, w = 9; const m = word(0, 0, r, w); const x = (C - m.width) / 2
  cell('9  blade lockup', `<line x1="${x + m.oCx}" y1="0" x2="${x + m.oCx}" y2="${300 + m.cy}" stroke="${INK}" stroke-width="2.5"/><g transform="translate(${x},300)">${m.svg}</g>`) }
// 10 node on line
cell('10 node', `<line x1="210" y1="0" x2="210" y2="420" stroke="${INK}" stroke-width="3"/><circle cx="210" cy="250" r="24" fill="${RED}"/>`)
// 11 visor bar
cell('11 visor', `<rect x="110" y="196" width="200" height="28" fill="${RED}"/>`)
// 12 half-lid
cell('12 half-lid', `<path d="M90 200 A120 120 0 0 0 330 200 Z" fill="none" stroke="${INK}" stroke-width="16" stroke-linejoin="round"/><path d="M162 208 A48 48 0 0 0 258 208 Z" fill="${RED}"/>`)
// 13 side-eye o in wordmark
{ const r = 19, w = 9; const m = word(0, 0, r, w, { oMode: 'side' }); const x = (C - m.width) / 2
  cell('13 side-eye o', `<g transform="translate(${x},235)">${m.svg}</g>`) }
// 14 seven lights vertical (the blade as LEDs)
{ let s = ''; for (let i = 0; i < 7; i++) s += `<circle cx="210" cy="${66 + i * 48}" r="12" fill="${i === 4 ? RED : INK}"/>`
  cell('14 led blade', s) }
// 15 red o on white
{ const r = 19, w = 9; const m = word(0, 0, r, w, { ink: '#0a0a0a' }); const x = (C - m.width) / 2
  cell('15 red o / white', `<g transform="translate(${x},235)">${m.svg}</g>`, '#f4f2ee') }
// 16 lamp in circle avatar
cell('16 lamp avatar', `<circle cx="210" cy="210" r="190" fill="#000" stroke="${DIM}" stroke-width="1"/><line x1="210" y1="20" x2="210" y2="232" stroke="${INK}" stroke-width="5"/><circle cx="210" cy="262" r="34" fill="${RED}"/>`)

const cols = 4, rows = Math.ceil(cells.length / cols)
let out = `<svg xmlns="http://www.w3.org/2000/svg" width="${cols * C}" height="${rows * (C + 40)}" viewBox="0 0 ${cols * C} ${rows * (C + 40)}"><rect width="100%" height="100%" fill="#1a1d20"/>`
cells.forEach((c, i) => {
  const x = (i % cols) * C, y = Math.floor(i / cols) * (C + 40)
  out += `<g transform="translate(${x},${y})"><rect x="4" y="4" width="${C - 8}" height="${C - 8}" fill="${c.bg}"/><svg x="0" y="0" width="${C}" height="${C}" viewBox="0 0 ${C} ${C}" overflow="hidden">${c.body}</svg><text x="14" y="${C + 26}" fill="#aab3bb" font-family="monospace" font-size="20">${c.label}</text></g>`
})
out += '</svg>'
writeFileSync('sheet1.svg', out)
await sharp(Buffer.from(out)).png().toFile('sheet1.png')
console.log('ok', cells.length)
