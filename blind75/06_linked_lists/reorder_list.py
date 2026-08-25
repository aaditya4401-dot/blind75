"""
Reorder List  |  LeetCode 143  |  Medium
https://leetcode.com/problems/reorder-list/

Given L0 -> L1 -> ... -> Ln-1 -> Ln, reorder it in place to
L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

You may not modify the values -- only the node links.

Example 1:
    Input:  head = [1, 2, 3, 4]
    Output: [1, 4, 2, 3]

Example 2:
    Input:  head = [1, 2, 3, 4, 5]
    Output: [1, 5, 2, 4, 3]

Constraints:
    1 <= number of nodes <= 5 * 10^4

Hint:
    Three known sub-problems stitched together:
      1. find the middle with slow/fast pointers,
      2. reverse the second half (problem 206),
      3. weave the two halves together alternating nodes.
    Remember to cut the first half loose (set mid.next = None) or you will build
    a cycle.

Target complexity: O(n) time, O(1) space
"""

from typing import Optional

from common.structures import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Reorder in place; return nothing."""
        pass
