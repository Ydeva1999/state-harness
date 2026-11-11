import unittest
import tempfile
import shutil
from pathlib import Path
from harness.scaffold import scaffold_project

class TestScaffold(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_scaffold_default_structure(self):
        scaffold_project(self.test_dir, ".harness")
        harness_path = self.test_dir / ".harness"

        self.assertTrue(harness_path.exists())
        self.assertTrue((harness_path / "context" / "spec.md").exists())
        self.assertTrue((harness_path / "context" / "rubric.md").exists())
        self.assertTrue((harness_path / "memory" / "state.json").exists())
        self.assertTrue((harness_path / "memory" / "calibrate.md").exists())
        self.assertTrue((harness_path / "entities").is_dir())
        self.assertTrue((harness_path / "reports").is_dir())
        self.assertTrue((harness_path / "verifier").is_dir())
        self.assertTrue((harness_path / "snapshots").is_dir())

    def test_scaffold_custom_name(self):
        scaffold_project(self.test_dir, ".agy")
        agy_path = self.test_dir / ".agy"
        self.assertTrue(agy_path.exists())
        self.assertTrue((agy_path / "context" / "spec.md").exists())

if __name__ == "__main__":
    unittest.main()
