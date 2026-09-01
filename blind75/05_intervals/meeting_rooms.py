"""
Meeting Rooms  |  LeetCode 252  |  Easy
https://leetcode.com/problems/meeting-rooms/

[LeetCode Premium] Given meeting time intervals, determine whether a person
could attend all of them.

Example 1:
    Input:  intervals = [[0, 30], [5, 10], [15, 20]]
    Output: False

Example 2:
    Input:  intervals = [[7, 10], [2, 4]]
    Output: True

Constraints:
    0 <= len(intervals) <= 10^4
    A meeting ending exactly when the next starts is fine.

Hint:
    Sort by start, then check consecutive pairs: any meeting starting strictly
    before the previous one ends is a conflict. Note the strictness --
    [[1,5],[5,8]] is attendable.

Target complexity: O(n log n) time, O(1) space
"""

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[0])
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:
                return False
       
        return True
            
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
