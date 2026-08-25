"""Tests for House Robber II. Run: pytest 03_dynamic_programming/test_house_robber_ii.py"""
import pytest

from house_robber_ii import Solution

@pytest.mark.parametrize("nums, expected", [
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4),
    ([1, 2, 3], 3),
    ([5], 5),
    ([1, 2], 2),
    ([200, 3, 140, 20, 10], 340),
    ([0, 0], 0),
])
def test_rob_circular(nums, expected):
    assert Solution().rob(nums) == expected

