"""
Cheapest Flights Within K Stops  |  LeetCode 787  |  Medium
https://leetcode.com/problems/cheapest-flights-within-k-stops/

There are `n` cities labelled 0..n-1. `flights[i] = [from, to, price]`
describes a flight. Given `src`, `dst`, and `k`, return the cheapest price to
get from src to dst with at most k stops (i.e. at most k+1 flights), or -1 if
no such route exists.

Example 1:
    Input:  n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
            src = 0, dst = 3, k = 1
    Output: 700   # 0 -> 1 -> 3

Example 2:
    Input:  n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]]
            src = 0, dst = 2, k = 1
    Output: 200   # 0 -> 1 -> 2

Example 3:
    Input:  n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]]
            src = 0, dst = 2, k = 0
    Output: 500   # no stops allowed, must go direct

Constraints:
    1 <= n <= 100
    0 <= len(flights) <= n * (n - 1) / 2
    0 <= src, dst, k < n
    src != dst

Hint:
    Plain Dijkstra doesn't work directly -- the cheapest path overall might use
    more stops than the cheapest path within k stops, so you can't just track
    "best cost per city". Instead run Bellman-Ford for exactly k+1 rounds:
    each round, relax every edge using distances frozen from the previous
    round (copy the distance array first, or you'll let a single round chain
    together more than one hop).

Target complexity: O(k * E) time, O(V) space
"""

from typing import List

from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:

        adj = defaultdict(list)
        for s , d, p in flights:
            adj[s].append((d,p))

        heap = [(0,src,0)]
        visited = {}
        while heap:
            price , node , flights_taken = heapq.heappop(heap)

            if node==dst:
                return price

            if flights_taken>=k+1:
                continue

            if node in visited and visited[node]<=flights_taken:
                continue
            visited[node] = flights_taken
            for nb, p in adj[node]:
                heapq.heappush(heap , (price + p , nb , flights_taken+1))


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
