"""Tests for Insert Interval. Run: pytest 05_intervals/test_insert_interval.py"""
import pytest

from insert_interval import Solution

@pytest.mark.parametrize("intervals, new_interval, expected", [
    ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
    ([], [5, 7], [[5, 7]]),
    ([[1, 5]], [2, 3], [[1, 5]]),
    ([[1, 5]], [6, 8], [[1, 5], [6, 8]]),
    ([[1, 5]], [0, 0], [[0, 0], [1, 5]]),
    ([[3, 5], [12, 15]], [6, 6], [[3, 5], [6, 6], [12, 15]]),
])
def test_insert(intervals, new_interval, expected):
    assert Solution().insert(intervals, new_interval) == expected

