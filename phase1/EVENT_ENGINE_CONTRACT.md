# Event engine and causal trace contract — specification v0.1
Status: PROPOSED / S01 and S07 UNTESTED | 2026-10-23. Parent: [Phase 1](PHASE1_MASTER_PLAN.md), [domain model](DEVICE_AND_INTERFACE_MODEL.md), [architecture](../architecture/ARCHITECTURE_BLUEPRINT.md).

## Model guarantees
Virtual time is a nonnegative integral tick quantity; `SimulationNow` increases monotonically. All event processing is controlled by ONE session owner; devices are modeled actors but not independent worker threads. Queue ordering is a total order: (scheduledTick, monotonically assigned insertionSeq). All inputs (commands and RNG seed) are part of reproducible trace. No UI filter, wall-time scheduling jitter, thread race or incidental map iteration changes semantic order.

### Message/event categories
- **ControlCommand**: user/CLI/scenario topology edits, configuration, run/step/pause/reset or injection. Has requestId, origin, expectedRevision, effective simulation tick, target ID and immutable command body.
- **InternalScheduledEvent**: link delivery, protocol timer expiry, state transition/dispatch, DHCP retransmit, MAC aging, run budget guard. Has eventId, eventGeneration (cancel/reuse safety), targetActor, time, insertion sequence, correlation and parents.
- **PacketIdentity**: one ingress/egress frame payload has lineage token and optional parentPacketId (broadcast fan-out branches have distinct transmission identities while sharing original probe correlation).
- **TraceFact**: append-only record of actual processed state transition, input packet/port, action/result, reason code, parent event and optional packet correlation.
- **ReadProjection**: indexed/filtered UI view of immutable trace facts and state summaries, may not schedule events or modify process.

### Deterministic command boundary and consistent edit semantics
At safe boundary after current atomic event, queued command with expected revision checks existing state and either commits a transaction with new revision or rejects. If engine is running, order input commands and assign effective tick (not Android receipt wall-clock). A `DisconnectLink` edit invalidates scheduled link deliveries via version tokens; policy regarding in-flight delivery must be chosen explicitly in S01 rather than guessed. Old timer belonging to an actor deleted/recreated with same display name cannot mutate new actor; IDs/generations govern validity.

### Scheduler kernel pseudosemantics
```text
schedule(target,t,kind,payload):
  if t < now or overflow(t) -> REJECT EVENT_TIME_INVALID
  if active_queue_size >= queue_budget -> PAUSE BUDGET_EXCEEDED
  issue sequence id monotonically; enqueue ordered by (t,seq)
processOne():
  process queued UI commands only at selected safe boundary
  if paused -> no event progression
  next = pop earliest valid non-cancelled event
  if none -> idle
  if next.tick < now -> invariant failure
  now = next.tick
  check same-tick budget, event lineage and current target generation
  transition = actor.handle(state, next.payload, seededRng)
  atomically apply resulting state, enqueue successor events,
    append actual trace with parent and reason, increment revision
  publish bounded snapshot deltas
```
Loop prevention is a resource policy independent of STP. Don't mask unimplemented STP by automatically removing network loops.

### Replay contract and unavoidable caveats
Same `LabDesign` + protocol/profile/engine versions + starting session snapshot/seed + **ordered user command log including accepted/rejected commands with exact effective virtual times** -> identical semantic trace. Wall timestamps, rendered animation frame count, or Android lifecycle times are excluded. Cross-version replay uses migration only when explicitly tested; otherwise refuse incompatible checkpoint and offer reset.
Randomness sources: one seeded deterministic generator per session or deterministically derived independent device streams (choose S01 after testing), never Android/clock/random UUID in runtime routing decisions.

### Event queue / cancellation tradeoffs
Min-heap vs tree vs calendar queue and lazy cancellation vs eager remove to be measured with realistic mixture of link delivery, DHCP timer, MAC-aging and background control events; ns-3 explicitly documents cancellations can retain scheduler memory. See https://www.nsnam.org/docs/manual/html/events.html . Put cap and compaction strategy in S01 results. Schedule same-tick generated events after already-scheduled equal-tick events if FIFO policy selected.

### Budget and failure behavior
Specific limits for active events, total event transitions, same-tick transitions, wall CPU slice per run request, trace ring/segment space, packet fan-out and maximum virtual time are **not chosen until phone benchmarks**. Limits are exposed per project policy, checked before allocating unbounded objects, with safe pause and reason; no silent truncation of important diagnostic outcome. Incomplete probe cannot report success.

### Trace fidelity contract
Every forwarding decision references a prior packet receive or local generation, exact ingress/egress and topology revision. Local delivery has no physical hop. Multi-copy broadcast frames have common parent lineage but separate transmission IDs and paths. Observability is designed into engine events; UI never derives the path by searching graph geometry.
Trace output: packetHeaderSummary, before/after state refs (or delta), event reason, actor, ingress, egress, virtualTime, queueSeq, parentEventId, correlationId, outcome (scheduled, dropped, delivered, ignored, local, unsupported). Retention/indexing policy separately measured; trace exports label missing segments.

### Proof experiment S01
- 100 identical replay seeds of 1k/10k events; mixed equal-tick insertion and fan-out.
- Catch wrong ordering after actor deletion or port unlink; no frame delivered to newly created different actor using reused display name.
- Cancel-vs-remove when many DHCP retransmit timers expire/cancel; measure retained queue and memory.
- Deliberately create switching loop without STP; bounded pause under storm, deterministic trace and explicit non-success.
- Validate smallest possible tick, near-maximum tick and overflow, zero-time recurrence and fair ability to pause.
- Run under JVM and Android-equivalent runtime; measure CPU/heap/GC and compare semantic trace hashes; no arbitrary performance claim until done.

**Note:** Proposed pseudosemantics only; implementation details remain unfrozen pending the S01 proof.
