"""
Longest Common Subsequence  |  LeetCode 1143  |  Medium
https://leetcode.com/problems/longest-common-subsequence/

Return the length of the longest subsequence common to `text1` and `text2`, or
0 if there is none.

Example 1:
    Input:  text1 = "abcde", text2 = "ace"
    Output: 3                   # "ace"

Example 2:
    Input:  text1 = "abc", text2 = "def"
    Output: 0

Constraints:
    1 <= len(text1), len(text2) <= 1000
    Both strings are lowercase English letters.

Hint:
    Classic 2D grid DP. dp[i][j] = LCS of text1[i:] and text2[j:].
        if text1[i] == text2[j]:  dp[i][j] = 1 + dp[i+1][j+1]
        else:                     dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    Pad with a zero row and column so the boundaries need no special-casing.

Target complexity: O(m * n) time, O(min(m, n)) space if you roll the rows
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
