"""Tests for Remove Nth Node From End of List. Run: pytest 06_linked_lists/test_remove_nth_node_from_end.py"""
import pytest

from common.structures import build_linked_list, linked_list_to_list
from remove_nth_node_from_end import Solution

@pytest.mark.parametrize("values, n, expected", [
    ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
    ([1], 1, []),
    ([1, 2], 1, [1]),
    ([1, 2], 2, [2]),
    ([1, 2, 3], 3, [2, 3]),
    ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
])
def test_remove_nth_from_end(values, n, expected):
    head = build_linked_list(values)
    assert linked_list_to_list(Solution().removeNthFromEnd(head, n)) == expected

