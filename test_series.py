"""Test functions in series.py."""
import pytest


@pytest.mark.parametrize('n, result', [(1, 0), (2, 1), (3, 1)])
def test_fibonacci(n, result):
    """Test fibonacci function."""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('m, result', [(1, 2), (2, 1), (3, 3)])
def test_lucas(m, result):
    """Test lucas function."""
    from series import lucas
    assert lucas(m) == result


@pytest.mark.parametrize('case, x, y, result', [(4, 3, 7, 27), (5, 4, 6, 42)])
def test_sum_series(case, x, y, result):
    """Test the sum of a series given it's 1st and 2nd cases."""
    from series import sum_series
    assert sum_series(case, x, y) == result
