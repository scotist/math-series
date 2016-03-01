"""Demonstrate fibonacci and lucas series."""


def fibonacci(n):
    """Return nth value in the fibonacci series."""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(m):
    """Return nth value in the lucas series."""
    if m == 1:
        return 2
    elif m == 2:
        return 1
    else:
        return lucas(m - 1) + lucas(m - 2)


def sum_series(case, x=0, y=1):
    """Return nth value in some random series."""
    if case == 0:
        return x
    elif case == 1:
        return y
    else:
        return sum_series(case - 1, x, y) + sum_series(case - 2, x, y)
