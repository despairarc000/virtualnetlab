# Validation strategy and fault model
Status: PROPOSED | 2026-10-23 | [Blueprint](ARCHITECTURE_BLUEPRINT.md) | [Lab acceptance](../knowledge-system/vault/specs/LAB_ACCEPTANCE.md).

## Test pyramid and independent oracles
1. **Pure unit**: typed IDs, parser and model invariants, masks, endian fields, event scheduler tie/order/cancel/overflow, seeded RNG.
2. **State-machine model tests**: DHCP/IPv4LL, ARP aging, STP selected profile, IPv4 routes, retry/backoff, flags/counters and failure reasons.
3. **Integration/fault tests**: create topology, inject activity, capture state transitions and per-interface forwarding, assert packet/route/probe outcome; test opposite edge conditions.
4. **Differential/cross-check**: protocol references and RFC examples; comparison to traces from a Linux network namespace lab, Wireshark PCAP or known-good ns-3/INET cases when available. Track deviations; do not infer interoperability from internal tests alone. Emulated equipment not essential to *run* offline app.
5. **Android**: orientation/state restore, suspended/kill process behavior, touch/zoom accuracy, accessibility semantics, imports, no internet, constrained memory and slow phone.
6. **CI/release**: deterministic JVM regression suite, lint/static analysis, malformed input fuzz/property tests, Gradle dependency + license inventory, Android instrumented tests and release signing/access controls.

## Invariants (negative assertions are first-class)
- No event at a device that is not reachable through an actual valid delivery/transport step.
- Every forwarded frame must identify ingress, egress, legitimate MAC learning/VLAN and a prior causal event.
- No virtual event precedes cause or processes with a negative timestamp; same-time FIFO within monotonic sequence.
- No forwarding on down port, blocked STP port, disallowed VLAN, absent route or invalid TTL without explicit behavior.
- DHCP server response must be generated only if policy and ingress/relay context permit it.
- IPv4LL presence cannot silently suspend a still-valid DHCP FSM; IPv4LL cannot provide cross-subnet route.
- A self-address echo or a packet to unintended router interface never proves connectivity to another selected device.
- One writer mutates core network state; GUI filters can't modify execution; pause/resume maintains events.
- File import cannot add duplicate IDs/unknown interface references, escape paths, allocate unbounded objects or execute arbitrary code.
- Event trace and probes remain accurate when there are background timers or multiple disconnected lab networks.

## Golden evidence format (proposal)
Fixture contains `schemaVersion`, `engineVersion`, `seed`, topology, input actions, expected **semantic assertions** (path, actor, packet fields, state transition, reason, target identity) and expected canonical trace hash for deterministic same-version runs. Avoid freezing incidental timestamps when protocol rules allow distributions; use invariant ranges. Version oracle fixture explicitly whenever changing model behavior.

## Fault injection matrix
Wrong physical port; wrong media; link shutdown mid-frame; MTU underflow; unsupported EtherType; ARP timeout; broadcast storm; switch loop; STP block; two DHCP servers; wrong router/gateway; duplicate MAC/IP; missing route; unreachable next hop; false local ping; overlapping LAN/WAN address; invalid DHCP lease; truncated packet; corrupt/older project; huge topology; event storm; app killed while saving; unknown device profile; malformed CLI; out-of-order user commands; invalid event cancellation.

## Measurement (hypothesis, NOT known performance)
Profiles: 10, 50 and 100 nodes; 1k, 10k, 100k simulated events; small and dense layouts; background timers; 4GB RAM/Android 15 target plus better reference device. Record p50/p95 engine event throughput, latency to pause, memory peak/GC, max queue, trace size, UI frame times (Macrobenchmark), wake/battery and process restore. Pass/fail budgets SET AFTER baseline measurements and product UX evaluation, not arbitrary promise.

## Protocol-support gates
Each model lists standards + specific RFC section and interpretation + capability subset + deviations + validation oracle + CI test IDs. Release label: NOT_IMPLEMENTED / EXPERIMENTAL / VERIFIED_SCOPE. Partial wire serialization not advertised as real PCAP fidelity. Verify known-good packet exchange and intentional failure with human-readable traces.

## Concrete example: WAN-connected switch
1. Create PC, switch, home router with LAN DHCP pool but WAN port linked to switch.
2. Assert DHCP Discover emitted on host, crosses switch, arrives router **WAN interface**; no DHCP Offer from LAN-only pool.
3. Retry protocol with bounded timer; if IPv4LL profile enabled, acquire address via modeled conflict detection, DHCP retries continue as policy.
4. Send ping to LAN router address off-link; no default route → source drop reason, no switch/remote ICMP event.
5. Move link to LAN; DHCP client obtains valid lease + option 3 gateway; ping follows actual L2 path to selected router interface.
6. Verify replay and compare corrected/failed traces. No Packet Tracer screenshot is acceptance proof; engine event evidence is.

## Performance/consistency and safety gates
O(events log events) rather than whole-network redraw per event. Bounded allocations; cancellation design without leaked stale timers; an iteration limit for zero-time loops; emergency pause always completes on a known safe boundary. Import test corpus includes archive bombs/traversal and oversized/deep nested payloads. Any future real-socket/remote backend has separate permission and network trust review.
