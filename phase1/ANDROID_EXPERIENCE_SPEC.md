# Android UX, execution, persistence and accessibility contract
Status: proposed Phase 1 product/platform specification, NOT implemented | 2026-10-23 | [Master](PHASE1_MASTER_PLAN.md), [system contracts](SYSTEM_CONTRACTS.md).

## User journeys with observable outcomes
1. **Create a lab**: new/open/recent -> choose starter blank or curated offline scenario -> viewport shows devices with names and link status; can save without login.
2. **Add and connect devices**: pick host/switch/router; inspect port list by tap/long press; explicitly select source/destination port and medium, show validation and WAN/LAN warnings; intentional WAN remains permitted; one undoable operation recorded.
3. **Configure**: device editor exposes physical/logical interfaces and protocol services, config diff/validation; CLI may later offer equivalent typed commands; changes reflected in same engine state.
4. **Run**: mode Live/Simulation. Live advances simulation without stepping and UI consumes throttled snapshots; Simulation filters, one-event step, next-packet hop, run-to-breakpoint, pause/reset; same scheduler/physics.
5. **Inspect**: tap a PDU event -> header fields, ingress/egress, exact hops, state before/after, virtual timestamps, reason and correlation chain. Cross-filter by device/protocol/test; showing/hiding does not stop protocol processing.
6. **Troubleshoot**: intentionally wrong router port -> UI explains ingress WAN, unbound DHCP service, client IP config; highlight potentially suspicious cabling but no false "auto fix".
7. **Test destination**: explicit source interface, destination IP and optional intended device; show reply and remote-target/path verification separately. Same IP on two routers can't produce a fake target-success badge.
8. **Share/learn**: import/export via Android document picker, offline guided tasks, results evaluated against engine assertions, not layout coordinates.

## Screen and interaction map (screen design NOT yet approved)
Landing/projects; topology workspace; device/port configuration; terminal/CLI; timeline packet inspector; diagnostics/path; scenario guidance/assessment; settings/model capability registry. On phone: collapsible sheets and panels, landscape enabled; tablets can dock inspector beside topology. Back navigation and task dismissal preserve design safely. Hardware keyboard/mouse and stylus optional; provide non-drag alternatives.

## Canvas/world model
Coordinates stored separately from network logic, ideally fixed world-space values with transformation camera. Zoom/pan must preserve port hit testing and cable endpoint identity; no link to generic router icon without showing selected physical port. Link shape, curved routing, grouping and labels are UI concerns; event playback arrows derived from actual ingress/egress traces. LOD and viewport culling investigated in spike; no hard-coded maximum until benchmarks. Animations are secondary to correctness.

## Accessibility and responsiveness
Large selectable target regions independent of visual port glyph size; TalkBack device/port lists as alternative to canvas gestures; dynamic type; high contrast, color-independent states, reduced-motion alternative, focus order and keyboard actions. Dedicated diagnostics textual narrative; don't rely solely on cable color or packet animation.

## Mobile resource/lifecycle model
Engine work runs off main thread with one owner; UI consumes coalesced snapshots and paged trace, not one recomposition per internal event. Handle rotation, split screen, process death, app background, low memory and thermal degradation. Default when app backgrounded: pause simulation at safe boundary and persist design/optional resumable state; UI informs when only a restart/replay is possible. Android restrictions mean no unbounded always-running task guarantee. Preview and activity replay do not leak real hardware packet network access.

Evidence: Android architecture https://developer.android.com/topic/architecture, UI state persistence https://developer.android.com/topic/libraries/architecture/saving-states, background restrictions https://developer.android.com/develop/background-work/background-tasks, benchmarking https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview .

## Offline storage split
- Portable LabDesign small, versioned and semantic (nodes/ports/interfaces/links/config, selected reusable placements); display metadata independent.
- SessionSnapshot optional + engine/model/seed/version identifiers, active protocol caches/leases and scheduler to resume identical simulation.
- Trace logs optional segmented/indexed and paged, potentially compressed; avoid keeping unbounded logs and keep dropped/incomplete trace explicit.
- Project catalog/search/history may use Room; JSON and archive contents only after S05. All file imports untrusted, size/nesting/counts limited before allocation. Storage Access Framework for user-selected import/export; use scoped app storage without unnecessary broad permissions.
- Autosave plan: revisioned journal/temp write + integrity/checksum and recovery; users can distinguish **saved design** from **saved runtime trace**.

## Failure paths and flows to design before UI coding
- Link selected to occupied or physically incompatible port: reject with detail, retain previous topology.
- WAN instead of LAN: warning with device interface role and consequence; still allow intentional topology.
- Insufficient memory / 100k events: bounded pause and trace compression/retention warning; never silently declare test success.
- Import invalid/conflicting version or zip-bomb: refuse safely, preserve current session.
- Background kill during running: saved design recoverable, runtime resume only if checkpoint complete.
- Multiple simultaneous edit actions or CLI changes: command queue and revisions prevent last-writer silent overwrite.
- Device model doesn't support DTP/STP/IPv6: display unsupported clearly instead of generating arbitrary frames.
- No default gateway: packet source decision shown before any imagined hop.
- Scenario success: verify logical path and intended destination independently.

## UX acceptance matrix (to be measured, no numbers asserted)
10/50/100 nodes, 2x links; add/connect 20 devices without invalid accidental links; large phone DPI scaling; text size change; TalkBack navigate port/device; 1k/10k/100k events while exploring inspector; orientation change, resume, force-stop/process death, airplane mode; import/export corrupt lab, reopen valid project; power and memory profiling on actual 4GB Android phone plus reference device.

## Open design decisions
minSdk/targetSdk, Compose Canvas vs hybrid View, whether live-running persists in background, visual wire-routing details, gesture discoverability, trace UI paging database, saved-file extension, storage limits. Gate: evidence plus wireframes and user testing before design freeze, not just screenshots.
