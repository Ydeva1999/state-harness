<div align="center">

# 🛡️ StateHarness
### The Zero-Dependency, State-Ledgered AI Agent Harness Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/stateharness/state-harness/actions/workflows/ci.yml/badge.svg)](https://github.com/stateharness/state-harness/actions/workflows/ci.yml)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9%2B-brightgreen.svg)](https://python.org)
[![Dependencies: Zero](https://img.shields.io/badge/Dependencies-Zero-orange.svg)](#)
[![Architecture: Sovereign](https://img.shields.io/badge/Architecture-State%20Harness-purple.svg)](#)

*Stop upgrading your AI model. Build an engineered harness instead.*

</div>

---

## 🏎️ The Core Thesis: The F1 Engine Analogy

In applied AI, whenever an agent hallucinates, drops constraints, or breaks a build, the default instinct is to wait for the next frontier LLM release.

**This is a mistake.** In Formula 1 racing, a faster engine alone does not win races. An engine without a chassis, telemetry, pit crew, and track limits crashes at high speed. 
* **The Model is only the Engine.**
* **The System around it is the Harness.**

$$\text{Production Reliability} = \text{Model (Engine)} + \text{Harness (Infrastructure)}$$

**StateHarness** is an ultra-lightweight, zero-dependency framework that transforms any probabilistic LLM into a deterministic, verifiable, and permanent engineering partner.

---

## 🧱 The 6 Architectural Layers

```
   ┌────────────────────────────────────────────────────────┐
   │             Layer 6: AUTOMATION (Scheduler / Cron)     │
   ├────────────────────────────────────────────────────────┤
   │             Layer 5: MEMORY (SHA-256 Ledger & Human)   │
   ├────────────────────────────────────────────────────────┤
   │             Layer 4: VERIFICATION (Judicial Subagent)  │
   ├────────────────────────────────────────────────────────┤
   │             Layer 3: OUTPUT (Codified Runbooks)        │
   ├────────────────────────────────────────────────────────┤
   │             Layer 2: TOOL ACCESS (Track Limits & ACI)  │
   ├────────────────────────────────────────────────────────┤
   │             Layer 1: CONTEXT (1-3-5 Rubrics & Bounds)  │
   ├────────────────────────────────────────────────────────┤
   │              🤖 CORE LLM (The Raw Engine)              │
   └────────────────────────────────────────────────────────┘
```

1. **Context & Rubrics:** Bounded 1-3-5 evaluation scales paired with the **Cardinal Evidence Mandate** (*"No verbatim source line citation = no assertion allowed"*).
2. **Tool Access & Track Limits:** Strict permission sandboxing and read-only inspection barriers.
3. **Output Codification:** Standardized Markdown schemas and executable runbooks that eliminate on-the-fly CLI trial-and-error.
4. **Independent Judicial Verification:** A decoupled, read-only verifier subagent with fresh context that audits exact line numbers and arithmetic (using the *"Confirmed"* protocol to avoid phantom nitpicks).
5. **Two-Tier Memory & State Caching:**
   * **Execution State Ledger:** Cryptographic SHA-256 hashes skip unchanged files in **0.03s consuming 0 tokens**.
   * **Supervised Calibration (`calibrate.md`):** Human-gated rule refinement that prevents autonomous self-improving prompt drift.
6. **Automation:** Scheduled headless execution triggers.

---

## 📂 Standard Directory Layout (`.harness/`)

```text
your-project/
  ├── .harness/
  │    ├── context/          # Layer 1: Contracts, specs, and 1-3-5 rubrics
  │    │    ├── spec.md
  │    │    └── rubric.md
  │    ├── entities/         # Layer 3 & 5: Markdown entity files (Durable state)
  │    │    └── <entity>.md
  │    ├── memory/           # Layer 5: State ledgers and calibration records
  │    │    ├── state.json   # Cryptographic SHA-256 delta cache
  │    │    └── calibrate.md # Human-approved rules
  │    ├── reports/          # Layer 3: Verified scorecards & audit summaries
  │    ├── verifier/         # Layer 4: Independent verification scripts
  │    └── snapshots/        # Layer 5: 1-click pre-change rollback archives
```

---

## ⚡ Quickstart in 60 Seconds

**StateHarness requires zero pip installations.** It runs on pure Python standard library (3.9+).

### 1. Initialize StateHarness in Your Repository
```bash
python -m harness.scaffold --target .
```

### 2. Run the Zero-Token Delta State Ledger
```bash
python -m harness.delta_runner --target .
```
*Checks your entities against cryptographic hashes. Unchanged files are verified in milliseconds at 0 LLM tokens.*

### 3. Run the Independent Judicial Verifier
```bash
python -m harness.verifier --source examples/resilient_http_client/client.py --scorecard examples/resilient_http_client/scorecard.json
```
*Catches off-by-one line shifts and verifies arithmetic independently.*

### 4. Create an Emergency Pre-Change Rollback Snapshot
```bash
python -m harness.snapshot --source . --name pre_major_refactor
```
*Generates an instant backup with 1-click restore scripts (`restore.sh` / `restore.ps1`).*

### 5. Run the Automated Test Suite
```bash
python -m unittest discover tests -v
```

### 6. Install as Local CLI Tool (Optional)
```bash
pip install -e .
# Now commands like state-harness-scaffold and state-harness-verify are globally available
```

---

## 📊 Empirical Validation: 509 Conversation Census

In a comprehensive census auditing **509 real-world AI coding sessions** across **67,277 tool calls**, unharnessed agent execution suffered from:
* **24.75% Zero-Verification Completions:** The agent declared tasks "Done" without running a single test.
* **1,410 Redundant File Reads:** Severe context bloat from re-reading unchanged files up to 12 times per session.
* **80.8% of Tool Failures from Uncodified CLI Guessing:** Improvising shell one-liners on the fly.

**StateHarness eliminates these failure modes completely** by externalizing state to disk and enforcing pre-execution verification gates.

---

## 🔌 Universal Agent Integrations

StateHarness is model-agnostic and agent-agnostic:
* **Antigravity / Gemini CLI:** Drop `integrations/antigravity/SKILL.md` into `~/.gemini/config/skills/`.
* **Claude Code:** Add `integrations/claude_code/CLAUDE.md` to your repository root.
* **OpenCode / Cursor / Cline:** Drop `integrations/opencode/AGENTS.md` into your project root.

---

## 🛡️ License

Distributed under the permissive [MIT License](LICENSE).
Built for sovereign developers and autonomous agent engineering.
