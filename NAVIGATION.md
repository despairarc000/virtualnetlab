# NAVIGATION — VirtualNetLab
Authoritative cold-start map. Open this file after [AGENTS.md](AGENTS.md). Document statuses: ACTIVE / PROPOSED / SUPERSEDED / REJECTED / HISTORICAL.

| Need | Read first | Then |
|---|---|---|
| Purpose, user goals, product constraints | [IDEA_PLAN.md](IDEA_PLAN.md) | [TECHNICAL_PLAN.md](TECHNICAL_PLAN.md) |
| Current state, branch, handoff | [CHECKPOINT.md](knowledge-system/vault/CHECKPOINT.md) | [WORKLOG.md](knowledge-system/vault/WORKLOG.md) |
| Implementation architecture | [TECHNICAL_PLAN.md](TECHNICAL_PLAN.md) | [ADR-0001](knowledge-system/vault/decisions/ADR-0001-ENGINE.md), [ADR-0002](knowledge-system/vault/decisions/ADR-0002-ANDROID.md) |
| Prior art and evidence | [NETWORK_SIMULATORS.md](knowledge-system/vault/research/NETWORK_SIMULATORS.md) | [EVIDENCE.md](knowledge-system/vault/EVIDENCE.md) |
| Protocol support and lab expectations | [PROTOCOL_MATRIX.md](knowledge-system/vault/specs/PROTOCOL_MATRIX.md) | [LAB_ACCEPTANCE.md](knowledge-system/vault/specs/LAB_ACCEPTANCE.md) |
| Context by task | [ICM.md](knowledge-system/icm/ICM.md) | `python tools/knowledge.py route <task>` |
| Source/dependency graph | [GRAPHIFY.md](knowledge-system/graphify/GRAPHIFY.md) | `python tools/knowledge.py graph` |
| Vault inventory | [INDEX.md](knowledge-system/vault/INDEX.md) | relevant node and its linked evidence |
| Contradictions/unknowns | [OPEN_QUESTIONS.md](knowledge-system/vault/OPEN_QUESTIONS.md) | [decisions](knowledge-system/vault/decisions/ADR-0001-ENGINE.md) |
| Validation and workflow | [AGENTS.md](AGENTS.md) | `python tools/knowledge.py doctor` |

## Cold-start protocol
1. Read AGENTS -> NAVIGATION -> CHECKPOINT and IDEA_PLAN.
2. Detect current branch/head; inspect changed files and ongoing contributor work.
3. Route task-specific context via ICM; read only relevant vault records and direct graph neighbors.
4. Identify known behavior vs proposed behavior, tests/evidence and conflicts. Document the smallest falsifiable implementation step.
5. Implement and run tests; update traceability docs, Graphify and checkpoint; never claim evidence from unrun tests.

## Important
All MD pages are navigation and persisted knowledge, not a replacement for executable tests. Graph edges are built from explicit links/source imports, not AI guesses. ICM routing is deterministic and searchable; it does not rely on remembered chat context. Main captures implementation-neutral user goals. Branches may hold implementation-specific provisional findings.
