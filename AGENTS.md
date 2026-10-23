# Agent operating contract — VirtualNetLab
Read [NAVIGATION.md](NAVIGATION.md) and [IDEA_PLAN.md](IDEA_PLAN.md) first. This contract applies repository-wide; nested AGENTS.md may narrow only local processes, not product intent.

## Mission and authority
Product intent: IDEA_PLAN.md. Technical baseline: TECHNICAL_PLAN.md and Accepted ADRs. Reality: reproducible source/test evidence and CHECKPOINT.md. A contradictory claim must be investigated, not silently reconciled.
Do NOT narrow this project into a diagram editor, fabricated animation, or single-protocol teaching demo. It is a real Android virtual networking laboratory with verifiable behavior.

## Phase 1 planning lock (2026-10-23)
[Phase 1 master plan](phase1/PHASE1_MASTER_PLAN.md) defines comprehensive planning down to implementable contracts; [Phase 1 exit audit](phase1/EXIT_AUDIT.md) currently blocks production engine and app feature coding. Do not mistake CI of Markdown tooling for architecture sign-off. Small throwaway proof-of-feasibility experiments are allowed to falsify high-risk hypotheses; log measurement, source/target hardware, negative cases, licensing and decision. Full production code requires Gate A acceptance and no unaddressed P0 questions. Model the long-term scope without prematurely implementing unvalidated breadth.

## Architecture source and proof requirements
Read [the Filius reuse audit](phase1/research/FILIUS_REUSE_AUDIT.md) before reusing any legacy engine. Current source-level verdict is **PARTIAL**, NOT approved; older third-party source does NOT establish current Filius v2.14 behavior. Consult [device/port model](phase1/DEVICE_AND_INTERFACE_MODEL.md), [event trace contract](phase1/EVENT_ENGINE_CONTRACT.md), and [standards test vectors](phase1/STANDARDS_TEST_VECTORS.md) before engine work. Do not claim a review is complete until the current tagged source has been inspected and planned packet fixtures actually executed. See [open items](phase1/REVIEW_OPEN_ITEMS.md).

## Every task
- Inspect branch/status and likely concurrent work. Avoid duplicating, overwriting or rebasing another worker's branch.
- Load routed context via `python tools/knowledge.py route <task>`; follow direct graph dependencies and evidence.
- For engine/API/storage/canvas decisions, check [Architecture Review](architecture/ARCHITECTURE_REVIEW.md), [Gate A spikes](architecture/SPIKES_AND_DECISION_GATES.md), [Risks](architecture/RISK_REGISTER.md) and [Decision Log](architecture/DECISION_LOG.md) before freezing contracts.
- State acceptance/negative cases *before* implementation. Keep independent facts, hypotheses, planned code, tested behavior, and unsupported features distinct.
- Make small auditable changes; use implementations with stable IDs, strict validation and reason-coded failures.
- Build tests for success, failure, replay, malformed input, topology ambiguity and cross-layer consistency.
- Update vault evidence, provenance, decisions, Graphify links, worklog and checkpoint as appropriate; run doctor and unit tests, log what actually ran.
- If unable to verify on a device/emulator, label **UNVERIFIED**. Never pretend an APK or test pass exists.
- Preserve engine/UI separation; no UI animation without an underlying event.

## Working conventions
- Branch-specific code and experimental technical approaches: `implementation/<topic>`. Shared stable goals, navigation and agreed knowledge: `main`.
- Status labels: ACTIVE (adopted), PROPOSED (unverified recommendation), SUPERSEDED, REJECTED, HISTORICAL.
- Documentation must link to sources and trace to explicit requirement, decision, code location, and test where possible.
- No unlicensed Cisco assets, IOS images, proprietary code, extracted firmware, or unsubstantiated .pkt compatibility.
- No secrets, user data or third-party APK binaries in repo.
- Do not mark protocol support complete without exact input/output/trace assertions and independent regression.
- Prefer offline-first functionality; do not introduce cloud authentication as a default dependency.
- Don't invent hardware limits, Android benchmark numbers, packet timings or protocol fidelity.
- If task is blocked, preserve a specific next action and evidence in OPEN_QUESTIONS and WORKLOG.

## Required commands
`python tools/knowledge.py route engine`
`python tools/knowledge.py graph`
`python tools/knowledge.py doctor`
`python -m unittest discover -s tests`
When generated dependency output is introduced, regenerate and compare as part of CI.

## Top-down and bottom-up architecture rule
Before implementing a new device, network protocol, UI operation, CLI command, save format or scenario, trace the user-facing requirement through [TOP_DOWN_CAPABILITY_MAP](phase1/TOP_DOWN_CAPABILITY_MAP.md) -> [NETWORK_STACK_DECOMPOSITION](phase1/NETWORK_STACK_DECOMPOSITION.md) -> [DEVICE_CAPABILITY_CATALOG](phase1/DEVICE_CAPABILITY_CATALOG.md) -> [DIAGNOSTICS_AND_EDUCATION](phase1/DIAGNOSTICS_AND_EDUCATION.md) -> [PERSISTENCE_AND_COMPATIBILITY](phase1/PERSISTENCE_AND_COMPATIBILITY.md). Check [CROSS_LAYER_GAPS](phase1/CROSS_LAYER_GAPS.md), [PLANNING_VERIFICATION_MATRIX](phase1/PLANNING_VERIFICATION_MATRIX.md) and [EXIT_AUDIT](phase1/EXIT_AUDIT.md). No implicit magic shortcuts across layers or false claims of measured conformance.
