# Deadlock detection (Banker's safety) - COMP 3300

## Run

```bash
python3 main.py samples/example_safe.json
python3 main.py samples/example_deadlock.json
```

On Windows, if `python3` is not on PATH:

```text
py -3 main.py samples/example_safe.json
```

## Input / output

Input JSON fields: `processes`, `resources`, `available`, `max`, `allocation` (see `samples/`).

- **SAFE:** `{"state":"SAFE","safe_sequence":["P1",...]}` - completion order from the safety algorithm.
- **DEADLOCK:** `{"state":"DEADLOCK","deadlocked_processes":["P1",...]}` - processes still unfinished when no process can proceed; listed in increasing process index.

## Design

- **Need matrix:** `need[i][j] = max[i][j] - allocation[i][j]`.
- **Safety check:** Banker's algorithm: repeatedly pick the smallest-index process `i` with `need[i] <= work` (component-wise), add `allocation[i]` to `work`, mark finished, until all finish (SAFE) or no progress (DEADLOCK).
- **Tie-breaking:** Among processes that can run in a step, scan `i = 0 .. n-1` and pick the first (**smallest process index first**).

## AI usage statement

Course policy: describe how AI tools were used. You must understand all submitted code.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

(Run from this project directory.)
