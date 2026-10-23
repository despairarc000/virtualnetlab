# Protocol behavior and fidelity specification for initial engine
Status: PLANNING REQUIREMENT / not implemented | 2026-10-23. Covers intended first engine milestones, not all future protocols. Every item needs named owner, standards section, versioned subset, FSM, packet fields, normal/failure cases, trace oracle and model deviations before being called supported. [Master plan](PHASE1_MASTER_PLAN.md), [contracts](SYSTEM_CONTRACTS.md), [tests](../architecture/VALIDATION_STRATEGY.md).

## Fidelity levels (cannot be silently promoted)
0 NOT_IMPLEMENTED: no invented control traffic or success.
1 EXPERIMENTAL_SEMANTIC: documented behavior subset, real modeled state transitions, synthetic/not wire-compatible payload.
2 VERIFIED_SEMANTIC: standards-backed positive/negative cases and independent oracle for supported subset, byte serialization may be partial.
3 VERIFIED_WIRE_SUBSET: encode/decode of declared packet fields matches captured/known-good wire bytes including lengths/checksums, with explicit unsupported options.
4 ADVANCED_INTEROPERABILITY: demonstrated against independent network implementations/test vectors within scoped versions.
All milestones begin at level 0. Passing only an internal self-test cannot advance to 3/4. Expose per-device-profile capabilities (e.g., not all switches negotiate DTP).

## Wire/packet processing pipeline — candidate
1. Application/test creates intent; host routing selection checks local delivery, destination subnet, route/gateway or rejects before L2.
2. If on-link or next-hop needs MAC resolution, ARP cache lookup/ARP request is scheduled; payload waits/drops on policy/timer. IPv4 and ARP packets do not magically teleport through switch.
3. Transport/application (e.g. DHCP UDP 68->67) serializes logical request into modeled IPv4/Ethernet frame. Initial DHCP Discover uses source IP 0.0.0.0 and limited broadcast destination 255.255.255.255 when using broadcast mode, **despite no default gateway**.
4. Sender checks port and forwarding rules, link scheduling produces physically corresponding ingress on neighbor, switch learns/floods based on actual bridge domain, VLAN and port state; router ingresses chosen L3 interface.
5. On router, interface role, L3 route, service policy and ingress context decide accept/forward/drop. LAN DHCP pool doesn't silently serve an unrelated WAN interface; a configured DHCP relay may change behavior in future.
6. Receive/ACK/reply can update independent runtime FSM and schedule new frames. Trace records each decision once, with correlation.

## 1. Physical link and Ethernet (G1/G2)
Reference: IEEE 802.3 and relevant current Ethernet rules; packet-level details need specific licensed standard reference before implementation.
Required modeled fields: src/dst MAC (48-bit), EtherType or declared 802.3 variant, payload length, optional FCS status, MTU policy, physical port, link up/down, propagation delay and duplex/link capability profile. Ethernet broadcast FF:FF:FF:FF:FF:FF is confined to L2 broadcast domain (subject to bridge forwarding rules). Validate malformed/short frames, oversized frames, down-port, incompatible endpoints, self-loop and disconnected link.
Do not equate "green cable" with IP reachability. No electrical signal simulation unless separately specified.

## 2. Bridge/switch (G2)
MAC learning and aging, unknown unicast flood, broadcast/multicast policy, forwarding filtering to exclude ingress port, source MAC validation, bridge-domain isolation; learning key = (bridge domain, VLAN if supported, source MAC), not a global table. No L3 forwarding on ordinary L2 switch by implicit magic. Tests: two hosts same switch, no L2 leap to disconnected topology, MAC move, aged entry, unknown MAC, VLAN separation (later). Define per-port switch model; timers must use event kernel. Loop behavior without STP requires explicit storm budget rather than app hang.

## 3. ARP (G2)
Reference: RFC 826 https://www.rfc-editor.org/rfc/rfc826.html and host requirements RFC 1122. Message fields: hardware/protocol types, hlen/plen, operation, sender and target hardware/protocol address. Request broadcast to local L2 domain; reply targeted according to model. ARP caches keyed by interface/network scope, with entries and aging. Cases: missing entry, who-has + reply, stale cache, dropped timeout, malformed address, wrong broadcast domain and ARP conflict observation. No ARP to remote destination if route uses next-hop gateway; resolve **gateway's** MAC instead. Record explicit unresolved queue policy and timeout at Gate A.

## 4. IPv4 and ICMPv4 (G2)
References: RFC 791 (IPv4), RFC 792 (ICMP), RFC 1122 (hosts), RFC 1812 (routers); check updates/errata before code.
Host route decision: exact self-address / loopback (if supported), on-link route longest-prefix, explicit route/default route, otherwise local NO_ROUTE_NO_GATEWAY; no Ethernet frame on source-side route rejection. Router forwarding: appropriate next-hop lookup, TTL decrement, ICMP time-exceeded behavior if supported, checksum update on modeled header; fragmentation/DF behavior scoped, never pretend unimplemented fragmentation worked. ICMP Echo: type/code/identifier/sequence and payload identity, request/reply correlation and timeout. Distinguish ping to same IP from verification of selected remote router identity. Negative tests: netmask mismatch, no gateway, conflicting IP, link down, ARP loss, routing loop and TTL expiry once implemented.

