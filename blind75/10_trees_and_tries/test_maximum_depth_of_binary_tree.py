"""Tests for Maximum Depth of Binary Tree. Run: pytest 10_trees_and_tries/test_maximum_depth_of_binary_tree.py"""
import pytest

from common.structures import build_tree
from maximum_depth_of_binary_tree import Solution

@pytest.mark.parametrize("values, expected", [
    ([3, 9, 20, None, None, 15, 7], 3),
    ([1, None, 2], 2),
    ([], 0),
    ([1], 1),
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, None, 3, None, 4], 4),
])
def test_max_depth(values, expected):
    assert Solution().maxDepth(build_tree(values)) == expected

