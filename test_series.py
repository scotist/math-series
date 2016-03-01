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
def test_fibonacci(n, result):
    """Test fibonacci function."""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('m, results', [(1, 2), (2, 1), (3, 3)])
def test_lucas(m, results):
    """Test lucas function."""
    from series import lucas
    assert lucas(m) == results


# @pytest.mark.parametrize('p, x, y', [(, x, y), ()])
def test_sum_series():
    """Test lucas function."""
    from series import sum_series
    assert sum_series(1) == 0
