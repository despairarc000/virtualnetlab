# Phase 1 — Engineering definition, research and architecture closure
Status: ACTIVE planning mandate; not a sign-off | 2026-10-23 | Product authority: [IDEA_PLAN](../IDEA_PLAN.md). Next phases: [roadmap](../architecture/IMPLEMENTATION_ROADMAP.md).

## What the user means by Phase 1
**Plan down to implementation-ready detail to avoid spending months coding into an architectural dead end.** Phase 1 encompasses repository/knowledge-system setup (old Stage 0), thorough requirements/architecture research, formal design, risk discovery, peer review, proof-of-feasibility *disposable* spikes (old G0), and handoff packets. Phase 2 starts only after the architecture gate is signed off. Subsequent G1–G7 labels in the technical roadmap represent implementation milestones, not new definitions of Phase 1.

### Hard boundary
- ALLOWED: specifications, RFC analysis, architecture comparisons, mock contracts, wireframes, test vectors, source licensing audits, deterministic simulation equations, executable tests **of prototypes**, temporary proof-of-concept code with recorded results, benchmarking.
- NOT ALLOWED as Phase 1 completion evidence: polished but untested UI, presumed Android performance, a demo animating packets, an unreviewed production library/API, silently imported GPL/proprietary source, fabricated compatibility.
- Production Kotlin feature code is Phase 2 work. A targeted throwaway spike is not a production deliverable; delete/isolate experimental branches unless the spike independently passes the later production gates.
- Do not aim to pre-specify every future protocol bit. Lock the **architecture and extension methodology**; define near-term protocols to field/state/exception/test detail. Later protocols require the same per-protocol design gate before implementation.

## Outcome: a buildable and falsifiable plan
Every feature or subsystem must have (1) scope/non-goals, (2) authoritative inputs & standard version, (3) owning component, (4) state and data contracts, (5) behavior transitions, (6) positive & negative cases, (7) failure and recovery behavior, (8) resource and security constraints, (9) evidence and test oracle, (10) dependencies and implementable work packets.

## Deliverable hierarchy
1. **Purpose and personas:** [vision](../IDEA_PLAN.md); students, self-directed learners, instructors, experimenters and power users. Avoid feature-only planning without user workflows.
2. **Technical alternatives:** [source research](../architecture/SOURCE_EVALUATION.md); build-vs-reuse Filius, ns-3/INET comparison, cost/license analysis. Avoid automatic sunk-cost dependence.
3. **Whole-system architecture:** [blueprint](../architecture/ARCHITECTURE_BLUEPRINT.md), [system boundaries](SYSTEM_CONTRACTS.md), [architecture review](../architecture/ARCHITECTURE_REVIEW.md).
4. **Per-protocol conformance and test taxonomy:** [protocol plan](PROTOCOL_BEHAVIOR_SPEC.md), [current matrix](../knowledge-system/vault/specs/PROTOCOL_MATRIX.md), [scenario acceptance](../knowledge-system/vault/specs/LAB_ACCEPTANCE.md).
5. **Android product mechanics:** [UX, persistence and platform contract](ANDROID_EXPERIENCE_SPEC.md), user journey, import/export, recoverability, accessibility, memory/power constraints.
6. **Failure and adversarial design:** [failure atlas](FAILURE_AND_SECURITY_ATLAS.md), [risk register](../architecture/RISK_REGISTER.md), [validation](../architecture/VALIDATION_STRATEGY.md).
7. **Decisions:** [decision gates](DECISION_GATES.md), [spikes](../architecture/SPIKES_AND_DECISION_GATES.md), [architecture ADRs](../architecture/DECISION_LOG.md).
8. **Execution handoff:** [work packets](WORK_BREAKDOWN.md), [traceability](../architecture/REQUIREMENTS_TRACEABILITY.md), [checkpoint](../knowledge-system/vault/CHECKPOINT.md).
9. **Audit:** [coverage and exit gate](EXIT_AUDIT.md), all P0 findings and design contradictions resolved.

