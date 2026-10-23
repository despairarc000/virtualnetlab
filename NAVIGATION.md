# NAVIGATION — VirtualNetLab
Authoritative cold-start map. Open this file after [AGENTS.md](AGENTS.md). Document statuses: ACTIVE / PROPOSED / SUPERSEDED / REJECTED / HISTORICAL.

| Need | Read first | Then |
|---|---|---|
| Purpose, user goals, product constraints | [IDEA_PLAN.md](IDEA_PLAN.md) | [TECHNICAL_PLAN.md](TECHNICAL_PLAN.md) |
| Current state, branch, handoff | [CHECKPOINT.md](knowledge-system/vault/CHECKPOINT.md) | [WORKLOG.md](knowledge-system/vault/WORKLOG.md) |
| **Phase 1: planning and design** | [PHASE1_MASTER_PLAN.md](phase1/PHASE1_MASTER_PLAN.md) | [SYSTEM_CONTRACTS.md](phase1/SYSTEM_CONTRACTS.md), [EXIT_AUDIT.md](phase1/EXIT_AUDIT.md) |
| **Phase 1: protocol and Android detail** | [PROTOCOL_BEHAVIOR_SPEC.md](phase1/PROTOCOL_BEHAVIOR_SPEC.md) | [ANDROID_EXPERIENCE_SPEC.md](phase1/ANDROID_EXPERIENCE_SPEC.md), [FAILURE_AND_SECURITY_ATLAS.md](phase1/FAILURE_AND_SECURITY_ATLAS.md) |
| **Phase 1: decisions and work packets** | [DECISION_GATES.md](phase1/DECISION_GATES.md) | [WORK_BREAKDOWN.md](phase1/WORK_BREAKDOWN.md) |
| **Phase 1: build versus adapt** | [FILIUS_REUSE_AUDIT.md](phase1/research/FILIUS_REUSE_AUDIT.md) | [REVIEW_OPEN_ITEMS.md](phase1/REVIEW_OPEN_ITEMS.md) |
| **Phase 1: physical and logical topology** | [DEVICE_AND_INTERFACE_MODEL.md](phase1/DEVICE_AND_INTERFACE_MODEL.md) | [SYSTEM_CONTRACTS.md](phase1/SYSTEM_CONTRACTS.md) |
| **Phase 1: engine time / traces** | [EVENT_ENGINE_CONTRACT.md](phase1/EVENT_ENGINE_CONTRACT.md) | [STANDARDS_TEST_VECTORS.md](phase1/STANDARDS_TEST_VECTORS.md) |
| Detailed architecture review | [ARCHITECTURE_REVIEW.md](architecture/ARCHITECTURE_REVIEW.md) | [ARCHITECTURE_BLUEPRINT.md](architecture/ARCHITECTURE_BLUEPRINT.md), [decisions](architecture/DECISION_LOG.md) |
| Architecture alternatives / sources | [SOURCE_EVALUATION.md](architecture/SOURCE_EVALUATION.md) | [EVIDENCE.md](knowledge-system/vault/EVIDENCE.md) |
| Risks / validation / implementation gates | [RISK_REGISTER.md](architecture/RISK_REGISTER.md) | [SPIKES_AND_DECISION_GATES.md](architecture/SPIKES_AND_DECISION_GATES.md), [IMPLEMENTATION_ROADMAP.md](architecture/IMPLEMENTATION_ROADMAP.md), [VALIDATION_STRATEGY.md](architecture/VALIDATION_STRATEGY.md) |
| Requirement-to-test traceability | [REQUIREMENTS_TRACEABILITY.md](architecture/REQUIREMENTS_TRACEABILITY.md) | [LAB_ACCEPTANCE.md](knowledge-system/vault/specs/LAB_ACCEPTANCE.md) |
| Implementation architecture | [TECHNICAL_PLAN.md](TECHNICAL_PLAN.md) | [ADR-0001](knowledge-system/vault/decisions/ADR-0001-ENGINE.md), [ADR-0002](knowledge-system/vault/decisions/ADR-0002-ANDROID.md) |
| Prior art and evidence | [NETWORK_SIMULATORS.md](knowledge-system/vault/research/NETWORK_SIMULATORS.md) | [EVIDENCE.md](knowledge-system/vault/EVIDENCE.md) |
| Protocol support and lab expectations | [PROTOCOL_MATRIX.md](knowledge-system/vault/specs/PROTOCOL_MATRIX.md) | [LAB_ACCEPTANCE.md](knowledge-system/vault/specs/LAB_ACCEPTANCE.md) |
| Context by task | [ICM.md](knowledge-system/icm/ICM.md) | `python tools/knowledge.py route <task>` |
| Source/dependency graph | [GRAPHIFY.md](knowledge-system/graphify/GRAPHIFY.md) | `python tools/knowledge.py graph` |
| Vault inventory | [INDEX.md](knowledge-system/vault/INDEX.md) | relevant node and its linked evidence |
| Contradictions/unknowns | [OPEN_QUESTIONS.md](knowledge-system/vault/OPEN_QUESTIONS.md) | [decisions](knowledge-system/vault/decisions/ADR-0001-ENGINE.md) |
| Validation and workflow | [AGENTS.md](AGENTS.md) | `python tools/knowledge.py doctor` |

## Cold-start protocol
1. Read AGENTS -> NAVIGATION -> CHECKPOINT and IDEA_PLAN; if planning/design/architecture, read [Phase 1 master](phase1/PHASE1_MASTER_PLAN.md) and its exit audit.
2. Detect current branch/head; inspect changed files and ongoing contributor work.
3. Route task-specific context via ICM; for architecture or implementation decisions check [Gate A](architecture/SPIKES_AND_DECISION_GATES.md) and unresolved [risks](architecture/RISK_REGISTER.md); read only relevant vault records and direct graph neighbors.
4. Identify known behavior vs proposed behavior, tests/evidence and conflicts. Document the smallest falsifiable implementation step.
5. Implement and run tests; update traceability docs, Graphify and checkpoint; never claim evidence from unrun tests.

## Important
All MD pages are navigation and persisted knowledge, not a replacement for executable tests. Graph edges are built from explicit links/source imports, not AI guesses. ICM routing is deterministic and searchable; it does not rely on remembered chat context. Main captures implementation-neutral user goals. Branches may hold implementation-specific provisional findings.
