# VirtualNetLab

**VirtualNetLab** is a proposed offline-first Android virtual networking laboratory: design, construct, configure, operate, simulate, inspect, troubleshoot, and learn networks without physical equipment.

> Status: **planning / repository bootstrap** — no Android application or networking engine has been implemented yet.

- [Phase 1 planning & design gate — ACTIVE](phase1/PHASE1_MASTER_PLAN.md)
- [Phase 1 exit audit — NOT COMPLETE](phase1/EXIT_AUDIT.md)
- [Filius engine reuse audit — partial](phase1/research/FILIUS_REUSE_AUDIT.md)
- [Device and interface topology contract](phase1/DEVICE_AND_INTERFACE_MODEL.md)
- [Virtual time and event trace contract](phase1/EVENT_ENGINE_CONTRACT.md)
- [Standards-indexed test vectors](phase1/STANDARDS_TEST_VECTORS.md)
- [Project vision](IDEA_PLAN.md)
- [Implementation roadmap](TECHNICAL_PLAN.md)
- [Architecture review and outstanding decision gates](architecture/ARCHITECTURE_REVIEW.md)
- [Architecture blueprint](architecture/ARCHITECTURE_BLUEPRINT.md)
- [Validation and implementation gates](architecture/VALIDATION_STRATEGY.md)
- [Knowledge & navigation](NAVIGATION.md)
- [Contribution rules](AGENTS.md)
- [Research and decisions](knowledge-system/vault/INDEX.md)

We use a deterministic virtual-network simulation engine as the baseline, with a future optional integration boundary for external emulation backends. We will not claim that an animated packet path is accurate without event-model tests.

This is an independent educational networking laboratory, not an official Cisco product. Do not add proprietary network operating system images, trademarked assets, or copied implementation code.

Research, architecture, milestones, accepted decisions and outstanding validation are documented in the repository.

## Top-down architecture planning
- [Full capability map](phase1/TOP_DOWN_CAPABILITY_MAP.md)
- [End-to-end stack execution and interface boundaries](phase1/NETWORK_STACK_DECOMPOSITION.md)
- [Composable device capability catalog](phase1/DEVICE_CAPABILITY_CATALOG.md)
- [Diagnostics, learning and assessment](phase1/DIAGNOSTICS_AND_EDUCATION.md)
- [Offline storage, versioning and failure recovery](phase1/PERSISTENCE_AND_COMPATIBILITY.md)
- [Cross-layer contradictions and gaps](phase1/CROSS_LAYER_GAPS.md)
- [Planning verification matrix](phase1/PLANNING_VERIFICATION_MATRIX.md)
- [Decision-critical planning queue](phase1/REVIEW_PRIORITY_QUEUE.md)

**Phase 1 status:** drafted contracts, NOT gate-approved; no network engine or Android app built yet.
