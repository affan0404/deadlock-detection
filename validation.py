"""Input validation for Banker's simulator."""


def validate_input(data: dict) -> None:
    """Raise ValueError with a clear message if input is inconsistent."""
    required = ("processes", "resources", "available", "max", "allocation")
    for key in required:
        if key not in data:
            raise ValueError(f"missing key: {key}")

    n = data["processes"]
    m = data["resources"]

    if not isinstance(n, int) or n < 1:
        raise ValueError("processes must be a positive integer")
    if not isinstance(m, int) or m < 1:
        raise ValueError("resources must be a positive integer")

    avail = data["available"]
    if not isinstance(avail, list) or len(avail) != m:
        raise ValueError("available must be a list of length resources")
    for x in avail:
        if not isinstance(x, int) or x < 0:
            raise ValueError("available entries must be non-negative integers")

    max_m = data["max"]
    alloc = data["allocation"]

    if not isinstance(max_m, list) or len(max_m) != n:
        raise ValueError("max must have processes rows")
    if not isinstance(alloc, list) or len(alloc) != n:
        raise ValueError("allocation must have processes rows")

    for row in max_m:
        if not isinstance(row, list) or len(row) != m:
            raise ValueError("each max row must have length resources")
        for x in row:
            if not isinstance(x, int) or x < 0:
                raise ValueError("max entries must be non-negative integers")

    for row in alloc:
        if not isinstance(row, list) or len(row) != m:
            raise ValueError("each allocation row must have length resources")
        for x in row:
            if not isinstance(x, int) or x < 0:
                raise ValueError("allocation entries must be non-negative integers")

    for i in range(n):
        for j in range(m):
            if alloc[i][j] > max_m[i][j]:
                raise ValueError(
                    f"allocation[{i}][{j}] exceeds max[{i}][{j}] for that process"
                )
