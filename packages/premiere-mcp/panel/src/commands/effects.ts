/**
 * Effects: list the catalogue, describe what is on a clip, apply, set, remove.
 *
 * Two facts shape everything here, both measured live (see docs/premiere/api-notes.md, T10):
 *
 * 1. 🔴 **An un-inserted `VideoFilterComponent` has no methods at all.** Its prototype is a bare
 *    `constructor` — `getParamCount`, `getParam` and `getMatchName` are all "not a function". It
 *    is an opaque token, good only for handing to `createAppendComponentAction`. So params can
 *    only ever be read off an APPLIED instance, and `describe_effect` requires a clip.
 *
 * 2. 🔴 **Actions in a `CompoundAction` do not compose** — they are all computed against the
 *    state at the start of the transaction. Applying a component and setting its params
 *    therefore cannot be one transaction: the params do not exist to be addressed until the
 *    append has committed. `apply_effect` runs two, and says so.
 */
import type { Component, VideoComponentChain } from 'premierepro'
import { didYouMean } from '../../../src/nearest'
import {
  PanelError,
  activeProject,
  activeSequence,
  dumpSequence,
  interpolationMode,
  numArg,
  plainValue,
  ppro,
  resolveClip,
  resolveComponent,
  resolveParam,
  secondsToTick,
  strArg,
  toPproValue,
  withAction,
  withActions,
} from '../ppro'
import type { CommandHandler } from './index'

/** The two components every clip is born with. Removing them is never what anyone meant. */
const INTRINSICS = ['AE.ADBE Opacity', 'AE.ADBE Motion']

const list_effects: CommandHandler = async (args) => {
  const [matchNames, displayNames] = await Promise.all([
    ppro.VideoFilterFactory.getMatchNames(),
    ppro.VideoFilterFactory.getDisplayNames(),
  ])
  const query = typeof args.query === 'string' ? args.query.toLowerCase() : ''
  const effects = matchNames
    .map((matchName, i) => ({ matchName, displayName: displayNames[i] ?? '' }))
    .filter((e) => !query || e.matchName.toLowerCase().includes(query) || e.displayName.toLowerCase().includes(query))
    .sort((a, b) => a.displayName.localeCompare(b.displayName))
  return { effects }
}

const describe_effect: CommandHandler = async (args) => {
  const { component, index } = await componentOn(args)
  const [matchName, displayName] = await Promise.all([component.getMatchName(), component.getDisplayName()])

  const count = component.getParamCount()
  const params = []
  for (let i = 0; i < count; i += 1) {
    const param = component.getParam(i)
    let value: unknown = null
    let unreadable = false
    try {
      value = plainValue(await param.getValueAtTime(ppro.TickTime.TIME_ZERO))
    } catch {
      unreadable = true
    }
    params.push({
      index: i,
      name: param.displayName,
      value,
      keyframable: await param.areKeyframesSupported(),
      timeVarying: param.isTimeVarying(),
      ...(unreadable ? { unreadable: true } : {}),
    })
  }
  return { matchName, displayName, componentIndex: index, params }
}

const apply_effect: CommandHandler = async (args) => {
  const project = await activeProject()
  const sequence = await activeSequence(project)
  const ref = strArg(args.clip, 'clip')
  const clip = await resolveClip(sequence, ref)

  const wanted = strArg(args.matchName, 'matchName')
  const matchName = await resolveMatchName(wanted)

  const chain = await clip.getComponentChain()
  const before = chain.getComponentCount()
  const component = await ppro.VideoFilterFactory.createComponent(matchName)
  const at = typeof args.index === 'number' ? Math.trunc(args.index) : null

  withAction(project, `apply ${matchName}`, () =>
    at === null
      ? chain.createAppendComponentAction(component)
      : (chain as VideoComponentChain).createInsertComponentAction(component, at)
  )

  // Re-resolve: the chain we appended to is a snapshot, and the applied instance is a different
  // object from the token we handed in.
  const fresh = await (await resolveClip(sequence, ref)).getComponentChain()
  if (fresh.getComponentCount() <= before) {
    throw new PanelError(
      'TRANSACTION_FAILED',
      `Premiere accepted "${matchName}" on ${ref} but the chain still has ${before} components.`
    )
  }
  const applied = fresh.getComponentAtIndex(at === null ? fresh.getComponentCount() - 1 : at)

  // A SECOND transaction, of necessity — see the note at the top of this file.
  const params = (args.params ?? {}) as Record<string, unknown>
  const keys = Object.keys(params)
  if (keys.length > 0) {
    const builders = keys.map((key) => () => {
      const { param } = resolveParam(applied, /^\d+$/.test(key) ? Number(key) : key)
      return param.createSetValueAction(param.createKeyframe(toPproValue(params[key])), true)
    })
    withActions(project, `set ${keys.join(', ')}`, builders)
  }

  return dumpSequence(project, sequence)
}

