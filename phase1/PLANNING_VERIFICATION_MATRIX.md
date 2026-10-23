# Phase 1 top-down/bottom-up design verification matrix
Status: PROPOSED V0.1 / no software tests run | 2026-10-23 | [master](PHASE1_MASTER_PLAN.md), [capability map](TOP_DOWN_CAPABILITY_MAP.md), [cross-layer gap register](CROSS_LAYER_GAPS.md).

## What is actually done versus what is still evidence debt
| Level | Requirement output / contract | Drafted document | Required independent closure |
|---|---|---|---|
| L0 Purpose | Product vision, roles, complete user journeys | [top-down map](TOP_DOWN_CAPABILITY_MAP.md) | User-role/task review and edge-case signoff |
| L1 Functional lab | Device authoring, simulate, inspect, assess | [device catalog](DEVICE_CAPABILITY_CATALOG.md) / [diagnostics](DIAGNOSTICS_AND_EDUCATION.md) | Screens, test tasks and alternate valid solutions |
| L2 Domain ontology | Stable typed IDs, ports, bridge domains, L3, service bindings | [device model](DEVICE_AND_INTERFACE_MODEL.md) | S03 independent model walkthrough and prototype |
| L3 Scheduler / time | Same-time FIFO, bounded queue, replay, commands | [event contract](EVENT_ENGINE_CONTRACT.md) | S01 proof, determinism + perf measured |
| L4 Transport/link/IP | Frame path, route, ARP, ICMP, UDP/DHCP | [network stack](NETWORK_STACK_DECOMPOSITION.md) / [protocol spec](PROTOCOL_BEHAVIOR_SPEC.md) | RFC versioned FSM/test vectors and oracle |
| L5 Observability | Event trace, completeness, selected target | [diagnostics](DIAGNOSTICS_AND_EDUCATION.md) | S07 attack fixtures and two-person agreement |
| L6 Data durability | Portable design, checkpoint, large trace, migration | [persistence](PERSISTENCE_AND_COMPATIBILITY.md) | S05/S06 Android storage+corruption proof |
| L7 Android UI | Touch canvas, configuration, CLI, inspector, accessible actions | [Android spec](ANDROID_EXPERIENCE_SPEC.md) | S04 constrained-device usability test |
| L8 Risk / security | Untrusted import, overload, licensing, recovery | [failure atlas](FAILURE_AND_SECURITY_ATLAS.md) / [cross-layer gaps](CROSS_LAYER_GAPS.md) | Threat review, fuzz corpus, explicit budget |
| L9 Teaching / assessment | Semantic rubrics, guided lab template, evidence-backed hints | [diagnostics](DIAGNOSTICS_AND_EDUCATION.md) | Independent valid-alternative score tests |
| L10 Build/release | APK, CI, profile versions, integrity/permissions | [roadmap](../architecture/IMPLEMENTATION_ROADMAP.md) | Reproducible CI, real phone, signed release process |
| L11 Reuse / portability | Independent engine vs Filius/other, licenses | [reuse audit](research/FILIUS_REUSE_AUDIT.md) | S10 full tagged code/legal review |

## Required reverse audit
Choose each domain object (link, port, bridge, L3 interface, route, packet, event, trace, project) and demonstrate: **why a user needs it → behavior owned → immutable/volatile state → schema field ownership → observable fault → standards/test oracle → persisted or not → UI presentation**. Missing arrow = plan gap, never just a to-do deferred to coding.

## Measurable exit evidence
- A protocol's support level and signature list must match executed test corpus.
- For every early user journey, there is at least one normal trace, one fault trace, and a no-false-success negative.
- For every persisted entity, import corruption and migration policy explicit.
- For every scheduled protocol timer, cancellation/actor invalidation and global queue ordering explicit.
- For every Android action, equivalent valid engine command and error semantics.
- For every P0 decision, alternatives, veto criteria, experiment results and ADR signoff.
- Two implementers independently derive congruent event/path sequences from contracts.

Status TODAY: **DRAFT ONLY**, no independently executed simulator/Android protocol/persistence evidence, no Gate A signoff. The knowledge-system CI ensures document navigation, not truthfulness of protocol semantics.
