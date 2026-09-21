"""
Reorganize String  |  LeetCode 767  |  Medium
https://leetcode.com/problems/reorganize-string/

Given a string `s`, rearrange its characters so no two adjacent characters are
the same. Return any valid rearrangement, or "" if none exists.

Example 1:
    Input:  s = "aab"
    Output: "aba"

Example 2:
    Input:  s = "aaab"
    Output: ""

Constraints:
    1 <= len(s) <= 500
    s consists of lowercase English letters only.

Hint:
    Greedy with a max-heap keyed by count: always place the currently most
    frequent character, then temporarily hold it out of the heap for one
    round so it can't be placed again immediately next. If the most frequent
    character's count exceeds ceil(len(s) / 2), no arrangement is possible.

Target complexity: O(n log k) time where k = distinct characters, O(k) space
"""

from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxheap = [(-cnt,char) for char,cnt in count.items()]
        heapq.heapify(maxheap)
        prev_cnt , prev_char = 0 , ''
        result = ''
        while maxheap:
            cnt  , char = heapq.heappop(maxheap)
            result+= char

            if prev_cnt<0:

                heapq.heappush(maxheap , (prev_cnt,prev_char) )

            prev_cnt , prev_char = cnt+1 , char

        return result if len(result)==len(s) else ''






        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
