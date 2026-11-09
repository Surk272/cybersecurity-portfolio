from pathlib import Path
import sys

SOURCE_DIR = Path("app")

# Synthetic marker used only for this lab.
FORBIDDEN_MARKERS = [
    "LAB_HARDCODED_SECRET"
]

def main():
    findings = []

    for file_path in SOURCE_DIR.rglob("*.py"):
        content = file_path.read_text(encoding="utf-8")

        for marker in FORBIDDEN_MARKERS:
            if marker in content:
                findings.append(
                    f"Forbidden marker found in {file_path}"
                )

    if findings:
        print("SECURITY CHECK FAILED")

        for finding in findings:
            print(finding)

        sys.exit(1)

    print("SECURITY CHECK PASSED")


if __name__ == "__main__":
    main()