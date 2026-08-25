"""Tests for Number of Connected Components in an Undirected Graph. Run: pytest 04_graphs/test_number_of_connected_components.py"""
import pytest

from number_of_connected_components import Solution

@pytest.mark.parametrize("n, edges, expected", [
    (5, [[0, 1], [1, 2], [3, 4]], 2),
    (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1),
    (1, [], 1),
    (4, [], 4),
    (4, [[0, 1], [2, 3], [1, 0]], 2),
    (6, [[0, 1], [2, 3], [4, 5]], 3),
])
def test_count_components(n, edges, expected):
    assert Solution().countComponents(n, edges) == expected

