# Contributing Guidelines

Thank you for your interest in contributing to this project! We welcome community contributions, bug fixes, and architectural improvements.

---

## 1. Ground Rules & Code of Conduct

* **Zero Leaks:** Never commit credentials, private tokens, internal paths, or uncompiled binaries (`.pyc`, `__pycache__`).
* **Evidence-Grounded PRs:** Bug fixes must include a minimal reproduction test or script demonstrating the fix.
* **Deterministic Code:** Keep code modular, typed where appropriate, and thoroughly tested before opening a PR.

---

## 2. Getting Started

1. **Fork the Repository:** Create a personal fork on GitHub.
2. **Clone Locally:**
   ```bash
   git clone https://github.com/stateharness/state-harness.git
   cd state-harness
   ```
3. **Set Up Pre-Commit Hooks:**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

---

## 3. Development Workflow

1. Create a feature branch with a descriptive name:
   ```bash
   git checkout -b feat/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```
2. Make your changes adhering to existing project conventions.
3. Run local tests and verify zero regressions:
   ```bash
   python -m unittest discover tests/
   ```
4. Commit your changes with conventional commit messages:
   ```bash
   git commit -m "feat: add support for exponential backoff in client"
   ```

---

## 4. Submitting a Pull Request (PR)

1. Push your branch to your fork:
   ```bash
   git push origin feat/your-feature-name
   ```
2. Open a Pull Request against the `main` branch.
3. Clearly explain:
   * **What problem does this PR solve?**
   * **What changes were made?**
   * **How was it tested?**
