"""
Same Tree  |  LeetCode 100  |  Easy
https://leetcode.com/problems/same-tree/

Given the roots of two binary trees, return True if they are structurally
identical and every corresponding node holds the same value.

Example 1:
    Input:  p = [1, 2, 3], q = [1, 2, 3]
    Output: True

Example 2:
    Input:  p = [1, 2], q = [1, None, 2]
    Output: False               # same values, different shape

Constraints:
    0 <= number of nodes in each tree <= 100

Hint:
    Recurse in lockstep. Both None -> True; exactly one None, or different
    values -> False; otherwise compare left with left and right with right.

Note: locally `TreeNode` comes from common.structures, and tests build trees
from LeetCode's level-order list format (None marks a missing child).

Target complexity: O(n) time, O(h) space
"""

from typing import Optional

from common.structures import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pass
