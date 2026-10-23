# Cross-layer dependency and contradiction audit — 2026-10-23
Status: REVIEW FINDINGS; no experimental closure. [Master](PHASE1_MASTER_PLAN.md), [top-down capability map](TOP_DOWN_CAPABILITY_MAP.md), [stack](NETWORK_STACK_DECOMPOSITION.md), [exit audit](EXIT_AUDIT.md).

## Review method
For each user goal, trace down to the lowest device/link behavior and back up through trace, persistence, UI and verification. Mark a missing contract as OPEN, not "implementation detail". This is a planning review, not independent source-code testing. Highest-risk findings block the relevant Phase 1 Gate A/API.

## Cross-layer issues discovered or reinforced
| ID / priority | Architectural collision / missing distinction | Design clarification | Required evidence |
|---|---|---|---|
| CL-01 / P0 | Diagram-level router/host maps to a single IP and one cable | Stable Device/Port/Bridge/L3Interface/Service roles; separate LAN internal bridge and WAN | S03 home-router topology + wrong-port DHCP |
| CL-02 / P0 | Physical connected implies subnet/DHCP/reachability | L1, L2, L3 and service eligibility independent | No-pool WAN trace; route drop |
| CL-03 / P0 | UI configuration and CLI hold competing truth | Typed single-writer config commands, effective revisions and immutable read views | UI-to-CLI-to-runtime round trip |
| CL-04 / P0 | Edit topology while events are pending | Choose explicit in-flight link delivery policy, version/generation-based stale event handling | Unplug in transit, deletion/re-add same name |
| CL-05 / P0 | Engine report "success" when packet reached local duplicate address | Probe source/selected IP/expected Device+Port/optional path; separate outcomes | Two same-IP routers detached WAN |
| CL-06 / P0 | Synthetic packet animation masquerades as real header/traversal | Modeled protocol fields and lineage; wire-accuracy level declared separately | Golden ARP/ICMP/DHCP tests and byte codec spike |
| CL-07 / P0 | Event queue can storm or run forever | Single virtual clock, deterministic priority, quotas, pause and exact error | 100x replay plus zero-delay switch loop |
| CL-08 / P0 | Device profile claims STP/DTP/Wi-Fi without state engine | Registry status NOT_IMPLEMENTED unless conformance tested; no fake control packets | Unsupported mode warnings, later mode FSM tests |
| CL-09 / P1 | Design "route table" confuses configured static routes with learned/runtime effective FIB | Config routes are durable; control-plane learned/connected routes and compiled effective forwarding entries are runtime derived | LPM/static-next-hop and cache invalidation fixture |
| CL-10 / P1 | IPv4LL test assumes immediate 169.254 assignment or route to gateway | Separate RFC 3927 FSM/ARP probing; link-local packets never routed by routers; policy and timers scoped | Conflict + no-server + DHCP recovery |
| CL-11 / P1 | Transport/application success short-circuits network models | Server/UDP/DHCP/DNS/HTTP future actors only accessible via real stack | Broken route must break application exchange |
| CL-12 / P1 | Trace retention/filters change interpretation | UI filters read-only; trace explicitly incomplete after eviction; never give definitive path claims on incomplete evidence | Hide DTP/STP events without state change |
| CL-13 / P1 | Offline "save" implies full runtime continuity | Durable design separated from optional engine/protocol-versioned checkpoint and trace | Process kill/incompatible checkpoint |
| CL-14 / P1 | Android lifecycle timer confused with simulated time | Virtual time only advances by scheduled events; background pause/checkpoint/replay policy | Real phone lifecycle test |
| CL-15 / P1 | Source of reachability conflates address vs selected device | Recipient identity/proof must include event delivery to intended actor, even with same IP on disconnected domain | Path-specific trace assert |
| CL-16 / P1 | Device port role is declared "WAN" but physical compatibility erroneously rejected | Port compatibility accepts legitimate WAN Ethernet uplink, warns on suspicious semantic mismatch | Auto-connect UX test with intentional WAN |
| CL-17 / P1 | Protocol model support mistaken for actual NOS/vendor compatibility | Separate profile/vendor features, supported RFC subset and codec level; no IOS images/assets | License/BOM and capability audit |
| CL-18 / P1 | One global MAC/ARP table leaks domains | MAC bridge domain + VLAN keys; ARP per network context/interface; route table scope | Cross-VLAN/isolated-LAN no-leak fixtures |
| CL-19 / P1 | Future Wi-Fi treated as a cable/port with different icon | Radio medium/association/SSID/security hooks distinct, connected bridge semantics | Candidate AP/client 802.11 logical model review |
| CL-20 / P1 | Timestamps/order unstable due to hash iteration or concurrency | Serial writer + tie-sequence; deterministic egress sorting and seeded randomness | Cross-runtime same semantic trace |
| CL-21 / P1 | Assessments grade one hard-coded IP/address/layout | Semantic predicate DSL over actual state/trace; allowed alternatives | Two equivalent valid schemes graded equally |
| CL-22 / P1 | Project file import can create arbitrary code or OOM | Data-only importer, parse budgets, schema validation, atomic install | Oversize/bomb/unknown-device tests |
| CL-23 / P1 | Persistence migration silently changes protocol semantics | Independent design/profile/engine/protocol versions, safe rejection or explicit migration | v0→v1 fixture + known-incompatible snapshot |
| CL-24 / P1 | Performance tuning changes simulator meaning | Snapshot/UI coalescing permitted; simulation scheduling and data-plane behavior immutable | UI speed/filter comparison hash |
| CL-25 / P1 | An "interface" can be physical port, SVI, VLAN subinterface or virtual loopback | Explicit type and parent scope, separate interface table abstraction | Multihomed/bridge/router-on-stick model walk |
| CL-26 / P1 | Conformance blanket claim despite unsupported frames/timers | Publish support status per model/version and source-backed subset/known deviations | Trace oracle/edge-case matrix |
| CL-27 / P2 | IPv6 later demands new per-node architecture | Address family, route/neighbor abstractions; never assume ND == ARP | Design-only two-address-family review |
| CL-28 / P2 | PCAP advertised despite typed-only semantic messages | Packet byte serialization and checksum/length validated first; export limitations labeled | External tool decoding test |
| CL-29 / P2 | Global diagnostics accidentally reveal personal data | Simulated data only by default; safe export, optional real integration separately consented | Threat review and permission manifest |
| CL-30 / P2 | Scope of "internet" cloud node undefined | Define deterministic ISP/network model or label placeholder, not access to actual Internet | Scenario supports deterministic upstream path |

