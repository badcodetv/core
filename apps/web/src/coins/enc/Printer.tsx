import {
  faucetView,
  formatBps,
  formatDuration,
  formatEnc,
  formatM2,
  formatUnits,
  nextH6Release,
  retirementView,
  treasuryView,
} from '@badcode/enc'
import type { EncChainState } from './useEncChain'

/**
 * The machine, reading out.
 *
 * Everything here is derived in `@badcode/enc` from accounts this page
 * subscribes to — no number is computed in a component, and none is fetched on
 * a timer. What ticks is the clock; the numbers move when the chain does.
 */

/** A date, in the only timezone the Fed publishes in. */
function easternDate(unix: number): string {
  if (unix <= 0) return 'never'
  return new Intl.DateTimeFormat('en-GB', {
    timeZone: 'America/New_York',
    day: 'numeric',
    month: 'short',
    year: 'numeric',
  }).format(new Date(unix * 1_000))
}

function Readout({
  label,
  value,
  unit,
  note,
}: {
  label: string
  value: string
  unit?: string
  note?: string
}) {
  return (
    <div className="enc-readout">
      <p className="enc-readout-label">{label}</p>
      <p className="enc-readout-value">
        {value}
        {unit ? <span className="enc-readout-unit"> {unit}</span> : null}
      </p>
      {note ? <p className="enc-readout-note">{note}</p> : null}
    </div>
  )
}

/**
 * The Emperor's share of all the money, with the floor drawn on it.
 *
 * The floor governs the faucet and never the burn — a floor enforced by
 * refusing to burn would break the peg — so the bar can and does go under it.
 */
function VaultBar({ shareBps, floorBps }: { shareBps: number; floorBps: number }) {
  const share = Math.min(100, shareBps / 100)
  return (
    <div
      className="enc-bar"
      role="img"
      aria-label={`The vault holds ${formatBps(shareBps)} of supply; the floor is ${formatBps(floorBps)}`}
    >
      <div className="enc-bar-fill" style={{ width: `${share}%` }} />
      <div className="enc-bar-floor" style={{ left: `${floorBps / 100}%` }}>
        <span>floor {formatBps(floorBps)}</span>
      </div>
    </div>
  )
}

