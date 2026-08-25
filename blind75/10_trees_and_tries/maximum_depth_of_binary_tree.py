"""
Maximum Depth of Binary Tree  |  LeetCode 104  |  Easy
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Return the maximum depth of a binary tree -- the number of nodes along the
longest path from the root down to a leaf.

Example 1:
    Input:  root = [3, 9, 20, None, None, 15, 7]
    Output: 3

Example 2:
    Input:  root = [1, None, 2]
    Output: 2

Constraints:
    0 <= number of nodes <= 10^4

Hint:
    depth(node) = 1 + max(depth(left), depth(right)), with depth(None) = 0.
    Three lines recursively. The iterative version is a BFS counting levels.

Note: locally `TreeNode` comes from common.structures, and tests build trees
from LeetCode's level-order list format (None marks a missing child).

Target complexity: O(n) time, O(h) space
"""

from typing import Optional

from common.structures import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
