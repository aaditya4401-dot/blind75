"""
Longest Repeating Character Replacement  |  LeetCode 424  |  Medium
https://leetcode.com/problems/longest-repeating-character-replacement/

You may change at most `k` characters of `s` to any uppercase letter. Return
the length of the longest substring containing a single repeated letter that
you can produce.

Example 1:
    Input:  s = "ABAB", k = 2
    Output: 4                   # turn both A's into B's

Example 2:
    Input:  s = "AABABBA", k = 1
    Output: 4                   # "AABA" -> "AAAA"

Constraints:
    1 <= len(s) <= 10^5
    s is uppercase English letters.
    0 <= k <= len(s)

Hint:
    Sliding window with a frequency count. A window is valid when
    (window length - count of its most common letter) <= k -- that difference is
    exactly how many replacements it would take.

    When it goes invalid, shrink from the left by one. The classic trick: you
    never need to shrink the max-count back down, because the answer only cares
    about the largest window ever seen.

Target complexity: O(n) time, O(26) space
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        maxfreq = 0

        result = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0)+1
            maxfreq = max(maxfreq,count[s[r]])

            while r-l+1 - maxfreq > k:
                count[s[l]]-=1
                l+=1

            result = max(result,r-l+1)

        return result



if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
