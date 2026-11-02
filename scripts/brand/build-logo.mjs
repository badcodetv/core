// Builds the BadCode logo files — the red triangle in the ring — from the settings Kai saved on the logo bench (2026-10-15).
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

// Bench save 2f6bogo164mzzi4lzz00 ("Saved version 5"), 2026-10-19 14:40 — Kai: "I'm just going to say that's our logo".
// The ring is 15% (was 8% on save b0dhojp15efdyw7rboj6, 2026-10-15); the name's o is the bench's "Solid red o" —
// a solid red circle, not a bare triangle (it "reads as an A") and no longer the ring + triangle.
// The ring-with-dot it replaced is in docs/brand/archive/2026-09-29-dot/ (generator: archive/build-logo-dot.mjs).
const SET = {
  ring: 0.15,    // ring line thickness, as a fraction of the ring's radius
  tSize: 0.36,   // triangle size: centre to corner, as a fraction of the ring's radius
  tPush: 0.61,   // how far off centre: 0 = centre, 1 = touching the inside of the ring
  tAngle: 55,    // which way it sits: degrees clockwise from 12 o'clock (about 2 o'clock)
  tRot: 55,      // which way it points: degrees clockwise from 12 o'clock
  tRound: 0.55,  // corner rounding, as a share of the most possible (the inradius)
  red: '#cc2b37',
  lw: 0.30,      // letter line weight, as a fraction of letter radius
  tr: 0.26,      // letter spacing, as a fraction of letter radius
  ck: 0.35,      // the c pulled toward the red o (optical kerning), fraction of letter radius
}
const INK = { dark: '#0a0a0a', light: '#eef3f6' }, GROUND = '#050607'
const f = n => +n.toFixed(2)

// ---- geometry (identical to the bench)
// Triangle path: r = centre-to-corner, rc = corner radius, rot = where the first corner points.
function triPath(x, y, r, rc, rot) {
  const V = [0, 1, 2].map(k => { const a = (rot + k * 120) * Math.PI / 180; return [x + r * Math.sin(a), y - r * Math.cos(a)] })
  if (rc <= 1e-6) return `M${V.map(p => p.map(f).join(' ')).join('L')}Z`
  const t = rc / r, lerp = (A, B) => [A[0] + (B[0] - A[0]) * t, A[1] + (B[1] - A[1]) * t].map(f).join(' ')
  let d = ''
  for (let k = 0; k < 3; k++) { const Vk = V[k], P = V[(k + 2) % 3], N = V[(k + 1) % 3]; d += `${k ? 'L' : 'M'}${lerp(Vk, P)}A${f(rc)} ${f(rc)} 0 0 1 ${lerp(Vk, N)}` }
  return d + 'Z'
}
// minSize: the small-size floor — the triangle's corner reach never drops below 2 x minSize.
function icon(cx, cy, R, ink, minW = 0, minSize = 0, ring = SET.ring) {
  const w = Math.max(ring * R, minW), r = SET.tSize * R, rc = SET.tRound * r / 2
  const room = Math.max(0, R - w / 2 - (r - rc) - R * 0.02), d = SET.tPush * room, a = SET.tAngle * Math.PI / 180
  const rr = Math.max(r, minSize * 2), k = rr / r
  return `<circle cx="${f(cx)}" cy="${f(cy)}" r="${f(R - w / 2)}" fill="none" stroke="${ink}" stroke-width="${f(w)}"/>` +
    `<path d="${triPath(cx + d * Math.sin(a), cy - d * Math.cos(a), rr, rc * k, SET.tRot)}" fill="${SET.red}"/>`
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
    // the o is a solid red circle, the letters' full outer size (Kai, 2026-10-19, bench save 5)
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

// ---- favicon + avatar: the icon on its own near-black disc/square, so it reads on any tab bar or app.  style-lint: ok (the logo is global)
// Small-size floors: line >= 1.5px always; at 48px and under (the favicon cut) the dot grows to
// >= 13% of the canvas, or at 16px it shrinks to a speck (checked 2026-09-29 for the dot; same floor
// for the triangle, applied the bench's way: its corner reach is at least twice the floor).
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
