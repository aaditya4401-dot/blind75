"""Tests for Kth Smallest Element in a BST. Run: pytest 10_trees_and_tries/test_kth_smallest_element_in_a_bst.py"""
import pytest

from common.structures import build_tree
from kth_smallest_element_in_a_bst import Solution

@pytest.mark.parametrize("values, k, expected", [
    ([3, 1, 4, None, 2], 1, 1),
    ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
    ([1], 1, 1),
    ([3, 1, 4, None, 2], 4, 4),
    ([2, 1, 3], 2, 2),
    ([5, 3, 6, 2, 4, None, None, 1], 6, 6),
])
def test_kth_smallest(values, k, expected):
    assert Solution().kthSmallest(build_tree(values), k) == expected

