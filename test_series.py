"""Test functions in series.py."""


def test_fibonacci_1():
    """Test fibonacci function."""
    from series import fibonacci
    assert fibonacci(1) == 0


def test_fibonacci_2():
    """Test fibonacci function."""
    from series import fibonacci
    assert fibonacci(2) == 1


def test_fibonacci_3():
    """Test fibonacci function."""
    from series import fibonacci
    assert fibonacci(7) == 8
