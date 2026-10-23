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
