# Domain and interface topology contract — specification v0.1
Status: **PROPOSED, UNPROVEN** (S03 P0). Updated 2026-10-23. [System contracts](SYSTEM_CONTRACTS.md) · [Phase 1](PHASE1_MASTER_PLAN.md) · [Failure atlas](FAILURE_AND_SECURITY_ATLAS.md).
The most expensive redesign risk is pretending a device is simply a screen node with one IP and a cable. This contract defines the minimum *separate* identities necessary for real behavior.

## Domain model and invariants
```text
LabDesign
  DeviceDefinition[]                   stable DeviceId, ProfileId, ProfileVersion
    PhysicalPortDefinition[]            stable PortId, physical media/capability, admin state
    BridgeInstance[]                    stable BridgeId, bridge forwarding context
      BridgeAttachment[]                physical port + access/trunk logical membership
    LogicalInterface[]                  stable InterfaceId, parent port / bridge / VLAN / loopback
      AddressBinding[]                  stable AddressBindingId, IPv4 prefix / address policy
      RouteEntry[]                      RouteId, dest prefix, next-hop, egress selector/metric
    ServiceBinding[]                    stable ServiceId, bind InterfaceId / ingress domain
      DhcpServerPool[]                   pool/prefix/ranges/reservations/options, lease policy
  PhysicalLinkDefinition[]             LinkId, endpoint PortIds, media, latency, impairment
  SimulationPolicy                      RNG seed, device defaults, background event policy
PresentationLayout                      DeviceId -> coordinates, labels, viewport (not forwarding)
RunSession                              config revision, runtime caches/FSMs, event queue, traces
```
- **PhysicalPort** is cable attachment, not necessarily a host IP interface. A generic switch port does not automatically have an IPv4 address.
- **BridgeInstance** forwards at L2 and owns learning/forwarding state by VLAN (when implemented). One bridge can have multiple physical access ports. An L3 SVI may attach to a bridge/VLAN as a logical interface.
- **LogicalInterface** attaches an L3 stack/address/policy to a port or L2 domain (or loopback). A home router can present one LAN IP on an internal bridge/SVI shared by four LAN ports and an independent WAN interface; neither one implies the other.
- **DHCP server pool** must have explicit receiving interface or relay binding; no reply through unrelated router WAN just because the device's DHCP toggle is enabled.
- Device profile describes enabled capabilities/defaults (Host, L2Switch, Router, SOHO-HomeRouter, future AP), but the network stack is assembled from bridge/router/service components. Profiles are versioned so future firmware-like behaviors do not retroactively alter old saved labs.
- Physical-link compatibility (media/port occupation/link up) is DISTINCT from semantic policy (LAN vs WAN, VLAN, DHCP reachability). An automatic cabling tool can warn but shouldn't disallow legitimate switch-to-WAN Internet uplinks.

## Identity and validation rules
1. Distinct immutable typed IDs for Device, Port, LogicalInterface, Bridge, Link, Service, Packet, Event and Probe; labels and IPs are not identity. Cross-project references invalid.
2. Each standard point-to-point wired port connected to at most one link. Self-cabling, same-port two endpoints, unknown/dangling ID, mismatched media and duplicate link claims rejected unless explicit future hardware profile supports it.
3. Every logical interface must have exactly one valid parent or documented special loopback/virtual link. A physical port may be member of only one untagged native/access bridge context per selected profile, while tagged VLAN membership rules are modeled separately.
4. A device may have duplicate IP to another *isolated* device; warn of overlapping IPs on shared domain but do not globally forbid (VRFs, isolated networks, experiments). A route must not be made automatically by a UI-canvas cable crossing.
5. Bridge membership, VLAN tag conversions, L3 address scopes and DHCP service-binding are explicit; no implicit any-port/any-VLAN forwarding.
6. Link/router config changes applied at an atomic engine command boundary; remove/detach invalidates cached ARP/MAC/FSM behavior by defined policy and suppresses stale pending delivery events. Do not assume all down-state caches flush; specify per protocol/profile.
7. Stable insertion order and numeric seeded default addresses never depend on nondeterministic hash iteration or Android rendering order.
8. Schemas must prevent unknown capability identifiers from being silently treated as compatible; unsupported features get typed errors, not no-op success.

