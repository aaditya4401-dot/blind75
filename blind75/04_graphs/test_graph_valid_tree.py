"""Tests for Graph Valid Tree. Run: pytest 04_graphs/test_graph_valid_tree.py"""
import pytest

from graph_valid_tree import Solution

@pytest.mark.parametrize("n, edges, expected", [
    (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),
    (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),
    (1, [], True),
    (2, [], False),
    (4, [[0, 1], [2, 3]], False),
    (3, [[0, 1], [1, 2]], True),
    (4, [[0, 1], [1, 2], [2, 3], [3, 0]], False),
])
def test_valid_tree(n, edges, expected):
    assert Solution().validTree(n, edges) is expected

