# Agent operating contract — VirtualNetLab
Read [NAVIGATION.md](NAVIGATION.md) and [IDEA_PLAN.md](IDEA_PLAN.md) first. This contract applies repository-wide; nested AGENTS.md may narrow only local processes, not product intent.

## Mission and authority
Product intent: IDEA_PLAN.md. Technical baseline: TECHNICAL_PLAN.md and Accepted ADRs. Reality: reproducible source/test evidence and CHECKPOINT.md. A contradictory claim must be investigated, not silently reconciled.
Do NOT narrow this project into a diagram editor, fabricated animation, or single-protocol teaching demo. It is a real Android virtual networking laboratory with verifiable behavior.

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
