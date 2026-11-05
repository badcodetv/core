// The BadCode government's manifesto, read at build time from docs/government/manifesto/.
// Each file is NN-<post>.md: front matter (title, line) then a markdown body. The cabinet in Bob
// writes them; a merge to main redeploys the site (design/2026-11-05-site-government.md).
import { readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

export function parseFrontMatter(text) {
  const m = String(text).match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  if (!m) return { meta: {}, body: String(text).trim() };
  const meta = {};
  for (const l of m[1].split('\n')) {
    const i = l.indexOf(':');
    if (i > 0) meta[l.slice(0, i).trim()] = l.slice(i + 1).trim();
  }
  return { meta, body: m[2].trim() };
}

export function readManifesto(dir) {
  return readdirSync(dir).filter(f => /^\d\d-[a-z-]+\.md$/.test(f)).sort().map(f => {
    const { meta, body } = parseFrontMatter(readFileSync(join(dir, f), 'utf8'));
    for (const k of ['title', 'line']) if (!meta[k]) throw new Error(`manifesto: ${f} has no ${k}`);
    return { post: f.slice(3, -3), title: meta.title, line: meta.line, body };
  });
}

const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

// Escaped text only: "## x" becomes <h2>, every other blank-line block a <p>. No raw HTML passes.
export function bodyHtml(body) {
  return String(body).split(/\n\s*\n/).map(b => b.trim()).filter(Boolean)
    .map(b => (b.startsWith('## ') ? `<h2>${esc(b.slice(3))}</h2>` : `<p>${esc(b.replace(/\s*\n\s*/g, ' '))}</p>`)).join('');
}
