# Architecture review — 2026-10-23
Status: REVIEWED DESIGN BASELINE, NOT IMPLEMENTED. Source-of-truth: [vision](../IDEA_PLAN.md); [blueprint](ARCHITECTURE_BLUEPRINT.md); [roadmap](IMPLEMENTATION_ROADMAP.md). An exhaustive review of a future system is impossible; this is a risk-indexed coverage audit with explicitly pending evidence.

## Review question
What architecture lets an offline Android user *really build, configure, run, inspect, troubleshoot and learn* virtual networks, with faithful bounded protocol semantics, reproducible evidence, low resource use and a path to grow?

## Source types and confidence
- **Grounded primary evidence:** RFC 2131, RFC 3927, RFC 826, RFC 792, RFC 1122, RFC 1812, ns-3 event manual, OMNeT++ manual and license, GNS3 architecture, CORE architecture, Android architecture/background/performance/storage/security guidance. Exact URLs in [EVIDENCE](../knowledge-system/vault/EVIDENCE.md).
- **Architecture inference:** independent simulation first, normalized device models, state/trace separation, touch-first UI, testing gates. Confidence MEDIUM, falsifiable by spikes.
- **Unverified:** actual Kotlin engine speed, Android app throughput/memory, UI frame times, broad protocol interoperability, licenses of any *future* vendored dependency. Confidence UNKNOWN.

## Independent alternatives — comparative fit (qualitative; not a measured benchmark)
| Strategy | Causal learning/inspection | Offline Android feasibility | Real NOS fidelity | Cost/risk | Conclusion |
|---|---|---|---|---|---|
| Animated topology/pseudo packets | Poor | High | None | Misleading teaching | REJECT |
| Independent deterministic discrete-event simulation | High if validated | High in principle | Per-implemented model, bounded | Implementation and validation burden | BASELINE |
| Embed ns-3 native libraries | Potentially high | Requires porting and UX bridge | Research-model dependent | JNI, memory, GPLv2 duties, complex integration | STUDY FOR ORACLE/OPTION |
| Embed OMNeT++/INET | Potentially high | Requires porting and licensing | Research-model dependent | Academic Public License, commercial restrictions, integration | DO NOT EMBED DEFAULT |
| Local GNS3/QEMU/CORE/Linux namespace emulation | Strong for real images | Not dependable on unprivileged budget Android | Higher when licensed images available | Privileges, images, resources, power | REJECT LOCAL BASELINE |
| Remote GNS3/containerlab emulation | Strong but not offline | Requires server/network | Higher | Complexity and security/trust | OPTIONAL FUTURE |
| Android client calling cloud-only simulator | Depends on backend | Poor offline | Varies | Privacy/cost/dependency | REJECT AS BASELINE |

The independent simulator is not selected because it is always more accurate: rather it preserves our **offline controllable observability** contract and feasible minimal deployment. Independent validation remains mandatory.

