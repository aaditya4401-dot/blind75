"""
Kth Smallest Element in a BST  |  LeetCode 230  |  Medium
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a BST and an integer `k`, return the kth smallest value
(1-indexed).

Example 1:
    Input:  root = [3, 1, 4, None, 2], k = 1
    Output: 1

Example 2:
    Input:  root = [5, 3, 6, 2, 4, None, None, 1], k = 3
    Output: 3

Constraints:
    1 <= k <= number of nodes <= 10^4

Hint:
    Inorder traversal visits a BST in sorted order, so the kth node you touch is
    the answer. Do not materialize the whole list -- stop at k.

    An iterative stack-based inorder makes stopping natural, and is the version
    to reach for if asked the follow-up about frequent queries on a mutating
    tree (there, augment nodes with subtree sizes).

Note: locally `TreeNode` comes from common.structures, and tests build trees
from LeetCode's level-order list format (None marks a missing child).

Target complexity: O(h + k) time, O(h) space
"""

from typing import Optional

from common.structures import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
