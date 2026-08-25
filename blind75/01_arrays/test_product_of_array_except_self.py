"""Tests for Product of Array Except Self. Run: pytest 01_arrays/test_product_of_array_except_self.py"""
import pytest

from product_of_array_except_self import Solution

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ([2, 3], [3, 2]),
    ([0, 0], [0, 0]),
    ([1, 0, 3], [0, 3, 0]),
    ([-1, -2, -3], [6, 3, 2]),
])
def test_product_except_self(nums, expected):
    assert Solution().productExceptSelf(nums) == expected

