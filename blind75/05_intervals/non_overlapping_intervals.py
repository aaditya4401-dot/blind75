"""
Non-overlapping Intervals  |  LeetCode 435  |  Medium
https://leetcode.com/problems/non-overlapping-intervals/

Return the minimum number of intervals you must remove so that the rest are
non-overlapping.

Example 1:
    Input:  intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    Output: 1                   # drop [1, 3]

Example 2:
    Input:  intervals = [[1, 2], [1, 2], [1, 2]]
    Output: 2

Constraints:
    1 <= len(intervals) <= 10^5
    Intervals that merely touch at an endpoint do NOT overlap.

Hint:
    This is the classic activity-selection problem in disguise: removing the
    fewest means keeping the most. Sort by END time and greedily keep every
    interval that starts at or after the last kept end -- finishing early leaves
    the most room. Sorting by start instead needs an extra rule (drop the one
    with the later end).

Target complexity: O(n log n) time, O(1) space
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1])
        prev_kept = intervals[0][1]
        count = 0
        for s,e in intervals[1:]:
            if s<prev_kept:
                count+=1
            else:
                prev_kept = e
        return count
                
                
            
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
