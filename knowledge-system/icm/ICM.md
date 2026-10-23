# ICM — Intelligent Context Management
Status: ACTIVE navigation protocol | 2026-10-23. ICM is deterministic **task-to-document routing**, not a vague claim that the AI memorizes the repo.

## How it works
Root [NAVIGATION.md](../../NAVIGATION.md) is the bootstrap. Run `python tools/knowledge.py route <task text>` to score task keywords against maintained route rules, expand to required documents and first-hop linked dependencies, and display only contextual paths. Always read root contract, project vision, plan and checkpoint. If task is ambiguous, print multiple relevant routes and unresolved context rather than guessing.

## Routes
- **engine / scheduler / replay / deterministic** -> TECHNICAL_PLAN, ADR-0001, LAB_ACCEPTANCE, PROTOCOL_MATRIX.
- **network / protocol / dhcp / arp / icmp / router / switch / vlan / stp / dtp** -> PROTOCOL_MATRIX, LAB_ACCEPTANCE, TECHNICAL_PLAN, EVIDENCE.
- **android / ux / compose / ui / canvas / apk** -> ADR-0002, TECHNICAL_PLAN, IDEA_PLAN, OPEN_QUESTIONS.
- **research / comparison / emulation / ns3 / gns3** -> NETWORK_SIMULATORS, EVIDENCE, ADR-0001.
- **knowledge / navigation / graph / icm / vault / documentation** -> NAVIGATION, vault INDEX, GRAPHIFY, this file.
- **handoff / status / continue** -> CHECKPOINT, WORKLOG, OPEN_QUESTIONS.

## Update contract
When a file moves, update ICM route map and Markdown links, run doctor. When source files are added, Graphify discovers Python imports and Markdown links, but semantic requirements/test links must be manually explicit. Route output is context recommendation, not implementation authorization.

## Architecture review route
- **architecture / design / tradeoffs / risk / scalability / decision / validation** -> [review](../../architecture/ARCHITECTURE_REVIEW.md), [blueprint](../../architecture/ARCHITECTURE_BLUEPRINT.md), [decision log](../../architecture/DECISION_LOG.md), [risks](../../architecture/RISK_REGISTER.md), [spikes](../../architecture/SPIKES_AND_DECISION_GATES.md), [roadmap](../../architecture/IMPLEMENTATION_ROADMAP.md).
This route must appear in tools/knowledge.py and its tests.

## Phase 1 required context (user sequencing rule)
- **phase1 / planning / spec / specification / readiness / signoff / freeze / before coding / risk-reduction** -> [master](../../phase1/PHASE1_MASTER_PLAN.md), [system](../../phase1/SYSTEM_CONTRACTS.md), [protocol](../../phase1/PROTOCOL_BEHAVIOR_SPEC.md), [Android](../../phase1/ANDROID_EXPERIENCE_SPEC.md), [decisions](../../phase1/DECISION_GATES.md), [exit audit](../../phase1/EXIT_AUDIT.md).
- Before any implementation recommendation, verify Phase 1 [EXIT_AUDIT](../../phase1/EXIT_AUDIT.md). Code Mode agents must not treat DRAFT plans as accepted API specifications.
