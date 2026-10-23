# Lab acceptance and negative cases
Status: PROPOSED test scenarios | 2026-10-23. Scenarios are NOT executed.

## A — healthy LAN
Create PC0/PC1 -> Switch0 -> WirelessRouter0 LAN. Router LAN=192.168.0.1/24, DHCP pool 192.168.0.100–149, mask /24, gateway .1. PC DHCP request eventually gets valid lease with gateway if advertised. Packet trace documents discover, offer, request, ack, then ARP and ICMP echo request/reply on selected interface. No fabricated packet at another device.

## B — WAN port misconnection
Move switch-to-router cable to Internet/WAN interface, keep LAN-only DHCP pool. Source emits Discover 0.0.0.0:68 -> 255.255.255.255:67. Switch forwards frame physically. Router accepts frame on WAN but DHCP service refuses it with `DHCP_POOL_NOT_BOUND_TO_INGRESS`; no Offer. After modeled retries, DHCP client may assign 169.254.0.0/16 address with no default gateway; ping to 192.168.0.1 drops on PC with `NO_ROUTE_NO_GATEWAY`. Correct cable and retry -> case A. Exact retry timings are configurable/standards-backed, not assumed from this document.

## C — false-positive router-to-router test
Two routers configured with equal LAN IP 192.168.0.1 and a WAN-to-WAN cable. User selects Router0 -> Router1 Simple PDU. Application MUST reveal actual selected destination address and interface. A response generated locally or by matching source IP must not count as verified remote reachability; target identity/path must be checked. Disconnect cable and re-run: cannot report successful physical traversal.

## D — background control traffic
Two disconnected switch LANs. Manually trigger ICMP in first while STP/DTP timers generate events elsewhere. Global timeline displays all events ordered by time; filter only hides display categories. A DTP event is not a ping hop; filtering must not mutate network state. Unsupported STP/DTP must not generate fake events.

## E — malformed inputs, ambiguity and replay
Reject unknown link interface ID, duplicate device IDs, duplicate port claims, invalid masks, frame larger than MTU, invalid virtual-time payloads and unsupported schema versions (or migrate with explicit tests). Replay the same seed/snapshot and commands: serialized event trace and result are identical. Bound queues/trace memory and provide deterministic failure reason.

## Trace schema assertions (proposed)
Every event: `id`, `time`, `seq`, `kind`, `actorDeviceId`, `ingressPortId?`, `egressPortId?`, `packetId?`, `parentEventId?`, `correlationId?`, `reasonCode?`, `stateVersion`. No logically impossible event paths or handwaved diagnostic cause.
