# Failure atlas, threat model and lifecycle recovery
Status: planning-grade adversarial checklist | 2026-10-23 | [Master](PHASE1_MASTER_PLAN.md), [risk register](../architecture/RISK_REGISTER.md), [validation](../architecture/VALIDATION_STRATEGY.md).

## Goals
Model intentional network faults and resist malformed lab files, unintended device identities, scheduler resource exhaustion, buggy protocol models and Android process loss. A virtual simulation must not silently leak into physical networking.

## 1. Topology and network errors
| Fault injection | Expected safe behavior | Evidence |
|---|---|---|
| Plug switch into router WAN instead of LAN | Physical Ethernet frames may reach WAN; no LAN-only DHCP service reply; explain ingress and offer absence | Per-port trace, no Offer |
| Duplicate IPs, separate LANs | Allowed as design if distinct L2/routing context; probe target identity isn't inferred from IP alone | Detach WAN, check target false |
| Duplicate IPs same LAN | Conflict possible; warning and ARP uncertainty/selected stack behavior | ARP/conflict event fixture |
| Missing default gateway | Off-link unicast rejected by host before Ethernet frame | Source trace only |
| Wrong subnet mask | May change on-link decision/ARP target; no silent "network knows best" | Routing-choice trace |
| Unavailable ARP target | ARP request and bounded retries/queued packet then failure | ARP_UNRESOLVED |
| Disabled port/link | No physical delivery; queued events invalidated | LINK_DOWN |
| Malformed EtherType/frame | Reject or explicit unsupported protocol state | INVALID_FRAME |
| VLAN mismatch/forbidden trunk | No VLAN crossing despite L1 up | VLAN_NOT_ALLOWED |
| Unprotected switch cycle | Finite simulation budget halts safely, no unbounded freeze | SAME_TICK_LIMIT/queue guard |
| DHCP server exhausted | No lease offered by inapplicable pool | POOL_EXHAUSTED |
| DHCP xid mismatch/late Offer | State machine ignores unmatching response | DHCP_XID_MISMATCH |
| DHCP disappears after lease | RENEW/REBIND behavior per selected modeled scope, eventual expiry | Lease state trace |
| IPv4LL candidate collision | ARP probing/conflict/new candidate, bounded | IPV4LL_CONFLICT |
| Fragment/TTL/routing loop | According to implemented model, no invented successful packet | TTL_EXPIRED or explicit unsupported |

## 2. Scheduler/replay robustness
- Pathological zero-delay recursion, same-tick broadcast storms, timer oversubscription, cancellation of deleted actor, changing link during in-flight frame, stale profile version and event sequence overflow.
- Every bounded resource failure preserves last validated state, emits typed code and stops the affected execution; no infinite loop or silent event clipping.
- No nondeterministic traversal of hash map/set for broadcast fan-out. Sorting/tie scheduling specified and golden-tested.
- UI filter, animation speed, rotation, live/simulation toggle cannot change semantic order.
- Multi-thread access to session rejected unless through command stream. Two commands to modify same revision -> detectable stale edit response.
- A trace's every child hop must have a connected, valid physical/logical path or modeled local delivery. Diagnostic actor/path is derived from actual engine records.

## 3. Input/project security
Threats: huge/unbounded JSON/deep nesting, arrays with duplicate IDs, links to nonexistent ports, invalid IP mask, profile not supported, unknown schema, path traversal in ZIP, decompression bomb, malformed UTF-8, string abuse, malicious scenario code, injected import filenames, arbitrary shell commands via CLI, untrusted extension metadata.
Controls: byte/time/depth/node/link budgets before allocation, explicit version handling, no shell eval/script execution from saved labs, allowlisted typed DSL commands, path canonicalization and archive unpack guards if archiving, checksums and safe failure that leaves current lab intact. Fuzz corpus and restore/regression must be part of Gate A/G4.
Future remote service adapters: separate opt-in and threat model; TLS/auth, hard socket/network permissions, revocation, resource limits. No default network permission for base laboratory if genuinely unneeded.

## 4. Android/data failures
- App backgrounded: scheduler pauses at boundary (if selected), save design and clear run-state semantics.
- Activity rotation: preserve viewport/select state without duplicating engine/session.
- Process death: recover committed LabDesign, optionally compatible and fully written SessionSnapshot; never silently "resume" from incomplete trace.
- Power/thermal/low RAM: adaptive UI frame throttling and engine bounded workloads; measurable pause responsiveness; no busy-loop to mimic network time.
- Import crashed mid-flight, disk full, concurrent save/migrate, incompatibility after upgrade: atomic revision files/checkpoint and clear recovery selection; never overwrite last known good file.

## 5. Privacy/legal/learning failure cases
No harvesting physical network data; no unapproved root, VPN or packet capture. Distinguish sample data vs any user-contributed packet bytes and strip personal information from shared traces. Document source licenses, icon branding, packet simulator limitations, official RFC version, security context. Assessments verify networking outcomes, not fixed pixel placements or a single hand-picked IP address. Accessibility must offer non-drag interaction.

## Required red-team validation
Run tests of one failure from **every row and bullet family**, including conflicting combinations: WAN misplug + IPv4LL + missing route; STP loop + 100k events; malicious file + restore; duplicate IP + local ping; background process kill during DHCP retry; unsupported protocol + user probe. Record actual result, branch/commit, model scope and any known deviation. No claim of comprehensive security certification based solely on design review.
