# Network stack, planes and event pipeline
Status: PROPOSED v0.1; not running code | 2026-10-23 | [capability map](TOP_DOWN_CAPABILITY_MAP.md), [device catalog](DEVICE_CAPABILITY_CATALOG.md), [event contract](EVENT_ENGINE_CONTRACT.md), [protocol scope](PROTOCOL_BEHAVIOR_SPEC.md).

## 1. Model boundary and reference architecture
A networking lab is a collection of bounded node/device contexts linked by explicit transmission media. A device hosts logical interfaces, protocol handlers, forwarding tables and local services. **Cabling alone does not imply IP subnet, routing, VLAN, service scope or reachability.** INET's primary documentation explicitly distinguishes its per-node InterfaceTable, wired interfaces and connecting channels; it is an architectural reference, not imported code: https://github.com/inet-framework/inet/blob/master/doc/src/users-guide/ch-network-interfaces.rst

```text
APP / INTENT     Scenario / CLI / Ping / DHCP client service / web request
TRANSPORT        UDP, TCP later, port binding, payload and checksum policy
NETWORK          IPv4 now, IPv6 later, local delivery, route lookup, TTL/hop limit
NEIGHBOR         ARP IPv4; ND IPv6 later, neighbor cache and resolution
LINK             Ethernet MAC, ingress rules, bridge/MAC table/VLAN/STP
MEDIA            link propagation, ports, link status, delay/bandwidth queue
SCHEDULER        orders event transitions in virtual time across all devices
TRACE            captures facts at every boundary above; no alternative forwarding path
RENDERER         reads trace/state to draw; does not execute a network protocol
```

OSI is an educational abstraction, not a guarantee that a real protocol has a one-to-one layer mapping. DHCP is application protocol over UDP over IPv4 over link media; ARP resolves IPv4 neighbor addresses for a link; STP changes bridge port states; DTP (future vendor feature) negotiates trunking. Model real dependencies rather than teaching overly rigid OSI classifications.

## 2. End-to-end operation: packet lifecycle contract
`source stimulus -> command validation -> local stack destination classification -> optional service/transport -> IP routing -> neighbor selection -> packet/frame creation -> egress port check -> link scheduler -> peer ingress -> bridge or L3 dispatch -> target protocol handling -> potential response -> reverse journey -> trace and outcome`.

### Host output decision
1. Validate source device and requested interface, destination address family and support level; reject ambiguous selected-device testing unless explicit destination/address handling is reported.
2. Detect local address/loopback. A local echo reply may complete without egress; does **not** prove another device was reached. Trace outcome `LOCAL_DELIVERY`.
3. Route resolution: longest-prefix match of effective routing table, then policy/metric and interface selection; if no route/gateway, drop before Ethernet. For remote destinations via gateway, next-hop address is the gateway, not ultimate remote IP.
4. Neighbor resolution: ARP for next hop, with bounded pending transmissions/timeout; source MAC and EtherType recorded. Once resolved, frame scheduled on physical/bridge egress.
5. Egress port administrative/link/VLAN/MTU/queue checks; successful send is a link event, not automatic remote reception.

### Link transmit/receive
Link event specifies sending endpoint ID, receiving endpoint ID, packet lineage, topology/config revision and delay; no unordered broadcast to nodes merely sharing drawn region. Half/full duplex, bandwidth, collisions, impairment and FCS modeled only according to declared device/media profile. If topology changes in flight, S01 chooses explicit **snapshot-at-send** or **validate-at-receive** policy and tests it; do not silently deliver over removed wire.

### Bridge/switch ingress
- Validate port/link and frame; learn source MAC on ingress in correct bridge/VLAN partition and respect STP or profile control state.
- Broadcast and unknown unicast fan out only across eligible ports in that bridge domain; egress list sorted by stable IDs for deterministic ties.
- Destination MAC known -> forward to learned eligible port, not ingress; age learning state with timers.
- May deliver to an integrated local L3 interface/service bound to the bridge. It is NOT physically the same as flooding to a separately routed WAN port.
- STP transitions, VLAN tag treatment, multicast management, MAC security and DTP features remain disabled if unimplemented; a storm uses safety caps, not fictional STP.

### Router input and IPv4 forwarding
- Logical ingress binding from physical port or bridge/SVI must be explicit.
- Determine local delivery to configured interface/service **versus** routed forwarding. A router receiving packets for its own IP does not necessarily forward those packets.
- For routed packets, verify permitted destination/route, next-hop, IP TTL, fragmentation/MTU and ACL if implemented. RFC 1812 §5.2–§5.3 describes router forwarding and TTL decrement; a router may receive for itself TTL=1 yet cannot forward beyond TTL exhaustion. https://www.rfc-editor.org/rfc/rfc1812.html
- Routing between broadcast domains is L3 behavior. For link-local 169.254/16, RFC 3927 §7 forbids router forwarding of packets with link-local source or destination; model correct host behavior, not just a generic no-default-gateway test. https://www.rfc-editor.org/rfc/rfc3927.html
- NAT, packet filters, routing protocols and IPv6 later add **ordered hook points** but not pretend-implemented decisions.

