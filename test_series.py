"""Test functions in series.py."""
import pytest


def test_fibonacci_1():
    """Test fibonacci function."""
    from series import fibonacci
    assert fibonacci(1) == 0


def test_fibonacci_2():
    """Test fibonacci function."""
    from series import fibonacci
    assert fibonacci(2) == 1


@pytest.mark.parametrize('n, result', [(1, 0), (2, 1), (3, 1)])
def test_fibonacci_3(n, result):
    """Test fibonacci function."""
    from series import fibonacci
    assert fibonacci(n) == result
