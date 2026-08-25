"""Tests for Course Schedule. Run: pytest 04_graphs/test_course_schedule.py"""
import pytest

from course_schedule import Solution

@pytest.mark.parametrize("num_courses, prerequisites, expected", [
    (2, [[1, 0]], True),
    (2, [[1, 0], [0, 1]], False),
    (1, [], True),
    (5, [[1, 4], [2, 4], [3, 1], [3, 2]], True),
    (3, [[0, 1], [1, 2], [2, 0]], False),
    (4, [[2, 0], [1, 0], [3, 1], [3, 2]], True),
    (20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14]], False),
])
def test_can_finish(num_courses, prerequisites, expected):
    assert Solution().canFinish(num_courses, prerequisites) is expected

