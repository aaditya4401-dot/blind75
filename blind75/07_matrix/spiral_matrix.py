"""
Spiral Matrix  |  LeetCode 54  |  Medium
https://leetcode.com/problems/spiral-matrix/

Return all elements of an m x n matrix in spiral order.

Example 1:
    Input:  matrix = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]
    Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Example 2:
    Input:  matrix = [[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12]]
    Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

Constraints:
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100

Hint:
    Keep four boundaries (top, bottom, left, right) and peel one layer at a
    time, shrinking the boundary you just consumed. The bug everyone hits is a
    leftover single row or column: after the top row and right column, re-check
    that top <= bottom and left <= right before walking back.

Target complexity: O(m * n) time, O(1) extra space
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
