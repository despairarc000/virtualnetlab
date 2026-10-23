# Filius build-vs-adapt audit — 2026-10-23
Status: **PARTIAL SOURCE REVIEW / S10 STILL BLOCKED**. This document is research, not a port, successful Android build or permission to copy Filius source. [Master](../PHASE1_MASTER_PLAN.md), [decisions](../DECISION_GATES.md), [risk](../../architecture/RISK_REGISTER.md).

## Reproducible upstream anchors
- Official Filius: https://gitlab.com/filius1/filius
- Official tags: https://gitlab.com/filius1/filius/-/tags — v2.14.0, dated 2026-08-29, upstream short revision 6656e245 (confirm *full* SHA before pinned-source code review).
- Official project README: https://gitlab.com/filius1/filius/-/blob/master/Readme.md — GPLv2 **or** GPLv3 stated; Java desktop program; supports Windows/Linux; desktop Swing/Java modules and optional Java compiler features included in build notes.
- License cross-source conflict: https://signpath.org/projects/filius/ lists GPLv3 only. Repo README and historical source headers say GPLv2 or GPLv3. Resolve using version-pinned full source LICENSE/copyright headers and legal distribution policy; third-party listing is not an authoritative substitution.
- Legacy snapshot, **not current master**: https://www.javatips.net/api/filius-master/src/filius/software/system/InternetKnotenBetriebssystem.java — explicitly starts layered `ethernet.starten(); arpVermittlung.starten(); vermittlung.starten(); icmpVermittlung.starten();` and describes starting protocol threads. https://www.javatips.net/api/filius-master/src/filius/gui/netzwerksicht/GUIMainArea.java — desktop GUI code owns device-specific component/image handling. Neither proves the same design in v2.14.0.
- Legacy UI/network model: https://www.javatips.net/api/filius-master/src/filius/hardware/knoten/Vermittlungsrechner.java and https://www.javatips.net/api/filius-master/src/filius/hardware/Verbindung.java .
- Academic historical account of educational architecture: https://noah.nrw/ubsihs/download/pdf/3559890 — historical, not current behavior evidence.

## What is grounded, inferred, unknown
| Observation | Evidence class | Architectural implication |
|---|---|---|
| Filius is an actively tagged educational network simulator | official repository/tags, PRIMARY | A serious candidate; do not reject by age or language alone |
| Upstream README declares Java desktop, Java desktop/runtime modules and GPLv2-or-v3 | official README, PRIMARY | Desktop UI replacement and GPL redistribution must be assessed |
| Legacy protocol software explicitly starts protocol threads | historical third-party snapshot, HISTORICAL SOURCE | Could conflict with deterministic central event queue; current implementation unknown |
| Legacy desktop UI calls `ImageIcon`, device type checks | historical third-party snapshot, HISTORICAL SOURCE | Separation of portable engine from Swing needs source inspection |
| Android cannot directly run standard Java Swing GUI / Java desktop modules as ordinary APK | engineering inference + Android platform limitations | A UI rewrite is expected, but engine portability remains unproven |
| Current engine is thread-based / unsuitable to port | UNVERIFIED | **DO NOT CLAIM** until v2.14.0 scheduler/protocol/device source inspected |
| Reusing some protocol code is faster | UNVERIFIED | Depends on coupling, tests, licenses and long-term maintenance |

## Detailed source-review tasks that MUST be done to close S10
1. Pin complete v2.14.0 Git commit, collect top-level `pom.xml`, `src/main` tree, LICENSE and dependency list, including generated/runtime compiler components.
2. Determine project module boundaries and package dependency graph; locate simulation clock and event ordering, protocol handler/thread creation, ports/NIC/bridge/router topology, packet classes, request/response tracking, serialization and checkpoint.
3. Trace **one ping** from application request across NIC/switch/router to reply, including if/where a real packet message exists and protocol worker synchronization. Repeat for DHCP handshake, retransmission, pool-to-ingress check, ARP cache lifecycle.
4. Identify Swing/AWT/desktop Java APIs imported by engine and all indirect dependencies; measure cost of isolating JVM-only core. Enumerate missing Android APIs and runtime code compiler/security concerns.
5. Inspect test matrix: deterministic repeated trace assertion? Packet byte oracle? Negative WAN/LAN cases? Multi-interface router? Control plane / STP? Android-compatible unit tests? Flag gaps, do not assume absence based on docs.
6. Licensing: determine exact release GPL option, whether app can/will be open-source under compatible terms, which code/assets originate elsewhere, third-party copyright and notices. Get explicit approval of project licensing choice before any code reuse.
7. Prototype **throwaway** adapter only if feasible and permitted: headless project with host-switch-router trace, JVM/Android test, 10/50/100-node CPU/memory measurement, lifecycle constraints.
8. Compare with a clean Kotlin DES spike on fidelity, determinism, time to adapt, documentation, license obligations, Android battery/memory, maintenance.
9. Record decision ACCEPT_ADAPT / ACCEPT_INDEPENDENT / ACCEPT_HYBRID only when measurements and signed ADR exist; code-free architectural lessons can be adopted now.

## Initial decision
**S10 remains OPEN**, with independent Kotlin DES the CONDITIONAL preference because it directly targets deterministic event stepping and zero desktop dependency. This is *not* a final rejection of Filius. GPL legal review needed if reuse is considered. No Filius code or assets imported into VirtualNetLab.

## Access limitations
During this review, direct GitLab API archive fetching/source listing was unavailable in the runtime, so v2.14 source-level call graph and full dependency/license audit were NOT completed. Official README/tags and historical examples were accessible via indexed web sources. Re-run upstream audit from a developer environment with GitLab access before S10 signoff.

## Adjacent references
ns-3 event semantics: https://www.nsnam.org/docs/manual/html/events.html (same-time events FIFO by sequence, cancel vs remove implications). This provides one control design for independent DES, not proof all network behavior will be accurate. [Network comparator](../../architecture/SOURCE_EVALUATION.md).
