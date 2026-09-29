// Napkin sketches, sheet 3: testing the research against the favourite.
import { createRequire } from 'node:module'
import { writeFileSync } from 'node:fs'
const require = createRequire('/home/kai/projects/badcode/badcode/package.json')
const sharp = require('sharp')
const LAMP = '#e6291c', CRIMSON = '#cc2b37', LABOUR = '#e4003b', INK = '#eef3f6', BG = '#050607', DIM = '#59626b', GOLD = '#e8c98a'
const C = 420, cells = []
const cell = (label, body, bg = BG) => cells.push({ label, body, bg })

// 1 attached vs 2 gap
cell('1 attached (a lamp)', `<line x1="210" y1="0" x2="210" y2="262" stroke="${INK}" stroke-width="3"/><circle cx="210" cy="284" r="26" fill="${LAMP}"/>`)
cell('2 gap (an !)', `<line x1="210" y1="0" x2="210" y2="232" stroke="${INK}" stroke-width="3"/><circle cx="210" cy="296" r="26" fill="${LAMP}"/>`)
// 3 badge cut, blunt
cell('3 badge cut (blunt)', `<circle cx="210" cy="210" r="190" fill="#000" stroke="${DIM}"/><clipPath id="k"><circle cx="210" cy="210" r="190"/></clipPath><g clip-path="url(#k)"><rect x="192" y="0" width="36" height="250" fill="${INK}"/><circle cx="210" cy="262" r="62" fill="${LAMP}"/></g>`, '#14171a')
// 4 badge at real sizes on dark + light UI
function badge(size) { const s = size / 420; return `<g transform="scale(${s})"><circle cx="210" cy="210" r="210" fill="#000"/><clipPath id="q${size}"><circle cx="210" cy="210" r="210"/></clipPath><g clip-path="url(#q${size})"><rect x="190" y="0" width="40" height="250" fill="${INK}"/><circle cx="210" cy="262" r="64" fill="${LAMP}"/></g></g>` }
{ let s = `<rect x="0" y="0" width="420" height="210" fill="#0f0f0f"/><rect x="0" y="210" width="420" height="210" fill="#ffffff"/>`
  let x = 24; for (const z of [96, 48, 32, 24, 16]) { s += `<svg x="${x}" y="${105 - z / 2}" width="${z}" height="${z}" viewBox="0 0 ${z} ${z}">${badge(z)}</svg><svg x="${x}" y="${315 - z / 2}" width="${z}" height="${z}" viewBox="0 0 ${z} ${z}">${badge(z)}</svg>`; x += z + 28 }
  cell('4 badge 96/48/32/24/16 dark+light UI', s) }

// wordmark voices via system fonts: BADC + disc + DE
function caps(font, weight, size, y, tracking, discScale = 1, capH = 0.72) {
  const d = size * capH * discScale, cx = 232
  const x0 = cx - d / 2 - size * 0.07, x1 = cx + d / 2 + size * 0.07
  return { cx, cy: y - size * capH / 2, d, svg:
    `<text x="${x0}" y="${y}" text-anchor="end" font-family="${font}" font-weight="${weight}" font-size="${size}" letter-spacing="${tracking}" fill="${INK}">BADC</text>` +
    `<circle cx="${cx}" cy="${y - size * capH / 2}" r="${d / 2}" fill="${LAMP}"/>` +
    `<text x="${x1}" y="${y}" text-anchor="start" font-family="${font}" font-weight="${weight}" font-size="${size}" letter-spacing="${tracking}" fill="${INK}">DE</text>` }
}
function lower(font, weight, size, y, tracking, xH = 0.52) {
  const d = size * xH * 1.04, cx = 236
  const x0 = cx - d / 2 - size * 0.05, x1 = cx + d / 2 + size * 0.05
  return { cx, cy: y - size * xH / 2, d, svg:
    `<text x="${x0}" y="${y}" text-anchor="end" font-family="${font}" font-weight="${weight}" font-size="${size}" letter-spacing="${tracking}" fill="${INK}">badc</text>` +
    `<circle cx="${cx}" cy="${y - size * xH / 2}" r="${d / 2}" fill="${LAMP}"/>` +
    `<text x="${x1}" y="${y}" text-anchor="start" font-family="${font}" font-weight="${weight}" font-size="${size}" letter-spacing="${tracking}" fill="${INK}">de</text>` }
}
const blade = (m, w = 2.5) => `<line x1="${m.cx}" y1="0" x2="${m.cx}" y2="${m.cy}" stroke="${INK}" stroke-width="${w}"/>`
{ const m = caps('Liberation Sans Narrow', 700, 92, 330, 1); cell('5 caps, heavy condensed', blade(m, 3) + m.svg) }
{ const m = caps('Nimbus Sans', 700, 70, 322, 2); cell('6 caps, plain grotesque', blade(m, 3) + m.svg) }
{ const m = lower('Nimbus Sans', 700, 84, 322, 0); cell('7 lowercase, plain bold', blade(m, 3) + m.svg) }
{ const m = lower('URW Gothic', 400, 84, 322, 0, 0.55); cell('8 lowercase, geometric', blade(m, 2.5) + m.svg) }

