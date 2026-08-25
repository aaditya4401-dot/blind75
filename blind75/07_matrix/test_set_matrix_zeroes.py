"""Tests for Set Matrix Zeroes. Run: pytest 07_matrix/test_set_matrix_zeroes.py"""
import pytest

from set_matrix_zeroes import Solution

@pytest.mark.parametrize("matrix, expected", [
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]],
     [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
    ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
     [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
    ([[1]], [[1]]),
    ([[0]], [[0]]),
    ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
    ([[1, 0], [3, 4]], [[0, 0], [3, 0]]),
])
def test_set_zeroes(matrix, expected):
    Solution().setZeroes(matrix)
    assert matrix == expected

