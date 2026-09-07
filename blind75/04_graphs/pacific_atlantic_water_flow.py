"""
Pacific Atlantic Water Flow  |  LeetCode 417  |  Medium
https://leetcode.com/problems/pacific-atlantic-water-flow/

`heights` is an m x n grid of cell heights. The Pacific touches the top and
left edges; the Atlantic touches the bottom and right edges. Water flows from a
cell to a neighbour of height less than or equal to it. Return every coordinate
from which water can reach BOTH oceans.

Example 1:
    Input:  heights = [[1,2,2,3,5],
                       [3,2,3,4,4],
                       [2,4,5,3,1],
                       [6,7,1,4,5],
                       [5,1,1,2,4]]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Constraints:
    1 <= m, n <= 200
    0 <= heights[i][j] <= 10^5

Hint:
    Do not search forwards from each cell -- that is O((mn)^2). Reverse it:
    start at the ocean edges and flow UPHILL (neighbour >= current), marking
    reachable cells. Run that once from the Pacific border and once from the
    Atlantic border; the answer is the intersection of the two sets.

Target complexity: O(m * n) time, O(m * n) space
"""

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m , n = len(heights) , len(heights[0])
        pacific_reachable = [[0]*n for _ in range(m)]
        atlantic_reachable = [[0]*n for _ in range(m)]

        def dfs(r,c,visited):
            visited[r][c]=1

            for dr,dc in  (1,0) , (0,1) , (-1,0) , (0,-1):
                nr,nc = r+dr , c+dc

                if 0<=nr<m and 0<=nc<n and visited[nr][nc]==0 and heights[nr][nc]>=heights[r][c]:
                    dfs(nr,nc,visited)

            return
        result = []
        for row in range(m):
            if pacific_reachable[row][0]==0:
                dfs(row,0,pacific_reachable)

        for row in range(m):
            if atlantic_reachable[row][n-1]==0:
                dfs(row,n-1,atlantic_reachable)

        for col in range(n):
            if pacific_reachable[0][col]==0:
                dfs(0,col,pacific_reachable)

        for col in range(n):
            if atlantic_reachable[m-1][col]==0:
                dfs(m-1,col,atlantic_reachable)

        for i in range(m):
            for j in range(n):
                if pacific_reachable[i][j]==1 and atlantic_reachable[i][j]==1:
                    result.append([i,j])

        return result


        pass



if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
