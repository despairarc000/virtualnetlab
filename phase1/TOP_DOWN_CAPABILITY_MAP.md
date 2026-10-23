# Top-down capability map: why, who, what, how, evidence
Status: PROPOSED v0.1; planning only | 2026-10-23 | [Phase 1](PHASE1_MASTER_PLAN.md) → [architecture](../architecture/ARCHITECTURE_BLUEPRINT.md) → [acceptance](../architecture/REQUIREMENTS_TRACEABILITY.md)

## 0. User-facing mission and definition of success
VirtualNetLab is an **offline-first Android virtual networking laboratory**. The target behavior is to design, connect, configure, operate, inspect, troubleshoot and learn a network, with the devices and protocols actually generating causally justified outcomes. A network diagram, animation or guessed diagnostic does **not** fulfill the mission. Full Cisco proprietary feature parity is neither the definition nor an immediate claim.

## 1. Roles and corresponding jobs
| Role | Real-world job | Must be able to prove |
|---|---|---|
| Beginner | Discover what switches, routers, subnets and protocols do | Build two-host LAN and explain observed ARP/ICMP path |
| Troubleshooter | Locate cause of a failure | Show source/ingress/decision causing DHCP or routing failure |
| Student | Complete topology/configuration lab | Meet semantically checked objectives without hidden scripted answer |
| Instructor | Author and assess a lab | Express constraints, tests, hints, rubrics and expected capabilities offline |
| Experimenter | Change topology/protocol config and compare | Repeat same seed/inputs; inspect deltas, invalidation and unsupported parts |
| Advanced learner | Understand interactions and edge cases | Examine L2/L3/transport/application control and data planes independently |

### Core user journeys (acceptance IDs)
- **UJ-01 Create:** blank network, starter topology, rename/save/restore, valid/invalid port attachment
- **UJ-02 Configure:** IP/prefix/gateway/DHCP on host/router with validated, versioned device state
- **UJ-03 Run:** global background timer events + user-sent PDU; exact step/run/pause semantics
- **UJ-04 Inspect:** trace packet headers, route/bridge decision, ingress/egress, cache/lease tables, timeout
- **UJ-05 Troubleshoot:** wrong WAN uplink, no pool on ingress, IPv4LL independently, source-side no route
- **UJ-06 Verify:** detect same-address local self-ping vs actual intended remote device/path
- **UJ-07 Learn:** explain why with trace-based evidence; objective-based lab assessment
- **UJ-08 Continue:** offline open/reopen; safe autosave and compatibility behavior
- **UJ-09 Scale:** inspect large topology with accessible touch targets and capped event logs
- **UJ-10 Extend:** add new device/protocol type under the same port/actor/trace/education contracts

## 2. Product capability tree (requirements, not claims)
```text
Virtual networking laboratory
 ├─ Author a network
 │   ├─ Device library: host, multi-NIC host, L2 switch, router, SOHO router, server, AP, wireless client
 │   ├─ Physical/logical topology: interfaces, media, LAN/WAN roles, VLAN domains, labels/layout
 │   ├─ Configuration: UI forms, typed CLI, service bindings, saved configs, validation/undo
 │   └─ Import/export: templates, shared labs, migrations, reversible actions
 ├─ Operate a virtual network
 │   ├─ Time engine: scheduler/queues/timeouts/seed/replay
 │   ├─ Link/bridge: Ethernet, MAC learning, ARP and link state
 │   ├─ Network: host routes, IP, ICMP, router forwarding, VLAN, STP, IPv6
 │   ├─ Transport/application: UDP/DHCP, TCP, DNS/HTTP, application servers
 │   └─ Wireless/security: 802.11 behavior, SSID/AP, ACL/NAT, optional advanced model levels
 ├─ Observe
 │   ├─ Realtime/simulation views of SAME run
 │   ├─ Event list, packet inspector, routing/MAC/ARP/DHCP states, correlation graph
 │   ├─ Per-event proof and failure reason with supported fidelity level
 │   └─ Snapshot/replay/trace compare, export with provenance and completeness flags
 ├─ Learn and evaluate
 │   ├─ Free exploration + guided activities + scenario templates
 │   ├─ Correctness judged from outcomes/config/state, not visual placement
 │   ├─ Why/how causal explanations tied to actual events and RFC/model scope
 │   └─ Instructor authored goals, rubrics, constraints, feedback
 └─ Deliver on Android
     ├─ Offline touch / accessible workspace, CLI keyboard
     ├─ Safe storage and process-restoration
     ├─ Constrained device performance and power budgets
     ├─ Threat-limited imported projects and model capabilities
     └─ Reproducible installable APK and independent device tests
```

