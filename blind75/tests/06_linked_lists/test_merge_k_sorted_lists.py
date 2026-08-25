"""Tests for Merge k Sorted Lists. Run: pytest 06_linked_lists/test_merge_k_sorted_lists.py"""
import pytest

from common.structures import build_linked_list, linked_list_to_list
from merge_k_sorted_lists import Solution

@pytest.mark.parametrize("lists, expected", [
    ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
    ([], []),
    ([[]], []),
    ([[], []], []),
    ([[1]], [1]),
    ([[], [1], []], [1]),
    ([[-2, -1, -1, -1], [], [-3, -1]], [-3, -2, -1, -1, -1, -1]),
])
def test_merge_k_lists(lists, expected):
    heads = [build_linked_list(values) for values in lists]
    assert linked_list_to_list(Solution().mergeKLists(heads)) == expected