## Resolutions at the planning level (not accepted runtime code)
- Architectural direction: retain three state planes, a per-device interface table / service binding and one deterministic event queue. This resolves a *conceptual ambiguity* only, not the physical/protocol correctness evidence.
- Clear security stance: imported laboratories are declarative, not executable; external emulation and real packet capturing are not baseline.
- Separate configured route objects from effective routing decision state. This should be incorporated in final persisted schema/actor design.
- Explicit source/target/path proof and completeness levels, never blanket success based on address alone.
- Prohibit nonimplemented STP/DTP "automatic" event injection; any background event must be generated by a modeled timer/state machine.
- Reinterpret Phase 1's "plan to last detail": near-term packet/routing/DHCP/IPv4LL vertical slice needs formal schema+FSM+positive and negative tests, while far-future RF/dynamic routing features require stable extension hooks and separate just-in-time conformance plans, not fabricated comprehensive protocol specs.

## Implementer-two-person agreement exercise (OPEN)
Hand each implementer only the [device model](DEVICE_AND_INTERFACE_MODEL.md), [engine contract](EVENT_ENGINE_CONTRACT.md), [protocol plan](PROTOCOL_BEHAVIOR_SPEC.md), and [stack specification](NETWORK_STACK_DECOMPOSITION.md). Ask them to independently list event order and state for (A) PC0 DHCP Discover to LAN bridge, (B) same switch cabled to WAN, (C) router self IP ping with WAN disconnected, (D) link unplugged during in-flight frame, (E) ARP pending and two simultaneous packets. Any incompatible traces reveal under-specified policy and require ADR. **Not run yet**.

## Gate effect
No CL-01–CL-08 may be waived through undocumented convenience decisions. Each receives a validated spike/test or explicit reversible assumption accepted at Gate A. P1 issues assigned owners and bounded before dependent feature. The [readiness audit](EXIT_AUDIT.md) remains NOT READY.
