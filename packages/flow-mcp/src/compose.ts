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
 * True when a VIDEO model-picker label already names `model`.
 *
 * The Settings-panel trigger renders as "<model name> arrow_drop_down" (flow-video.md:114).
 * Same prefix trap as `modelAlreadySelected`, different shape: "Veo 3.1 Lite" is a strict
 * prefix of "Veo 3.1 Lite[Lower Priority]", but the trailing text is a bracketed suffix glued
 * on with no space, not a " Lite"-style word — so the negative lookahead has to reject the
 * match whenever the next character continues the label at all (a word character, or the `[`
 * that opens "[Lower Priority]"), not just a specific trailing word. `[` and `]` are regex
 * metacharacters, so this is exactly where `escapeRegExp` earns its keep — both on `model`
 * (already required) and implicitly in the character class below (which uses literal chars,
 * not user input, so no separate escaping is needed there).
 */
export function videoModelAlreadySelected(label: string | null, model: string): boolean {
  return new RegExp(`${escapeRegExp(model)}(?![\\w[])`, 'i').test(label ?? '')
}

/**
 * Map an aspect ratio like "16:9" to the Material-icon ligature Flow's compose-bar CONFIG
 * TRIGGER renders for it. Confirmed live (flow-selectors.md:172-174) for exactly two: 16:9 ->
 * `crop_16_9` (the ratio spelled out with an underscore, not a colon) and 4:3 -> `crop_landscape`
 * (Flow reuses the real Material Symbols name here instead of a derived `crop_4_3`). Every other
 * ratio is assumed to follow the confirmed `crop_<w>_<h>` pattern by symmetry with 16:9 — and
 * with `ensureVideoSettings`'s already-shipped `crop_9_16` guess for 9:16 — but that is
 * UNCONFIRMED; flag for Wave B. `3:4` is guessed as `crop_portrait` by the same
 * descriptive-name logic as 4:3/`crop_landscape`.
 */
function aspectIcon(aspect: string): string {
  if (aspect === '4:3') return 'crop_landscape'
  if (aspect === '3:4') return 'crop_portrait'
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
