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
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_number_of_islands.py"))]))
