import {
  MELT_ANNUAL_BPS,
  claimView,
  formatBps,
  formatEnc,
  meltedBalance,
} from '@badcode/enc'
import { explorerUrl } from '@badcode/chain-kit'
import { useCluster } from '@badcode/chain-react'
import { useRef, useState } from 'react'
import type { EncActions } from './useEncActions'
import type { EncChainState } from './useEncChain'

/**
 * What the coin does to you, and the one button that lets you in.
 *
 * The Gazette below is where a wallet spends; this is where it arrives and
 * where it watches what it has quietly stop being worth anything. The two
 * halves of the joke, in the order they happen to a person.
 */

/** A signature, as a link out to something that is not us. */
export function Sent({ signature }: { signature: string }) {
  const cluster = useCluster()
  return (
    <a
      className="enc-sent"
      href={explorerUrl(cluster, 'tx', signature)}
      target="_blank"
      rel="noreferrer"
    >
      Landed — read it on the explorer ↗
    </a>
  )
}

/** Whatever just went wrong, as a sentence rather than a number. */
export function Refused({ message }: { message: string }) {
  return (
    <p className="enc-refused" role="status">
      {message}
    </p>
  )
}

/**
 * The melting balance.
 *
 * **Nothing on this chain decays.** There is no demurrage, no interest-bearing
 * extension, no instruction that could take a token out of a wallet — the
 * number the chain holds is the number that will be there tomorrow. What falls
 * is what it buys: every price on this page is a fixed share of the money
 * supply, so a balance that sits still loses ground every second that anyone
 * anywhere prints. The page renders that loss instead of the balance, because
 * a coin about seeing what is not there ought to lie to you about what you have
 * and then admit it in the next paragraph.
 *
 * The clock starts when this page first saw the balance, not when the wallet
 * acquired it. The chain does not record when you got it and neither do we.
 */
function Melting({ balance, now }: { balance: bigint; now: number }) {
  // Hover and tap are tracked apart so that a mouse user who hovers *and then
  // clicks* does not toggle the reveal straight back off — the click pins it
  // instead, and clicking again lets go. On a touch device there is no hover
  // and the tap is the whole mechanism.
  const [pinned, setPinned] = useState(false)
  const [hovered, setHovered] = useState(false)
  const revealed = pinned || hovered
  // Re-anchored whenever the balance itself changes, so a claim that lands
  // shows the number that arrived rather than continuing an old descent.
  const since = useRef({ balance, at: now })
  if (since.current.balance !== balance) since.current = { balance, at: now }
  const held = Math.max(0, now - since.current.at)
  const shown = meltedBalance(balance, held)

  return (
    <div className="enc-melting">
      <p className="enc-readout-label">What you are holding</p>
      <button
        type="button"
        className="enc-melting-value"
        onClick={() => setPinned((p) => !p)}
        onMouseEnter={() => setHovered(true)}
        onMouseLeave={() => setHovered(false)}
        title="The chain's number, not this one"
      >
        {formatEnc(revealed ? balance : shown, { fractionDigits: 6, padFraction: true })}
        <span className="enc-readout-unit"> ENC</span>
      </button>
      <p className="enc-melting-note">
        {revealed ? (
          <>
            <strong>That is the true balance</strong>, exactly as the chain holds it. Nothing has
            been taken from you and nothing can be.
          </>
        ) : (
          <>
            Falling at {formatBps(MELT_ANNUAL_BPS, 0)} a year, which is roughly how fast they
            print. Nothing is leaving your wallet — what is falling is what the number buys, and
            every price on this page is a fixed share of the money supply. Hover or tap it for the
            figure the chain actually holds.
          </>
        )}
      </p>
    </div>
  )
}

