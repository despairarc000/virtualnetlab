import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("knowledge", ROOT / "tools/knowledge.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class KnowledgeTests(unittest.TestCase):
    def test_required_files_and_links(self):
        self.assertEqual(mod.doctor(), [])

    def test_route_engine(self):
        hits, paths = mod.route("implement deterministic scheduler engine")
        self.assertTrue(any(name == "engine" for name, _ in hits))
        self.assertIn("IDEA_PLAN.md", paths)
        self.assertTrue(any("ADR-0001" in p for p in paths))
        self.assertEqual(len(paths), len(set(paths)))

    def test_architecture_route(self):
        hits, paths = mod.route("architecture risk decision review")
        self.assertIn(("architecture", 3), hits)
        self.assertIn("architecture/ARCHITECTURE_REVIEW.md", paths)
        self.assertIn("architecture/RISK_REGISTER.md", paths)

    def test_phase1_route(self):
        hits, paths = mod.route("phase1 planning before coding")
        self.assertTrue(any(name == "phase1" for name, _ in hits))
        self.assertIn("phase1/PHASE1_MASTER_PLAN.md", paths)
        self.assertIn("phase1/EXIT_AUDIT.md", paths)
        self.assertEqual(len(paths), len(set(paths)))

    def test_phase1_deep_routes(self):
        tests = [
            ("Filius gpl reuse", "phase1/research/FILIUS_REUSE_AUDIT.md"),
            ("WAN LAN bridge port", "phase1/DEVICE_AND_INTERFACE_MODEL.md"),
            ("event scheduler replay", "phase1/EVENT_ENGINE_CONTRACT.md"),
            ("DHCP IPv4LL RFC", "phase1/STANDARDS_TEST_VECTORS.md"),
        ]
        for query, expected in tests:
            with self.subTest(query=query):
                _, paths = mod.route(query)
                self.assertIn(expected, paths)
                self.assertEqual(len(paths), len(set(paths)))

    def test_top_down_routes_and_reachability(self):
        queries = [
            ("mission user journey", "phase1/TOP_DOWN_CAPABILITY_MAP.md"),
            ("stack forwarding pipeline", "phase1/NETWORK_STACK_DECOMPOSITION.md"),
            ("device profile wifi", "phase1/DEVICE_CAPABILITY_CATALOG.md"),
            ("assessment learning", "phase1/DIAGNOSTICS_AND_EDUCATION.md"),
            ("save import migration", "phase1/PERSISTENCE_AND_COMPATIBILITY.md"),
            ("cross-layer contradictions audit", "phase1/CROSS_LAYER_GAPS.md"),
        ]
        for query, expected in queries:
            with self.subTest(query=query):
                _, paths = mod.route(query)
                self.assertIn(expected, paths)
        self.assertEqual(mod.doctor(), [])

    def test_protocol_route(self):
        _, paths = mod.route("fix dhcp wan switch")
        self.assertTrue(any("LAB_ACCEPTANCE" in p for p in paths))

    def test_broken_link_detected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "README.md").write_text("[missing](missing.md)", encoding="utf-8")
            errs = mod.doctor(root)
            self.assertTrue(any("Broken local link" in e for e in errs))

    def test_rendered_graph(self):
        report = mod.graph_report()
        self.assertIn("Graphify derived relationships", report)
        self.assertIn("| From | To | Type |", report)
        self.assertNotIn("\\`", report)

    def test_graph_edges_stable(self):
        a = mod.graph_edges()
        self.assertEqual(a, sorted(a))
        self.assertTrue(any(e[2] == "doc-link" for e in a))


if __name__ == "__main__":
    unittest.main()
