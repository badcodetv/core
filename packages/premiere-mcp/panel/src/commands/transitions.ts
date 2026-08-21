/**
 * Transitions: list what this install has, put one on a cut, take it off again.
 *
 * 🔴 **Video only.** The declarations carry `createAddVideoTransitionAction` on
 * `VideoClipTrackItem` and nothing equivalent anywhere for audio — there is no
 * `AudioTransition` type, no `createAddAudioTransitionAction`, nothing. An audio ref is
 * therefore rejected here rather than being passed to Premiere to fail obscurely. Audio
 * crossfades have to be done by hand in the UI.
 *
 * A transition is attached to a CLIP, not to a cut: `at: 'end'` on the outgoing clip and
 * `at: 'start'` on the incoming one describe the same dissolve from either side.
 */
import type { AddTransitionOptions, VideoClipTrackItem } from 'premierepro'
import { didYouMean } from '../../../src/nearest'
import {
  PanelError,
  activeProject,
  activeSequence,
  countTransitions,
  dumpSequence,
  numArg,
  ppro,
  resolveClip,
  secondsToTick,
  strArg,
  withAction,
} from '../ppro'
import type { CommandHandler } from './index'

const list_transitions: CommandHandler = async (args) => {
  const names = await matchNames()
  const query = typeof args.query === 'string' ? args.query.toLowerCase() : ''
  const filtered = query ? names.filter((n) => n.toLowerCase().includes(query)) : names
  return { transitions: filtered.map((matchName) => ({ matchName })) }
}

const add_transition: CommandHandler = async (args) => {
  const project = await activeProject()
  const sequence = await activeSequence(project)
  const ref = strArg(args.clip, 'clip')
  const clip = await videoClip(sequence, ref)

  // Check the name against the catalogue FIRST. `createVideoTransition` on an unknown match name
  // does not fail usefully — the transaction just does nothing — so the "did you mean" has to
  // happen before Premiere is involved at all.
  const wanted = strArg(args.matchName, 'matchName')
  const names = await matchNames()
  if (!names.includes(wanted)) {
    throw new PanelError('TRANSITION_NOT_FOUND', `No transition "${wanted}".${didYouMean(wanted, names)}`)
  }

  const applyToStart = args.at === 'start'
  if (args.at !== 'start' && args.at !== 'end') {
    throw new PanelError('INVALID_ARGS', 'add_transition needs at: "start" or "end".')
  }

  const transition = ppro.TransitionFactory.createVideoTransition(wanted)
  let options: AddTransitionOptions = new ppro.AddTransitionOptions().setApplyToStart(applyToStart)
  if (typeof args.duration === 'number') options = options.setDuration(secondsToTick(numArg(args.duration, 'duration')))
  // Alignment is a FRACTION of the transition that sits before the cut — 0.5 (the default,
  // read back live) centres it. Not an enum, despite reading like one.
  if (typeof args.alignment === 'number') options = options.setTransitionAlignment(args.alignment)

  // Count before and after. `executeTransaction` returning true is NOT proof the edit happened
  // — Premiere has been caught reporting success on calls that did nothing (see api-notes.md) —
  // and since a transition cannot be read back, the count is the only verification available.
  const track = await trackOf(sequence, ref)
  const before = countTransitions(track)

  withAction(project, `${wanted.replace(/^\w+\.\w+ /, '')} on ${ref}`, () =>
    clip.createAddVideoTransitionAction(transition, options)
  )

  if (countTransitions(await trackOf(sequence, ref)) <= before) {
    throw new PanelError(
      'TRANSACTION_FAILED',
      `Premiere accepted the "${wanted}" transition on ${ref} (${args.at}) but the track still has ${before} ` +
        'transition(s), so nothing was actually added. Note this is NOT the missing-handles case — a clip with no ' +
        'media beyond the cut still gets a transition, just a single-sided one. Cause unknown; probe with premiere_eval.'
    )
  }
  return dumpSequence(project, sequence)
}

const remove_transition: CommandHandler = async (args) => {
  const project = await activeProject()
  const sequence = await activeSequence(project)
  const ref = strArg(args.clip, 'clip')
  const clip = await videoClip(sequence, ref)

  if (args.at !== 'start' && args.at !== 'end') {
    throw new PanelError('INVALID_ARGS', 'remove_transition needs at: "start" or "end".')
  }
  const position =
    args.at === 'start' ? ppro.Constants.TransitionPosition.START : ppro.Constants.TransitionPosition.END

  // No before/after check here: removing a transition that was never there is a legitimate
  // no-op, so a flat count proves nothing either way. The returned state's `transitionCount`
  // is what a caller should read.
  withAction(project, `remove transition at ${args.at} of ${ref}`, () =>
    clip.createRemoveVideoTransitionAction(position)
  )
  return dumpSequence(project, sequence)
}

/* ---- helpers ---------------------------------------------------------------------------------- */

async function matchNames(): Promise<string[]> {
  const names = await ppro.TransitionFactory.getVideoTransitionMatchNames()
  return [...names].sort()
}

/** The `VideoTrack` a `v<n>:<i>` ref names. */
async function trackOf(sequence: import('premierepro').Sequence, ref: string): Promise<import('premierepro').VideoTrack> {
  const index = Number(ref.slice(1).split(':')[0])
  const track = await sequence.getVideoTrack(index)
  if (!track) throw new PanelError('CLIP_NOT_FOUND', `No video track ${index}.`)
  return track
}

/** Resolve a ref and insist it is a video clip — the transition API exists on nothing else. */
async function videoClip(
  sequence: import('premierepro').Sequence,
  ref: string
): Promise<VideoClipTrackItem> {
  if (!ref.startsWith('v')) {
    throw new PanelError(
      'INVALID_ARGS',
      `Transitions are video-only — "${ref}" is an audio clip. Premiere's UXP API offers no audio ` +
        'transition at all; a crossfade has to be added by hand in the timeline.'
    )
  }
  return (await resolveClip(sequence, ref)) as VideoClipTrackItem
}

export const transitionCommands = {
  list_transitions,
  add_transition,
  remove_transition,
}
