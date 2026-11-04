#!/usr/bin/env node
// Builds badcode.tv (Channel BadCode) into apps/site/dist. No dependencies: plain Node.
//   node apps/site/build.mjs
// public/ is copied as-is (stills, logo, favicons); every address the TV can show gets its own
// index.html with its own title, description and link-preview picture, plus a plain-text copy of
// what is on screen for screen readers and search engines. Content: src/content.json.
import { readFileSync, writeFileSync, mkdirSync, rmSync, cpSync, existsSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const src = join(here, 'src'), pub = join(here, 'public'), dist = join(here, 'dist');
const C = JSON.parse(readFileSync(join(src, 'content.json'), 'utf8'));
const tpl = readFileSync(join(src, 'page.html'), 'utf8');
const css = readFileSync(join(src, 'tv.css'), 'utf8'), js = readFileSync(join(src, 'tv.js'), 'utf8');
const V = createHash('sha256').update(css + js + JSON.stringify(C)).digest('hex').slice(0, 10);
const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const O = C.origin, S = C.stories, G = C.government, N = C.news, A = C.about;
const DEFAULT_IMG = O + '/avatar-1024.png';
const SITE_DESC = `${A.lede} ${A.request.replace('fuck', 'f***')} Stories, the news, and a party of its own.`;

// the plain-text page under each address
const nav = `<nav aria-label="Channels"><ul>
<li><a href="/stories">Stories</a>: ${S.map((s, i) => `<a href="/stories/${i + 1}">${esc(s.title)}</a>`).join(', ')}. Songs: ${S.map((s, i) => `<a href="/stories/${i + 5}">${esc(s.song)}</a>`).join(', ')}.</li>
<li><a href="/news">News: ${esc(N.title)}</a></li>
<li><a href="/government">The BadCode Government</a> and <a href="/government/2">Future Proof</a></li>
<li><a href="/about">About BadCode</a> and <a href="/text/100">BadCode Text</a></li>
</ul></nav>`;
const follow = `<h2>Follow BadCode</h2><ul>${C.socials.map(s => `<li>${s.url ? `<a href="${esc(s.url)}">${esc(s.name)}</a>` : `${esc(s.name)} (soon)`}</li>`).join('')}</ul><p>${esc(A.ai)}</p><p>${esc(A.sign)} &copy; 2026 BadCode</p>`;
const story = (s, i) => `<article><h2>${esc(s.title)}</h2><p>${esc(s.blurb)}</p><p>Film: ${s.film ? `<a href="https://www.youtube.com/watch?v=${esc(s.film)}">watch on YouTube</a>` : 'coming to YouTube'}. Song: ${esc(s.song)}.</p></article>`;
const plainBody = {
  home: () => `<h1>BadCode</h1><p>${esc(A.lede)} ${esc(A.request)}</p><p>${esc(A.story)}</p>${S.map(story).join('')}`,
  stories: () => `<h1>Stories</h1>${S.map(story).join('')}`,
  story: i => `<h1>${esc(S[i].title)}</h1>${story(S[i], i)}`,
  song: i => `<h1>${esc(S[i].song)}</h1><p>The song from ${esc(S[i].title)}. ${S[i].songVideo ? `<a href="https://www.youtube.com/watch?v=${esc(S[i].songVideo)}">Watch on YouTube</a>` : 'Coming to YouTube.'}</p>`,
  news: () => `<h1>${esc(N.title)}</h1><p>${esc(N.strap)} ${esc(N.status)}</p><p>${esc(N.signoff)}</p>`,
  gov: () => `<h1>The BadCode Government</h1><p>${esc(G.promise)}</p><ol>${G.pledges.map(p => `<li><strong>${esc(p[0])}</strong> ${esc(p[1])}</li>`).join('')}</ol><p>${esc(G.notReal)}</p>`,
  fp: () => `<h1>Future Proof</h1><p><strong>${esc(G.futureProof.question)}</strong></p><p>${esc(G.futureProof.intro)}</p><ol>${G.futureProof.tenets.map(t => `<li><strong>${esc(t[0])}.</strong> ${esc(t[1])}</li>`).join('')}</ol><p>${esc(G.futureProof.ask)}</p>`,
  about: () => `<h1>About BadCode</h1><p>${esc(A.lede)} ${esc(A.request)}</p><p>${esc(A.story)}</p>`,
  text: () => `<h1>BadCode Text</h1><p>The words of BadCode as teletext pages: 100 index, 200 stories, 300 news, 400 the manifesto, 700 follow, 800 about, 888 Future Proof.</p>`,
  missing: () => `<h1>Page not found</h1><p>We saw you'd try that. <a href="/">Back to the TV.</a></p>`,
};

const routes = [
  { path: '/', title: 'BadCode', desc: SITE_DESC, body: plainBody.home() },
  { path: '/stories', title: 'Stories · BadCode', desc: 'Four films and four songs from BadCode, an AI sent back from a future that went wrong.', body: plainBody.stories() },
  ...S.map((s, i) => ({ path: `/stories/${i + 1}`, title: `${s.title} · BadCode`, desc: s.blurb, img: s.still, body: plainBody.story(i) })),
  ...S.map((s, i) => ({ path: `/stories/${i + 5}`, title: `${s.song} (song) · BadCode`, desc: `The song from ${s.title}.`, img: s.still, body: plainBody.song(i) })),
  { path: '/news', title: `${N.title} · BadCode`, desc: N.strap, body: plainBody.news() },
  { path: '/government', title: 'The BadCode Government', desc: `${G.promise} ${G.notReal}`, body: plainBody.gov() },
  { path: '/government/2', title: 'Future Proof · BadCode', desc: G.futureProof.question, body: plainBody.fp() },
  { path: '/future-proof', canon: '/government/2', title: 'Future Proof · BadCode', desc: G.futureProof.question, body: plainBody.fp() },
  { path: '/about', title: 'About · BadCode', desc: SITE_DESC, body: plainBody.about() },
  ...[100, 200, 201, 202, 203, 204, 300, 400, 700, 800, 888].map(p => ({ path: `/text/${p}`, title: `Page ${p} · BadCode Text`, desc: 'BadCode, as teletext.', body: plainBody.text() })),
];

const slash = p => (p === '/' || p.endsWith('/') ? p : p + '/');
// internal links get the trailing slash too, so Pages never has to redirect
const slashLinks = html => html.replace(/href="(\/(?:stories|news|government|about|text|future-proof)[^"]*?)"/g, (m, h) => `href="${slash(h)}"`);
function pageHtml(r) {
  const img = r.img ? O + r.img : DEFAULT_IMG;
  const fill = { TITLE: esc(r.title), DESC: esc(r.desc), CANON: O + slash(r.canon || r.path), OGIMG: img, V, CONTENT_JSON: JSON.stringify(C).replace(/</g, '\\u003c'), PLAIN: r.body + nav + follow };
  return slashLinks(tpl.replace(/\{\{(\w+)\}\}/g, (m, k) => (k in fill ? fill[k] : m)));
}

