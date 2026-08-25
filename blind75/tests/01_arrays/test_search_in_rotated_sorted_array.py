"""Tests for Search in Rotated Sorted Array. Run: pytest 01_arrays/test_search_in_rotated_sorted_array.py"""
import pytest

from search_in_rotated_sorted_array import Solution

@pytest.mark.parametrize("nums, target, expected", [
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ([1], 0, -1),
    ([1], 1, 0),
    ([3, 1], 1, 1),
    ([5, 1, 3], 3, 2),
    ([1, 2, 3, 4, 5], 5, 4),
])
def test_search(nums, target, expected):
    assert Solution().search(nums, target) == expected

