"""
Remove Nth Node From End of List  |  LeetCode 19  |  Medium
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Remove the nth node from the end of the list and return its head.

Example 1:
    Input:  head = [1, 2, 3, 4, 5], n = 2
    Output: [1, 2, 3, 5]

Example 2:
    Input:  head = [1], n = 1
    Output: []

Constraints:
    1 <= number of nodes <= 30
    1 <= n <= number of nodes

Hint:
    Two pointers n nodes apart: advance `fast` n steps, then move both until
    fast falls off the end -- `slow` now sits just before the target.

    Start both from a dummy node in front of head; otherwise removing the first
    node (n == length) needs its own branch.

Target complexity: O(n) time, O(1) space, one pass
"""

from typing import Optional

from common.structures import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    sys.exit(pytest.main(["-v", str(pathlib.Path(__file__).with_name("test_remove_nth_node_from_end.py"))]))
