"""
Reverse Linked List  |  LeetCode 206  |  Easy
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse it and return the new head.

Example 1:
    Input:  head = [1, 2, 3, 4, 5]
    Output: [5, 4, 3, 2, 1]

Example 2:
    Input:  head = []
    Output: []

Constraints:
    0 <= number of nodes <= 5000
    -5000 <= Node.val <= 5000

Hint:
    Three pointers: prev (starts None), curr, and a temp holding curr.next.
    Each step: save next, point curr.next at prev, then slide both forward.
    Write the recursive version too -- interviewers ask for both.

Target complexity: O(n) time, O(1) space
"""

from typing import Optional

from common.structures import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pathlib
    import sys

    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
