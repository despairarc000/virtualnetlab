# Evidence ledger
Status: ACTIVE | 2026-10-23. Sources are references, not imported/copied source code.

| ID | Claim supported | Primary source | Limit |
|---|---|---|---|
| S1 | Packet Tracer is a medium-fidelity learning simulation, visualization, collaboration and assessment environment | https://tutorials.ptnetacad.net/help/default/intro.htm | Does not prove full network fidelity or mobile support |
| S2 | ns-3 implements a C++ discrete-event simulation core, supports trace/model workflows | https://www.nsnam.org/docs/manual/singlehtml/index.html | No validated Android embedding for this project |
| S3 | OMNeT++ is a modular discrete-event library; INET supplies networking models | https://omnetpp.org/intro/ and https://inet.omnetpp.org/ | License and integration complexity require review before reuse |
| S4 | GNS3 mixes simulation with network OS emulation, frequently uses VMs | https://docs.gns3.com/docs | Does not establish suitability as standalone offline mobile engine |
| S5 | containerlab orchestrates containerized NOS and topology wiring | https://containerlab.dev/ | Needs a container-capable host |
| S6 | Kathará uses Docker/container-backed emulation | https://www.kathara.org/man-pages/kathara.1.html | Needs container runtime, not default unprivileged Android |
| S7 | CORE emulates network nodes with Linux namespaces and virtual links | https://coreemu.github.io/core/ and https://github.com/coreemu/core/blob/master/docs/architecture.md | Not a ready native Android simulation engine |
| S8 | Batfish verifies modeled config reachability/security/compliance | https://github.com/batfish/batfish | Complementary analysis, not interactive packet simulator |
| S9 | Compose can render custom Android visualizations; Kotlin libraries support JVM/Android test boundaries | https://developer.android.com/develop/ui/compose/graphics/draw/overview and https://kotlinlang.org/docs/multiplatform/multiplatform-discover-project.html | Implementation and performance untested |

## User-observed regression evidence (transcribed, not independently reproduced)
- Packet Tracer: PC -> switch -> home wireless router *Internet* port, DHCP Discover UDP 68->67 dst 255.255.255.255 reached WAN, router reported no pool for ingress, dropped; PC used 169.254.x.x, gateway absent, outside-subnet ICMP dropped on PC.
- Packet Tracer: unrelated STP/DTP background events interleaved with manual PDU globally.
- Packet Tracer: a successful router-to-router Simple PDU with overlapping router LAN IPs may fail to prove WAN traversal. Hypothesis: address selection/local-self delivery; needs a controlled test before asserting exact mechanism.

## Source use rules
Keep independent observations separate from official docs and hypotheses. Record source URL, date, build/version and experiment when validating. Standards-based models need RFC/IEEE references at implementation time and a model deviation registry.


## Protocol specifications to consult at implementation
- DHCPv4 RFC 2131: https://www.rfc-editor.org/rfc/rfc2131.html — formal DHCP client/server states, port use, retries and broadcasts; model deviations must be documented.
- IPv4 Link-Local RFC 3927: https://www.rfc-editor.org/rfc/rfc3927.html — IPv4LL 169.254/16 acquisition, probes and collisions; distinguish APIPA as a host policy, not DHCP success.
- ARP RFC 826: https://www.rfc-editor.org/rfc/rfc826.html — address resolution.
- ICMP RFC 792: https://www.rfc-editor.org/rfc/rfc792.html — IPv4 control messages.
- Traditional STP port states and timing (Cisco reference): https://www.cisco.com/c/en/us/support/docs/switches/catalyst-6500-series-switches/24330-185.html — model only the selected STP profile.

## Architecture review primary sources (2026-10-23)
| ID | Observed source statement | Primary URL | Limits |
|---|---|---|---|
| S10 | ns-3 uses discrete-time scheduler; equal-time events ordered by unique event ID | https://www.nsnam.org/docs/manual/html/events.html | Architecture reference, not direct library reuse |
| S11 | ns-3's software is GNU GPLv2 | https://www.nsnam.org/about/ | Any incorporation requires license analysis |
| S12 | OMNeT++ is modular discrete-event infrastructure, INET supplies models | https://doc.omnetpp.org/omnetpp/manual/ and https://inet.omnetpp.org/docs/developers-guide/ch-introduction.html | Its Academic Public License restricts commercial use |
| S13 | OMNeT++ Academic Public License / commercial option | https://omnetpp.org/intro/license.html | External counsel may be required before integration |
| S14 | GNS3's GUI/controller/compute/emulator separation | https://docs.gns3.com/docs/using-gns3/design/architecture | Useful later for remote optional backend |
| S15 | CORE uses namespaces/virtual Ethernet on Linux | https://github.com/coreemu/core/blob/master/docs/architecture.md | Not native unprivileged Android default |
| S16 | Android favors separation of concerns and single source of truth | https://developer.android.com/topic/architecture | Doesn't prove Compose Canvas performance |
| S17 | Android's offline-first and process/lifecycle constraints | https://developer.android.com/topic/architecture/data-layer/offline-first and https://developer.android.com/develop/background-work/background-tasks | Must validate Android lifecycle empirically |
| S18 | Android recommends Macrobenchmark for frame/UI performance | https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview | Does not supply performance numbers |
| S19 | Android Storage Access Framework and Room document persistence options | https://developer.android.com/guide/topics/providers/document-provider and https://developer.android.com/training/data-storage/room | Candidate, not format decision |
| S20 | RFC 1122 host-layer requirements and RFC 1812 IPv4 router requirements | https://www.rfc-editor.org/rfc/rfc1122.html and https://www.rfc-editor.org/rfc/rfc1812.html | Older texts may have updates/errata; track model subset |
| S21 | Kotlin Serialization supports JSON and configurable unknown-key behavior | https://kotlinlang.org/docs/serialization.html and https://kotlinlang.org/docs/serialization-json-configuration.html | Strict semantic validation still mandatory |
| S22 | Android recommends accessibility support, including larger touch targets | https://developer.android.com/guide/topics/ui/accessibility/apps | Real device testing remains needed |

