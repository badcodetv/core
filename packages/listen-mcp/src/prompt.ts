/**
 * The exact instruction sent to Gemini: the lens, then the facts we measured locally, then the
 * caller's question, then the headings to answer under.
 *
 * Measured facts are stated as things not to contradict, because a model that hears a 16 kbps
 * mono copy is worse at tempo and loudness than a meter. Tempo goes in only when two detectors
 * agreed on it (TRUSTED_TEMPO) — a wrong "fact" would do more harm than none. Stereo numbers are
 * never sent: Gemini hears mono, so it could only parrot them.
 *
 * 🔑 `sunoBoxes` is what turns a description into a LOOP (Kai, 2026-09-12). Handing over the
 * prompt that produced the audio lets the answer be a *diff* — desired versus actual — instead of
 * a review, and a diff is the thing the next prompt edit can be derived from. It is opt-in
 * because it only makes sense with the `suno-diff` lens; a plain `music` describe must not see it.
 *
 * 🔴 It also creates the failure mode the lens is written against: a model holding the prompt
 * will happily confirm whatever the prompt claims. The warning below is deliberately blunt and is
 * repeated after the boxes, which is the last thing read before the headings.
 */
import type { Lens, Measurements, SunoBoxes } from './types'

export const TRUSTED_TEMPO: ReadonlySet<string> = new Set(['high', 'fair', 'tempo-only'])

export function buildPrompt(input: {
  lens: Lens
  measurements: Measurements
  question?: string
  rangeLabel?: string
  sunoBoxes?: SunoBoxes
}): string {
  const { lens, measurements: m, question, rangeLabel, sunoBoxes } = input
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
  if (sunoBoxes) parts.push(renderSunoBoxes(sunoBoxes))
  if (question && question.trim()) parts.push(`EXTRA QUESTION:\n${question}`)
  parts.push(`Answer using exactly these headings, in order:\n${lens.headings.map((h) => `## ${h}`).join('\n')}`)
  return parts.join('\n\n')
}

/**
 * The prompt that produced the audio, as the diff's left-hand side. Order matters: Style, then
 * Exclude, then Lyrics — the same order as the create form, so a reader can follow it box by box.
 * Empty boxes are labelled rather than omitted, because "there was no exclude list" is itself a
 * finding (a stale or missing ban is one of our most common faults).
 */
export function renderSunoBoxes(b: SunoBoxes): string {
  const box = (label: string, text: string | undefined, note = '') => {
    const body = (text ?? '').trim()
    if (!body) return `## ${label}\n(empty — nothing was given to Suno in this box.)`
    return `## ${label}${note}\n\`\`\`\n${body}\n\`\`\``
  }
  const head = [
    'THE PROMPT THAT PRODUCED THIS AUDIO.',
    'These are the boxes that went into Suno. Diff the audio against them, box by box.',
    '',
    '🔴 Holding the prompt makes it very easy to describe what you were told to expect rather',
    'than what you hear. If you cannot hear a clause, the answer is "absent" — even where the',
    'prompt is emphatic. Confirming a clause you cannot actually hear costs a paid round and',
    'sends the next one the wrong way.',
  ].join('\n')
  const parts = [
    head,
    box('Style box', b.style, b.style ? ` (${b.style.trim().length} characters)` : ''),
    box('Exclude box', b.exclude),
  ]
  if (b.lyrics !== undefined) {
    parts.push(box('Lyrics box', b.lyrics, ' (bracketed lines are section directions, not sung words)'))
  }
  if (b.settings) parts.push(`## Settings\n${b.settings.trim()}`)
  return parts.join('\n\n')
}
