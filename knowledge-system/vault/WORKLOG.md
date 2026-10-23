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

## 2026-10-23 — Phase 1 planning-only commitment
- User defined first program phase as *thorough end-to-end planning to implementation-ready detail* so irreversible coding begins only with validated architecture. Reversible throwaway experiments are allowed to settle unknowns.
- Added Phase 1 master plan, typed domain and scheduling contracts, protocol semantics, Android/UX/storage/lifecycle design, failure/security atlas, research/reuse decision gates, detailed handoff packets, glossary and live exit audit.
- Connected these through ICM, vault and navigation and extended test checks for route coverage.
- Not yet performed: independent peer review, actual source-level Filius audit, 4GB Android benchmark, packet buffer/scheduler spikes, protocol source-level conformance execution or Gate A sign-off. The exit audit explicitly remains NOT READY.

## 2026-10-23 — continuing Phase 1 P0 engineering contracts
- Rechecked latest known upstream Filius v2.14.0 tag 2026-08-29, GPL dual-option statement and legacy source showing layer worker start; **no current tagged source-level audit possible through runtime**. Decision remains blocked; no GPL source copied.
- Drafted device/port/bridge-domain/L3/service composition and WAN DHCP edge-case fixtures; defined scheduler event identity, serial mutation, stale event suppression, trace provenance and overload failure behaviors.
- Added standards-indexed DHCP/IPv4LL/ARP/ICMP/IPv4/RFC negative cases and urgent evidence debt. Next: S10 tagged-code review and S03/S01/S02/S04 measured spikes; no production code authorization.
