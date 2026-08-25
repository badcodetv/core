/**
 * Sequence markers, and the playhead.
 *
 * Markers are the cheapest way to hand a human a note inside Premiere — "beat here", "Kai: this
 * cut is a frame late". They already come back in every `SequenceState`; this adds the writing
 * half.
 *
 * The playhead is not an edit and is not undoable: `setPlayerPosition` is a plain async call,
 * not an Action, so it runs outside any transaction. It exists so a session can point a human at
 * the moment it is talking about.
 */
import {
  activeProject,
  activeSequence,
  dumpSequence,
  numArg,
  ppro,
  secondsToTick,
  strArg,
  tickToSeconds,
  withAction,
} from '../ppro'
import type { CommandHandler } from './index'

const add_marker: CommandHandler = async (args) => {
  const project = await activeProject()
  const sequence = await activeSequence(project)

  const name = strArg(args.name, 'name')
  const time = secondsToTick(numArg(args.time, 'time'))
  const duration = secondsToTick(typeof args.duration === 'number' ? args.duration : 0)
  const comments = typeof args.comments === 'string' ? args.comments : ''

  const markers = await ppro.Markers.getMarkers(sequence)
  withAction(project, `marker "${name}"`, () =>
    markers.createAddMarkerAction(name, ppro.Marker.MARKER_TYPE_COMMENT, time, duration, comments)
  )
  return dumpSequence(project, sequence)
}

const set_playhead: CommandHandler = async (args) => {
  const project = await activeProject()
  const sequence = await activeSequence(project)

  await sequence.setPlayerPosition(secondsToTick(numArg(args.time, 'time')))
  // Read it back rather than echoing what was asked for: the playhead snaps to a frame boundary
  // like everything else, so the requested time is not the time it landed on.
  return { playhead: tickToSeconds(await sequence.getPlayerPosition()) }
}

export const markerCommands = {
  add_marker,
  set_playhead,
}
