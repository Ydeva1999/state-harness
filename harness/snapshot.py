#!/usr/bin/env python3
"""
Automated Pre-Change Rollback Snapshot Utility.
Captures working directory state before high-risk changes and outputs 1-click restore scripts.
Zero dependencies. Pure Python standard library.
"""

import os
import sys
import shutil
import argparse
from pathlib import Path
from datetime import datetime

def create_snapshot(source_dir: Path, snapshot_name: str = None):
    src = source_dir.resolve()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    name = snapshot_name or f"snapshot_{timestamp}"
    
    snapshots_root = src / ".harness" / "snapshots"
    if not snapshots_root.parent.exists():
        snapshots_root = src / "snapshots"
    
    target_backup = snapshots_root / name
    target_backup.mkdir(parents=True, exist_ok=True)

    print(f"📦 Creating Pre-Change Snapshot: {name}")
    print(f"Target: {target_backup}")

    # Copy files excluding git, venv, and snapshots
    ignored_patterns = shutil.ignore_patterns(
        ".git", ".harness/snapshots", "snapshots", "__pycache__", "node_modules", "venv", ".venv"
    )

    for item in src.iterdir():
        if item.name in [".git", "snapshots", ".harness"]:
            continue
        dest = target_backup / item.name
        if item.is_dir():
            shutil.copytree(item, dest, ignore=ignored_patterns, dirs_exist_ok=True)
        else:
            shutil.copy2(item, dest)

    # Generate 1-click restore scripts
    restore_sh = target_backup / "restore.sh"
    restore_sh.write_text(
        f"#!/bin/bash\n"
        f"# 1-Click Rollback Script for {name}\n"
        f"echo 'Restoring baseline from {name}...'\n"
        f"cp -r \"$(dirname \"$0\")\"/* \"{src}\"/\n"
        f"echo 'Rollback complete.'\n",
        encoding="utf-8"
    )
    restore_sh.chmod(0o755)

    restore_ps1 = target_backup / "restore.ps1"
    restore_ps1.write_text(
        f"# 1-Click Rollback Script for {name}\n"
        f"Write-Host 'Restoring baseline from {name}...' -ForegroundColor Yellow\n"
        f"Copy-Item -Path \"$PSScriptRoot\\*\" -Destination \"{src}\" -Recurse -Force\n"
        f"Write-Host 'Rollback complete.' -ForegroundColor Green\n",
        encoding="utf-8"
    )

    manifest_file = target_backup / "MANIFEST.json"
    manifest_file.write_text(
        f"{{\n"
        f"  \"snapshot_name\": \"{name}\",\n"
        f"  \"created_at\": \"{datetime.now().isoformat()}\",\n"
        f"  \"source_directory\": \"{src}\"\n"
        f"}}\n",
        encoding="utf-8"
    )

    print(f"✅ Snapshot successfully saved at: {target_backup}")
    print("Includes 1-click restore scripts: restore.sh & restore.ps1")

def main():
    parser = argparse.ArgumentParser(description="Create a pre-change rollback snapshot.")
    parser.add_argument("--source", default=".", help="Source directory to snapshot")
    parser.add_argument("--name", default=None, help="Custom snapshot name")
    args = parser.parse_args()

    create_snapshot(Path(args.source), args.name)

if __name__ == "__main__":
    main()
