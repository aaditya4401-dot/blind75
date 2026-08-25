"""
Palindromic Substrings  |  LeetCode 647  |  Medium
https://leetcode.com/problems/palindromic-substrings/

Return the number of palindromic substrings in `s`. Substrings at different
start or end positions count separately, even if identical.

Example 1:
    Input:  s = "abc"
    Output: 3                   # "a", "b", "c"

Example 2:
    Input:  s = "aaa"
    Output: 6                   # "a" x3, "aa" x2, "aaa"

Constraints:
    1 <= len(s) <= 1000
    s is lowercase English letters.

Hint:
    Same expand-around-center machinery as problem 5, but count every successful
    expansion instead of tracking the longest. Both odd and even centers again.

Target complexity: O(n^2) time, O(1) space
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_palindromic_substrings.py"))]))
