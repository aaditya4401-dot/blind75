"""
Invert Binary Tree  |  LeetCode 226  |  Easy
https://leetcode.com/problems/invert-binary-tree/

Invert a binary tree -- mirror it left to right -- and return its root.

Example 1:
    Input:  root = [4, 2, 7, 1, 3, 6, 9]
    Output: [4, 7, 2, 9, 6, 3, 1]

Example 2:
    Input:  root = [2, 1, 3]
    Output: [2, 3, 1]

Constraints:
    0 <= number of nodes <= 100

Hint:
    Swap each node's children, then recurse into both. Order does not matter as
    long as you swap the references, not just the values. (Yes -- this is the
    problem Max Howell famously did not get.)

Note: locally `TreeNode` comes from common.structures, and tests build trees
from LeetCode's level-order list format (None marks a missing child).

Target complexity: O(n) time, O(h) space
"""

from typing import Optional

from common.structures import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_invert_binary_tree.py"))]))