## 5. UDP (G3)
Reference: RFC 768 and later applicable corrections. Model minimal ports, source/destination IP, length, payload, checksum policy; declare whether wire codec is verified. Deliver to correct interface and bound socket/service, not any protocol label. Broadcast not routed by default. Unbound service decision explicit.

## 6. DHCPv4 (G3)
Reference: RFC 2131 https://www.rfc-editor.org/rfc/rfc2131.html and RFC 2132 options https://www.rfc-editor.org/rfc/rfc2132.html.
Required **client state-space** map, even if first supported subset is narrower: INIT, SELECTING, REQUESTING, INIT-REBOOT/REBOOTING, BOUND, RENEWING, REBINDING; failure/restart and lease expiration. Per-network-interface client independent (RFC 2131 §3.6). Transmission includes transaction ID (xid), chaddr/client identifier, port 68->67, option 53 message type, requested address, server identifier, configured mask/lease/router options as applicable.
Offer/Request/Ack flow: client sends DISCOVER (broadcast), receives offer matching xid, selects offer, sends REQUEST, server sends ACK/NAK; client accepts matching response, records lease and starts T1/T2 expiry clocks. RFC 2131 discusses default T1 0.5 and T2 0.875 of lease if not configured; implement only after correct policy, retry fuzz and timers defined.
Server must check binding to ingress interface or configured relay context, lease pool allocation/collision/selection and requested options; not accept arbitrary LAN pool on unrelated WAN. Multiple DHCP servers/offers and expired lease require explicit behavior.
Retries: schedule bounded retransmissions; timeouts **do not mean immediate** IPv4LL fallback; host policy controls coexistence and probing.
Tests: successful LAN DORA and gateway option, no server, wrong WAN ingress (discover reaches port; zero offer), missing gateway option, pool exhausted, mismatched xid, lease renew/rebind, reconnect, 2 servers, invalid options, relay unsupported warning.

## 7. IPv4 Link-Local / APIPA-like mode (G3)
Reference: RFC 3927 https://www.rfc-editor.org/rfc/rfc3927.html. Address range 169.254.0.0/16, with RFC-defined selection restrictions, ARP probe/announce/conflict defend mechanism, and link-local-only reachability. A chosen address is not "DHCP given"; a gateway must not appear automatically. IPv4LL and DHCP clients are distinct state machines; profile policy decides when IPv4LL is attempted after DHCP delay and whether DHCP retries continue. Record exact timers, probe count, collision behavior and source addresses from RFC before code; do not hardcode undocumented timing from screenshots.
Tests: no DHCP -> probe -> usable link-local, conflict -> new candidate, disabled policy -> no address, link-local peer ping on same L2, off-link no gateway failure, eventual valid DHCP lease superseding/deactivating link-local per selected profile policy.

## 8. Planned later protocols (G5+; ZERO support today)
- VLAN / 802.1Q: tagged vs untagged ingress, PVID, trunk allowed list, separate learning domains and disallowed frames.
- STP/RSTP: BPDUs, root selection, root/designated/alternate port roles, forwarding/blocking/timing and link convergence. Select profile/edition before work, and do not emit decorative BPDUs.
- DTP: Cisco-specific negotiation modes, vendor/device capability gates and security considerations; not part of ordinary Ethernet.
- Static routing + router forwarding, NAT/ACL, DNS/TCP/HTTP, IPv6+ICMPv6 ND, Wi-Fi association/802.11, OSPF/RIP/BGP: each demands its own RFC/standards map, device profile, supported-version declaration, failure taxonomy, formal tests and staged gate. They are roadmap goals, **not Phase 1 fully-specified wire implementations**.

## Proto requirements matrix
| Module | Mandatory positive | Mandatory negative | Critical diagnostic |
|---|---|---|---|
| Link | actual frame delivery | link down/no port | LINK_DOWN |
| Ethernet switch | MAC learn/unicast and broadcast | isolated LAN, invalid frame | NO_L2_PATH / VLAN_NOT_ALLOWED |
| ARP | request/reply and cache | reply not received | ARP_UNRESOLVED |
| Host IPv4 | on-link and routed next-hop | off-subnet without gateway | NO_ROUTE_NO_GATEWAY |
| ICMP | echo request/reply | lost/expired/target mismatch | TARGET_NOT_CONFIRMED |
| DHCP | valid four-way exchange | LAN pool on wrong WAN | NO_DHCP_SERVICE_ON_INGRESS |
| IPv4LL | probe+adopt | address conflict and off-link | IPV4LL_CONFLICT |
| STP (later) | loop-free convergence | failure and reconvergence | PORT_BLOCKED_BY_STP |

## Protocol implementation handoff template
For each protocol: target level, normative versions+section+errata; field schemas and validators; state/timer diagram; dispatch ingress/egress; acceptance and rejection transitions; latency/resource budget; interoperability or oracle; lab and negative case; trace fields and reason taxonomy; profile enablement; known unsupported cases; actual CI evidence.
