import unittest
import tempfile
import shutil
from pathlib import Path
from harness.snapshot import create_snapshot

class TestSnapshot(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        (self.test_dir / "app.py").write_text("print('hello')", encoding="utf-8")
        (self.test_dir / "data.json").write_text("{}", encoding="utf-8")

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_create_snapshot_artifacts(self):
        create_snapshot(self.test_dir, "test_backup_01")
        backup_path = self.test_dir / "snapshots" / "test_backup_01"

        self.assertTrue(backup_path.exists())
        self.assertTrue((backup_path / "app.py").exists())
        self.assertTrue((backup_path / "data.json").exists())
        self.assertTrue((backup_path / "restore.sh").exists())
        self.assertTrue((backup_path / "restore.ps1").exists())
        self.assertTrue((backup_path / "MANIFEST.json").exists())

if __name__ == "__main__":
    unittest.main()
