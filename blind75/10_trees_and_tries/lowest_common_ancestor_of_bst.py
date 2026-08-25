"""
Lowest Common Ancestor of a Binary Search Tree  |  LeetCode 235  |  Medium
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a BST and two nodes `p` and `q` in it, return their lowest common
ancestor. A node may be a descendant of itself.

Example 1:
    Input:  root = [6,2,8,0,4,7,9,None,None,3,5], p = 2, q = 8
    Output: 6

Example 2:
    Input:  same root, p = 2, q = 4
    Output: 2                   # a node can be its own ancestor

Constraints:
    2 <= number of nodes <= 10^5
    All values are unique; p and q both exist in the tree.

Hint:
    Exploit the BST ordering instead of searching. Walk down from the root: if
    both values are smaller, go left; if both are larger, go right; the moment
    they split (or one equals the current node) you are standing on the LCA.
    No recursion needed.

Note: locally `TreeNode` comes from common.structures, and tests build trees
from LeetCode's level-order list format (None marks a missing child).

Target complexity: O(h) time, O(1) space iteratively
"""

from common.structures import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_lowest_common_ancestor_of_bst.py"))]))
