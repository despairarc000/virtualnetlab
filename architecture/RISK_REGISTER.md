# Architecture risk register — 2026-10-23
Status: ACTIVE proposed controls; P0 blocks stable API or big implementation. Likelihood/impact qualitative, not measurements.

| ID | Severity | Risk | Mitigation & evidence gate |
|---|---|---|---|
| R01 | P0 | A visually working but semantically false simulation | Headless protocol tests and provenance from actual events |
| R02 | P0 | Irreversible packet API chosen without profiling | Compare typed/byte/hybrid memory, decode fidelity and trace output in spike |
| R03 | P0 | Topology graph collapses physical ports with logical L2/L3 and broadcast domains | Typed port/interface/bridge-domain invariants and WAN-port negative test |
| R04 | P0 | Simulation stalls on storm, zero-time loop, timer explosion or overflow | Bounded scheduler, monotonic integer ticks, cancellation, pause/quotas |
| R05 | P0 | Same IP self-ping falsely validates remote reachability | Target and path identity assertions, disconnect test |
| R06 | P0 | Engine/design/CLI/GUI maintain different configurations | Single-writer canonical configuration commands; cross-view tests |
| R07 | P0 | Overexpansion before first valid end-to-end behavior | Gate-delivered vertical slices; no speculative feature flags as support |
| R08 | P0 | Import vulnerability or unbounded memory allocation from lab | File/schema size ceilings, identity checks, migration, fuzz and atomic save |
| R09 | P0 | Third-party reuse breaches license or proprietary IP | SPDX/legal review per dependency, no vendor firmware or UI assets |
| R10 | P1 | Android 4GB phone freezes or drains battery | Early UX spike, headless throttled snapshot, benchmark & budgets |
| R11 | P1 | Background Android lifecycle loses active run | Pause/checkpoint/restore, autosave process-death tests |
| R12 | P1 | Unbounded trace growth | Segmented/indexed trace and retention/export strategy |
| R13 | P1 | Incorrect DHCP/IPv4LL interplay | Separate FSMs per RFC 2131/RFC 3927; lease/ARP conflict tests |
| R14 | P1 | Unsupported STP/DTP portrayed as working | Capability registry, no synthetic BPDUs without state machine |
| R15 | P1 | Model fidelity diverges from standards without disclosure | Scope versions, deviations, external oracle |
| R16 | P1 | Android touch interactions select wrong WAN vs LAN ports | Explicit port selection, proposed warnings, undo and affordances |
| R17 | P1 | CLI creates conflicting shadow behavior | Parser maps to same commands; cross-view consistency |
| R18 | P1 | Saved scenario unopenable after engine upgrade | Versioned migrations, round-trip/replay fixtures |
| R19 | P1 | Remote/emulator feature weakens offline/privacy promise | Separate optional backend requiring opt-in, security model, no required permissions |
| R20 | P1 | Educational goals depend on hardcoded topology/addresses | Assertions on semantic outcomes and constraints, alternate-valid-solution tests |
| R21 | P1 | Protocol extension API leaks internal implementation | Versioned capability contracts and compatibility tests |
| R22 | P2 | Fidelity needs byte-perfect payload and PCAP | Specify per-protocol codec level and explicit status; validate exported bytes |
| R23 | P2 | App accessibility unusable for motor/visual impairments | Port selection alternatives, contrast/hit areas, TalkBack test |
| R24 | P2 | Performance smoke tests don't model dense topologies | Standardized 10/50/100 node and 1k/10k/100k events scenarios |
| R25 | P2 | Research becomes stale, agent updates unsupported claims | Evidence IDs/status/date, automated link audits, ADR review |
| R26 | P2 | GitHub Actions success conflated with real APK delivery | Separate CI jobs/gates, checksum/artifact inspection, real device test |
| R27 | P2 | Resource constraints incentivize unrealistic instant physics | Distinguish default conceptual latency from configurable measured model |
| R29 | P1 | Reimplementing an entire educational stack without first evaluating a legally reusable existing simulator | S10: inspect Filius code boundaries, actual port/testing cost, license and future maintenance |
| R28 | P2 | Unknown/future link type creates impossible packet semantics | Typed link capabilities and validators with explicit unsupported response |

Owners assigned at first work-item planning; severity re-evaluated after each spike. See [experiments](SPIKES_AND_DECISION_GATES.md) and [acceptance](VALIDATION_STRATEGY.md).
