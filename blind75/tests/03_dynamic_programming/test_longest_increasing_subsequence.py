"""Tests for Longest Increasing Subsequence. Run: pytest 03_dynamic_programming/test_longest_increasing_subsequence.py"""
import pytest

from longest_increasing_subsequence import Solution

@pytest.mark.parametrize("nums, expected", [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1),
    ([1], 1),
    ([5, 4, 3, 2, 1], 1),
    ([1, 2, 3, 4, 5], 5),
    ([4, 10, 4, 3, 8, 9], 3),
])
def test_length_of_lis(nums, expected):
    assert Solution().lengthOfLIS(nums) == expected

