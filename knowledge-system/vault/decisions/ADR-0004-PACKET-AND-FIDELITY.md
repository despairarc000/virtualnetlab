# ADR-0004 — Model actual packet semantics and declare fidelity
Status: PROPOSED_CONTRACT, pending S02/S08 | Date: 2026-10-23

## Context
Labels like "ICMP" or a plotted animation don't guarantee a correct packet or protocol. Full raw-byte modeling on every hop could create unnecessary complexity; fully semantic ad-hoc messages cannot claim PCAP/wire-level accuracy. See [architecture blueprint](../../../architecture/ARCHITECTURE_BLUEPRINT.md).

## Recommendation
Start with validated typed PDU fields and state-machine dispatch, design explicit codecs for RFC-scoped formats as proof of fidelity. Define a per-protocol support matrix, modeled states/fields, unsupported modes and deviations. Report real traced state transitions and port-level causes, not hand-scripted advice. Compare typed, hybrid, and raw-byte approaches in S02 before freezing packet API. Preserve parent/child packet/trace correlation through clones, tagging and TTL changes.

## Rejected
Pure visual packet token; arbitrary packet labels; assuming all simulated headers are wire compatible; exposing PCAP export before codecs validated.

## Verify
Golden encode/decode, malformed length/checksum, ICMP Echo and ARP fields, DHCP option and state-machine cases, packet mutation, latency/memory and trace test. Primary refs: [RFC 826](https://www.rfc-editor.org/rfc/rfc826.html), [RFC 792](https://www.rfc-editor.org/rfc/rfc792.html), [RFC 2131](https://www.rfc-editor.org/rfc/rfc2131.html), [RFC 3927](https://www.rfc-editor.org/rfc/rfc3927.html).
