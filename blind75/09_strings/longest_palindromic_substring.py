"""
Longest Palindromic Substring  |  LeetCode 5  |  Medium
https://leetcode.com/problems/longest-palindromic-substring/

Return the longest palindromic substring of `s`.

Example 1:
    Input:  s = "babad"
    Output: "bab"               # "aba" is equally valid

Example 2:
    Input:  s = "cbbd"
    Output: "bb"

Constraints:
    1 <= len(s) <= 1000
    s is letters and digits.

Hint:
    Expand around centers. There are 2n - 1 centers -- n single characters (odd
    lengths) and n - 1 gaps between characters (even lengths). Push outwards
    from each while the ends match, and keep the longest.

    Forgetting the even-length centers is the standard bug: it silently fails on
    "cbbd".

Target complexity: O(n^2) time, O(1) space
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        best = ""
        def extend(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1

            return s[l+1:r]

        for i in range(len(s)):
            for word in extend(i,i),extend(i,i+1):
                if len(word)>len(best):
                    best = word

        return best

        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
