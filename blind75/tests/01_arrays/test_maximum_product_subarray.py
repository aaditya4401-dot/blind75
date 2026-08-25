"""Tests for Maximum Product Subarray. Run: pytest 01_arrays/test_maximum_product_subarray.py"""
import pytest

from maximum_product_subarray import Solution

@pytest.mark.parametrize("nums, expected", [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
    ([-2], -2),
    ([-2, 3, -4], 24),
    ([0, 2], 2),
    ([-1, -2, -9, -6], 108),
    ([2, -5, -2, -4, 3], 24),
])
def test_max_product(nums, expected):
    assert Solution().maxProduct(nums) == expected

