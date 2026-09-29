// Builds the BadCode brace logo files from the round-4 tuner settings Kai picked (2026-09-13).
// Usage (from a scratch dir with `npm i opentype.js@1.3.4`):
//   curl -L -o PlexMono-SemiBold.ttf https://github.com/google/fonts/raw/main/ofl/ibmplexmono/IBMPlexMono-SemiBold.ttf
//   node build-logo.mjs <repo>/docs/brand/logo PlexMono-SemiBold.ttf
// PNGs are then rendered from the SVGs with headless Chrome (see docs/brand/README.md).
import opentype from 'opentype.js';
import { mkdirSync, writeFileSync } from 'node:fs';

const OUT = process.argv[2];
mkdirSync(OUT, { recursive: true });

const SET = { depth: 0.59, point: 0.54, dot: 0.5, red: '#cc2b37', blue: '#2696d4' };
const font = opentype.loadSync(process.argv[3]);
const f = n => +n.toFixed(2);

// Same geometry as the tuner: point at x=0, height H, tips at x=D.
function brace(H, sw, ink) {
  const D = SET.depth * H, s = SET.point * D;
  const m = Math.min(s * 0.9, H * 0.16);
  const c = Math.min(Math.max(D - s, 4) * 0.9, H / 2 - m);
  const top = `M${f(D)} 0C${f(s + (D - s) * 0.45)} 0 ${f(s)} ${f(c * 0.55)} ${f(s)} ${f(c)}V${f(H / 2 - m)}C${f(s)} ${f(H / 2 - m * 0.45)} ${f(s * 0.45)} ${f(H / 2)} 0 ${f(H / 2)}`;
  const bot = `M${f(D)} ${f(H)}C${f(s + (D - s) * 0.45)} ${f(H)} ${f(s)} ${f(H - c * 0.55)} ${f(s)} ${f(H - c)}V${f(H / 2 + m)}C${f(s)} ${f(H / 2 + m * 0.45)} ${f(s * 0.45)} ${f(H / 2)} 0 ${f(H / 2)}`;
  const r = Math.max(SET.dot * sw, sw / 2);
  const inkAttr = ink ? `stroke="${ink}"` : 'class="ink"';
  const svg = `<g fill="none" ${inkAttr} stroke-width="${f(sw)}" stroke-linecap="round" stroke-linejoin="round"><path d="${top}"/><path d="${bot}"/></g>` +
    `<circle cx="${f(D)}" cy="0" r="${f(r)}" fill="${SET.red}"/><circle cx="${f(D)}" cy="${f(H)}" r="${f(r)}" fill="${SET.blue}"/>`;
  return { D, r, svg, box: [-sw / 2, -Math.max(r, sw / 2), D + Math.max(r, sw / 2), H + Math.max(r, sw / 2)] };
}

const doc = (vb, body, extra = '') =>
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="${vb.map(f).join(' ')}"${extra}>\n${body}\n</svg>\n`;

function squareVB([x0, y0, x1, y1], padFrac) {
  const side = Math.max(x1 - x0, y1 - y0) * (1 + padFrac * 2);
  return [(x0 + x1) / 2 - side / 2, (y0 + y1) / 2 - side / 2, side, side];
}

// ---- Mark (the brace on its own) ----
function mark(ink, sw = 8.5, pad = 0.08) {
  const b = brace(60, sw, ink);
  return doc(squareVB(b.box, pad), `<title>BadCode</title>${b.svg}`, ' role="img"');
}
writeFileSync(`${OUT}/badcode-mark.svg`, mark('#000'));
writeFileSync(`${OUT}/badcode-mark-reversed.svg`, mark('#fff'));

// ---- Favicon: heavier line for small sizes; ink follows the browser's theme ----
{
  const b = brace(60, 13, null);
  const style = `<style>.ink{stroke:#000}@media (prefers-color-scheme:dark){.ink{stroke:#fff}}</style>`;
  writeFileSync(`${OUT}/favicon.svg`, doc(squareVB(b.box, 0.04), `${style}${b.svg}`));
}

// ---- Wordmark: "Bad" + brace at cap height + "ode", lettering outlined from IBM Plex Mono SemiBold ----
function wordmark(ink) {
  const capH = 70, sw = 11, baseline = 130, H = capH - sw;
  const b = brace(H, sw, ink);
  const bx = 3 * 60 + 8 + sw / 2, by = baseline - capH + sw / 2;
  const odeX = bx + b.D + Math.max(b.r, sw / 2) + 6;
  const bad = font.getPath('Bad', 0, baseline, 100), ode = font.getPath('ode', odeX, baseline, 100);
  const bb1 = bad.getBoundingBox(), bb2 = ode.getBoundingBox();
  const x0 = bb1.x1, x1 = bb2.x2;
  const y0 = Math.min(bb1.y1, bb2.y1, by + b.box[1]), y1 = Math.max(bb1.y2, bb2.y2, by + b.box[3]);
  const pad = 6;
  const body = `<title>BadCode</title><g fill="${ink}"><path d="${bad.toPathData(2)}"/><path d="${ode.toPathData(2)}"/></g>` +
    `<g transform="translate(${f(bx)} ${f(by)})">${b.svg}</g>`;
  return doc([x0 - pad, y0 - pad, x1 - x0 + pad * 2, y1 - y0 + pad * 2], body, ' role="img"');
}
writeFileSync(`${OUT}/badcode-wordmark.svg`, wordmark('#000'));
writeFileSync(`${OUT}/badcode-wordmark-reversed.svg`, wordmark('#fff'));

// ---- Avatar sources (square, ground painted, mark centred with room for a circle crop) ----
for (const [name, ground, ink] of [['avatar', '#fff', '#000'], ['avatar-reversed', '#000', '#fff']]) {
  const b = brace(60, 10, ink);
  const vb = squareVB(b.box, 0.42);
  writeFileSync(`${OUT}/${name}.svg`, doc(vb, `<rect x="${f(vb[0])}" y="${f(vb[1])}" width="${f(vb[2])}" height="${f(vb[3])}" fill="${ground}"/>${b.svg}`));
}
console.log('ok');
