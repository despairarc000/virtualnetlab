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

    def test_protocol_route(self):
        _, paths = mod.route("fix dhcp wan switch")
        self.assertTrue(any("LAB_ACCEPTANCE" in p for p in paths))

    def test_broken_link_detected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "README.md").write_text("[missing](missing.md)", encoding="utf-8")
            errs = mod.doctor(root)
            self.assertTrue(any("Broken local link" in e for e in errs))

    def test_graph_edges_stable(self):
        a = mod.graph_edges()
        self.assertEqual(a, sorted(a))
        self.assertTrue(any(e[2] == "doc-link" for e in a))


if __name__ == "__main__":
    unittest.main()
