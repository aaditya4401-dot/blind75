"""
Construct Binary Tree from Preorder and Inorder Traversal  |  LeetCode 105  |  Medium
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given `preorder` and `inorder` traversals of a binary tree with unique values,
rebuild and return the tree.

Example 1:
    Input:  preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
    Output: [3, 9, 20, None, None, 15, 7]

Example 2:
    Input:  preorder = [-1], inorder = [-1]
    Output: [-1]

Constraints:
    1 <= len(preorder) <= 3000
    Values are unique, and inorder is a permutation of preorder.

Hint:
    preorder[0] is always the root. Find it in inorder: everything to its left
    is the left subtree, everything to its right is the right subtree, and the
    left size tells you how to split preorder. Recurse.

    Naively calling inorder.index() each time is O(n^2); precompute
    value -> index once and pass array bounds instead of slicing.

Note: locally `TreeNode` comes from common.structures, and tests build trees
from LeetCode's level-order list format (None marks a missing child).

Target complexity: O(n) time with an index map, O(n) space
"""

from typing import List, Optional

from common.structures import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