const set_param: CommandHandler = async (args) => {
  const project = await activeProject()
  const sequence = await activeSequence(project)
  const ref = strArg(args.clip, 'clip')
  const clip = await resolveClip(sequence, ref)
  const chain = await clip.getComponentChain()
  const component = await resolveComponent(chain, keyArg(args.component, 'component'))
  const { param, index } = resolveParam(component, keyArg(args.param, 'param'))
  const value = toPproValue(args.value)

  if (typeof args.time !== 'number') {
    withAction(project, `set param ${index} on ${ref}`, () => param.createSetValueAction(param.createKeyframe(value), true))
    return dumpSequence(project, sequence)
  }

  if (!(await param.areKeyframesSupported())) {
    throw new PanelError('INVALID_ARGS', `Param ${index} ("${param.displayName}") does not support keyframes.`)
  }

  const tick = secondsToTick(numArg(args.time, 'time'))

  // Turning a param time-varying is its OWN transaction: until it has committed, there is no
  // keyframe track for `createAddKeyframeAction` to add to (Actions do not compose).
  if (!param.isTimeVarying()) {
    withAction(project, `keyframe param ${index} on ${ref}`, () => param.createSetTimeVaryingAction(true))
  }

  const interpolation = typeof args.interpolation === 'string' ? args.interpolation : null
  withActions(project, `keyframe param ${index} at ${args.time}s`, [
    () => {
      const keyframe = param.createKeyframe(value)
      keyframe.position = tick
      return param.createAddKeyframeAction(keyframe)
    },
  ])
  if (interpolation) {
    withAction(project, `${interpolation} at ${args.time}s`, () =>
      param.createSetInterpolationAtKeyframeAction(tick, interpolationMode(interpolation), true)
    )
  }

  return dumpSequence(project, sequence)
}

const remove_effect: CommandHandler = async (args) => {
  const project = await activeProject()
  const sequence = await activeSequence(project)
  const ref = strArg(args.clip, 'clip')
  const clip = await resolveClip(sequence, ref)
  const chain = await clip.getComponentChain()
  const component = await resolveComponent(chain, keyArg(args.component, 'component'))

  const matchName = await component.getMatchName()
  if (INTRINSICS.includes(matchName)) {
    throw new PanelError(
      'INVALID_ARGS',
      `"${matchName}" is an intrinsic component — every clip has one and Premiere's own UI will not let you ` +
        'delete it. Reset its params instead of removing it.'
    )
  }

  withAction(project, `remove ${matchName} from ${ref}`, () => chain.createRemoveComponentAction(component))
  return dumpSequence(project, sequence)
}

/* ---- helpers ---------------------------------------------------------------------------------- */

/** Effects can be named by match name OR display name — resolve either, or say what is near. */
async function resolveMatchName(wanted: string): Promise<string> {
  const [matchNames, displayNames] = await Promise.all([
    ppro.VideoFilterFactory.getMatchNames(),
    ppro.VideoFilterFactory.getDisplayNames(),
  ])
  if (matchNames.includes(wanted)) return wanted

  const lower = wanted.toLowerCase()
  const byDisplay = displayNames.findIndex((d) => (d ?? '').toLowerCase() === lower)
  if (byDisplay >= 0) return matchNames[byDisplay]

  // Rank against both name lists so "gaussian blur" finds it whichever way it was written.
  const all = [...matchNames, ...displayNames.filter(Boolean)]
  throw new PanelError('EFFECT_NOT_FOUND', `No effect "${wanted}".${didYouMean(wanted, all)}`)
}

async function componentOn(args: Record<string, unknown>): Promise<{ component: Component; index: number }> {
  const project = await activeProject()
  const sequence = await activeSequence(project)
  const clip = await resolveClip(sequence, strArg(args.clip, 'clip'))
  const chain = await clip.getComponentChain()
  const component = await resolveComponent(chain, keyArg(args.component, 'component'))

  let index = -1
  for (let i = 0; i < chain.getComponentCount(); i += 1) {
    if ((await chain.getComponentAtIndex(i).getMatchName()) === (await component.getMatchName())) {
      index = i
      break
    }
  }
  return { component, index }
}

function keyArg(v: unknown, name: string): string | number {
  if (typeof v === 'number' && Number.isFinite(v)) return Math.trunc(v)
  if (typeof v === 'string' && v) return v
  throw new PanelError('INVALID_ARGS', `${name} must be an index or a name.`)
}

export const effectCommands = {
  list_effects,
  describe_effect,
  apply_effect,
  set_param,
  remove_effect,
}
