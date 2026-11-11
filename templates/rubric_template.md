# [Domain Name] Evaluation Rubric

## Objective
Evaluate candidate implementations, PRs, or artifacts against non-negotiable architectural requirements.

## Bounded Scoring Scale (1, 3, 5)
Every dimension MUST be scored strictly as **1**, **3**, or **5**. No intermediate or subjective scores.

### 1. Dimension One: [e.g., Error Handling & Resiliency]
* **5 (Production-Ready):** Comprehensive error handling with typed exceptions, structured telemetry, and zero unhandled failure modes.
* **3 (Partial / Deficient):** Basic error handling present, but misses edge cases, uses generic catch blocks, or leaks internal state.
* **1 (Failure / Dangerous):** Bare `except: pass`, swallowed errors, or missing validation.

### 2. Dimension Two: [e.g., Concurrency & State Safety]
* **5 (Production-Ready):** Explicit bounded concurrency (Semaphores / Queues) and thread-safe / task-safe mutable state.
* **3 (Partial / Deficient):** Unbounded concurrency or incomplete lock coverage.
* **1 (Failure / Dangerous):** Unsynchronized shared mutations or blocking calls inside async loops.

### 3. Dimension Three: [e.g., Resource Lifecycle & Leaks]
* **5 (Production-Ready):** Implements context managers (`__enter__`/`__exit__` or `__aenter__`/`__aexit__`) guaranteeing zero leaks on exceptions.
* **3 (Partial / Deficient):** Requires manual `.close()` calls; vulnerable to connection leaks on aborts.
* **1 (Failure / Dangerous):** Completely unmanaged resources left open indefinitely.

---

## ⛔ CARDINAL EVIDENCE MANDATE
> **NO VERBATIM SOURCE CITATION = NO SCORE ALLOWED.**  
> Every finding or grade MUST cite the exact, clickable line number (`file.py#L42-L55`) and the verbatim snippet proving the evaluation. If an assertion lacks verbatim proof, the score defaults to 1.
