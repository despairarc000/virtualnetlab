# Offline lab persistence, compatibility and recovery plan
Status: PROPOSED; archive format/storage engine NOT selected | 2026-10-23 | [master](PHASE1_MASTER_PLAN.md), [Android](ANDROID_EXPERIENCE_SPEC.md), [state](SYSTEM_CONTRACTS.md).

## Three distinct assets with different guarantees
1. **Portable LabDesign (durable)**: topology, per-device profile/version, typed config and presentation layout, scenario constraints, optional seed; small enough to share. Must not include runtime secret/untrusted code.
2. **SimulationSession checkpoint (optional)**: clock, ordered pending event queue, actor FSM states and timers, MAC/ARP/DHCP caches/leases, effective configuration/engine/protocol versions, RNG state and state revision. Only resumable if *all* compatibility and integrity checks succeed.
3. **Trace archive (optional/large)**: immutable chronological event segments with run ID, actor and packet lineage, model versions, completeness boundary, indexes, size budgets and retention policy. Missing/truncated sections flagged.

Saved design and saved runtime are not interchangeable. A project can reopen with design intact even if replay must restart because its old checkpoint is incompatible.

## Storage entities / key contracts (candidate)
```text
ProjectCatalog(projectId, revision, title, lastOpened, schemaVersion, pathRef, healthStatus)
LabDesign(schemaVersion, projectId, revision, deviceProfiles{}, topology{}, config{}, layout{}, scenario?)
RunManifest(runId, designRevision, engineVersion, profileVersions, seed, commandLogRef, checkpointRef?, traceRefs[], completeness)
SessionSnapshot(runId, nowTicks, queueOrdered[], stateActor[], rngState, configRevision, snapshotVersion, hash)
TraceSegment(runId, rangeStart, rangeEnd, index, compressionVersion?, hash, complete)
```
Portable format JSON (with explicit migration) is a candidate, not final; large traces may warrant binary segments. Room is possible for catalog/query and local transactional metadata. Kotlin serialization is plausible for typed model. Make human-readable export and deterministic semantic replay separate requirements.

## Version policy before implementation
- Track `LabSchemaVersion`, `DeviceProfileVersion`, `EngineSemanticVersion`, `ProtocolModelVersion`, `ScenarioSchemaVersion` independently.
- A minor visual layout change cannot be allowed to retroactively alter device protocol semantics.
- Unknown future schema: safe read-only preview only if semantics can be interpreted without guesswork; otherwise refuse with upgrade request. Never silently drop unknown service settings.
- Migrations must be pure, versioned and tested with before/after semantic assertions; publish upgrade provenance and preserve original on failure.
- Checkpoint replay requires compatible engine and model versions, verified hashes and RNG/queue state. If not, let user restart from LabDesign and show explicit lost runtime status.
- Saved run traces label completeness and retention. Exported trace cannot pretend to include events that were dropped by retention policy.

## Atomic save/recovery lifecycle
1. Validate command mutation into canonical design revision.
2. On autosave, serialize to temporary validated file (or transaction), checksum, commit/atomic replace with prior known-good backup and catalog update; exact fsync/rename semantics verified per Android storage API.
3. On crash/disk-full, last committed LabDesign remains. Incomplete temp/snapshot flagged, never loaded as authoritative.
4. Background default: request safe engine pause; save design always, runtime checkpoint only when complete/compatible. Android may kill process before save finishes, so keep revisions incrementally durable rather than assuming onPause completes.
5. Rotation/split screen updates presentation state without creating a second engine.
6. Export via Android document picker; files may be large, so stream/limit and never hold unbounded trace in memory.

## Import pipeline as untrusted data
Read stream under byte/CPU/depth limit -> identify format/version -> parse structural schema -> validate references/IDs/count/ranges/IP prefixes/ports/capabilities -> run semantic migrations -> recompute indexes and integrity -> preview changes -> transactional install. No scripts, dynamic bytecode/plugins or shell commands on import. If archive-based, reject absolute paths, traversal, symlinks if unsupported, nested archive/decompression bomb and duplicate conflicting member names. Maintain a fuzz/negative corpus including missing fields, duplicate IDs, malformed enum and impossible topology. Import failure must leave existing lab unchanged.

## Branches, undo and edit/run lifecycle
- Distinguish project editing undo from a simulation-time reversal. Undo config uses inverse validated commands or versioned design restoration; an old runtime snapshot is invalidated when configuration no longer matches.
- Replaying a run from baseline plus deterministic commands is primary method of time travel. Heavy full-state per-event snapshots should be deferred until memory measurements.
- Copy lab = new projectId with fresh device identity namespace or explicitly retained internal stable IDs scoped by new project; never allow cross-project references.
- Sharing a scenario containing student response/trace must be privacy-aware; default export of design only, optional trace after explicit selection.

## Tests and forced failure cases
Round-trip export/import of LAN/WAN topology retains port IDs and DHCP binding; malformed project rejected before allocation explosion; v0->v1 schema migration; unknown profile does not quietly act as working host; crash between temp write/catalog update; out-of-disk/no permission; checkpoint from different engine semantic version; huge 100k-event trace; duplicate projectId collision; missing trace segment; modified config invalidates replay; session copied without command log cannot claim reproducibility.

## Open Gate S05/S06
Storage format and container choice, integrity algorithm, data migration model, committed autosave frequency, trace index compression, persisted queue representation and Android API version. Performance and correctness experiments are mandatory before freezing them.
