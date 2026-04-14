"""
Banker's need matrix and safety algorithm.

Tie-breaking: when several processes can proceed, pick the smallest process index first.
Process labels in output: P1 .. Pn (row index i maps to Pi+1).
"""

from __future__ import annotations


def compute_need(max_m: list[list[int]], allocation: list[list[int]]) -> list[list[int]]:
    n = len(max_m)
    m = len(max_m[0]) if n else 0
    return [[max_m[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]


def _pid(i: int) -> str:
    return f"P{i + 1}"


def solve(data: dict) -> dict:
    """
    Return spec-shaped dict: SAFE + safe_sequence, or DEADLOCK + deadlocked_processes.

    Unsafe branch (deadlocked list): processes that remain unfinished after the
    safety simulation, sorted by increasing index (smallest Pi first).
    """
    n = data["processes"]
    m = data["resources"]
    available = list(data["available"])
    max_m = data["max"]
    allocation = data["allocation"]

    need = compute_need(max_m, allocation)

    for i in range(n):
        for j in range(m):
            if need[i][j] < 0:
                raise ValueError("invalid state: negative need")

    work = available[:]
    finish = [False] * n
    sequence_indices: list[int] = []

    while True:
        progressed = False
        # Try processes in index order 0..n-1; first satisfiable wins this round
        for i in range(n):
            if finish[i]:
                continue
            if all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += allocation[i][j]
                finish[i] = True
                sequence_indices.append(i)
                progressed = True
                break
        if not progressed:
            break

    if all(finish):
        return {
            "state": "SAFE",
            "safe_sequence": [_pid(i) for i in sequence_indices],
        }

    deadlocked = [_pid(i) for i in range(n) if not finish[i]]
    return {
        "state": "DEADLOCK",
        "deadlocked_processes": deadlocked,
    }
