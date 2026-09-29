// Builds the BadCode logo files — "The Look" — from the settings Kai saved on the logo bench (2026-09-29).
// Usage: node scripts/brand/build-logo.mjs            (writes docs/brand/logo/, needs the repo's `sharp`)
// Change SET, re-run, never hand-edit an SVG. Geometry is the bench's own (design/research/2026-09-29-logo/tuner/).
import { createRequire } from 'node:module'
import { mkdirSync, writeFileSync, readFileSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'
const root = join(dirname(fileURLToPath(import.meta.url)), '../..')
const sharp = createRequire(join(root, 'package.json'))('sharp')
const OUT = join(root, 'docs/brand/logo')
mkdirSync(OUT, { recursive: true })

// Bench save 52d1h96436mwhgdqjrj7, 2026-09-29 18:30 — Kai: "it's perfect".
const SET = {
  ring: 0.17,    // ring line thickness, as a fraction of the ring's radius
  dot: 0.245,    // red dot radius, as a fraction of the ring's radius
  push: 0.51,    // how far off centre: 0 = centre, 1 = touching the inside of the ring
  angle: 55,     // which way it looks: degrees clockwise from 12 o'clock
  red: '#cc2b37',
  lw: 0.30,      // letter line weight, as a fraction of letter radius
  tr: 0.26,      // letter spacing, as a fraction of letter radius
  ck: 0.42,      // the c pulled toward the red o (optical kerning), fraction of letter radius
}
const INK = { dark: '#0a0a0a', light: '#eef3f6' }, GROUND = '#050607'
const f = n => +n.toFixed(2)

// ---- geometry (identical to the bench)
function icon(cx, cy, R, ink, minW = 0, minDot = 0) {
  const w = Math.max(SET.ring * R, minW), pr = Math.max(SET.dot * R, minDot)
  const room = Math.max(0, R - w / 2 - SET.dot * R - R * 0.02), d = SET.push * room, a = SET.angle * Math.PI / 180
  return `<circle cx="${f(cx)}" cy="${f(cy)}" r="${f(R - w / 2)}" fill="none" stroke="${ink}" stroke-width="${f(w)}"/>` +
    `<circle cx="${f(cx + d * Math.sin(a))}" cy="${f(cy - d * Math.cos(a))}" r="${f(pr)}" fill="${SET.red}"/>`
}
// The name, drawn from circles and stems — no font. Baseline at y=base; returns its box.
function word(x0, base, r, ink) {
  const w = r * SET.lw, step = 2 * r + w + r * SET.tr, cy = base - r, top = base - 2 * r * 1.55, k = SET.ck * r, L = []
  const ring = cx => `<circle cx="${f(cx)}" cy="${f(cy)}" r="${f(r)}"/>`
  const stem = (x, y1, y2) => `<line x1="${f(x)}" y1="${f(y1)}" x2="${f(x)}" y2="${f(y2)}"/>`
  const arc = (cx, a1, a2) => { const p = a => [cx + r * Math.cos(a * Math.PI / 180), cy + r * Math.sin(a * Math.PI / 180)]; const [x1, y1] = p(a1), [x2, y2] = p(a2); return `<path d="M${f(x1)} ${f(y1)}A${f(r)} ${f(r)} 0 1 1 ${f(x2)} ${f(y2)}"/>` }
  let o = ''
  'badcode'.split('').forEach((ch, i) => {
    const cx = x0 + r + w / 2 + i * step - (i >= 4 ? k : 0)
    if (ch === 'b') L.push(ring(cx), stem(cx - r, top, base + w / 2))
    if (ch === 'a') L.push(ring(cx), stem(cx + r, cy - r - w / 2, base + w / 2))
    if (ch === 'd') L.push(ring(cx), stem(cx + r, top, base + w / 2))
    if (ch === 'c') L.push(arc(cx, 42, -42))
    if (ch === 'e') L.push(arc(cx, 38, 0), `<line x1="${f(cx - r)}" y1="${f(cy)}" x2="${f(cx + r + w / 2)}" y2="${f(cy)}"/>`)
    if (ch === 'o') o = `<circle cx="${f(cx)}" cy="${f(cy)}" r="${f(r + w / 2)}" fill="${SET.red}"/>`
  })
  const svg = `<g fill="none" stroke="${ink}" stroke-width="${f(w)}">${L.join('')}</g>${o}`
  return { svg, box: [x0, top, x0 + 7 * step - r * SET.tr - k, base + w / 2] }
}
const doc = ([x, y, w, h], body, bg) =>
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${[x, y, w, h].map(f).join(' ')}" role="img"><title>BadCode</title>\n` +
  (bg ? `<rect x="${f(x)}" y="${f(y)}" width="${f(w)}" height="${f(h)}" fill="${bg}"/>\n` : '') + body + '\n</svg>\n'
const pad = ([x0, y0, x1, y1], p) => [x0 - p, y0 - p, x1 - x0 + 2 * p, y1 - y0 + 2 * p]
const files = []
const write = (name, s) => { writeFileSync(join(OUT, name), s); files.push(name) }
const png = async (name, svgText, width) => { await sharp(Buffer.from(svgText), { density: 300 }).resize(width).png().toFile(join(OUT, name)); files.push(name) }

// ---- the icon (transparent; -reversed = light ring for dark grounds)
const R = 100
write('badcode-mark.svg', doc(pad([-R, -R, R, R], 8), icon(0, 0, R, INK.dark)))
write('badcode-mark-reversed.svg', doc(pad([-R, -R, R, R], 8), icon(0, 0, R, INK.light)))

// ---- the name
{ const m = word(0, 0, 30, INK.dark), p = pad(m.box, 12)
  write('badcode-wordmark.svg', doc(p, m.svg))
  write('badcode-wordmark-reversed.svg', doc(p, word(0, 0, 30, INK.light).svg)) }

// ---- lock-ups: side by side (everyday) and stacked (sleeves, posters)
function side(ink) {
  const r = 15, m = word(0, 0, r, ink), IR = 30, gap = 26, x = 2 * IR + gap
  const body = icon(IR, 0, IR, ink) + `<g transform="translate(${x} ${r})">${m.svg}</g>`
  return doc(pad([0, -IR, x + m.box[2], IR], 8), body)
}
function stacked(ink) {
  const r = 11, m = word(0, 0, r, ink), IR = 82, wx = -m.box[2] / 2, base = IR + 44 + 3.1 * r
  const body = icon(0, 0, IR, ink) + `<g transform="translate(${f(wx)} ${f(base)})">${m.svg}</g>`
  return doc(pad([Math.min(-IR, wx), -IR, Math.max(IR, -wx), base + m.box[3]], 10), body)
}
write('badcode-lockup.svg', side(INK.dark)); write('badcode-lockup-reversed.svg', side(INK.light))
write('badcode-stacked.svg', stacked(INK.dark)); write('badcode-stacked-reversed.svg', stacked(INK.light))

// ---- favicon + avatar: the icon on its own near-black disc/square, so it reads on any tab bar or app.
// Small-size floors: line >= 1.5px always; at 48px and under (the favicon cut) the dot grows to
// >= 13% of the canvas, or at 16px it shrinks to a speck (checked 2026-09-29).
const badgeSVG = (z, shape) => doc([0, 0, z, z],
  (shape === 'disc' ? `<circle cx="${z / 2}" cy="${z / 2}" r="${z / 2}" fill="${GROUND}"/>` : `<rect width="${z}" height="${z}" fill="${GROUND}"/>`) +
  icon(z / 2, z / 2, z * 0.4, INK.light, 1.5, z <= 48 ? z * 0.13 : 0))
write('favicon.svg', badgeSVG(32, 'disc'))
for (const z of [16, 32, 48, 180]) await png(`favicon-${z}.png`, badgeSVG(z, 'disc'), z)
write('avatar.svg', badgeSVG(1024, 'square'))
await png('avatar-1024.png', badgeSVG(1024, 'square'), 1024)
await png('badcode-wordmark-2400.png', readFileSync(join(OUT, 'badcode-wordmark.svg'), 'utf8'), 2400)
await png('badcode-wordmark-reversed-2400.png', readFileSync(join(OUT, 'badcode-wordmark-reversed.svg'), 'utf8'), 2400)
await png('badcode-stacked-reversed-2400.png', readFileSync(join(OUT, 'badcode-stacked-reversed.svg'), 'utf8'), 2400)

// favicon.ico — PNG-in-ICO (16, 32, 48), which every current browser reads
{ const imgs = [16, 32, 48].map(z => ({ z, b: readFileSync(join(OUT, `favicon-${z}.png`)) }))
  const head = Buffer.alloc(6 + 16 * imgs.length); head.writeUInt16LE(0, 0); head.writeUInt16LE(1, 2); head.writeUInt16LE(imgs.length, 4)
  let off = head.length
  imgs.forEach(({ z, b }, i) => { const e = 6 + 16 * i; head[e] = z; head[e + 1] = z; head.writeUInt16LE(1, e + 4); head.writeUInt16LE(32, e + 6); head.writeUInt32LE(b.length, e + 8); head.writeUInt32LE(off, e + 12); off += b.length })
  writeFileSync(join(OUT, 'favicon.ico'), Buffer.concat([head, ...imgs.map(x => x.b)])); files.push('favicon.ico') }

console.log(files.join('\n'))
