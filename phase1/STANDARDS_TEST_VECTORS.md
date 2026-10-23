# Phase 1 — standards-indexed behavioral test vectors
Status: **DESIGN TESTS ONLY, NOT EXECUTED** | 2026-10-23. Applies to [protocol spec](PROTOCOL_BEHAVIOR_SPEC.md), [device model](DEVICE_AND_INTERFACE_MODEL.md), [scheduler contract](EVENT_ENGINE_CONTRACT.md) and [validation](../architecture/VALIDATION_STRATEGY.md).

## How to use
Each test has preconditions, trigger, observable state changes, expected trace path, negative assertions, and exact standards citation. Frame bytes, packet counts, and timers not settled by selected normative standards must remain unasserted or marked model-specific. Never confuse Packet Tracer implementation quirks with normative protocol requirements.

### Test S-DHCP-01: normal LAN DORA
Setup: host unconfigured connected to switch and LAN bridge/SVI with DHCP server service bound to LAN interface. Server pool 192.168.0.100..149/24, option 3 (router) 192.168.0.1 and lease. Stimulus: enable DHCP and advance event queue. Trace: client INIT -> DISCOVER UDP 68->67 / broadcast 255.255.255.255; switch floods correct broadcast domain; server sends OFFER matching transaction; client selects and sends REQUEST; server ACK; client moves to BOUND, with lease/timers. Assertions: correct advertised IP, prefix, gateway option; no invented relay/server; all hop interfaces valid. RFC 2131 §3.1, §4.3, §4.4; RFC 2132 options.

### Test S-DHCP-02: WAN ingress has no LAN DHCP binding
Setup same but physical switch-to-router cable on WAN with no DHCP service there. DHCP DISCOVER arrives physically at router WAN port; server actor must **not** respond using LAN-only pool. No ACK or lease from that router. Trace must show service binding decision, not "can't reach device". Negative: no offer, no cross-domain broadcast leakage. A legitimately configured server/relay on WAN could behave differently and must not be universally forbidden. Standards provide DHCP semantics; ingress service binding is VirtualNetLab device-profile policy.

### Test S-DHCP-03: mismatched xid, NAK, retry, renewal
Inject OFFER/ACK with wrong xid: ignore and do not enter BOUND. Inject NAK for selected request: restart appropriate initialization; simulate no response to REQUEST: retransmit with bounded timers and eventually restart per configured RFC-compliant policy; renew at T1 and rebind at T2 with lease expiry. Per-interface client state independent. RFC 2131 §§4.1, 4.4, 4.4.5. Assert never invent ACK. Separate possible relay-support future behavior.

### Test S-IPV4LL-01: DHCP unavailable, address probe
No DHCP responses, IPv4LL enabled. Policy triggers candidate within permitted 169.254/16 selection (exclude first/last 256 as RFC). ARP probe before use, 3 probes and waits according to selected RFC 3927 timing policy, announcement and assignment only if no conflicting response. DHCP policy continues independently as configured. No default gateway magically installed, and no router forwards link-local sourced/destined IP. RFC 3927 §2.1–2.5, §7, §9.

### Test S-IPV4LL-02: conflicting candidate
Another host already claims candidate or sends colliding ARP probe. Client detects ARP conflict, retries candidate and rate-limits after threshold; does not retain a disputed address. Under duplicate-IP/no-DHCP, topology updates cannot create two silently successful claimed IPv4LL addresses. RFC 3927 §2.2, §2.5, constants §9.

### Test S-ARP-01: on-link vs gateway next-hop
Host A wants to ping same-subnet Host B with no ARP cache: Ethernet ARP who-has B local L2 broadcast; B replies; A sends ICMP echo via B MAC. For remote B via gateway G, ARP asks for G's MAC on local interface, not B's; absence of route/gateway blocks transmission. RFC 826 packet format/next-hop, RFC 1122 §3.3 route selection. Negative: no ARP request traverses a router as bare Ethernet broadcast without a bridge/relay.

### Test S-ICMP-01: physical and identity proof
One physical LAN path from host to router; echo with explicit destination 192.168.0.1 and expected router interface. Echo reply and actual trace at router confirm expected remote target. Duplicate-address isolated routers with WAN cable disconnected: a local reply (if any) must never set remote target/path flags. RFC 792 echo format + VirtualNetLab probe identity extension. Link down or ARP timeout must be causally visible.

### Test S-IPV4-01: route and TTL
Host sends off-subnet unicast without default or matching route: source drop before any egress Ethernet frame. With routed next hop: ARP next-hop, forward at router with TTL decrement and IPv4 checksum policy; near TTL zero must not be forwarded. IPv4 RFC 791 §3.1, RFC 1812 router forwarding. Fragmentation/PMTU features must be explicit model support levels, not presumed implemented.

### Test S-ENGINE-01: background events not hops
Two disconnected networks, ICMP manually injected in first; background timer in second. Simulator queue contains both; global event list shows chronological interleaving; filtered UI may hide unrelated events but never changes physics. Missing route on PC cannot produce a remote ICMP hop in second network.

### Test S-ENGINE-02: switch cycle storm
Two/three switches with redundant links; STP unsupported or disabled. Broadcast may circulate, but no process freeze: event/queue/fanout limits stop safely, trace marks incomplete storm. If selected STP model later enabled, BPDUs and correct port state transitions must causally prevent loop. No generic safety policy should masquerade as working STP.

### Test S-ANDROID-01: lifecycle integrity
Build same scenario on 4GB Android device; run, pause, rotate, background/return, kill process, relaunch. Saved LabDesign must survive; runtime only resumes where compatible checkpoint is present. No trace claim of success after process death before completed probe. Android state-saving docs https://developer.android.com/topic/libraries/architecture/saving-states .

## Blocking evidence requirements
Each case is a specification until a fixture implementation, executed CI result, engine commit, model/version, independent oracle or documented deviation, and actual failure-case trace are linked. Test expected physical hop chain and source/destination *identities*, not only a ping summary. No false green pass badges from UI.
