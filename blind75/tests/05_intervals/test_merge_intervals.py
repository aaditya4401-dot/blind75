"""Tests for Merge Intervals. Run: pytest 05_intervals/test_merge_intervals.py"""
import pytest

from merge_intervals import Solution

@pytest.mark.parametrize("intervals, expected", [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]]),
    ([[1, 4], [0, 4]], [[0, 4]]),
    ([[1, 4], [2, 3]], [[1, 4]]),
    ([[1, 1]], [[1, 1]]),
    ([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]], [[1, 10]]),
    ([[5, 6], [1, 2]], [[1, 2], [5, 6]]),
])
def test_merge(intervals, expected):
    assert Solution().merge(intervals) == expected

