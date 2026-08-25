"""
Word Search  |  LeetCode 79  |  Medium
https://leetcode.com/problems/word-search/

Given an m x n grid of characters and a string `word`, return True if `word`
can be spelled by walking horizontally or vertically adjacent cells. The same
cell may not be used more than once in a single path.

Example 1:
    Input:  board = [["A","B","C","E"],
                     ["S","F","C","S"],
                     ["A","D","E","E"]], word = "ABCCED"
    Output: True

Example 2:
    Input:  same board, word = "ABCB"
    Output: False               # the B would have to be reused

Constraints:
    1 <= m, n <= 6
    1 <= len(word) <= 15

Hint:
    DFS + backtracking from every cell. Mark the current cell as visited before
    recursing (overwrite it with "#" and restore it afterwards) so the path
    cannot fold back on itself. Prune early: bail the moment the letter does not
    match.

Target complexity: O(m * n * 4^L) time, O(L) space for the recursion
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
