"""
Graph Valid Tree  |  LeetCode 261  |  Medium
https://leetcode.com/problems/graph-valid-tree/

[LeetCode Premium] Given `n` nodes labelled 0..n-1 and a list of undirected
edges, return True if the edges form a valid tree.

Example 1:
    Input:  n = 5, edges = [[0,1], [0,2], [0,3], [1,4]]
    Output: True

Example 2:
    Input:  n = 5, edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    Output: False               # contains a cycle

Constraints:
    1 <= n <= 2000
    No duplicate edges and no self-loops.

Hint:
    A tree is exactly: connected AND acyclic. Two conditions, and the cheap
    shortcut is that with len(edges) == n - 1 enforced, connected implies
    acyclic -- so check the edge count, then confirm one DFS/BFS from node 0
    reaches all n nodes. Union-Find also works: any union of two already-joined
    nodes means a cycle.

Target complexity: O(V + E) time, O(V + E) space
"""

from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
