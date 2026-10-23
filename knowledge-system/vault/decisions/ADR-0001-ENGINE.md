# ADR-0001: Deterministic packet/network simulator first
Status: ACCEPTED planning baseline | Date: 2026-10-23 | Revisitable on measured evidence.

## Context
Goal is offline-capable Android virtual network laboratory with inspectable cause/effect, not merely a topological editor or unlicensed vendor OS clone. See [IDEA_PLAN](../../../IDEA_PLAN.md) and [research](../research/NETWORK_SIMULATORS.md).

## Decision
Implement headless discrete-event engine with canonical virtual devices, ports, links, layered state machines and deterministic trace; all tests run against engine without GUI. Provide extension boundary for future emulation/alternate simulators but do not depend on them.

## Alternatives
- GNS3, CORE, containerlab, Kathará for local device emulation: deferred; depend on host privileges, containers, VM/image support or remote server.
- Port ns-3/OMNeT++: not selected initially due integration/mobile UX/license evaluation; reference models rather than copied code.
- Fake packet animations: rejected, because cannot verify causal correctness.
- Cloud-only backend: rejected as baseline because offline laboratory is required.

## Consequences and constraints
We must implement/prove every claimed protocol. Core abstraction supports evolving models and independent conformance verification. Performance needs measured testing on budget Android devices. No claim of fidelity for unimplemented protocol.
## Falsification criteria
Revisit if event engine cannot reasonably deliver target behaviors, tests reveal systematic fidelity limits, mobile memory/latency is unacceptable, or a vetted portable engine lowers cost without jeopardizing offline constraints/licensing.
