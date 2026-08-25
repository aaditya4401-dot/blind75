"""
Number of Connected Components in an Undirected Graph  |  LeetCode 323  |  Medium
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

[LeetCode Premium] Given `n` nodes labelled 0..n-1 and a list of undirected
edges, return the number of connected components.

Example 1:
    Input:  n = 5, edges = [[0, 1], [1, 2], [3, 4]]
    Output: 2

Example 2:
    Input:  n = 5, edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    Output: 1

Constraints:
    1 <= n <= 2000
    No duplicate edges and no self-loops.

Hint:
    Build an adjacency list, then DFS/BFS from every node you have not visited
    yet -- each fresh launch is one component.

    Union-Find version: start the count at n and decrement on every successful
    union. Worth writing at least once; it is the same tool as Graph Valid Tree.

Target complexity: O(V + E) time, O(V + E) space
"""

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_number_of_connected_components.py"))]))
