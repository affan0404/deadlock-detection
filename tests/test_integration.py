"""Integration tests: main.py and sample JSON files."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


class TestMainCli(unittest.TestCase):
    def test_sample_safe_roundtrip(self) -> None:
        inp = ROOT / "samples" / "example_safe.json"
        proc = subprocess.run(
            [sys.executable, str(ROOT / "main.py"), str(inp)],
            capture_output=True,
            text=True,
            check=False,
            cwd=str(ROOT),
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        out = json.loads(proc.stdout)
        self.assertEqual(out["state"], "SAFE")
        self.assertEqual(out["safe_sequence"], ["P1", "P2"])

    def test_sample_deadlock(self) -> None:
        inp = ROOT / "samples" / "example_deadlock.json"
        proc = subprocess.run(
            [sys.executable, str(ROOT / "main.py"), str(inp)],
            capture_output=True,
            text=True,
            check=False,
            cwd=str(ROOT),
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        out = json.loads(proc.stdout)
        self.assertEqual(out["state"], "DEADLOCK")


if __name__ == "__main__":
    unittest.main()
