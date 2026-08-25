"""
Binary Tree Level Order Traversal  |  LeetCode 102  |  Medium
https://leetcode.com/problems/binary-tree-level-order-traversal/

Return the level-order traversal of a binary tree's values -- one inner list
per level, left to right.

Example 1:
    Input:  root = [3, 9, 20, None, None, 15, 7]
    Output: [[3], [9, 20], [15, 7]]

Example 2:
    Input:  root = []
    Output: []

Constraints:
    0 <= number of nodes <= 2000

Hint:
    BFS with a deque. The trick that keeps levels separate: snapshot
    len(queue) at the top of each round and pop exactly that many nodes -- those
    are precisely the current level.

Note: locally `TreeNode` comes from common.structures, and tests build trees
from LeetCode's level-order list format (None marks a missing child).

Target complexity: O(n) time, O(n) space
"""

from typing import List, Optional

from common.structures import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass
