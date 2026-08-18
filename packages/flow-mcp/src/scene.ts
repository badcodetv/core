/**
 * Flow's Scene Builder — the surface behind `/project/<projectId>/edit/<sceneId>`.
 *
 * Pure, so the selectors and URL shapes can be tested without a browser; the clicking lives in
 * flow-client.ts. Every fact below was mapped against the live UI on 2026-08-18.
 *
 * WHY THIS EXISTS: `docs/flow/platform-controls.md` recorded on 2026-08-12 that Extend "does
 * not exist in this account". That check read the clip's hover menu and the scene editor's
 * VISIBLE controls, and both are Extend-free. Extend is one level deeper — inside the
 * timeline's `Add Clip` DROPDOWN — so it was missed. It is real, and it is the only way to
 * continue a clip with the model's own context rather than a still.
 */

/** Clicking a clip in the project grid opens the scene editor at this path. */
export const SCENE_PATH_RE = /\/project\/([0-9a-f-]{36})\/edit\/([0-9a-f-]{36})/i

/**
 * After an Extend, Flow moves to a DIFFERENT path with a NEW id: `/scene/<id>`, not
 * `/edit/<id>`. Measured 2026-08-18 — and it is why the first live Extend looked like a
 * timeout. It had in fact succeeded.
 *
 * The distinction matters: `/edit/<id>` is one clip's editor, `/scene/<id>` is an assembled
 * multi-segment scene. Extend turns the former into the latter.
 */
export const SCENE_COMPOSED_PATH_RE = /\/project\/([0-9a-f-]{36})\/scene\/([0-9a-f-]{36})/i

export function sceneUrl(projectId: string, sceneId: string): string {
  return `https://labs.google/fx/tools/flow/project/${projectId}/edit/${sceneId}`
}

/** Pull the ids back out of a scene-editor URL — this is the URL a user pastes from Flow. */
export function parseSceneUrl(url: string): { projectId: string; sceneId: string } | null {
  const m = SCENE_PATH_RE.exec(url)
  return m ? { projectId: m[1]!, sceneId: m[2]! } : null
}

/**
 * Either scene URL — the single-clip editor or the composed scene — with which one it was.
 * Anything that has to survive an Extend must use this, not parseSceneUrl.
 */
export function parseAnySceneUrl(
  url: string,
): { projectId: string; sceneId: string; kind: 'edit' | 'scene' } | null {
  const edit = SCENE_PATH_RE.exec(url)
  if (edit) return { projectId: edit[1]!, sceneId: edit[2]!, kind: 'edit' }
  const composed = SCENE_COMPOSED_PATH_RE.exec(url)
  if (composed) return { projectId: composed[1]!, sceneId: composed[2]!, kind: 'scene' }
  return null
}

/**
 * The timeline's `Add Clip` button. Opens a two-item menu; it is NOT itself the add action.
 * Named "add Add Clip" because Flow renders the material icon name into the accessible name.
 */
export const ADD_CLIP_BUTTON_RE = /^add\s*Add Clip$/i

/**
 * The two menu items behind `Add Clip`.
 *
 * The Extend label carries its model inline — observed as "Extend (Veo 3.1 - Lite)". The tier
 * is NOT selectable: Extend is pinned to whatever Flow puts in that label, and on 2026-08-18
 * that was Veo 3.1 Lite on an account whose compose bar offers Fast and Quality freely. Treat
 * the label as the source of truth and surface it to the caller rather than assuming Lite
 * forever.
 */