// 9 extended signature: the fork (gold way out) before the lamp
cell('9 the fork: the way off the line', `<line x1="210" y1="0" x2="210" y2="296" stroke="${INK}" stroke-width="3"/><path d="M210 150 C210 200 300 190 300 250 L300 420" fill="none" stroke="${GOLD}" stroke-width="3" stroke-dasharray="10 9"/><circle cx="210" cy="318" r="26" fill="${LAMP}"/>`)
// 10 sold: the dot lands on things
cell('10 the dot as a SOLD sticker', `<rect x="70" y="90" width="280" height="200" fill="#1b2026" stroke="#3a424a"/><path d="M110 250 L170 170 L215 225 L250 190 L310 250 Z" fill="#2a3138"/><rect x="70" y="300" width="280" height="1" fill="#3a424a"/><text x="70" y="330" font-family="Nimbus Sans" font-size="15" fill="#8e98a1" letter-spacing="1">YOUR WATER COMPANY</text><circle cx="332" cy="272" r="22" fill="${LAMP}"/>`)
// 11 side-eye, machine version (no white of the eye)
cell('11 alt: the look', `<circle cx="210" cy="210" r="150" fill="#0b0d10" stroke="${INK}" stroke-width="10"/><circle cx="292" cy="180" r="40" fill="${LAMP}"/>`)
// 12 pilot plate
{ const t = `<rect x="50" y="70" width="320" height="280" fill="#0b0d10" stroke="#8e98a1" stroke-width="2"/><circle cx="130" cy="150" r="30" fill="${LAMP}"/><text x="210" y="300" text-anchor="middle" font-family="Liberation Sans Narrow" font-weight="700" font-size="64" letter-spacing="4" fill="${INK}">BADCODE</text><circle cx="66" cy="86" r="4" fill="#59626b"/><circle cx="354" cy="86" r="4" fill="#59626b"/><circle cx="66" cy="334" r="4" fill="#59626b"/><circle cx="354" cy="334" r="4" fill="#59626b"/>`
  cell('12 alt: pilot plate', t) }
// 13 reds compared
cell('13 lamp red / current crimson / Labour', `<circle cx="100" cy="210" r="46" fill="${LAMP}"/><circle cx="210" cy="210" r="46" fill="${CRIMSON}"/><circle cx="320" cy="210" r="46" fill="${LABOUR}"/><text x="100" y="292" text-anchor="middle" font-family="monospace" font-size="15" fill="#aab3bb">${LAMP}</text><text x="210" y="292" text-anchor="middle" font-family="monospace" font-size="15" fill="#aab3bb">${CRIMSON}</text><text x="320" y="292" text-anchor="middle" font-family="monospace" font-size="15" fill="#aab3bb">${LABOUR}</text>`)
// 14 on paper (sticker): black ink + red
cell('14 sticker on white', `<line x1="210" y1="0" x2="210" y2="250" stroke="#0a0a0a" stroke-width="14"/><circle cx="210" cy="262" r="60" fill="${LAMP}"/>`, '#f3f1ec')
// 15 video frame: mark as end card, 16:9
cell('15 end card 16:9', `<rect x="10" y="95" width="400" height="225" fill="#000" stroke="#2a3138"/><svg x="10" y="95" width="400" height="225" viewBox="0 0 400 225">${(() => { const size = 30, y = 168, cx = 222, d = size * 0.72; return `<line x1="${cx}" y1="0" x2="${cx}" y2="${y - size * 0.36}" stroke="${INK}" stroke-width="1.2"/><text x="${cx - d / 2 - 2}" y="${y}" text-anchor="end" font-family="Liberation Sans Narrow" font-weight="700" font-size="${size}" letter-spacing="0.5" fill="${INK}">BADC</text><circle cx="${cx}" cy="${y - size * 0.36}" r="${d / 2}" fill="${LAMP}"/><text x="${cx + d / 2 + 2}" y="${y}" text-anchor="start" font-family="Liberation Sans Narrow" font-weight="700" font-size="${size}" letter-spacing="0.5" fill="${INK}">DE</text>` })()}</svg>`, '#14171a')
// 16 hand-drawn test: wobbly marker version
cell('16 drawn badly (marker test)', `<path d="M204 4 C212 60 200 120 209 180 C214 215 205 235 208 258" fill="none" stroke="${INK}" stroke-width="9" stroke-linecap="round"/><path d="M208 262 m-34 4 c-4 -30 30 -44 52 -28 c26 18 16 60 -16 64 c-24 3 -34 -14 -36 -36 z" fill="${LAMP}"/>`)

const cols = 4, rows = Math.ceil(cells.length / cols)
let out = `<svg xmlns="http://www.w3.org/2000/svg" width="${cols * C}" height="${rows * (C + 40)}"><rect width="100%" height="100%" fill="#1a1d20"/>`
cells.forEach((c, i) => {
  const x = (i % cols) * C, y = Math.floor(i / cols) * (C + 40)
  out += `<g transform="translate(${x},${y})"><rect x="4" y="4" width="${C - 8}" height="${C - 8}" fill="${c.bg}"/><svg x="0" y="0" width="${C}" height="${C}" viewBox="0 0 ${C} ${C}" overflow="hidden">${c.body}</svg><text x="14" y="${C + 26}" fill="#aab3bb" font-family="monospace" font-size="19">${c.label}</text></g>`
})
out += '</svg>'
writeFileSync('sheet3.svg', out)
await sharp(Buffer.from(out)).png().toFile('sheet3.png')
console.log('ok', cells.length)
