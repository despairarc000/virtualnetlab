# Vault index
A curated, provenance-aware Markdown knowledge base. Use [navigation](../../NAVIGATION.md) or [ICM routes](../icm/ICM.md) to load the smallest relevant context.

- [CHECKPOINT.md](CHECKPOINT.md) — last verified state, next actions, unverified components.
- [EVIDENCE.md](EVIDENCE.md) — source catalog and assertion provenance.
- [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md) — unresolved decisions and experiment proposals.
- [WORKLOG.md](WORKLOG.md) — handoff and chronological progress.
- [NETWORK_SIMULATORS.md](research/NETWORK_SIMULATORS.md) — researched comparable systems and tradeoffs.
- [ADR-0001-ENGINE.md](decisions/ADR-0001-ENGINE.md) — why a deterministic simulator first.
- [ADR-0002-ANDROID.md](decisions/ADR-0002-ANDROID.md) — native Android and shared core boundary.
- [PROTOCOL_MATRIX.md](specs/PROTOCOL_MATRIX.md) — planned fidelity and honest support statuses.
- [LAB_ACCEPTANCE.md](specs/LAB_ACCEPTANCE.md) — acceptance scenarios and adversarial behavior.

Entry standards: heading, date, status, claim/fact vs inference, evidence links, dependencies, result/next check. Historical notes are preserved and annotated rather than silently rewritten.

## Architecture review package
- [architecture audit](../../architecture/ARCHITECTURE_REVIEW.md)
- [architecture blueprint](../../architecture/ARCHITECTURE_BLUEPRINT.md)
- [source and license evaluation](../../architecture/SOURCE_EVALUATION.md)
- [requirements traceability](../../architecture/REQUIREMENTS_TRACEABILITY.md)
- [validation strategy](../../architecture/VALIDATION_STRATEGY.md)
- [risk register](../../architecture/RISK_REGISTER.md)
- [spikes and decision gates](../../architecture/SPIKES_AND_DECISION_GATES.md)
- [execution roadmap](../../architecture/IMPLEMENTATION_ROADMAP.md)
- [decision register](../../architecture/DECISION_LOG.md)

## New architecture ADRs (proposed, pending spikes)
- [ADR-0003 state and time](decisions/ADR-0003-STATE-AND-TIME.md)
- [ADR-0004 packet and fidelity](decisions/ADR-0004-PACKET-AND-FIDELITY.md)
- [ADR-0005 ports and identity](decisions/ADR-0005-PORTS-AND-IDENTITY.md)
- [ADR-0006 persistence and lifecycle](decisions/ADR-0006-PERSISTENCE-AND-LIFECYCLE.md)
- [ADR-0007 extensions and security](decisions/ADR-0007-EXTENSIONS-AND-SECURITY.md)

## Phase 1 — detailed planning (current)
- [Phase 1 master](../../phase1/PHASE1_MASTER_PLAN.md)
- [System contracts](../../phase1/SYSTEM_CONTRACTS.md)
- [Protocol behavior](../../phase1/PROTOCOL_BEHAVIOR_SPEC.md)
- [Android experience contract](../../phase1/ANDROID_EXPERIENCE_SPEC.md)
- [Failure and security atlas](../../phase1/FAILURE_AND_SECURITY_ATLAS.md)
- [Decision gates](../../phase1/DECISION_GATES.md)
- [Work packets](../../phase1/WORK_BREAKDOWN.md)
- [Vocabulary and decision rules](../../phase1/GLOSSARY_AND_DECISION_RULES.md)
- [Exit audit: not approved](../../phase1/EXIT_AUDIT.md)

## P0 architecture detail / Phase 1 continuing
- [Source-level Filius candidate audit](../../phase1/research/FILIUS_REUSE_AUDIT.md) — partial, no approved reuse
- [Physical/logical ports, bridge and WAN/LAN](../../phase1/DEVICE_AND_INTERFACE_MODEL.md)
- [Virtual time, events, trace identity and replay](../../phase1/EVENT_ENGINE_CONTRACT.md)
- [Network standards test vectors](../../phase1/STANDARDS_TEST_VECTORS.md)
- [Priority unresolved evidence](../../phase1/REVIEW_OPEN_ITEMS.md)
