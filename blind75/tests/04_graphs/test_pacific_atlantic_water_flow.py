"""Tests for Pacific Atlantic Water Flow. Run: pytest 04_graphs/test_pacific_atlantic_water_flow.py"""
import pytest

from pacific_atlantic_water_flow import Solution

@pytest.mark.parametrize("heights, expected", [
    ([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]],
     [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]),
    ([[1]], [[0, 0]]),
    ([[2, 1], [1, 2]], [[0, 0], [0, 1], [1, 0], [1, 1]]),
    ([[1, 2, 3], [8, 9, 4], [7, 6, 5]],
     [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]),
])
def test_pacific_atlantic(heights, expected):
    result = Solution().pacificAtlantic(heights)
    assert sorted(map(list, result)) == sorted(expected)

