# Device capability and composition catalog (candidate v0.1)
Status: PLANNING / not implemented | 2026-10-23 | [top-down map](TOP_DOWN_CAPABILITY_MAP.md) · [network stack](NETWORK_STACK_DECOMPOSITION.md) · [port model](DEVICE_AND_INTERFACE_MODEL.md).

## Why profiles, not magic device classes
A "router" icon is NOT an inherent rule for switching, DHCP, wireless, NAT or VLANs. Each virtual device is a versioned **profile** made of physical ports, optional bridges, L3 interfaces, protocol agents, services and management surface. Several roles may coexist in one device. Basic hosts may have multiple NICs. Adding a new profile must not change existing project behavior without migration or explicit opt-in.

### Candidate profile metadata (not final serialized ABI)
`ProfileId; profileSchemaVersion; displayCategory; manufacturingNeutralName; portTemplates; bridgeTemplates; interfaceTemplates; protocols{version,supportLevel}; serviceTemplates; defaultConfig; allowedConfigOperations; telemetrySchema; simulatedCostHints; migrationStrategy`.

Capability declarations cover *implemented behavior*, not arbitrary protocol badges. A model's support level is the minimum verified conformance level across required transitions. Unknown profile/version: explicit unsupported error, no silent replacement with "generic working device".

## Initial and future profiles: exhaustive foundation, scoped support
| Device profile | Physical / logical architecture | Earliest meaningful support | Explicit boundary |
|---|---|---|---|
| Host-PC | One Ethernet NIC; L3 IPv4 stack, ARP, ICMP; DHCP client | initial core | No implied physical Internet or full desktop OS |
| Multi-NIC host | Two+ physical interfaces; per-NIC ARP/DHCP, common or selected routing policy | model now, enable after tests | Multi-homed source/egress selection not handwaved |
| Ethernet L2 switch | N physical access ports, bridge, learned MAC table; later VLAN/STP | initial core basic switching | No implicit IP routing or automatically functioning STP |
| Plain router | 2+ physical ports with distinct L3 interfaces, route table | basic L3 after host/switch | No implicit NAT/DHCP/Wi-Fi |
| SOHO/home router | Four-ish LAN switch/bridge ports + separate Internet WAN port, LAN L3 SVI, DHCP server, optional NAT/AP | test focus early | LAN and WAN not interchangeable; DHCP pool bound to LAN |
| Server | Host NIC + selected service agents (DHCP, later DNS/HTTP/FTP) | initial DHCP service via router/host | No real Linux server, no app success without packet exchange |
| Wireless access point | Wired uplink/bridge + radio MAC/association/SSID; optional security | later logical Wi-Fi slice | Association alone is not RF propagation fidelity |
| Wireless station | Wi-Fi NIC + logical host IP stack, per-BSS association | later | No automatic airtime/802.11 frame realism |
| L3 switch | L2 bridge/VLAN + L3 SVIs and routing | expansion | Must not share unrelated routing/bridge tables |
| Cloud/ISP node | Explicit topology source/sink or provider model with defined service | optional | Do not imply actual internet access |
| Security appliance | Routed/bridged interfaces + ACL/state/NAT models | future | Unsupported policy is not automatically enforced |
| End-user mobile device | Wi-Fi client + host stack + simple app intents | later | Separate Android-host app from *simulated* mobile node |

## Device lifecycle
1. Place device with stable ID/profile/version. Display/layout is separate.
2. Instantiate validated default configuration with explicit physical ports and logical groups; default IP/service policy recorded, not randomly inferred.
3. Bind link endpoints; physical up/down and negotiation modeled within declared scope.
4. Start session actor graph; deterministic control timers only for supported services.
5. Apply config via typed command. Capability and revision checks; state transition and trace.
6. Disconnect/disable/delete: invalidate pending event generations; preserve or flush caches only per profile policy; exact effects documented.
7. Persist design and optional runtime snapshot with version compatibility; unknown newer profile gives safe "unsupported" with no fictional output.

## Internal composition examples
SOHO A:
```text
port Internet: Ethernet wired -> L3 WAN (independent broadcast domain)
ports LAN1..LAN4: Ethernet -> internal Bridge B-LAN -> L3 LAN=192.168.0.1/24
B-LAN -> DHCP server service bound to LAN L3 / ingress
router IP FIB: local delivery + WAN/LAN connected routes
NAT/firewall: NOT IMPLEMENTED until explicitly modeled
wireless AP: NOT IMPLEMENTED until association/bridging model verified
```
Switch S: Ethernet ports -> bridge B-DEFAULT with MAC table -> no L3 by default. Future VLAN access/trunk membership maps tagged frames into distinct bridge domains; one network-visible physical switch may own many logical VLAN contexts.
PC H: NIC -> ARP cache scope -> IPv4 stack/routes/ICMP, DHCP/IPv4LL FSM per policy. Application requests use host network stack; no direct fake ping.
 
## Operational capability matrix rules
- `canForwardL2`, `canForwardIPv4`, `canServeDHCPv4`, `canUseDhcpClient`, `canCreateVlan`, `canRunSTP`, `canNegotiateDTP`, `canHostService`, `canAssociateWiFi` must represent VERIFIED capability plus selected device configuration; boolean alone insufficient to express fidelity level/version, so persist typed capability references.
- Default status of STP/DTP/Wi-Fi/NAT/IPv6 is NOT_IMPLEMENTED until conforming model tests pass.
- Device-specific factory defaults are *profile data*, and must not be mistaken for universal networking standards. The user's observed DHCP/WAN failure is one particular SOHO profile configuration, not a rule preventing DHCP on every WAN.
- A user may deliberately select physically valid but logically surprising WAN links; tooling warns with evidence, never silently rewires to LAN.

## Profile conformance matrix
Host fixture: on-link, off-link/no route, local self address, multiple NIC routing.
Switch fixture: broadcast flooding, known MAC egress, unknown-unicast flooding, link down, cycle safety.
Router fixture: local vs forwarded IPv4 packet, connected route, next hop, TTL, no route.
SOHO fixture: LAN bridge / WAN isolation, DHCP bound ingress, duplicate LAN IP remote test.
Server fixture: protocol/socket binding/UDP service, no direct fake response.
AP fixture: only allowed once binding/association/medium subset is named and tested.
All profiles: typed IDs, revision control, save/reload, timer invalidation, trace identities, supported feature registry; no "device added" success without valid instantiated model.

## Decisions before stable profile schema
Bridge membership structure, profile capability keys/version migration, embedded internal bus/virtual ports, per-profile timers, L3 subinterfaces/VRFs, manual default service presets, wireless medium abstraction and event runtime cost. Gate S03 checks these before code, not during broad device feature development.
