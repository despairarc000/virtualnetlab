# IDEA PLAN — VirtualNetLab
Status: ACTIVE vision | Updated: 2026-10-23 | Authority: product intent, not an implementation claim.

## Purpose
Build an **offline-first Android virtual networking laboratory** enabling anyone to design, construct, configure, operate, simulate, visualize, inspect, troubleshoot, assess and understand networks without needing physical networking equipment. The purpose is the laboratory, not merely the appearance of Cisco Packet Tracer.

## User outcomes
1. Construct network topologies with hosts, switches, routers, wireless nodes, interfaces and links.
2. Configure real modeled device state (ports, addressing, DHCP, forwarding, VLANs, routing, services).
3. Execute repeatable labs with meaningful packet and timer behaviors, not pre-scripted animations.
4. Observe every network decision through chronological events, packet headers, interface state, tables and drop reasons.
5. Experiment with wrong designs: wrong WAN port, APIPA after unsuccessful DHCP, missing gateway, loops, addressing conflicts, unreachable paths.
6. Diagnose *why* behavior occurred, change configuration and verify repairs.
7. Save, resume, compare, share and assess offline labs, with gradual support for larger networks and instructional curricula.
8. Use touch-first interfaces on budget Android hardware; support accessibility and landscape/tablet use.

## Non-negotiable quality contracts
- **One canonical simulated world**. UI, CLI, packet inspector, device panels and diagnostics read/write the same state.
- **Causality**. Every forwarding, drop, lease, timer and route decision follows explicitly implemented rules. A green success icon cannot replace a verified end-to-end packet exchange.
- **Truthful scope**. Unsupported feature, partial fidelity, abstraction level and known deviations must be visible; never silently pretend to implement real behavior.
- **Replay and evidence**. Seeded runs and deterministic event ordering allow the same initial snapshot and actions to reproduce the same trace.
- **Protocol correctness**. Independent conformance, negative tests and trace assertions precede marking a protocol supported.
- **Offline-first**. Core lab creation, execution, inspection, saving and help must work without internet or accounts.
- **Intent versus possibility**. Auto-link helpers may suggest ports, but cannot silently treat electrically compatible WAN/LAN selections as semantically correct. Explain, warn, and allow valid intentional WAN connections.
- **No IP guessing**. Destination testing must show the exact chosen IPv4/IPv6 destination/interface; local address matches must not be presented as evidence of inter-device connectivity.
- **Open, independent implementation**. No copied Cisco code, IOS firmware, proprietary icons, assets or unsupported .pkt compatibility claims.

## Scope horizon
Foundational: topology & editable device interfaces; L1/L2 Ethernet; ARP; IPv4; ICMP; UDP; DHCP; switching; routing; comprehensive diagnostics; saved projects.
Expansion: VLAN/802.1Q, STP/RSTP, CLI, TCP, DNS/HTTP, NAT, ACL, Wi-Fi, IPv6, dynamic routing, assessment, educational content.
Advanced research targets: high-fidelity wireless, latency/queues/impairments, multi-backend integration, emulation bridges (external/opt-in) and collaboration. **Not promises of immediate parity**.

## Product acceptance
A person can create a PC—switch—router lab, observe DHCP DORA, deliberately connect the switch to a WAN-only router port and watch Discover reach but get dropped for the *correct* interface/pool reason, then repair the link and obtain 192.168.0.x/24 and successfully ping the LAN router IP. They can also demonstrate that a coincidentally matching local IP is not proof of a remote WAN traversal. The simulation exposes each step and saves/replays identically.

## Design principle
**Possible ≠ intended ≠ functional; simulation success must prove the intended observable outcome.**

## Relationship to plans
This document owns product intent. [TECHNICAL_PLAN.md](TECHNICAL_PLAN.md) specifies an evolving strategy. [NAVIGATION.md](NAVIGATION.md) routes all agents and contributors. Technical substitutions may not quietly narrow the mission.

## Engineering sequencing rule (2026-10-23)
The user defined [Phase 1](phase1/PHASE1_MASTER_PLAN.md) as exhaustive *planning and architecture risk reduction* before production implementation, so feature coding does not run into avoidable architecture walls. This does not narrow the ultimate laboratory scope. A few disposable, instrumented proof-of-feasibility experiments are allowed to resolve things research cannot prove; they are not counted as production progress. No engine/API freeze before the [Phase 1 exit gate](phase1/EXIT_AUDIT.md).
