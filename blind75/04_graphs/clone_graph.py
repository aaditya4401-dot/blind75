"""
Clone Graph  |  LeetCode 133  |  Medium
https://leetcode.com/problems/clone-graph/

Given a reference to a node in a connected undirected graph, return a deep copy
of the whole graph. Each node holds a `val` and a list of `neighbors`.

Example 1:
    Input:  adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    Output: [[2, 4], [1, 3], [2, 4], [1, 3]]   (a brand new set of nodes)

Constraints:
    0 <= number of nodes <= 100
    The graph is connected, undirected, has no repeated edges and no self-loops.

Hint:
    A dict from original node -> its copy does two jobs at once: it stores the
    result and acts as the visited set, which is what keeps cycles from looping
    forever. Create the copy and register it in the dict BEFORE recursing into
    neighbors. Handle node=None up front.

Note: locally the node class is `GraphNode` from common.structures; on LeetCode
it is called `Node`.

Target complexity: O(V + E) time, O(V) space
"""

from typing import Optional

from common.structures import GraphNode


class Solution:
    def cloneGraph(self, node: Optional[GraphNode]) -> Optional[GraphNode]:
        if not node:
            return None
        cloned = {}
        def dfs(node):
            if node in cloned:
                return cloned[node]

            clone = GraphNode(node.val)
            cloned[node]= clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
