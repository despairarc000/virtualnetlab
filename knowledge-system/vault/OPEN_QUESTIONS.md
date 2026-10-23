# Open questions — 2026-10-23
Status: ACTIVE questions. No implicit approval of an answer.

| ID | Question / test | Decision owner | Exit evidence |
|---|---|---|---|
| Q1 | Kotlin/JVM vs Kotlin Multiplatform targets or JNI/native core? | Engine | Build prototype, trace equality, measured APK/CPU/memory |
| Q2 | Event/frame serialization (immutable class, pooled data, ByteArray)? | Engine | Golden traces, memory/GC tests |
| Q3 | Wi-Fi fidelity: logical association only or radio propagation model? | Protocols | Standards scope and benchmark |
| Q4 | What exact IOS-like CLI surface can be independently implemented safely? | CLI | Commands mapped to canonical model with parser tests |
| Q5 | What project format can be versioned/migrated, and what import limits? | Persistence | Schema fixtures plus malformed-project fuzz |
| Q6 | Which Android API level and device budgets for 4 GB RAM baseline? | Android | Real-device profiling and supported min SDK decision |
| Q7 | What optional remote emulator integration is valuable without impairing offline core? | Platform | Security model and demand evidence |
| Q8 | Will switch BPDUs and DTP control traffic be modeled accurately per hardware profile? | L2 | Standards references, device behavior matrix and tests |
| Q9 | How should ping identity distinguish selected device from same-valued local address? | Diagnostics | User-focused negative acceptance test |
| Q10 | When do we need virtual time vs real-time mode and background app lifecycle handling? | Engine/Android | Timers, replay, process death/instrumentation tests |

Record experiments, commit refs and tests when resolving. Move accepted outcomes into ADRs and update NAVIGATION, CHECKPOINT and implementation plan.

## Architecture review P0 resolutions pending (do not freeze decisions)
- S01: virtual integer-tick unit, event cancellation and same-tick flood rate; required [spike](../../architecture/SPIKES_AND_DECISION_GATES.md).
- S02: typed vs byte-backed PDU architecture, PCAP fidelity boundary and memory budget.
- S03: profile/port/broadcast-domain representation for integrated wireless routers and logical bridges.
- S04: Compose Canvas/custom View performance under large topology and constrained phone memory.
- S05: exact portable project container, checkpoint format, migration and secure import schema.
- S06: Android process lifecycle, run/pause semantics and resource budget on real hardware.
- S07: probe identity proof and path assertions under overlapping IPs.
- S08: explicit protocol implementation/fidelity level and independent oracle.
- S09: external backend extension boundary / privacy and permission architecture.
See [source review](../../architecture/SOURCE_EVALUATION.md), [risks](../../architecture/RISK_REGISTER.md) and [decision log](../../architecture/DECISION_LOG.md).
