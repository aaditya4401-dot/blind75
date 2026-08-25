"""
Validate Binary Search Tree  |  LeetCode 98  |  Medium
https://leetcode.com/problems/validate-binary-search-tree/

Determine whether a binary tree is a valid BST: every node in the left subtree
is strictly less than the node, every node in the right subtree is strictly
greater, and both subtrees are themselves BSTs.

Example 1:
    Input:  root = [2, 1, 3]
    Output: True

Example 2:
    Input:  root = [5, 1, 4, None, None, 3, 6]
    Output: False               # 3 is in the right subtree of 5

Constraints:
    1 <= number of nodes <= 10^4
    -2^31 <= Node.val <= 2^31 - 1

Hint:
    Comparing each node only with its two children is WRONG -- example 2 passes
    that check. Every node must satisfy the whole ancestor chain, so carry a
    (low, high) range down the recursion, narrowing it at each step.

    Alternative: an inorder traversal of a BST is strictly increasing; walk it
    and compare against the previous value. Use None/±inf as open bounds rather
    than integer sentinels, since node values span the full 32-bit range.

Note: locally `TreeNode` comes from common.structures, and tests build trees
from LeetCode's level-order list format (None marks a missing child).

Target complexity: O(n) time, O(h) space
"""

from typing import Optional

from common.structures import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pass
