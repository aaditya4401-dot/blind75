"""Tests for Construct Binary Tree from Preorder and Inorder Traversal. Run: pytest 10_trees_and_tries/test_construct_binary_tree_preorder_inorder.py"""
import pytest

from common.structures import tree_to_list
from construct_binary_tree_preorder_inorder import Solution

@pytest.mark.parametrize("preorder, inorder, expected", [
    ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
    ([-1], [-1], [-1]),
    ([1, 2], [2, 1], [1, 2]),
    ([1, 2], [1, 2], [1, None, 2]),
    ([1, 2, 3], [2, 1, 3], [1, 2, 3]),
    ([3, 2, 1, 4], [1, 2, 3, 4], [3, 2, 4, 1]),
])
def test_build_tree(preorder, inorder, expected):
    assert tree_to_list(Solution().buildTree(preorder, inorder)) == expected

