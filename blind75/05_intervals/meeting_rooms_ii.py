"""
Meeting Rooms II  |  LeetCode 253  |  Medium
https://leetcode.com/problems/meeting-rooms-ii/

[LeetCode Premium] Given meeting time intervals, return the minimum number of
conference rooms required.

Example 1:
    Input:  intervals = [[0, 30], [5, 10], [15, 20]]
    Output: 2

Example 2:
    Input:  intervals = [[7, 10], [2, 4]]
    Output: 1

Constraints:
    0 <= len(intervals) <= 10^4
    A meeting ending at time t frees the room for one starting at t.

Hint:
    Min-heap of end times: sort by start, and for each meeting pop the heap if
    its earliest end is <= this start (that room is free), then push this end.
    The heap size is the answer.

    Or the sweep line: sort starts and ends separately, walk both with two
    pointers, +1 room on a start and -1 on an end, and track the peak.

Target complexity: O(n log n) time, O(n) space
"""

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_meeting_rooms_ii.py"))]))
