def tail(sequence, n):
    """Returns the last n items of a given sequence."""
    if n <= 0:
        return []
    return list(sequence[-n:])