## Architecture coverage audit
| Domain | Desired property | Current decision | Residual risk / proof needed |
|---|---|---|---|
| Mission / audience | Self-guided genuine lab and assessment | Vision authoritative | Task-based UX evaluation |
| Fidelity | No fabricated protocol behavior | Capability levels + RFC-backed cases | Device-specific divergence |
| Virtual time | Step, fast run, reproducible timing | Single deterministic scheduler | Long queues/timers/overflow |
| Concurrency | No race-dependent result | Serial engine actor; UI commands queued | Pause/command order semantics |
| Topology | Explicit ports/media/link endpoints | Normalized topology | VLAN/bridge/wireless boundary |
| Devices | Hosts, switches, routers, APs as composed roles | Capability-based profiles | Profile proliferation |
| Packets | Header correctness and inspectability | Typed packet model initially; prototype byte codec | Unknown memory/fidelity balance |
| Forwarding | MAC learning, flooding, routing, TTL | Protocol-layer handlers | Invalid route and loop behavior |
| Routing | LPM, direct/indirect next-hop, gateway | Explicit route resolution | Asymmetric/overlap/NAT |
| DHCP | Real state machine and per-interface service | DHCP RFC-guided model | Retransmission, lease edge cases |
| IPv4LL | DHCP-independent 169.254/16 behavior | RFC 3927 policy model | Conflict detection/timers |
| STP/DTP/VLAN | Don't generate decorative protocol events | Scoped state-machine implementations later | Spanning tree convergence and vendor variation |
| Diagnostics | Why/where/drop reason with evidence | Structured trace, immutable event chain | Overhead and misleading inference |
| CLI | Typed commands using same config API as GUI | Adapter/parser not second engine | Cisco compatibility scope |
| User tests | Source AND intended target identity proof | Explicit targeted probe | NAT/proxies/load balancing future |
| Interaction | Touch/pen/mouse, visible ports, accessibility | Compose shell + custom canvas candidate | Large graph hit testing/jank |
| Storage | Resume, migrate, portable project | Versioned model + separate trace/session | Corruption and zip-bombs |
| Android lifecycle | Don't lose labs on process death | Transactional autosave + pause/snapshot | Background restrictions |
| Performance | Usable on low-end RAM/CPU | Bounded traces, no UI per event | Unknown until profiling |
| Privacy | No accounts needed | Offline by default, no live network bridging | Import and future plugin threats |
| Extensibility | New protocols without redesign | Layered actor/capability boundaries | Overgeneralization risk |
| Education | Real experiments, not canned animations | Scenario DSL and assertions | Accessibility and learning validity |
| Testing | Standard-based, adversarial, trace-based | Fixture and property/differential tests | Oracle availability |
| Licenses | Independent open implementation | Third-party license inventory before reuse | Future license compatibility |
| Build/release | Reproducible signed APK process | Gradle + CI planned | Real device validation |
| Governance | No spec drift; recoverable context | ICM/Graphify/vault/ADRs | Stale maps / undocumented changes |
| Real-time/remote | Optional future experiments | Versioned backend contract later | Synchronizing external state |

### Highest-risk architecture traps
1. Accidental conflation of visual cable graph with actual frames/interfaces and VLAN broadcast domains.
2. Conflating persistent configuration, ephemeral runtime state, and presentation state.
3. Claiming a simulated packet equals a real byte-accurate frame despite missing header/option rules.
4. Assuming simulated timestamps are Android elapsed/wall-clock time.
5. Infinite loops/zero-time event storms and unbounded logs freezing a 4 GB device.
6. Revealing a single green PDU as proof that a particular remote device received it.
7. Exposing CLI commands that update a shadow config not applied to the engine.
8. Attempting local router OS emulation on an unprivileged phone without resource/licensing validation.
9. Treating a screenshot/Packet Tracer oddity as normative protocol behavior.
10. Freezing a public file format or extension ABI before migration/version experiments.

## Architecture choices ready to adopt conditionally
- DES core, UI-free test path, explicit time/sequence ordering, owned serial mutation.
- Device/interface/link identity independent of screen coordinates.
- Canonical configuration and runtime model distinct from UI; all commands use one mutation boundary.
- Per-packet chain-of-custody, explicit reason codes and tests for verified target/path.
- No root permission, real packet injection or cloud requirement in baseline.
- Model support registry truthful to implementation/validation.
- Offline saved projects, guarded import limits and validation.

## Choices still subject to spikes
Binary vs typed packet implementation; storage and snapshot format; Compose Canvas vs hybrid custom View for largest scenes; exact min SDK and performance budgets; execution checkpoint granularity; multi-platform portability; wireless fidelity; emulation integration. See [spikes](SPIKES_AND_DECISION_GATES.md), [risks](RISK_REGISTER.md).

## Review verdict
**GO for time-boxed architectural spikes and formal contracts. NOT GO for broad protocol implementation or permanent file format/API until Gate A is passed.** The mission remains comprehensive but delivery is an expanding set of accurately modeled capabilities. Formal results belong in ADR updates and validated tests, not conclusions inferred from this document.
