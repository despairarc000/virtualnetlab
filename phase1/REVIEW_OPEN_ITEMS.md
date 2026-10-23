# Phase 1 open-items register and evidence debt
Status: ACTIVE / blockers not completed, updated 2026-10-23. [Master](PHASE1_MASTER_PLAN.md), [exit audit](EXIT_AUDIT.md).

## Highest-leverage unresolved tasks in order
| ID | What could hit a wall | Required next proof | Blocking gate |
|---|---|---|---|
| P0-S10 | Filius vs fresh engine decision based on guesswork | Current v2.14 tagged source trace, packages/threads/license + Kotlin DES contrast | Engine selection signoff |
| P0-S03 | Cannot represent home router WAN vs LAN bridge/VLAN | Validate typed [port/interface schema](DEVICE_AND_INTERFACE_MODEL.md) via two independent architecture reviews and test topology | Model/schema freeze |
| P0-S01 | Race/non-replayable event engine | Prototype scheduler with same-time/cancel/storm/overflow and seeded 100-replay trace | Scheduler API freeze |
| P0-S02 | Logical packet API cannot express real fields and packet buffers overuse RAM | Compare typed/hybrid/byte codec with RFC vectors, memory and trace profiling | Packet API freeze |
| P0-S04 | Android UI unusable under real topology workload | Canvas vs View 10/50/100 nodes, touch hit test, frame/heap/GC on 4GB device | Android renderer selection |
| P0-R09 | Mixed GPL/proprietary code license | Release-tag/license/header review, dependency list and project licensing policy | Existing-code import |
| P1-S05 | Lost/corrupted lab at storage/API changes | Import v0/v1 fixtures, atomic saves, malformed inputs and disk-full | Public saved project format |
| P1-S06 | Android process death invalidates running session | Test foreground/background/kill/restore on actual phone | Run persistence |
| P1-S07 | Local-self ping reported as remote | Probe identity and expected-target trace assertions | Ping success claims |
| P1-S08 | Wrongly simplified RFC protocols | FSM state tables and tested subset with updated RFC list | Public protocol support |
| P1-S09 | Optional emulation API becomes security risk | Separate trust/memory/license review and mock capability negotiation | External adapter |
| P1-UX | UI warning wrongly bans legitimate WAN uplink | Port selection UX prototype with tests of intentional WAN | Auto-connect |
| P1-TRACE | Huge global packet trace exhausts memory | Indexed/segmented trace design, retention and backpressure experiment | Trace storage |
| P1-EDU | Assessment rewards only one IP layout rather than semantics | Scenario DSL semantics and alternative-correct-topology fixtures | Teaching/assessment |
| P1-IPV6 | IPv6 design extension becomes rewrite | Prove port/interface address family boundaries can support ND/ICMPv6 | Future compatibility |
| P1-ARCH | Contradiction between modules and specs | Reciprocal requirements -> ADR -> code -> tests graph reviewed | Gate A |

## Newly surfaced evidence and correction
Filius official v2.14.0 tag dated 2026-08-29 is active; old third-party accessible code shows thread-started protocol layers, **but that is not proof of current engine implementation**. Current GitLab source archive fetch was not possible during review. [Filius audit](research/FILIUS_REUSE_AUDIT.md) remains PARTIAL.
RFC 3927 requires probing and forbids routing packets with IPv4LL source/destination; address selection isn't a magic 169.254 assignment. RFC 2131 includes DHCP xid, retransmit, renewal, rebinding; [standards test fixtures](STANDARDS_TEST_VECTORS.md) must precede implementation.

## Execution discipline
Keep unresolved assumptions P0 and blocking. Spikes and small throwaway tests can be planned/executed but no full-feature production coding. Prioritize *smallest proof that could invalidate design*. Each completed item requires evidence links, date, owner, reproducible commands/test results and revision to [decision log](../architecture/DECISION_LOG.md). A completed doc only counts as DRAFT/REVIEWED, not measured evidence.
