"""Tests for Top K Frequent Elements. Run: pytest 08_heap/test_top_k_frequent_elements.py"""
import pytest

from top_k_frequent_elements import Solution

@pytest.mark.parametrize("nums, k, expected", [
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ([1], 1, [1]),
    ([1, 2], 2, [1, 2]),
    ([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2]),
    ([5, 5, 5, 5], 1, [5]),
    ([3, 0, 1, 0], 1, [0]),
])
def test_top_k_frequent(nums, k, expected):
    assert sorted(Solution().topKFrequent(nums, k)) == sorted(expected)