## 3. Dependency chain from user's goal to low-level machine behavior
A user asks "Can PC0 ping Router0?" -> UI captures explicit target -> validated Probe command -> host route decision -> ARP/cache and Ethernet -> switch bridge decision -> destination port delivery -> destination IP/ICMP handler -> reply -> reverse path -> causal trace -> truth-based inspection and success classification. Every arrow requires an owner and test. *A green icon is the consequence of this chain, never its cause.*

A user asks "Why did DHCP not work?" -> DHCP client FSM -> UDP/IPv4/Ethernet frame broadcast -> physical switch ingress/egress -> router WAN/LAN domain -> applicable service binding -> no applicable pool -> no Offer -> retry/possibly independent IPv4LL acquisition -> local route decision for later ping -> trace-linked diagnostic. Here physical connectivity exists while application-layer service availability does not.

## 4. Functional planes must stay independent
- **Physical/media** describes where frames may move.
- **Data plane** executes each packet/frame forwarding decision.
- **Control plane** produces/changes forwarding/config state (ARP cache, route protocols, STP, DHCP client/server protocol messages as applicable).
- **Management plane** exposes user/CLI config, debugging and reset (not a second network runtime).
- **Observation plane** projects immutable actual runtime evidence.
- **Learning plane** evaluates versioned scenarios using state/events and documented goals.
These names are architectural separations; specific protocols may span planes. Do not classify every DHCP packet as a purely routing-plane event.

## 5. Delivery scope and fidelity
Level A (initial full lab slice): standalone wired Ethernet + switch + host/IPv4/ARP/ICMP + DHCP/IPv4LL and WAN-port semantics + full inspection. Level B: VLAN/routing/STP plus multi-hop server operations. Level C: CLI/guided labs, DNS/HTTP/TCP, NAT/ACL, IPv6 and modeled Wi-Fi. Level D: advanced protocols, large-scale performance, teacher authoring and optional external emulator bridge. Each new capability declares support status, RFC/standard subset and tests; do not imply it is currently implemented.
See [protocol matrix](../knowledge-system/vault/specs/PROTOCOL_MATRIX.md) and [stack plan](NETWORK_STACK_DECOMPOSITION.md).

## 6. Top-down coverage trace
| Mission verb | Concrete functionality | Owning planning spec | Evidence |
|---|---|---|---|
| Design | graph, typed ports, physical and logical topology | [device model](DEVICE_AND_INTERFACE_MODEL.md) / [catalog](DEVICE_CAPABILITY_CATALOG.md) | UJ-01, D01–D10 |
| Configure | canonical config and service bindings | [system contracts](SYSTEM_CONTRACTS.md) | UJ-02 |
| Operate | queued deterministic protocol events | [event contract](EVENT_ENGINE_CONTRACT.md) / [stack](NETWORK_STACK_DECOMPOSITION.md) | UJ-03, S-ENGINE-01 |
| Inspect | source-to-destination trace and live state | [diagnostics](DIAGNOSTICS_AND_EDUCATION.md) | UJ-04, S-ICMP-01 |
| Troubleshoot | decision reason codes and ambiguous address checks | [failure atlas](FAILURE_AND_SECURITY_ATLAS.md) | UJ-05/06 |
| Learn | goal/rubric/hint with evidence | [diagnostics](DIAGNOSTICS_AND_EDUCATION.md) | UJ-07 |
| Save/share | durable portable versioned design | [persistence](PERSISTENCE_AND_COMPATIBILITY.md) | UJ-08 |
| Work on phone | responsive offline app and recovery | [Android experience](ANDROID_EXPERIENCE_SPEC.md) | UJ-09 |
| Expand | profiles/feature registry/standards and tests | [catalog](DEVICE_CAPABILITY_CATALOG.md), [roadmap](WORK_BREAKDOWN.md) | UJ-10 |

## Explicit non-goals of initial version
Running an actual IOS image, tapping the user's real Wi-Fi traffic, privileged emulation, automatic .pkt import, replicating Cisco branding, arbitrary plugin code, complete network protocol/radio realism, unrestricted indefinite background execution. These remain distinct research issues, not silently supported features.

## Validation & outstanding design questions
Personas need independent user/task review; mobile usability not measured; final lesson/rubric authoring format unfrozen; wireless physical fidelity and server OS application scope require separate later gates. Status: mapped, NOT independently validated.
