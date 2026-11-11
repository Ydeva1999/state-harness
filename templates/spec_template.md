# Specification: [System or Module Name]

## 1. Executive Objective
State in 1-2 paragraphs the exact operational outcome this module or task achieves.

## 2. Hard Invariants (What Must NEVER Break)
1. **Invariant 1:** [e.g., Under no circumstances may auth tokens be logged in plain text.]
2. **Invariant 2:** [e.g., Max retry count must never exceed 5 to prevent thundering herds.]
3. **Invariant 3:** [e.g., Database connections must release within 5000ms.]

## 3. Interfaces & Contracts
* **Inputs:** [Types, shapes, schemas]
* **Outputs:** [Deterministic return signatures]
* **External Dependencies:** [Permitted libraries; forbid unapproved bloat]

## 4. Negative Exemplars (When NOT to Emulate)
* *Do NOT introduce heavy third-party frameworks for trivial helpers.*
* *Do NOT copy stylistic formatting from legacy files if they violate modern standards.*
