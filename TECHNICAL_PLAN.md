# TECHNICAL PLAN — VirtualNetLab
Status: PROPOSED architecture / accepted planning baseline | 2026-10-23. No runtime is implemented.

## Evidence and comparison
Read [comparative research](knowledge-system/vault/research/NETWORK_SIMULATORS.md), [ADR-0001](knowledge-system/vault/decisions/ADR-0001-ENGINE.md), [ADR-0002](knowledge-system/vault/decisions/ADR-0002-ANDROID.md), and [protocol matrix](knowledge-system/vault/specs/PROTOCOL_MATRIX.md). Research supports design hypotheses, not claims of experimentally benchmarked Android builds.

## Chosen approach
A deterministic **discrete-event packet/network simulator** as an independently testable Kotlin core, backed by a touch-native Android UI built with Kotlin + Jetpack Compose. Use simulated frames and layered protocol state machines, not Linux namespaces, privileged tun/tap or virtualization on the user's phone. Design versioned extension points for optional future remote/external emulation but do NOT depend on them for offline labs. Re-evaluate migration to native engine/other platforms based on measured bottlenecks and licensing.

## Architectural boundaries
1. **Topology & configuration model**: device and port IDs, link endpoint IDs, VLAN membership, interfaces, IP settings, services, policies, physical/link status. Strict schema with stable IDs, migration and validation. Graphical coordinates are presentation metadata only.
2. **Deterministic scheduler**: simulation clock, monotonic sequence ID for same-time ordering, ordered event queue, bounded step/run/pause/replay, deterministic seed, reproducible snapshots. No wall clock dependence inside models.
3. **Link and frame layer**: Ethernet source/destination MAC, EtherType, VLAN tag when supported, rate/latency/MTU/link-up state, unicast/flood/broadcast, MAC learning/aging, frame delivery/drop.
4. **Node protocol actors**: hosts, switches, routers with separate port ingress/egress and interface roles. ARP cache and timers; IP subnet and routing decisions; ICMP; UDP/DHCP state machines. Protocol code schedules events, never directly manipulates drawings.
5. **Services and CLI**: DHCP server pools scoped to binding/interface; host DHCP client with DORA and retry/APIPA; evolving router/switch management commands mapped into canonical configuration; no fictional hardware OS.
6. **Trace and diagnostics**: every event carries parent/correlation IDs, actor, ingress/egress, before/after state reference, packet details, reason code, and outcomes. Diagnostic explanation is derived from trace facts.
7. **Persistence**: explicit versioned JSON schema for topology/configuration (or alternative after ADR); optional snapshot plus trace; import validates references, limits, dup IDs, unknown enums and version.
8. **Android presentation**: pan/zoom topology, touch selection/wiring, device property editor, terminal, simulation filters, timeline, packet inspector; render only immutable engine snapshots.

### Behavior execution contract
Input command -> validate -> mutate canonical config or inject test stimulus -> scheduler event -> interface actor -> protocol dispatch -> enqueue outgoing events -> append immutable trace -> display snapshot; rejected actions emit explicit reason.
No renderer/CLI bypass of engine state. Event order key = (simulation_timestamp, insertion_sequence). Pausing freezes simulated scheduling but not Android UI.

### Special test identity rule
A ping is a test tuple of source *interface*, explicit destination *address*, optional expected target device/interface, and expected path. Report: (a) echo reply from that exact destination, (b) whether expected target/interface was reached, (c) any local delivery/self-match. Don't equate address-only echo with proof of a different device's reachability.

