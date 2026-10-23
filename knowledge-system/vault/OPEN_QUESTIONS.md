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
