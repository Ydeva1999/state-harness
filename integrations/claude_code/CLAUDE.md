# Claude Code Harness Integration

Add this file to your repository root as `CLAUDE.md` to enforce harness engineering patterns in Claude Code.

## Project Invariants
* **Evidence Mandate:** Never assert code quality or correctness without citing verbatim source lines (`file.py#L10`).
* **Entity-as-a-Markdown-File:** Maintain long-term task state in `.harness/entities/` instead of relying on chat memory.
* **Pre-Change Safety:** Before editing critical configurations or core pipelines, execute:
  `python -m harness.snapshot --source .`
* **Zero-Token Delta Checking:** Before re-evaluating unchanged files, run:
  `python -m harness.delta_runner --target .`
* **Human Gate on Calibrations:** Never modify rules or memory without explicit user approval.
