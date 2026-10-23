# Phase 1 decision matrix — evidence before irreversible commitments
Status: OPEN until experiments and ADRs | 2026-10-23 | [Master plan](PHASE1_MASTER_PLAN.md), [spike table](../architecture/SPIKES_AND_DECISION_GATES.md).

## Decision policy
Use a documented Decision Card with **Problem / Constraints / Candidates / Source evidence / Experiment / Actual measurements / Adversarial cases / Selection & rationale / Rejected alternatives / Failure trigger / Rollback**. No oral assumption counts as an accepted choice. "Unknown" is a first-class result.

| ID | Risk | Candidate A | Candidate B/C | Evidence required | Disposition today |
|---|---|---|---|---|---|
| D01 Simulation basis | P0 | Independent deterministic Kotlin DES | Adapt Filius; embed ns-3/INET; local emulation | License + source architecture + Android constraints + reproducible trace spike | CONDITIONAL DES |
| D02 State ownership | P0 | Single writer/immutable snapshots | Shared mutable device/UI state | Race/cross-view and replay tests | STRONG PROPOSAL |
| D03 Event clock | P0 | Int64 microsecond/nanosecond ticks + seq | Rational/bigint/float time; alternative event scheduler | Overflow, cancellation, tie-break, same-tick storms, precision | INTEGER RECOMMENDED; UNIT OPEN |
| D04 Packet representation | P0 | Typed immutable PDUs | Byte arrays; hybrid slices/ref-counted payload | Codec conformance, 100k event memory/GC, trace inspectability | OPEN |
| D05 Device topology | P0 | Physical port + bridge domain + logical L3 | Simplified node-edge | Wrong-port DHCP, VLAN isolation, home-router and multi-NIC fixtures | STRUCTURE PROPOSED |
| D06 Work scheduling | P0 | Headless single actor loop | Concurrent per-device actor processing | Reproducible interleaving, latency/throughput, pause latency | SINGLE-WRITER BASELINE |
| D07 Auto-cabling | P1 | Explicit port choice + warning | Pick first compatible port silently | Discoverability/error/legitimate WAN use usability study | EXPLICIT PORTS PROPOSED |
| D08 Android UI drawing | P0 | Compose Canvas | Custom View/hybrid | 10/50/100 node & dense-edge jank/memory, hit tests, accessibility | OPEN |
| D09 Storage | P0 | Versioned JSON lab + database index + segmented trace | Single blob/binary archive | Migration, partial writes, 100k event logs, hostile imports | BOUNDARIES PROPOSED; FORMAT OPEN |
| D10 Lifecycle | P0 | Pause/snapshot & recovery on background/process death | Persistent background service | OS behavior, recovery and battery | PAUSE/SAVE PROPOSED |
| D11 Extensibility | P1 | Built-in versioned capability profiles | Arbitrary imported executable plugins | Security, cost, performance, backward compatibility | DATA-ONLY PROFILES |
| D12 License and reuse | P0 | New Kotlin engine | Adapt GPL Filius, GPL ns-3, OMNeT++ license | Tagged source audit, SPDX/BOM, distribution/legal decision | UNRESOLVED; S10 |
| D13 Time travel | P1 | Deterministic replay from start with sparse checkpoints | Full every-event snapshot | memory/restore cost and semantic trace equality | OPEN |
| D14 CLI | P1 | Custom typed command grammar->same config commands | Run actual Cisco IOS / separate state machine | License, grammar feasibility and cross-view tests | INDEPENDENT GRAMMAR |
| D15 Wireless fidelity | P1 | Layer-2 logical association initially | PHY/radio propagation model | User workflow + correctness oracle/performance | FUTURE SPEC |
| D16 Performance contract | P0 | CPU/RAM/event budgets set by device measurements | Arbitrary threshold | Android 4GB + JVM baseline dataset | NO METRICS YET |
| D17 Observability | P0 | Causal event record with packet lineage | Logging from UI guesses | wrong WAN and local-self-ping trace review | STRONG PROPOSAL |
| D18 Target identity | P0 | Separate network reply and expected-device/path proof | Address-only green check | same-address routers with detached WAN | STRONG PROPOSAL |

## Research-derived constraints
- **DHCP RFC 2131**, sections 3.1 and 4.4, has more than just DORA: INIT/SELECTING/REQUESTING/BOUND, lease renewal and rebinding, distinct per-interface DHCP state, retransmissions and transaction matching. Design with full state-space even if first release implements a documented subset: https://www.rfc-editor.org/rfc/rfc2131.html
- **IPv4LL RFC 3927** requires address selection and probing/announcement/conflict behavior and addresses link-local-only destinations. Never implement it merely as "set 169.254 when DHCP fails" without a scoped simplification notice: https://www.rfc-editor.org/rfc/rfc3927.html
- **Android UI state** may be reclaimed; large laboratory data belongs in local persistent storage, not SavedStateHandle: https://developer.android.com/topic/libraries/architecture/saving-states
- **ns-3** scheduling examples establish a reproducible event-time model and distinguish cancel vs remove memory tradeoffs: https://www.nsnam.org/docs/manual/html/events.html
- **Filius** currently lists Java, educational network simulation and GPLv2-or-GPLv3 in its upstream README: https://gitlab.com/filius1/filius . Use version-pinned LICENSE/code inspection before any copying; upstream activity alone does not establish Android portability.

## Decision signoff procedure
1. Record architecture source at stable URL/revision and applicable license.
2. Design minimal controlled experiment: baseline, adversarial case, known-good oracle and Android device.
3. Execute experiment; attach logs, peak memory, duration, events, correctness, traces and environment details.
4. Compare maintainability and reversibility; explain *why* winner beats alternatives.
5. Update relevant ADR (accepted/rejected/deferred, with effective version).
6. Write no production-dependent interface until unresolved P0 is resolved or has consciously bounded reversible option.
7. Record reviewer, date, commit, proof, and rollback.

## Evidence not yet obtained
No S01–S10 experiments, no source-level current Filius architecture audit, no Kotlin engine, Android performance sample, APK, or protocol engine have been executed in this phase. Documentation/CI only is not design sign-off.