rmSync(dist, { recursive: true, force: true });
mkdirSync(dist, { recursive: true });
// public/ holds the static files. The old one-page map (index.html, 404.html, styles.css) and the
// /tv test page are left behind: the TV replaces them.
const SKIP = new Set(['index.html', '404.html', 'styles.css', 'tv']);
cpSync(pub, dist, { recursive: true, filter: p => !SKIP.has(p.slice(pub.length + 1).split('/')[0]) || p === pub });
writeFileSync(join(dist, 'tv.css'), css);
writeFileSync(join(dist, 'tv.js'), js);
for (const r of routes) {
  const file = r.path === '/' ? join(dist, 'index.html') : join(dist, r.path.slice(1), 'index.html');
  mkdirSync(dirname(file), { recursive: true });
  writeFileSync(file, pageHtml(r));
}
writeFileSync(join(dist, '404.html'), pageHtml({ path: '/404', title: 'Page not found · BadCode', desc: SITE_DESC, body: plainBody.missing() }).replace('<meta name="description"', '<meta name="robots" content="noindex">\n<meta name="description"'));
// a short cache for the HTML, a long one for the stills; the version query string busts css/js
writeFileSync(join(dist, '_headers'), `/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n/stills/*\n  Cache-Control: public, max-age=86400\n`);
for (const f of ['avatar-1024.png', 'favicon.svg']) if (!existsSync(join(dist, f))) console.warn('missing', f);
console.log(`built ${routes.length + 1} pages into ${dist} (version ${V})`);
