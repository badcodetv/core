// Builds the page's feed: every valid published issue, newest first, plus the scoreboard.
// Invalid or unfinished files are left out and listed, never shown half-made.
import { validateIssue } from './issue.mjs';

export function buildFeed(docs, { today } = {}) {
  const issues = [], skipped = [];
  for (const d of docs) {
    const { errors } = validateIssue(d, { today });
    if (errors.length) { skipped.push({ id: d?.id ?? '?', errors }); continue; }
    if (d.stage !== 'published') { skipped.push({ id: d.id, errors: [`not published yet (stage ${d.stage})`] }); continue; }
    issues.push(d);
  }
  // newest news first; ties broken by id so the order never wobbles
  issues.sort((a, b) => (b.run.news_date.localeCompare(a.run.news_date)) || b.id.localeCompare(a.id));
  const preds = issues.flatMap((d) => d.predictions.map((p) => ({ issue: d.id, short: d.issue.short, ...p })));
  const count = (r) => preds.filter((p) => p.result === r).length;
  const marked = count('hit') + count('miss');
  return {
    schema: 'fp-sim-feed/1',
    stamp: 'SIMULATED',
    built: today,
    issues,
    skipped,
    scoreboard: {
      total: preds.length,
      pending: count('pending'),
      hit: count('hit'),
      miss: count('miss'),
      void: count('void'),
      hit_rate: marked ? count('hit') / marked : null,
      next_due: preds.filter((p) => p.result === 'pending').sort((a, b) => a.due.localeCompare(b.due)).slice(0, 12),
    },
  };
}
