# Package contents

| File | Role |
|------|------|
| `main.py` | Load JSON, validate, call `banker.solve`, print JSON |
| `validation.py` | Dimension and value checks |
| `banker.py` | Must implement `solve(data) -> dict` |

## Run

Requires a working `banker.solve` implementation.

```bash
python3 main.py path/to/input.json
```
