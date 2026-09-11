/**
 * The exact instruction sent to Gemini: the lens, then the facts we measured locally, then the
 * caller's question, then the headings to answer under.
 *
 * Measured facts are stated as things not to contradict, because a model that hears a 16 kbps
 * mono copy is worse at tempo and loudness than a meter. Tempo goes in only when two detectors
 * agreed on it (TRUSTED_TEMPO) — a wrong "fact" would do more harm than none. Stereo numbers are
 * never sent: Gemini hears mono, so it could only parrot them.
 */
import type { Lens, Measurements } from './types'

export const TRUSTED_TEMPO: ReadonlySet<string> = new Set(['high', 'fair', 'tempo-only'])

export function buildPrompt(input: {
  lens: Lens
  measurements: Measurements
  question?: string
  rangeLabel?: string
}): string {
  const { lens, measurements: m, question, rangeLabel } = input
  const facts = [`- Duration: ${m.durationSec.toFixed(1)} seconds`]
  if (m.integratedLufs !== null) facts.push(`- Integrated loudness: ${m.integratedLufs.toFixed(1)} LUFS`)
  if (m.truePeakDbtp !== null) facts.push(`- True peak: ${m.truePeakDbtp.toFixed(1)} dBTP`)
  if (m.tempo.bpm !== null && TRUSTED_TEMPO.has(m.tempo.confidence)) {
    facts.push(`- Tempo: ${Math.round(m.tempo.bpm)} BPM`)
  }

  const parts = [lens.body.trim(), `MEASURED FACTS — do not contradict these:\n${facts.join('\n')}`]
  if (rangeLabel) {
    parts.push(`This clip is ${rangeLabel} of a longer track; timestamps are relative to the clip start.`)
  }
  if (question && question.trim()) parts.push(`EXTRA QUESTION:\n${question}`)
  parts.push(`Answer using exactly these headings, in order:\n${lens.headings.map((h) => `## ${h}`).join('\n')}`)
  return parts.join('\n\n')
}
