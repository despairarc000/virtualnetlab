# Technical implementation plan — VirtualNetLab
Status: **REVIEWED PROPOSED v0.2 / implementation NOT STARTED** | 2026-10-23.
This page is the stable plan entrypoint. [Product intent](IDEA_PLAN.md) overrides convenience changes. Decisions with no prototype validation remain provisional; see [review](architecture/ARCHITECTURE_REVIEW.md).

## Chosen implementation direction (conditional on Gate A)
- Headless **deterministic discrete-event** network simulator with typed actor state, integer virtual time, one serialized engine writer and explicit causal event trace.
- Kotlin/JVM engine modules without Android dependencies; native Android Compose application, with measurable canvas renderer choices. UI is a projection/controller, not the simulation.
- Independent validated networking models; composable device profiles distinguish physical ports, bridging/broadcast domains, logical IP interfaces, WAN/LAN roles and optional services.
- A typed packet/message representation initially for fidelity experiments; raw/hybrid codec strategy is NOT frozen.
- Strictly versioned portable laboratory design; run checkpoint and packet trace separate. Offline by default, no privileged network access or vendor firmware in baseline.

## Why this approach?
Read primary-source [comparison](knowledge-system/vault/research/NETWORK_SIMULATORS.md), [architecture audit](architecture/ARCHITECTURE_REVIEW.md), [decision matrix](architecture/DECISION_LOG.md) and [evidence](knowledge-system/vault/EVIDENCE.md). Local full-OS emulation with GNS3/CORE/containerlab is not the primary phone-friendly plan, but a future OPTIONAL adapter is possible after a separate gate. Benchmarks and dependencies must be proven before freezing technical choices.

## Contract inventory
- [Detailed architecture and engine/Android boundaries](architecture/ARCHITECTURE_BLUEPRINT.md)
- [Risk-graded audit](architecture/ARCHITECTURE_REVIEW.md)
- [First-class risks](architecture/RISK_REGISTER.md)
- [Implementation stages, work packets and gates](architecture/IMPLEMENTATION_ROADMAP.md)
- [Adversarial / standards-based tests](architecture/VALIDATION_STRATEGY.md)
- [Experiments that could change decisions](architecture/SPIKES_AND_DECISION_GATES.md)
- [Requirements traceability](architecture/REQUIREMENTS_TRACEABILITY.md)
- [Prior-art review and licensing](architecture/SOURCE_EVALUATION.md)
- [Per-protocol planned/implemented support](knowledge-system/vault/specs/PROTOCOL_MATRIX.md)
- [User-originated lab cases](knowledge-system/vault/specs/LAB_ACCEPTANCE.md)
- [Open questions](knowledge-system/vault/OPEN_QUESTIONS.md)

## Delivery sequence (evidence gates, not calendar commitments)
**G0 — Resolve architecture spikes and decide stable semantics:** event scheduler, packet representation, port/domain model, Android canvas spike, import/security and license check.

**G1 — Engine kernel:** canonical IDs/config, deterministic event queue, seeded replay, validation, packet/trace semantics and budget guards.

**G2 — True wired LAN:** physical interface/links, Ethernet, switching, ARP, IPv4/gateway, ICMP and explicit intended-target probe; headless positive and negative traces.

**G3 — DHCP/IPv4LL and WAN/LAN:** scoped pool, DHCP FSM, retries, leases and independent 169.254/16 policy; reproduce router wrong-port scenario causally.

**G4 — Functional Android lab:** configure, draw, connect, step/run/pause, packet event inspection and offline saved/imported labs; real device profiling and restoration.

**G5 — L2/L3 breadth:** VLAN/802.1Q, STP profile, routing, DTP if genuinely supported; prove loop/VLAN/routing failure cases.

**G6 — Student learning and more protocols:** independent CLI commands, activities/grading, then DNS, NAT, TCP, Wi-Fi, IPv6, dynamic routing and security models in validated subsets.

**G7 — maturity:** scale and performance, safe migration, instrumentation, accessibility/legal/security, optional external emulation integration if justified.

UI proof-of-feasibility starts in G0/G1 **in parallel** with headless proof. Building all protocols before any phone experiment is specifically rejected.

## First important acceptance experiment
PC -> switch -> home-router LAN: DHCP and ICMP work. Move switch uplink to router WAN: frame physically arrives, LAN DHCP pool is inapplicable, no Offer, client eventually has modeled IPv4LL state while continuing its DHCP policy, and outside-subnet ICMP without gateway drops at source. Restore LAN link: DHCP acquisition and correct remote ICMP path must work. Same-address router WAN probe must NOT be falsely marked as verified remote connection. Evidence includes full causal per-port event chain.

## Quality and implementation authority
Read [AGENTS.md](AGENTS.md). No announced protocol support without standards-backed tests, no claim of Android success without APK/device test. Decision acceptance is a planning baseline; actual performance, fidelity, ABI, minimum Android SDK and persistence archive need experiments. Next actionable work is **G0 spikes**, not a full premature engine rewrite.
