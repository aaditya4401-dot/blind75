"""Tests for Meeting Rooms. Run: pytest 05_intervals/test_meeting_rooms.py"""
import pytest

from meeting_rooms import Solution

@pytest.mark.parametrize("intervals, expected", [
    ([[0, 30], [5, 10], [15, 20]], False),
    ([[7, 10], [2, 4]], True),
    ([], True),
    ([[1, 5]], True),
    ([[1, 5], [5, 8]], True),
    ([[5, 8], [1, 5]], True),
    ([[1, 5], [4, 8]], False),
])
def test_can_attend_meetings(intervals, expected):
    assert Solution().canAttendMeetings(intervals) is expected

