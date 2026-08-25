"""Tests for Missing Number. Run: pytest 02_binary/test_missing_number.py"""
import pytest

from missing_number import Solution

@pytest.mark.parametrize("nums, expected", [
    ([3, 0, 1], 2),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ([0, 1], 2),
    ([1], 0),
    ([0], 1),
    ([1, 2], 0),
])
def test_missing_number(nums, expected):
    assert Solution().missingNumber(nums) == expected

