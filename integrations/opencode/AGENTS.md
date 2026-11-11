# OpenCode & Cursor Agent Harness Integration

Place this file in your workspace root as `AGENTS.md` (or `.cursorrules`).

## Execution Protocols
1. **Deterministic 1-3-5 Rubrics:** Evaluate code using bounded scoring (`.harness/context/rubric.md`).
2. **Independent Verification:** Run verification checks via `python -m harness.verifier` before declaring completion.
3. **Rollback Assurance:** Always create a snapshot via `python -m harness.snapshot` prior to multi-file refactoring.
