"""Tests for Longest Consecutive Sequence. Run: pytest 04_graphs/test_longest_consecutive_sequence.py"""
import pytest

from longest_consecutive_sequence import Solution

@pytest.mark.parametrize("nums, expected", [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ([], 0),
    ([1], 1),
    ([1, 2, 0, 1], 3),
    ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7),
    ([-5, -4, -3], 3),
])
def test_longest_consecutive(nums, expected):
    assert Solution().longestConsecutive(nums) == expected

