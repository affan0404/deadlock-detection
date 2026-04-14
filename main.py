#!/usr/bin/env python3
"""
CLI and JSON I/O.

Usage: python3 main.py input.json > output.json
"""

from __future__ import annotations

import json
import sys

from banker import solve
from validation import validate_input


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py input.json", file=sys.stderr)
        sys.exit(2)
    path = sys.argv[1]
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except OSError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"invalid JSON: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        validate_input(data)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

    out = solve(data)
    print(json.dumps(out, separators=(",", ":")))


if __name__ == "__main__":
    main()
