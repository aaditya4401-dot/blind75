"""Tests for Non-overlapping Intervals. Run: pytest 05_intervals/test_non_overlapping_intervals.py"""
import pytest

from non_overlapping_intervals import Solution

@pytest.mark.parametrize("intervals, expected", [
    ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
    ([[1, 2], [1, 2], [1, 2]], 2),
    ([[1, 2], [2, 3]], 0),
    ([[1, 100], [11, 22], [1, 11], [2, 12]], 2),
    ([[1, 2]], 0),
    ([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]], 2),
])
def test_erase_overlap_intervals(intervals, expected):
    assert Solution().eraseOverlapIntervals(intervals) == expected

