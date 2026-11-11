# Supervised Calibration Memory

This document records architectural lessons and rubric refinements derived strictly from human engineer feedback.
An AI agent is strictly forbidden from unilaterally modifying, deleting, or inventing rules in this document without explicit human authorization.

## Protocol for Proposing Calibrations
1. **Friction Event:** The human engineer identifies a flaw or expresses dissatisfaction with an agent verdict.
2. **Root Cause Analysis:** The agent isolates the underlying structural ambiguity in the existing rubric or spec.
3. **Generalized Proposal:** The agent formulates an abstract rule update (avoiding overfitted one-off hacks).
4. **Human Gate:** The agent presents the proposed rule update to the engineer and halts execution.
5. **Durable Persistence:** Upon receiving explicit approval ("Approved" or "Yes"), the lesson is committed below.

---

## Active Calibrations & Refined Rules

### [YYYY-MM-DD]: [Rule Title / Domain]
* **Context / Trigger:** [What went wrong or was misunderstood]
* **Refined Rule:** [The exact operational invariant to follow in all future turns]
* **Approved By:** Human Lead Engineer
