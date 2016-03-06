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
    print(u""" This module defines functions that implement
        mathematical series.""")
    print(u"")
    print(u"")
    print(u"fibonacci(n):")
    print(fibonacci.__doc__)
    print(u"fibonacci(11) returns %s" % fibonacci(11))
    print(u"")
    print(u"lucas(n):")
    print(lucas.__doc__)
    print(u"lucas(17) returns %s" % lucas(17))
    print(u"")
    print(u"sum_series(n):")
    print(sum_series.__doc__)
    print(u"sum_series(9, x=7, y=21) returns %s" % sum_series(9, x=7, y=21))
