// take-row.mts — pure helpers for suno.mts (no browser, no I/O), unit-tested in take-row.test.mts.
// This module must import NOTHING from suno.mts: suno.mts imports from here, and pulling it in would
// drag Playwright into every test. Later tickets add more helpers here.

/** A Suno duration string → seconds. Accepts 'M:SS' / 'MM:SS' and 'H:MM:SS'; throws on anything else. */
export function durToSeconds(dur: string): number {
  const s = dur.trim()
  const m = /^(?:(\d+):([0-5]\d)|(\d+)):([0-5]\d)$/.exec(s)
  if (!m) throw new Error(`durToSeconds: not a M:SS or H:MM:SS duration: ${JSON.stringify(dur)}`)
  const [, h, mm, mOnly, ss] = m
  return h !== undefined
    ? Number(h) * 3600 + Number(mm) * 60 + Number(ss)
    : Number(mOnly) * 60 + Number(ss)
}