export function Wallet({ state, actions }: { state: EncChainState; actions: EncActions }) {
  const { config, now } = state
  if (!config) return null

  if (!actions.wallet) {
    return (
      <section className="enc-counter">
        <h2 className="enc-section-title">The counter</h2>
        <p className="enc-section-strap">
          Connect something and the page grows buttons: a faucet that hands out the Emperor&rsquo;s
          money once an epoch, and ten columns you can bid on. Nothing above needs any of that.
        </p>
        <p className="enc-hint">
          There is no <em>buy</em> button and there will not be one. The program has no purchase
          instruction, we seed no liquidity pool and we sell no ENC, ever. The faucet is the only
          route in that we control; anything else is strangers trading a plain SPL token among
          themselves, which we neither prevent nor point at.
        </p>
      </section>
    )
  }

  const claim = claimView({
    epoch: state.epochIndex,
    config,
    player: actions.player,
    current: state.currentEpoch,
    previous: state.previousEpoch,
    supply: state.supply,
    vaultBalance: state.vaultBalance,
  })

  return (
    <section className="enc-counter">
      <h2 className="enc-section-title">The counter</h2>

      <div className="enc-counter-grid">
        <Melting balance={actions.balance} now={now} />

        <div className="enc-claim">
          <p className="enc-readout-label">
            The faucet, for you specifically · epoch {claim.epoch.toString()}
          </p>
          <p className="enc-claim-line">{claimSentence(claim)}</p>
          <button
            type="button"
            className="enc-do"
            disabled={!claim.claimable || actions.pending}
            onClick={() => void actions.claim()}
          >
            {actions.pending ? 'Waiting on the chain…' : 'Claim this epoch'}
          </button>
          <p className="enc-melting-note">
            {claim.case === 'below-floor' ? (
              <>
                The vault is at or under its floor of {formatBps(config.floorBps)} of all supply.
                Below it the faucet pays <strong>nothing at all</strong> — no share, no welcome
                grant, no exceptions — and waits for the Fed. Arriving during the tightening and
                finding the door shut is the lesson, not a bug.
              </>
            ) : (
              <>
                Claiming registers you for this epoch, and a registration is what a share is paid
                against next epoch. On today&rsquo;s headcount that share would be{' '}
                <strong>{formatEnc(claim.shareNextEpoch)} ENC</strong> — it falls as more wallets
                register, which is precisely why a thousand fresh wallets dilute each other instead
                of draining the vault.
              </>
            )}
          </p>
        </div>
      </div>

      {actions.result?.kind === 'sent' && actions.result.signature ? (
        <Sent signature={actions.result.signature} />
      ) : null}
      {actions.result?.kind === 'failed' && actions.result.message ? (
        <Refused message={actions.result.message} />
      ) : null}

      <p className="enc-hint">
        <strong>There is no buy button, and there will not be one.</strong> The program has no
        purchase instruction: we seed no liquidity pool and sell no ENC, ever. The faucet is the
        only route in that we control. Anyone may pool a plain SPL token if they want to — we
        neither prevent it nor point at it.
      </p>
    </section>
  )
}

/** Which of the faucet's five outcomes this wallet is in, said plainly. */
function claimSentence(claim: ReturnType<typeof claimView>): string {
  switch (claim.case) {
    case 'below-floor':
      return 'Nothing today. The Emperor is under his floor and the faucet is shut for everyone.'
    case 'already-claimed':
      return 'You have already claimed this epoch. Come back next one — that is the whole shape of it.'
    case 'first-ever':
      return `First time here. This registers you and pays the welcome grant of ${formatEnc(
        claim.grant,
      )} ENC. Your share of the pot arrives on your next claim, not this one.`
    case 'share-due':
      return `You registered last epoch, so there is ${formatEnc(
        claim.share,
      )} ENC waiting${claim.grant > 0n ? `, plus a ${formatEnc(claim.grant)} ENC welcome grant` : ''}.`
    case 'no-share-due':
      return `You missed an epoch, so there is no share this time — it stayed in the vault. Claiming now registers you again.${
        claim.grantTaken ? '' : ' Your welcome grant is still owed and comes with it.'
      }`
  }
}
