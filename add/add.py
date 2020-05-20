def add(*matrices):
    """Adds corresponding numbers in lists-of-lists."""
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]
