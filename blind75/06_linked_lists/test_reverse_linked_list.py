"""Tests for Reverse Linked List. Run: pytest 06_linked_lists/test_reverse_linked_list.py"""
import pytest

from common.structures import build_linked_list, linked_list_to_list
from reverse_linked_list import Solution

@pytest.mark.parametrize("values, expected", [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2], [2, 1]),
    ([], []),
    ([1], [1]),
    ([1, 1, 2], [2, 1, 1]),
])
def test_reverse_list(values, expected):
    head = build_linked_list(values)
    assert linked_list_to_list(Solution().reverseList(head)) == expected

