#!/usr/bin/env python3
"""
Cryptographic SHA-256 Delta State Ledger.
Skips unchanged entities in milliseconds at 0 LLM tokens.
Zero dependencies. Pure Python standard library.
"""

import os
import sys
import json
import hashlib
import argparse
from pathlib import Path
from datetime import datetime

def compute_sha256(filepath: Path) -> str:
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()

def evaluate_deltas(target_dir: Path, harness_dir_name: str = ".harness", auto_sync: bool = False):
    root = target_dir.resolve()
    harness_path = root / harness_dir_name
    memory_file = harness_path / "memory" / "state.json"
    entities_dir = harness_path / "entities"

    if not memory_file.exists():
        print(f"❌ Error: state.json not found at {memory_file}.")
        print("Please run `python -m harness.scaffold` first.")
        sys.exit(1)

    with open(memory_file, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    registered_entities = ledger.get("entities", {})
    entity_files = list(entities_dir.glob("*.md"))

    cached = []
    pending = []

    for ef in sorted(entity_files):
        fname = ef.name
        current_hash = compute_sha256(ef)

        if fname in registered_entities and registered_entities[fname].get("hash") == current_hash:
            cached.append(fname)
        else:
            pending.append((fname, current_hash))
            if auto_sync:
                registered_entities[fname] = {
                    "hash": current_hash,
                    "status": "PENDING_VERIFICATION",
                    "updated_at": datetime.now().isoformat()
                }

    print(f"\n📊 [StateHarness Delta Ledger] Status for {harness_path.name}:")
    print(f"  ⏩ Cached / Unchanged: {len(cached)} entities (0 tokens consumed)")
    print(f"  🔍 Modified / New:     {len(pending)} entities requiring evaluation\n")

    if pending:
        print("Pending Entities:")
        for item, h in pending:
            print(f"  - {item} (SHA: {h[:8]}...)")

    if auto_sync and pending:
        ledger["last_run"] = datetime.now().isoformat()
        ledger["entities"] = registered_entities
        with open(memory_file, "w", encoding="utf-8") as f:
            json.dump(ledger, f, indent=2)
        print("\n💾 State ledger automatically synchronized.")

    return {
        "cached": cached,
        "pending": pending,
        "total": len(entity_files)
    }

def main():
    parser = argparse.ArgumentParser(description="Run the StateHarness Delta State Runner.")
    parser.add_argument("--target", default=".", help="Target project root directory")
    parser.add_argument("--name", default=".harness", help="Name of harness directory (.harness or .agy)")
    parser.add_argument("--sync", action="store_true", help="Auto-sync modified hashes into state ledger")
    args = parser.parse_args()

    evaluate_deltas(Path(args.target), args.name, args.sync)

if __name__ == "__main__":
    main()
