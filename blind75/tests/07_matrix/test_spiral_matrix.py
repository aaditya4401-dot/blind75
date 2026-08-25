"""Tests for Spiral Matrix. Run: pytest 07_matrix/test_spiral_matrix.py"""
import pytest

from spiral_matrix import Solution

@pytest.mark.parametrize("matrix, expected", [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
     [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    ([[1]], [1]),
    ([[1, 2], [3, 4]], [1, 2, 4, 3]),
    ([[1], [2], [3]], [1, 2, 3]),
    ([[1, 2, 3]], [1, 2, 3]),
    ([[2, 5], [8, 4], [0, -1]], [2, 5, 4, -1, 0, 8]),
])
def test_spiral_order(matrix, expected):
    assert Solution().spiralOrder(matrix) == expected

