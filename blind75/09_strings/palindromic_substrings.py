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
        result = 0
        def expand(l,r):
            count=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
                count+=1

            return count

        for r in range(len(s)):
            result += expand(r,r) + expand(r,r+1)
        return result
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
