"""Tests for Combination Sum IV. Run: pytest 03_dynamic_programming/test_combination_sum_iv.py"""
import pytest

from combination_sum_iv import Solution

@pytest.mark.parametrize("nums, target, expected", [
    ([1, 2, 3], 4, 7),
    ([9], 3, 0),
    ([1, 2, 3], 32, 181997601),
    ([2, 3], 7, 3),
    ([1], 5, 1),
    ([4, 2, 1], 32, 39882198),
])
def test_combination_sum4(nums, target, expected):
    assert Solution().combinationSum4(nums, target) == expected

