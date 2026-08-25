"""Tests for Reorder List. Run: pytest 06_linked_lists/test_reorder_list.py"""
import pytest

from common.structures import build_linked_list, linked_list_to_list
from reorder_list import Solution

@pytest.mark.parametrize("values, expected", [
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([1, 2, 3], [1, 3, 2]),
    ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
])
def test_reorder_list(values, expected):
    head = build_linked_list(values)
    Solution().reorderList(head)
    assert linked_list_to_list(head) == expected

