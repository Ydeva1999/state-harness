#!/usr/bin/env python3
"""
Scaffold a StateHarness directory structure in any target project.
Zero dependencies. Pure Python standard library.
"""

import os
import sys
import json
import argparse
from pathlib import Path

def scaffold_project(target_dir: Path, harness_dir_name: str = ".harness"):
    root = target_dir.resolve()
    harness_path = root / harness_dir_name

    subdirs = [
        harness_path / "context",
        harness_path / "entities",
        harness_path / "memory",
        harness_path / "reports",
        harness_path / "verifier",
        harness_path / "snapshots",
    ]

    for d in subdirs:
        d.mkdir(parents=True, exist_ok=True)

    # 1. Initialize context/spec.md
    spec_file = harness_path / "context" / "spec.md"
    if not spec_file.exists():
        spec_file.write_text(
            "# Project Specification & Invariants\n\n"
            "## Objective\n"
            "Describe the high-level objective and architectural boundaries of this system.\n\n"
            "## Non-Negotiable Invariants\n"
            "1. **Safety:** What must NEVER happen.\n"
            "2. **Correctness:** What criteria constitute a pass.\n"
            "3. **Scope:** Files and subsystems allowed to be modified.\n",
            encoding="utf-8"
        )

    # 2. Initialize context/rubric.md
    rubric_file = harness_path / "context" / "rubric.md"
    if not rubric_file.exists():
        rubric_file.write_text(
            "# Deterministic Evaluation Rubric\n\n"
            "## 1-3-5 Scoring Scale\n"
            "* **5 (Production-Ready):** 100% compliant with zero technical debt.\n"
            "* **3 (Partial / Deficient):** Functional, but carries structural debt or missing edge cases.\n"
            "* **1 (Dangerous / Failure):** Violates core invariants, missing security checks, or crashing.\n\n"
            "## ⛔ Cardinal Evidence Mandate\n"
            "> **NO VERBATIM SOURCE CITATION = NO SCORE ALLOWED.**\n"
            "Every score awarded MUST cite the exact line number (`file.py#L42`) and verbatim quote.\n",
            encoding="utf-8"
        )

    # 3. Initialize memory/state.json
    state_file = harness_path / "memory" / "state.json"
    if not state_file.exists():
        initial_state = {
            "version": "1.0.0",
            "last_run": None,
            "entities": {}
        }
        state_file.write_text(json.dumps(initial_state, indent=2), encoding="utf-8")

    # 4. Initialize memory/calibrate.md
    cal_file = harness_path / "memory" / "calibrate.md"
    if not cal_file.exists():
        cal_file.write_text(
            "# Supervised Calibration Memory\n\n"
            "Lessons and refined rubric rules explicitly approved by the human engineer.\n"
            "An AI agent must NEVER unilaterally mutate this file without explicit human sign-off.\n\n"
            "## Active Lessons & Calibrations\n",
            encoding="utf-8"
        )

    print(f"✅ Successfully initialized StateHarness at: {harness_path}")
    print("Created directory structure:")
    print("  ├── context/          (Contracts, specs, and 1-3-5 rubrics)")
    print("  ├── entities/         (Durable Markdown entity files)")
    print("  ├── memory/           (Cryptographic state ledger & calibration log)")
    print("  ├── reports/          (Deterministic audit & verification reports)")
    print("  ├── verifier/         (Read-only validation scripts)")
    print("  └── snapshots/        (Pre-change 1-click restore points)")

def main():
    parser = argparse.ArgumentParser(description="Bootstrap a StateHarness in your project.")
    parser.add_argument("--target", default=".", help="Target project root directory (default: current directory)")
    parser.add_argument("--name", default=".harness", help="Name of harness directory (default: .harness, or .agy)")
    args = parser.parse_args()

    scaffold_project(Path(args.target), args.name)

if __name__ == "__main__":
    main()
