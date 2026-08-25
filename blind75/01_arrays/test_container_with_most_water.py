"""Tests for Container With Most Water. Run: pytest 01_arrays/test_container_with_most_water.py"""
import pytest

from container_with_most_water import Solution

@pytest.mark.parametrize("height, expected", [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([4, 3, 2, 1, 4], 16),
    ([1, 2, 1], 2),
    ([2, 3, 4, 5, 18, 17, 6], 17),
    ([0, 0], 0),
])
def test_max_area(height, expected):
    assert Solution().maxArea(height) == expected

