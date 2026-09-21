"""
Network Delay Time  |  LeetCode 743  |  Medium
https://leetcode.com/problems/network-delay-time/

There are `n` network nodes labelled 1..n. `times[i] = [u, v, w]` means a
signal travels from node u to node v in w time. Starting from node `k`, return
the minimum time for all n nodes to receive the signal, or -1 if impossible.

Example 1:
    Input:  times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
    Output: 2

Example 2:
    Input:  times = [[1,2,1]], n = 2, k = 1
    Output: 1

Example 3:
    Input:  times = [[1,2,1]], n = 2, k = 2
    Output: -1

Constraints:
    1 <= k <= n <= 100
    1 <= len(times) <= 6000
    0 <= wi <= 100
    All (ui, vi) pairs are distinct.

Hint:
    Classic single-source shortest path on a weighted directed graph:
    Dijkstra with a min-heap. Push (0, k), pop the closest unvisited node each
    time, relax its outgoing edges. The answer is the max distance across all
    n nodes once the heap drains -- if fewer than n nodes were ever reached,
    return -1.

Target complexity: O(E log V) time, O(V + E) space
"""

from typing import List

from collections import defaultdict , deque
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u,v,t in times:
            adj[u].append((v,t))

        visited = set()

        heap = [(0,k)]

        while heap:
            time , node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited)==n:
                return time

            for nb,t in adj[node]:
                if nb not in visited:
                    heapq.heappush(heap,(time+t,nb))
        return -1
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
