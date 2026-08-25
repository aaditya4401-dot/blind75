"""Tests for Meeting Rooms II. Run: pytest 05_intervals/test_meeting_rooms_ii.py"""
import pytest

from meeting_rooms_ii import Solution

@pytest.mark.parametrize("intervals, expected", [
    ([[0, 30], [5, 10], [15, 20]], 2),
    ([[7, 10], [2, 4]], 1),
    ([], 0),
    ([[1, 5]], 1),
    ([[1, 5], [5, 10]], 1),
    ([[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]], 4),
    ([[9, 10], [4, 9], [4, 17]], 2),
])
def test_min_meeting_rooms(intervals, expected):
    assert Solution().minMeetingRooms(intervals) == expected

