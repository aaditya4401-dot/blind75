"""Tests for Sum of Two Integers. Run: pytest 02_binary/test_sum_of_two_integers.py"""
import pytest

from sum_of_two_integers import Solution

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (-2, -3, -5),
    (5, -3, 2),
    (-1000, 1000, 0),
    (1000, 1000, 2000),
])
def test_get_sum(a, b, expected):
    assert Solution().getSum(a, b) == expected