export const ADD_CLIP_MENU_ITEM_RE = /^add\s*Add Clip$/i
export const EXTEND_MENU_ITEM_RE = /Extend\s*\(/i

/**
 * Extend ARMS, it does not fire — clicking the menu item spends nothing. It puts the compose
 * bar into extend mode, which is visible three ways:
 *   - the prompt placeholder changes to "What happens next?"
 *   - a dismissible chip reading "Extend (<model>)" appears beside Create
 *   - the timeline grows a "Prompt to Extend" slot
 * The Create button stays DISABLED until the prompt has text. Verified live 2026-08-18.
 */
export const EXTEND_CHIP_RE = /^Extend\s*\(.+\)\s*close$/i
export const EXTEND_PLACEHOLDER = 'What happens next?'
export const EXTEND_TIMELINE_SLOT_RE = /Prompt to Extend/i

/**
 * Flow names a saved frame "Saved Frame from <scene title>", so this prefix finds every one of
 * them in the asset picker. Detection has to go through the picker: the scene editor does not
 * render the project gallery, so the in-page media scrape cannot see a frame it just saved
 * (measured 2026-08-18).
 */
export const SAVED_FRAME_QUERY = 'Saved Frame'
export const SAVED_FRAME_TITLE_RE = /^Saved Frame from /i

/** The player overlay's frame grab — saves the frame at the CURRENT playhead into the project. */
export const SAVE_FRAME_RE = /^add_photo_alternate\s*Save Frame$/i

/** Player transport, used to park the playhead before Save Frame. */
export const SKIP_NEXT_RE = /^skip_next\s*next$/i
export const SKIP_PREV_RE = /^skip_previous\s*Previous$/i

/**
 * Recover the model tier from the Extend control's label.
 *
 * Flow writes it as "Extend (Veo 3.1 - Lite)" — a hyphen where the compose bar uses a space
 * ("Veo 3.1 Lite"), so callers comparing against canonicalVideoModel() need the normalised
 * form, not the raw label.
 *
 * Returns null for the disabled placeholder button, whose label is the literal, unrendered
 * "Extend ({{modelName}})" — a Flow templating bug seen live on 2026-08-18. Reading that as a
 * model name would produce a nonsense tier, so it is rejected explicitly.
 */
export function extendModelFromLabel(label: string): string | null {
  const m = /Extend\s*\(([^)]+)\)/i.exec(label)
  if (!m) return null
  const inner = m[1]!.trim()
  if (inner.includes('{{') || inner.includes('}}')) return null
  return inner.replace(/\s*-\s*/g, ' ').replace(/\s+/g, ' ').trim()
}

/** Seconds → Flow's "MM:SS:FF" playhead readout, at its fixed 24fps timeline. */
export const SCENE_FPS = 24

export function toTimecode(seconds: number, fps = SCENE_FPS): string {
  const total = Math.max(0, seconds)
  const mm = Math.floor(total / 60)
  const ss = Math.floor(total % 60)
  const ff = Math.round((total - Math.floor(total)) * fps) % fps
  const pad = (n: number): string => String(n).padStart(2, '0')
  return `${pad(mm)}:${pad(ss)}:${pad(ff)}`
}

export function fromTimecode(tc: string, fps = SCENE_FPS): number | null {
  const m = /^(\d{2}):(\d{2}):(\d{2})$/.exec(tc.trim())
  if (!m) return null
  return Number(m[1]) * 60 + Number(m[2]) + Number(m[3]) / fps
}

/** Where to park the playhead before grabbing a frame. */
export type FramePosition = 'current' | 'end'

/**
 * The reason Flow will refuse this extend request, or null if it will accept it.
 *
 * Mirrors videoRequestError's contract: full "CODE: detail" string so the caller just throws
 * it, checked before a browser is touched.
 */
export function sceneExtendError(req: { prompt: string; sceneId?: string }): string | null {
  if (!req.prompt.trim()) {
    return 'SCENE_EXTEND_EMPTY_PROMPT: Extend needs a prompt — Flow keeps Create disabled until the box has text, so an empty prompt hangs rather than failing.'
  }
  if (req.sceneId !== undefined && !/^[0-9a-f-]{36}$/i.test(req.sceneId)) {
    return `SCENE_ID_INVALID: "${req.sceneId}" is not a scene id. A scene id is the 36-character uuid after /edit/ in a Flow scene URL — not a media id and not a project id.`
  }
  return null
}
