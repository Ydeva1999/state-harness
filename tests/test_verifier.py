import unittest
import tempfile
import shutil
import json
from pathlib import Path
from harness.verifier import audit_scorecard

class TestVerifier(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        self.source_file = self.test_dir / "sample.py"
        self.source_file.write_text(
            "import time\n"
            "def calculate(a, b):\n"
            "    # critical line\n"
            "    return a + b\n",
            encoding="utf-8"
        )

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_verifier_confirmed(self):
        scorecard_file = self.test_dir / "scorecard.json"
        scorecard_data = {
            "entity": "sample.py",
            "total_score": 5,
            "dimensions": {
                "correctness": {
                    "score": 5,
                    "line": 4,
                    "quote": "return a + b"
                }
            }
        }
        scorecard_file.write_text(json.dumps(scorecard_data), encoding="utf-8")

        status, notes = audit_scorecard(self.source_file, scorecard_file)
        self.assertEqual(status, "CONFIRMED")

    def test_verifier_arithmetic_mismatch(self):
        scorecard_file = self.test_dir / "scorecard_math_err.json"
        scorecard_data = {
            "entity": "sample.py",
            "total_score": 10, # Incorrect, should be 5
            "dimensions": {
                "correctness": {
                    "score": 5,
                    "line": 4,
                    "quote": "return a + b"
                }
            }
        }
        scorecard_file.write_text(json.dumps(scorecard_data), encoding="utf-8")

        status, notes = audit_scorecard(self.source_file, scorecard_file)
        self.assertEqual(status, "FLAGGED")
        self.assertIn("Arithmetic Mismatch", notes)

    def test_verifier_line_shift_flagged(self):
        scorecard_file = self.test_dir / "scorecard_shift.json"
        scorecard_data = {
            "entity": "sample.py",
            "total_score": 5,
            "dimensions": {
                "correctness": {
                    "score": 5,
                    "line": 2, # Line 2 is def calculate, not return
                    "quote": "return a + b"
                }
            }
        }
        scorecard_file.write_text(json.dumps(scorecard_data), encoding="utf-8")

        status, notes = audit_scorecard(self.source_file, scorecard_file)
        self.assertEqual(status, "FLAGGED")
        self.assertIn("Line Shift", notes)

if __name__ == "__main__":
    unittest.main()