## Ordered Phase 1 work, no skipped gates
**P1.01 Vision and coverage:** map every desired workflow to outcomes and supported-scope phases; identify feature boundaries and exclusions, owner product.
**P1.02 Prior art/feasibility:** inspect primary implementations/standards, license BOM, Filius engine dependency audit, and record make-vs-reuse decision, owner architecture.
**P1.03 Invariants and domain schema:** physical/link/logical identity, configuration/runtime/presentation state, device composition, validation; owner engine/domain.
**P1.04 Virtual-time model:** event ordering, command timing, timeout/seed, message cancellation, queue/trace limits, pause/resume; owner scheduler.
**P1.05 Packet+protocol method:** semantic fields vs byte codec contract, protocol FSMs, supported subset, standards, inference vs normative; owner protocol.
**P1.06 Path & diagnostics:** forwarding, packet identity, provenance, target identity, reason taxonomy, snapshots; owner diagnostics.
**P1.07 Android product:** touch topology, accessibility, layout, CLI, timeline, inspector, offline project, lifecycle, security boundaries; owner Android.
**P1.08 Persistence/export:** project schema, version/migration, transaction, malicious import limits, replay equivalence; owner persistence.
**P1.09 Validation design:** every requirement maps to fixture/assertion/oracle and negative test; owner QA.
**P1.10 Performance & resources:** define test hardware, 10/50/100 node + event workloads, engine/UI metrics, resource ceilings chosen based on measurements; owner performance.
**P1.11 Experimental spikes:** execute S01–S10, retain logs, record rejected choices and measurable tradeoffs; owner architecture.
**P1.12 Implementation work packets:** exact module responsibilities, dependencies, entry/exit criteria, independent test artifacts, branch scope, owner lead.
**P1.13 Cross-discipline adversarial review:** networking correctness, Android/UX/accessibility, data/security/licensing, state consistency, failure modes; owner reviewers.
**P1.14 Gate A sign-off:** no unaddressed P0; accepted ADR updates; traceable requirements; evidence-backed decisions; explicit deferred features; owner project lead.

## Quality gate: NOT ready until ALL conditions meet
- Every P0 decision has accepted ADR backed by required tests or a consciously bounded, reversible assumption. No unknown P0 dependency can silently pass.
- Bidirectional traceability for Stage 1–4 deliverables: requirement -> model contract -> fixture -> owner and reverse.
- Device model, link/bridge/L3 separation, time/event representation, command model, trace identity, replay model and error semantics precise enough that **two implementers can independently describe the same observable behavior**.
- S01–S04 and S10 disposition with actual evidence; Android device/emulator feasibility and licensing decisions supported.
- Protocol models near-term reference specific standards/sections, including state-machine failures and fidelity exclusions.
- Security/privacy, accessibility, import corruption, background lifecycle, storage migration, resource overload, plugin boundaries documented.
- CI validates navigation/vault and test fixtures; review checks claims against existing code, no fake support.
- Every implementation packet has prerequisites, work estimate class/size (without fictional timetable), acceptance tests, rollback plan.
- Gate sign-off record cites version, branch, commit SHA, checked tests, outstanding risks, reviewer decisions. Only then Phase 2.

## Realistic limitation
This phase drastically reduces rework, but cannot promise **zero** implementation surprises, perfect performance predictions or total networking protocol parity. When a risk cannot be settled on paper, build the smallest reversible *experiment*, measure, document and either commit an ADR or stop implementation.

## Next action
Complete and review [system contracts](SYSTEM_CONTRACTS.md), [protocol behavior](PROTOCOL_BEHAVIOR_SPEC.md) and [device Android contract](ANDROID_EXPERIENCE_SPEC.md); execute [decision spikes](DECISION_GATES.md) before authorizing production network engine.
