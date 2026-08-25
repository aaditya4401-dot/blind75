"""Tests for Find Minimum in Rotated Sorted Array. Run: pytest 01_arrays/test_find_minimum_in_rotated_sorted_array.py"""
import pytest

from find_minimum_in_rotated_sorted_array import Solution

@pytest.mark.parametrize("nums, expected", [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([11, 13, 15, 17], 11),
    ([1], 1),
    ([2, 1], 1),
    ([5, 1, 2, 3, 4], 1),
])
def test_find_min(nums, expected):
    assert Solution().findMin(nums) == expected

