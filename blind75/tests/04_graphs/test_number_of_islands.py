"""Tests for Number of Islands. Run: pytest 04_graphs/test_number_of_islands.py"""
import pytest

from number_of_islands import Solution

@pytest.mark.parametrize("grid, expected", [
    ([["1", "1", "1", "1", "0"],
      ["1", "1", "0", "1", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "0", "0", "0"]], 1),
    ([["1", "1", "0", "0", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "1", "0", "0"],
      ["0", "0", "0", "1", "1"]], 3),
    ([["0"]], 0),
    ([["1"]], 1),
    ([["1", "0", "1", "0", "1"]], 3),
    ([["1", "1"], ["0", "1"]], 1),
])
def test_num_islands(grid, expected):
    assert Solution().numIslands(grid) == expected

