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
