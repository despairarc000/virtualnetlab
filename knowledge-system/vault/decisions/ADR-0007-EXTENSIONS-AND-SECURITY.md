# ADR-0007 — Capability-bounded extensions and offline security
Status: PROPOSED_CONTRACT, pending S09 | Date: 2026-10-23

## Context
We want an expanding library of devices, protocol models, curricula and potential real-OS emulation, but executing user-supplied code, embedding vendor firmware or opening real sockets by default can threaten privacy, stability and licensing.

## Recommendation
Versioned immutable device profile metadata and explicit model capability flags. Built-in trusted protocol components initially; user-imported projects contain only declarative data and data-only constrained scenario DSL, not arbitrary executable plugins. No real packet injection/network bridging or cloud login for core functionality. Future adapter to external GNS3/containerlab-like service must have separate user opt-in, authenticated transport, capability negotiation, sandbox, permission model and licensing review. Third-party dependencies require license checks and source attribution.

## Rejected
Silently downloading firmware, copying vendor code/assets, unreviewed embedded ns-3/OMNeT++, arbitrary plugin execution from imported files, auto-opening host-network connectivity.

## Verify
Threat-model red team import corpus, manifest permission audit, SBOM/license review, optional backend API mock. OMNeT++ Academic Public License restricts commercial usage; ns-3 is GPLv2—these licensing issues matter before incorporation. [License evidence](../EVIDENCE.md).
