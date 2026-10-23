# VirtualNetLab system contracts (pre-implementation design)
Status: CANDIDATE semantics / architectural review required | 2026-10-23. No binary ABI, field serialization or minSDK is frozen. [Blueprint](../architecture/ARCHITECTURE_BLUEPRINT.md), [master plan](PHASE1_MASTER_PLAN.md).

## 0. Invariant vocabulary
Device = simulated equipment with capabilities; Port = distinct physically connectable endpoint; Link = pair of ports and medium; BridgeDomain = L2 forwarding/broadcast partition; LogicalInterface = L3 address/routing attachment to a bridge or independent port; ServiceBinding = protocol service attached to explicit interface/domain; Runtime = FSMs, queues, MAC/ARP tables, DHCP leases; Presentation = visualization only.
**Canonical IDs are typed, stable, immutable within one project**, never names, coordinates or IP values. Multi-LAN/WAN consumer router is a composed device (LAN bridge, WAN L3, optional switch ports, IP stack, DHCP/NAT as enabled). A physical cable does not entail one subnet or broadcast domain.

## 1. Candidate entities, fields and validation
| Concept | Candidate fields | Must hold |
|---|---|---|
| LabDesign | schemaVersion, projectId, seed, profileVersions, nodes, ports, links, config, layout | No orphan ID; deterministic order; version recognized |
| Device | deviceId, displayName, deviceProfileRef, enabledCapabilities, configRevision | Name not unique ID; capability and profile version agree |
| PhysicalPort | portId, deviceId, medium, duplex/capabilities, adminStatus, portRole, connectedLinkId? | A point-to-point Ethernet port participates in at most 1 physical link |
| Link | linkId, endpointA, endpointB, medium, adminStatus, physicalDelay, impairmentPolicy | Distinct existing endpoints, compatible roles/media, no self-link unless model explicitly permits |
| BridgeDomain | bridgeId, memberPortIds, VLAN/rule set, STP context? | No unintended L2 leak; explicit tag/access mapping |
| LogicalInterface | interfaceId, deviceId, parentPhysicalPortOrBridgeId, addressBindings, adminStatus, mtu | No implicit L3 address on bare unmanaged switch ports |
| IpConfiguration | addresses, prefixLengths, onLinkRoutes, defaultRoutes, DNS, assignmentPolicy | Network/routing policy validates mask and next-hop for configured scope |
| ServiceBinding | serviceId, protocol, boundInterfaceOrDomain, config, enabled | DHCP LAN pool cannot respond on unrelated WAN by mere device presence |
| SimulationSession | designRevision, engineVersion, clockTicks, queue, PRNG, runtimeActors, stateRevision | Compatibility and deterministic rehydration documented |
| TraceRecord | eventId, virtualTime, seq, actorId, ingressPort?, egressPort?, packetId?, parentId?, correlationId?, outcome, reasonCode?, stateRevision | If forwarding event, source/target and causal parent actually exist |
| Probe | probeId, originDeviceId, originInterfaceId, destinationAddress, expectedDeviceId?, expectedInterfaceId?, expectedPath? | Response identity and intended-target evidence are separate |

Fields above are **candidate public semantics**, not a claim of finalized JSON schema. No arbitrary model-specific property dictionaries without validation.

## 2. Session semantics
- Single owner processes all action commands and scheduled events; UI/CLI, automation and scenarios send the **same validated command types**.
- Commands: CreateDevice, DeleteDevice, ConnectPort, DisconnectPort, SetPortConfig, ConfigureLogicalInterface, ConfigureService, InjectProbe, BeginRun, PauseRun, StepEvent, ResetSession, SaveDesign, SaveCheckpoint, ImportProject. Mutating config produces validation response with durable design revision and explicit **runtime invalidation** rules.
- Commands have request ID, expected design/session revision (optimistic collision guard), origin (GUI/CLI/scenario), payload and desired effective boundary. Reject stale edits explicitly rather than overwrite.
- Engine is the authoritative virtual-time clock. Ordered commands received while running are assigned a **safe event boundary**; deterministic replay logs order and effective virtual timestamp. Live UI thread does not mutate runtime actors.
- Event scheduling uses non-negative integral ticks and strict (timestamp, insertionSequence) total order; equal-time events never depend on thread interleaving or hash-table iteration.
- A simulation event is an atomic state transition: ingress/actor check -> protocol dispatch -> egress/scheduled actions -> trace/state delta. Background events are actual state changes/timers, not generated because someone selected a protocol checkbox.
- Define hard caps on same-tick events, per-run steps, queue occupancy, recursion depth, data size and trace retention **before production**. Hitting limit halts/pauses with auditable error and last valid snapshot.
- A canceled timer MUST NOT later mutate a replaced/deleted device; use actor generation/version tokens or event cancel semantics; choose based on S01.

