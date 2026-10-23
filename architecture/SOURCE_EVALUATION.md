# Research source evaluation and adoption analysis
Date: 2026-10-23 | Status: reviewed research, not code or legal advice. Linked [EVIDENCE](../knowledge-system/vault/EVIDENCE.md).

## Comparable system architectural lessons
| System | Useful mechanism | Integration burden / constraints | Decision |
|---|---|---|---|
| Cisco Packet Tracer | Learning-first topology editor, PDU event mode, assessment; scope is medium-fidelity simulation | Proprietary and not portable source | Benchmark *workflow*, not code/assets; verify semantics independently |
| ns-3 | Ordered DES events, extensible research models, simulation trace workflows | C++, CMake, mobile JNI/integration, GNU GPLv2; native embedding requires licensing+engineering review | Use as design reference and possible external test oracle |
| OMNeT++ / INET | Component/message architecture with rich networking models | C++, INET dependencies, Academic Public License for OMNeT++, commercial constraints, unproven Android portability | Use as reference and oracle; no default embedded implementation |
| GNS3 | GUI/controller/compute/emulator, configurable real IOS-like lab backends | Running emulator processes/images and server, resource burden, licenses for vendor images | Optional remote backend someday, not offline core |
| CORE | Linux namespaces, bridges and gRPC interface | Host Linux namespace/privilege and process model | Optional future backend only |
| containerlab | Declarative node/lab topology using container NOS | Linux containers and privileged networking | Inspiration for declarative labs |
| Kathará | Docker topology labs and automation | Docker runtime | External comparison |
| Batfish | Static config analysis and reachability checks | Not real-time packet simulator | Inspiration for scenario validator and policy diagnostic |

## Licensing checkpoints
- ns-3 official: https://www.nsnam.org/about/ declares GPLv2. Any code/library inclusion is subject to GPL compliance, compatibility and distribution duties. General architectural ideas are not copyrighted implementation code.
- OMNeT++: https://omnetpp.org/intro/license.html Academic Public License for noncommercial purposes, commercial license otherwise. Do not embed without permission/license strategy.
- Every third-party model, icon, protocol implementation, library, firmware image and transitive dependency requires a license inventory and provenance. No Cisco IOS binaries, Packet Tracer asset extraction or proprietary `.pkt` compatibility promises.
- Device/CLI behavior and networking specifications may be modeled independently with documented standards. No vendor-trademark claims of official endorsement.

## Standards reference set and model-deviation planning
- ARP: RFC 826 https://www.rfc-editor.org/rfc/rfc826.html
- IPv4 host requirements: RFC 1122 https://www.rfc-editor.org/rfc/rfc1122.html
- IPv4 routers: RFC 1812 https://www.rfc-editor.org/rfc/rfc1812.html
- ICMPv4: RFC 792 https://www.rfc-editor.org/rfc/rfc792.html
- DHCPv4: RFC 2131 https://www.rfc-editor.org/rfc/rfc2131.html
- IPv4 link-local: RFC 3927 https://www.rfc-editor.org/rfc/rfc3927.html
- Later: IPv6/ND RFC 8200/4861, TCP RFC 9293, DNS RFC 1034/1035, IEEE Ethernet and spanning-tree details with available licensed documentation. Validate any superseding RFC and exact section before each implementation; label 802.1D/802.1Q profile/edition explicitly rather than invent source-level conclusions.

## Android implementation references
- App separation and SSOT https://developer.android.com/topic/architecture
- Offline data architecture https://developer.android.com/topic/architecture/data-layer/offline-first
- Compose drawing https://developer.android.com/develop/ui/compose/graphics/draw/overview
- Lifecycle/background constraints https://developer.android.com/develop/background-work/background-tasks
- Macrobenchmark https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview
- File selection/import https://developer.android.com/guide/topics/providers/document-provider
- Room https://developer.android.com/training/data-storage/room
- Accessibility https://developer.android.com/guide/topics/ui/accessibility/apps

## Comparative decision
Make **simulation engine** an independent deterministic core with bounded per-protocol fidelity, before integrating any existing simulator. Explicitly leave integration decisions provisional and reopen with measured cost + legal review. The highest payoff from existing systems is *architecture and test methodology*, not wholesale mobile porting.
