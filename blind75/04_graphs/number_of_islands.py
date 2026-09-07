"""
Number of Islands  |  LeetCode 200  |  Medium
https://leetcode.com/problems/number-of-islands/

Given an m x n grid of "1" (land) and "0" (water), return the number of
islands. An island is land connected 4-directionally, and the grid is
surrounded by water on all sides.

Example 1:
    Input:  grid = [["1","1","1","1","0"],
                    ["1","1","0","1","0"],
                    ["1","1","0","0","0"],
                    ["0","0","0","0","0"]]
    Output: 1

Example 2:
    Input:  grid = [["1","1","0","0","0"],
                    ["1","1","0","0","0"],
                    ["0","0","1","0","0"],
                    ["0","0","0","1","1"]]
    Output: 3

Constraints:
    1 <= m, n <= 300
    grid[i][j] is "0" or "1".

Hint:
    Scan every cell; when you hit an unvisited "1", increment the counter and
    flood-fill the whole island so it is never counted again. Sinking the island
    in place (write "0") is the cheapest visited-marker. On a 300x300 grid,
    recursive DFS can blow the stack -- an explicit stack or BFS queue is safer.

Target complexity: O(m * n) time, O(m * n) space worst case
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])

        visited= [[0]*n for _  in range(m)]

        def dfs(r,c):
            visited[r][c]=1

            for dr,dc in (1,0),(0,1),(-1,0),(0,-1):
                nr,nc = r+dr,c+dc

                if 0<=nr<m and 0<=nc<n and visited[nr][nc]==0 and grid[nr][nc]=='1':
                    dfs(nr,nc)
            return

        islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and visited[i][j]==0:
                    dfs(i,j)
                    islands+=1
        return islands
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
