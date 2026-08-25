"""Tests for Lowest Common Ancestor of a Binary Search Tree. Run: pytest 10_trees_and_tries/test_lowest_common_ancestor_of_bst.py"""
import pytest

from common.structures import build_tree, find_node
from lowest_common_ancestor_of_bst import Solution

TREE = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]


@pytest.mark.parametrize("values, p_val, q_val, expected", [
    (TREE, 2, 8, 6),
    (TREE, 2, 4, 2),
    (TREE, 3, 5, 4),
    (TREE, 0, 5, 2),
    (TREE, 7, 9, 8),
    ([2, 1], 2, 1, 2),
])
def test_lowest_common_ancestor(values, p_val, q_val, expected):
    root = build_tree(values)
    p, q = find_node(root, p_val), find_node(root, q_val)
    assert Solution().lowestCommonAncestor(root, p, q).val == expected

