# Diagnostics, learning workflow and assessment contract
Status: PROPOSED design | 2026-10-23 | [capabilities](TOP_DOWN_CAPABILITY_MAP.md) · [system contracts](SYSTEM_CONTRACTS.md) · [test vectors](STANDARDS_TEST_VECTORS.md).

## Observation must reveal cause, not speculate
A user needs answers to: *What did I do? What really happened? Where? In what order? With what headers/state? Why did it stop or succeed? What can I change to verify a hypothesis?* The assistant/help UI is a reader of trace facts and published protocol rules, never a generator of fictitious packets.

### Required information models
- **Event**: simulation time, total sequence, actor (device and protocol component), ingress/egress physical/logical interface IDs, operation (generated/received/scheduled/forwarded/dropped/local), code, previous event, packet lineage and correlations, relevant state delta and model version.
- **Packet inspector**: decoded supported header fields across applicable stack; show undecoded/unsupported payload explicitly; selected payload is not necessarily full wire bytes.
- **State inspector**: link/admin state, bridging/MAC entries, ARP cache, IP addresses/prefixes/routes, DHCP FSM/lease, protocol control state, pending timers and warnings within scoped model support.
- **Path explorer**: provenance graph from injected probe to descendant frames and responses; branches for flooding, asynchronous timers and background control; no magical single linear path if multiple egress copies exist.
- **Test result**: `echoReplyObserved`, `matchingRemoteTargetObserved`, `expectedPathConfirmed`, `simulationComplete`, `confidenceAndLimits` stored as distinct fields, not a generic green boolean.
- **Diagnostic**: finding ID, actual triggered reason, evidence event IDs, actor/interface, relevant config and supported model; candidates/hypotheses labeled separately.

## Global event queue and view semantics
Global scheduler contains automatic control traffic and user-triggered traffic from all independently connected networks. UI filters only change visible events: protocol type, device, correlation/probe, time, packet family, status. A filter must **never** pause, drop, re-order, cancel or create events. StepInternalEvent acts on next actual scheduled event; FollowThisPacket groups descendants while the engine advances through other real events as needed. "Next hop" is UI navigation through causal events, not a different simulator.

## Explanations of an observed DHCP failure
- Fact 1: DHCP Discover created by PC0, UDP 68 to UDP 67, L2 broadcast and IPv4 limited broadcast, no existing IPv4 lease required.
- Fact 2: Switch0 receives and forwards frame to router Internet port; physical path was valid.
- Fact 3: LAN DHCP server's service/pool binding does not cover WAN ingress; no response from that service.
- Fact 4: Client retransmits, and possibly begins a separate IPv4LL FSM after policy-specific delay, probes and conflict checking.
- Fact 5: Later off-link packet may fail at source because no route/default gateway; this **cannot be attributed to switch STP or DTP without supporting trace evidence**.
- Remediation suggestion: check uplink port and pool binding; choosing WAN may be intentional, so offer to verify desired network design, not force "fix."

## Provenance and diagnostic certainty
Truth table:
| Case | Allow statement |
|---|---|
| ICMP echo reply from unspecified matching IP | "Echo reply observed from address X" |
| Event delivered to expected device's IP handler | "Intended device observed receiving packet" |
| Full expected physical path correlated | "Specified path verified for supported model" |
| No echo during timer budget | "No reply observed within this simulated interval" |
| Unsupported protocol component | "Result unknown / feature unsupported", NOT "failed" |
| Retained trace truncated | "Only partial evidence available", never complete path |
| Local-source IP self-match | "Local delivery; cannot prove remote link" |

No "why" explanation solely based on diagram geometry, IP label, or green PDU status. Descriptive AI helper, if introduced, only paraphrases structured evidence and citations. The offline core must not require remote inference.

## Lab definition, learning and assessment
```text
LabTemplate:
  id/version, skill objectives, supported feature/model versions
  starting LabDesign, optional initial runtime seed
  stated constraints (allowed devices/operations), instructions, hint tiers
  completion predicates (semantic state, trace, path, configuration)
  prohibited shortcuts, accepted alternatives, grading rubric/weights
  feedback/evidence snippets, accessibility language/localization
```
Evaluation is a **bounded query over canonical design/runtime/trace evidence**, not arbitrary executable code, shell commands or user-scriptable plugins. It may require 2 subnets, host reachability across router, isolated VLANs, router DHCP pool, or documented evidence of fix. It must accept functionally equivalent topologies/IP schemes unless task explicitly constrains addresses and ports. It must not grant credit when packet animation happened but required remote target never received a message.

### Hint tiers
Level 0 objective reminder; Level 1 suggest subsystem to inspect (interface / ARP / route / DHCP); Level 2 point to evidence event and relevant configuration; Level 3 explain causal chain; Level 4 show a possible fix with explicit alternative paths. Hints never mutate simulation unless user explicitly applies a valid configuration command.

## Learning accessibility
Beginner and advanced views share identical network state, differing only in disclosure. Offer text-first inspectable event details, semantic color-independent badges, TalkBack device/port lists, reversible exploration, read-only snapshot of previous trace and "what changed" diff after editing.

## Test design
- One network with two possible correct host IP schemes; both pass semantic objective.
- Wrong WAN-port DHCP failure; diagnostic cites actual ingress and service binding, not generic "DHCP off."
- Duplicate router LAN addresses on isolated domains; selected target identity must not be faked.
- STP/DTP background events appear globally; filter does not affect processing, StepNextPacket follows selected causal chain.
- Truncated trace, unsupported model or incomplete run never yields definitive success.
- Bad DSL import with unknown assertions fails without execution.
- Check explanations for consistency with trace; unknown remains unknown.

## Later decisions
Scenario schema and rubric DSL details, localization, instructor authoring interface, snapshot compare format, retention/privacy of logs, optional adaptive hints/AI and graded exports. Design separate independent assessment engine and trace adapter before making promises.
