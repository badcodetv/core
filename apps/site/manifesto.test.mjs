import { describe, it, expect } from 'vitest';
import { mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { parseFrontMatter, readManifesto, bodyHtml } from './manifesto.mjs';

const dir = files => { const d = mkdtempSync(join(tmpdir(), 'manifesto-')); for (const [n, t] of Object.entries(files)) writeFileSync(join(d, n), t); return d; };

describe('parseFrontMatter', () => {
  it('splits keys on the first colon only and returns the body', () => {
    const { meta, body } = parseFrontMatter('---\ntitle: Chancellor of the Exchequer\nline: A time: now\n---\n\n## Position\n\nText.\n');
    expect(meta).toEqual({ title: 'Chancellor of the Exchequer', line: 'A time: now' });
    expect(body).toBe('## Position\n\nText.');
  });
  it('treats a file without front matter as all body', () => {
    expect(parseFrontMatter('just text')).toEqual({ meta: {}, body: 'just text' });
  });
});

describe('readManifesto', () => {
  it('reads NN-<post>.md in file order', () => {
    const d = dir({
      '01-chancellor.md': '---\ntitle: Chancellor\nline: Ledger.\n---\nBody C',
      '00-prime-minister.md': '---\ntitle: Prime Minister\nline: Promise.\n---\nBody P',
      'README.txt': 'ignored',
    });
    expect(readManifesto(d)).toEqual([
      { post: 'prime-minister', title: 'Prime Minister', line: 'Promise.', body: 'Body P' },
      { post: 'chancellor', title: 'Chancellor', line: 'Ledger.', body: 'Body C' },
    ]);
  });
  it('throws on a file with no title or line', () => {
    expect(() => readManifesto(dir({ '02-foreign.md': '---\nline: x\n---\n' }))).toThrow(/02-foreign\.md.*title/);
    expect(() => readManifesto(dir({ '02-foreign.md': '---\ntitle: x\n---\n' }))).toThrow(/line/);
  });
});

describe('bodyHtml', () => {
  it('escapes text, makes ## headings h2 and blank-line paragraphs p', () => {
    expect(bodyHtml('## Position\n\nTax <b>wealth</b>\nnow.\n\n- one')).toBe('<h2>Position</h2><p>Tax &lt;b&gt;wealth&lt;/b&gt; now.</p><p>- one</p>');
  });
});
