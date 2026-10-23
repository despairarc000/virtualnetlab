# Architecture spikes and decision gates
Status: PROPOSED | 2026-10-23. All outputs currently **NOT RUN**. A completed analysis paper is not a benchmark.

## Pre-implementation decision process
For each experiment: hypothesis, alternatives, test inputs, measurements, negative cases, result (links to code/CI/logs), accepted ADR amendment and rollback plan. A lightweight throwaway spike may be built on a branch. Don't merge demo code as production engine without meeting validation.

| Spike | Question | Experiment | Stop/choose rule |
|---|---|---|---|
| S01 | Is Kotlin deterministic scheduler stable and sufficiently light? | 1k/10k/100k events, same-tick order, cancel/reschedule, clock overflow and replay 100 runs on JVM/Android | Require exact semantic hash reproducibility + bounded memory and pause |
| S02 | Typed vs byte/hybrid PDUs? | Ethernet/ARP/IPv4/ICMP/DHCP encode/decode, immutable forwarding and trace growth | Choose smallest maintainable representation meeting data correctness, serialization and mobile budget |
| S03 | Which device/port model? | Home router with LAN bridge group and WAN IP port, switch per-VLAN bridge, PC with multiple NICs | Correct subnets, DHCP ingress binding and distinct broadcast domains with no device-type hacks |
| S04 | Compose Canvas vs custom View/hybrid? | 10/50/100 nodes and ~2x links, zoom, pan, selection at multiple DPIs | Choose measured frame time, touch accuracy, accessibility and memory, not aesthetic preference |
| S05 | JSON+Room vs alternative persistence? | Export/import, schema v0->v1 migration, corrupted files, 100k event log append and interrupted save | Human-readable portable topology and bounded transactional recovery |
| S06 | Android lifecycle execution policy? | Background/resume/rotate/low-memory process death; compare resumed run hash | Explicit pause+recovery, no reliance on unrestricted background execution |
| S07 | How to prove packet-to-device identity? | Same LAN IP on two routers, self-ping, WAN link attach/detach and selected-target trace | Remote success requires remote observed event/identity, not only reply from duplicated address |
| S08 | Protocol fidelity level in first public release? | RFC-driven DHCP/IPv4LL test matrix with Packet Tracer discrepancy recorded | Declare exactly supported states, deviations, unimplemented edge cases |
| S10 | Could we reuse/adapt Filius instead of building engine from scratch? | Read current tagged Filius source, map scheduler/threading/CLI/device/package/UI dependencies, license obligations, prototype an Android-agnostic protocol unit only if authorized | Select reuse vs fresh Kotlin only after demonstrated deterministic behavior, maintenance, Android compatibility and explicit distribution-license policy |
| S09 | Native-only vs optional external backend boundary? | Mock backend describes capabilities/snapshots/commands; compare offline API | Do not implement network connector until proven requirements + security review |

### Gate A: architecture accepted for production
- Primary schema IDs, port/bridge hierarchy, timing units and command/trace contracts reviewed.
- S01, S02, S03, S04 proof linked or reversible interim assumption explicitly signed off.
- License inventory of code dependencies and vendor assets prepared; no accidental Copyleft integration.
- S10 comparison of Filius (GPLv2/v3, architecture viability) against fresh engine completed or explicitly scoped out with documented reason.
- Failure model, data import/security and per-protocol scope reviewed.
- Labs A/B/C from acceptance rewritten into structured fixtures before code is called production-ready.

### Gate B: first end-to-end network engine
- G1/G2 headless tests pass in CI and trace equality across supported platforms.
- External protocol oracle status recorded, unsupported header fields called out.
- Packet inspector faithfully projects trace and context-independent device identity.

### Gate C: Android usability
- Debug APK installed, offline run, normal workflow on constrained real Android device.
- Frame time, input accuracy, RAM, battery and crash recovery measured; regressions gate release.

## What is explicitly NOT decided yet
No final `minSdk`, byte serialization format, plugin ABI, project archive extension, per-event trace retention budget, expected maximum network size, PCAP compatibility, native/emulation bridge implementation, or public performance claim. Define them from results, not assumptions.
