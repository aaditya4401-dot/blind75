"""Tests for Contains Duplicate. Run: pytest 01_arrays/test_contains_duplicate.py"""
import pytest

from contains_duplicate import Solution

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ([1], False),
    ([-1, -1], True),
])
def test_contains_duplicate(nums, expected):
    assert Solution().containsDuplicate(nums) is expected

