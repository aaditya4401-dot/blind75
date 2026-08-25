"""
Rotate Image  |  LeetCode 48  |  Medium
https://leetcode.com/problems/rotate-image/

Rotate an n x n matrix 90 degrees clockwise, in place. You may not allocate
another 2D matrix.

Example 1:
    Input:  matrix = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]
    Output: [[7, 4, 1],
             [8, 5, 2],
             [9, 6, 3]]

Constraints:
    n == len(matrix) == len(matrix[i])
    1 <= n <= 20

Hint:
    Transpose (swap across the main diagonal, only j > i to avoid undoing it),
    then reverse each row. Counter-clockwise is the same transpose followed by
    reversing each column instead.

Target complexity: O(n^2) time, O(1) space
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Modify matrix in place; return nothing."""
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
