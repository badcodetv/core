/**
 * Pure helpers for reading Flow's compose bars. Both surfaces (project canvas and character
 * editor) share these quirks, and both are easy to get subtly wrong, so they live here with
 * tests rather than inline in the client.
 */

/** Placeholder text Flow renders INSIDE an empty contenteditable, across all compose surfaces. */
const PLACEHOLDER_RE =
  /(What do you want to (create|change)\?|Describe body and outfit[.…]*|Describe your character[.…]*)/g

/** Zero-width characters the editor leaves behind after clearing. */
const INVISIBLE_RE = /[​﻿]/g

/**
 * True when the prompt box holds no user text. An empty contenteditable still reports its
 * placeholder in textContent, and the placeholder differs per surface — treating that as
 * content makes a submit look like it never fired.
 */
export function isBoxCleared(textContent: string | null): boolean {
  return (textContent ?? '').replace(INVISIBLE_RE, '').replace(PLACEHOLDER_RE, '').trim() === ''
}

/** Escape a string for embedding as a literal match inside a RegExp. */
export function escapeRegExp(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
}

/**
 * True when a model-picker label already names `model`.
 *
 * The labels concatenate without separators ("🍌 Nano Banana 2crop_16_91x"), and "Nano Banana 2"
 * is a strict prefix of "Nano Banana 2 Lite" — so a naive substring test would report the Lite
 * model as already-selected and silently generate on the wrong tier.
 */
export function modelAlreadySelected(label: string | null, model: string): boolean {
  return new RegExp(`${escapeRegExp(model)}(?![\\w ]*Lite)`, 'i').test(label ?? '')
}

/**
 * The video model names exactly as Flow's Settings menu renders them, captured live
 * 2026-08-12. Note the ` - ` separators and the SPACE before `[Lower Priority]`; both had
 * been guessed wrong, and both matter (see canonicalVideoModel / videoModelAlreadySelected).
 */
export const VIDEO_MODELS = [
  'Omni Flash',
  'Veo 3.1 - Lite',
  'Veo 3.1 - Fast',
  'Veo 3.1 - Quality',
  'Veo 3.1 - Lite [Lower Priority]',
] as const

const normaliseModel = (s: string): string => s.toLowerCase().replace(/[^a-z0-9]/g, '')

/**
 * Resolve a loosely-written model name to the exact label Flow's menu shows.
 *
 * Callers, docs and env vars all say "Veo 3.1 Fast" while the menu says "Veo 3.1 - Fast", and
 * an exact-match click on the former simply never finds anything: that is precisely how a
 * request for a specific model turned into a 90s hang. Comparing with punctuation and case
 * stripped makes every reasonable spelling work while keeping the CLICK target exact.
 *
 * An unrecognised name is returned unchanged rather than rejected, so a model Flow adds
 * tomorrow still works without a code change.
 */
export function canonicalVideoModel(model: string): string {
  const want = normaliseModel(model)
  return VIDEO_MODELS.find(m => normaliseModel(m) === want) ?? model
}

/**
 * True when the Settings-panel model trigger already shows `model` selected.
 *
 * Compares for EQUALITY against the canonical name rather than searching for a substring,
 * which is what finally kills the "Veo 3.1 - Lite" ⊂ "Veo 3.1 - Lite [Lower Priority]" prefix
 * trap: no lookahead can be tuned well enough to survive both that suffix and the trigger's
 * own glued-on "arrow_drop_down". The previous attempt failed in both directions at once —
 * it accepted Lower Priority as Lite (the suffix has a leading SPACE, which the guard let
 * through), and it rejected every genuine match (the trigger renders
 * "Omni Flasharrow_drop_down", so the guard's "no trailing word character" rule always
 * fired). The second bug hid the first: nothing ever short-circuited, so nothing was ever
 * wrongly kept.
 */
export function videoModelAlreadySelected(label: string | null, model: string): boolean {
  const shown = (label ?? '').replace(/arrow_drop_down\s*$/i, '').trim()
  return normaliseModel(shown) === normaliseModel(canonicalVideoModel(model))
}

/**
 * Map an aspect ratio like "16:9" to the Material-icon ligature Flow's compose-bar CONFIG
 * TRIGGER renders for it.
 *
 * The compose popover offers exactly five image ratios, and all five ligatures are now CONFIRMED
 * live (2026-08-12, smoke-compose-popover.ts, which dumps each tab as "<ligature><ratio text>"):
 * 16:9 -> `crop_16_9`, 9:16 -> `crop_9_16`, 4:3 -> `crop_landscape`, 3:4 -> `crop_portrait`,
 * 1:1 -> `crop_square`. Note the pattern is NOT uniform: the two wide/tall ratios spell the
 * numbers out with an underscore, the other three use descriptive Material Symbols names. `1:1`
 * was previously derived as `crop_1_1` by the numeric rule and matched nothing — harmless (the
 * short-circuit just never fired, so the menu reopened every time) but wrong.
 *
 * Any ratio outside that set falls back to the numeric rule. Flow does not currently offer one.
 */
function aspectIcon(aspect: string): string {
  if (aspect === '4:3') return 'crop_landscape'
  if (aspect === '3:4') return 'crop_portrait'
  if (aspect === '1:1') return 'crop_square'
  return `crop_${aspect.replace(':', '_')}`
}

/**
 * True when the (collapsed) config-trigger label already shows `aspect` selected.
 *
 * Unlike `modelAlreadySelected`, the trigger does NOT carry the human-readable ratio text at
 * all — confirmed live it concatenates as "🍌 Nano Banana 2crop_16_91x": icon ligature name
 * then the count, straight through, no colon anywhere (see `ensureImageMode`'s short-circuit
 * comment in flow-client.ts). So this matches on the derived icon name instead of the ratio text.
 *
 * No negative-lookahead guard here, unlike `modelAlreadySelected`/`videoModelAlreadySelected` —
 * and that omission is deliberate, not an oversight. The count tab's digits sit immediately
 * after the icon name with no separator ("crop_16_9" + "1x" = "crop_16_91x"), so a lookahead
 * that rejects trailing word characters (the shape that guards the real "Nano Banana 2" vs
 * "Nano Banana 2 Lite" bug) would reject the count digits too and this would never
 * short-circuit at all — it would always reopen the menu, which is safe but pointless. It's
 * safe to skip the guard: none of the derived icon names in Flow's aspect set are a strict
 * prefix of another (`crop_16_9` / `crop_9_16` / `crop_1_1` / `crop_21_9` / … all diverge at
 * their first digit), so there is no equivalent of the Lite trap to guard against here — the
 * tests below exist to PROVE that for the pairs called out in the task, not to assume it.
 */
export function aspectAlreadySelected(label: string | null, aspect: string): boolean {
  return new RegExp(escapeRegExp(aspectIcon(aspect)), 'i').test(label ?? '')
}
