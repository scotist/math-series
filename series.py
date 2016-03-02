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


if __name__ == "__main__":
    print(u"""
        This module defines functions that implement mathematical series.
        ...

        fibonacci(n):
            Returns the nth value in the fibonacci series

        >>> fibonacci(2)
        1

        lucas(n):
            Returns the nth value in the lucas series

        >>> lucas(5)
        7

        sum_series(case, x, y):
            Returns the nth value in an arbitrary series

        >>> sum_series(4, 3, 7)
        27

           """)
