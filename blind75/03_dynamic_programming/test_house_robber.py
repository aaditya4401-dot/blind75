"""Tests for House Robber. Run: pytest 03_dynamic_programming/test_house_robber.py"""
import pytest

from house_robber import Solution

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([5], 5),
    ([2, 1], 2),
    ([2, 1, 1, 2], 4),
    ([0, 0, 0], 0),
    ([100, 1, 1, 100], 200),
])
def test_rob(nums, expected):
    assert Solution().rob(nums) == expected

