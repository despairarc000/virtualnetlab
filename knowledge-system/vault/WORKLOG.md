# Worklog
## 2026-10-23 — bootstrap
- Context: user instructed setup of ICM, Graphify, vault and navigation on despairarc000/virtualnetlab, capture full virtual-network-laboratory vision, research related systems and choose an implementation plan.
- Decision: deterministic, Kotlin-based simulation-first architecture; document rationale, explicit rejection of running full Linux emulation locally on unprivileged Android for first release.
- Actions: root/scoped AGENTS, navigation, vault research/decisions, routing rules, graph builder, doctor and tests prepared.
- Not done: Android application, runtime engine, APK or real-device tests.
- Next: headless schema and scheduler, test-first.

## 2026-10-23 — architecture depth review
- Scope: revisit implementation feasibility and dependency/fidelity contracts before any network code is built.
- Research: ns-3 event tie semantics/GPLv2; OMNeT++/INET modules/Academic Public License; GNS3 controller/emulation; CORE Linux namespace; Android SSOT/UDF, graphics, background/process lifecycle and offline persistence; RFC 2131/3927/826/792/1122/1812.
- Decision: maintain DES/Kotlin/Compose as an accepted baseline, but defer packet representation/API/persistent storage format and minimum SDK until instrumented spikes.
- Add design/runtime/presentation state separation; physical port/bridge-domain/L3 interface separation; explicit target-device probe identity; causal trace and truthful fidelity.
- Add G0 architecture gate, risk register, traceability and test strategy. Status: paper review only; no code or measured device result.
