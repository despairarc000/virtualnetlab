# ADR-0006 — Portable lab, runtime checkpoint and trace are distinct
Status: PROPOSED_CONTRACT, pending S05/S06 | Date: 2026-10-23

## Context
Human-editable network designs are small relative to packet event logs. Android process death can occur even when user did not explicitly save. Importing user-supplied laboratories is an untrusted-data boundary.

## Recommendation
Design/configuration saved in schema-versioned portable format; optional runtime snapshots and segmented traces stored separately with matched engine/model version and integrity metadata. JSON+Kotlin Serialization is a candidate export format; Room is an Android project-index option. Exact archive format deliberately not frozen until S05. Strict parsing, semantic invariants, bounded nesting and size, no code execution from scenarios. Atomic autosave and explicit fail-safe recovery. Android offscreen run defaults to pause/snapshot rather than unrestricted background service.

## Rejected
Unversioned opaque save with embedded full trace; blind JSON leniency; indefinite unbounded trace in RAM; privileged storage access for core export; silently resuming incompatible engine snapshots.

## Verify
Open/save after process death, malformed schema corpus, schema v0-to-v1 migration, 100k-event trace workload, partial write, repeated import, backwards/forwards compatibility policy. [Android offline-first](https://developer.android.com/topic/architecture/data-layer/offline-first) and [SAF](https://developer.android.com/guide/topics/providers/document-provider).
