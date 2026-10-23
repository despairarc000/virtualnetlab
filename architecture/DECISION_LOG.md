# Architecture decision register
Status: ACTIVE planning register | 2026-10-23.
Accepted means accepted **design direction**, not validated implementation or permanent ABI. Refusing to freeze uncertain details is itself a conscious architecture decision.

| ADR | Decision | Status | Revisit when |
|---|---|---|---|
| [0001](../knowledge-system/vault/decisions/ADR-0001-ENGINE.md) | Deterministic DES headless engine instead of fake or local emulation | ACCEPTED_BASELINE | Runnable spike invalidates feasibility |
| [0002](../knowledge-system/vault/decisions/ADR-0002-ANDROID.md) | Kotlin core and Compose Android UI | ACCEPTED_BASELINE | Device performance or portability spike |
| [0003](../knowledge-system/vault/decisions/ADR-0003-STATE-AND-TIME.md) | Separate design/runtime/presentation; single-writer integer-tick scheduler | PROPOSED_CONTRACT | S01/S03 |
| [0004](../knowledge-system/vault/decisions/ADR-0004-PACKET-AND-FIDELITY.md) | Typed PDU baseline, measured codec options, explicit fidelity declarations | PROPOSED_CONTRACT | S02/S08 |
| [0005](../knowledge-system/vault/decisions/ADR-0005-PORTS-AND-IDENTITY.md) | Interface/bridge/port identity and expected-target probe validation | PROPOSED_CONTRACT | S03/S07 |
| [0006](../knowledge-system/vault/decisions/ADR-0006-PERSISTENCE-AND-LIFECYCLE.md) | Portable designs distinct from traces/checkpoints, offline local first | PROPOSED_CONTRACT | S05/S06 |
| [0007](../knowledge-system/vault/decisions/ADR-0007-EXTENSIONS-AND-SECURITY.md) | Guarded capability profiles and optional later emulation, import limits | PROPOSED_CONTRACT | S09 / security review |

Record new architecture choices here, in navigation and risk coverage before beginning work that depends on them.
