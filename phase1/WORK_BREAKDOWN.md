# Phase 1 planning work packets and Phase 2 implementation handoff
Status: PROPOSED task contracts | 2026-10-23. [Master plan](PHASE1_MASTER_PLAN.md), [decision gates](DECISION_GATES.md), [implementation roadmap](../architecture/IMPLEMENTATION_ROADMAP.md).

## Ownership and dependency principles
No production PR may invent an upstream contract while bypassing its ADR. Parallel workers can research/study/test disjoint components, but shared domain ID/event contracts need gate sign-off. Every packet includes requirement IDs, applicable RFC/Android evidence, threats, dependencies, positive/negative fixtures, result links, maintenance/rollback implications and update obligations.

## Phase 1 review/handoff deliverables
| Packet | Deliverable | Dependency | Acceptance and owner |
|---|---|---|---|
| P101 | Requirements/personas + journeys completeness matrix | Vision | Five workflows and non-goals trace to requirement/test/owner; product |
| P102 | Build-vs-adapt: Filius/ns-3/INET/license | Research | Tagged source/files/third-party license and portability report; architecture/legal |
| P103 | Topology typed-ID and device-role dictionary | P101 | Interface/bridge/physical port invariants; WAN and multi-NIC fixtures; domain |
| P104 | Virtual-time kernel semantics and resource guard draft | P103 | S01 equal-time/cancel/overflow/rollback experiment; engine |
| P105 | PDU representation options and RFC mappings | P103, P104 | S02 codecs/heap/GC/trace memory outcome; protocol |
| P106 | Protocol initial state-machine tables and failure codes | P103–P105 | Per-protocol scope, standards sections, positive/negative fixtures; protocol |
| P107 | Trace/probe identity and diagnostics schema | P103–P106 | No false target success, packet lineage and port/path provenance; diagnostics |
| P108 | Offline Android UX storyboard and capability registry | P101, P103 | Usability, accessible port choice and trace inspector; Android |
| P109 | Low-end graphics, lifecycle and storage prototypes | P104, P108 | S04–S06 Android real-device/emulator evidence; Android/data |
| P110 | Secure project import/export/migration contract | P103/P104, P109 | Malformed corpus and interrupted write test; security/data |
| P111 | Scenario and test oracle mapping | P103–P107 | All near-term requirements have independent negative cases; QA |
| P112 | System-wide threat model and performance budget | P104–P111 | Prioritized known risks, bounded scheduler, phone evidence; security/performance |
| P113 | Integrate ADR choices and specifications | P102–P112 | All P0 rationales, experiments and alternatives documented; architecture |
| P114 | Adversarial design review and Gate A sign-off | P101–P113 | Exit audit conditions all met; project lead + reviewers |

## Phase 2 production work packets (do not authorize prematurely)
| Work packet | Upstream gate | Deliverables | Tests necessary for merge |
|---|---|---|---|
| E001 core model | Gate A P103 | stable typed IDs, physical links, bridge domains, logical interfaces, strict topology validator | duplicate ID, occupied port, WAN/LAN separation |
| E002 scheduler | Gate A P104 | serial deterministic integer-time queue, cancellation, safe commands | 100x identical trace, tie ordering, event-storm budgets |
| E003 typed packet + trace | Gate A P105/P107 | PDU semantic fields, forwarding lineage, structured reasons | malformed payload, no fabricated hop |
| E004 Ethernet switch | E001–E003 | ingress/egress actors, MAC learning, flooding and aging | unicast, broadcast, isolation, link-down |
| E005 host ARP/IP/ICMP | E003/E004 | on-link route, ARP cache/timeout, echo request/reply | wrong gateway, target identity, self-ping |
| E006 UDP/DHCP/IPv4LL | E005 | service bindings, DORA/lease, retry timers, link-local FSM | WAN pool drop, no server, conflict, lease expiration |
| E007 Android workspace | Gate A UX + E001/E002 | touch topology, port choice, config, pan/zoom and run controls | user interaction, no UI state divergence |
| E008 inspectors and lab storage | E003, E007, Gate A data | truth-based PDU view, export/import, recovery | filter invariance, process death, invalid file |
| E009 L2/L3 breadth | Validated E001–E008 | VLAN, routing, STP subset; DTP only if modeled | no VLAN leak, convergence, TTL/routing |
| E010 educational scenario framework | E003/E008 | reusable versioned scenarios and trace-based grading | alternate valid solutions, no screenshot-based scoring |

## Work packet standard
- Problem/WHY; acceptance criterion; scope/non-goals; standards and version; IDs/interfaces; preconditions; failure behavior; time/space performance hypothesis; security/privacy/IP constraints; protocol conformance and fixture/oracle; test plan; dependencies; rollback and migration; documents touched; exact repository paths; status+evidence. No "done" without CI/real-device evidence when required.

## First implementation critical path (subject to Gate A)
P103 + P104 + P105 + P107 -> E001 + E002 + E003 -> E004 + E005 -> E006 -> E007/E008 (Android UI spike earlier in Phase 1) -> later E009.
Breadth features such as Wi-Fi radio simulation, BGP, vendor command emulation and physical signal emulation remain *scoped future plans*, not dependencies of the minimal truthful LAN lab.

## Rules for assistant/Codex handoffs
Read root [AGENTS](../AGENTS.md) and [navigation](../NAVIGATION.md); load [Phase 1](PHASE1_MASTER_PLAN.md) and targeted ICM route. Do not construe an architecture suggestion as code. Report actual branch/commit/test/review status and unresolved risks; no silent assumptions, premature merge or fake passes. When a packet is blocked, identify smallest experiment or required decision and add evidence to [open questions](../knowledge-system/vault/OPEN_QUESTIONS.md).

## Explicit planning handoff updates
P102: use [Filius source audit](research/FILIUS_REUSE_AUDIT.md) and pin complete tagged source SHA; examine current protocol threading/UI coupling/licenses before choosing reuse.
P103: treat [device/interface model](DEVICE_AND_INTERFACE_MODEL.md) as S03 draft: validate 10 tests, bridge/SVI/WAN separation before schema freeze.
P104/P107: use [event contract](EVENT_ENGINE_CONTRACT.md) as S01/S07 draft; repeat deterministic traces with resource budgets and no accidental local ping success.
P106/P111: run [standards-indexed fixtures](STANDARDS_TEST_VECTORS.md) and document RFC section/model deviations before production claims.
All unfinished evidence is listed in [REVIEW_OPEN_ITEMS](REVIEW_OPEN_ITEMS.md) and [exit gate](EXIT_AUDIT.md).
