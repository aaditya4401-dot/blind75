"""Tests for Task Scheduler. Run: pytest 08_heap/test_task_scheduler.py"""
import pytest


from task_scheduler import Solution


@pytest.mark.parametrize(
    "tasks, n, expected",
    [
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "A", "A", "B", "B", "B"], 0, 6),
        (
            ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"],
            2,
            16,
        ),
    ],
)
def test_least_interval(tasks, n, expected):
    assert Solution().leastInterval(tasks, n) == expected


def test_single_task():
    assert Solution().leastInterval(["A"], 2) == 1


def test_all_distinct_tasks_need_no_idle():
    assert Solution().leastInterval(["A", "B", "C", "D"], 2) == 4
