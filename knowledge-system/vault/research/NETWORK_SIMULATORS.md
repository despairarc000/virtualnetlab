# Comparative research: network laboratories and simulation approaches
Date: 2026-10-23 | Status: ACTIVE research, PROPOSED conclusions. Sources checked Oct 2026; exact versions/licensing must be re-checked before dependencies are imported.

## What to reproduce
Cisco Packet Tracer's stated purpose is a medium-fidelity visual network learning, troubleshooting, collaboration and assessment environment, not a complete emulator of every hardware feature. See [S1](../EVIDENCE.md). Our target is **full laboratory workflows** with explicitly bounded and correct model fidelity, not binary or icon parity.

| System | Method | Lessons to adopt | Why not use as Android baseline |
|---|---|---|---|
| Cisco Packet Tracer | Integrated educational simulation | Live/event mode, PDU inspector, lessons, topology configuration | Proprietary; no source to port; reported behaviors need independent validation |
| ns-3 | C++ discrete-event network simulator | Event-time discipline, trace model, validation and diverse model architecture | Research workflow integration and Android toolchain complexity; GPLv2 needs legal assessment |
| OMNeT++ + INET | Modular C++ event simulator + protocol models | Composition, message-based actors, protocol extensibility | Not a turnkey touch-Android app; OMNeT++ academic license review and heavy porting |
| GNS3 | Simulation plus vendor OS emulation (often VM/QEMU) | Realistic device CLI, modular device backends | Heavy OS images/virtualization/resource burden; dependencies and OS image rights |
| CORE | Linux namespace / virtual Ethernet based emulator | Stateful lab sessions and useful GUI/daemon separation | Linux privilege/userspace assumptions unsuitable as native phone default |
| containerlab | Containerized network OS topology orchestration | Declarative topology formats, repeatable labs | Container runtime and privileged networking not assumed on Android |
| Kathará | Docker-container network emulator | Reproducible scripts, executable network nodes | Container host assumption and resource cost |
| Batfish | Configuration-based symbolic reachability analysis | Static diagnostics before packet execution, policy validation | Not a time-dependent interactive packet simulator |

## Synthesis
No reviewed system simultaneously provides our desired offline low-resource Android touch UI, educational observability and widely extensible packet simulation as an out-of-box embedded component. The **best starting strategy is an independent small deterministic discrete-event engine** with strong regression tests and clear protocol scope. Borrow concepts/interfaces; don't copy proprietary or license-incompatible code.

Use GNS3/CORE/containerlab/Kathará later as optional remote/emulation complement if research establishes user benefit. ns-3 or OMNeT++ can serve as reference/validation or future backend after portability and license study; do not claim that native Android execution is already validated.

## Why pure real network emulation isn't the first milestone
A Linux namespace/bridge/container or QEMU lab running full router operating systems is materially different from portable logical simulation. Android app sandbox, privileged networking, hardware support, proprietary images and mobile memory/power make local emulation a poor *default* assumption. These are engineering inferences to test, not measured impossibilities.

## Primary-source links
- Packet Tracer: https://tutorials.ptnetacad.net/help/default/intro.htm
- ns-3 manual: https://www.nsnam.org/docs/manual/singlehtml/index.html
- ns-3 overview / GPLv2: https://www2.nsnam.org/about/
- OMNeT++: https://omnetpp.org/intro/
- INET: https://inet.omnetpp.org/
- GNS3: https://docs.gns3.com/docs
- CORE: https://coreemu.github.io/core/
- containerlab: https://containerlab.dev/
- Kathará: https://www.kathara.org/man-pages/kathara.1.html
- Batfish: https://github.com/batfish/batfish
- Android Compose graphics: https://developer.android.com/develop/ui/compose/graphics/draw/overview

## Further research before implementation
Protocol standards/RFCs, reference packet captures and constrained-device benchmarks; current third-party licenses, build distributions and alternatives; independent traces for compatibility-sensitive behavior.

## October 2026 deeper architecture review update
- Actual ns-3 scheduling ties use monotonic event IDs; design our own order contract without importing GPLv2 code: https://www.nsnam.org/docs/manual/html/events.html and https://www.nsnam.org/about/
- OMNeT++ is under Academic Public License; external commercial distribution/use can require commercial licensing, so it is **NOT** a drop-in LGPL module: https://omnetpp.org/intro/license.html
- GNS3 divides topology client from controller/compute/emulator nodes; this supports future optional remote backend separation, not a decision to use one now: https://docs.gns3.com/docs/using-gns3/design/architecture
- CORE's Linux namespace networking depends on host facilities: https://github.com/coreemu/core/blob/master/docs/architecture.md
- Review is now indexed through [source evaluation](../../../architecture/SOURCE_EVALUATION.md) and [architecture audit](../../../architecture/ARCHITECTURE_REVIEW.md). Comparisons are qualitative, not measured Android performance.