## 3. Time and replay
Time = simulated, not wall-clock. Running in a fast-forward mode advances to next scheduled event, even minutes later; real-time mode delays **presentation/execution** to match the visual clock when possible without changing event order. Single-step means ONE internal event; "next packet hop" walks the causal chain and is a UI action over successive events.
Replay identity tuple: (versioned lab design, initial runtime snapshot or reset seed, engine/protocol versions, ordered commands with virtual boundaries). The invariant is identical **semantic** event trace, including accepted/rejected commands and per-port packet decisions. Byte-identical trace archive format is a separate target.

## 4. Packet contract and state boundaries
A logical packet or frame is NOT a pictogram. Minimum explicit header fields for modeled protocols, valid ingress and egress interface, immutable packet identity/provenance plus authorized mutable fields (TTL, checksums, VLAN tags). Distinguish protocol events vs packet events vs UI animation frames; transient packet hops are derived from actual dispatch records.
A trace has **packet lineage** and test correlation; a flood may legitimately spawn branches but may not fabricate origin. Routing/ARP next hop and VLAN domain determine real destination. Pure local delivery can be successful ICMP *but not* evidence of a different expected remote device.

## 5. Failure classification
Required typed errors and trace reasons:
- Invalid design/action: UNKNOWN_DEVICE, UNKNOWN_PORT, PORT_ALREADY_LINKED, INCOMPATIBLE_MEDIUM, INVALID_IP_PREFIX, STALE_REVISION, UNSUPPORTED_FEATURE, INVALID_PROFILE_VERSION.
- L1/L2: LINK_DOWN, PORT_ADMIN_DOWN, VLAN_NOT_ALLOWED, STP_BLOCKING, INVALID_FRAME, NO_L2_PATH.
- Host/L3: NO_ROUTE, DEFAULT_GATEWAY_MISSING, ARP_UNRESOLVED, TTL_EXPIRED, INVALID_ADDRESS, MTU_POLICY_UNSUPPORTED.
- DHCP: NO_DHCP_SERVICE_ON_INGRESS, POOL_EXHAUSTED, DHCP_XID_MISMATCH, DHCP_LEASE_EXPIRED, CLIENT_RETRANSMIT, IPV4LL_CONFLICT.
- Engine/storage: EVENT_LIMIT_REACHED, EVENT_TIME_OVERFLOW, SAME_TICK_LIMIT_REACHED, TRACE_RETENTION_LIMIT, CORRUPT_FILE, UNSUPPORTED_SCHEMA.
- Diagnostic result levels: REPLY_OBSERVED, EXPECTED_TARGET_CONFIRMED, EXPECTED_PATH_CONFIRMED, UNKNOWN_TARGET_IDENTITY, NOT_REACHABLE, INCOMPLETE_SIMULATION.
Each reason triggers **only on a modeled condition**. Some are planned and not enabled until corresponding protocol implementation. A suppressed UI event is NOT a dropped packet.

## 6. Simulator/Android interface design
- Engine accepts high-level validated immutable commands; returns success/failure plus new revision and a bounded set of read-only state/trace projections. Device editor/CLI must reflect same command result. UI reads snapshots (not internal mutable references).
- Android may request trace pagination by timeline range, device ID, packet correlation or protocol; rendering and filtering must not modify engine queue.
- Storage receives portable LabDesign and optional versioned SessionSnapshot/TraceSegments; never persist large run object into SavedStateHandle.
- Threat boundary: imported lab is untrusted **data**, not code. No arbitrary engine plugin loading, OS socket/raw packet access or filesystem capability from user project.

## 7. Four mandatory invariant proof fixtures
(1) Source/self ping with detached WAN proves **reply != remote device reached**.
(2) DHCP Discover traverses PC-switch-WAN physical link but service bound LAN ignores it; no made-up Offer.
(3) Multi-port bridge vs routed WAN have distinct broadcast domains, even on same named router.
(4) Renderer filters out STP/DTP/ARP events without mutating or rescheduling them.

## Decisions deferred and blocking tasks
Numeric virtual time unit, data layout, serialization archive, packet byte encoding, max sizes, allowed live configuration edits, exact order of event generation for protocol timers, selected base device profiles, integer overflow behavior and "host sends while ARP pending" queue policy. See [decision gates](DECISION_GATES.md); no production API freeze until these have evidence.
