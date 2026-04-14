"""Unit tests for banker logic."""

from __future__ import annotations

import unittest

from banker import compute_need, solve


class TestComputeNeed(unittest.TestCase):
    def test_basic(self) -> None:
        max_m = [[7, 5, 3], [3, 2, 2], [9, 0, 2]]
        alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2]]
        need = compute_need(max_m, alloc)
        self.assertEqual(need[0], [7, 4, 3])
        self.assertEqual(need[1], [1, 2, 2])
        self.assertEqual(need[2], [6, 0, 0])


class TestSolve(unittest.TestCase):
    def test_safe_two_processes_tiebreak_order(self) -> None:
        data = {
            "processes": 2,
            "resources": 2,
            "available": [3, 3],
            "max": [[1, 1], [1, 1]],
            "allocation": [[0, 0], [0, 0]],
        }
        out = solve(data)
        self.assertEqual(out["state"], "SAFE")
        self.assertEqual(out["safe_sequence"], ["P1", "P2"])

    def test_safe_single_process(self) -> None:
        data = {
            "processes": 1,
            "resources": 1,
            "available": [5],
            "max": [[2]],
            "allocation": [[0]],
        }
        self.assertEqual(solve(data)["safe_sequence"], ["P1"])

    def test_deadlock_pdf_matrix(self) -> None:
        data = {
            "processes": 3,
            "resources": 3,
            "available": [3, 3, 2],
            "max": [[7, 5, 3], [3, 2, 2], [9, 0, 2]],
            "allocation": [[0, 1, 0], [2, 0, 0], [3, 0, 2]],
        }
        out = solve(data)
        self.assertEqual(out["state"], "DEADLOCK")
        self.assertEqual(out["deadlocked_processes"], ["P1", "P3"])


if __name__ == "__main__":
    unittest.main()
