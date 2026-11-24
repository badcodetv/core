// Drawing by lot (copied from scripts/government/sim/lot.mjs), the same way every time: a seed string gives the same draw on any machine,
// so anyone can rerun it and check nobody picked the citizens or the jury by hand.
// Zero dependencies: Bob workers run it with plain `node`.

/** A small, well-known seeded generator (mulberry32 over an FNV-1a hash of the seed). */
export function rng(seed) {
  let h = 2166136261 >>> 0;
  for (const ch of String(seed)) { h ^= ch.charCodeAt(0); h = Math.imul(h, 16777619) >>> 0; }
  let a = h || 1;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/** Pick k distinct items from a list (partial Fisher–Yates), in draw order. */
export function drawK(list, k, seed) {
  if (k > list.length) throw new Error(`can't draw ${k} from ${list.length}`);
  const r = rng(seed), a = list.slice();
  for (let i = 0; i < k; i++) { const j = i + Math.floor(r() * (a.length - i)); [a[i], a[j]] = [a[j], a[i]]; }
  return a.slice(0, k);
}

/** Pick one key from {key: share} with the given random number. */
export function pick(shares, x) {
  const entries = Object.entries(shares);
  const total = entries.reduce((s, [, v]) => s + v, 0);
  let acc = 0;
  for (const [k, v] of entries) { acc += v / total; if (x < acc) return k; }
  return entries[entries.length - 1][0];
}

/**
 * The draw for one issue: `citizens` people set the tests; the jury is drawn from the REST of the
 * pool, so nobody sets the test and then judges it. Seeds are printed in the issue file.
 */
export function drawForIssue(pool, issueId, { citizens = 100, jury = 12 } = {}) {
  const ids = pool.map((p) => p.id);
  const citizenSeed = `${issueId}/citizens`, jurySeed = `${issueId}/jury`;
  const drawn = drawK(ids, citizens, citizenSeed);
  const rest = ids.filter((id) => !drawn.includes(id));
  return { citizenSeed, citizens: drawn, jurySeed, jury: drawK(rest, jury, jurySeed) };
}
