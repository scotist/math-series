"""Demonstrate fibonacci and lucas series."""


def fibonacci(n):
    """Return nth value in the fibonacci series."""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """Return nth value in the lucas series."""
    pass
