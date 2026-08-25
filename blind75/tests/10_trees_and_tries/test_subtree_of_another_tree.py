"""Tests for Subtree of Another Tree. Run: pytest 10_trees_and_tries/test_subtree_of_another_tree.py"""
import pytest

from common.structures import build_tree
from subtree_of_another_tree import Solution

@pytest.mark.parametrize("root, sub_root, expected", [
    ([3, 4, 5, 1, 2], [4, 1, 2], True),
    ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
    ([1], [1], True),
    ([1, 1], [1], True),
    ([3, 4, 5, 1, 2], [3, 1, 2], False),
    ([1, 2, 3], [2], True),
    ([12], [2], False),
])
def test_is_subtree(root, sub_root, expected):
    assert Solution().isSubtree(build_tree(root), build_tree(sub_root)) is expected

