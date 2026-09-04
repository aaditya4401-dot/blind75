"""
Minimum Window Substring  |  LeetCode 76  |  Hard
https://leetcode.com/problems/minimum-window-substring/

Given strings `s` and `t`, return the shortest substring of `s` that contains
every character of `t` including duplicates. If there is none, return "".

Example 1:
    Input:  s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"

Example 2:
    Input:  s = "a", t = "aa"
    Output: ""                  # only one 'a' available

Constraints:
    1 <= len(s), len(t) <= 10^5
    The answer is guaranteed to be unique.

Hint:
    Expanding/contracting sliding window. Count what t needs, then grow `right`
    until the window is complete, and shrink `left` as far as it can go while
    staying complete, recording the best window each time.

    Track a `have`/`need` counter of *satisfied character types* rather than
    re-comparing whole dicts -- that is what keeps it linear.

Target complexity: O(n + m) time, O(alphabet) space
"""
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l= 0
        mini = float("inf")
        counter = Counter(t)

        need = len(counter)
        have = 0

        result = ""
        window = {}
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1

            if window[s[r]]==counter[s[r]]:
                have+=1

            while have==need:
                if r-l+1<mini:
                    mini = r-l+1
                    result = s[l:r+1]

                window[s[l]]-=1

                if window[s[l]]<counter.get(s[l],0):
                    have-=1

                l+=1

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