### Protocol/application delivery
- Dispatch according to network protocol, transport port, destination and service binding (not just frame type label). Example: DHCPv4 Discover src UDP 68 -> dst UDP 67, initial IPv4 src 0.0.0.0 -> 255.255.255.255, Ethernet broadcast; permitted despite host lacking DHCP lease or default gateway.
- DHCP server checks interface/relay binding then pool/lease policy. Wrong WAN ingress with LAN-only pool -> no applicable response even if frame physically arrived. Responses must originate as actual scheduled messages with valid matching transaction ID.
- Service outputs use the same route/neighbor/link pipeline as ordinary traffic unless protocol-specific link rules apply.

## 3. Control plane versus data plane versus management
| Plane | Responsible for | Not responsible for |
|---|---|---|
| Data plane | Actual forwarding, filtering and deliver/drop packets | Imagining route tables or user-visible animation |
| Control / protocol state | ARP, MAC aging, STP (later), route protocol (later), DHCP FSM, timers | Modifying UI directly or bypassing ingress |
| Management | Device config, CLI, status, admin link settings | Shadow-state alternative stack |
| Observation / diagnostic | Event evidence, before/after tables and causal chains | Guessing physics or filtering events out of scheduler |
| Education | Scenario goals, scored outcomes, feedback, replay | Hard-coded selected cable or IP as only correct answer |

## 4. Subsystem contracts / port-boundary events
| Owner | Input | Output | Critical invariant |
|---|---|---|---|
| Lab graph | Create/remove/configure | versioned graph revision | No dangling endpoint or illegal medium |
| Scheduler | validated event/time/actor | ordered transition | Same-time FIFO, bounded queue |
| Media | egress frame + link | peer ingress or drop | Exact 2-port link + delay |
| Ethernet bridge | ingress frame/port | eligible egress copies / local receive | VLAN and bridge partition |
| Neighbor | IP next-hop request | MAC mapping or timeout | ARP cannot traverse unrelated router as bare L2 |
| Host stack | application packet intent | local / route / ARP / emit / reject | Missing route drops before wire |
| Router stack | IP packet on L3 interface | local delivery or forwarding / ICMP error | TTL and prefix/next-hop consistency |
| UDP/DHCP | message+service-bound ingress | server state, lease and next message | No off-interface LAN pool response |
| Trace | actual transition + parent event | factual record/delta | No fabricated hops or impossible IDs |
| Probe/assessment | command + target expectations | separated observation/proof statuses | Reply is not proof of intended target |

## 5. Protocol scaling seams (must be present in schema; don't implement early)
- IPv4/IPv6 address family interfaces, independently supported route/neighbor managers; IPv6 ND is NOT ARP with larger numbers.
- Network namespaces/VRF and multiple bridges/VLAN SVIs can be represented without device-as-single-subnet assumption.
- Wireless AP client association maps to authorized L2 forwarding and later radio contention, not imaginary copper Ethernet.
- SOHO home routers compose LAN switch/bridge, WAN IP, router, DHCP server, NAT/firewall under profile; no special-case hacks through drawable node.
- Application services on virtual end hosts (HTTP/DNS/FTP etc.) dispatch through defined transport ports and network stacks; no direct "server success" without messages.
- Routing protocols later update route table through protocol FSMs; forwarding pipeline consults effective routes, not learning animations.
- Physical layer realism such as CSMA/CD legacy Ethernet, fiber optics, serial PPP and RF requires explicitly named model scope and available standards tests.

## 6. Critical ambiguity to resolve before interface freeze
Internal link serialization timing, event-level packet receive/transmit boundaries, ingress bridge-to-L3 delivery rules, route precedence/metrics and duplicate subnet handling, forwarding of IPv4 link-local, MTU/fragmentation supported subset, optional DHCP relay, case where link changes in flight, MAC/vlan learning table schema, future NAT/ACL hooks. These are Gate A questions, tracked in [cross-layer review](CROSS_LAYER_GAPS.md).

## Primary standards/method references
RFC 826 ARP https://www.rfc-editor.org/rfc/rfc826.html ; RFC 791 IPv4 https://www.rfc-editor.org/rfc/rfc791.html ; RFC 1122 host requirements https://www.rfc-editor.org/rfc/rfc1122.html ; RFC 1812 router requirements https://www.rfc-editor.org/rfc/rfc1812.html ; RFC 2131 DHCP https://www.rfc-editor.org/rfc/rfc2131.html ; RFC 3927 IPv4LL https://www.rfc-editor.org/rfc/rfc3927.html ; ns-3 event semantics https://www.nsnam.org/docs/manual/html/events.html .
