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
