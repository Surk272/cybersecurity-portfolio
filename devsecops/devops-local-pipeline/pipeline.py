import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent


def run_step(name, command, working_dir=None):
    print(f"\n=== {name} ===")

    result = subprocess.run(command, check=False, cwd=str(working_dir) if working_dir else None)

    if result.returncode != 0:
        print(f"FAILED: {name}")
        sys.exit(result.returncode)

    print(f"PASSED: {name}")


def main():
    run_step(
        "UNIT TESTS",
        [sys.executable, "-m", "pytest", "-v"],
        working_dir=PROJECT_DIR,
    )

    run_step(
        "SECURITY CHECK",
        [sys.executable, str(PROJECT_DIR / "scripts" / "security_check.py")],
        working_dir=PROJECT_DIR,
    )

    artifacts = PROJECT_DIR / "artifacts"
    artifacts.mkdir(exist_ok=True)

    metadata = {
        "application": "payment-service",
        "build_status": "SUCCESS",
        "created_at": datetime.now(timezone.utc).isoformat()
    }

    metadata_path = artifacts / "build-metadata.json"

    metadata_path.write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8"
    )

    print("\nBUILD ARTIFACT CREATED")
    print(metadata_path)

    print("\nPIPELINE SUCCESSFUL")


if __name__ == "__main__":
    main()