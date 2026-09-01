"""
Merge Intervals  |  LeetCode 56  |  Medium
https://leetcode.com/problems/merge-intervals/

Given an array of intervals, merge all overlapping intervals and return the
non-overlapping intervals that cover all the input.

Example 1:
    Input:  intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    Output: [[1, 6], [8, 10], [15, 18]]

Example 2:
    Input:  intervals = [[1, 4], [4, 5]]
    Output: [[1, 5]]            # touching counts as overlapping

Constraints:
    1 <= len(intervals) <= 10^4
    0 <= start <= end <= 10^4

Hint:
    Sort by start -- everything falls out after that. Walk the sorted list: if
    the current interval starts at or before the last merged one's end, extend
    that end to max(both ends); otherwise start a new block.

Target complexity: O(n log n) time, O(n) space
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        result = [intervals[0]]
        
        for i in range(1,len(intervals)):
            last = result[-1]
            curr = intervals[i]
            
            if last[1]>=curr[0]:
                last[1] = max(last[1],curr[1])
            
            else:
                result.append(intervals[i])
                
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