export function Printer({ state }: { state: EncChainState }) {
  const { config, printer, now } = state
  if (!config || !printer) return null

  const treasury = treasuryView({
    config,
    printer,
    supply: state.supply,
    vaultBalance: state.vaultBalance,
    escrowBalance: state.escrowBalance,
  })
  const faucet = faucetView({
    now,
    config,
    current: state.currentEpoch,
    previous: state.previousEpoch,
  })
  const retirement = retirementView(config, printer, now)
  const release = nextH6Release(now)
  const encPerThousand = formatUnits(treasury.k, treasury.encDecimals)

  return (
    <section className="enc-printer">
      <h2 className="enc-section-title">The printer</h2>
      <p className="enc-section-strap">
        Two numbers, and a rule between them that nobody may edit. The Fed decides the first. The
        second follows, whether or not anyone is watching.
      </p>

      <div className="enc-readouts">
        <Readout
          label="What the Fed says money is"
          value={formatM2(treasury.m2Value)}
          note={`M2, as published on ${easternDate(treasury.m2ReleaseDate)}.`}
        />
        <Readout
          label="What exists because of it"
          value={formatEnc(treasury.supply, { fractionDigits: 0 })}
          unit="ENC"
          note={`${encPerThousand} ENC per $1,000 of the money supply. They print, we print.`}
        />
        <Readout
          label="The Fed speaks again in"
          value={formatDuration(release - now)}
          note={`H.6, fourth Tuesday, 1pm in New York — ${easternDate(release)}. Nothing here waits for it: anyone may sync the peg, and the peg moves when somebody bothers.`}
        />
      </div>

      <div className="enc-fact">
        <h3>The peg, stated honestly</h3>
        <p>
          The rule is <code>supply ≥ k × M2</code>, and the <code>≥</code> is not a typo we never
          got round to fixing. A contraction burns from the vault, and if the vault cannot cover the
          burn the excess stays out in the world until the next release retargets it. We could have
          written <code>=</code> and been wrong once a decade. This is the number instead.
        </p>
        <dl className="enc-pairs">
          <div>
            <dt>Aimed at</dt>
            <dd>{formatEnc(treasury.targetSupply, { fractionDigits: 0 })} ENC</dd>
          </div>
          <div>
            <dt>Actually out there</dt>
            <dd>{formatEnc(treasury.supply, { fractionDigits: 0 })} ENC</dd>
          </div>
          <div>
            <dt>Drift</dt>
            <dd className={treasury.drift > 0n ? 'enc-drift' : undefined}>
              {treasury.drift === 0n
                ? 'none, today'
                : `${formatEnc(treasury.drift)} ENC over target`}
            </dd>
          </div>
        </dl>
      </div>

      <div className="enc-fact">
        <h3>The Emperor&rsquo;s pocket</h3>
        <VaultBar shareBps={treasury.vaultShareBps} floorBps={config.floorBps} />
        <p>
          The vault holds {formatEnc(treasury.vaultBalance, { fractionDigits: 0 })} ENC —{' '}
          <strong>{formatBps(treasury.vaultShareBps)} of every coin in existence</strong>. Newly
          printed money lands here first, exactly as it does where you live. The floor is{' '}
          {formatBps(config.floorBps)}: below it the faucet pays nothing at all — no share, no
          welcome grant, no exceptions — and the machine simply waits for the Fed to top it up.
          {treasury.aboveFloor
            ? ' Today there is something to give away.'
            : ' Today there is not. Arrive during the tightening and there is nothing for you; that is the lesson, not a bug.'}
        </p>
        <dl className="enc-pairs">
          <div>
            <dt>Floor</dt>
            <dd>{formatEnc(treasury.floor, { fractionDigits: 0 })} ENC</dd>
          </div>
          <div>
            <dt>Locked in bids</dt>
            <dd>{formatEnc(treasury.escrowBalance, { fractionDigits: 0 })} ENC</dd>
          </div>
          <div>
            <dt>Held by everyone else</dt>
            <dd>
              {formatEnc(treasury.supply - treasury.vaultBalance, { fractionDigits: 0 })} ENC
            </dd>
          </div>
        </dl>
        <p className="enc-aside">
          Escrowed bids sit in their own pocket, not the vault&rsquo;s. A monetary contraction burns
          the Emperor&rsquo;s money; it was never allowed to burn yours.
        </p>
      </div>

      <div className="enc-fact">
        <h3>The faucet</h3>
        <p>
          Register today, collect tomorrow. Today&rsquo;s pot was frozen the moment somebody first
          claimed, and it is divided among <em>yesterday&rsquo;s</em> registrants — which is why a
          thousand fresh wallets dilute each other instead of draining it.
        </p>
        <dl className="enc-pairs">
          <div>
            <dt>Today&rsquo;s pot</dt>
            <dd>
              {faucet.opened
                ? `${formatEnc(faucet.pot, { fractionDigits: 0 })} ENC`
                : 'not opened yet today'}
            </dd>
          </div>
          <div>
            <dt>Registered today</dt>
            <dd>{faucet.registrants}</dd>
          </div>
          <div>
            <dt>Yesterday&rsquo;s share, each</dt>
            <dd>{formatEnc(faucet.shareToday)} ENC</dd>
          </div>
          <div>
            <dt>This epoch ends in</dt>
            <dd>{formatDuration(faucet.current.secondsRemaining)}</dd>
          </div>
        </dl>
        <p className="enc-aside">
          {faucet.opened
            ? 'The welcome grant is one per wallet, ever, and it buys you nothing. That is the joke, and it is also the arithmetic.'
            : 'No epoch account exists yet today. That is not an outage — it is created by whoever claims first, and nobody has.'}
        </p>
      </div>

      <div className="enc-fact">
        <h3>The end, if it comes</h3>
        {retirement.retired ? (
          <p className="enc-retired">
            It is over. Someone observed that the Fed had stopped speaking and said so on-chain, and
            the peg will never move again. Everything else still runs: the auctions go on trading at
            the last prices a vanished world ever reported.
          </p>
        ) : (
          <p>
            Last heard from the Fed {easternDate(retirement.lastSyncAt)}. If{' '}
            {formatDuration(retirement.silenceSeconds)} ever passes without a new number,{' '}
            <strong>anyone</strong> may retire this coin — once, permanently, no key consulted.{' '}
            {retirement.ready
              ? 'That silence has already run out here: the coin is one transaction from its own ending, and nobody needs permission to send it.'
              : `That leaves ${formatDuration(retirement.secondsRemaining)}.`}{' '}
            The program cannot tell whether the dollar ended or everyone stopped looking, and from
            where it sits those are the same event.
          </p>
        )}
      </div>
    </section>
  )
}
