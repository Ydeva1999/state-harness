---
name: harness-engineering
description: Production-grade AI Harness Engineering framework. Scaffolds and enforces deterministic, stateful, and verified agent workflows using markdown entity ledgers, strict 1-3-5 rubrics, evidence-grounded assertions ("No line citation, no claim"), hash-based zero-token delta caching, and independent judicial verifier subagents.
---

# Harness Engineering for Antigravity

Activate this skill when building multi-step pipelines, conducting rigorous code audits, refactoring, or managing state across long-horizon tasks.

## Quickstart
1. **Scaffold Harness:**
   ```powershell
   python -m harness.scaffold --target "."
   ```
2. **Run State Ledger:**
   ```powershell
   python -m harness.delta_runner --target "."
   ```
3. **Verify Scorecard:**
   ```powershell
   python -m harness.verifier --source "path/to/source.py" --scorecard "path/to/scorecard.json"
   ```
4. **Create Pre-Change Snapshot:**
   ```powershell
   python -m harness.snapshot --source "." --name "pre_refactor"
   ```
