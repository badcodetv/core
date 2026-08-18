import { describe, it, expect } from 'vitest'
import {
  parseSceneUrl,
  parseAnySceneUrl,
  sceneUrl,
  extendModelFromLabel,
  toTimecode,
  fromTimecode,
  sceneExtendError,
  EXTEND_MENU_ITEM_RE,
  EXTEND_CHIP_RE,
  ADD_CLIP_BUTTON_RE,
  SAVE_FRAME_RE,
  SAVED_FRAME_QUERY,
  SAVED_FRAME_TITLE_RE,
} from './scene'

const PROJECT = '1774dff0-02b0-45a7-9d53-ecc549bc60a5'
const SCENE = 'bb7b9fad-5f0b-426a-865d-0f0451d14e2b'

describe('parseSceneUrl', () => {
  it('recovers both ids from the URL a user pastes out of Flow', () => {
    expect(parseSceneUrl(sceneUrl(PROJECT, SCENE))).toEqual({ projectId: PROJECT, sceneId: SCENE })
  })

  it('rejects a plain project URL, which has no scene', () => {
    expect(parseSceneUrl(`https://labs.google/fx/tools/flow/project/${PROJECT}`)).toBe(null)
  })

  it('is not fooled by a media id pasted on its own', () => {
    expect(parseSceneUrl(SCENE)).toBe(null)
  })
})

describe('extendModelFromLabel', () => {
  it("normalises Flow's hyphenated tier to the compose bar's spelling", () => {
    expect(extendModelFromLabel('Extend (Veo 3.1 - Lite)')).toBe('Veo 3.1 Lite')
  })

  it('handles a label that is already spaced', () => {
    expect(extendModelFromLabel('Extend (Veo 3.1 Fast)')).toBe('Veo 3.1 Fast')
  })

  it('refuses the unrendered template placeholder rather than inventing a tier', () => {
    // Flow ships the disabled button with its literal mustache still in it (seen 2026-08-18).
    expect(extendModelFromLabel('Extend ({{modelName}})')).toBe(null)
  })

  it('returns null when there is no parenthesised tier at all', () => {
    expect(extendModelFromLabel('Extend')).toBe(null)
  })
})

describe('timecode', () => {
  it('formats seconds the way the scene player prints them', () => {
    expect(toTimecode(8)).toBe('00:08:00')
    expect(toTimecode(7.958)).toBe('00:07:23')
    expect(toTimecode(0)).toBe('00:00:00')
    expect(toTimecode(65.5)).toBe('01:05:12')
  })

  it('clamps a negative playhead rather than emitting nonsense', () => {
    expect(toTimecode(-3)).toBe('00:00:00')
  })

  it('round-trips through fromTimecode', () => {
    expect(fromTimecode('00:08:00')).toBe(8)
    expect(fromTimecode(toTimecode(65.5))).toBeCloseTo(65.5, 1)
  })

  it('rejects a malformed readout', () => {
    expect(fromTimecode('8s')).toBe(null)
    expect(fromTimecode('0:8:0')).toBe(null)
  })
})

describe('sceneExtendError', () => {
  it('accepts an ordinary request', () => {
    expect(sceneExtendError({ prompt: 'the camera keeps falling' })).toBe(null)
    expect(sceneExtendError({ prompt: 'x', sceneId: SCENE })).toBe(null)
  })

  it('refuses an empty prompt, because Flow would just leave Create disabled', () => {
    expect(sceneExtendError({ prompt: '   ' })).toMatch(/^SCENE_EXTEND_EMPTY_PROMPT:/)
  })

  it('refuses something that is not a scene id', () => {
    expect(sceneExtendError({ prompt: 'x', sceneId: 'not-a-uuid' })).toMatch(/^SCENE_ID_INVALID:/)
  })
})

describe('selectors match the live accessible names', () => {
  // Captured verbatim from the 2026-08-18 snapshot of the scene editor.
  it('matches the timeline Add Clip button', () => {
    expect(ADD_CLIP_BUTTON_RE.test('add Add Clip')).toBe(true)
  })

  it('matches the Extend menu item with its inline tier', () => {
    expect(EXTEND_MENU_ITEM_RE.test('keyboard_double_arrow_right Extend (Veo 3.1 - Lite)')).toBe(true)
  })

  it('matches the armed-mode chip, which is how we know extend mode took', () => {
    expect(EXTEND_CHIP_RE.test('Extend (Veo 3.1 - Lite) close')).toBe(true)
  })

  it('does not confuse the armed chip with the menu item', () => {
    expect(EXTEND_CHIP_RE.test('keyboard_double_arrow_right Extend (Veo 3.1 - Lite)')).toBe(false)
  })

  it('matches the player overlay frame grab', () => {
    expect(SAVE_FRAME_RE.test('add_photo_alternate Save Frame')).toBe(true)
  })
})

describe('saved frames', () => {
  it('matches the title Flow actually gives a saved frame', () => {
    // Verbatim from the live gallery, 2026-08-18.
    expect(SAVED_FRAME_TITLE_RE.test('Saved Frame from Satellite orbiting Earth')).toBe(true)
  })

  it('does not match an ordinary generation', () => {
    expect(SAVED_FRAME_TITLE_RE.test('Camera descending toward coastal…')).toBe(false)
  })

  it('the picker query is a prefix of the real title', () => {
    expect('Saved Frame from Satellite orbiting Earth'.startsWith(SAVED_FRAME_QUERY)).toBe(true)
  })
})

describe('parseAnySceneUrl', () => {
  const base = `https://labs.google/fx/tools/flow/project/${PROJECT}`

  it('recognises the single-clip editor', () => {
    expect(parseAnySceneUrl(`${base}/edit/${SCENE}`)).toEqual({
      projectId: PROJECT,
      sceneId: SCENE,
      kind: 'edit',
    })
  })

  it('recognises the composed scene an Extend leaves you on', () => {
    // Extend navigates from /edit/<id> to /scene/<newId>. Missing this made a successful
    // Extend look like a 480s timeout (2026-08-18).
    expect(parseAnySceneUrl(`${base}/scene/${SCENE}`)).toEqual({
      projectId: PROJECT,
      sceneId: SCENE,
      kind: 'scene',
    })
  })

  it('still rejects a bare project URL', () => {
    expect(parseAnySceneUrl(base)).toBe(null)
  })

  it('parseSceneUrl alone does NOT see the composed scene — that is the bug it caused', () => {
    expect(parseSceneUrl(`${base}/scene/${SCENE}`)).toBe(null)
  })
})
