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
        pass
