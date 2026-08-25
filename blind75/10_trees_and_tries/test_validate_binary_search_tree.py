"""Tests for Validate Binary Search Tree. Run: pytest 10_trees_and_tries/test_validate_binary_search_tree.py"""
import pytest

from common.structures import build_tree
from validate_binary_search_tree import Solution

@pytest.mark.parametrize("values, expected", [
    ([2, 1, 3], True),
    ([5, 1, 4, None, None, 3, 6], False),
    ([1], True),
    ([1, 1], False),
    ([2, 2, 2], False),
    ([5, 4, 6, None, None, 3, 7], False),
    ([10, 5, 15, None, None, 6, 20], False),
    ([3, 1, 5, 0, 2, 4, 6], True),
    ([2147483647], True),
])
def test_is_valid_bst(values, expected):
    assert Solution().isValidBST(build_tree(values)) is expected

