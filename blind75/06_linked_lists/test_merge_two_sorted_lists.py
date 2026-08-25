"""Tests for Merge Two Sorted Lists. Run: pytest 06_linked_lists/test_merge_two_sorted_lists.py"""
import pytest

from common.structures import build_linked_list, linked_list_to_list
from merge_two_sorted_lists import Solution

@pytest.mark.parametrize("a, b, expected", [
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([], [], []),
    ([], [0], [0]),
    ([1], [], [1]),
    ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ([5], [1, 2, 4], [1, 2, 4, 5]),
    ([2, 2], [2, 2], [2, 2, 2, 2]),
])
def test_merge_two_lists(a, b, expected):
    merged = Solution().mergeTwoLists(build_linked_list(a), build_linked_list(b))
    assert linked_list_to_list(merged) == expected

