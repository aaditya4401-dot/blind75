"""
Merge Two Sorted Lists  |  LeetCode 21  |  Easy
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists into one sorted list, splicing together the
existing nodes. Return the head of the merged list.

Example 1:
    Input:  list1 = [1, 2, 4], list2 = [1, 3, 4]
    Output: [1, 1, 2, 3, 4, 4]

Example 2:
    Input:  list1 = [], list2 = [0]
    Output: [0]

Constraints:
    0 <= number of nodes in each list <= 50
    Both lists are sorted non-decreasing.

Hint:
    A dummy head node removes every "is this the first element" special case.
    Walk both lists appending the smaller node, then attach whichever list still
    has nodes left -- it is already sorted, no need to keep looping.

Target complexity: O(n + m) time, O(1) space
"""

import pathlib
import sys
from typing import Optional

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from common.structures import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr  = dummy
        while list1 and list2:
            if list1.val>list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next  = list1
                list1 = list1.next

            curr = curr.next

        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next
        pass


if __name__ == "__main__":
    # Run this file to check your answer against this problem's tests.
    import pytest

    _f = pathlib.Path(__file__).resolve()
    _test = _f.parents[1] / "tests" / _f.parent.name / ("test_" + _f.name)
    sys.exit(pytest.main(["-v", str(_test)]))
