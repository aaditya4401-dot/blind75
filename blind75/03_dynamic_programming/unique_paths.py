"""
Unique Paths  |  LeetCode 62  |  Medium
https://leetcode.com/problems/unique-paths/

A robot starts at the top-left of an m x n grid and can only move right or
down. How many distinct paths reach the bottom-right corner?

Example 1:
    Input:  m = 3, n = 7
    Output: 28

Example 2:
    Input:  m = 3, n = 2
    Output: 3

Constraints:
    1 <= m, n <= 100
    The answer fits in a 32-bit integer.

Hint:
    dp[i][j] = dp[i-1][j] + dp[i][j-1], with the top row and left column all 1.
    One row rolled in place is enough space.

    Closed form: every path is (m-1) downs and (n-1) rights in some order, so
    the answer is C(m + n - 2, m - 1).

Target complexity: O(m * n) time, O(n) space (or O(1) with combinatorics)
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_unique_paths.py"))]))