## Worked topology A: correct home LAN
```text
PC1.NIC-0   -- Switch0.Fa0/1
PC0.NIC-0   -- Switch0.Fa0/2
Switch0.Fa0/3 -- SOHO-Router0.Ethernet1
SOHO-Router0 LAN bridge = {Ethernet1, Ethernet2, Ethernet3, Ethernet4}
SOHO-Router0 LAN logical interface = 192.168.0.1/24 on LAN bridge
SOHO-Router0 WAN logical interface = Internet0 (separate routing domain)
DHCP server ServiceBinding = Router0.LAN; pool 192.168.0.100..149,
  DHCP router option 192.168.0.1 and mask 255.255.255.0
```
Discover: source PC unconfigured -> limited broadcast out PC.NIC; switch floods to Ethernet1; router internal bridge delivers to LAN DHCP service; server offers valid configuration if pool/lease permits. Packet/events cite each port and actual service decision.

## Worked topology B: physically valid, semantically wrong for LAN DHCP
Cable Switch0.Fa0/3 -> SOHO-Router0.Internet0 (WAN). Physical layer accepts if Ethernet media compatible. The switch can deliver DHCP Discover to WAN ingress, but NO LAN service responds without a separately bound DHCP service or relay. PC DHCP retries according to FSM and *may*, per selected IPv4LL policy and RFC, choose 169.254/16 after conflict probing; absence of default route makes off-subnet ICMP drop at source. **Not every legitimate WAN link is an error**. The diagnostic is "pool not bound here", not "no physical path".

## Worked topology C: misleading equal IP labels
Two SOHO routers independently have LAN IP 192.168.0.1 on separate bridge domains; each has separate WAN port, WAN-to-WAN cable may be up. Simple PDU "Router0 -> Router1" is incomplete unless source port/interface and precise destination IP/optional expected remote router/interface are visible. Successful local loopback/self-address ICMP is not remote reachability. Disconnect WAN; a remote-target result must fail (or UNKNOWN until trace proves reachability), even if address-only echo returns locally.

## Candidate run-time forwarding path (must be prototyped)
```text
Host route-selection -> local delivery OR neighbor resolution -> IP PDU + Ethernet frame
 -> physical port egress -> link propagation/queue event -> peer port ingress
 -> bridge membership/VLAN checks -> MAC table action (drop/forward/flood)
 -> logical interface/host stack ingress OR more bridged forwarding
 -> protocol service bound at correct interface -> eventual response via same rules
```
Crossing a router into another broadcast domain requires explicit IP forwarding/route behavior, not Ethernet flooding.

## Future completeness probes
- Wi-Fi: association/radio link vs L2 bridge member, SSID/VLAN/security; cannot model as a copper cable disguised as radio.
- Layer-3 switch: SVIs routed between VLAN bridge instances without duplicating devices.
- Router-on-a-stick: VLAN-tagged subinterfaces sharing one physical trunk.
- Subinterfaces, VLAN 0/4095 reserved tags, QinQ future, native VLAN mismatch.
- DHCP relay crosses L3 boundary by explicit relay component, not all-LAN broadcast forwarding.
- VPN/tunnels/VRF need separate logical contexts and routing tables, not new physical copper lines.
- Stacked switches/bundles/LAG and shared wireless medium require port/link cardinality additions with explicit profile and migration policy.
- Packet trace continuity when topology changes while frame is in flight: policy chosen and tested.
- MAC/IPv4 config changes during lease/ARP transactions: actor-generation tokens and stale event handling.

## Acceptance table (planned, NOT tested)
| Fixture | Input | Required observable outcome |
|---|---|---|
| D01 | PC to switch to LAN bridge with DHCP | Discover reaches LAN service; valid Offer/ACK possible |
| D02 | PC to switch to WAN with LAN-only pool | Discover reaches WAN ingress; zero LAN pool Offer |
| D03 | PC to switch, no router route | off-link unicast dropped at host before frame |
| D04 | two routers, duplicate isolated LAN IP | allowed config; selected-target proof not faked |
| D05 | untagged port placed in incompatible bridge mode | validator rejects/warns as configured |
| D06 | switch unplugged during frame transit | deterministic in-flight event policy; never phantom successful receive |
| D07 | host multiple NICs | independent address/DHCP/neighbor tables and route selection |
| D08 | auto-wiring sees WAN vs LAN | explicit chosen port with warning and override |
| D09 | new AP SSID wireless station | requires specified association/broadcast model; no unsupported magic |
| D10 | route via next-hop | ARP resolves next-hop IP on local egress, not remote destination |

## Open S03 decisions
- Model device-local bridge links as explicit graph edges vs contained object memberships?
- Per-interface VRF and VLAN tagging representation; avoid premature public serialization freeze.
- Ethernet media speed/duplex/auto-negotiation approximation and precise wireless medium representation.
- Default device profile semantics and profile-version migration.
- Dynamic topology changes and event invalidation policy.
- UI "two routers connected" target-address resolution and self-address verification.
Stop architecture freeze until targeted prototype + adversarial fixtures succeed. Document final choices in ADR-0005.
