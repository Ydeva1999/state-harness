import unittest
import tempfile
import shutil
import json
from pathlib import Path
from harness.scaffold import scaffold_project
from harness.delta_runner import evaluate_deltas, compute_sha256

class TestDeltaRunner(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        scaffold_project(self.test_dir, ".harness")
        self.entities_dir = self.test_dir / ".harness" / "entities"

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_delta_detection_and_sync(self):
        # 1. Add an entity
        entity_file = self.entities_dir / "user_auth.md"
        entity_file.write_text("# User Auth Spec", encoding="utf-8")

        # 2. Evaluate deltas before sync
        res = evaluate_deltas(self.test_dir, ".harness", auto_sync=False)
        self.assertEqual(len(res["pending"]), 1)
        self.assertEqual(len(res["cached"]), 0)
        self.assertEqual(res["pending"][0][0], "user_auth.md")

        # 3. Evaluate with auto_sync=True
        res_sync = evaluate_deltas(self.test_dir, ".harness", auto_sync=True)
        self.assertEqual(len(res_sync["pending"]), 1)

        # 4. Immediate re-run should report cached (0 tokens)
        res_cached = evaluate_deltas(self.test_dir, ".harness", auto_sync=False)
        self.assertEqual(len(res_cached["cached"]), 1)
        self.assertEqual(len(res_cached["pending"]), 0)

    def test_sha256_stability(self):
        sample_file = self.test_dir / "test.txt"
        sample_file.write_text("Deterministic content", encoding="utf-8")
        hash1 = compute_sha256(sample_file)
        hash2 = compute_sha256(sample_file)
        self.assertEqual(hash1, hash2)

if __name__ == "__main__":
    unittest.main()
