"""Tests for Binary Tree Maximum Path Sum. Run: pytest 10_trees_and_tries/test_binary_tree_maximum_path_sum.py"""
import pytest

from common.structures import build_tree
from binary_tree_maximum_path_sum import Solution

@pytest.mark.parametrize("values, expected", [
    ([1, 2, 3], 6),
    ([-10, 9, 20, None, None, 15, 7], 42),
    ([-3], -3),
    ([2, -1], 2),
    ([-2, -1], -1),
    ([1, -2, -3, 1, 3, -2, None, -1], 3),
    ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 48),
])
def test_max_path_sum(values, expected):
    assert Solution().maxPathSum(build_tree(values)) == expected

