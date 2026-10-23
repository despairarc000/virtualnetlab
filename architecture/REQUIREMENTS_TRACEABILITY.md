# Requirements and verification traceability
Status: PROPOSED, no executable runtime tests yet | 2026-10-23. Define acceptance before code. Links: [vision](../IDEA_PLAN.md), [blueprint](ARCHITECTURE_BLUEPRINT.md), [gates](IMPLEMENTATION_ROADMAP.md), [validation](VALIDATION_STRATEGY.md).

| ID | User/product requirement | Owning module/contract | Proof / scenario | Target gate |
|---|---|---|---|---|
| REQ-01 | Construct actual virtual network topology | Topology model / port validator | connect/disconnect port and wrong-media tests | G1 |
| REQ-02 | Config and real runtime behavior agree | Command reducer / protocol actors | UI vs CLI vs engine state identity | G1, G6 |
| REQ-03 | Simulation step/run/pause accurate | Integer-tick scheduler / serial actor | deterministic equal-time replay, no wallclock dependence | G1 |
| REQ-04 | PC-switch LAN ICMP works | Ethernet, bridge, ARP, IPv4, ICMP | golden same-LAN probe with actual port chain | G2 |
| REQ-05 | Link/network failure produces actual drop reason | Trace and diagnostics | missing gateway and link down negative traces | G2 |
| REQ-06 | DHCP success and WAN-only failure | DHCP client/server per interface | WAN-port wrong-pool Discover, DHCP not returned | G3 |
| REQ-07 | IPv4LL fallback is not fictional DHCP success | Separate IPv4LL state machine | 169.254 address, probes/retries and missing gateway | G3 |
| REQ-08 | Same-valued local IP not proof remote path | Probe expected target/interface | physically disconnected WAN test | G2 |
| REQ-09 | Transparent background events and filters | Simulation + read-only inspector | STP/DTP when supported; filter never changes queue | G4/G5 |
| REQ-10 | Device protocols have declared accurate boundaries | Model registry and standards mapping | positive/negative RFC-based test per model | each gate |
| REQ-11 | Mobile touch lab is usable | Android Canvas/View + ViewModel | hit-tested ports, zoom/pan, TalkBack and screen rotation | G0/G4 |
| REQ-12 | Offline first and recoverable | Storage repository / checkpoint | airplane-mode operation, process death save recovery | G4 |
| REQ-13 | Projects share safely | Strict schema/parser/importer | bad IDs/version/zip bomb/path traversal/adversarial file tests | G4 |
| REQ-14 | A student can learn from genuine outcomes | Scenario evaluator + causal diagnostic | alternate valid solutions accepted; reason cited by event | G6 |
| REQ-15 | Functional scale on 4GB phone | Engine budgets, trace paging, UI throttling | measured memory/frame/throughput for 10/50/100 nodes | G0/G4/G7 |
| REQ-16 | Port auto-choice does not mislead | Port capabilities + warning UI | WAN warning without banning legitimate WAN | G4 |
| REQ-17 | Vendor independence / legal licensing | Asset/dependency management | SPDX SBOM, no proprietary firmware/branding | every gate |
| REQ-18 | Extensible without sacrificing safety | Capability profile and adapters | unknown profile rejected; no executable import plugins | G1/G7 |
| REQ-19 | Test results prove destination path | Probe correlation & expected path | reply, expected device, path independently reported | G2 |
| REQ-20 | Build/install Android APK rather than static mock | Android Gradle app and CI | APK + emulator and real-device test | G4 |

### Completion discipline
A requirement passes only after its test exists and ran successfully with recorded code head, Android/engine version, fixture and oracle. Developer prose and Packet Tracer screenshots are not success evidence. Test IDs assigned in repository as code arrives; update this table and Graphify links in the same PR.

## End-to-end capability trace extension — 2026-10-23
| UJ | User requirement | Owner / subsystem | Planned proof |
|---|---|---|---|
| UJ-01 | Create lab | [device model](../phase1/DEVICE_AND_INTERFACE_MODEL.md), [catalog](../phase1/DEVICE_CAPABILITY_CATALOG.md) | Valid/invalid links and saved project |
| UJ-02 | Configure | [system contracts](../phase1/SYSTEM_CONTRACTS.md) | UI+CLI+engine config same revision |
| UJ-03 | Run | [event engine](../phase1/EVENT_ENGINE_CONTRACT.md) | Same seeded traces in live/step |
| UJ-04 | Inspect | [diagnostics](../phase1/DIAGNOSTICS_AND_EDUCATION.md) | Port/parent/packet/actor trace |
| UJ-05 | Troubleshoot | [network stack](../phase1/NETWORK_STACK_DECOMPOSITION.md) | Wrong WAN DHCP and source no-route |
| UJ-06 | Verify | [diagnostics](../phase1/DIAGNOSTICS_AND_EDUCATION.md) | Local self-ping never remote success |
| UJ-07 | Learn | [diagnostics](../phase1/DIAGNOSTICS_AND_EDUCATION.md) | Equivalent subnet designs score same |
| UJ-08 | Continue | [persistence](../phase1/PERSISTENCE_AND_COMPATIBILITY.md) | Crash/recovery/migration |
| UJ-09 | Scale | [Android spec](../phase1/ANDROID_EXPERIENCE_SPEC.md) | 4GB frame/heap/queue benchmark |
| UJ-10 | Extend | [capability catalog](../phase1/DEVICE_CAPABILITY_CATALOG.md) | Unknown profile rejected, versioned capability |
Not implemented/verified yet. Read [Phase 1 audit](../phase1/EXIT_AUDIT.md) before promotion.
