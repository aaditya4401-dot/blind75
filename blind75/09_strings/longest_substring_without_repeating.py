"""
Longest Substring Without Repeating Characters  |  LeetCode 3  |  Medium
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string `s`, return the length of the longest substring without
repeating characters.

Example 1:
    Input:  s = "abcabcbb"
    Output: 3                   # "abc"

Example 2:
    Input:  s = "bbbbb"
    Output: 1                   # "b"

Example 3:
    Input:  s = "pwwkew"
    Output: 3                   # "wke" -- "pwke" is a subsequence, not a substring

Constraints:
    0 <= len(s) <= 5 * 10^4
    s may contain letters, digits, symbols and spaces.

Hint:
    Sliding window. Extend `right`; when the new character is already inside the
    window, pull `left` forward past its previous occurrence. Storing
    char -> last index lets you jump `left` directly instead of shrinking one
    step at a time -- but never let `left` move backwards.

Target complexity: O(n) time, O(min(n, alphabet)) space
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxi = 0
        myset = set()
        for r in range(len(s)):
            while s[r] in myset:
                myset.remove(s[l])
                l+=1
            myset.add(s[r])
            maxi = max(maxi,r-l+1)
        return maxi



if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
