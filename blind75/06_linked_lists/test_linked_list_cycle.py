"""Tests for Linked List Cycle. Run: pytest 06_linked_lists/test_linked_list_cycle.py"""
import pytest

from common.structures import build_cyclic_list
from linked_list_cycle import Solution

@pytest.mark.parametrize("values, pos, expected", [
    ([3, 2, 0, -4], 1, True),
    ([1, 2], 0, True),
    ([1], -1, False),
    ([], -1, False),
    ([1, 2, 3, 4], -1, False),
    ([1], 0, True),
    ([1, 2, 3], 2, True),
])
def test_has_cycle(values, pos, expected):
    head = build_cyclic_list(values, pos)
    assert Solution().hasCycle(head) is expected

