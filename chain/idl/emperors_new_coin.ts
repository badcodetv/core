/**
 * Program IDL in camelCase format in order to be used in JS/TS.
 *
 * Note that this is only a type helper and is not the actual IDL. The original
 * IDL can be found at `target/idl/emperors_new_coin.json`.
 */
export type EmperorsNewCoin = {
  "address": "5YSzNEzi1Hk9uTCq3SuYDtjYVUUTN9A69AxX2hy58XCT",
  "metadata": {
    "name": "emperorsNewCoin",
    "version": "0.1.0",
    "spec": "0.1.0",
    "description": "Emperor's New Coin — supply pegged to the Fed's M2 money supply."
  },
  "instructions": [
    {
      "name": "breakThePen",
      "docs": [
        "End the editorship, permanently. **Editor only, and there is no way",
        "back** — the paper goes feral."
      ],
      "discriminator": [
        205,
        64,
        174,
        172,
        159,
        39,
        238,
        75
      ],
      "accounts": [
        {
          "name": "editor",
          "docs": [
            "The current editor, and nobody else. Checked in the handler so that \"no",
            "pen exists\" and \"you are not the editor\" come back as different errors."
          ],
          "signer": true
        },
        {
          "name": "config",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  99,
                  111,
                  110,
                  102,
                  105,
                  103
                ]
              }
            ]
          }
        }
      ],
      "args": []
    },
    {
      "name": "claim",
      "docs": [
        "Take your share of yesterday's pot and register for today. **Anyone may",
        "call this**, and it is the only route into the economy that we built."
      ],
      "discriminator": [
        62,
        198,
        214,
        193,
        213,
        159,
        108,
        210
      ],
      "accounts": [
        {
          "name": "claimer",
          "writable": true,
          "signer": true
        },
        {
          "name": "config",
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  99,
                  111,
                  110,
                  102,
                  105,
                  103
                ]
              }
            ]
          }
        },
        {
          "name": "player",
          "docs": [
            "Created on a wallet's first ever claim, at that wallet's expense."
          ],
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  112,
                  108,
                  97,
                  121,
                  101,
                  114
                ]
              },
              {
                "kind": "account",
                "path": "claimer"
              }
            ]
          }
        },
        {
          "name": "epochAccount",
          "docs": [
            "This epoch. Created by whoever claims first, which is what freezes the",
            "pot — everyone who registers today divides today's pot tomorrow."
          ],
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  101,
                  112,
                  111,
                  99,
                  104
                ]
              },
              {
                "kind": "arg",
                "path": "epoch"
              }
            ]
          }
        },
        {
          "name": "previousEpoch",
          "docs": [
            "Last epoch, the one being paid out. **Optional**, and legitimately",
            "absent in three cases: the very first epoch anyone ever claimed in, an",
            "epoch nobody claimed in at all, and one already closed by `close_epoch`.",
            "Omitting it costs the caller their own share and nobody else anything,",
            "so it needs no defending beyond the handler's check that it really is",
            "the previous epoch."
          ],
          "optional": true
        },
        {
          "name": "mint",
          "docs": [
            "Read-only on purpose: **the faucet cannot mint.** Only `sync_m2` may",
            "change the supply, and only against what the Fed published."
          ]
        },
        {
          "name": "vault",
          "docs": [
            "signs the payout."
          ],
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  118,
                  97,
                  117,
                  108,
                  116
                ]
              }
            ]
          }
        },
        {
          "name": "vaultTokenAccount",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "account",
                "path": "vault"
              },
              {
                "kind": "const",
                "value": [
                  6,
                  221,
                  246,
                  225,
                  215,
                  101,
                  161,
                  147,
                  217,
                  203,
                  225,
                  70,
                  206,
                  235,
                  121,
                  172,
                  28,
                  180,
                  133,
                  237,
                  95,
                  91,
                  55,
                  145,
                  58,
                  140,
                  245,
                  133,
                  126,
                  255,
                  0,
                  169
                ]
              },
              {
                "kind": "account",
                "path": "mint"
              }
            ],
            "program": {
              "kind": "const",
              "value": [
                140,
                151,
                37,
                143,
                78,
                36,
                137,
                241,
                187,
                61,
                16,
                41,
                20,
                142,
                13,
                131,
                11,
                90,
                19,
                153,
                218,
                255,
                16,
                132,
                4,
                142,
                123,
                216,
                219,
                233,
                248,
                89
              ]
            }
          }
        },
        {
          "name": "claimerTokenAccount",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "account",
                "path": "claimer"
              },
              {
                "kind": "const",
                "value": [
                  6,
                  221,
                  246,
                  225,
                  215,
                  101,
                  161,
                  147,
                  217,
                  203,
                  225,
                  70,
                  206,
                  235,
                  121,
                  172,
                  28,
                  180,
                  133,
                  237,
                  95,
                  91,
                  55,
                  145,
                  58,
                  140,
                  245,
                  133,
                  126,
                  255,
                  0,
                  169
                ]
              },
              {
                "kind": "account",
                "path": "mint"
              }
            ],
            "program": {
              "kind": "const",
              "value": [
                140,
                151,
                37,
                143,
                78,
                36,
                137,
                241,
                187,
                61,
                16,
                41,
                20,
                142,
                13,
                131,
                11,
                90,
                19,
                153,
                218,
                255,
                16,
                132,
                4,
                142,
                123,
                216,
                219,
                233,
                248,
                89
              ]
            }
          }
        },
        {
          "name": "tokenProgram",
          "address": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
        },
        {
          "name": "associatedTokenProgram",
          "address": "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL"
        },
        {
          "name": "systemProgram",
          "address": "11111111111111111111111111111111"
        }
      ],
      "args": [
        {
          "name": "epoch",
          "type": "u64"
        }
      ]
    },
    {
      "name": "closeEpoch",
      "docs": [
        "Reclaim the rent from an epoch nobody can be paid from any more.",
        "**Anyone may call this**, and keeps the lamports for their trouble."
      ],
      "discriminator": [
        13,
        87,
        7,
        133,
        109,
        14,
        83,
        25
      ],
      "accounts": [
        {
          "name": "closer",
          "writable": true,
          "signer": true
        },
        {
          "name": "config",
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  99,
                  111,
                  110,
                  102,
                  105,
                  103
                ]
              }
            ]
          }
        },
        {
          "name": "epochAccount",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  101,
                  112,
                  111,
                  99,
                  104
                ]
              },
              {
                "kind": "arg",
                "path": "epoch"
              }
            ]
          }
        }
      ],
      "args": [
        {
          "name": "epoch",
          "type": "u64"
        }
      ]
    },
    {
      "name": "fileCopy",
      "docs": [
        "Write this term's column. **Current tenant only, once per term.** The",
        "Emperor's slots are held by a PDA, so they can never be filed."
      ],
      "discriminator": [
        167,
        52,
        237,
        153,
        42,
        12,
        192,
        251
      ],
      "accounts": [
        {
          "name": "tenant",
          "docs": [
            "The tenancy holder, checked against the asset's own record."
          ],
          "signer": true
        },
        {
          "name": "asset",
          "docs": [
            "Boxed: `Asset` is 414 bytes and Anchor deserialises into a 4KB stack",
            "frame. See the note in `place_bid.rs`."
          ],
          "writable": true
        }
      ],
      "args": [
        {
          "name": "index",
          "type": "u8"
        },
        {
          "name": "text",
          "type": "string"
        }
      ]
    },
    {
      "name": "initAsset",
      "docs": [
        "Create one parody asset and its NFT. Called ten times, in order."
      ],
      "discriminator": [
        133,
        1,
        51,
        41,
        37,
        45,
        8,
        38
      ],
      "accounts": [
        {
          "name": "authority",
          "writable": true,
          "signer": true
        },
        {
          "name": "program",
          "docs": [
            "program — the same gate as `initialize`."
          ],
          "address": "5YSzNEzi1Hk9uTCq3SuYDtjYVUUTN9A69AxX2hy58XCT"
        },
        {
          "name": "programData"
        },
        {
          "name": "config",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  99,
                  111,
                  110,
                  102,
                  105,
                  103
                ]
              }
            ]
          }
        },
        {
          "name": "vault",
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  118,
                  97,
                  117,
                  108,
                  116
                ]
              }
            ]
          }
        },
        {
          "name": "asset",
          "docs": [
            "Boxed: `Asset` is 414 bytes and Anchor deserialises into a 4KB stack",
            "frame. See the note in `place_bid.rs`."
          ],
          "writable": true
        },
        {
          "name": "assetMint",
          "docs": [
            "The NFT.",
            "",
            "`metadata_address` points at the mint itself, which is what \"embedded",
            "metadata\" means: there is no separate metadata account to lose."
          ],
          "writable": true
        },
        {
          "name": "vaultNftAccount",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "account",
                "path": "vault"
              },
              {
                "kind": "account",
                "path": "tokenProgram"
              },
              {
                "kind": "account",
                "path": "assetMint"
              }
            ],
            "program": {
              "kind": "const",
              "value": [
                140,
                151,
                37,
                143,
                78,
                36,
                137,
                241,
                187,
                61,
                16,
                41,
                20,
                142,
                13,
                131,
                11,
                90,
                19,
                153,
                218,
                255,
                16,
                132,
                4,
                142,
                123,
                216,
                219,
                233,
                248,
                89
              ]
            }
          }
        },
        {
          "name": "tokenProgram",
          "address": "TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb"
        },
        {
          "name": "associatedTokenProgram",
          "address": "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL"
        },
        {
          "name": "systemProgram",
          "address": "11111111111111111111111111111111"
        },
        {
          "name": "rent",
          "address": "SysvarRent111111111111111111111111111111111"
        }
      ],
      "args": [
        {
          "name": "index",
          "type": "u8"
        },
        {
          "name": "name",
          "type": "string"
        },
        {
          "name": "symbol",
          "type": "string"
        },
        {
          "name": "uri",
          "type": "string"
        },
        {
          "name": "genesisPrice",
          "type": "u64"
        }
      ]
    },
    {
      "name": "initialize",
      "docs": [
        "Create the mint, the vault, the rules and the printer. Once, ever, and",
        "only by the program's upgrade authority."
      ],
      "discriminator": [
        175,
        175,
        109,
        31,
        13,
        152,
        155,
        237
      ],
      "accounts": [
        {
          "name": "authority",
          "docs": [
            "The program's upgrade authority, and nobody else."
          ],
          "writable": true,
          "signer": true
        },
        {
          "name": "program",
          "docs": [
            "record of who may upgrade this program."
          ],
          "address": "5YSzNEzi1Hk9uTCq3SuYDtjYVUUTN9A69AxX2hy58XCT"
        },
        {
          "name": "programData"
        },
        {
          "name": "config",
          "docs": [
            "`init` is what makes this callable exactly once: the second attempt",
            "fails because the account already exists."
          ],
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  99,
                  111,
                  110,
                  102,
                  105,
                  103
                ]
              }
            ]
          }
        },
        {
          "name": "printer",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  112,
                  114,
                  105,
                  110,
                  116,
                  101,
                  114
                ]
              }
            ]
          }
        },
        {
          "name": "vault",
          "docs": [
            "authority, the landlord and the faucet, and it signs by seed."
          ],
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  118,
                  97,
                  117,
                  108,
                  116
                ]
              }
            ]
          }
        },
        {
          "name": "mint",
          "docs": [
            "ENC itself. Classic SPL so every DEX can list it.",
            "",
            "**Freeze authority is `None`, and that is not optional.** A freeze",
            "authority is a live key over other people's coins; omitting the",
            "constraint is what sets it to `None` at creation, irreversibly.",
            "The mint authority stays on the vault PDA forever, so scanners will",
            "report ENC as arbitrarily inflatable — which is true, and is the joke."
          ],
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  109,
                  105,
                  110,
                  116
                ]
              }
            ]
          }
        },
        {
          "name": "vaultTokenAccount",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "account",
                "path": "vault"
              },
              {
                "kind": "const",
                "value": [
                  6,
                  221,
                  246,
                  225,
                  215,
                  101,
                  161,
                  147,
                  217,
                  203,
                  225,
                  70,
                  206,
                  235,
                  121,
                  172,
                  28,
                  180,
                  133,
                  237,
                  95,
                  91,
                  55,
                  145,
                  58,
                  140,
                  245,
                  133,
                  126,
                  255,
                  0,
                  169
                ]
              },
              {
                "kind": "account",
                "path": "mint"
              }
            ],
            "program": {
              "kind": "const",
              "value": [
                140,
                151,
                37,
                143,
                78,
                36,
                137,
                241,
                187,
                61,
                16,
                41,
                20,
                142,
                13,
                131,
                11,
                90,
                19,
                153,
                218,
                255,
                16,
                132,
                4,
                142,
                123,
                216,
                219,
                233,
                248,
                89
              ]
            }
          }
        },
        {
          "name": "tokenProgram",
          "address": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
        },
        {
          "name": "associatedTokenProgram",
          "address": "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL"
        },
        {
          "name": "systemProgram",
          "address": "11111111111111111111111111111111"
        },
        {
          "name": "rent",
          "address": "SysvarRent111111111111111111111111111111111"
        }
      ],
      "args": [
        {
          "name": "params",
          "type": {
            "defined": {
              "name": "initializeParams"
            }
          }
        }
      ]
    },
    {
      "name": "mintCertificate",
      "docs": [
        "Issue the current tenancy's certificate to its holder. Immutable at",
        "issue, never reclaimed, and never worth the asset."
      ],
      "discriminator": [
        53,
        2,
        104,
        84,
        51,
        197,
        179,
        10
      ],
      "accounts": [
        {
          "name": "payer",
          "docs": [
            "Anyone. The certificate lands in the holder's wallet regardless."
          ],
          "writable": true,
          "signer": true
        },
        {
          "name": "config",
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  99,
                  111,
                  110,
                  102,
                  105,
                  103
                ]
              }
            ]
          }
        },
        {
          "name": "asset",
          "docs": [
            "Boxed: `Asset` is 414 bytes and Anchor deserialises into a 4KB stack",
            "frame. See the note in `place_bid.rs`."
          ]
        },
        {
          "name": "holder"
        },
        {
          "name": "vault",
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  118,
                  97,
                  117,
                  108,
                  116
                ]
              }
            ]
          }
        },
        {
          "name": "noneAuthority",
          "docs": [
            "encodes \"no update authority\". The System Program's id *is* that key."
          ],
          "address": "11111111111111111111111111111111"
        },
        {
          "name": "certMint",
          "docs": [
            "Seeded by (asset, term), so one term issues one certificate, ever."
          ],
          "writable": true
        },
        {
          "name": "holderCertAccount",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "account",
                "path": "holder"
              },
              {
                "kind": "account",
                "path": "tokenProgram"
              },
              {
                "kind": "account",
                "path": "certMint"
              }
            ],
            "program": {
              "kind": "const",
              "value": [
                140,
                151,
                37,
                143,
                78,
                36,
                137,
                241,
                187,
                61,
                16,
                41,
                20,
                142,
                13,
                131,
                11,
                90,
                19,
                153,
                218,
                255,
                16,
                132,
                4,
                142,
                123,
                216,
                219,
                233,
                248,
                89
              ]
            }
          }
        },
        {
          "name": "tokenProgram",
          "address": "TokenzQdBNbLqP5VEhdkAS6EPFLC1PHnBqCXEpPxuEb"
        },
        {
          "name": "associatedTokenProgram",
          "address": "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL"
        },
        {
          "name": "systemProgram",
          "address": "11111111111111111111111111111111"
        }
      ],
      "args": [
        {
          "name": "index",
          "type": "u8"
        },
        {
          "name": "term",
          "type": "u64"
        }
      ]
    },
    {
      "name": "passThePen",
      "docs": [
        "Hand the pen to a successor. **Editor only.** The one power in this",
        "program that had to be rotatable, because after T22 there is no upgrade",
        "authority to recover a lost key with."
      ],
      "discriminator": [
        153,
        92,
        248,
        51,
        18,
        64,
        26,
        20
      ],
      "accounts": [
        {
          "name": "editor",
          "docs": [
            "The current editor, and nobody else. Checked in the handler so that \"no",
            "pen exists\" and \"you are not the editor\" come back as different errors."
          ],
          "signer": true
        },
        {
          "name": "config",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  99,
                  111,
                  110,
                  102,
                  105,
                  103
                ]
              }
            ]
          }
        }
      ],
      "args": [
        {
          "name": "newEditor",
          "type": "pubkey"
        }
      ]
    },
    {
      "name": "placeBid",
      "docs": [
        "Bid on a tenancy, escrowing your own ENC. **Signed by the bidder** —",
        "which is the entire reason this replaced the forced sale."
      ],
      "discriminator": [
        238,
        77,
        148,
        91,
        200,
        151,
        92,
        146
      ],
      "accounts": [
        {
          "name": "bidder",
          "writable": true,
          "signer": true
        },
        {
          "name": "config",
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  99,
                  111,
                  110,
                  102,
                  105,
                  103
                ]
              }
            ]
          }
        },
        {
          "name": "asset",
          "docs": [
            "Boxed, like every other `Asset` in this program. It is 414 bytes since",
            "the Gazette landed, and Anchor deserialises accounts into the",
            "instruction's own 4KB BPF stack frame — unboxed, `place_bid` overflowed",
            "it and failed with \"Access violation in stack frame 5\", which names",
            "neither the account nor the size. Boxing is a uniform rule here rather",
            "than a per-instruction judgement so nothing has to be re-measured when",
            "an account list next grows."
          ],
          "writable": true
        },
        {
          "name": "bid",
          "writable": true
        },
        {
          "name": "mint"
        },
        {
          "name": "bidderTokenAccount",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "account",
                "path": "bidder"
              },
              {
                "kind": "const",
                "value": [
                  6,
                  221,
                  246,
                  225,
                  215,
                  101,
                  161,
                  147,
                  217,
                  203,
                  225,
                  70,
                  206,
                  235,
                  121,
                  172,
                  28,
                  180,
                  133,
                  237,
                  95,
                  91,
                  55,
                  145,
                  58,
                  140,
                  245,
                  133,
                  126,
                  255,
                  0,
                  169
                ]
              },
              {
                "kind": "account",
                "path": "mint"
              }
            ],
            "program": {
              "kind": "const",
              "value": [
                140,
                151,
                37,
                143,
                78,
                36,
                137,
                241,
                187,
                61,
                16,
                41,
                20,
                142,
                13,
                131,
                11,
                90,
                19,
                153,
                218,
                255,
                16,
                132,
                4,
                142,
                123,
                216,
                219,
                233,
                248,
                89
              ]
            }
          }
        },
        {
          "name": "escrow",
          "docs": [
            "the escrow token account and the only thing that can sign a release."
          ],
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  101,
                  115,
                  99,
                  114,
                  111,
                  119
                ]
              }
            ]
          }
        },
        {
          "name": "escrowTokenAccount",
          "docs": [
            "Every bidder's ENC, pooled. Created on the first bid ever placed."
          ],
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "account",
                "path": "escrow"
              },
              {
                "kind": "const",
                "value": [
                  6,
                  221,
                  246,
                  225,
                  215,
                  101,
                  161,
                  147,
                  217,
                  203,
                  225,
                  70,
                  206,
                  235,
                  121,
                  172,
                  28,
                  180,
                  133,
                  237,
                  95,
                  91,
                  55,
                  145,
                  58,
                  140,
                  245,
                  133,
                  126,
                  255,
                  0,
                  169
                ]
              },
              {
                "kind": "account",
                "path": "mint"
              }
            ],
            "program": {
              "kind": "const",
              "value": [
                140,
                151,
                37,
                143,
                78,
                36,
                137,
                241,
                187,
                61,
                16,
                41,
                20,
                142,
                13,
                131,
                11,
                90,
                19,
                153,
                218,
                255,
                16,
                132,
                4,
                142,
                123,
                216,
                219,
                233,
                248,
                89
              ]
            }
          }
        },
        {
          "name": "tokenProgram",
          "address": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
        },
        {
          "name": "associatedTokenProgram",
          "address": "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL"
        },
        {
          "name": "systemProgram",
          "address": "11111111111111111111111111111111"
        }
      ],
      "args": [
        {
          "name": "index",
          "type": "u8"
        },
        {
          "name": "amount",
          "type": "u64"
        }
      ]
    },
    {
      "name": "retire",
      "docs": [
        "End it. **Anyone may call this**, and only once the program has gone",
        "long enough without hearing what money is. No key, no discretion, no",
        "announcement — a passer-by can observe that it is over."
      ],
      "discriminator": [
        44,
        138,
        153,
        31,
        222,
        53,
        21,
        16
      ],
      "accounts": [
        {
          "name": "config",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  99,
                  111,
                  110,
                  102,
                  105,
                  103
                ]
              }
            ]
          }
        },
        {
          "name": "printer",
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  112,
                  114,
                  105,
                  110,
                  116,
                  101,
                  114
                ]
              }
            ]
          }
        }
      ],
      "args": []
    },
    {
      "name": "rollTerm",
      "docs": [
        "End a term nobody won: the incumbent keeps it, and any stale high bid is",
        "released to be withdrawn. **Anyone may call this**, and it needs no",
        "signer at all."
      ],
      "discriminator": [
        63,
        192,
        247,
        236,
        51,
        250,
        42,
        239
      ],
      "accounts": [
        {
          "name": "config",
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  99,
                  111,
                  110,
                  102,
                  105,
                  103
                ]
              }
            ]
          }
        },
        {
          "name": "asset",
          "docs": [
            "Boxed: `Asset` is 414 bytes and Anchor deserialises into a 4KB stack",
            "frame. See the note in `place_bid.rs`."
          ],
          "writable": true
        }
      ],
      "args": [
        {
          "name": "index",
          "type": "u8"
        }
      ]
    },
    {
      "name": "settleAuction",
      "docs": [
        "End a term somebody won: the whole winning bid to the outgoing holder,",
        "the tenancy to the winner, a fresh term for both. **Anyone may call",
        "this**, and it asks nothing of either party."
      ],
      "discriminator": [
        246,
        196,
        183,
        98,
        222,
        139,
        46,
        133
      ],
      "accounts": [
        {
          "name": "caller",
          "docs": [
            "Whoever bothered to run it. Pays for any account this has to create and",
            "is otherwise not consulted."
          ],
          "writable": true,
          "signer": true
        },
        {
          "name": "config",
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  99,
                  111,
                  110,
                  102,
                  105,
                  103
                ]
              }
            ]
          }
        },
        {
          "name": "asset",
          "docs": [
            "Boxed: `Asset` is 414 bytes and Anchor deserialises into a 4KB stack",
            "frame. See the note in `place_bid.rs`."
          ],
          "writable": true
        },
        {
          "name": "winningBid",
          "docs": [
            "The winner's escrow record. Closed here; its rent returns to the winner,",
            "who paid it."
          ],
          "writable": true
        },
        {
          "name": "winner",
          "docs": [
            "handler checks against the bid account before anything moves."
          ],
          "writable": true
        },
        {
          "name": "outgoingHolder",
          "docs": [
            "be the vault (the Emperor held it) or the winner (a self-bid renewal)."
          ]
        },
        {
          "name": "mint"
        },
        {
          "name": "outgoingHolderTokenAccount",
          "docs": [
            "Created if absent, payer = caller. Rule 2: nobody gets to veto their own",
            "eviction by closing an account."
          ],
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "account",
                "path": "outgoingHolder"
              },
              {
                "kind": "const",
                "value": [
                  6,
                  221,
                  246,
                  225,
                  215,
                  101,
                  161,
                  147,
                  217,
                  203,
                  225,
                  70,
                  206,
                  235,
                  121,
                  172,
                  28,
                  180,
                  133,
                  237,
                  95,
                  91,
                  55,
                  145,
                  58,
                  140,
                  245,
                  133,
                  126,
                  255,
                  0,
                  169
                ]
              },
              {
                "kind": "account",
                "path": "mint"
              }
            ],
            "program": {
              "kind": "const",
              "value": [
                140,
                151,
                37,
                143,
                78,
                36,
                137,
                241,
                187,
                61,
                16,
                41,
                20,
                142,
                13,
                131,
                11,
                90,
                19,
                153,
                218,
                255,
                16,
                132,
                4,
                142,
                123,
                216,
                219,
                233,
                248,
                89
              ]
            }
          }
        },
        {
          "name": "escrow",
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  101,
                  115,
                  99,
                  114,
                  111,
                  119
                ]
              }
            ]
          }
        },
        {
          "name": "escrowTokenAccount",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "account",
                "path": "escrow"
              },
              {
                "kind": "const",
                "value": [
                  6,
                  221,
                  246,
                  225,
                  215,
                  101,
                  161,
                  147,
                  217,
                  203,
                  225,
                  70,
                  206,
                  235,
                  121,
                  172,
                  28,
                  180,
                  133,
                  237,
                  95,
                  91,
                  55,
                  145,
                  58,
                  140,
                  245,
                  133,
                  126,
                  255,
                  0,
                  169
                ]
              },
              {
                "kind": "account",
                "path": "mint"
              }
            ],
            "program": {
              "kind": "const",
              "value": [
                140,
                151,
                37,
                143,
                78,
                36,
                137,
                241,
                187,
                61,
                16,
                41,
                20,
                142,
                13,
                131,
                11,
                90,
                19,
                153,
                218,
                255,
                16,
                132,
                4,
                142,
                123,
                216,
                219,
                233,
                248,
                89
              ]
            }
          }
        },
        {
          "name": "tokenProgram",
          "address": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
        },
        {
          "name": "associatedTokenProgram",
          "address": "ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL"
        },
        {
          "name": "systemProgram",
          "address": "11111111111111111111111111111111"
        }
      ],
      "args": [
        {
          "name": "index",
          "type": "u8"
        }
      ]
    },
    {
      "name": "spike",
      "docs": [
        "Strike a column to a fixed redaction marker. **Editor only, once per",
        "column per term.** It takes no text: the pen strikes words, it never",
        "authors them."
      ],
      "discriminator": [
        149,
        199,
        30,
        147,
        2,
        236,
        202,
        60
      ],
      "accounts": [
        {
          "name": "editor",
          "signer": true
        },
        {
          "name": "config",
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  99,
                  111,
                  110,
                  102,
                  105,
                  103
                ]
              }
            ]
          }
        },
        {
          "name": "asset",
          "docs": [
            "Boxed: `Asset` is 414 bytes and Anchor deserialises into a 4KB stack",
            "frame. See the note in `place_bid.rs`."
          ],
          "writable": true
        }
      ],
      "args": [
        {
          "name": "index",
          "type": "u8"
        }
      ]
    },
    {
      "name": "syncM2",
      "docs": [
        "Read the oracle and move the supply to `k × M2`. **Anyone may call",
        "this.** The ten Asset PDAs go in `remaining_accounts`, writable, in",
        "index order."
      ],
      "discriminator": [
        183,
        4,
        78,
        180,
        186,
        237,
        229,
        237
      ],
      "accounts": [
        {
          "name": "config",
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  99,
                  111,
                  110,
                  102,
                  105,
                  103
                ]
              }
            ]
          }
        },
        {
          "name": "printer",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  112,
                  114,
                  105,
                  110,
                  116,
                  101,
                  114
                ]
              }
            ]
          }
        },
        {
          "name": "oracle",
          "docs": [
            "knows what shape this account has — a Switchboard feed in a real build,",
            "a mock in a mock one."
          ]
        },
        {
          "name": "mint",
          "writable": true
        },
        {
          "name": "vault",
          "docs": [
            "tokens this instruction may burn."
          ],
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  118,
                  97,
                  117,
                  108,
                  116
                ]
              }
            ]
          }
        },
        {
          "name": "vaultTokenAccount",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "account",
                "path": "vault"
              },
              {
                "kind": "const",
                "value": [
                  6,
                  221,
                  246,
                  225,
                  215,
                  101,
                  161,
                  147,
                  217,
                  203,
                  225,
                  70,
                  206,
                  235,
                  121,
                  172,
                  28,
                  180,
                  133,
                  237,
                  95,
                  91,
                  55,
                  145,
                  58,
                  140,
                  245,
                  133,
                  126,
                  255,
                  0,
                  169
                ]
              },
              {
                "kind": "account",
                "path": "mint"
              }
            ],
            "program": {
              "kind": "const",
              "value": [
                140,
                151,
                37,
                143,
                78,
                36,
                137,
                241,
                187,
                61,
                16,
                41,
                20,
                142,
                13,
                131,
                11,
                90,
                19,
                153,
                218,
                255,
                16,
                132,
                4,
                142,
                123,
                216,
                219,
                233,
                248,
                89
              ]
            }
          }
        },
        {
          "name": "tokenProgram",
          "address": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
        }
      ],
      "args": []
    },
    {
      "name": "withdrawBid",
      "docs": [
        "Take an escrowed bid back. Always available except while it is the",
        "standing high bid of a term that has not settled yet."
      ],
      "discriminator": [
        110,
        53,
        157,
        195,
        147,
        100,
        110,
        73
      ],
      "accounts": [
        {
          "name": "bidder",
          "writable": true,
          "signer": true
        },
        {
          "name": "config",
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  99,
                  111,
                  110,
                  102,
                  105,
                  103
                ]
              }
            ]
          }
        },
        {
          "name": "asset",
          "docs": [
            "Boxed: `Asset` is 414 bytes and Anchor deserialises into a 4KB stack",
            "frame. See the note in `place_bid.rs`."
          ]
        },
        {
          "name": "bid",
          "docs": [
            "Closed on the way out, rent back to the bidder who paid it."
          ],
          "writable": true
        },
        {
          "name": "mint"
        },
        {
          "name": "bidderTokenAccount",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "account",
                "path": "bidder"
              },
              {
                "kind": "const",
                "value": [
                  6,
                  221,
                  246,
                  225,
                  215,
                  101,
                  161,
                  147,
                  217,
                  203,
                  225,
                  70,
                  206,
                  235,
                  121,
                  172,
                  28,
                  180,
                  133,
                  237,
                  95,
                  91,
                  55,
                  145,
                  58,
                  140,
                  245,
                  133,
                  126,
                  255,
                  0,
                  169
                ]
              },
              {
                "kind": "account",
                "path": "mint"
              }
            ],
            "program": {
              "kind": "const",
              "value": [
                140,
                151,
                37,
                143,
                78,
                36,
                137,
                241,
                187,
                61,
                16,
                41,
                20,
                142,
                13,
                131,
                11,
                90,
                19,
                153,
                218,
                255,
                16,
                132,
                4,
                142,
                123,
                216,
                219,
                233,
                248,
                89
              ]
            }
          }
        },
        {
          "name": "escrow",
          "pda": {
            "seeds": [
              {
                "kind": "const",
                "value": [
                  101,
                  115,
                  99,
                  114,
                  111,
                  119
                ]
              }
            ]
          }
        },
        {
          "name": "escrowTokenAccount",
          "writable": true,
          "pda": {
            "seeds": [
              {
                "kind": "account",
                "path": "escrow"
              },
              {
                "kind": "const",
                "value": [
                  6,
                  221,
                  246,
                  225,
                  215,
                  101,
                  161,
                  147,
                  217,
                  203,
                  225,
                  70,
                  206,
                  235,
                  121,
                  172,
                  28,
                  180,
                  133,
                  237,
                  95,
                  91,
                  55,
                  145,
                  58,
                  140,
                  245,
                  133,
                  126,
                  255,
                  0,
                  169
                ]
              },
              {
                "kind": "account",
                "path": "mint"
              }
            ],
            "program": {
              "kind": "const",
              "value": [
                140,
                151,
                37,
                143,
                78,
                36,
                137,
                241,
                187,
                61,
                16,
                41,
                20,
                142,
                13,
                131,
                11,
                90,
                19,
                153,
                218,
                255,
                16,
                132,
                4,
                142,
                123,
                216,
                219,
                233,
                248,
                89
              ]
            }
          }
        },
        {
          "name": "tokenProgram",
          "address": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
        }
      ],
      "args": [
        {
          "name": "index",
          "type": "u8"
        }
      ]
    }
  ],
  "accounts": [
    {
      "name": "asset",
      "discriminator": [
        234,
        180,
        241,
        252,
        139,
        224,
        160,
        8
      ]
    },
    {
      "name": "bid",
      "discriminator": [
        143,
        246,
        48,
        245,
        42,
        145,
        180,
        88
      ]
    },
    {
      "name": "config",
      "discriminator": [
        155,
        12,
        170,
        224,
        30,
        250,
        204,
        130
      ]
    },
    {
      "name": "faucetEpoch",
      "discriminator": [
        164,
        249,
        251,
        129,
        245,
        111,
        173,
        240
      ]
    },
    {
      "name": "player",
      "discriminator": [
        205,
        222,
        112,
        7,
        165,
        155,
        206,
        218
      ]
    },
    {
      "name": "printer",
      "discriminator": [
        111,
        163,
        143,
        162,
        163,
        3,
        241,
        112
      ]
    }
  ],
  "events": [
    {
      "name": "claimed",
      "discriminator": [
        217,
        192,
        123,
        72,
        108,
        150,
        248,
        33
      ]
    },
    {
      "name": "retired",
      "discriminator": [
        106,
        202,
        161,
        255,
        255,
        39,
        222,
        10
      ]
    },
    {
      "name": "synced",
      "discriminator": [
        114,
        244,
        163,
        97,
        99,
        80,
        164,
        70
      ]
    }
  ],
  "errors": [
    {
      "code": 6000,
      "name": "mathOverflow",
      "msg": "Arithmetic overflow or underflow"
    },
    {
      "code": 6001,
      "name": "invalidRate",
      "msg": "A rate was given outside the range 0-10000 basis points"
    },
    {
      "code": 6002,
      "name": "oracleUnavailable",
      "msg": "This build cannot read the oracle"
    },
    {
      "code": 6003,
      "name": "wrongFeed",
      "msg": "The quote is for a different feed than this program accepts"
    },
    {
      "code": 6004,
      "name": "staleRelease",
      "msg": "That M2 release has already been applied"
    },
    {
      "code": 6005,
      "name": "noBaselineM2",
      "msg": "This program has no previous M2 to measure a move against"
    },
    {
      "code": 6006,
      "name": "notUpgradeAuthority",
      "msg": "Only the program's upgrade authority may do that"
    },
    {
      "code": 6007,
      "name": "assetOutOfOrder",
      "msg": "Assets must be initialised in order"
    },
    {
      "code": 6008,
      "name": "notFullyInitialized",
      "msg": "The ten assets are not all initialised yet"
    },
    {
      "code": 6009,
      "name": "invalidAssetIndex",
      "msg": "Asset index out of range"
    },
    {
      "code": 6010,
      "name": "assetAlreadyInitialized",
      "msg": "That asset already exists"
    },
    {
      "code": 6011,
      "name": "wrongHolderAccount",
      "msg": "That token account does not belong to the holder"
    },
    {
      "code": 6012,
      "name": "invalidInterpolationWindow",
      "msg": "Invalid price interpolation window"
    },
    {
      "code": 6013,
      "name": "bidBelowReserve",
      "msg": "That bid is below what M2 says this asset is worth"
    },
    {
      "code": 6014,
      "name": "bidNotHighEnough",
      "msg": "That bid does not beat the standing high bid"
    },
    {
      "code": 6015,
      "name": "termEnded",
      "msg": "This term has ended; it must be settled before bidding reopens"
    },
    {
      "code": 6016,
      "name": "termNotEnded",
      "msg": "This term has not ended yet"
    },
    {
      "code": 6017,
      "name": "staleBidOutstanding",
      "msg": "Withdraw your bid from the previous term first"
    },
    {
      "code": 6018,
      "name": "bidIsStanding",
      "msg": "The standing high bid cannot be withdrawn until the term settles"
    },
    {
      "code": 6019,
      "name": "wrongBidAccount",
      "msg": "That is not the standing high bid for this asset"
    },
    {
      "code": 6020,
      "name": "noQualifyingBid",
      "msg": "No bid cleared the reserve for this term"
    },
    {
      "code": 6021,
      "name": "qualifyingBidExists",
      "msg": "A bid did clear the reserve; this term must be settled"
    },
    {
      "code": 6022,
      "name": "noCertificateDue",
      "msg": "No certificate is issuable for that tenancy"
    },
    {
      "code": 6023,
      "name": "notTheTenant",
      "msg": "Only the current tenant of this column may file copy"
    },
    {
      "code": 6024,
      "name": "alreadyFiled",
      "msg": "This column has already been filed this term"
    },
    {
      "code": 6025,
      "name": "columnSpiked",
      "msg": "This column has been spiked; the next term gets a fresh page"
    },
    {
      "code": 6026,
      "name": "copyTooLong",
      "msg": "That copy is longer than a column"
    },
    {
      "code": 6027,
      "name": "notTheEditor",
      "msg": "Only the editor may do that"
    },
    {
      "code": 6028,
      "name": "penBroken",
      "msg": "The pen is broken; this paper has no editor and never will again"
    },
    {
      "code": 6029,
      "name": "alreadyClaimedThisEpoch",
      "msg": "You have already claimed this epoch"
    },
    {
      "code": 6030,
      "name": "epochNotSettled",
      "msg": "That epoch is not settled yet"
    },
    {
      "code": 6031,
      "name": "wrongEpoch",
      "msg": "That is not the epoch this chain is currently in"
    },
    {
      "code": 6032,
      "name": "notSilentEnough",
      "msg": "This coin has heard about money too recently to be retired"
    },
    {
      "code": 6033,
      "name": "retired",
      "msg": "This coin has retired; the peg has stopped"
    }
  ],
  "types": [
    {
      "name": "asset",
      "docs": [
        "One of the ten parody assets: a Token-2022 NFT, held for a term.",
        "",
        "The NFT itself never leaves program custody — this account records who holds",
        "the *tenancy*, and the holder's own wallet gets a certificate instead. That",
        "is what lets settlement be permissionless without a permanent delegate:",
        "there is no wallet to reach into."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "index",
            "type": "u8"
          },
          {
            "name": "holder",
            "docs": [
              "Who holds it. Equal to the vault PDA when the Emperor holds it — the",
              "client renders that case as \"unowned\". A sentinel rather than an",
              "`Option` so the account layout is fixed-size and the two cases cost the",
              "same to read."
            ],
            "type": "pubkey"
          },
          {
            "name": "priceFrom",
            "docs": [
              "Price interpolation: `price_from` at `interp_start`, `price_to` at",
              "`interp_end`, straight line between, flat outside. Every supply change",
              "rescales both endpoints and restarts the window, so the displayed price",
              "moves every slot rather than jumping once a month."
            ],
            "type": "u64"
          },
          {
            "name": "priceTo",
            "type": "u64"
          },
          {
            "name": "interpStart",
            "type": "i64"
          },
          {
            "name": "interpEnd",
            "type": "i64"
          },
          {
            "name": "termNumber",
            "docs": [
              "Which tenancy this is. Starts at 0 (the Emperor's own) and increments at",
              "every settlement, whether or not the asset changed hands.",
              "",
              "It does two jobs beyond counting: it numbers the certificate, and it is",
              "what makes a bid *stale* — a bid placed in an earlier term is no longer",
              "live, so its escrow is always withdrawable."
            ],
            "type": "u64"
          },
          {
            "name": "termEndsAt",
            "docs": [
              "When the current tenancy ends and anyone may settle it.",
              "",
              "Replaces T7's `last_touched`, which was the rent clock. Nothing else",
              "needed \"when was this last written\" — the price curve carries its own",
              "window — so an explicit term end is the honest field."
            ],
            "type": "i64"
          },
          {
            "name": "highBid",
            "docs": [
              "The standing high bid, in base units. Zero means nobody has bid."
            ],
            "type": "u64"
          },
          {
            "name": "highBidder",
            "docs": [
              "Who placed it. The default (all-zero) key when there is no high bid.",
              "",
              "A bid is *locked* only while it is both the standing high bid and from",
              "the current term; everything else is withdrawable by its owner alone."
            ],
            "type": "pubkey"
          },
          {
            "name": "copy",
            "docs": [
              "What this column currently says. UTF-8, left-aligned, zero-padded.",
              "",
              "**It persists across settlement.** A new tenancy does not blank the page",
              "— yesterday's news stands until today's edition is filed, so a column",
              "nobody writes in keeps saying whatever it last said, for as long as that",
              "takes. Only `file_copy` and `spike` ever write here."
            ],
            "type": {
              "array": [
                "u8",
                280
              ]
            }
          },
          {
            "name": "copyLen",
            "docs": [
              "How many of `copy`'s bytes are real.",
              "",
              "Carried explicitly rather than left for the client to find, because",
              "\"read until the first zero byte\" is a guess: nothing stops a tenant",
              "filing a NUL, and the array is zero-padded either way. Zero means the",
              "column has never been written and the page should render the Emperor's",
              "own default copy — which is what every slot looks like at genesis and",
              "what the vault-held ones look like forever."
            ],
            "type": "u16"
          },
          {
            "name": "copyFiled",
            "docs": [
              "Whether this term's copy has been filed. **Once per term, write-once.**",
              "",
              "Not a rate limit — a decision. Unlimited rewrites would turn moderation",
              "into a war of attrition that only a bot BadCode ran forever could win,",
              "which puts us back in the loop as an operational dependency. One filing",
              "per term makes the pen decisive instead."
            ],
            "type": "bool"
          },
          {
            "name": "copySpiked",
            "docs": [
              "Whether the editor has struck this column this term. Blocks a second",
              "spike, and blocks a re-file: a spiked column stays struck until the term",
              "rolls, or the pen would just be the opening move of that same war."
            ],
            "type": "bool"
          },
          {
            "name": "bump",
            "type": "u8"
          }
        ]
      }
    },
    {
      "name": "bid",
      "docs": [
        "One bidder's escrowed ENC on one asset.",
        "",
        "The escrow itself pools in a single token account; this records who is owed",
        "what. Keyed by (asset, bidder), so a wallet has at most one live bid per",
        "asset and the accounting cannot drift from the pool."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "assetIndex",
            "type": "u8"
          },
          {
            "name": "bidder",
            "type": "pubkey"
          },
          {
            "name": "amount",
            "docs": [
              "Base units sitting in escrow against this bid."
            ],
            "type": "u64"
          },
          {
            "name": "termNumber",
            "docs": [
              "The term this bid was placed in. Once the asset moves past it, the bid",
              "is dead and the money is the bidder's to take back."
            ],
            "type": "u64"
          },
          {
            "name": "bump",
            "type": "u8"
          }
        ]
      }
    },
    {
      "name": "claimed",
      "docs": [
        "What one claim actually paid, so the page can say which of the three things",
        "happened — yesterday's share, a welcome grant, or nothing and why."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "wallet",
            "type": "pubkey"
          },
          {
            "name": "epoch",
            "type": "u64"
          },
          {
            "name": "share",
            "type": "u64"
          },
          {
            "name": "grant",
            "type": "u64"
          },
          {
            "name": "pot",
            "docs": [
              "The pot this claim just registered for, collectable next epoch."
            ],
            "type": "u64"
          },
          {
            "name": "registrants",
            "type": "u32"
          },
          {
            "name": "aboveFloor",
            "docs": [
              "False when the vault sits at or below its floor, where nothing pays out."
            ],
            "type": "bool"
          }
        ]
      }
    },
    {
      "name": "config",
      "docs": [
        "The rules. Written once at `initialize`, never changed afterwards.",
        "",
        "There is deliberately no instruction that mutates the economic parameters —",
        "not gated behind an authority, not present at all — because the program ships",
        "non-upgradeable and \"not even we can change the rule\" has to be literally",
        "true, not merely intended.",
        "",
        "Two fields here move without any key at all, and both are **one-way",
        "latches**: `initialized_assets` counts up to ten during bootstrap and then",
        "never moves again, and `retired` flips once, permissionlessly, when the",
        "program has gone long enough without hearing a new M2 figure. Neither can be",
        "set back, and neither is anyone's decision — the second is a condition the",
        "program checks about itself.",
        "",
        "One field here **is** a key: `editor`, the pen. It is the single exception in",
        "the whole program and it is deliberately narrow — no key over the money, one",
        "pen over the words. See its own doc for exactly what it can reach."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "mint",
            "docs": [
              "The ENC mint. Classic SPL, 6 decimals, freeze authority `None`."
            ],
            "type": "pubkey"
          },
          {
            "name": "vault",
            "docs": [
              "The vault PDA — mint authority, landlord, and the Emperor's pocket."
            ],
            "type": "pubkey"
          },
          {
            "name": "expectedFeedId",
            "docs": [
              "The Switchboard feed this program will accept a quote from, and only",
              "this one. A feed *is* the hash of its own fetch job, so pinning the hash",
              "pins the data source itself: no key exists that could repoint it."
            ],
            "type": {
              "array": [
                "u8",
                32
              ]
            }
          },
          {
            "name": "k",
            "docs": [
              "Base units of ENC per unit of `m2_value`. `supply = k × m2_value`."
            ],
            "type": "u64"
          },
          {
            "name": "encDecimals",
            "docs": [
              "Decimals on the mint. Six: nine would overflow u64 at this supply."
            ],
            "type": "u8"
          },
          {
            "name": "faucetAlphaBps",
            "docs": [
              "Share of the distributable surplus paid out per epoch, in basis points."
            ],
            "type": "u16"
          },
          {
            "name": "floorBps",
            "docs": [
              "The vault's floor, in basis points of total supply. Below it the faucet",
              "pays nothing at all — no share, no welcome grant."
            ],
            "type": "u16"
          },
          {
            "name": "welcomeGrant",
            "docs": [
              "One-off payment to a wallet's first ever claim, in base units."
            ],
            "type": "u64"
          },
          {
            "name": "grantsPerEpoch",
            "docs": [
              "How many welcome grants may be issued in a single epoch."
            ],
            "type": "u16"
          },
          {
            "name": "termSeconds",
            "docs": [
              "How long one tenancy lasts, in seconds.",
              "",
              "Aligned with `PRICE_INTERPOLATION_SECONDS` on purpose: a term is exactly",
              "as long as it takes a price to finish travelling to its new target, so",
              "each auction settles against a price that has arrived rather than one",
              "still in motion."
            ],
            "type": "i64"
          },
          {
            "name": "epochSeconds",
            "docs": [
              "How long one faucet epoch lasts, in seconds. One day in the shipped",
              "parameters; see `DEFAULT_SECONDS_PER_EPOCH` for why it is a field.",
              "",
              "It is a **PDA seed input**, so it decides which `FaucetEpoch` accounts",
              "can ever exist. Fixed at genesis and without a setter, like everything",
              "else here."
            ],
            "type": "i64"
          },
          {
            "name": "retirementSilenceSeconds",
            "docs": [
              "How long the program must go without a new M2 figure before anyone may",
              "`retire` it, in seconds. A year in the shipped parameters.",
              "",
              "Long on purpose: the flag is irreversible on a non-upgradeable program,",
              "so a Switchboard outage or a bad month must never be able to end the",
              "artwork. M2 publishes monthly; a year is twelve missed chances."
            ],
            "type": "i64"
          },
          {
            "name": "maxChangeBps",
            "docs": [
              "How far the peg will move in one `sync_m2`, in basis points.",
              "",
              "**A speed limit, not a veto** (T29). A release beyond it is absorbed",
              "over several permissionless calls rather than refused — refusing it was",
              "permanent, because the baseline only advances on success. There is",
              "deliberately no companion cap in absolute base units: any fixed number",
              "of tokens is exceeded by an ordinary month once M2 has grown enough, and",
              "on a non-upgradeable program that is a timer, not a guard."
            ],
            "type": "u16"
          },
          {
            "name": "initializedAssets",
            "docs": [
              "Counts up to `ASSET_COUNT` during bootstrap, then never moves."
            ],
            "type": "u8"
          },
          {
            "name": "retired",
            "docs": [
              "Whether the coin has noticed its own end. One-way, and nobody's",
              "decision: `retire` sets it when the silence condition is already true,",
              "and no instruction anywhere can set it back.",
              "",
              "The **only** thing it stops is `sync_m2`. Everything else keeps running",
              "on the last prices the Fed ever reported — the machine grinding on,",
              "auctioning flags at the valuations of a vanished world. That also",
              "removes the one hazard a freeze would have carried: escrow that can",
              "never be withdrawn."
            ],
            "type": "bool"
          },
          {
            "name": "editor",
            "docs": [
              "The editor's pen: the one key in this program, and it can only strike",
              "words.",
              "",
              "It reaches exactly one instruction, `spike`, which replaces a column's",
              "copy with `SPIKE_MARKER` — a fixed string it does not get to choose —",
              "once per column per term. **The blast radius is ten columns a month, and",
              "it cannot move a token.** Not one ENC, not one asset NFT, not one",
              "certificate; the shape test in `initialize.ts` asserts the key appears in",
              "no instruction that touches a token account.",
              "",
              "It exists because there is no on-chain answer to vile text and",
              "pretending otherwise is how this gets ugly. A newspaper has an editor.",
              "",
              "`Some` while a pen exists, `None` once `break_the_pen` has been called —",
              "which is irrevocable, because `pass_the_pen` needs a current editor to",
              "sign and nothing else writes this field. Rotatable on purpose: a lost or",
              "stolen key must be survivable without an upgrade authority to fall back",
              "on, since by T22 there will not be one."
            ],
            "type": {
              "option": "pubkey"
            }
          },
          {
            "name": "bump",
            "type": "u8"
          }
        ]
      }
    },
    {
      "name": "faucetEpoch",
      "docs": [
        "One day of the faucet.",
        "",
        "Created by whoever claims first that day, which is also what snapshots the",
        "pot. Everyone who registers today divides *today's* pot tomorrow."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "epoch",
            "type": "u64"
          },
          {
            "name": "pot",
            "docs": [
              "`α × max(0, vault − floor × supply)`, frozen at creation. Frozen because",
              "a pot that moved with the vault balance could not be divided fairly",
              "among a set of registrants that is still growing."
            ],
            "type": "u64"
          },
          {
            "name": "registrants",
            "docs": [
              "How many wallets registered during this epoch. The divisor for this",
              "pot — *next* epoch."
            ],
            "type": "u32"
          },
          {
            "name": "grantsIssued",
            "docs": [
              "Welcome grants issued during this epoch, capped at `grants_per_epoch`."
            ],
            "type": "u16"
          },
          {
            "name": "bump",
            "type": "u8"
          }
        ]
      }
    },
    {
      "name": "initializeParams",
      "docs": [
        "The economic parameters, chosen once and then unchangeable.",
        "",
        "Supplied by the caller rather than hardcoded so `chain/params.genesis.json`",
        "stays the single source of truth and T15 can replace the placeholders",
        "without touching Rust. Everything here is validated below; nothing here has",
        "a setter anywhere in the program."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "expectedFeedId",
            "docs": [
              "The Switchboard feed this program will ever accept a quote from."
            ],
            "type": {
              "array": [
                "u8",
                32
              ]
            }
          },
          {
            "name": "k",
            "docs": [
              "Base units of ENC per unit of `m2_value`."
            ],
            "type": "u64"
          },
          {
            "name": "faucetAlphaBps",
            "type": "u16"
          },
          {
            "name": "floorBps",
            "type": "u16"
          },
          {
            "name": "welcomeGrant",
            "type": "u64"
          },
          {
            "name": "grantsPerEpoch",
            "type": "u16"
          },
          {
            "name": "termSeconds",
            "type": "i64"
          },
          {
            "name": "epochSeconds",
            "type": "i64"
          },
          {
            "name": "retirementSilenceSeconds",
            "type": "i64"
          },
          {
            "name": "maxChangeBps",
            "type": "u16"
          },
          {
            "name": "editor",
            "docs": [
              "Who holds the editor's pen at genesis, or `None` for a paper that is",
              "feral from birth.",
              "",
              "**Not an economic parameter**, which is why it is not in",
              "`params.genesis.json` alongside the rest — it is a key, chosen at",
              "deployment, and the only one this program ever accepts. It can be",
              "rotated afterwards by its holder and broken by its holder, and by",
              "nobody else, ever."
            ],
            "type": {
              "option": "pubkey"
            }
          }
        ]
      }
    },
    {
      "name": "player",
      "docs": [
        "A wallet that has played."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "wallet",
            "type": "pubkey"
          },
          {
            "name": "lastRegisteredEpoch",
            "docs": [
              "The last epoch this wallet registered in.",
              "",
              "One field does two jobs: it rejects a second claim in the same epoch",
              "(`== current`), and it decides eligibility for the previous pot",
              "(`== current - 1`). Keeping them as one field means they cannot",
              "disagree."
            ],
            "type": "u64"
          },
          {
            "name": "welcomeGrantTaken",
            "docs": [
              "Whether the one-off welcome grant has been taken. Never resets."
            ],
            "type": "bool"
          },
          {
            "name": "bump",
            "type": "u8"
          }
        ]
      }
    },
    {
      "name": "printer",
      "docs": [
        "What the Fed last told us, and what we did about it."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "m2Value",
            "docs": [
              "M2SL in **billions of USD, fixed-point with 6 decimals**.",
              "`22176.1` is stored as `22_176_100_000`. Getting this wrong by a factor",
              "of a thousand is the easiest catastrophic mistake available here."
            ],
            "type": "u64"
          },
          {
            "name": "m2ReleaseDate",
            "docs": [
              "Unix seconds of the **Fed's release**, not of our sync. This is what the",
              "anti-double-mint guard compares, because it is the only timestamp an",
              "attacker cannot advance by waiting."
            ],
            "type": "i64"
          },
          {
            "name": "lastSyncSlot",
            "docs": [
              "Slot of the last successful sync. Informational."
            ],
            "type": "u64"
          },
          {
            "name": "lastSyncAt",
            "docs": [
              "Unix seconds of the last successful sync — **our** clock, not the Fed's.",
              "",
              "This is the retirement clock, and it has to be wall time rather than the",
              "slot beside it: a program cannot convert a slot into a date, so",
              "`last_sync_slot` can never answer \"how long has it been\". Seeded at",
              "`initialize` rather than left at zero, or the coin would be a year",
              "overdue for retirement the moment it was born.",
              "",
              "It advances only on a **successful** sync, which is what makes silence",
              "mean silence: a feed still serving a dead series fails the release-date",
              "guard, this clock stops, and `retire` becomes true on schedule."
            ],
            "type": "i64"
          },
          {
            "name": "targetSupply",
            "docs": [
              "`k × m2_value` at the last sync — what supply was aimed at.",
              "",
              "Actual supply can sit *above* this, when a burn was larger than the",
              "vault could cover. That is the honest invariant: `supply ≥ k × M2`."
            ],
            "type": "u64"
          },
          {
            "name": "bump",
            "type": "u8"
          }
        ]
      }
    },
    {
      "name": "retired",
      "docs": [
        "Emitted once, ever. The receipt for the end of the artwork."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "at",
            "docs": [
              "When the bit was flipped."
            ],
            "type": "i64"
          },
          {
            "name": "lastSyncAt",
            "docs": [
              "The last time anyone told this program what money was."
            ],
            "type": "i64"
          },
          {
            "name": "finalM2Value",
            "docs": [
              "What the Fed last said, and when they said it — the numbers the",
              "auctions go on trading at forever."
            ],
            "type": "u64"
          },
          {
            "name": "finalM2ReleaseDate",
            "type": "i64"
          }
        ]
      }
    },
    {
      "name": "synced",
      "docs": [
        "Emitted on every successful sync, so the website and any indexer can show",
        "what the printer did without replaying the whole chain."
      ],
      "type": {
        "kind": "struct",
        "fields": [
          {
            "name": "m2Value",
            "type": "u64"
          },
          {
            "name": "m2ReleaseDate",
            "type": "i64"
          },
          {
            "name": "targetSupply",
            "type": "u64"
          },
          {
            "name": "supplyDelta",
            "docs": [
              "Positive when minted, negative when burned."
            ],
            "type": "i128"
          },
          {
            "name": "uncoveredBurn",
            "docs": [
              "How much of a burn the vault could not cover. Non-zero means supply is",
              "left above target on purpose."
            ],
            "type": "u64"
          },
          {
            "name": "releaseCommitted",
            "docs": [
              "False when this was one capped step of a catch-up walk rather than the",
              "whole move — the release date is not committed until the walk lands, so",
              "an indexer can tell \"still catching up\" from \"done\"."
            ],
            "type": "bool"
          },
          {
            "name": "slot",
            "type": "u64"
          }
        ]
      }
    }
  ]
};
