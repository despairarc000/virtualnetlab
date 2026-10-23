# ADR-0005 — Physical port vs logical domain and probe identity
Status: PROPOSED_CONTRACT, pending S03/S07 | Date: 2026-10-23

## Context
A physically valid switch-to-WAN connection can be inappropriate for LAN DHCP. A router may have multiple L2 groups, multiple L3 interfaces or duplicated addresses on unrelated domains. Address-only ping success is not proof of the selected remote endpoint.

## Recommendation
Stable IDs for physical port, media link, bridge/broadcast domain, L3 interface, device, packet/probe. Model bridge/LAN grouping separately from WAN interfaces; support capability-based profiles (PC/switch/router/home-router/AP). For each test, record explicitly chosen source interface and destination IP plus optionally intended remote device/interface and expected traversed path. Provide distinct echo-reply and intended-target-reached outcomes. Link auto-selection may warn; must allow legitimately chosen WAN link and display exact ports.

## Reject
"Switch connected to any router Ethernet port" implies LAN membership; global switch MAC table despite VLAN membership; "success" based on matching IP alone; equality of device name as identity.

## Verify
LAN/WAN DHCP negative fixture, multi-NIC host, ambiguous address, self-ping with cable disconnected, loopback/duplicate IP across separate networks. S03/S07.
