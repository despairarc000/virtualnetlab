# Shared terminology and planning invariants
Status: proposed glossary | 2026-10-23. [Master](PHASE1_MASTER_PLAN.md).

- **Networking laboratory**: users build/configure/operate/inspect virtual devices and receive causal, testable network behavior; not merely a topology picture.
- **Simulation**: model-based behavioral representation of network events with explicit fidelity level and modeled time.
- **Emulation**: running a real/near-real OS stack or packet IO under compatible runtime; different operating/security/license demands.
- **Protocol conformance**: verified behavior within specified standard and supported scope, not unspecified global equivalence.
- **Discrete event**: clock jumps between scheduled events; sim time and Android wall time are different quantities.
- **Physical port**: cable/wireless attachment endpoint with medium, mode and link state.
- **Logical interface**: configured L3/network attachment (possibly over bridge/VLAN/port) with address/routing semantics.
- **Bridge/broadcast domain**: domain in which specified L2 frames may forward or flood, with VLAN/STP membership and boundaries.
- **Ingress/egress**: exact receiving/sending interface in event trace; not a device icon.
- **LAN/WAN role**: port/profile network role, not a universal property of copper; switch-to-WAN cabling can be physically valid.
- **DHCP lease**: configuration offered and acknowledged by DHCP server, with timing state; link-local 169.254 address is NOT a DHCP lease.
- **Probe**: explicit test stimulus with source, IP destination and optionally intended remote device/path, producing independently validated outcomes.
- **Packet identity/lineage**: persistent correlation across forwarding and broadcast copies, distinct from identical payload bytes.
- **State planes**: design/configuration, execution/runtime and UI/presentation — never conflate.
- **Causal diagnostics**: explanation derived from actual scheduled event transition and reason code, not assumed from topology geometry.
- **Golden test**: fixed input/actions/seed/model-version and asserted semantic trace, plus negative alternatives.
- **RFC normative text**: MUST/SHOULD/MAY have different meanings; implement documented subset with deviations and dated revisions.
- **Architecture gate**: objective evidence threshold for committing to long-lived contracts; docs being extensive is insufficient.
- **Disposable spike**: minimal throwaway experiment to resolve uncertainty; not a product milestone, production compatibility promise or code-quality exemption.
- **Open architecture decision**: explicit blocker or reversible assumption; absence of evidence is not approval.

## Requirement wording rule
Use SHALL for project requirements only when outcome is testable; label RECOMMENDED vs OPTIONAL for platform choices; label ASSUMPTION and OPEN for unverified facts. Every future "support" claim cites model version, tested cases and exclusions.

## Scope language
Phase 1 = planning, evidence and sign-off. Phase 2 = staged production implementation. Existing technical roadmap G0 = Phase 1 experimentation; G1 onwards are Phase 2 milestones. We plan the whole product but formally detail the earliest protocol vertical slices now. Subsequent protocols undergo the same design gate as they enter scope. Do not confuse phase names with network OSI layer numbers.
