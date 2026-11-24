import { test } from 'vitest';
import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { demoPage, plainList, readTree, TITLE, DESC } from './demo.mjs';

const here = dirname(fileURLToPath(import.meta.url));
const pagePath = join(here, '..', '..', 'docs', 'demo', 'page', 'index.html');
const frag = existsSync(pagePath) ? readFileSync(pagePath, 'utf8') : '<style></style><main></main><script></script>';
const cabinet = JSON.parse(readFileSync(join(here, '..', '..', 'docs', 'demo', 'cabinet.json'), 'utf8'));
const d = {
  id: '2026-11-10-x', run: { news_date: '2026-11-10' }, ending: 'accepted',
  case: { title: 'A <title>', question: 'Who pays?', place: 'Fernbridge (made up)', story: 'A story.' },
  minister: { minister: 'housing', text: 'Adopted: a repair line.' },
};
const feed = { days: [d], endings: { accepted: 1, partly: 0, rejected: 0 }, government: { ministers: cabinet.ministers, lines: [{ minister: 'housing', live: true, status: 'policy', text: 'Every home gets a repair line.' }] } };

test('the title, description and preview say it is a demo', () => {
  assert.match(TITLE, /Demo/);
  assert.match(DESC, /^A demo/);
  const html = demoPage(frag, feed, { origin: 'https://www.badcode.tv', img: '/demo/preview.png' });
  assert.match(html, /^<!doctype html>/);
  assert.match(html, /<title>Future Proof Demo · BadCode<\/title>/);
  assert.match(html, /og:image" content="https:\/\/www\.badcode\.tv\/demo\/preview\.png"/);
  assert.equal((html.match(/<title>/g) || []).length, 1);
});

test('the plain list escapes text, says demo, and lists the manifestos', () => {
  const p = plainList(feed);
  assert.match(p, /This is a demo/);
  assert.match(p, /A &lt;title&gt;/);
  assert.match(p, /Minister for Housing, Bea Hartwell \(invented\)/);
  assert.match(p, /Every home gets a repair line/);
  assert.match(plainList(null), /This is a demo/);
});

test('the page says "This is a demo" and never calls the citizens "the public"', () => {
  assert.match(frag, /This is a demo/i);
  assert.doesNotMatch(frag.replace(/public sector/gi, ''), /\bthe public\b/i);
});

test('a missing branch gives null, not an error', () => {
  assert.equal(readTree(here, 'refs/heads/no-such-branch-here', 'docs/demo/days'), null);
});
