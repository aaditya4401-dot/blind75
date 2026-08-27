"""
Word Break  |  LeetCode 139  |  Medium
https://leetcode.com/problems/word-break/

Given a string `s` and a dictionary `wordDict`, return True if `s` can be
segmented into a space-separated sequence of dictionary words. A word may be
reused any number of times.

Example 1:
    Input:  s = "leetcode", wordDict = ["leet", "code"]
    Output: True

Example 2:
    Input:  s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
    Output: False

Constraints:
    1 <= len(s) <= 300
    1 <= len(wordDict) <= 1000

Hint:
    dp[i] = "can s[:i] be segmented". dp[0] = True. For each i, look back at
    every j < i where dp[j] is True and check whether s[j:i] is in the
    dictionary. Put wordDict in a set -- the membership test is the inner loop.
    Greedy longest-match fails on "catsandog".

Target complexity: O(n^2 * k) time, O(n) space
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [-1]*(len(s)+1)
        return self.helper(len(s),s,words,dp)

    def helper(self, ind, s,words,dp):
        if ind==0:
            return True
        if dp[ind] !=-1:
            return dp[ind]

        dp[ind]=False

        for j in range(ind):
            if self.helper(j, s, words, dp) and s[j:ind] in words:
                dp[ind] = True
                break

        return dp[ind]
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
