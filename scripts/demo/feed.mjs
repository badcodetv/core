// Builds the demo page's feed: every valid published day (newest first), the government folded from
// them, and the scoreboard. Invalid or unfinished files are left out and listed, never shown half-made.
import { validateDay, scoreAnswers, bestAnswer } from './issue.mjs';
import { foldGovernment } from './government.mjs';

export function buildDemoFeed(dayDocs, govDocs, cabinet, { today } = {}) {
  const days = [], skipped = [];
  for (const d of dayDocs) {
    const { errors } = validateDay(d, { today });
    if (errors.length) { skipped.push({ id: d?.id ?? '?', errors }); continue; }
    if (d.stage !== 'published') { skipped.push({ id: d.id, errors: [`not published yet (stage ${d.stage})`] }); continue; }
    days.push({ ...d, scores: scoreAnswers(d), best: bestAnswer(d) });
  }
  days.sort((a, b) => b.run.news_date.localeCompare(a.run.news_date) || b.id.localeCompare(a.id));
  const gov = foldGovernment(new Map(days.map((d) => [d.id, d])), govDocs);
  for (const s of gov.skipped) skipped.push({ id: `government ${s.date}`, errors: s.errors });
  const preds = days.flatMap((d) => d.predictions.map((p) => ({ day: d.id, short: d.case.short, area: d.plan.area, ...p })));
  const count = (r) => preds.filter((p) => p.result === r).length;
  const endings = Object.fromEntries(['accepted', 'partly', 'rejected'].map((e) => [e, days.filter((d) => d.ending === e).length]));
  return {
    schema: 'fp-demo-feed/1',
    built: today,
    days,
    skipped,
    endings,
    government: {
      ministers: cabinet.ministers,
      lines: gov.lines,
      debates: gov.applied.sort((a, b) => b.date.localeCompare(a.date)),
    },
    scoreboard: {
      total: preds.length,
      pending: count('pending'),
      hit: count('hit'),
      miss: count('miss'),
      void: count('void'),
      next_due: preds.filter((p) => p.result === 'pending').sort((a, b) => a.due.localeCompare(b.due)).slice(0, 12),
    },
  };
}
