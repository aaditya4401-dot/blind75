"""
Binary Tree Maximum Path Sum  |  LeetCode 124  |  Hard
https://leetcode.com/problems/binary-tree-maximum-path-sum/

A path is any sequence of nodes connected by edges; it need not pass through
the root, and each node appears at most once. Return the maximum sum of any
non-empty path.

Example 1:
    Input:  root = [1, 2, 3]
    Output: 6                   # 2 -> 1 -> 3

Example 2:
    Input:  root = [-10, 9, 20, None, None, 15, 7]
    Output: 42                  # 15 -> 20 -> 7

Constraints:
    1 <= number of nodes <= 3 * 10^4
    -1000 <= Node.val <= 1000

Hint:
    Two different quantities, and conflating them is the whole trap:

      * what you RETURN to the parent: node.val plus the better single branch,
        because a path through the parent cannot fork here;
      * what you record in the ANSWER: node.val + left + right, the path that
        peaks at this node.

    Clamp negative branch contributions to 0 (dropping a branch is always
    allowed), and seed the answer with -infinity, not 0, since all values may be
    negative.

Note: locally `TreeNode` comes from common.structures, and tests build trees
from LeetCode's level-order list format (None marks a missing child).

Target complexity: O(n) time, O(h) space
"""

from typing import Optional

from common.structures import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
