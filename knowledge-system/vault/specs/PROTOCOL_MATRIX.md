# Protocol and device support matrix
Date: 2026-10-23 | Status: planning only. **NONE of the items is implemented yet.**

| Feature | Target stage | Planned fidelity boundary | Required verification |
|---|---|---|---|
| Physical port/link topology | 1 | discrete port pairing, link up/down; not electrical signals | wrong port, disconnected, duplicate edge rejection |
| Ethernet frames/switch forwarding | 1 | MAC, EtherType, broadcast/flood, learning/aging | flood/unicast, no spontaneous cross-network frame |
| ARP / IPv4 / ICMP | 1 | subnet/ARP/echo/timeouts, selected destination identity | same-LAN ping, missing gateway, self-ping |
| DHCPv4 / UDP | 2 | Discover/Offer/Request/Ack, timers, pool per ingress, APIPA model | LAN success vs WAN drop trace |
| UI packet inspector / event filters | 3 | immutable factual event projection | filters never change processing |
| VLAN / 802.1Q | 4 | access/trunk membership and tagging | isolation and allowed VLAN |
| STP | 4 | BPDU/state/timers and loop prevention per documented profile | redundant links/convergence |
| DTP | 4 or later | actual trunk negotiation state machine if needed | mode matrix/disable |
| Static routes / IPv4 gateway | 4 | longest prefix selection and interface forwarding | multihop/unreachable |
| TCP / DNS / NAT / ACLs / Wi-Fi | 5+ | per-feature separately bounded model | positive/negative captures |
| IPv6 / ND / ICMPv6 | 5+ | independent IPv6 path | neighbor reachability |
| OSPF/BGP/RIP etc. | future | no claims before model scope decision | RFC-driven conformance |

Model status lifecycle: NOT_IMPLEMENTED -> EXPERIMENTAL -> VERIFIED_SCOPE -> DEPRECATED. UI must show declared scope, limitations and version. Do not mark implemented simply because event type labels appear.
