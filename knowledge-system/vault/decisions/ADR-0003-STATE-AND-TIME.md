# ADR-0003 — Separate state planes and serialized virtual time
Status: PROPOSED_CONTRACT, pending S01/S03 | Date: 2026-10-23

## Context
Conflating visual state, durable design and ephemeral simulation allows fake events, non-reproducible state and data loss. Thread races and wall-clock timers destroy deterministic replay. Reference [blueprint](../../../architecture/ARCHITECTURE_BLUEPRINT.md) and [ns-3 event architecture](https://www.nsnam.org/docs/manual/html/events.html).

## Recommendation
Canonical versioned configuration; separate mutable session/runtime (scheduler, caches, FSM timers); independently derived UI state. All changes to simulation world serialized through one command owner. Event order (integer ticks, monotonic insertion sequence); engine-specific deterministic seeded pseudo-randomness; stable actor identity. UI can animate without clock affecting behavior. Immutable read projections and bounded trace segments.

## Rejected
Multiple independent CLI/UI state stores; wall clock as scheduler; re-running protocol logic independently in UI; unordered parallel event handling.

## Verify
S01 deterministic equal-time ordering/overflow/cancellation across JVM/Android; S03 topology mutation; same-action same-trace hash; process restore invariant. Exact integer unit and snapshot granularity intentionally open pending spike.
