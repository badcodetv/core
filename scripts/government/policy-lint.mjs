#!/usr/bin/env node
// Lint the government's policy files: node scripts/government/policy-lint.mjs [--today YYYY-MM-DD]
// Fails (exit 1) on any error; prints "Not ready" drafts and warnings without failing.
// Rules: docs/government/policies/README.md.
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { readPolicies, lintPolicies, POSTS } from '../../apps/site/policies.mjs';
import { readManifesto } from '../../apps/site/manifesto.mjs';

export function lintAll(root, opts = {}) {
  const gov = join(root, 'docs', 'government');
  const policies = readPolicies(join(gov, 'policies'));
  const res = lintPolicies(policies, opts);
  const pages = readManifesto(join(gov, 'manifesto'));
  const listed = new Map();
  for (const page of pages) {
    for (const id of String(page.policies).split(/\s*[;,]\s*/).filter(Boolean)) {
      if (!policies.some(p => p.meta.id === id)) res.errors.push(`manifesto/${page.post}: lists ${id}, which does not exist`);
      if (!id.startsWith(`${page.post}/`)) res.errors.push(`manifesto/${page.post}: lists ${id}, which another minister owns`);
      if (listed.has(id)) res.errors.push(`manifesto/${page.post}: ${id} is already listed by ${listed.get(id)}`);
      listed.set(id, page.post);
    }
  }
  if (policies.length) {
    for (const p of policies) if (p.meta.status !== 'dropped' && p.meta.id && !listed.has(p.meta.id))
      res.warnings.push(`${p.file}: on no manifesto page`);
    for (const post of POSTS) if (!policies.some(p => p.meta.owner === post))
      res.warnings.push(`${post}: owns no policies`);
  }
  return { ...res, count: policies.length };
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const i = process.argv.indexOf('--today');
  const opts = i > 0 ? { today: process.argv[i + 1] } : {};
  const root = join(dirname(fileURLToPath(import.meta.url)), '..', '..');
  const { errors, warnings, notReady, count } = lintAll(root, opts);
  for (const [id, miss] of notReady) console.log(`Not ready: ${id} (missing ${miss.join(', ')})`);
  for (const w of warnings) console.log(`warning: ${w}`);
  for (const e of errors) console.error(`error: ${e}`);
  console.log(`${count} policies, ${notReady.size} not ready, ${warnings.length} warnings, ${errors.length} errors`);
  process.exit(errors.length ? 1 : 0);
}