Review-specific inferences and unknowns are labeled in [architecture audit](../../architecture/ARCHITECTURE_REVIEW.md).

## Additional comparable-system evidence
| ID | Observed source statement | Primary URL | Limits |
|---|---|---|---|
| S23 | Filius is a Java educational network simulator; its README advertises GPLv2 or GPLv3 and Windows/Linux support | https://gitlab.com/filius1/filius | Needs current tagged license/source and architecture review |
| S24 | Cisco Modeling Labs runs licensed virtual network OS images and cautions against using images outside CML | https://developer.cisco.com/docs/modeling-labs/vm-images-for-cml-labs/ | No inclusion of proprietary images in our project |
| S25 | Mininet uses Linux namespaces and virtual Ethernet links | https://mininet.org/overview/ | Linux-centric emulation, not a built-in Android engine |
| S26 | EVE-NG requires hypervisor capabilities | https://www.eve-ng.net/index.php/supported-hardware-and-software-systems/ | Exact resource requirements vary by lab |
| S27 | Boson NetSim supports interactive educational assessment | https://netsim.boson.com/ | Proprietary/cloud service |

## Phase 1 source-level notes (2026-10-23)
- RFC 2131 §3.6 and §4.4 explicitly describe independent client processing per interface, INIT→SELECTING→REQUESTING→BOUND and RENEWING/REBINDING/expiry behavior: https://www.rfc-editor.org/rfc/rfc2131.html . DORA alone is not complete DHCP.
- RFC 3927 §§2.1–2.5 include IPv4LL selection, ARP probing, announcements and conflict handling, not merely assigning arbitrary 169.254: https://www.rfc-editor.org/rfc/rfc3927.html .
- ns-3 scheduler documentation distinguishes discrete simulation time from wall time, scheduled events, cancel/remove and equal-time ordering: https://www.nsnam.org/docs/manual/html/events.html .
- Android Saved State guidance says large/complex application data requires local persistence, not SavedStateHandle: https://developer.android.com/topic/libraries/architecture/saving-states .
- Android foreground/background task guidance cautions restrictions and battery/power overhead: https://developer.android.com/develop/background-work/background-tasks .
- Filius upstream repository is an educational Java simulator under GPLv2 or GPLv3; reuse needs version-pinned source/legal analysis: https://gitlab.com/filius1/filius .
These documents are **planning references** and not test evidence that VirtualNetLab implements them.

## Phase 1 current review sources and limits — 2026-10-23
- Filius official upstream tags: https://gitlab.com/filius1/filius/-/tags (v2.14.0 2026-08-29 / short SHA 6656e245). README https://gitlab.com/filius1/filius/-/blob/master/Readme.md says dual GPLv2 or GPLv3.
- Alternate distribution listing: https://signpath.org/projects/filius/ says GPLv3-only. **Conflict flagged**, not interpreted as legal answer.
- Historical Filius per-layer worker starts: https://www.javatips.net/api/filius-master/src/filius/software/system/InternetKnotenBetriebssystem.java . Historical snapshot is NOT current v2.14 source.
- ns-3 DES / equal-time FIFO and cancel memory tradeoff: https://www.nsnam.org/docs/manual/html/events.html .
- IPv4LL candidate MUST be probed before use; duplicate detection, rate limits and link-local router forwarding prohibition: https://www.rfc-editor.org/rfc/rfc3927.html §§2,7,9.
- DHCP initialization, transaction xid, retry and lease state: https://www.rfc-editor.org/rfc/rfc2131.html §§3.1,4.4.
- ARP packet layout/next-hop address lookup: https://www.rfc-editor.org/rfc/rfc826.html ; host on-link gateway behavior: https://www.rfc-editor.org/rfc/rfc1122.html .
- Android UI state preservation limits: https://developer.android.com/topic/libraries/architecture/saving-states . Compose `drawWithCache` graphics memory tradeoffs: https://developer.android.com/agents/skills/jetpack-compose/jetpack-compose-performance/references/graphics-performance .
These citations support **requirements and architecture hypotheses**, not implementation or performance success.

## Cross-layer reference addendum (2026-10-23)
- INET network interface table and physical channel design (interface registry distinct from ports/link transmission): https://github.com/inet-framework/inet/blob/master/doc/src/users-guide/ch-network-interfaces.rst . External architectural reference, **not** reused code.
- RFC 1812 §5.2–5.3 on IPv4 router forwarding/local delivery and TTL behavior: https://www.rfc-editor.org/rfc/rfc1812.html . Router processing for own IP need not be forwarded; TTL semantics matter.
- RFC 3927 §§2.6/7 forbids IPv4 link-local packets forwarded by routers: https://www.rfc-editor.org/rfc/rfc3927.html . This is stronger than "no gateway from APIPA".
- Android offline-first local sources are source of truth for app data: https://developer.android.com/topic/architecture/data-layer/offline-first . Applied as design for offline saved labs, not proof Room/database choice.
- ns-3 event manual: timestamp order and same-time event ID tie resolution: https://www.nsnam.org/docs/manual/html/events.html . A design reference only.
