# Implementation roadmap, dependencies and exit gates
Status: PROPOSED v0.2 | 2026-10-23. Goal: improve implementation order without shrinking the user vision. Stages are **evidence gates**, not calendar promises.

## Development tracks
A **engine/protocol correctness**; B **Android UX and persistence**; C **verification/oracles/performance**; D **educational activities/diagnostics**. Tracks run in parallel where interfaces are agreed. A thin Android feasibility prototype should happen EARLY to prevent spending months on an engine that cannot be used comfortably on phones. But the UI can never fake protocol outcomes.

### G0 — Architecture contract & falsification spikes (BLOCKING BEFORE ENGINE API FREEZE)
Deliver: review checklist, source/license register, module boundary spike, packet representation prototype, scheduler proof, Android pan/zoom + trace paging spike, persistence version fixture.
Gate: all P0 questions resolved with tests/measurements or explicitly bounded reversible assumption, baseline ADRs updated, proof on JVM + Android device/emulator; **no long-lived file/plugin API freeze**.
### G1 — Deterministic event/kernel foundation
Deliver: headless JVM project, typed IDs, topology validator, versioned schema draft, event queue with integer ticks + stable sequence, seed RNG, serialized action ingestion, bounded run, trace causal IDs, snapshot/replay tests.
Gate: deterministic traces across 100 repeat runs of same fixture, cancellation and equal-time ordering, time overflow/event storm rejection, invalid topology rejection, tests in CI.
### G2 — Ethernet + host connectivity
Deliver: port/media states, Ethernet frame/MAC, bridge forwarding/flood/learning/aging, ARP, IPv4 on-link, host routes/gateway, ICMP echo, explicit probe identity, path/drop inspector projections.
Gate: golden cases for one-LAN success, switch learning, no forwarding over disconnected link, no cross-domain frame, source self-ping vs remote target, subnet missing-gateway, protocol packet fields.
### G3 — DHCP & IPv4 Link-Local
Deliver: UDP min layer, DHCP client/server, scoped pools, options for router/mask, acquisition/lease/renewal subset, retransmission and IPv4LL policy/probe as supported, WAN/LAN domains.
Gate: user original LAN/WAN/169.254 failure modeled causally; DHCP DORA transitions traced; no invented Offer/Ack; DHCP not disabled by IPv4LL; lease and duplicate-address negatives.
### G4 — Android functional vertical slice
Deliver: installable debug APK, editable topology canvas (port selection), property editor, run/pause/step, OSI/PDU inspector and filtered global event list, device runtime panels, saved/reopened labs.
Gate: physical Android test including 4GB target, long-press and zoom/pan, orientation/process restore, run same fixture with equal engine trace JVM vs phone, offline operation. Automated UI test and graphics profile.
### G5 — VLANs, multi-hop routing, STP subset
Deliver: VLAN/802.1Q, bridging domain separation, static IPv4 routing and route resolution, selected 802.1D STP or RSTP based on independent spec; DTP only if device profile and negotiation FSM justify it.
Gate: switch triangle convergence and loop prevention; no VLAN leak, router two-hop TTL/ARP proof; disallowed VLAN tagged frame; spec-selected timer/oracle tests.
### G6 — Larger learning workflows
Deliver: typed CLI mapped to common canonical config, validation/hints, lab challenge/assessment DSL, layered OSI explanations; DNS/TCP/HTTP/NAT/ACL and IPv6 in individually verified increments; wireless association as clearly bounded model before RF.
Gate: assessment not based on arbitrary UI choices, routing correctness tests, accessible UX, visible supported-feature matrix.
### G7 — Maturity, operations & optional backends
Deliver: traces indexing/compression, scale profiling, stable import/export, crash recovery, migration suite, CI signed release process, expanded devices/protocols; optional external emulation adapter after separate security/license review.
Gate: end-to-end proof on low-end hardware, reproducible builds, privacy/accessibility/legal check, documented known fidelity limits.

## Dependency graph
G0 -> G1 -> G2 -> G3 -> G4 -> G5 -> G6 -> G7 describes primary verification readiness, **not strict team serialization**. B can prototype UI during G0/G1 against recorded events. C starts at G0. Do not build a fictional graph UI waiting for a completed network stack.

## Initial work packets
- W01: implement event queue equal-timestamp tie ordering/cancel/overflow tests, no Android.
- W02: topology IDs, physical port vs L3 interface vs bridge domain validation and JSON fixture.
- W03: typed Ethernet/PDU vs byte representation spike + memory benchmark.
- W04: Android canvas 10/50/100 node touch interactions & detailed frame/memory profile.
- W05: end-to-end host ICMP across switch with path-specific trace assertions.
- W06: router LAN/WAN + DHCP service pool binding and IPv4LL behavior per standards.
- W07: save/import corrupted-project and migration v0->v1 tests.
- W08: scenario DSL exercise with success criterion on trace and intended target.

## Work packet template
Goal; source requirement; scope and explicit NON-goals; input model versions; prerequisites; protocol reference; design alternatives; invariants; positive/negative cases; golden trace/oracle; latency/memory impact; security/license review; code paths; tests executed; CI/Android evidence; checkpoint & documentation updates.

## Definition of done
Production-source test and an independent negative test, semantics matched documented scope; no visual-only fake; verified on selected platform; broken-link & knowledge doctor passed; traceability updated; known limitations stated. Cannot satisfy a gate with screenshots alone.
