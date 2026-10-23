#!/usr/bin/env python3
"""VirtualNetLab dependency graph, deterministic context routing and docs doctor.
Stdlib only. Usage: python tools/knowledge.py {doctor|graph|route} [args]
"""
from __future__ import annotations

import argparse
import ast
from collections import deque
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "AGENTS.md", "NAVIGATION.md", "IDEA_PLAN.md", "TECHNICAL_PLAN.md",
    "knowledge-system/icm/ICM.md", "knowledge-system/graphify/GRAPHIFY.md",
    "knowledge-system/vault/INDEX.md", "knowledge-system/vault/CHECKPOINT.md",
)
MD_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
BASE = ["AGENTS.md", "NAVIGATION.md", "IDEA_PLAN.md", "TECHNICAL_PLAN.md",
        "knowledge-system/vault/CHECKPOINT.md"]
ROUTES = {
    "engine": (("engine", "scheduler", "replay", "deterministic", "event", "core"),
        ("knowledge-system/vault/decisions/ADR-0001-ENGINE.md", "knowledge-system/vault/specs/LAB_ACCEPTANCE.md", "knowledge-system/vault/specs/PROTOCOL_MATRIX.md")),
    "protocol": (("protocol", "network", "dhcp", "arp", "icmp", "router", "switch", "vlan", "stp", "dtp", "wan", "packet"),
        ("knowledge-system/vault/specs/PROTOCOL_MATRIX.md", "knowledge-system/vault/specs/LAB_ACCEPTANCE.md", "knowledge-system/vault/EVIDENCE.md")),
    "android": (("android", "ux", "compose", "ui", "canvas", "apk", "touch"),
        ("knowledge-system/vault/decisions/ADR-0002-ANDROID.md", "knowledge-system/vault/OPEN_QUESTIONS.md")),
    "research": (("research", "comparison", "emulation", "ns3", "ns-3", "gns3", "omnet", "containerlab"),
        ("knowledge-system/vault/research/NETWORK_SIMULATORS.md", "knowledge-system/vault/EVIDENCE.md", "knowledge-system/vault/decisions/ADR-0001-ENGINE.md")),
    "knowledge": (("knowledge", "navigation", "graph", "icm", "vault", "documentation"),
        ("knowledge-system/icm/ICM.md", "knowledge-system/graphify/GRAPHIFY.md", "knowledge-system/vault/INDEX.md")),
    "handoff": (("handoff", "status", "continue", "checkpoint", "next"),
        ("knowledge-system/vault/CHECKPOINT.md", "knowledge-system/vault/WORKLOG.md", "knowledge-system/vault/OPEN_QUESTIONS.md")),
}


def md_files(root=ROOT):
    return sorted(p for p in root.rglob("*.md") if ".git" not in p.parts and ".gradle" not in p.parts)


def path_key(path, root=ROOT):
    return path.relative_to(root).as_posix()


def local_links(path, root=ROOT):
    text = path.read_text(encoding="utf-8")
    for raw in MD_LINK.findall(text):
        url = raw.strip().split(" ", 1)[0].strip("<>")
        if not url or url.startswith(("#", "http://", "https://", "mailto:", "data:")):
            continue
        target = url.split("#", 1)[0].split("?", 1)[0]
        if target:
            yield raw, (path.parent / target).resolve()


def graph_edges(root=ROOT):
    edges = set()
    existing = {p.resolve() for p in root.rglob("*") if p.is_file()}
    for doc in md_files(root):
        for _, target in local_links(doc, root):
            if target in existing and target.suffix == ".md":
                edges.add((path_key(doc, root), path_key(target, root), "doc-link"))
    pyfiles = sorted(root.rglob("*.py"))
    py_index = {path_key(p, root)[:-3].replace("/", "."): p for p in pyfiles}
    for p in pyfiles:
        try:
            tree = ast.parse(p.read_text(encoding="utf-8"))
        except (SyntaxError, UnicodeDecodeError):
            continue
        src = path_key(p, root)
        for node in ast.walk(tree):
            names = []
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                names = [node.module]
            for name in names:
                dep = py_index.get(name)
                if dep and dep != p:
                    edges.add((src, path_key(dep, root), "python-import"))
    return sorted(edges)


def route(task):
    words = set(re.findall(r"[a-z0-9-]+", task.lower()))
    hits = []
    paths = list(BASE)
    for name, (keys, docs) in ROUTES.items():
        score = sum(1 for k in keys if k in words)
        if score:
            hits.append((name, score))
            paths.extend(docs)
    if not hits:
        paths.extend(["knowledge-system/vault/INDEX.md", "knowledge-system/vault/OPEN_QUESTIONS.md"])
    unique = list(dict.fromkeys(paths))
    return sorted(hits, key=lambda t: (-t[1], t[0])), unique


def doctor(root=ROOT):
    errors = []
    for required in REQUIRED:
        if not (root / required).is_file():
            errors.append(f"Missing canonical file: {required}")
    docs = md_files(root)
    for doc in docs:
        for original, target in local_links(doc, root):
            if not target.is_relative_to(root.resolve()):
                errors.append(f"Escaping local link: {path_key(doc, root)} -> {original}")
            elif not target.exists():
                errors.append(f"Broken local link: {path_key(doc, root)} -> {original}")
    # Every vault doc should be reachable from INDEX through explicit Markdown links.
    index = (root / "knowledge-system/vault/INDEX.md").resolve()
    visited = set()
    if index.exists():
        work = deque([index])
        while work:
            current = work.popleft()
            if current in visited or not current.exists() or current.suffix != ".md":
                continue
            visited.add(current)
            work.extend(t for _, t in local_links(current, root) if t not in visited)
    for doc in docs:
        if "knowledge-system/vault/" in path_key(doc, root) and doc.resolve() not in visited:
            errors.append(f"Vault page unreachable from INDEX: {path_key(doc, root)}")
    for name, (_, paths) in ROUTES.items():
        for path in paths:
            if not (root / path).is_file():
                errors.append(f"ICM {name}: route missing {path}")
    return errors


def graph_report(root=ROOT):
    edges = graph_edges(root)
    files = sorted({x for a, b, _ in edges for x in (a, b)})
    lines = ["# Graphify derived relationships", "", "Generated by tools/knowledge.py. Edges are literal links or statically identified Python imports.", "", f"Nodes: {len(files)} | Edges: {len(edges)}", "", "| From | To | Type |", "|---|---|---|"]
    lines.extend(f"| `{a}` | `{b}` | {t} |" for a, b, t in edges)
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("doctor")
    g = sub.add_parser("graph")
    g.add_argument("--output", help="Write deterministic markdown graph to repo-relative file")
    r = sub.add_parser("route")
    r.add_argument("task", nargs="+", help="Task description or keywords")
    args = parser.parse_args()
    if args.cmd == "doctor":
        errs = doctor()
        if errs:
            print("\n".join("ERROR: " + e for e in errs), file=sys.stderr)
            return 1
        print(f"PASS: {len(md_files())} Markdown documents; required files, links, routes and vault reachability valid")
    elif args.cmd == "graph":
        report = graph_report()
        if args.output:
            target = (ROOT / args.output).resolve()
            if not target.is_relative_to(ROOT):
                parser.error("--output must stay within repository")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(report, encoding="utf-8")
            print(f"Generated {target.relative_to(ROOT)}")
        else:
            print(report, end="")
    elif args.cmd == "route":
        hits, paths = route(" ".join(args.task))
        print("Matched routes:", ", ".join(name for name, _ in hits) if hits else "fallback")
        for p in paths:
            print(p)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
