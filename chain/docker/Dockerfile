# The Solana development toolchain, pinned.
#
# Why this image exists: the host install is fragile and platform-specific.
# Anchor's prebuilt binaries need glibc 2.39, which Ubuntu 22.04 does not have,
# so a host install has to build Anchor from source (slow, and it breaks when
# the host's Rust moves). Ubuntu 24.04 ships glibc 2.39, so inside here the
# prebuilt just works and the versions stop depending on whose laptop it is.
#
# Versions must match chain/versions.json. They are passed in as build args by
# docker-compose.yml, which reads them from chain/.env (written by `chain image`).
FROM ubuntu:24.04

ARG RUST_VERSION=1.97.1
ARG AGAVE_VERSION=3.1.10
ARG ANCHOR_VERSION=1.1.2
ARG NODE_MAJOR=22

# Match the host user so files written into the bind-mounted repo (chain/target,
# chain/idl) are owned by you and not by root. Override with `--build-arg UID=`.
ARG UID=1000
ARG GID=1000

ENV DEBIAN_FRONTEND=noninteractive
ENV CARGO_HOME=/home/dev/.cargo
ENV RUSTUP_HOME=/home/dev/.rustup
ENV PATH=/home/dev/.cargo/bin:/home/dev/.local/share/solana/install/active_release/bin:/home/dev/.avm/bin:$PATH

RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential ca-certificates clang cmake curl git libssl-dev \
      libudev-dev llvm pkg-config protobuf-compiler python3 ssh \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL "https://deb.nodesource.com/setup_${NODE_MAJOR}.x" | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*

# Ubuntu 24.04 ships a stock `ubuntu` user at uid 1000, which collides with the
# host user we want to mirror. Take the uid over rather than working around it.
RUN userdel -r ubuntu 2>/dev/null || true \
    && groupadd -g "${GID}" dev 2>/dev/null || true \
    && useradd -m -u "${UID}" -g "${GID}" -s /bin/bash dev \
    && mkdir -p /work && chown "${UID}:${GID}" /work

USER dev
WORKDIR /home/dev

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \
      | sh -s -- -y --no-modify-path --default-toolchain "${RUST_VERSION}" --profile minimal \
    && rustup component add rustfmt clippy

# ORDER IS LOAD-BEARING: install Anchor BEFORE Solana.
#
# `avm install` downloads its own matching Agave and drops it into the active
# release directory, silently overwriting whatever Solana you installed first.
# Installing Solana second means our pin is the one that survives. Getting this
# backwards produces a working setup on a version you did not choose.
RUN cargo install --git https://github.com/coral-xyz/anchor avm --tag "v${ANCHOR_VERSION}" --locked \
    && avm install "${ANCHOR_VERSION}" \
    && avm use "${ANCHOR_VERSION}"

RUN sh -c "$(curl -sSfL https://release.anza.xyz/v${AGAVE_VERSION}/install)"

# Fail the build rather than shipping an image whose versions drifted from the
# pins — a silently-wrong toolchain is the expensive failure mode here.
RUN set -eux; \
    rustc --version   | grep -q "${RUST_VERSION}"; \
    solana --version  | grep -q "${AGAVE_VERSION}"; \
    anchor --version  | grep -q "${ANCHOR_VERSION}"; \
    node --version    | grep -q "v${NODE_MAJOR}\."; \
    cargo build-sbf --version

WORKDIR /work/chain
CMD ["bash"]
