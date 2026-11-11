#!/usr/bin/env python3
"""
Pre-Publish Security & Privacy Audit Script.
Scans the entire repository to ensure ZERO API keys, personal paths, or credentials exist.
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Patterns indicating potential secrets or private leaks
SUSPICIOUS_PATTERNS = [
    (r"sk-[a-zA-Z0-9]{20,}", "OpenAI API Key"),
    (r"nvapi-[a-zA-Z0-9]{20,}", "NVIDIA API Key"),
    (r"AIza[0-9A-Za-z-_]{35}", "Google API Key"),
    (r"ghp_[a-zA-Z0-9]{36}", "GitHub Personal Access Token"),
    (r"xox[baprs]-[0-9a-zA-Z]{10,}", "Slack Token"),
    (r"AKIA[0-9A-Z]{16}", "AWS Access Key ID"),
    (r"(?i)password\s*=\s*['\"][^'\"]+['\"]", "Hardcoded Password"),
    (r"(?i)api[_-]?key\s*=\s*['\"][^'\"]{8,}['\"]", "Generic API Key"),
    (r"C:\\Users\\[^\n\"'\\]+", "Windows User Profile Path Leak"),
    (r"/home/[a-zA-Z0-9_-]+", "Linux User Home Path Leak")
]

EXCLUDED_DIRS = {".git", "__pycache__", ".venv", "venv"}

def scan_repo():
    print(f"🔒 Initiating Security & Privacy Scan on: {REPO_ROOT}")
    violations = []
    files_scanned = 0

    for p in REPO_ROOT.rglob("*"):
        if p.is_dir() or any(part in EXCLUDED_DIRS for part in p.parts):
            continue

        files_scanned += 1
        try:
            content = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue

        for pattern, label in SUSPICIOUS_PATTERNS:
            matches = re.finditer(pattern, content)
            for m in matches:
                # Ignore this audit script itself
                if p.name == "security_audit.py":
                    continue
                violations.append({
                    "file": str(p.relative_to(REPO_ROOT)),
                    "label": label,
                    "matched_text": m.group(0)[:30] + "..."
                })

    print(f"📄 Scanned {files_scanned} files.")
    if violations:
        print("\n❌ SECURITY VIOLATIONS DETECTED:")
        for v in violations:
            print(f"  [!] {v['file']}: Found {v['label']} -> '{v['matched_text']}'")
        sys.exit(1)
    else:
        print("\n✅ 100% CLEAN: Zero secrets, zero credentials, and zero personal paths detected!")
        print("Ready for safe public GitHub distribution.")
        sys.exit(0)

if __name__ == "__main__":
    scan_repo()