## Delivery stages and release gates
### Stage 0 — Repository & executable knowledge system (NOW)
Vision/plan, comparisons, scope, ADRs, ICM routes, Graphify dependency graph, vault, navigation, task contracts, doctor + CI. Gate: docs linked, scripts tested, no feature falsely represented as implemented.
### Stage 1 — Engine thin vertical slice
Topology schema, interface/link events, Ethernet frames, switch MAC learning/flooding, host IPv4/ARP/ICMP, scheduler and detailed trace. Headless JVM tests first. Gate: tests prove positive and negative same-LAN pings, exact event chronology, no off-topology delivery.
### Stage 2 — DHCP and WAN/LAN interface semantics
UDP minimal support, DHCP DORA/lease/client retransmission, pool binding, APIPA policy, LAN/WAN isolation, missing gateway diagnostic and target disambiguation. Gate: reproduce real user investigation with packet-level assertions, and explicit negative WAN-port case.
### Stage 3 — Native Android lab
Compose canvas, connect-port selection, config editor, event list, PDU/OSI inspector, filters, step/play/pause/reset, import/export, offline persistence. Gate: install and test APK on constrained Android hardware; verify replay matches JVM engine.
### Stage 4 — Switching & network services
802.1Q VLANs, trunk/access, STP (with legitimate BPDU/state/timers), routing/static routes, gateway support; DTP only if explicitly modeled and covered, not a decorative label. Gate: convergence/failure tests, forbidden path tests, no VLAN leakage.
### Stage 5 — Teaching workflow and broader stack
CLI abstraction, guided activities/assessment, diagnostics, IPv6, TCP, DNS, NAT, Wi-Fi and ACL; add protocols one by one behind truthfully declared support levels. Gate: conformance, regression and UX tests.
### Stage 6 — Performance and extensions
Profiling large topologies, incremental trace storage, efficient event queues, extensible models, optional external emulation bridge, independent Android release validation. Gate: measured benchmarks, memory/time budgets and security review.

## First acceptance scenarios
Detailed executable narratives in [LAB_ACCEPTANCE.md](knowledge-system/vault/specs/LAB_ACCEPTANCE.md). Prioritize:
- A: PC0--Switch0--Router0 LAN; DHCP 192.168.0.100–149, default gateway 192.168.0.1 and ICMP successful.
- B: Switch0 accidentally to Router0 Internet; DHCP Discover reaches that ingress, no bound pool, drops; client retries then APIPA, no gateway, ICMP outside subnet drops on PC.
- C: two routers with identical LAN IPs and WAN physical cable; PDU MUST not silently claim remote WAN communication if ICMP destination resolves locally.
- D: switch background STP/DTP events interleave independently of manually created ICMP; global queue filter affects view, not routing.
- E: disconnected destinations, subnet mismatch, stale ARP, link down, duplicated IDs and malformed project rejection.

## Unit and integration testing
Headless golden-trace fixtures, assertion of protocol/port/state/reason, seeded replay, adversarial imports, timer and queue limits, independent oracle based on RFC/standards/network captures where legally accessible. CI runs knowledge doctor, unit tests, topology tests, lint, Android instrumented tests when available. Never claim tests passed without output.

## Early design risks and mitigation
- Sim fidelity: source-level standards notes and deviation registry per feature; independent negative tests.
- Scope explosion: vertical slices tied to user experiments with explicit support status.
- Android constrained resources: headless engine profiling, lazy UI snapshots, bounded traces, avoid all-node recomputation.
- CLI complexity: parse typed commands into canonical config, no separate CLI state.
- Legal/branding: independent assets and implementation, no proprietary firmware or unauthorized compatibility claims.
- External emulators: optional and deferred; Linux virtualization is not a safe default assumption on Android.

## Decisions pending measurement
Event representation/payload memory cost; persistence serializer; trace compression; graph UI performance; Android minimum SDK; Wi-Fi fidelity target; protocol standards versions; potential engine portability. Track evidence in [OPEN_QUESTIONS.md](knowledge-system/vault/OPEN_QUESTIONS.md).

## Next actionable engineering task
Design and implement the *headless Stage 1* topology schema, event ordering contract, link/frame actors, and test harness; only then start UI interactions. Branch convention: implementation-specific work on `implementation/<topic>`; main keeps accepted vision, cross-cutting vault, navigational contracts. Do not overwrite other active work.
