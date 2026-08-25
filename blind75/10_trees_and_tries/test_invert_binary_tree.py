"""Tests for Invert Binary Tree. Run: pytest 10_trees_and_tries/test_invert_binary_tree.py"""
import pytest

from common.structures import build_tree, tree_to_list
from invert_binary_tree import Solution

@pytest.mark.parametrize("values, expected", [
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
    ([2, 1, 3], [2, 3, 1]),
    ([], []),
    ([1], [1]),
    ([1, 2], [1, None, 2]),
    ([1, 2, 3, 4, None, None, 5], [1, 3, 2, 5, None, None, 4]),
])
def test_invert_tree(values, expected):
    assert tree_to_list(Solution().invertTree(build_tree(values))) == expected

