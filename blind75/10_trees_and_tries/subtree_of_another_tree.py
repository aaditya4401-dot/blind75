"""
Subtree of Another Tree  |  LeetCode 572  |  Easy
https://leetcode.com/problems/subtree-of-another-tree/

Return True if `subRoot` appears in `root` as a subtree -- some node of root
together with ALL of its descendants is identical to subRoot.

Example 1:
    Input:  root = [3, 4, 5, 1, 2], subRoot = [4, 1, 2]
    Output: True

Example 2:
    Input:  root = [3, 4, 5, 1, 2, None, None, None, None, 0], subRoot = [4, 1, 2]
    Output: False               # the match must include every descendant

Constraints:
    1 <= nodes in root <= 2000
    1 <= nodes in subRoot <= 1000

Hint:
    Reuse Same Tree: at every node of root, ask isSameTree(node, subRoot). The
    "all descendants" clause is what makes a partial match insufficient --
    example 2 is exactly that trap.

    O(n + m) alternative: serialize both with null markers and do a substring
    search (wrap values in delimiters so 2 does not match 12).

Note: locally `TreeNode` comes from common.structures, and tests build trees
from LeetCode's level-order list format (None marks a missing child).

Target complexity: O(m * n) time naive, O(h) space
"""

from typing import Optional

from common.structures import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
