"""
Set Matrix Zeroes  |  LeetCode 73  |  Medium
https://leetcode.com/problems/set-matrix-zeroes/

Given an m x n matrix, if an element is 0 set its entire row and column to 0.
Do it in place.

Example 1:
    Input:  matrix = [[1, 1, 1],
                      [1, 0, 1],
                      [1, 1, 1]]
    Output: [[1, 0, 1],
             [0, 0, 0],
             [1, 0, 1]]

Constraints:
    1 <= m, n <= 200
    -2^31 <= matrix[i][j] <= 2^31 - 1

Hint:
    The naive fix -- zeroing as you scan -- cascades, because the zeros you
    write look like input zeros. So mark first, write second. O(m + n) space is
    two sets of rows/cols to clear. For O(1), use row 0 and column 0 themselves
    as the marker storage, with one extra flag for "column 0 must be zeroed"
    since matrix[0][0] has to serve double duty.

Target complexity: O(m * n) time, O(1) space
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
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
