"""Tests for Same Tree. Run: pytest 10_trees_and_tries/test_same_tree.py"""
import pytest

from common.structures import build_tree
from same_tree import Solution

@pytest.mark.parametrize("p, q, expected", [
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2], [1, None, 2], False),
    ([1, 2, 1], [1, 1, 2], False),
    ([], [], True),
    ([1], [], False),
    ([1], [1], True),
    ([1, 2, 3, 4], [1, 2, 3, 4], True),
])
def test_is_same_tree(p, q, expected):
    assert Solution().isSameTree(build_tree(p), build_tree(q)) is expected

