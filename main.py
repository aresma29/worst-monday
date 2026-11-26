"""Print the Worst Monday one-liner from entry.txt, byte for byte.

The entry file is resolved relative to this script, so the program
works from any working directory, even on a read-only filesystem.
"""
from pathlib import Path
import sys


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    text = entry_path.read_text(encoding="utf-8")
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
