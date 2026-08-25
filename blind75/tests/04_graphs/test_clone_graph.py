"""Tests for Clone Graph. Run: pytest 04_graphs/test_clone_graph.py"""
import pytest

from common.structures import build_graph, graph_to_adj
from clone_graph import Solution

@pytest.mark.parametrize("adj", [
    [[2, 4], [1, 3], [2, 4], [1, 3]],
    [[]],
    [],
    [[2], [1]],
    [[2, 3], [1], [1]],
])
def test_clone_graph_shape(adj):
    original = build_graph(adj)
    clone = Solution().cloneGraph(original)
    assert graph_to_adj(clone) == adj


def test_clone_is_deep_copy():
    original = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
    clone = Solution().cloneGraph(original)
    assert clone is not original
    assert clone.val == original.val
    originals = {id(n) for n in original.neighbors} | {id(original)}
    assert all(id(n) not in originals for n in clone.neighbors)


def test_clone_empty():
    assert Solution().cloneGraph(None) is None

