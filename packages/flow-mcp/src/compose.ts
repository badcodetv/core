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
