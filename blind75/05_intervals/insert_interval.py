"""
Insert Interval  |  LeetCode 57  |  Medium
https://leetcode.com/problems/insert-interval/

`intervals` is sorted by start and non-overlapping. Insert `newInterval`,
merging where necessary, and return the result still sorted and
non-overlapping.

Example 1:
    Input:  intervals = [[1, 3], [6, 9]], newInterval = [2, 5]
    Output: [[1, 5], [6, 9]]

Example 2:
    Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1, 2], [3, 10], [12, 16]]

Constraints:
    0 <= len(intervals) <= 10^4
    intervals is sorted by start.

Hint:
    One pass, three phases: copy everything ending before newInterval starts;
    then absorb every interval that overlaps, widening newInterval to
    min(starts)/max(ends); append it; then copy the rest. No sorting needed --
    the input is already ordered.

Target complexity: O(n) time, O(n) space for the output
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i=0
        while i<len(intervals) and intervals[i][1]<=newInterval[0]:
            result.append(intervals[i])
            i+=1
            
        while i<len(intervals)and intervals[i][0]<=newInterval[1]:
            newInterval[0] = min (newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
            i+=1
        result.append(newInterval)
        
        while i<len(intervals):
            result.append(intervals[i])
            i+=1
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
