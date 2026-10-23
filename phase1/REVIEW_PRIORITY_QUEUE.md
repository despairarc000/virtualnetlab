# Prioritized planning queue and critical path
Status: ACTIVE planning guidance | 2026-10-23 | [Phase 1 master](PHASE1_MASTER_PLAN.md), [P0 evidence debt](REVIEW_OPEN_ITEMS.md), [verification](PLANNING_VERIFICATION_MATRIX.md).

## Dependency-ranked sequence
**1. Mission and domain agreement**: Audit [top-down capability map](TOP_DOWN_CAPABILITY_MAP.md), [device catalog](DEVICE_CAPABILITY_CATALOG.md) and [cross-layer gap list](CROSS_LAYER_GAPS.md) against all user workflows. Confirm exact Stage 1–4 acceptance and future architecture hooks, without overclaiming advanced features.

**2. Build-versus-adapt feasibility S10**: Inspect current source/CI/license of Filius and relevant comparable systems, map port/link/domain model, threading and runtime/UI coupling, compare clean Kotlin DES prototype. If adaptation is chosen, validate app redistribution/license policy FIRST.

**3. Typed domain model S03**: Resolve physical port–bridge–L3–service schema, address family, route representation, topology edit semantics and profile capability IDs; independent two-implementer tabletop trace for WAN/LAN and multiNIC/VLAN.

**4. Event scheduler S01 and packet buffer S02**: Prove deterministic event kernel, cancellation/overflow/storm containment and typed/hybrid/byte codec memory/data fidelity. These are foundations for every later protocol.

**5. Early Android feasibility S04**: Test Compose/custom View 10/50/100 nodes, port hit testing, pan/zoom, accessible alternative. Do this in parallel with 2–4, NOT after full network implementation.

**6. Near-term protocol and causal diagnostic validation**: RFC 826/791/792/1122/1812/2131/2132/3927 sourced state-machine tables; create machine-readable trace assertions for PC-switch-router LAN/WAN, ARP, self-ping, DHCP/IPv4LL. Select source-target-path verification semantics. Gate S07/S08.

**7. Persistence/security/lifecycle S05/S06**: Versioned design vs run/checkpoint, zero trust imported lab and retained trace, corruption/disk-full, process death, resource quota, arbitrary code/real packet isolation. Compare storage/serialization alternatives with evidence.

**8. Cross-disciplinary review and Gate A**: Resolve all P0 findings or consciously accept reversible constrained assumptions, update ADRs and decision matrix, trace each requirement to proof, sign off only with measured environment/CI and real Android evidence. End state [exit audit](EXIT_AUDIT.md) is ACCEPTED, not just many pages.

## Next most valuable single experiment
S03: write a *throwaway*, platform-independent topology schema and three fixtures (LAN bridge, WAN misplug, two isolated duplicate router IPs) with validators and exact path/identity assertions. If it cannot describe the user case without special casing a router icon, revise ontology before scheduler/protocol code. This is a feasibility **spike**, not production implementation. If concurrent worker already owns S03, don't duplicate; instead review its schema and negative tests.

## Rules
No fictitious speed/time estimates. A blocker stays in [open items](REVIEW_OPEN_ITEMS.md) until reproducible evidence is attached. Cross-layer failures must appear in [gap review](CROSS_LAYER_GAPS.md) and relevant ADR. Keep uncertainty explicitly labeled and do not silently promote draft to ACCEPTED.
