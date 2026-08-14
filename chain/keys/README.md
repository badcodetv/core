# Program keypairs

A Solana program's address is the public key of a keypair. Anchor generates that
keypair into `target/deploy/` on first build and reads it from there forever
after — which is a problem, because `target/` is a build artifact. Delete it and
every program silently gets a *new* address, which no longer matches the
`declare_id!` in its own source, and the build fails in a way that looks like a
compiler problem.

So the canonical copy lives here, and `./stack build` restores anything missing
into `target/deploy/` before building. Same address on every machine, in and out
of the container, across as many `rm -rf target` as you like.

## What may go in here

**Development identities only.** These files are committed, so treat every key in
this directory as public.

- `counter-keypair.json` — the toolchain demo program. Deliberately public. It is
  a counter; there is nothing to steal.
- `emperors_new_coin-keypair.json` — the ENC development address, for localnet and
  devnet. Also public, and it must not become the mainnet address: a mainnet
  program keypair is generated at deploy time and backed up out of band.

## What must never go in here

Anything you would deploy to mainnet. A mainnet program keypair is generated at
deploy time, used once, and backed up out of band — see the deployment ticket in
`design/2026-08-06-solana-toolchain-and-emperors-new-coin.md`.

Note that a program keypair is not the upgrade authority. It only authorises the
*initial* deploy to that address; upgrades are authorised by the deployer wallet,
and a program shipped non-upgradeable has no upgrade path at all. The real risk of
publishing one is small — someone could squat the address on a cluster you have
not deployed to yet — but it is a risk with no upside for a real program.
