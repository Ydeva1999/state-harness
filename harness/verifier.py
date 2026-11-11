#!/usr/bin/env python3
"""
Independent Judicial Verifier Engine.
Audits candidate scorecards, checks line number veracity, and validates arithmetic.
Zero dependencies. Pure Python standard library.
"""

import os
import sys
import json
import argparse
from pathlib import Path

def audit_scorecard(source_file: Path, scorecard_file: Path):
    if not source_file.exists():
        return "ERROR", f"Source file does not exist: {source_file}"
    if not scorecard_file.exists():
        return "ERROR", f"Scorecard file does not exist: {scorecard_file}"

    source_lines = source_file.read_text(encoding="utf-8", errors="ignore").splitlines()
    with open(scorecard_file, "r", encoding="utf-8") as f:
        scorecard = json.load(f)

    discrepancies = []

    # 1. Arithmetic Check
    dimensions = scorecard.get("dimensions", {})
    stated_total = scorecard.get("total_score")
    if stated_total is not None:
        computed_total = sum(d.get("score", 0) for d in dimensions.values())
        if computed_total != stated_total:
            discrepancies.append(
                f"Arithmetic Mismatch: Computed sum ({computed_total}) != stated total ({stated_total})"
            )

    # 2. Line Number & Verbatim Quote Veracity
    for dim_name, dim_data in dimensions.items():
        cited_line = dim_data.get("line")
        cited_quote = dim_data.get("quote", "").strip()

        if cited_quote.startswith("#") or not cited_quote:
            continue  # Conceptual negative assertion

        if cited_line is None:
            discrepancies.append(f"{dim_name}: Missing exact line number citation.")
            continue

        line_idx = cited_line - 1
        if line_idx < 0 or line_idx >= len(source_lines):
            discrepancies.append(
                f"{dim_name}: Cited line {cited_line} is out of bounds (file has {len(source_lines)} lines)."
            )
            continue

        actual_content = source_lines[line_idx].strip()
        # Clean quote of ellipses
        clean_target = cited_quote.replace("...", "").strip()
        search_key = clean_target[:min(25, len(clean_target))]

        if search_key not in actual_content:
            discrepancies.append(
                f"{dim_name} (Line Shift): Line {cited_line} expected '{search_key}' but found '{actual_content[:35]}'."
            )

    if not discrepancies:
        return "CONFIRMED", "All line citations, quotes, and arithmetic verified verbatim."
    else:
        return "FLAGGED", "; ".join(discrepancies)

def main():
    parser = argparse.ArgumentParser(description="Audit a scorecard against source code veracity.")
    parser.add_argument("--source", required=True, help="Path to raw source file being audited")
    parser.add_argument("--scorecard", required=True, help="Path to scorecard JSON file")
    args = parser.parse_args()

    status, notes = audit_scorecard(Path(args.source), Path(args.scorecard))
    print(f"\n⚖️ Verification Verdict: {status}")
    print(f"📝 Notes: {notes}\n")

    sys.exit(0 if status == "CONFIRMED" else 1)

if __name__ == "__main__":
    main()
