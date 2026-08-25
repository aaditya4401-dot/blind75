"""Tests for Binary Tree Level Order Traversal. Run: pytest 10_trees_and_tries/test_binary_tree_level_order_traversal.py"""
import pytest

from common.structures import build_tree
from binary_tree_level_order_traversal import Solution

@pytest.mark.parametrize("values, expected", [
    ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
    ([1], [[1]]),
    ([], []),
    ([1, 2, 3, 4, 5], [[1], [2, 3], [4, 5]]),
    ([1, None, 2, None, 3], [[1], [2], [3]]),
])
def test_level_order(values, expected):
    assert Solution().levelOrder(build_tree(values)) == expected

