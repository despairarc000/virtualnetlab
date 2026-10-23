# ADR-0002: Native Android presentation and independently testable Kotlin core
Status: ACCEPTED planning baseline | Date: 2026-10-23.

## Context
Phone-first app, touch topology, offline persistence, scalable UI, reproducible simulation and need to test engine without Android display lifecycle. See [IDEA_PLAN](../../../IDEA_PLAN.md), [TECHNICAL_PLAN](../../../TECHNICAL_PLAN.md).

## Decision
Use Kotlin core modules with no Android framework dependency and JVM unit tests; Android shell in Kotlin + Jetpack Compose. Model + scheduler updates are serialized in an engine owner, UI observes immutable/snapshot state. Deliver APK via reproducible Gradle/GitHub Actions build once source exists; real device tests remain mandatory.

## Alternatives
Compose Multiplatform, Flutter or embedded web frontend may be revisited with measured touch-UX, memory and build data. No need to commit to KMP cross-platform targets yet.

## Risks
Memory/canvas performance, Android API level, background lifecycle and trace cardinality; all need measured acceptance before release. Don't promise any working APK from documentation alone.
